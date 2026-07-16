---
layout: page
title: System Overview
slug: ""
summary: ""
status: publish
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

# System Overview

## Primary Flow

1. User creates or imports a transaction.
2. App builds split lines.
3. Ledger validator checks balance.
4. Data is saved to Supabase.
5. Dashboard and reports derive from splits.

## Design Intent

Reports should not rely on duplicated summary data unless cached. The ledger is the truth.
