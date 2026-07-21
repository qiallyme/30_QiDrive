---
layout: page
title: Deployment Topology
slug: deployment-topology
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
uid: 27b2467cb293468b8ea8b4991036c6ba
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Deployment Topology

## Proposed Topology

```text
Browser App
  ↓
Cloudflare Pages
  ↓
Supabase API
  ↓
Postgres Database
```

## Later Additions

```text
Bank Provider API
Receipt Storage
Background Jobs
AI Classification Worker
Billing Provider
```
