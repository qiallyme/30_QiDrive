---
layout: page
title: Index.infrastructure
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
