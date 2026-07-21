---
layout: section
title: Title 15. QiDrive
slug: qicode-title-15-qidrive
summary: QiDrive governs 30_QiDrive — the file and markdown source-of-truth layer for files, evidence, docs, and archives.
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
  - qilabs
source_type: manual
---

# Title 15. QiDrive

## Citation

- Legal citation: `QiCode Title 15`
- Article citation: `QiCode Title 15, Article #`
- Section citation: `QiCode Sec. 15.##.###`
- Stable ID alias: `QiCode T15.A##.S###.L###`

## Rule of Construction

- `Rule 15.001.L001` This title governs `30_QiDrive` — the file and markdown source-of-truth layer. (stable ID `T15.R001.L001`)
- `Rule 15.001.L002` A section states a governing principle; a line states a citeable rule or application. (stable ID `T15.R001.L002`)
- `Rule 15.001.L003` Exceptions must be named, reviewed, and linked to the record that justifies them. (stable ID `T15.R001.L003`)

## Article 1. QiDrive Purpose

Stable ID: `T15.A01`

### Sec. 15.01.010. Primary Function

Stable ID: `T15.A01.S010`

- `Line 1` QiDrive is the file and markdown source-of-truth layer: files, evidence, docs, assets, exports, and archives. (`Sec. 15.01.010.L001`; stable ID `T15.A01.S010.L001`)
- `Line 2` QiApps are interface layers; QiDrive preserves the source material that apps display or operate on. (`Sec. 15.01.010.L002`; stable ID `T15.A01.S010.L002`)
- `Line 3` If use is ambiguous, the placement rule for the nearest parent title controls. (`Sec. 15.01.010.L003`; stable ID `T15.A01.S010.L003`)

## Article 2. Drive as Source of Truth

Stable ID: `T15.A02`

### Sec. 15.02.010. Google Drive as Primary Runtime

Stable ID: `T15.A02.S010`

- `Line 1` Google Drive is the primary runtime for QiDrive files and is governed by QiDrive doctrine. (`Sec. 15.02.010.L001`; stable ID `T15.A02.S010.L001`)
- `Line 2` Local `30_QiDrive` is the vault-facing mirror or staging area; Google Drive is the live source. (`Sec. 15.02.010.L002`; stable ID `T15.A02.S010.L002`)
- `Line 3` Conflicts between local and cloud versions must default to the cloud version unless a conflict policy exists. (`Sec. 15.02.010.L003`; stable ID `T15.A02.S010.L003`)

## Article 3. Ingestion

Stable ID: `T15.A03`

### Sec. 15.03.010. Ingestion Policy

Stable ID: `T15.A03.S010`

- `Line 1` Files enter QiDrive through a documented ingestion path; drop-copying without metadata is not permitted for source material. (`Sec. 15.03.010.L001`; stable ID `T15.A03.S010.L001`)
- `Line 2` Ingested files must carry at minimum: source, date, sensitivity classification, and content type. (`Sec. 15.03.010.L002`; stable ID `T15.A03.S010.L002`)
- `Line 3` QiSpark docs may be authored as markdown in QiDrive and published through QiSpark build pipelines. (`Sec. 15.03.010.L003`; stable ID `T15.A03.S010.L003`)

## Article 4. Files and Evidence

Stable ID: `T15.A04`

### Sec. 15.04.010. Evidence Handling

Stable ID: `T15.A04.S010`

- `Line 1` Evidence files carry heightened protection and must not be moved, renamed, or modified without documented justification. (`Sec. 15.04.010.L001`; stable ID `T15.A04.S010.L001`)
- `Line 2` Evidence files must retain original metadata and file integrity checksums where available. (`Sec. 15.04.010.L002`; stable ID `T15.A04.S010.L002`)
- `Line 3` Access to evidence files is governed by the sensitivity classification in the file's frontmatter or container record. (`Sec. 15.04.010.L003`; stable ID `T15.A04.S010.L003`)

## Article 5. Folder Structure

Stable ID: `T15.A05`

### Sec. 15.05.010. Folder Organization

Stable ID: `T15.A05.S010`

- `Line 1` QiDrive folder structure must reflect the governed domain hierarchy documented in the QiCode title map. (`Sec. 15.05.010.L001`; stable ID `T15.A05.S010.L001`)
- `Line 2` Ad hoc folders must not be created without documentation in the corresponding domain title. (`Sec. 15.05.010.L002`; stable ID `T15.A05.S010.L002`)
- `Line 3` Top-level Drive folders mirror QiLabs root domain bands where applicable. (`Sec. 15.05.010.L003`; stable ID `T15.A05.S010.L003`)

## Article 6. Protected Records

Stable ID: `T15.A06`

### Sec. 15.06.010. Protection Policy

Stable ID: `T15.A06.S010`

- `Line 1` Legal records, evidence, medical records, and financial records in QiDrive are protected and governed by enhanced retention rules. (`Sec. 15.06.010.L001`; stable ID `T15.A06.S010.L001`)
- `Line 2` Protected records must not be deleted, renamed, or moved without an explicit governance decision. (`Sec. 15.06.010.L002`; stable ID `T15.A06.S010.L002`)
- `Line 3` Protected records must carry `sensitivity: confidential` or higher in their frontmatter or folder-level policy. (`Sec. 15.06.010.L003`; stable ID `T15.A06.S010.L003`)

## Article 7. Archive and Retention

Stable ID: `T15.A07`

### Sec. 15.07.010. Archive Policy

Stable ID: `T15.A07.S010`

- `Line 1` Archived material must be moved to a clearly labeled archive folder; delete is not acceptable for source-of-truth material. (`Sec. 15.07.010.L001`; stable ID `T15.A07.S010.L001`)
- `Line 2` Retention periods for protected records must be documented and respected. (`Sec. 15.07.010.L002`; stable ID `T15.A07.S010.L002`)
- `Line 3` Archive actions must be logged in the domain's changelog or a migration record. (`Sec. 15.07.010.L003`; stable ID `T15.A07.S010.L003`)

## Cross References

- [QiCode Index](../_index.md)
- [Title 10 — QiLabs](../title_10_qilabs/title_10_qilabs.md)
- [Migration Map](../reference/qilabs_title_migration_map.md)
