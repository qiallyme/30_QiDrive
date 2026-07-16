---
layout: page
title: Data Dependencies
slug: ""
summary: ""
status: publish
created_at: ""
updated_at: ""
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Money: Data Dependencies
*   **Reads/Writes**: Writes to `transactions` and `obligations` tables.
*   **Foreign Keys**: Connects to `people` (via label or link) and `threads` (via `thread_id`).
