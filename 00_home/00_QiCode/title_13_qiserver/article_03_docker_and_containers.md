---
layout: article
title: Article 3. Docker and Containers
slug: qicode-title-13-article-03-docker-and-containers
summary: ""
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
qicode_title: 13
qicode_article: 3
parent_title: Title 13. QiServer
canonical_ref: QiCode T13.A03
source_type: manual
---

## Article 3. Docker and Containers

Stable ID: `T13.A03`

### Sec. 13.03.010. Container Governance

Stable ID: `T13.A03.S010`

- `Line 1` All containerized services must be defined in version-controlled Docker Compose files. (`Sec. 13.03.010.L001`; stable ID `T13.A03.S010.L001`)
- `Line 2` Container configurations must not include secrets inline; use environment files or secrets managers. (`Sec. 13.03.010.L002`; stable ID `T13.A03.S010.L002`)
- `Line 3` Portainer manages container state; Portainer itself is governed by QiServer. (`Sec. 13.03.010.L003`; stable ID `T13.A03.S010.L003`)


