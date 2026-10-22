# Requirements summary

| Requirement | Status | Evidence |
| --- | --- | --- |
| Independently selectable reusable Hot Sheet rules | Shipped | Five migrated `rules/hotsheet-*.md` sources and manifest validation |
| Preserve existing rule behavior and contributor guidance | Shipped | Exact body migration and preserved bootstrap files |
| `AGENTS.md` as the single contributor-instruction source; `CLAUDE.md` imports it | Shipped | `CLAUDE.md` is `@AGENTS.md`; `validate_bootstrap` and its tests; Hot Sheet 2 refresh keeps it from `86b82e29` |
| Playbook-originated rules: owner prefixes, `tags`, no Hot Sheet baseline | Shipped | `validate_entry`, `section_marker`, and their tests |
| Opinionated engineering and Kerf-UI rules, selectable per technology | Shipped | Eighteen playbook-originated `rules/*.md`; `kerf-ui-interaction-defaults` points at the Kerf house grammar shipped by `KF-Q4FMX5` (HS2-1NP0A5) |
| Git commit/push policy, release, gitgist, and deployment script rules | Shipped | `git-commit-and-push`, `release-scripts`, `gitgist-release-notes`, `deployment-scripts` (HS2-1E43RN) |
| Versioned source provenance and immutable consumer pins | Shipped | Manifest baseline, body hashes, documented release policy |
| Offline Hot Sheet setup from pinned snapshots | Shipped in Hot Sheet 2 | HS2-R5V3AZ; `guidance/ai-playbook.lock.json` and exact-source drift checks |
| Rulesync opt-in workflow and writer ownership | Shipped in Hot Sheet 2 | HS2-QS38E1; [validated consumer guide](https://github.com/Small-Tale/hotsheet2/blob/main/guidance/rulesync/README.md), real CLI acceptance, and explicit ownership |

The [README](../README.md) is the source requirement and contributor contract.
