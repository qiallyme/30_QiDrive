---
title: QiMatrix YAML Update Prompt
slug: qimatrix_yaml_prompt
realm: QiOS
type: rule
node: file
created: 2025-01-27T00:00:00Z
updated: 2025-01-27T00:00:00Z
version: 1.0.0
status: publish
system: qios
keywords: [qimatrix, yaml, cursor, prompt, update]
tags: [prompt, cursor, automation, tooling]
context: Cursor prompt for updating QiMatrix YAML file. Ensures exact structure preservation.
sensitivity: internal
classification: system_darkmatter
layout: page
summary: ""
created_at: "2026-07-16T06:19:39-04:00"
updated_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
aliases: []
realm_label: ""
uid: cb3d6242e1fd4781ae7abeabc2c24b4c
canonical_ref: ""
source_type: manual
template_key: master-template
---

# QiMatrix YAML Update Prompt

Update the file at `data/schemas/qios_matrix.yaml` to the exact structure Gina provided.

Do not alter formatting.

Ensure all IDs, arrays, keys, and subtrees are preserved.

Validate YAML with a schema-free linter.

