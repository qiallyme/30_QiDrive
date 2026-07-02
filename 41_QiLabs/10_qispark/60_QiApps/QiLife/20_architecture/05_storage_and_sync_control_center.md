---
layout: page
title: Storage and Sync Control Center
slug: storage-and-sync-control-center
status: active
updated_at: "2026-06-29"
tags:
  - qispark
source_type: manual
summary: ""
created_at: ""
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
template_key: master-template
---

# Storage and Sync Control Center
QiLife must eliminate manual file/folder management.

The app manages:
- local data root
- blob/file root
- Drive/QiNexus mirror folder
- server connection
- database mode
- sync mode
- backup/export status
- storage health

## Default Locations

- Repo/code: C:\QiLabs\60_QiApps\_qilife
- Private data: C:\QiLifeData
- SQLite DB: C:\QiLifeData\db\qilife.sqlite
- File vault: C:\QiLifeData\files
- Exports/backups: C:\QiLifeData\exports and C:\QiLifeData\backups

## Storage Doctrine

- Code repo is not data.
- Database is structured truth.
- Blob store holds raw files.
- Drive/QiNexus is mirror/export/archive.
- Folders are projections of metadata, not the source of truth.
- Buckets are metadata/views inside QiLife.
