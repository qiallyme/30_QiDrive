---
layout: page
title: Secrets Management
slug: secrets-management
summary: ""
status: active
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
uid: eec24c09eada4762afdd8e17369fd9e2
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Secrets Management

## Rules

- Never commit `.env` files.
- Document required variables in `.env.example`.
- Use platform secrets for deployment.
- Rotate keys if exposed.

## Expected Secrets

- Supabase URL
- Supabase anon key
- Supabase service role key for server-only operations
- Future AI provider keys
- Future bank provider keys
