---
layout: page
title: Schema
slug: schema
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
uid: bb6fbe4c66e546b2a48eec61875a365b
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Schema

## Overview

`Schema/` describes QiOS domains, entities, relationships, flows, and boundaries while distinguishing intent from verified implementation.

## Responsibilities

- Define shared system concepts.
- Link detailed schemas from their owning domain.
- Mark proposed structures as proposed.
- Avoid duplicating migrations or runtime configuration.

## Current Model

```text
QiAccess -> QiLife -> (QiSystem + QiNexus + QiCapture + QiConnect)
                         |
                      QiServer
```
