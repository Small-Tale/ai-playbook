"""Validate selectable guidance and optionally compare a Hot Sheet bundle."""
import argparse
import hashlib
import json
from pathlib import Path
import re


def rule_body(text):
    match = re.match(r'\A---\nroot: true\ntargets: \["\*"\]\ndescription: "[^"\n]+"\n---\n\n', text)
    if not match:
        raise ValueError('expected a root Rulesync rule with wildcard targets')
    return text[match.end():]


def validate(root, hotsheet=None):
    manifest = json.loads((root / 'rules-manifest.json').read_text())
    if manifest['schema_version'] != 1:
        raise ValueError('unsupported manifest version')
    expected = set()
    for rule in manifest['rules']:
        path = rule['path']
        if path != f"rules/{rule['name']}.md" or not re.fullmatch(r'hotsheet-[a-z-]+', rule['name']):
            raise ValueError(f'invalid rule path: {path}')
        if path in expected:
            raise ValueError(f'duplicate rule: {path}')
        expected.add(path)
        body = rule_body((root / path).read_text())
        if hashlib.sha256(body.encode()).hexdigest() != rule['sha256']:
            raise ValueError(f'body hash mismatch: {path}; update its version and manifest')
        section = rule['name'].removeprefix('hotsheet-')
        marker = (f'<!-- hotsheet-instructions-version: {rule["version"]} -->' if section == 'workflow'
                  else f'<!-- hotsheet:begin section={section} v={rule["version"]} -->')
        if not body.startswith(marker + '\n'):
            raise ValueError(f'version mismatch: {path}')
        if hotsheet:
            for bundled in rule['baseline_paths']:
                if (hotsheet / bundled).read_text() != body:
                    raise ValueError(f'baseline differs: {bundled}')
    actual = {str(path.relative_to(root)) for path in (root / 'rules').glob('*.md')}
    if actual != expected:
        raise ValueError('manifest does not cover every selectable rule')
    return len(expected)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--hotsheet', type=Path, help='compare bodies with a Hot Sheet checkout')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    print(f'Validated {validate(root, args.hotsheet)} selectable rules')
