---
layout: page
title: Rls
slug: ""
summary: ""
status: active
created_at: ""
updated_at: ""
author: ""
owner: ""
tags: []
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
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
