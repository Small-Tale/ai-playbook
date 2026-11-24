# Instruction payload budgets

HS2-JS9A83, measured 2026-11-24. Counts are UTF-8 bytes of managed rule bodies,
excluding Rulesync frontmatter. `instruction-budgets.json` sets per-rule ceilings
rounded up to 128-byte boundaries and their combined ceiling. CI runs
`python3 scripts/check_instruction_budget.py`; increases require a reviewed size
report and reason, not just regenerating limits to silence the check.

| Shared rule | v1.8.0 bytes | New bytes | Saved |
| --- | ---: | ---: | ---: |
| hotsheet-workflow v66 | 12,607 | 6,167 | 6,440 |
| hotsheet-ticket-driven-work v9 | 1,997 | 1,455 | 542 |
| hotsheet-testing-philosophy v8 | 3,577 | 2,520 | 1,057 |
| test-operations v4 | 1,648 | 1,224 | 424 |
| **Changed bodies** | **19,829** | **11,366** | **8,463** |

After the shared-rule change, all 23 selectable bodies totaled 52,227 bytes. This is a source
payload ceiling, not a promise that every rule plus project guidance fits a
32,768-byte instruction budget. Do not drop binding rules to make a number pass.

## Specialized rules (HS2-9JB8EE)

Measured against the same v1.8.0 source bodies; these eight files did not overlap
the first ticket's edits. Binding contracts stay in the selected rules. Kerf's
installed documents remain the authority for framework details, with explicit
read triggers; no consumer depends on an uninstalled local playbook reference.

| Rule / new version | Before bytes | New bytes | Saved |
| --- | ---: | ---: | ---: |
| release-scripts v2 | 4,139 | 2,675 | 1,464 |
| git-commit-and-push v3 | 3,787 | 2,209 | 1,578 |
| gitgist-release-notes v2 | 2,817 | 1,651 | 1,166 |
| deployment-scripts v2 | 2,766 | 1,727 | 1,039 |
| kerf-ui-usage v3 | 3,114 | 2,224 | 890 |
| kerf-ui-interaction-defaults v2 | 2,795 | 1,646 | 1,149 |
| ui-composition v4 | 3,116 | 2,129 | 987 |
| ui-evaluation v3 | 1,937 | 1,330 | 607 |
| **Changed bodies** | **24,471** | **15,591** | **8,880** |

All rule bodies now total **43,347** bytes (reviewed ceiling **44,672**).
Combined savings versus v1.8.0: **17,343** source bytes. Critical policy tests
preserve tag-only betas, partial-release recovery, credential-isolated publishing,
curated changelog history, deployment secrets/confirmation, named staging and
push policies, Kerf gates, and the bounded one-screen sign-off exception.

## Actual generation

Rulesync **38.0.0** ran in isolated temporary checkouts, with `features: ["rules"]`
and `targets: ["agentsmd"]`. No live consumer files or pins were changed.

| Consumer / source selection | Generated AGENTS.md bytes |
| --- | ---: |
| Hot Sheet 2 installed selection, pinned `02b66e656098ed5de7d2b042f37b862a8a057482` | 78,422 |
| Same 22 selected rules updated to ai-playbook v1.8.0 | 76,581 |
| Same selection with HS2-JS9A83 | 68,118 |
| Same selection with both tickets | 59,238 |
| Minimal consumer, five Hot Sheet default rules at v1.8.0 | 21,474 |
| Same minimal consumer with HS2-JS9A83 | 13,435 |

The installed Hot Sheet 2 reproduction is byte-identical to its real `AGENTS.md`.
It copies `.rulesync/rules/project-local.md` and the selected curated sources,
including the bundled sandbox-recovery section from the generated file. Keep the
same `.curated/` directory structure: moving sources changes generator ordering.
The baseline and changed runs replace only selected ai-playbook source files;
project-local guidance and bundled recovery stay byte-identical. The minimal
consumer selects workflow, ticket-driven-work, testing-philosophy,
requirements-documentation and visual-qa, with no local rule. Both runs use the
same generator/configuration. These are generated measurements, not an estimate
from subtracting source lengths.

Hot Sheet 2 still exceeds 32,768 bytes by **26,470** after both tickets.
The final generated reduction from its installed pin is **19,184 bytes (24.5%)**. Its existing
adoption ticket **HS2-FBHJ95** owns the consumer pin/snapshot update and local-size
coordination. Follow-up **HS2-2KPPWJ** tracks the next release and adoption;
both source tickets link it through typed follow-up relations.

## Reproduction and adoption

To measure a consumer, copy its Rulesync configuration, local rules and selected
source files to a temporary project. Generate its installed baseline first and
compare bytes with the real output. Replace the selected sources with the reviewed
playbook revision, generate again, and check that each marker occurs once and local
rules are unchanged. For the five-rule fixture, use the selection listed above.
Run the consumer's installed/pinned `rulesync generate` from the temporary project,
then `rulesync generate --check`. Measure the result read-only:

```sh
python3 scripts/check_instruction_budget.py --generated <temp-project>/AGENTS.md
```

Preserve managed marker names, manifest baseline paths/ref and consumer ownership.
The workflow’s final push-policy paragraph is a byte-exact setup replacement anchor;
it is intentionally unchanged and pinned by a source regression test.
Bump rule versions and hashes together. Move consumer pins and regenerate snapshots
through its normal reviewed guidance workflow; never overwrite bundled snapshots
or generated instruction files independently. `check_rules.py --hotsheet` compares
bodies to a checkout already updated to that revision, not the historical pin.
The installed `hotsheet` skill supplies queue command recipes; condensed root rules
retain lifecycle, required gates, completion, confidence and push-policy precedence.
No new local-only reference is required to obey a rule.

## Verification record

- Unit: body ceilings/total/selection failures and Unicode byte counts;
  lifecycle, phase, confidence, CI, notification and retry contract assertions,
  plus the specialized exception checks listed above.
- End to end: budget CLI measures a real file without mutation; real Rulesync
  generation covers the 22-rule Hot Sheet 2 selection and a five-rule consumer.
- Manual: inspect rule diffs against the prior bodies and the independent contract
  review. Rendered UI QA is inapplicable: this repository publishes instructions.
- Migration: existing marker identity, body hashes, version checks and comparison
  tests remain authoritative; consumer adoption is tracked separately.
