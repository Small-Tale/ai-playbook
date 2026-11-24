---
root: true
targets: ["*"]
description: "How to judge a rendered UI and what passing tools do not prove"
---

<!-- hotsheet:begin section=ui-evaluation v=3 -->

## UI Evaluation

- Follow `hotsheet-visual-qa` for rebuilt real-app evidence, widths and transition. Add revealing long/two-line/full content, open rails/dialogs/menus, empty/loading states and both color schemes on the real backdrop. Use WebKit plus Chromium for sizing/overflow/sticky/focus-ring changes.
- Before attaching, zoom into ancestor clipping (including shadows/focus rings), icon/label/selection alignment against the highlight box even when hidden, double insets, separators, truncation/overlap/contrast, offscreen popovers and reference typography.
- Green tools prove only encoded checks, not contract compliance, hierarchy/rhythm/density/fit. Re-read composed parent/child contracts and pin real-parent browser assertions; DOM/style assertions cannot establish visual readability/alignment.
- Match named-reference typography, toolbar density, search, settings and demo before customization; differences are defects unless requested.
- Measure first-render performance against the user's baseline before shipping. No per-item subprocess loops; meet project local-interaction latency budgets.
- Prefer human review of annotated real-browser captures over prose; derive one ticket per annotation with its exact nouns.

<!-- hotsheet:end section=ui-evaluation -->
