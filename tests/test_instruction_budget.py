import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
spec = importlib.util.spec_from_file_location('budget', ROOT / 'scripts/check_instruction_budget.py')
budget = importlib.util.module_from_spec(spec)
spec.loader.exec_module(budget)


class InstructionBudgetTests(unittest.TestCase):
    def test_hs2_js9a83_reviewed_source_budgets(self):
        sizes = budget.measure(ROOT)
        limits = json.loads((ROOT / 'instruction-budgets.json').read_text())
        budget.check_budget(sizes, limits)

    def test_limits_include_every_rule_and_total(self):
        budget.check_budget({'one': 2}, {'rules': {'one': 2}, 'total': 2})
        for sizes, limits, message in (
            ({'one': 3}, {'rules': {'one': 2}, 'total': 4}, 'one:'),
            ({'one': 2}, {'rules': {'one': 2}, 'total': 1}, 'all rule bodies'),
            ({'one': 1}, {'rules': {}, 'total': 5}, 'every selectable rule'),
            ({}, {'rules': {'extra': 1}, 'total': 5}, 'every selectable rule'),
        ):
            with self.subTest(message=message), self.assertRaisesRegex(ValueError, message):
                budget.check_budget(sizes, limits)

    def test_utf8_bytes_exclude_frontmatter(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'rule.md').write_text(
                '---\nroot: true\ntargets: ["*"]\ndescription: "Example"\n---\n\né\n')
            (root / 'rules-manifest.json').write_text(json.dumps(
                {'rules': [{'name': 'example', 'path': 'rule.md'}]}))
            self.assertEqual(budget.measure(root), {'example': 3})

    def test_cli_reports_actual_generated_bytes_and_overage_read_only(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'AGENTS.md'
            original = ('é' * 16385).encode()
            path.write_bytes(original)
            result = subprocess.run(
                [sys.executable, str(ROOT / 'scripts/check_instruction_budget.py'),
                 '--generated', str(path)], capture_output=True, text=True, check=True)
            self.assertIn('Generated AGENTS.md: 32770 bytes; 2 over', result.stdout)
            self.assertEqual(path.read_bytes(), original)


if __name__ == '__main__':
    unittest.main()
