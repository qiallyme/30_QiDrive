---
layout: page
title: Index.infrastructure
slug: index-infrastructure
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
uid: 2fea4ec5fadb4832b887ec4d336d1ed6
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Infrastructure Overview

QiFinance infrastructure should support single-user development now and multi-user operation later without a rewrite.

## Current Target

- Frontend: web app
- Backend: Supabase/Postgres
- Auth: deferred, but ownership fields included now
- Hosting: Cloudflare Pages or equivalent
- Storage: Supabase storage later for receipts/files

## Core Rule

No record should assume Cody is the only possible user.
