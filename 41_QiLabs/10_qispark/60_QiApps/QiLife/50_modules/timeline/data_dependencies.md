---
layout: page
title: Timeline: Data Dependencies
slug: timeline-data-dependencies
status: active
updated_at: "2026-06-29"
tags:
  - qispark
source_type: manual
summary: ""
created_at: ""
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
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
