---
layout: page
title: Rls
slug: rls
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
uid: 6e5cab15cef546adb8d97a5f58d12f51
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Row-Level Security

## MVP

RLS may be disabled during local development.

## Product Requirement

All workspace-owned records require policies limiting access to workspace members.

## Policy Pattern

```text
record.workspace_id IN user_authorized_workspaces
```
