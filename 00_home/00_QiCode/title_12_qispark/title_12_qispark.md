---
layout: section
title: Title 12. QiSpark
slug: qicode-title-12-qispark
summary: QiSpark is the docs, landing, doctrine, map, and navigation layer for the QiLabs system.
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
  - qilabs
source_type: manual
---

# Title 12. QiSpark

## Citation

- Legal citation: `QiCode Title 12`
- Article citation: `QiCode Title 12, Article #`
- Section citation: `QiCode Sec. 12.##.###`
- Stable ID alias: `QiCode T12.A##.S###.L###`

## Rule of Construction

- `Rule 12.001.L001` This title governs `10_Qispark` as the docs, landing, doctrine, and navigation layer. (stable ID `T12.R001.L001`)
- `Rule 12.001.L002` A section states a governing principle; a line states a citeable rule or application. (stable ID `T12.R001.L002`)
- `Rule 12.001.L003` Exceptions must be named, reviewed, and linked to the record that justifies them. (stable ID `T12.R001.L003`)

## Article 1. QiSpark Purpose

Stable ID: `T12.A01`

### Sec. 12.01.010. Primary Function

Stable ID: `T12.A01.S010`

- `Line 1` QiSpark is the docs and landing layer: it explains, maps, and routes between QiLabs domains. (`Sec. 12.01.010.L001`; stable ID `T12.A01.S010.L001`)
- `Line 2` QiSpark must not operate life data; it navigates and documents, it does not store personal records. (`Sec. 12.01.010.L002`; stable ID `T12.A01.S010.L002`)
- `Line 3` If use is ambiguous, the placement rule for the nearest parent title controls. (`Sec. 12.01.010.L003`; stable ID `T12.A01.S010.L003`)

### Sec. 12.01.020. Scope

Stable ID: `T12.A01.S020`

- `Line 1` QiSpark may include the homepage, navigation bookmarks, and the QiDNA doctrine content layer. (`Sec. 12.01.020.L001`; stable ID `T12.A01.S020.L001`)
- `Line 2` QiDNA is doctrine content inside QiSpark docs, not a separate system or module. (`Sec. 12.01.020.L002`; stable ID `T12.A01.S020.L002`)
- `Line 3` QiAccess is retired as a standalone module; its navigation function is absorbed into QiSpark. (`Sec. 12.01.020.L003`; stable ID `T12.A01.S020.L003`)

## Article 2. Landing Page

Stable ID: `T12.A02`

### Sec. 12.02.010. Homepage Rule

Stable ID: `T12.A02.S010`

- `Line 1` The QiLabs homepage or navigation hub is a QiSpark output, not a QiApps product. (`Sec. 12.02.010.L001`; stable ID `T12.A02.S010.L001`)
- `Line 2` The homepage routes to governed domains; it does not duplicate content owned by other titles. (`Sec. 12.02.010.L002`; stable ID `T12.A02.S010.L002`)
- `Line 3` Homepage decisions must be documented in QiSpark ADRs or equivalent. (`Sec. 12.02.010.L003`; stable ID `T12.A02.S010.L003`)

## Article 3. Documentation Structure

Stable ID: `T12.A03`

### Sec. 12.03.010. Docs Hierarchy

Stable ID: `T12.A03.S010`

- `Line 1` QiSpark docs are organized as: Policies → Rules and Standards → Registries → Schemas → Decisions (ADRs). (`Sec. 12.03.010.L001`; stable ID `T12.A03.S010.L001`)
- `Line 2` Each layer governs a different level of abstraction and must not be used as a dump for the other. (`Sec. 12.03.010.L002`; stable ID `T12.A03.S010.L002`)
- `Line 3` Duplicate docs in the legacy source are not migrated; only the canonical version is authoritative. (`Sec. 12.03.010.L003`; stable ID `T12.A03.S010.L003`)

## Article 4. QiDNA and Doctrine

Stable ID: `T12.A04`

### Sec. 12.04.010. QiDNA is Doctrine Content

Stable ID: `T12.A04.S010`

- `Line 1` QiDNA refers to the core doctrine, principles, and identity narrative content housed within QiSpark documentation. (`Sec. 12.04.010.L001`; stable ID `T12.A04.S010.L001`)
- `Line 2` QiDNA must not be treated as a separate module, folder domain, or deployment target. (`Sec. 12.04.010.L002`; stable ID `T12.A04.S010.L002`)
- `Line 3` QiCode Titles 01–09 are the canonical personal doctrine; QiSpark/QiDNA extends this into the technical/system layer. (`Sec. 12.04.010.L003`; stable ID `T12.A04.S010.L003`)

## Article 5. Publishing Rules

Stable ID: `T12.A05`

### Sec. 12.05.010. Public vs. Private

Stable ID: `T12.A05.S010`

- `Line 1` QiSpark content that is published publicly must pass a sensitivity review before deployment. (`Sec. 12.05.010.L001`; stable ID `T12.A05.S010.L001`)
- `Line 2` Private doctrine, personal records, legal material, and evidence must not be included in any QiSpark public build. (`Sec. 12.05.010.L002`; stable ID `T12.A05.S010.L002`)
- `Line 3` The `sensitivity` frontmatter field governs inclusion; files marked `internal` or higher must not be published. (`Sec. 12.05.010.L003`; stable ID `T12.A05.S010.L003`)

## Article 6. Public and Private Boundary

Stable ID: `T12.A06`

### Sec. 12.06.010. Boundary Definition

Stable ID: `T12.A06.S010`

- `Line 1` The public boundary is the set of docs that can be shipped in a static site or accessible via a public URL. (`Sec. 12.06.010.L001`; stable ID `T12.A06.S010.L001`)
- `Line 2` Everything inside `40_QiVault`, `30_QiDrive`, and protected case folders is private by default. (`Sec. 12.06.010.L002`; stable ID `T12.A06.S010.L002`)
- `Line 3` Explicit `publish_target` in frontmatter is required to move a file across the public boundary. (`Sec. 12.06.010.L003`; stable ID `T12.A06.S010.L003`)

## Article 7. Build and Deployment

Stable ID: `T12.A07`

### Sec. 12.07.010. Build Rules

Stable ID: `T12.A07.S010`

- `Line 1` QiSpark sites are built with static site tooling; the build target is separate from the source vault. (`Sec. 12.07.010.L001`; stable ID `T12.A07.S010.L001`)
- `Line 2` Build outputs belong in `70_QiSites`; do not commit build artifacts into the source docs. (`Sec. 12.07.010.L002`; stable ID `T12.A07.S010.L002`)
- `Line 3` Deployment decisions must be documented in QiSpark ADRs or equivalent. (`Sec. 12.07.010.L003`; stable ID `T12.A07.S010.L003`)

## Cross References

- [QiCode Index](../_index.md)
- [Title 10 — QiLabs](../title_10_qilabs/title_10_qilabs.md)
- [Migration Map](../reference/qilabs_title_migration_map.md)
