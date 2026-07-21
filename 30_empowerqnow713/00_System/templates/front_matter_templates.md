---
title: Front Matter Templates
section: 01_Q/99_system
access_level: L1
visibility: private
ai_ingest: true
status: active
last_updated: 2026-05-24
layout: page
slug: front-matter-templates
summary: ""
created_at: "2026-07-16T06:19:39-04:00"
updated_at: "2026-07-18T11:03:16-04:00"
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: 473c2245285e4d999b4ca1016da0ce4f
canonical_ref: ""
source_type: manual
template_key: master-template
type: note
---

# Front Matter Templates

## Standard File

```yaml
---
title:
section: 01_Q/
category:
access_level: L2
visibility: private
ai_ingest: true
shareable: conditional
status: draft
created: 2026-05-24
last_updated: 2026-05-24
related: []
tags:
---
```

## Clinical / Sensitive File

```yaml
---
title:
section: 01_Q/30_clinical
category: clinical
access_level: L3
visibility: restricted
ai_ingest: conditional
shareable: provider_only
status: draft
created: 2026-05-24
last_updated: 2026-05-24
related: []
tags:
---
```

## Locked File

```yaml
---
title:
section: 01_Q/90_locked
category: locked
access_level: L4
visibility: locked
ai_ingest: false
shareable: never
status: raw
created: 2026-05-24
last_updated: 2026-05-24
warning: my_eyes_only
related: []
tags:
---
```

## Sealed File

```yaml
---
title:
section: 01_Q/90_locked
category: sealed
access_level: L5
visibility: sealed
ai_ingest: false
shareable: never
status: restricted
created: 2026-05-24
last_updated: 2026-05-24
rule: no_processing_without_explicit_case_by_case_permission
related: []
tags:
---
```
