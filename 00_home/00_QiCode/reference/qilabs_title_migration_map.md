---
layout: section
title: QiLabs Title Migration Map
slug: qilabs-title-migration-map
summary: Maps legacy 50_QiLabs source material to canonical QiCode Titles 10–18.
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
  - qilabs
  - migration
source_type: manual
---

# QiLabs Title Migration Map

## Migration Metadata

- **Legacy Source:** `40_QiVault/50_QiLabs`
- **Target Structure:** QiCode Titles 10–18
- **Migration Date:** 2026-07-21
- **Type:** Controlled doctrine migration — source is preserved, not deleted or renamed

## Mapping Table

| Legacy Area | New QiCode Title | Notes |
|---|---|---|
| `50_QiLabs` root | Title 10 — QiLabs | Root operating environment constitution |
| `50_QiLabs/00_QiLabs.workspace` | Title 11 — QiLabs Workspace | Workspace/tools/templates/housekeeping |
| `50_QiLabs/10_Qispark` | Title 12 — QiSpark | Docs/site/landing/doctrine layer |
| `50_QiLabs/20_QiServer` | Title 13 — QiServer | Runtime/infrastructure/services |
| *(no legacy mirror)* | Title 14 — QiWorkers | APIs/workers/automation — written from doctrine spec |
| `50_QiLabs/30_QiDrive` (stub only) | Title 15 — QiDrive | Drive/files/evidence source of truth |
| `40_QiVault` root | Title 16 — QiVault | Markdown vault / local knowledge workspace |
| `50_QiLabs/60_QiApps` | Title 17 — QiApps | Apps/projects/UI layers |
| `50_QiLabs/70_QiSites` | Title 18 — QiSites | Static/public site output |

## Out-of-Scope Legacy Sections

The following legacy sections exist in `50_QiLabs` but are **not** mapped to Titles 10–18:

| Legacy Folder | Status | Notes |
|---|---|---|
| `50_QiLabs/30_QiDrive` stub | Not in scope | Title 15 written from doctrine spec |
| `50_QiConnect` (appears in sub-docs) | Not in scope | QiConnect is not a standalone title in T10–18 |
| `30_QiMemory` (legacy sub-section) | Not in scope | QiMemory content lives under QiServer/QiWorkers doctrine |
| `50_QiLabs/90_ARCH` | Not in scope | Legacy ARCH notes — reference only |

## Doctrine Updates

- **QiAccess** is retired as a separate module. It does not receive a title.
- **QiDNA** is not a standalone module. It is doctrine content inside QiSpark / QiCode docs.
- **QiSpark** now governs docs, landing, navigation, and doctrine — not just a dev layer.
- **QiDrive** is the file and markdown source-of-truth layer (Google Drive primary runtime).

## Cross References

- [QiCode Index](../_index.md)
- [Legacy 50_QiLabs Source](../sources/qilabs_legacy_50_qilabs.md)
