# Codebase map

- `rules/`: twenty-three independent Rulesync root rules (five migrated from Hot Sheet 2,
  eighteen playbook-originated), each wrapped in a Hot Sheet section marker.
- `rules-manifest.json`: rule names, versions, body hashes, optional `owner` (enforced name
  prefix) and `tags`, and original HS2 `baseline_paths`/ref for migrated rules only.
- `skills/`: tool-neutral skills, one `skills/<name>/SKILL.md` each (plus helper files when a
  skill needs them), in the layout Hot Sheet 2's guidance picker scans and installs into each
  tool's skill directory (HS2-XGWQZ9).
- `skills-manifest.json`: skill names, versions, `SKILL.md` hashes, `tags`, optional `owner`,
  and helper files with their hashes. Hot Sheet 2 does not read it; it is this repository's
  version record, like the section versions for rules.
- `scripts/check_rules.py`: standard-library rule, skill, and bootstrap validation, plus
  optional bundle comparison.
- `tests/test_rules.py`: valid, changed, unlisted, version, downstream drift,
  `CLAUDE.md` import, `.gitignore` machine-local coverage cases, and the one-owner-per-topic
  policy for overlapping sections (HS2-8S1KZG).
- `tests/test_skills.py`: import layout, changed and unlisted skills and helper files, version
  marker, frontmatter name, naming, owner prefix, and unsafe path cases.
- `AGENTS.md`, `.agents/skills/`, `.claude/skills/`: preserved contributor bootstrap;
  `AGENTS.md` is the one instruction source for all AI tools.
- `CLAUDE.md`: only `@AGENTS.md` (Claude Code import), enforced by `check_rules.py`.
- `.hotsheet2/settings.json`: the declared push policy (`push-per-ticket`), which Hot Sheet
  setup and refresh render into the push-policy block of `AGENTS.md` and the skill files;
  the store, local settings, worklist, HS1 `.hotsheet/` runtime directory, and generated
  tool configs are machine-local and ignored by `.gitignore` (HS2-W3RAMK).
- `ruff.toml`: lint rules for `scripts/` and `tests/`; `.github/workflows/check.yml` runs
  the pinned `ruff check .`, the validator, and the unit tests.
- `README.md`: ownership, release policy, consumption, and verification commands.

There is no application runtime or credential storage. Rule and skill inputs are plain
Markdown; publication is a verified git commit and immutable annotated release tag.
