---
layout: page
title: Timeline: Data Dependencies
slug: timeline-data-dependencies
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
uid: 0f9922c710414937b0a5b20f4ab22da0
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
