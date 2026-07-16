---
layout: page
title: Money: Data Dependencies
slug: money-data-dependencies
status: publish
updated_at: "2026-06-29"
tags:
  - qispark
source_type: manual
summary: ""
created_at: ""
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
template_key: master-template
---

# Money: Data Dependencies
*   **Reads/Writes**: Writes to `transactions` and `obligations` tables.
*   **Foreign Keys**: Connects to `people` (via label or link) and `threads` (via `thread_id`).
