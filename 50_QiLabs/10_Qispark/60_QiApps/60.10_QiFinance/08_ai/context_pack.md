---
layout: page
title: Context Pack
slug: context-pack
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
uid: bc28e2ab2589477ebe103008589bc0bb
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
