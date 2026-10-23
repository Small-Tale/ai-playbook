"""Validate selectable guidance (rules and skills) and optionally compare a Hot Sheet bundle."""
import argparse
import hashlib
import json
from pathlib import Path
import re

SLUG = re.compile(r'[a-z][a-z0-9]*(-[a-z0-9]+)*')
SKILL_FRONTMATTER = re.compile(
    r'\A---\nname: ([^\n]+)\ndescription: [^\n]+\n(?:allowed-tools: [^\n]+\n)?---\n\n')


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


def skill_marker(name, version):
    """Return the version marker that opens a skill body.

    Skills are copied verbatim into each tool's skill directory, so the marker is informational:
    it lets a reader of an installed copy see which published version it came from.
    """
    return f'<!-- ai-playbook:skill name={name} v={version} -->'


def validate_naming(kind, record):
    """Check a manifest record's name, owner prefix, and tags; shared by rules and skills."""
    name = record['name']
    if not SLUG.fullmatch(name):
        raise ValueError(f'invalid {kind} name: {name}')
    owner = record.get('owner')
    if owner is not None and (not SLUG.fullmatch(owner) or not name.startswith(f'{owner}-')):
        raise ValueError(f'{kind} name must start with its owner prefix: {name}')
    for tag in record.get('tags', []):
        if not SLUG.fullmatch(tag):
            raise ValueError(f'invalid tag {tag!r}: {name}')


def validate_entry(rule):
    """Check a manifest entry's name, path, owner prefix, and tags."""
    validate_naming('rule', rule)
    if rule['path'] != f'rules/{rule["name"]}.md':
        raise ValueError(f'invalid rule path: {rule["path"]}')


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


def validate_skill(root, skill):
    """Check one skill: Hot Sheet 2's import layout, frontmatter, version marker, and every file's hash."""
    name = skill['name']
    validate_naming('skill', skill)
    if skill['path'] != f'skills/{name}/SKILL.md':
        raise ValueError(f'invalid skill path: {skill["path"]}')
    directory = root / 'skills' / name
    text = (directory / 'SKILL.md').read_text()
    match = SKILL_FRONTMATTER.match(text)
    if not match:
        raise ValueError(f'expected skill frontmatter with name, description, optional allowed-tools: {name}')
    if match.group(1).strip() != name:
        raise ValueError(f'skill frontmatter name must match its directory: {name}')
    if not text[match.end():].startswith(skill_marker(name, skill['version']) + '\n'):
        raise ValueError(f'skill version mismatch: {name}')
    listed = {'SKILL.md': skill['sha256']}
    for extra in skill.get('files', []):
        parts = extra['path'].split('/')
        if extra['path'] in listed or any(part in ('', '.', '..') for part in parts):
            raise ValueError(f'unsafe or duplicate skill file path: {name}/{extra["path"]}')
        listed[extra['path']] = extra['sha256']
    actual = {str(path.relative_to(directory)): hashlib.sha256(path.read_bytes()).hexdigest()
              for path in directory.rglob('*') if path.is_file()}
    if set(actual) != set(listed):
        raise ValueError(f'skill files not listed in the manifest, or listed but missing: {name}')
    for path, digest in listed.items():
        if actual[path] != digest:
            raise ValueError(f'skill file hash mismatch: {name}/{path}; update its version and manifest')


def validate_skills(root):
    manifest = json.loads((root / 'skills-manifest.json').read_text())
    if manifest['schema_version'] != 1:
        raise ValueError('unsupported skills manifest version')
    expected = set()
    for skill in manifest['skills']:
        validate_skill(root, skill)
        if skill['name'] in expected:
            raise ValueError(f'duplicate skill: {skill["name"]}')
        expected.add(skill['name'])
    actual = {path.name for path in (root / 'skills').iterdir() if path.is_dir()}
    if actual != expected:
        raise ValueError('skills manifest does not cover every skill directory')
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
    print(f'Validated {validate(root, args.hotsheet)} selectable rules and {validate_skills(root)} skills')
