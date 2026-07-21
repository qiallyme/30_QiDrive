---
layout: article
title: Article 6. Build Artifacts
slug: qicode-title-18-article-06-build-artifacts
summary: ""
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
qicode_title: 18
qicode_article: 6
parent_title: Title 18. QiSites
canonical_ref: QiCode T18.A06
source_type: manual
---

## Article 6. Build Artifacts

Stable ID: `T18.A06`

### Sec. 18.06.010. Artifact Policy

Stable ID: `T18.A06.S010`

- `Line 1` Build artifacts (HTML, CSS, JS bundles) in `70_QiSites` are treated as derived content and may be regenerated. (`Sec. 18.06.010.L001`; stable ID `T18.A06.S010.L001`)
- `Line 2` Do not commit sensitive data, API keys, or personal records inside build artifacts. (`Sec. 18.06.010.L002`; stable ID `T18.A06.S010.L002`)
- `Line 3` If artifact content diverges from source, the source governs; rebuild, do not patch the artifact. (`Sec. 18.06.010.L003`; stable ID `T18.A06.S010.L003`)


