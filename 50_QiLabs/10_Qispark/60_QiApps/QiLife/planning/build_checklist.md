---
layout: page
title: Build Checklist
slug: build-checklist
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
uid: 4a53fc55b06b45de84e07bccf749a704
canonical_ref: ""
template_key: master-template
---

# Build Checklist

## Phase 1: Core Scaffold & First Vertical Slice

- [ ] Scaffold `frontend/src/config/features.ts` (Feature Registry)
- [ ] Scaffold SQLite DB with migrations for core tables (`activity_log`, `qibits`, `file_objects`, `spaces`, etc.)
- [ ] Implement Capture Module (UI intake for text/files)
- [ ] Implement Ingestion Module (dedupe checks, text extraction)
- [ ] Implement Mock Agent Draft (generate mock drafts from ingestion items)
- [ ] Implement Draft Review UI
- [ ] Implement Approval Flow (saving to QiBits, Actions, Timeline)
- [ ] Implement Context Dock Placeholder

## Phase 2: Spaces and Storage

- [ ] Implement Storage & Sync settings UI
- [ ] Build Document Vault UI and hashing logic
- [ ] Implement Space switcher and Mom Care scoped access

## Phase 3: Legacy Bridge

- [ ] Create legacy bridge tables
- [ ] Implement import script/UI for Supabase legacy data
