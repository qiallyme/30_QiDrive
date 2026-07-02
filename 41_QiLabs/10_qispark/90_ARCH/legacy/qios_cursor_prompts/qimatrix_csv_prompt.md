---
layout: page
title: QiMatrix CSV Update Prompt
slug: qimatrix_csv_prompt
status: canonical
updated_at: "2026-06-29"
sensitivity: internal
classification: system_darkmatter
context: Cursor prompt for updating QiMatrix CSV file. Ensures header validation and Supabase import script generation.
tags:
  - prompt
  - cursor
  - automation
  - tooling
  - qispark
keywords:
  - qimatrix
  - csv
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

# QiMatrix CSV Update Prompt

Place `qios_matrix.csv` into `data/sheets/`.

Validate headers.

Generate matching Supabase import script for `qios_matrix`.
