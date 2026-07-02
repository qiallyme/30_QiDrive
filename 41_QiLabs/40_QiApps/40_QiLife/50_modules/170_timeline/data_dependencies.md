---
layout: page
title: Data Dependencies
slug: ""
summary: ""
status: active
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

# Timeline: Data Dependencies

- **Reads**:
  - `qibits`
  - `actions`
  - `transactions`
  - `events`
  - `daily_summaries`
- **Projection rules**:
  - QiBits by `COALESCE(happened_at, captured_at, created_at)`
  - Actions by `completed_at`, else `scheduled_for`, else `created_at`
  - Transactions by `date`
  - Events by `start_time`
  - Daily summaries by `date`
- **Writes**: none directly; Timeline is a read model built from other tables.
