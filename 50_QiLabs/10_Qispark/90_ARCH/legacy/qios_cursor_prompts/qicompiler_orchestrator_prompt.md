---
layout: page
title: QiCompiler Orchestrator Integration Prompt
slug: qicompiler_orchestrator_prompt
status: publish
updated_at: "2026-07-16T06:49:40-04:00"
sensitivity: internal
classification: system_darkmatter
context: Cursor prompt for updating orchestrator to consume compiled constitution instead of raw registries.
tags: []
  - prompt
  - cursor
  - automation
  - tooling
  - qispark
keywords: []
  - qicompiler
  - orchestrator
  - cursor
  - prompt
  - integration
source_type: manual
realm: QiOS
type: rule
node: file
created: 2025-01-27T00:00:00Z
updated: 2025-01-27T00:00:00Z
version: 1.0.0
system: qios
summary: ""
created_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
aliases: []
realm_label: ""
uid: 436f49737e534b3daf248616fcda4044
canonical_ref: ""
template_key: master-template
---

# QiCompiler Orchestrator Integration Prompt

Update `workers/orchestrator/worker_orchestrator.ts`:

- Remove direct reads of registries.
- Load constitution via `_shared/constitution.ts`.
- Use `constitution.rules.layers` for pipeline ordering.
- Use `constitution.ignore.patterns` for scans.
- Use `constitution.realms` for enable/disable decisions.

Preserve existing durable object logic.
