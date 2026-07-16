---
layout: page
title: Threads: Data Dependencies
slug: threads-data-dependencies
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
uid: 857cf69ba44c4d948c5c94c614eeb8ac
canonical_ref: ""
template_key: master-template
---

# Threads: Data Dependencies
*   **Reads/Writes**: Writes to the `threads` table.
*   **Foreign Keys**: Actions, QiBits, and Transactions possess a nullable `thread_id` pointing directly to this table.
