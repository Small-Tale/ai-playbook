---
root: true
targets: ["*"]
description: "How to judge a rendered UI and what passing tools do not prove"
---

<!-- hotsheet:begin section=ui-evaluation v=1 -->

## UI Evaluation

- **Evidence comes from the real app**, not the demo route, on the rebuilt instance, with revealing content (long titles, two-line fields, full output). Capture wide, medium, and narrow widths and the wide-narrow-wide transition; open rails, dialogs, and menus; include empty and loading states; use WebKit as well as Chromium when sizing, overflow, sticky layers, or focus rings are involved; check both color schemes on the real backdrop.
- **Inspect before attaching**, zoomed to the edge in question: anything clipped by an ancestor (shadows and focus rings included); icons not on one x, labels not on one x, selection boxes not on one edge, measured against the highlight box even when hidden; double insets; stray separators; truncation; overlap; contrast; popovers off the viewport; font or size that differs from the reference app. A capture with a visible defect is never correctness evidence: fix, rerun, recapture.
- **Tool output is not judgment.** A green doctor, analyzer, or evaluator proves the checks it encodes, not component-contract compliance, hierarchy, rhythm, density, or fit. After composing a component, re-read its parent and children contract and pin it with a real-parent browser assertion. A passing DOM or computed-style assertion does not establish that content is readable, centered, unclipped, or aligned.
- **Compare to the reference.** Typography, toolbar density, search affordances, settings layout, and the demo route match the named reference app before any customization; a visible difference from the reference is a defect unless the ticket asked for it.
- **Measure performance** against the user's baseline (for example the CLI the product wraps) before shipping a first render; no per-item subprocess loops; keep local interactions within the project's latency budget.
- **Review loop.** Prefer annotated real-browser captures reviewed by the human over prose; derive one ticket per annotation carrying its exact nouns; the after capture matches the before's component, state, and viewport.

<!-- hotsheet:end section=ui-evaluation -->
