---
layout: page
title: Exports
slug: exports
status: publish
updated_at: "2026-07-16T06:49:38-04:00"
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
uid: 220365203a4246beada9b63d2606db95
canonical_ref: ""
template_key: master-template
---

# Exports

## Exports are Non-Canonical

> Exports are derived outputs generated from canonical records. They are **not** truth sources.

An export is always regeneratable from its source canonical records. If regenerating an export produces different results, the **canonical records** are the authority — not the export.

## Export Types

| Export Type | Source | Format |
|---|---|---|
| Case summary reports | `qicase` records | PDF, Markdown |
| Extracted text | `qiarchive.archive_chunks` | Plain text, JSON |
| Embedding snapshots | `qiarchive.archive_chunks.embedding` | Parquet, JSON |
| Graph exports | `qigraph.edges` + `qigraph.master_index` | GraphML, JSON |
| Financial reports | `qihome.expenses`, `qitax.returns` | PDF, CSV |
| AI chat transcripts | `qially.sessions`, `qially.messages` | Markdown, JSON |

## Export Rules

* Exports must be clearly labeled as derived (not canonical)
* Exports must include a reference to their source `canonical_id` or `archive_id`
* Exports must not be committed back to canonical tables
* Exports may be cached but must be versioned and timestamped
* Stale exports must be flagged, not silently used

## Export Location

Exports should be stored outside the canonical database:

* Local: `C:/QiData/exports/` (temporary)
* Cloud: A dedicated non-canonical storage bucket or folder
* Never: back into a canonical schema table as if they were primary records
