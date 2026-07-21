---
layout: article
title: Article 4. Databases
slug: qicode-title-13-article-04-databases
summary: ""
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
qicode_title: 13
qicode_article: 4
parent_title: Title 13. QiServer
canonical_ref: QiCode T13.A04
source_type: manual
---

## Article 4. Databases

Stable ID: `T13.A04`

### Sec. 13.04.010. Database Authority

Stable ID: `T13.A04.S010`

- `Line 1` Local databases hosted on QiServer (Neo4j, Qdrant, Firefly III DB, BookStack DB, SolidTime DB) are governed by QiServer doctrine for access, backups, and migrations. (`Sec. 13.04.010.L001`; stable ID `T13.A04.S010.L001`)
- `Line 2` Supabase is a cloud-hosted SaaS database and is the canonical data authority for QiLife and connected apps; it is NOT hosted on QiServer â€” QiServer connects to it remotely (ADR-0018). (`Sec. 13.04.010.L002`; stable ID `T13.A04.S010.L002`)
- `Line 3` Directus is the admin UI and API layer for Supabase/Postgres per ADR-0019; NocoDB is deprecated and scheduled for decommissioning. Schema changes must be versioned migration scripts, not Directus-panel edits. (`Sec. 13.04.010.L003`; stable ID `T13.A04.S010.L003`)


