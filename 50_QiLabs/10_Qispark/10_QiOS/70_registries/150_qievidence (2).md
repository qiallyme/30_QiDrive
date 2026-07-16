---
layout: page
title: 150 Qievidence
slug: ""
summary: ""
status: publish
created_at: ""
updated_at: ""
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
source_type: manual
template_key: master-template
---

# QiEvidence Domain (QiEn)

## Purpose
QiEvidence (internal engine name: **QiEn**) is a local-first evidence intelligence module that transforms raw multimedia and documents (videos, photos, PDFs, audio, screenshots, etc.) into a structured, cross-referenced, searchable evidence archive.

Core capabilities:
- Timestamped transcription and visual event extraction
- Neutral, cold, objective narration (no emotion, no speculation, no mind-reading)
- Entity normalization and tracking (people, vehicles, locations, accounts, etc.)
- Automated contradiction / inconsistency detection
- Master timeline assembly across all artifacts
- Human review queue for uncertain or conflicting items

It is a disciplined evidence-processing engine with two brains:
- **Extractor**: Factual, structured output only.
- **Analyst**: Cross-referencing, flagging, and neutral narration.

## Folder Structure
The local execution environment uses a standardized folder hierarchy:

```
/QiEvidence/
├── input/
│   ├── videos/
│   ├── photos/
│   ├── documents/
│   └── other/
├── working/
│   ├── audio/
│   ├── frames/
│   └── transcripts/
├── output/
│   ├── events/
│   ├── entities/
│   ├── timelines/
│   ├── reports/
│   └── reviews/
└── archive/ (hashed originals + metadata)
```

## Schema: `qievidence`
The domain uses the following tables, linked to `qione.tenants` and `qicase.cases`.

| Table | Description |
|---|---|
| `evidence_records` | Master artifact registry (one row per file) |
| `evidence_segments` | Chunked slices of long media/documents |
| `evidence_entities` | Canonical people, vehicles, locations, accounts, etc. |
| `evidence_entity_mentions` | Join table (where each entity appears) |
| `evidence_events` | Observed or extracted events |
| `evidence_claims` | Statements/assertions extracted from content |
| `evidence_observations` | Machine-grounded visual/textual facts (non-claims) |
| `evidence_links` | Cross-references between any two objects |
| `evidence_conflicts` | Detected inconsistencies (the “money” table) |
| `evidence_timelines` | Named timeline containers |
| `evidence_timeline_items` | Ordered items in timelines |
| `evidence_reviews` | Human review queue |

## Processing Pipeline
1. **Ingest**: Hash file, read metadata, assign evidence ID, store in `evidence_records`.
2. **Extract**: 
   - Audio → `faster-whisper` → transcript.
   - Video → `ffmpeg` keyframes → `Qwen2.5-VL` observations.
   - Photos/Docs → OCR + `Qwen2.5-VL` description.
3. **Structure**: Populate segments, entities, events, claims, observations.
4. **Link & Compare**: Build links and run contradiction scanner.
5. **Timeline Assembly**: Populate timelines and items.
6. **Narrate**: Final cold, logical report using strict prompt rules.
7. **Review**: Push uncertain/conflicting items to `evidence_reviews`.

## Narration Rules
- No emotion words.
- No speculation or intent inference.
- Separate Observed / Stated / Uncertain.
- Preserve timestamps and source IDs.
- Mark unclear audio/visuals explicitly.
