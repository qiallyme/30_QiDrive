---
layout: page
title: Pipelines
slug: pipelines
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
uid: 1269b2022a2c4a23bcf0f2a7a867e790
canonical_ref: ""
template_key: master-template
---

# Pipelines

## Canonical Ingestion Flow

Every file that enters QiOS must pass through this sequence:

```
source
→ detect
→ resolve domain / namespace
→ register in QiArchive (assign canonical identity)
→ assign short visible code (Q + 6 hex)
→ normalize filename
→ extract / inspect
→ enrich metadata
→ chunk
→ embed (local)
→ index (pgvector in qiarchive)
→ route / review / act
```

## Pipeline States

Every archive record must carry one of:

| State | Meaning |
|---|---|
| `detected` | File seen by watcher |
| `registered` | Archive record created, canonical ID assigned |
| `normalized` | Filename normalized per naming contract |
| `extracted` | Text extracted from file |
| `enriched` | Metadata populated |
| `chunked` | Text chunked deterministically |
| `embedded` | Vectors generated |
| `indexed` | Pushed to pgvector |
| `review_pending` | Awaiting human review |
| `routed` | Placement confirmed |
| `finalized` | Full lifecycle complete |
| `failed` | Error state — retryable |

## Failure Philosophy

Failures must be **visible, stateful, retryable, and tied to canonical IDs**.

* Do not silently drop files.
* Do not overwrite state.
* Do not advance objects with weak provenance.

## Supported Input Paths

* Watched local inbox (`C:/QiData/inbox/`)
* Manual import
* Synced storage
* App upload
* Future: email/connector intake

## Subprocess Categories

| Subprocess | Responsibility |
|---|---|
| OCR subprocess | Extract text from scanned docs |
| Extraction subprocess | Parse text from structured files |
| Embedding subprocess | Generate local vector embeddings |
| File scanner | Detect new files in watched paths |
| Sync subprocess | Reconcile local ↔ cloud state |
| Graph projection job | Push canonical records into `qigraph` |
| Retrieval orchestration | Coordinate pgvector + Neo4j recall |
