---
root: true
targets: ["*"]
description: "Follow the Kerf UI consumer house grammar for chrome, actions, lists, input, latency, responsive layout, and roles; deviate only on record"
---

<!-- hotsheet:begin section=kerf-ui-interaction-defaults v=1 -->

## Kerf UI Interaction Defaults

Kerf owns the interaction conventions of every application built on `@kerfjs/ui`. They are the consumer house grammar at `node_modules/@kerfjs/ui/docs/interaction-conventions.md` (shipped from `@kerfjs/ui@5.0.0-beta.118`; Kerf's `llms.txt` and `ai/skill.md` link it; in a workspace the path is relative to the package that installs `@kerfjs/ui`). They are defaults, not suggestions: a composition that departs from them without a recorded deviation is a defect, whoever asked for it.

- **Read it before composing.** After the retrieval order in `kerf-ui-usage`, open the installed document before planning a screen, toolbar, list, dialog, or editor. It governs chrome ownership and hierarchy; actions, feedback, and dialogs; lists and selection; text editing, autosave, and continuity; latency; responsive layout, platform, and roles; and the review of a real composition. Name the sections that apply in the ticket's preliminary note and carry their nouns into the region plan and test names.
- **Point, never restate.** The project's UI conventions document links the installed path and records only the project's deviations and project-specific decisions. Local copies of these conventions (a design-philosophy section, a hard-rejection list, a lesson table) are retired in favor of the pointer, because copies drift and a correction made in one project never reaches the others.
- **Deviate on record.** A project departs from a default only for a compelling product reason, decided at the project level and written in its UI conventions document as the section departed from, the reason, and the ticket slug. One screen's screenshot, a maintainer's request for a specific visual, an AI note, or an existing screen that already differs is not a deviation; the first three are tickets and the last is a defect.
- **Grow it upstream.** When a question the grammar does not answer recurs, or a default proves wrong in use, file a `KF-*` ticket in the Kerf store that proposes the sentence to add or change, reference it from the application ticket, record the interim local decision beside that slug, and remove the local decision when the Kerf release ships it.
- **Pin corrections.** When a reviewer corrects a violation, pin it as `conventions-as-code` prescribes: a source-level policy test or lint rule, named with the ticket slug and the house-grammar section, in the same change as the fix.
- **Re-read on upgrade.** Each Kerf upgrade (`kerf-ui-upgrades`) diffs the installed document against the previous version. A new or changed default yields one ticket per surface that no longer complies, never a silent local exception.

<!-- hotsheet:end section=kerf-ui-interaction-defaults -->
