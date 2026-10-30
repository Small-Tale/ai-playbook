# Requirements summary

| Requirement | Status | Evidence |
| --- | --- | --- |
| Independently selectable reusable Hot Sheet rules | Shipped | Five migrated `rules/hotsheet-*.md` sources and manifest validation |
| Preserve existing rule behavior and contributor guidance | Shipped | Exact body migration and preserved bootstrap files |
| `AGENTS.md` as the single contributor-instruction source; `CLAUDE.md` imports it | Shipped | `CLAUDE.md` is `@AGENTS.md`; `validate_bootstrap` and its tests; Hot Sheet 2 refresh keeps it from `86b82e29` |
| Playbook-originated rules: owner prefixes, `tags`, no Hot Sheet baseline | Shipped | `validate_entry`, `section_marker`, and their tests |
| Opinionated engineering and Kerf-UI rules, selectable per technology | Shipped | Eighteen playbook-originated `rules/*.md`; `kerf-ui-interaction-defaults` points at the Kerf house grammar shipped by `KF-Q4FMX5` (HS2-1NP0A5); exercised live on a bounded glassbox2 redesign under `v1.3.0` on 2026-10-23 (findings on HS2-4JCDWY); the three rule amendments it proposed landed the same day as `ui-composition` v3, `playwright-operations` v2, and `kerf-ui-catalog-demos` v2 (HS2-ZKRNDF, HS2-XFWPG6, HS2-BXWMBV), awaiting release under HS2-Z7KRZC |
| Git commit/push policy, release, gitgist, and deployment script rules | Shipped | `git-commit-and-push`, `release-scripts`, `gitgist-release-notes`, `deployment-scripts` (HS2-1E43RN) |
| One owning rule per topic in a generated `AGENTS.md` (testing, requirements docs, commit hygiene and slugs, quiet test output, rebuilt-instance realism, UI after-images) | Shipped here; partial downstream | `hotsheet-workflow` v65, `hotsheet-testing-philosophy` v7, `hotsheet-ticket-driven-work` v7, `git-commit-and-push` v2, `test-operations` v3 and the HS2-8S1KZG/HS2-R7G5KB policy test; unreleased, and Hot Sheet 2 and Rulesync consumers pick it up when they move their pin |
| Selectable skills, importable like rules through the Hot Sheet 2 guidance picker | Shipped | Layout, `skills-manifest.json`, `validate_skills`, and eight generic skills under HS2-XGWQZ9: the quality trio (`analyze-code-quality`, `check-code-hygiene`, `check-requirements-against-code`, released as `v1.5.0`) and the maintainer-chosen second set (`technical-changelog`, `ui-ux-review`, `security-review`, `feature-health`, `prep-major-release`, for the next minor release); picker import verified end to end with `hotsheet-cli guidance` |
| Versioned source provenance and immutable consumer pins | Shipped | Manifest baseline, body hashes, documented release policy |
| Offline Hot Sheet setup from pinned snapshots | Shipped in Hot Sheet 2 | HS2-R5V3AZ; `guidance/ai-playbook.lock.json` and exact-source drift checks |
| Rulesync opt-in workflow and writer ownership | Shipped in Hot Sheet 2 | HS2-QS38E1; [validated consumer guide](https://github.com/Small-Tale/hotsheet2/blob/main/guidance/rulesync/README.md), real CLI acceptance, and explicit ownership |

The [README](../README.md) is the source requirement and contributor contract.
