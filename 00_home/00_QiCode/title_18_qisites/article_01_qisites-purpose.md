---
layout: article
title: Article 1. QiSites Purpose
slug: qicode-title-18-article-01-qisites-purpose
summary: ""
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
qicode_title: 18
qicode_article: 1
parent_title: Title 18. QiSites
canonical_ref: QiCode T18.A01
source_type: manual
---

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


