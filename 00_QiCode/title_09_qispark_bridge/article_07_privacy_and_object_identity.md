---
layout: article
title: Article 7. Privacy and Object Identity
status: publish
doctrine_status: active
qicode_title: 09
qicode_article: 7
canonical_ref: QiCode T09.A07
updated_at: "2026-07-29"
tags: [qicode, privacy, objects, identity]
source_type: manual
---

## Article 7. Privacy and Object Identity

### Sec. 9.07.010. Privacy and Separation

Stable ID: `QIC-09-07-001` (`T09.A07.S010`)

Public code and doctrine do not contain private user records. Private data
remains owner-scoped. Secrets are separated from searchable records and
ordinary AI context. Exports and logs respect sensitivity classifications.

### Sec. 9.07.020. Universal Object Identity

Stable ID: `QIC-09-07-002` (`T09.A07.S020`)

A persistent thing receives a stable internal object identity independent of
identifiers issued by providers. Provider identifiers never replace canonical
internal identity.

### Sec. 9.07.030. Object Evidence and Relationships

Stable ID: `QIC-09-07-003` (`T09.A07.S030`)

Object identifiers, relationships, history, and source evidence remain
separate records linked by stable internal IDs. Human-readable titles may be
resolved for display without replacing those IDs.

### Sec. 9.07.040. Secret References

Stable ID: `QIC-09-07-004` (`T09.A07.S040`)

Systems record where access material is protected, not the plaintext secret.
Secret references and sensitive identifier values are excluded from ordinary
AI context unless a specifically approved workflow requires them.
