---
root: true
targets: ["*"]
description: "Encode corrected conventions as tests and govern lint and doctor suppressions"
---

<!-- hotsheet:begin section=conventions-as-code v=1 -->

## Conventions as Code

Instruction-file prose does not hold on its own. When a reviewer corrects a convention, encode it in the same change as a source-level test or a lint rule, and name the test or rule with the ticket slug so the reason stays discoverable.

- **Policy tests.** Keep one structural test file per package that greps or parses source to pin conventions: no emoji or Unicode glyph icons; no cross-component CSS selectors; one exported component per file; every export has a demo; every signal has a reset; no handwritten boundary types outside the contract module; no machine-local paths; no invisible Unicode. Add a case for each new correction; never delete one without the ticket that retires the convention.
- **Suppressions.** A lint disable carries a reason and a ticket slug on the same line, and a policy test caps disables per file. Unused disables fail lint. Formatter-ignore comments are banned.
- **Doctor and profile exceptions.** UI library doctor exceptions are exact `{id, rule, target, rationale}` entries, each naming the upstream ticket; a test pins their count and asserts each rationale's target still exists. The count only decreases. No broad suppression or raised budget substitutes for a fix; a missing library capability is an upstream ticket, not an exception.
- **Generated artifacts** (catalogs, composition manifests, API contracts, lockfiles) are checked in and byte-checked in CI; regenerate them in the same change that changes their source.

<!-- hotsheet:end section=conventions-as-code -->
