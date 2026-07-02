---
layout: page
title: Inbox: Data Dependencies
slug: inbox-data-dependencies
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

# Inbox: Data Dependencies
*   **Reads/Writes**: Reads and updates the `qibits` table.
*   **Writes**: Creates records in `actions`, `obligations`, or `threads` when triage outcomes are committed.
