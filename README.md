# Small Tale AI playbook

Reusable Hot Sheet guidance maintained by Small Tale Inc. Projects may consume all
or selected rules with Rulesync. Hot Sheet's built-in setup remains the default and
does not require Rulesync, a network connection, or this checkout.

| Selectable name | Section version | Purpose |
| --- | --- | --- |
| `hotsheet-ticket-driven-work` | 5 | Ticket lifecycle, follow-ups, evidence, and note hygiene |
| `hotsheet-testing-philosophy` | 5 | Risk tiers, behavioral coverage, and verification |
| `hotsheet-requirements-documentation` | 3 | Human requirements and concise AI summaries |
| `hotsheet-visual-qa` | 1 | Real rendered inspection and evidence |
| `hotsheet-workflow` | 64 | Hot Sheet CLI/MCP workflow, claims, phases, and confidence |

The maintained sources are the direct Markdown children of `rules/`. Rulesync
frontmatter is packaging; the body retains Hot Sheet's managed markers and version.
`rules-manifest.json` records body hashes and the HS2 migration baseline. The root
`AGENTS.md` and local Hot Sheet skills are preserved bootstrap instructions for
contributors, not additional selectable rule sources. `AGENTS.md` is the single source
of contributor instructions for every AI tool: `CLAUDE.md` contains only the Claude
Code import `@AGENTS.md`, and validation rejects any other content, so edit
`AGENTS.md` instead.

Rule names follow one convention. A rule owned by, or most closely associated with, one
tool or technology carries that owner as its prefix (`hotsheet-*`, `kerf-ui-*`,
`typescript-*`, `playwright-*`); a general rule has no prefix. The manifest's optional
`owner` field names that prefix and validation enforces it; the optional `tags` field
lists the languages and technologies a rule applies to, so a picker can filter by stack.
Rules migrated from Hot Sheet 2 keep their original section names and record
`baseline_paths` for the byte-for-byte comparison; rules that originate here use their
full name as the section name, start at section version 1, and have no baseline, so the
comparison skips them.

Hot Sheet 2 setup and refresh leave a plain `@AGENTS.md` line untouched from commit
`86b82e29` (HS2-HP1S4H) onward and keep the shared guidance in `AGENTS.md`. Older
builds, including a running server's automatic refresh, append a `hotsheet:claude`
block, which `check_rules.py` then rejects. Update Hot Sheet, restore `CLAUDE.md` to
the single import line, and preview with `hotsheet-cli setup --diagnose --project .`,
which is read-only.

HS2-specific engineering policy (Kerf, providers, build gates, product terminology),
plugin manifests, tool integrations, legacy migration bodies, and skill adapters stay
in Hot Sheet 2. They are implementation contracts rather than general rule prose.

## Ownership and changes

Propose changes here through a reviewed commit or pull request. Change the source
rule, increase its embedded section version, and update its manifest version and
SHA-256 body hash together. Preserve managed marker names. A prose change that affects
behavior requires downstream setup/refresh verification before release. Do not edit
generated snapshots in Hot Sheet 2 independently; update its pinned source revision.

Each release uses an annotated immutable `vMAJOR.MINOR.PATCH` tag. Never move or reuse
a published tag. Increase major for removed/renamed rules or incompatible markers,
minor for new rules or compatible behavior changes, and patch for corrections that
preserve behavior. Section versions increase independently whenever a body changes.
Consumers can pin a full commit SHA; a tag plus a committed Rulesync lockfile also
records the exact resolved commit. `main` is a development branch, not an immutable pin.

Before publishing, run the checks below and create the annotated release tag only on
the verified commit, then push that commit and tag. Release notes list changed rule
names, section versions, and downstream migration requirements.

## Validation

```sh
python3 -m pip install ruff==0.17.1  # once; matches the CI pin
ruff check .
python3 scripts/check_rules.py
python3 -m unittest discover -s tests -q
python3 scripts/check_rules.py --hotsheet ../hotsheet2
```

The last command reproduces the initial byte-for-byte migration comparison against
the paths and baseline commit recorded in the manifest. After a deliberate upstream
change, compare with a Hot Sheet checkout updated to that release instead.

Rulesync discovers these flat files through its `rules` source selection. Hot Sheet's
[validated consumer guide](https://github.com/Small-Tale/hotsheet2/blob/main/guidance/rulesync/README.md) provides all-rule and selected-rule examples,
an exact committed lock, update/outdated commands, local override behavior, and reviewed
migration/return paths. The tested Rulesync 38 Git transport uses `main` plus a committed
lock because its initial raw-SHA and annotated-tag resolution have limitations; frozen
installs retain the reviewed commit. Ordinary Hot Sheet setup remains offline and
does not install or invoke Rulesync.

Repository orientation: [codebase map](docs/CODEBASE-MAP.md).
Product scope and status: [requirements summary](docs/REQUIREMENTS-SUMMARY.md).
