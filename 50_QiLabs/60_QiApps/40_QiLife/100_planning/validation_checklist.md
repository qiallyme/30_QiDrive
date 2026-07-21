---
layout: page
title: Validation Checklist
slug: validation-checklist
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
uid: 3ecc03f4a7fc44d1907f5df7f90f70c2
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Validation Checklist

## Vertical Slice 1: Capture to Timeline
- [ ] Can capture raw text/files in the UI?
- [ ] Is it saved as an ingestion item in the DB?
- [ ] Does it trigger a Mock AI Draft?
- [ ] Can the draft be reviewed in the UI?
- [ ] Can the draft be approved/edited/rejected?
- [ ] Does approval create an official QiBit and Timeline entry?
- [ ] Are all actions logged in the `activity_log`?

## Storage and Dedupe
- [ ] Are uploaded files hashed?
- [ ] Does the system block exact duplicate blobs?
- [ ] Are files stored in the managed file vault (not raw repo)?

## Spaces
- [ ] Does data default to Cody Private?
- [ ] Can an item be shared to the Mom Care space?
- [ ] Is visibility correctly scoped by space selection?
