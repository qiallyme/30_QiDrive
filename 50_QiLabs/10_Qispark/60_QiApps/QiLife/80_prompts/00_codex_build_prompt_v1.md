---
layout: page
title: Codex Build Prompt v1
slug: codex-build-prompt-v1
status: publish
updated_at: "2026-07-16T06:49:40-04:00"
tags: []
  - qispark
source_type: manual
summary: ""
created_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: 46c922258e7241ff99abce00c72b1e1b
canonical_ref: ""
template_key: master-template
---

# Codex Build Prompt v1

You are building the first phase of QiLife, an AI Life Copilot with a Personal LifeDesk cockpit.

**DO NOT begin with generic CRUD screens.**
Build the final scaffold and first vertical slice:

Capture
→ Ingestion
→ Mock Agent Draft
→ Draft Review
→ Approval
→ QiBit
→ Timeline
→ Activity Log
→ Context Dock placeholder

Ensure all work aligns with the new Agent-First Doctrine.
The repo uses React and Vite. Database is local SQLite.

Review the docs in `docs/` for specific architecture decisions before starting:
- `docs/10_product/05_agent_first_product_doctrine.md`
- `docs/40_ui_flows/01_capture_ingestion_review_flow.md`
- `docs/90_decisions/0009_agent_first_copilot_cockpit.md`
