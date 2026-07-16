---
layout: page
title: QiMatrix YAML Update Prompt
slug: qimatrix_yaml_prompt
status: publish
updated_at: "2026-07-16T06:49:40-04:00"
sensitivity: internal
classification: system_darkmatter
context: Cursor prompt for updating QiMatrix YAML file. Ensures exact structure preservation.
tags: []
  - prompt
  - cursor
  - automation
  - tooling
  - qispark
keywords: []
  - qimatrix
  - yaml
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
created_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
aliases: []
realm_label: ""
uid: 28e3f2e805074e8b9db2bdb1da4ff5a9
canonical_ref: ""
template_key: master-template
---

# QiMatrix YAML Update Prompt

Update the file at `data/schemas/qios_matrix.yaml` to the exact structure Gina provided.

Do not alter formatting.

Ensure all IDs, arrays, keys, and subtrees are preserved.

Validate YAML with a schema-free linter.
