---
root: true
targets: ["*"]
description: "Test isolation, build-once, flake and quarantine policy, and quiet output"
---

<!-- hotsheet:begin section=test-operations v=4 -->

## Test Operations

- Isolate home/data at runner or build-config level, not per test. Never touch real homes, stores or running services; retain a test rejecting machine-local fixture/output paths.
- Build binaries/bundles once in global setup, skipping fresh builds, never per test file. The full gate runs the built artifact and its health endpoint, beyond compiling.
- Wait for events/readiness/state, never fixed delays; pending-response fakes gate on promises/channels, not timers.
- A flake fix must pass repeatedly without retries under full-suite load (e.g. 20 repeats). Retries occur only in full CI, at most two, visible in reports, with a ticket for every retried test. Quarantine markers name fix tickets and match a table one-to-one in CI; neither retry nor quarantine is a fix.
- `hotsheet-testing-philosophy` owns quiet output. The failure-only wrapper prints summary, capped failure excerpts and log path. Keep and act on a slowest-tests profile.
- Validate the feature coverage matrix by script: unit/E2E/manual statuses match evidence paths. The manual plan covers only behavior CI cannot reliably check.

<!-- hotsheet:end section=test-operations -->
