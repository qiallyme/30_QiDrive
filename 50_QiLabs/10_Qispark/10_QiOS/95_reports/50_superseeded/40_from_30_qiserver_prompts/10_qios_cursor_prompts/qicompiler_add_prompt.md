---
title: QiCompiler Add Prompt
slug: qicompiler_add_prompt
realm: QiOS
type: rule
node: file
created: 2025-01-27T00:00:00Z
updated: 2025-01-27T00:00:00Z
version: 1.0.0
status: publish
system: qios
keywords: [qicompiler, cursor, prompt, tools]
tags: [prompt, cursor, automation, tooling]
context: Cursor prompt for adding QiCompiler to tools directory. Ensures exact file creation and test run.
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
uid: 3a191aca2f4f4e7188c9f73b4ea7d28f
canonical_ref: ""
source_type: manual
template_key: master-template
---

# QiCompiler Add Prompt

Create `tools/qicompiler.py` and `tools/qicompiler_config.yaml` exactly as provided.

Do not refactor filenames or paths.

After creation, run a local compile test against existing registries and confirm output at `data/compiled/qios_constitution_v1.json`.

