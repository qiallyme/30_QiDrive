---
layout: page
title: Threads: Data Dependencies
slug: threads-data-dependencies
status: active
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

# Threads: Data Dependencies
*   **Reads/Writes**: Writes to the `threads` table.
*   **Foreign Keys**: Actions, QiBits, and Transactions possess a nullable `thread_id` pointing directly to this table.
