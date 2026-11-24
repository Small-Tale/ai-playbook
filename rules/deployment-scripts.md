---
root: true
targets: ["*"]
description: "One phased, re-runnable deploy script per environment with SHA-tagged artifacts and stdin-only secrets"
---

<!-- hotsheet:begin section=deployment-scripts v=2 -->

## Deployment Scripts

One checked-in environment-argument script beside infrastructure definitions serves people and agents (e.g. `scripts/deploy.sh beta`); never deploy by hand console.

- Tag artifacts with short commit SHA; dirty trees add `-dirty`, go only to non-production and announce this first. Production uses only CI-built/tested SHA or tag.
- Before mutation, check tools, every credential type used (CLI and application-default may differ), and state backend with cheap real read-only calls. On terminal stdin offer the fix; otherwise print its exact command and exit nonzero.
- Run repeatable phases: (1) base APIs/registries/accounts/buckets/databases/empty secrets; (2) fill machine secrets, list missing human secrets with exact `set-secret.sh <env> <NAME>` commands, stop with exit 0 until filled; (3) build for pinned runtime architecture, push, plan, show/confirm, apply, smoke-test deployed URL. No service may reference an unversioned secret. Base phases may auto-approve; running-service changes require confirmation.
- Secret values never enter argv, committed variables, logs or repository. `set-secret.sh` accepts stdin/hidden prompt and writes a new version. Commit nonsecret per-environment variables separately.
- Every phase is repeat-safe; failure recovery is fix and rerun the same command. Never auto-approve destruction of stateful resources.
- Architecture deployment docs list environments/script/tools/smoke test; codebase map links infrastructure. Shipping ticket records deployed environment and SHA.

Project-level deviations require a compelling/necessary reason in conventions.

<!-- hotsheet:end section=deployment-scripts -->
