---
layout: page
title: Context Pack
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

# AI Context Pack

## Project

QiFinance is a personal/gig-worker finance app with double-entry accounting under the hood.

## Current Priority

Build infrastructure and ledger core without locking the app to Cody-only usage.

## Architecture Rules

- Workspace ownership from day one
- Splits first-class
- Supabase source of truth
- No localStorage for durable finance data
- Manual-first MVP
- Auth later but not blocked by current design

## Product Voice

Plainspoken, practical, financially honest.

## Avoid

- QuickBooks clone thinking
- Budget app fluff
- Hardcoded user assumptions
- Schema before infrastructure
