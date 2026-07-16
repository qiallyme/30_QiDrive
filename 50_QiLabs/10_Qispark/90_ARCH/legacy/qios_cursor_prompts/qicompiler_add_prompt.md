---
layout: page
title: QiCompiler Add Prompt
slug: qicompiler_add_prompt
status: publish
updated_at: "2026-06-29"
sensitivity: internal
classification: system_darkmatter
context: Cursor prompt for adding QiCompiler to tools directory. Ensures exact file creation and test run.
tags:
  - prompt
  - cursor
  - automation
  - tooling
  - qispark
keywords:
  - qicompiler
  - cursor
  - prompt
  - tools
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

# QiCompiler Add Prompt

Create `tools/qicompiler.py` and `tools/qicompiler_config.yaml` exactly as provided.

Do not refactor filenames or paths.

After creation, run a local compile test against existing registries and confirm output at `data/compiled/qios_constitution_v1.json`.
