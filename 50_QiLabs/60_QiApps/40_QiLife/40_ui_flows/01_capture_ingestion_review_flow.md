---
layout: page
title: 01 Capture Ingestion Review Flow
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

# Capture, Ingestion, and Review Flow

The first real working pipeline for QiLife is:
Capture → Ingestion Item → File/Text Extraction → Mock AI Draft → Draft Review → Approval/Edit/Reject → Official QiBit/Action/Thread → Timeline → Activity Log → Context Dock / Retrieval hooks

## Doctrine
- Raw capture is sacred.
- AI interpretation is draft until approved or trusted.
- Approval/edit/rejection must be logged.
- Future trust rules can auto-approve low-risk guesses.
- High-risk areas (money, legal, medical, deletion, messaging) require review.
