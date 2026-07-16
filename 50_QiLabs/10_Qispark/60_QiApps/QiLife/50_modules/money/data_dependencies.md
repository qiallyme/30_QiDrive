---
layout: page
title: Money: Data Dependencies
slug: money-data-dependencies
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
uid: 2716e24be5c3424a90c2d7d60579bea7
canonical_ref: ""
template_key: master-template
---

# Money: Data Dependencies
*   **Reads/Writes**: Writes to `transactions` and `obligations` tables.
*   **Foreign Keys**: Connects to `people` (via label or link) and `threads` (via `thread_id`).
