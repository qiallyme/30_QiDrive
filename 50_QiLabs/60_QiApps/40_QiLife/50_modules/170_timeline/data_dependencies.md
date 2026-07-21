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
uid: c8f83da1ff104b61bb18184349bc04f5
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
