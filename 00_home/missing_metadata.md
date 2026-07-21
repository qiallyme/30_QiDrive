---
layout: page
type: index
title: Missing Metadata
slug: missing-metadata
summary: Review notes missing the minimum master-template properties.
status: active
visibility: internal
publish_target: none
publish_url: ""
created_at: "2026-07-16"
updated_at: "2026-07-18T11:03:10-04:00"
author: Cody J. Rice-Velasquez
owner: Cody
nav_title: Missing Metadata
nav_group: system
nav_order: 90
nav_hidden: true
is_index: true
parent_ref: "[[00_home]]"
sensitivity: internal
classification: business_internal
realm_label: ""
tags: [dashboard, metadata]
keywords: []
aliases: []
context: ""
uid: 7c80e0343f2a4219b0cf8a87c6dcb955
canonical_ref: ""
source_type: manual
template_key: master-template
index_scope: ""
generated_by: ""
generated_at: ""
---

# Missing Metadata

```dataview
TABLE WITHOUT ID file.link AS Note, file.folder AS Folder, type AS Type, status AS Status, file.mtime AS Updated
FROM ""
WHERE !contains(file.path, ".obsidian/")
  AND !contains(file.path, ".trash/")
  AND (!layout OR !type OR !title OR !status OR !source_type OR !template_key)
SORT file.mtime DESC
LIMIT 200
```

Use the housekeeping console’s preview mode before applying bulk normalization.
