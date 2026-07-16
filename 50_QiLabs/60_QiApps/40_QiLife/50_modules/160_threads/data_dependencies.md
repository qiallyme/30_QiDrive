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
uid: 03a5eb93849d460fb3369d01b04e2bca
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Threads: Data Dependencies
*   **Reads/Writes**: Writes to the `threads` table.
*   **Foreign Keys**: Actions, QiBits, and Transactions possess a nullable `thread_id` pointing directly to this table.
