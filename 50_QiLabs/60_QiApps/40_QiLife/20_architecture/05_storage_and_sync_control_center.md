---
layout: page
title: 05 Storage And Sync Control Center
slug: 05-storage-and-sync-control-center
summary: ""
status: publish
created_at: "2026-07-16T06:19:39-04:00"
updated_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: b7798210c1594a77841e9e4815de758b
canonical_ref: ""
source_type: manual
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
