---
layout: article
title: Article 2. API Workers
slug: qicode-title-14-article-02-api-workers
summary: ""
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
qicode_title: 14
qicode_article: 2
parent_title: Title 14. QiWorkers
canonical_ref: QiCode T14.A02
source_type: manual
---

## Article 2. API Workers

Stable ID: `T14.A02`

### Sec. 14.02.010. API Governance

Stable ID: `T14.A02.S010`

- `Line 1` API workers expose callable endpoints that bridge between QiLabs systems and external or internal consumers; Cloudflare Workers are the preferred deployment surface for public-facing API workers. (`Sec. 14.02.010.L001`; stable ID `T14.A02.S010.L001`)
- `Line 2` Each API worker must have a documented contract (id, trigger, input, output, fleet_context, failure policy). (`Sec. 14.02.010.L002`; stable ID `T14.A02.S010.L002`)
- `Line 3` Worker state must be logged to `qisys.jobs` as: `queued`, `running`, `completed`, `failed`, or `retrying`. (`Sec. 14.02.010.L003`; stable ID `T14.A02.S010.L003`)

### Sec. 14.02.020. Worker Categories

Stable ID: `T14.A02.S020`

- `Line 1` Authorized worker categories include: Graph projection, Retrieval orchestration, Metadata enrichment, Repair/retry job, Background embedding, Sync worker, Enrollment reconciliation, Config distribution, Folder assignment sync, and Node update/repair. (`Sec. 14.02.020.L001`; stable ID `T14.A02.S020.L001`)
- `Line 2` Workers never redefine canonical identity; they always operate on canonically-identified records (via `canonical_id`). (`Sec. 14.02.020.L002`; stable ID `T14.A02.S020.L002`)
- `Line 3` Workers never write directly to canonical schemas (`qiarchive`) without going through the pipeline contract. (`Sec. 14.02.020.L003`; stable ID `T14.A02.S020.L003`)


