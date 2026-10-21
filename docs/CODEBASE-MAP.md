# Codebase map

- `rules/`: five independent Rulesync root rules, each with existing Hot Sheet markers.
- `rules-manifest.json`: rule names, versions, body hashes, and original HS2 paths/ref.
- `scripts/check_rules.py`: standard-library rule and bootstrap validation, plus optional
  bundle comparison.
- `tests/test_rules.py`: valid, changed, unlisted, version, downstream drift, and
  `CLAUDE.md` import cases.
- `AGENTS.md`, `.agents/skills/`, `.claude/skills/`: preserved contributor bootstrap;
  `AGENTS.md` is the one instruction source for all AI tools.
- `CLAUDE.md`: only `@AGENTS.md` (Claude Code import), enforced by `check_rules.py`.
- `ruff.toml`: lint rules for `scripts/` and `tests/`; `.github/workflows/check.yml` runs
  the pinned `ruff check .`, the validator, and the unit tests.
- `README.md`: ownership, release policy, consumption, and verification commands.

There is no application runtime or credential storage. Rule inputs are plain Markdown;
publication is a verified git commit and immutable annotated release tag.
