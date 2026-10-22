---
root: true
targets: ["*"]
description: "Kerf UI catalog demos are the production components, exercised for real"
---

<!-- hotsheet:begin section=kerf-ui-catalog-demos v=1 -->

## Kerf UI Catalog Demos

The `/ux-demo` route mounts Kerf's `Catalog` with production components. It is absent from production builds and is the first place to look before composing a screen.

- Every exported component has its own demo file that renders the production component with deterministic fixtures (no API calls), exposes every variant and state through settings with a reset, opens dialogs from a visible trigger and lets them dismiss, and runs live behavior (timers, drag, validation) for real.
- Demos reuse production CSS and wiring and never own interaction behavior; a demo that reimplements a fake version of a screen is misinformation and is removed.
- An application-views group mounts the real root for every routed state so the whole app is reviewable without setup.
- A structural test enforces export-level demo coverage and signal resets; the catalog manifest (`kerf.components.json` → `component-composition.json`) is regenerated in the same change and byte-checked in CI.
- An enabled control that works only in the demo is a production bug: end-to-end tests exercise child actions through each shipped parent, and unsupported controls are disabled with a reason.

<!-- hotsheet:end section=kerf-ui-catalog-demos -->
