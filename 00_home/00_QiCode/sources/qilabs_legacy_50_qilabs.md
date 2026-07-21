---
layout: section
title: QiLabs Legacy Source — 50_QiLabs
slug: qilabs-legacy-50-qilabs-source
summary: Preserved outline of the legacy 50_QiLabs source material used as reference for QiCode Titles 10–18.
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
  - qilabs
  - legacy
  - source
source_type: manual
---

# QiLabs Legacy Source — 50_QiLabs

This document preserves the structural outline of the legacy `50_QiLabs` vault folder used as reference material for the QiCode Titles 10–18 doctrine migration.

> The original source at `c:\QiLabs\40_QiVault\50_QiLabs` is **not deleted or renamed**. This is reference-only.

## Source Path

`c:\QiLabs\40_QiVault\50_QiLabs`

## Legacy Top-Level Structure

```text
50_QiLabs/
├── 000_RUN_ME_FIRST.md
├── _index.md
├── TAG_REGISTRY_PATTERN.md
├── 2026-05-17_supabase_markmind.md
├── qiingest_life_feed_reference_architecture.md
├── 00_QiLabs.workspace/     → workspace templates, codex, tools
├── 10_Qispark/              → QiOS policies, rules, schemas, registries, ADRs
│   └── 10_QiOS/
│       ├── 10_Policies/
│       ├── 20_Rules-and-standards/
│       ├── 30_roadmaps/
│       ├── 40_Structure/
│       ├── 50_metadata/
│       ├── 60_decisions/    → ADRs 0001–0019
│       ├── 70_registries/
│       ├── 80_schemas/
│       └── 90_Templates/
├── 20_QiServer/             → server docs, cockpit, docker, services, workers
├── 30_QiDrive/              → stub (_40_QiVault.md only)
├── 60_QiApps/               → QiLife, QiFi, GINA, Sites, etc.
└── 70_QiSites/              → (not found in vault legacy mirror)
```

## Notable Legacy Sub-Content

### 10_Qispark/10_QiOS/60_decisions (ADRs 0001–0019)
Key architectural decisions recorded in this legacy source:
- ADR-0001: QiOS DNA as Master Doctrine Repo
- ADR-0006: QiSystem Numbering Bands
- ADR-0008: QiLabs Root
- ADR-0012: Data Strategy
- ADR-0013: Folder Documentation Model
- ADR-0018: Supabase QiLife Data Authority
- ADR-0019: Directus as Supabase Admin and API Layer

### 10_Qispark/10_QiOS/70_registries
Band registry, domain registry, folder registry, namespace registry, realms registry, sensitivity classification, and slug mappings.

### 20_QiServer
Cockpit, Docker Compose, Portainer, Tailscale, Uptime Kuma, GetHomepage, services (n8n, ActivityWatch, SolidTime, QiLedger), workers, infrastructure docs.

### 60_QiApps
QiLife (full product docs, modules, architecture, data model, decisions), QiFi (full product docs), GINA, QiJourney.

## Retired / Out-of-Scope Legacy Items

- **QiAccess** — retired as a standalone module; not receiving a QiCode title
- **QiDNA** — not a standalone module; doctrine content inside QiSpark
- **QiConnect** — legacy section but not in T10–18 scope
- **QiMemory** — legacy section; content referenced under QiServer/QiWorkers doctrine
- **50_QiLabs/90_ARCH** — legacy ARCH notes; reference only

## Cross References

- [Migration Map](qilabs_title_migration_map.md)
- [QiCode Index](../_index.md)
