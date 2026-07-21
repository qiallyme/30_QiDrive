---
layout: section
title: Title 14. QiWorkers
slug: qicode-title-14-qiworkers
summary: QiWorkers governs 25_QiWorkers — background jobs, API workers, sync tools, queues, and automation.
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
  - qilabs
source_type: manual
---

# Title 14. QiWorkers

## Citation

- Legal citation: `QiCode Title 14`
- Article citation: `QiCode Title 14, Article #`
- Section citation: `QiCode Sec. 14.##.###`
- Stable ID alias: `QiCode T14.A##.S###.L###`

## Rule of Construction

- `Rule 14.001.L001` This title governs `25_QiWorkers` — background jobs, APIs, sync tools, and automation workers. (stable ID `T14.R001.L001`)
- `Rule 14.001.L002` A section states a governing principle; a line states a citeable rule or application. (stable ID `T14.R001.L002`)
- `Rule 14.001.L003` Exceptions must be named, reviewed, and linked to the record that justifies them. (stable ID `T14.R001.L003`)

## Article 1. Worker Purpose

Stable ID: `T14.A01`

### Sec. 14.01.010. Primary Function

Stable ID: `T14.A01.S010`

- `Line 1` QiWorkers holds background jobs, APIs, sync tools, and automation workers that operate across QiLabs domains. (`Sec. 14.01.010.L001`; stable ID `T14.A01.S010.L001`)
- `Line 2` Workers do not become app UI; interface concerns belong in QiApps. (`Sec. 14.01.010.L002`; stable ID `T14.A01.S010.L002`)
- `Line 3` If use is ambiguous, the placement rule for the nearest parent title controls. (`Sec. 14.01.010.L003`; stable ID `T14.A01.S010.L003`)

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

## Article 3. Ingestion Workers

Stable ID: `T14.A03`

### Sec. 14.03.010. Ingestion Governance

Stable ID: `T14.A03.S010`

- `Line 1` Ingestion workers handle pulling, transforming, and routing data from external sources into QiLabs systems. (`Sec. 14.03.010.L001`; stable ID `T14.A03.S010.L001`)
- `Line 2` Ingestion workers must log every operation and expose a status endpoint or dashboard. (`Sec. 14.03.010.L002`; stable ID `T14.A03.S010.L002`)
- `Line 3` Source material routed by an ingestion worker must retain provenance metadata after ingestion. (`Sec. 14.03.010.L003`; stable ID `T14.A03.S010.L003`)

## Article 4. Sync and Automation

Stable ID: `T14.A04`

### Sec. 14.04.010. Sync Governance

Stable ID: `T14.A04.S010`

- `Line 1` Sync workers reconcile state between QiLabs systems; they must be idempotent and recoverable. (`Sec. 14.04.010.L001`; stable ID `T14.A04.S010.L001`)
- `Line 2` Automation workflows (n8n or equivalent) that cross domain boundaries must be documented in QiWorkers. (`Sec. 14.04.010.L002`; stable ID `T14.A04.S010.L002`)
- `Line 3` Sync operations must not silently overwrite canonical records without a conflict resolution policy. (`Sec. 14.04.010.L003`; stable ID `T14.A04.S010.L003`)

## Article 5. Queues and Jobs

Stable ID: `T14.A05`

### Sec. 14.05.010. Job Queue Policy

Stable ID: `T14.A05.S010`

- `Line 1` Long-running or deferred operations must use a queue; fire-and-forget is not acceptable for critical workflows. (`Sec. 14.05.010.L001`; stable ID `T14.A05.L010.L001`)
- `Line 2` Queue failures must be logged, alerted, and recoverable without manual data reconstruction. (`Sec. 14.05.010.L002`; stable ID `T14.A05.S010.L002`)
- `Line 3` Job retention and dead-letter policy must be documented for each queue. (`Sec. 14.05.010.L003`; stable ID `T14.A05.S010.L003`)

## Article 6. Error Handling

Stable ID: `T14.A06`

### Sec. 14.06.010. Error Policy

Stable ID: `T14.A06.S010`

- `Line 1` Workers must be observable: every worker must emit structured logs accessible without SSH. (`Sec. 14.06.010.L001`; stable ID `T14.A06.S010.L001`)
- `Line 2` Workers must be recoverable: failure state must not require manual reconstruction of lost work. (`Sec. 14.06.010.L002`; stable ID `T14.A06.S010.L002`)
- `Line 3` Workers must be documented: the runbook for each worker must exist before it is deployed. (`Sec. 14.06.010.L003`; stable ID `T14.A06.S010.L003`)

## Article 7. Deployment Rules

Stable ID: `T14.A07`

### Sec. 14.07.010. Deployment Governance

Stable ID: `T14.A07.S010`

- `Line 1` Workers are deployed to QiServer (Docker), Cloudflare Workers, or an equivalent governed runtime. (`Sec. 14.07.010.L001`; stable ID `T14.A07.S010.L001`)
- `Line 2` Deployment configuration must be version-controlled in `25_QiWorkers`. (`Sec. 14.07.010.L002`; stable ID `T14.A07.S010.L002`)
- `Line 3` Environment secrets must not be committed to source control; use `.env.example` and a secrets manager. (`Sec. 14.07.010.L003`; stable ID `T14.A07.S010.L003`)

## Cross References

- [QiCode Index](../_index.md)
- [Title 10 — QiLabs](../title_10_qilabs/title_10_qilabs.md)
- [Title 13 — QiServer](../title_13_qiserver/title_13_qiserver.md)
- [Migration Map](../reference/qilabs_title_migration_map.md)
