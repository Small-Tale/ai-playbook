import hashlib
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
PUBLISHED = len(json.loads((ROOT / 'rules-manifest.json').read_text())['rules'])


class RulesTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        shutil.copytree(ROOT / 'rules', self.root / 'rules')
        shutil.copy(ROOT / 'rules-manifest.json', self.root)

    def add_rule(self, name, **entry):
        """Write a playbook-originated rule and list it in the manifest."""
        body = (f'<!-- hotsheet:begin section={name} v=1 -->\n\n## Heading\n\nBody.\n\n'
                f'<!-- hotsheet:end section={name} -->\n')
        (self.root / f'rules/{name}.md').write_text(
            f'---\nroot: true\ntargets: ["*"]\ndescription: "{name}"\n---\n\n{body}')
        path = self.root / 'rules-manifest.json'
        manifest = json.loads(path.read_text())
        manifest['rules'].append({'name': name, 'path': f'rules/{name}.md', 'version': 1,
                                  'sha256': hashlib.sha256(body.encode()).hexdigest(), **entry})
        path.write_text(json.dumps(manifest))

    def write_bundle(self):
        bundle = self.root / 'bundle'
        manifest = json.loads((self.root / 'rules-manifest.json').read_text())
        for rule in manifest['rules']:
            for relative in rule.get('baseline_paths', []):
                path = bundle / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(checker.rule_body((self.root / rule['path']).read_text()))
        return bundle

    def test_published_rules_are_valid(self):
        self.assertEqual(checker.validate(self.root), PUBLISHED)

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
        bundle = self.write_bundle()
        self.assertEqual(checker.validate(self.root, bundle), PUBLISHED)
        (bundle / 'plugins/codex/instructions.md').write_text('drift')
        with self.assertRaisesRegex(ValueError, 'baseline differs'):
            checker.validate(self.root, bundle)

    def test_playbook_rule_without_prefix_is_accepted(self):
        self.add_rule('sample-general-rule', tags=['general'])
        self.assertEqual(checker.validate(self.root), PUBLISHED + 1)

    def test_owner_prefixed_rule_is_accepted(self):
        self.add_rule('kerf-ui-sample', owner='kerf-ui', tags=['kerf-ui', 'typescript'])
        self.assertEqual(checker.validate(self.root), PUBLISHED + 1)

    def test_owner_prefix_mismatch_is_rejected(self):
        self.add_rule('ui-usage', owner='kerf-ui')
        with self.assertRaisesRegex(ValueError, 'owner prefix'):
            checker.validate(self.root)

    def test_malformed_names_are_rejected(self):
        for name in ('Sample-Rule', 'typescript-', '-general', 'a--b', 'rust_lint'):
            with self.subTest(name=name):
                shutil.copy(ROOT / 'rules-manifest.json', self.root)
                self.add_rule(name)
                with self.assertRaisesRegex(ValueError, 'invalid rule name'):
                    checker.validate(self.root)

    def test_invalid_tag_is_rejected(self):
        self.add_rule('sample-tagged-rule', tags=['Customer Data'])
        with self.assertRaisesRegex(ValueError, 'invalid tag'):
            checker.validate(self.root)

    def test_baseline_comparison_skips_playbook_rules(self):
        self.add_rule('sample-no-baseline')
        self.assertEqual(checker.validate(self.root, self.write_bundle()), PUBLISHED + 1)

    def test_section_markers_follow_rule_origin(self):
        self.assertEqual(checker.section_marker('hotsheet-visual-qa', 1),
                         '<!-- hotsheet:begin section=visual-qa v=1 -->')
        self.assertEqual(checker.section_marker('hotsheet-workflow', 64),
                         '<!-- hotsheet-instructions-version: 64 -->')
        self.assertEqual(checker.section_marker('kerf-ui-usage', 1),
                         '<!-- hotsheet:begin section=kerf-ui-usage v=1 -->')

    def test_claude_imports_agents(self):
        checker.validate_bootstrap(ROOT)
        (self.root / 'AGENTS.md').write_text('Shared instructions.\n')
        (self.root / 'CLAUDE.md').write_text('@AGENTS.md\n')
        checker.validate_bootstrap(self.root)

    def test_inlined_claude_instructions_are_rejected(self):
        (self.root / 'AGENTS.md').write_text('Shared instructions.\n')
        (self.root / 'CLAUDE.md').write_text('@AGENTS.md\n\nClaude-only drift.\n')
        with self.assertRaisesRegex(ValueError, 'only import AGENTS.md'):
            checker.validate_bootstrap(self.root)

    def test_missing_import_target_is_rejected(self):
        (self.root / 'CLAUDE.md').write_text('@AGENTS.md\n')
        with self.assertRaisesRegex(ValueError, 'missing AGENTS.md'):
            checker.validate_bootstrap(self.root)

    def test_machine_local_hotsheet_files_are_ignored(self):
        """HS2-W3RAMK: .gitignore, not a clone's .git/info/exclude, hides setup output."""
        patterns = [line.strip() for line in (ROOT / '.gitignore').read_text().splitlines()
                    if line.strip() and not line.startswith('#')]
        for pattern in ('/.hotsheet2/*', '!/.hotsheet2/settings.json', '/.hotsheet/',
                        '/.mcp.json', '/.claude/settings.local.json', '/.codex/config.toml',
                        '/.codex/hooks.json', '/.agents/mcp_config.json', '/opencode.json'):
            self.assertIn(pattern, patterns)

    def test_python_bytecode_caches_are_ignored(self):
        """HS2-9NE1WE: the unit-test gate must leave the clone clean."""
        self.assertIn('__pycache__/', (ROOT / '.gitignore').read_text().splitlines())


if __name__ == '__main__':
    unittest.main()
