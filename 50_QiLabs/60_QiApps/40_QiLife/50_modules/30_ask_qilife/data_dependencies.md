---
layout: page
title: Data Dependencies
slug: ""
summary: ""
status: publish
created_at: ""
updated_at: ""
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
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
