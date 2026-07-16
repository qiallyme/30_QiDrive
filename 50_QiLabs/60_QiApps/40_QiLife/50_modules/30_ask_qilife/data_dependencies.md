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
uid: 99747417f5c04438b96218903c36441b
canonical_ref: ""
source_type: manual
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
