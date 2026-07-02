---
layout: page
title: Authorization Strategy
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

# Authorization Strategy

## MVP

Application-level separation using `workspace_id` and `user_id` fields.

## Product

Supabase Row-Level Security.

## Rule

RLS policies should eventually enforce:

- User can access workspaces where they are a member.
- User can only mutate records in allowed workspaces.
- Demo workspace can be reset safely.
