"""Validate selectable guidance and optionally compare a Hot Sheet bundle."""
import argparse
import hashlib
import json
from pathlib import Path
import re

SLUG = re.compile(r'[a-z][a-z0-9]*(-[a-z0-9]+)*')


def rule_body(text):
    match = re.match(r'\A---\nroot: true\ntargets: \["\*"\]\ndescription: "[^"\n]+"\n---\n\n', text)
    if not match:
        raise ValueError('expected a root Rulesync rule with wildcard targets')
    return text[match.end():]


def section_marker(name, version):
    """Return the managed marker that opens a rule body.

    Rules migrated from Hot Sheet keep their original section names: the `hotsheet-` prefix is
    dropped and the workflow rule uses the instructions-version marker. Rules that originate in
    this playbook use their full name as the section name.
    """
    if name == 'hotsheet-workflow':
        return f'<!-- hotsheet-instructions-version: {version} -->'
    return f'<!-- hotsheet:begin section={name.removeprefix("hotsheet-")} v={version} -->'


def validate_entry(rule):
    """Check a manifest entry's name, path, owner prefix, and tags."""
    name = rule['name']
    if not SLUG.fullmatch(name):
        raise ValueError(f'invalid rule name: {name}')
    if rule['path'] != f'rules/{name}.md':
        raise ValueError(f'invalid rule path: {rule["path"]}')
    owner = rule.get('owner')
    if owner is not None and (not SLUG.fullmatch(owner) or not name.startswith(f'{owner}-')):
        raise ValueError(f'rule name must start with its owner prefix: {name}')
    for tag in rule.get('tags', []):
        if not SLUG.fullmatch(tag):
            raise ValueError(f'invalid tag {tag!r}: {name}')


def validate(root, hotsheet=None):
    manifest = json.loads((root / 'rules-manifest.json').read_text())
    if manifest['schema_version'] != 1:
        raise ValueError('unsupported manifest version')
    expected = set()
    for rule in manifest['rules']:
        validate_entry(rule)
        path = rule['path']
        if path in expected:
            raise ValueError(f'duplicate rule: {path}')
        expected.add(path)
        body = rule_body((root / path).read_text())
        if hashlib.sha256(body.encode()).hexdigest() != rule['sha256']:
            raise ValueError(f'body hash mismatch: {path}; update its version and manifest')
        if not body.startswith(section_marker(rule['name'], rule['version']) + '\n'):
            raise ValueError(f'version mismatch: {path}')
        if hotsheet:
            for bundled in rule.get('baseline_paths', []):
                if (hotsheet / bundled).read_text() != body:
                    raise ValueError(f'baseline differs: {bundled}')
    actual = {str(path.relative_to(root)) for path in (root / 'rules').glob('*.md')}
    if actual != expected:
        raise ValueError('manifest does not cover every selectable rule')
    return len(expected)


def validate_bootstrap(root):
    if (root / 'CLAUDE.md').read_text() != '@AGENTS.md\n':
        raise ValueError('CLAUDE.md must only import AGENTS.md; edit AGENTS.md instead')
    if not (root / 'AGENTS.md').is_file():
        raise ValueError('CLAUDE.md imports a missing AGENTS.md')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--hotsheet', type=Path, help='compare bodies with a Hot Sheet checkout')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    validate_bootstrap(root)
    print(f'Validated {validate(root, args.hotsheet)} selectable rules')
