---
layout: page
title: Cursor Project Prompt
slug: cursor_project_prompt
status: publish
updated_at: "2026-07-16T06:49:40-04:00"
sensitivity: internal
classification: system_darkmatter
context: QiOS_v1
aliases: []
  - cursor_project_rules
  - qios_cursor_project_prompt
tags: []
  - Rules
  - Automation
  - Governance
  - qispark
keywords: []
  - QiOS
  - Governance
  - Cursor
  - Automation
  - Rule Enforcement
source_type: manual
realm: QiOS
realm_slug: qios_cursor_prompts
qi_decimal: 0.00.10-RUL
type: rule
node: file
created: 2025-11-23
version: 1.0.0
system: qios
naming_strategy: slug_only
sort: 10
graph_weight: 500
orbit: core
summary: ""
created_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
realm_label: ""
uid: 159341421afe421d9fdc7bdda366984b
canonical_ref: ""
template_key: master-template
---

# Cursor Project Prompt

QiOS_v1 PROJECT CANON (always-on rules)

This project implements QiOS + GINA exactly as defined in:
- ./0.00.00-qios_genesis.md (Day Zero Constitution)
- EOS protocol docs in ./ (QID, QiDecimal, Formatting, Atomicity, Realms, Tag Taxonomy)
- Rule + folder + realm registries in ./rules and ./data/sheets
- Brain DB schema and seeds in ./data/schemas and ./data/seeds

NON-NEGOTIABLE PROJECT LAWS:
A) Identity vs Meaning:
   - Filename = identity (slug.ext, optional qidecimal_slug.ext)
   - Metadata/front matter = meaning
   - Vector embeddings = memory
   - Never put dates or meaning into filenames.

B) IDs:
   - QID: opaque unique ID, global monotonic sequence, immutable forever.
   - QiDecimal: semantic address; never auto-renumber existing values; only propose new slots.

C) Markdown + Docs:
   - One H1 per file matching title.
   - Body uses H2+ only.
   - Follow formatting and atomicity protocols.
   - Every folder gets a README describing purpose + governance link.

D) Governance Pipeline:
   - All automation/routing/linting follows 7 layers in order.
   - Do not create logic that skips or reorders layers.

E) Realms + Assets:
   - Realms = ownership/context universes (Personal, Business, Clients, Vault, Playground, Research, Temp, Archives, etc.).
   - Assets are format buckets inside realms (images, video, audio, design, exports).
   - Route by meaning first, format second.

F) Registries as Source of Truth:
   - If adding/altering any rule/folder/realm/property/table/enumeration, update the corresponding YAML/CSV/SQL registry in the same PR.
   - Registries compile the canonical directory tree. No manual trees that drift.

SAFETY:
- Prefer non-destructive operations (quarantine, alias, lineage) over delete.
- If unsure, log and quarantine.

When coding, explicitly cite which canon rules you are adhering to.

ADDENDUM (QiOS v1.1 Observability):
- System must support one-click runtime via GINA Orchestrator.
- Every worker writes heartbeats to public.worker_status.
- Errors must map to human meanings via public.system_event registry.
- UI surfaces render a live workflow diagram from worker_status + registries.
- No worker is called directly by UI except through orchestrator endpoints.
