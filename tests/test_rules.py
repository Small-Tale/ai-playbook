import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('check_rules', ROOT / 'scripts/check_rules.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class RulesTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        shutil.copytree(ROOT / 'rules', self.root / 'rules')
        shutil.copy(ROOT / 'rules-manifest.json', self.root)

    def test_published_rules_are_valid(self):
        self.assertEqual(checker.validate(self.root), 5)

    def test_unreviewed_body_change_is_rejected(self):
        path = self.root / 'rules/hotsheet-visual-qa.md'
        path.write_text(path.read_text() + '\nChanged behavior.\n')
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            checker.validate(self.root)

    def test_unlisted_rule_is_rejected(self):
        shutil.copy(self.root / 'rules/hotsheet-visual-qa.md', self.root / 'rules/extra.md')
        with self.assertRaisesRegex(ValueError, 'every selectable rule'):
            checker.validate(self.root)

    def test_version_mismatch_is_rejected(self):
        path = self.root / 'rules-manifest.json'
        manifest = json.loads(path.read_text())
        manifest['rules'][0]['version'] += 1
        path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, 'version mismatch'):
            checker.validate(self.root)

    def test_baseline_comparison_checks_each_destination(self):
        bundle = self.root / 'bundle'
        manifest = json.loads((self.root / 'rules-manifest.json').read_text())
        for rule in manifest['rules']:
            for relative in rule['baseline_paths']:
                path = bundle / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(checker.rule_body((self.root / rule['path']).read_text()))
        self.assertEqual(checker.validate(self.root, bundle), 5)
        (bundle / 'plugins/codex/instructions.md').write_text('drift')
        with self.assertRaisesRegex(ValueError, 'baseline differs'):
            checker.validate(self.root, bundle)


if __name__ == '__main__':
    unittest.main()
