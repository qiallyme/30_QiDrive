---
layout: article
title: Article 6. Public and Private Boundary
slug: qicode-title-12-article-06-public-and-private-boundary
summary: ""
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
qicode_title: 12
qicode_article: 6
parent_title: Title 12. QiSpark
canonical_ref: QiCode T12.A06
source_type: manual
---

## Article 6. Public and Private Boundary

Stable ID: `T12.A06`

### Sec. 12.06.010. Boundary Definition

Stable ID: `T12.A06.S010`

- `Line 1` The public boundary is the set of docs that can be shipped in a static site or accessible via a public URL. (`Sec. 12.06.010.L001`; stable ID `T12.A06.S010.L001`)
- `Line 2` Everything inside `40_QiVault`, `30_QiDrive`, and protected case folders is private by default. (`Sec. 12.06.010.L002`; stable ID `T12.A06.S010.L002`)
- `Line 3` Explicit `publish_target` in frontmatter is required to move a file across the public boundary. (`Sec. 12.06.010.L003`; stable ID `T12.A06.S010.L003`)


