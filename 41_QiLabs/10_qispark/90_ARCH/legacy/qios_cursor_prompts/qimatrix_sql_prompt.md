---
layout: page
title: QiMatrix SQL Update Prompt
slug: qimatrix_sql_prompt
status: canonical
updated_at: "2026-06-29"
sensitivity: internal
classification: system_darkmatter
context: Cursor prompt for updating QiMatrix SQL schema file. Ensures proper SQL formatting and table creation.
tags:
  - prompt
  - cursor
  - automation
  - tooling
  - qispark
keywords:
  - qimatrix
  - sql
  - cursor
  - prompt
  - update
source_type: manual
realm: QiOS
type: rule
node: file
created: 2025-01-27T00:00:00Z
updated: 2025-01-27T00:00:00Z
version: 1.0.0
system: qios
summary: ""
created_at: ""
author: ""
owner: ""
aliases: []
realm_label: ""
uid: ""
canonical_ref: ""
template_key: master-template
---

# QiMatrix SQL Update Prompt

Place `qios_matrix.sql` into `data/schemas/` exactly as provided.

Run through SQL formatter but do not reorder columns.

Ensure table exists in Supabase.
