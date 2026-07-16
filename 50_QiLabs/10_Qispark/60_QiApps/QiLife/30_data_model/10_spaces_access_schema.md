---
layout: page
title: Spaces & Access Schema
slug: spaces-access-schema
status: publish
updated_at: "2026-07-16T06:49:40-04:00"
tags: []
  - qispark
source_type: manual
summary: ""
created_at: "2026-07-16T06:19:39-04:00"
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: dca015fd4c9f41b1884a7d9210f75656
canonical_ref: ""
template_key: master-template
---

# Spaces & Access Schema
QiLife supports scoped shared access via Spaces.

## Planned Tables

- `spaces`
- `space_members`
- `share_events`

## Major Record Fields

- `space_id`
- `visibility` (private, space_visible, restricted, archived)
- `created_by_person_id`

Mom Care acts as a scoped shared space, not a full EMR. Keep it simple: lightweight buckets, date/time notes, optional archive, and Cody-approved sharing from private records to Care Notes.
