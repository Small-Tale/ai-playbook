# Small Tale AI playbook

Reusable Hot Sheet guidance maintained by Small Tale Inc. Projects may consume all
or selected rules with Rulesync. Hot Sheet's built-in setup remains the default and
does not require Rulesync, a network connection, or this checkout.

| Selectable name | Section version | Purpose |
| --- | --- | --- |
| `hotsheet-ticket-driven-work` | 6 | Ticket lifecycle, follow-ups, scope fidelity, evidence, and note hygiene |
| `hotsheet-testing-philosophy` | 6 | Risk tiers, behavioral coverage, policy tests, and verification |
| `hotsheet-requirements-documentation` | 4 | Human requirements, concise AI summaries, and the UI conventions doc |
| `hotsheet-visual-qa` | 2 | Real rendered inspection and evidence |
| `hotsheet-workflow` | 64 | Hot Sheet CLI/MCP workflow, claims, phases, and confidence |
| `project-bootstrap` | 1 | Day-one gate, skeleton, docs set, and reference parity |
| `conventions-as-code` | 2 | Policy tests (source, CSS, instruction files) and lint/doctor suppression governance |
| `test-operations` | 1 | Isolation, build-once, flake and quarantine policy, quiet output |
| `ui-composition` | 1 | Design-system-first construction process |
| `ui-evaluation` | 1 | Judging a rendered UI and what passing tools do not prove |
| `customer-data-hygiene` | 1 | No customer content in tickets, logs, fixtures, or telemetry |
| `web-client-organization` | 1 | Directory roles, component granularity, CSS ownership, size limits |
| `typescript-lint-and-format` | 1 | Prettier, strict type-aware ESLint, tsconfig defaults |
| `rust-lint-and-format` | 1 | Clippy, rustfmt, toolchain pin, test isolation |
| `playwright-operations` | 1 | Per-worker isolation, readiness waits, real geometry, flake criteria |
| `kerf-ui-usage` | 1 | Kerf guidance retrieval order, gates, Web Awesome policy, component gaps |
| `kerf-ui-upgrades` | 1 | Lockstep Kerf package upgrades |
| `kerf-ui-catalog-demos` | 1 | Catalog demos are the production components, exercised for real |
| `kerf-ui-interaction-defaults` | 1 | Pointer to Kerf's consumer house grammar; deviations only on record |
| `git-commit-and-push` | 1 | Commit shape, staging by path, history safety, declared push policy |
| `release-scripts` | 1 | One resumable release command that tags; CI publishes from the tag |
| `gitgist-release-notes` | 1 | gitgist for release notes and commit drafts, configured once |
| `deployment-scripts` | 1 | Phased, re-runnable deploy script with SHA-tagged artifacts |

Rules are opinionated by design; a project that adopts one deviates only at the project
level for a compelling or necessary reason, recorded in its own conventions document.
`kerf-ui-interaction-defaults` points at Kerf's own consumer house grammar
(`node_modules/@kerfjs/ui/docs/interaction-conventions.md`, from `@kerfjs/ui@5.0.0-beta.118`)
rather than restating it; Kerf owns that document and its design philosophy.

`git-commit-and-push` requires each adopting project to declare one of two named push
policies (`push-per-ticket` or `push-per-batch`) in its instructions. The Hot Sheet
workflow's own "pushing is up to this repository" sentence defers to that declaration.

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
`typescript-*`, `playwright-*`, `gitgist-*`); a general rule has no prefix. The manifest's optional
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
