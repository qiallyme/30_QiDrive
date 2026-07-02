---
layout: page
title: Data Dependencies
slug: ""
summary: ""
status: active
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

# Threads: Data Dependencies
*   **Reads/Writes**: Writes to the `threads` table.
*   **Foreign Keys**: Actions, QiBits, and Transactions possess a nullable `thread_id` pointing directly to this table.
