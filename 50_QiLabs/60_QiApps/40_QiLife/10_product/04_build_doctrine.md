---
layout: page
title: 04 Build Doctrine
slug: 04-build-doctrine
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
uid: b5c843e7c2c347178e7a66be544bd9c4
canonical_ref: ""
source_type: manual
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
