---
layout: page
title: Build Doctrine
slug: build-doctrine
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
uid: 7bb63f414eca4b90b8631f3ea5bee24c
canonical_ref: ""
template_key: master-template
---

# Build Doctrine
- North Star Scaffold + Daily Vertical Slices.
- The final repo/module boundaries should exist from day one, even if some are stubs.
- Do not build throwaway MVPs.
- Do not build temporary isolated CRUD pages.
- Every implemented feature should be a vertical slice: UI → API → service → database → activity_log → retrieval/context hook.

## Required Module Boundaries

- capture, ingestion, extraction, review, agent, qibits, timeline, buckets, threads, actions, calendar, people, money, knowledge, documents, insights, reports, retrieval, context_dock, storage, sync, settings, exports, spaces/access.
