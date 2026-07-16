---
layout: page
title: Data Dependencies
slug: data-dependencies
summary: ""
status: publish
created_at: "2026-07-16T06:19:39-04:00"
updated_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: e0a5e53471684803b9982a5330c40b73
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Money: Data Dependencies
*   **Reads/Writes**: Writes to `transactions` and `obligations` tables.
*   **Foreign Keys**: Connects to `people` (via label or link) and `threads` (via `thread_id`).
