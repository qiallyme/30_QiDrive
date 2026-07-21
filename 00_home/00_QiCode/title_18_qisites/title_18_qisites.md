---
layout: section
title: Title 18. QiSites
slug: qicode-title-18-qisites
summary: QiSites governs 70_QiSites — public and static site output targets for the QiLabs system.
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
  - qilabs
source_type: manual
---

# Title 18. QiSites

## Citation

- Legal citation: `QiCode Title 18`
- Article citation: `QiCode Title 18, Article #`
- Section citation: `QiCode Sec. 18.##.###`
- Stable ID alias: `QiCode T18.A##.S###.L###`

## Rule of Construction

- `Rule 18.001.L001` This title governs `70_QiSites` — public and static site output for QiLabs. (stable ID `T18.R001.L001`)
- `Rule 18.001.L002` A section states a governing principle; a line states a citeable rule or application. (stable ID `T18.R001.L002`)
- `Rule 18.001.L003` Exceptions must be named, reviewed, and linked to the record that justifies them. (stable ID `T18.R001.L003`)

## Article 1. QiSites Purpose

Stable ID: `T18.A01`

### Sec. 18.01.010. Primary Function

Stable ID: `T18.A01.S010`

- `Line 1` QiSites holds static and public site output: the deployable artifacts produced by QiSpark or QiApps builds. (`Sec. 18.01.010.L001`; stable ID `T18.A01.S010.L001`)
- `Line 2` QiSites is output-only; it does not hold source material, vault content, or live databases. (`Sec. 18.01.010.L002`; stable ID `T18.A01.S010.L002`)
- `Line 3` If use is ambiguous, the placement rule for the nearest parent title controls. (`Sec. 18.01.010.L003`; stable ID `T18.A01.S010.L003`)

### Sec. 18.01.020. Source and Output Distinction

Stable ID: `T18.A01.S020`

- `Line 1` Source markdown for public sites lives in QiSpark (docs) or QiApps (landing); `70_QiSites` holds the build output only. (`Sec. 18.01.020.L001`; stable ID `T18.A01.S020.L001`)
- `Line 2` Modifying built files directly inside `70_QiSites` is not permitted; changes must come from the source layer. (`Sec. 18.01.020.L002`; stable ID `T18.A01.S020.L002`)
- `Line 3` Build outputs must be clearly separated from source files in `git` history. (`Sec. 18.01.020.L003`; stable ID `T18.A01.S020.L003`)

## Article 2. Deployment

Stable ID: `T18.A02`

### Sec. 18.02.010. Deployment Targets

Stable ID: `T18.A02.S010`

- `Line 1` Sites in `70_QiSites` are deployed to Cloudflare Pages, GitHub Pages, or equivalent governed static hosting. (`Sec. 18.02.010.L001`; stable ID `T18.A02.S010.L001`)
- `Line 2` Each site must have a documented deployment target, custom domain (if any), and CI/CD configuration. (`Sec. 18.02.010.L002`; stable ID `T18.A02.S010.L002`)
- `Line 3` Deployment must be automated; manual uploads are not a governed deployment method. (`Sec. 18.02.010.L003`; stable ID `T18.A02.S010.L003`)

## Article 3. Privacy and Sensitivity

Stable ID: `T18.A03`

### Sec. 18.03.010. Public Boundary

Stable ID: `T18.A03.S010`

- `Line 1` Only material explicitly approved for public publishing may enter `70_QiSites`. (`Sec. 18.03.010.L001`; stable ID `T18.A03.S010.L001`)
- `Line 2` The build pipeline must enforce sensitivity filtering; `sensitivity: internal` or higher must not pass through. (`Sec. 18.03.010.L002`; stable ID `T18.A03.S010.L002`)
- `Line 3` A published file must be traceable back to its source and its sensitivity review. (`Sec. 18.03.010.L003`; stable ID `T18.A03.S010.L003`)

## Article 4. Site Inventory

Stable ID: `T18.A04`

### Sec. 18.04.010. Site Registry

Stable ID: `T18.A04.S010`

- `Line 1` A site registry document in `70_QiSites` must list all active public sites, their domains, and their source. (`Sec. 18.04.010.L001`; stable ID `T18.A04.S010.L001`)
- `Line 2` Decommissioned sites must be documented in the registry with a retirement date and redirect policy. (`Sec. 18.04.010.L002`; stable ID `T18.A04.S010.L002`)
- `Line 3` Sites with overlapping content must have a documented reason for the overlap or must be consolidated. (`Sec. 18.04.010.L003`; stable ID `T18.A04.S010.L003`)

## Article 5. EmpowerQNow

Stable ID: `T18.A05`

### Sec. 18.05.010. EmpowerQNow Site Governance

Stable ID: `T18.A05.S010`

- `Line 1` EmpowerQNow public site output lives in `70_QiSites/empowerqnow` and is governed by this title. (`Sec. 18.05.010.L001`; stable ID `T18.A05.S010.L001`)
- `Line 2` EmpowerQNow content follows the public boundary policy in Sec. 18.03.010. (`Sec. 18.05.010.L002`; stable ID `T18.A05.S010.L002`)
- `Line 3` Teaching and empowerment content must return power to the reader in alignment with QiCode T01.A03. (`Sec. 18.05.010.L003`; stable ID `T18.A05.S010.L003`)

## Article 6. Build Artifacts

Stable ID: `T18.A06`

### Sec. 18.06.010. Artifact Policy

Stable ID: `T18.A06.S010`

- `Line 1` Build artifacts (HTML, CSS, JS bundles) in `70_QiSites` are treated as derived content and may be regenerated. (`Sec. 18.06.010.L001`; stable ID `T18.A06.S010.L001`)
- `Line 2` Do not commit sensitive data, API keys, or personal records inside build artifacts. (`Sec. 18.06.010.L002`; stable ID `T18.A06.S010.L002`)
- `Line 3` If artifact content diverges from source, the source governs; rebuild, do not patch the artifact. (`Sec. 18.06.010.L003`; stable ID `T18.A06.S010.L003`)

## Article 7. Custom Domains

Stable ID: `T18.A07`

### Sec. 18.07.010. Domain Policy

Stable ID: `T18.A07.S010`

- `Line 1` Custom domains for QiSites must be registered in the QiSpark domain registry. (`Sec. 18.07.010.L001`; stable ID `T18.A07.S010.L001`)
- `Line 2` DNS changes must be documented before they are applied. (`Sec. 18.07.010.L002`; stable ID `T18.A07.S010.L002`)
- `Line 3` Expired or abandoned domains must be retired from the site registry and from active DNS. (`Sec. 18.07.010.L003`; stable ID `T18.A07.S010.L003`)

## Cross References

- [QiCode Index](../_index.md)
- [Title 10 — QiLabs](../title_10_qilabs/title_10_qilabs.md)
- [Title 12 — QiSpark](../title_12_qispark/title_12_qispark.md)
- [Migration Map](../reference/qilabs_title_migration_map.md)
