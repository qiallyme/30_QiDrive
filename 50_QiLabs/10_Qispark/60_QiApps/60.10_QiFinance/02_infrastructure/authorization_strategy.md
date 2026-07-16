---
layout: page
title: Authorization Strategy
slug: authorization-strategy
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
uid: 4e13eab4da1b45c7b46987967a51e644
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
