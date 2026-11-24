"""Measure UTF-8 rule bodies and generated instructions; enforce reviewed source budgets."""
import argparse
import json
from pathlib import Path

from check_rules import rule_body


def measure(root):
    """Exclude Rulesync frontmatter: consumers install the managed body only."""
    manifest = json.loads((root / 'rules-manifest.json').read_text())
    return {rule['name']: len(rule_body((root / rule['path']).read_text()).encode('utf-8'))
            for rule in manifest['rules']}


def check_budget(sizes, limits):
    """Require a ceiling for every selectable rule as well as the combined payload."""
    if set(sizes) != set(limits['rules']):
        raise ValueError('instruction budgets must cover every selectable rule')
    for name, size in sizes.items():
        if size > limits['rules'][name]:
            raise ValueError(f'{name}: {size} bytes exceeds budget {limits["rules"][name]}')
    total = sum(sizes.values())
    if total > limits['total']:
        raise ValueError(f'all rule bodies: {total} bytes exceeds budget {limits["total"]}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--generated', type=Path, action='append', default=[],
                        help='measure an actual generated AGENTS.md (repeatable; read-only)')
    args = parser.parse_args()
    sizes = measure(args.root)
    limits = json.loads((args.root / 'instruction-budgets.json').read_text())
    check_budget(sizes, limits)
    for name, size in sizes.items():
        print(f'{name}: {size} bytes (budget {limits["rules"][name]})')
    print(f'All rule bodies: {sum(sizes.values())} bytes (budget {limits["total"]})')
    for path in args.generated:
        size = len(path.read_bytes())
        print(f'Generated {path.name}: {size} bytes; '
              f'{max(0, size - 32768)} over a 32768-byte instruction budget')
    print('Source budgets do not guarantee consumer fit; measure generated files and local guidance.')


if __name__ == '__main__':
    main()
