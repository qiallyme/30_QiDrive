---
layout: page
title: Ask QiLife: Data Dependencies
slug: ask-qilife-data-dependencies
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
uid: 158b5d1b733d4fbf804652dcdcb784de
canonical_ref: ""
template_key: master-template
---

# Ask QiLife: Data Dependencies

- **Reads**: all primary tables plus `links`, `activity_log`, `ai_outputs`, and `daily_summaries` as needed.
- **Writes**:
  - `ai_outputs` for staged query snapshots or suggestions
  - optionally `actions`
  - optionally `knowledge_items`
  - optionally `qibits` of type `note` or `reflection`

Ask QiLife should not depend on a separate `notes` table.
