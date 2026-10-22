---
root: true
targets: ["*"]
description: "One phased, re-runnable deploy script per environment with SHA-tagged artifacts and stdin-only secrets"
---

<!-- hotsheet:begin section=deployment-scripts v=1 -->

## Deployment Scripts

Deploying is one checked-in script that takes the environment as its argument (`scripts/deploy.sh beta`), lives beside the infrastructure definitions it applies, and runs the same way for a person and for an agent. Nothing is deployed by hand from a cloud console.

- **Artifact identity.** The image or bundle is tagged with the short commit SHA, with a `-dirty` suffix when the tree has uncommitted changes. A dirty deploy goes only to a non-production environment and the script says so in its first line of output. Production deploys only a SHA or tag that CI has already built and tested.
- **Pre-flight.** Check required tools, every kind of credential the run uses (for example the CLI account and application-default credentials, which are separate), and the state backend with a real, cheap, read-only call before applying anything, because an expired credential otherwise fails mid-apply where it cannot prompt. When stdin is a terminal, offer to run the fix; otherwise print the exact command and exit non-zero.
- **Phased apply.** Phase one creates base infrastructure: APIs, registries, service accounts, buckets, databases, and empty secrets. Phase two fills machine-set secrets (a generated session secret, a derived connection string), then lists every human secret still empty with the exact `set-secret.sh <env> <NAME>` command and stops with exit 0, so a running service never references a secret that has no version. Phase three builds for the runtime's platform (pin the architecture; an arm64 host builds amd64 for the service), pushes, plans, shows the plan and confirms, applies, and smoke-tests the deployed URL. Base phases may auto-approve; the phase that changes the running service confirms.
- **Secrets.** A secret value is never on a command line, in a committed variables file, in a log, or in the repository. `set-secret.sh` reads from stdin or a hidden prompt and writes a new secret version. Non-secret, environment-specific configuration lives in a committed per-environment variables file.
- **Re-runnable.** Every phase is safe to repeat and the recovery path after any failure is "fix, re-run the same command". The script never auto-approves a plan that destroys a stateful resource.
- **Document and record.** The architecture document's deployment section names the environments, the script, the required tools, and the smoke test; the codebase map points at the infrastructure directory. The ticket that shipped a change records the environment and SHA it was deployed as.

Deviate only at the project level for a compelling or necessary reason, recorded in the project's conventions document.

<!-- hotsheet:end section=deployment-scripts -->
