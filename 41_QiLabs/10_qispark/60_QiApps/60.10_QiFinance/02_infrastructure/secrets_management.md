---
layout: page
title: Secrets Management
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
