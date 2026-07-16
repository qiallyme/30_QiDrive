---
layout: page
title: 0007 App Managed Storage And Sync
slug: 0007-app-managed-storage-and-sync
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
uid: a8f73748b018428a85ff88636b87376f
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Decision 0007: App-Managed Storage and Sync

## Context
Managing files and syncing manually across folders is brittle and error-prone.

## Decision
QiLife will act as a control center managing its own storage footprint (DB, file vault, exports). Folders will be projections of metadata rather than the source of truth.

## Consequences
- Eliminates manual folder management.
- Requires building storage management and health check features.
- Clear separation between repo (code), private data (DB/files), and exports (Drive/QiNexus).
