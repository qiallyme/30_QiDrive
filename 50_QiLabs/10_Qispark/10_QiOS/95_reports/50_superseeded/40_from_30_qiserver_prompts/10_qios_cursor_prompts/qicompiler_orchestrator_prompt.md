---
title: QiCompiler Orchestrator Integration Prompt
slug: qicompiler_orchestrator_prompt
realm: QiOS
type: rule
node: file
created: 2025-01-27T00:00:00Z
updated: 2025-01-27T00:00:00Z
version: 1.0.0
status: publish
system: qios
keywords: [qicompiler, orchestrator, cursor, prompt, integration]
tags: [prompt, cursor, automation, tooling]
context: Cursor prompt for updating orchestrator to consume compiled constitution instead of raw registries.
sensitivity: internal
classification: system_darkmatter
layout: page
summary: ""
created_at: "2026-07-16T06:19:39-04:00"
updated_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
aliases: []
realm_label: ""
uid: 4382e4d7bc0c48a08eb52995868c93c8
canonical_ref: ""
source_type: manual
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

