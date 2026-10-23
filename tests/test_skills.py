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
PUBLISHED = len(json.loads((ROOT / 'skills-manifest.json').read_text())['skills'])


class SkillsTests(unittest.TestCase):
    """HS2-XGWQZ9: skills ship in the layout Hot Sheet 2's guidance picker imports."""

    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        shutil.copytree(ROOT / 'skills', self.root / 'skills')
        shutil.copy(ROOT / 'skills-manifest.json', self.root)

    def manifest(self):
        return json.loads((self.root / 'skills-manifest.json').read_text())

    def write_manifest(self, manifest):
        (self.root / 'skills-manifest.json').write_text(json.dumps(manifest))

    def add_skill(self, name, version=1, extra=None, **entry):
        """Write a skill and list it in the manifest; `extra` maps helper paths to bytes."""
        directory = self.root / 'skills' / name
        directory.mkdir(parents=True)
        text = (f'---\nname: {name}\ndescription: {name}\n---\n\n'
                f'{checker.skill_marker(name, version)}\n\nBody.\n')
        (directory / 'SKILL.md').write_text(text)
        files = []
        for path, data in (extra or {}).items():
            target = directory / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            files.append({'path': path, 'sha256': hashlib.sha256(data).hexdigest()})
        manifest = self.manifest()
        record = {'name': name, 'path': f'skills/{name}/SKILL.md', 'version': version,
                  'sha256': hashlib.sha256(text.encode()).hexdigest(), **entry}
        if files:
            record['files'] = files
        manifest['skills'].append(record)
        self.write_manifest(manifest)

    def test_published_skills_are_valid(self):
        self.assertEqual(checker.validate_skills(self.root), PUBLISHED)

    def test_published_skills_follow_the_import_layout(self):
        """Every published skill is `skills/<slug>/SKILL.md`, the layout Hot Sheet 2 scans."""
        for directory in (ROOT / 'skills').iterdir():
            with self.subTest(skill=directory.name):
                self.assertRegex(directory.name, checker.SLUG)
                self.assertTrue((directory / 'SKILL.md').is_file())

    def test_changed_skill_is_rejected(self):
        path = self.root / 'skills/analyze-code-quality/SKILL.md'
        path.write_text(path.read_text() + '\nChanged behavior.\n')
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            checker.validate_skills(self.root)

    def test_unlisted_skill_directory_is_rejected(self):
        shutil.copytree(self.root / 'skills/analyze-code-quality', self.root / 'skills/extra')
        with self.assertRaisesRegex(ValueError, 'every skill directory'):
            checker.validate_skills(self.root)

    def test_listed_but_missing_skill_is_rejected(self):
        shutil.rmtree(self.root / 'skills/check-code-hygiene')
        with self.assertRaises(FileNotFoundError):
            checker.validate_skills(self.root)

    def test_version_marker_mismatch_is_rejected(self):
        manifest = self.manifest()
        manifest['skills'][0]['version'] += 1
        self.write_manifest(manifest)
        with self.assertRaisesRegex(ValueError, 'version mismatch'):
            checker.validate_skills(self.root)

    def test_frontmatter_name_must_match_directory(self):
        self.add_skill('sample-skill')
        path = self.root / 'skills/sample-skill/SKILL.md'
        text = path.read_text().replace('name: sample-skill', 'name: other', 1)
        path.write_text(text)
        manifest = self.manifest()
        manifest['skills'][-1]['sha256'] = hashlib.sha256(text.encode()).hexdigest()
        self.write_manifest(manifest)
        with self.assertRaisesRegex(ValueError, 'match its directory'):
            checker.validate_skills(self.root)

    def test_missing_frontmatter_is_rejected(self):
        self.add_skill('sample-skill')
        path = self.root / 'skills/sample-skill/SKILL.md'
        text = checker.skill_marker('sample-skill', 1) + '\n\nBody.\n'
        path.write_text(text)
        manifest = self.manifest()
        manifest['skills'][-1]['sha256'] = hashlib.sha256(text.encode()).hexdigest()
        self.write_manifest(manifest)
        with self.assertRaisesRegex(ValueError, 'frontmatter'):
            checker.validate_skills(self.root)

    def test_malformed_names_are_rejected(self):
        for name in ('Sample-Skill', 'typescript-', '-general', 'a--b', 'rust_skill'):
            with self.subTest(name=name):
                shutil.copy(ROOT / 'skills-manifest.json', self.root)
                self.add_skill(name)
                with self.assertRaisesRegex(ValueError, 'invalid skill name'):
                    checker.validate_skills(self.root)

    def test_owner_prefix_mismatch_is_rejected(self):
        self.add_skill('ui-sample', owner='kerf-ui')
        with self.assertRaisesRegex(ValueError, 'owner prefix'):
            checker.validate_skills(self.root)

    def test_owner_prefixed_skill_is_accepted(self):
        self.add_skill('kerf-ui-sample', owner='kerf-ui', tags=['kerf-ui'])
        self.assertEqual(checker.validate_skills(self.root), PUBLISHED + 1)

    def test_invalid_tag_is_rejected(self):
        self.add_skill('sample-skill', tags=['Code Quality'])
        with self.assertRaisesRegex(ValueError, 'invalid tag'):
            checker.validate_skills(self.root)

    def test_helper_files_are_listed_and_hashed(self):
        self.add_skill('with-helper', extra={'scripts/helper.sh': b'#!/bin/sh\n'})
        self.assertEqual(checker.validate_skills(self.root), PUBLISHED + 1)
        helper = self.root / 'skills/with-helper/scripts/helper.sh'
        helper.write_bytes(b'#!/bin/sh\necho changed\n')
        with self.assertRaisesRegex(ValueError, 'file hash mismatch'):
            checker.validate_skills(self.root)

    def test_unlisted_helper_file_is_rejected(self):
        self.add_skill('with-helper')
        (self.root / 'skills/with-helper/notes.md').write_text('stray\n')
        with self.assertRaisesRegex(ValueError, 'not listed'):
            checker.validate_skills(self.root)

    def test_unsafe_helper_path_is_rejected(self):
        for path in ('../escape.sh', 'scripts//helper.sh', './helper.sh', 'SKILL.md'):
            with self.subTest(path=path):
                shutil.copy(ROOT / 'skills-manifest.json', self.root)
                shutil.rmtree(self.root / 'skills/with-helper', ignore_errors=True)
                self.add_skill('with-helper')
                manifest = self.manifest()
                manifest['skills'][-1]['files'] = [{'path': path, 'sha256': '0' * 64}]
                self.write_manifest(manifest)
                with self.assertRaisesRegex(ValueError, 'unsafe or duplicate skill file path'):
                    checker.validate_skills(self.root)

    def test_duplicate_skill_is_rejected(self):
        manifest = self.manifest()
        manifest['skills'].append(manifest['skills'][0])
        self.write_manifest(manifest)
        with self.assertRaisesRegex(ValueError, 'duplicate skill'):
            checker.validate_skills(self.root)

    def test_unsupported_manifest_version_is_rejected(self):
        manifest = self.manifest()
        manifest['schema_version'] = 2
        self.write_manifest(manifest)
        with self.assertRaisesRegex(ValueError, 'unsupported skills manifest version'):
            checker.validate_skills(self.root)

    def test_skill_marker_format(self):
        self.assertEqual(checker.skill_marker('analyze-code-quality', 3),
                         '<!-- ai-playbook:skill name=analyze-code-quality v=3 -->')


if __name__ == '__main__':
    unittest.main()
