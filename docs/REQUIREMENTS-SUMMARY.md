# Requirements summary

| Requirement | Status | Evidence |
| --- | --- | --- |
| Independently selectable reusable Hot Sheet rules | Shipped | Five flat `rules/*.md` sources and manifest validation |
| Preserve existing rule behavior and contributor guidance | Shipped | Exact body migration and preserved bootstrap files |
| `AGENTS.md` as the single contributor-instruction source; `CLAUDE.md` imports it | Shipped | `CLAUDE.md` is `@AGENTS.md`; `validate_bootstrap` and its tests |
| Versioned source provenance and immutable consumer pins | Shipped | Manifest baseline, body hashes, documented release policy |
| Offline Hot Sheet setup from pinned snapshots | Downstream work | HS2-R5V3AZ in Hot Sheet 2 |
| Rulesync opt-in workflow and writer ownership | Downstream work | HS2-QS38E1 in Hot Sheet 2 |

The [README](../README.md) is the source requirement and contributor contract.
