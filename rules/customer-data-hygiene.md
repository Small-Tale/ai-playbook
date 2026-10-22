---
root: true
targets: ["*"]
description: "Keep customer content out of tickets, logs, fixtures, and telemetry"
---

<!-- hotsheet:begin section=customer-data-hygiene v=1 -->

## Customer Data Hygiene

Never copy customer documents, messages, names, or figures into tickets, notes, commit messages, logs, test fixtures, demo data, or telemetry. Record ids, counts, sizes, timings, and shapes instead. Reproduce a customer-reported defect with synthetic data that matches the shape, and state in the ticket that no customer content was copied. Observability events carry identifiers and metrics only. When a capture would show customer content, use demo data or redact before attaching.

<!-- hotsheet:end section=customer-data-hygiene -->
