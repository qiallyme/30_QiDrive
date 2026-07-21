---
layout: page
type: index
title: Inbox Dashboard
slug: inbox-dashboard
summary: Unprocessed captures and recently added inbox material.
status: active
visibility: internal
publish_target: none
publish_url: ""
created_at: "2026-07-16"
updated_at: "2026-07-18T11:03:10-04:00"
author: Cody J. Rice-Velasquez
owner: Cody
nav_title: Inbox
nav_group: dashboards
nav_order: 10
nav_hidden: false
is_index: true
parent_ref: "[[00_home]]"
sensitivity: internal
classification: business_internal
realm_label: ""
tags: [dashboard, inbox]
keywords: [inbox, capture, processing]
aliases: []
context: ""
uid: dc690d7c81284b94b348b5c75fd3e3e3
canonical_ref: ""
source_type: manual
template_key: master-template
index_scope: ""
generated_by: ""
generated_at: ""
---

# Inbox Dashboard

```dataview
TABLE WITHOUT ID file.link AS Item, file.folder AS Folder, file.ctime AS Added, file.mtime AS Updated
FROM "01_inbox"
WHERE file.name != "_index"
SORT file.mtime DESC
LIMIT 50
```

## Processing rule

For each item: delete obvious junk, connect it to an existing note, move it to the correct durable space, or turn it into a project/task. The inbox is a landing zone, not permanent storage.
