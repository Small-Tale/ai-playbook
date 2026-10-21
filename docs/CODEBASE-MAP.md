# Codebase map

- `rules/`: five independent Rulesync root rules, each with existing Hot Sheet markers.
- `rules-manifest.json`: rule names, versions, body hashes, and original HS2 paths/ref.
- `scripts/check_rules.py`: standard-library validation and optional bundle comparison.
- `tests/test_rules.py`: valid, changed, unlisted, version, and downstream drift cases.
- `AGENTS.md`, `CLAUDE.md`, `.agents/skills/`, `.claude/skills/`: preserved contributor bootstrap.
- `README.md`: ownership, release policy, consumption, and verification commands.

There is no application runtime or credential storage. Rule inputs are plain Markdown;
publication is a verified git commit and immutable annotated release tag.
