---
layout: page
title: 06 Spaces And Scoped Access
slug: 06-spaces-and-scoped-access
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
uid: 07a9faf82bd3488392086f371a52177a
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Spaces and Scoped Access
QiLife is Cody-private by default but must support scoped shared spaces.

## Doctrine
- Cody Private is the default space. Nothing is shared by default.
- Mom Care is a scoped shared space/portal, not a separate app.
- Same backend, different access scope and UI.
- Mom should only see records explicitly assigned/shared to Mom Care.
- Private raw QiBits can generate cleaned shared Care Notes, but Cody must approve sharing.

## Default Spaces
- Cody Private
- Mom Care
- Household

## Visibility Values
- private
- space_visible
- restricted
- archived

## Roles
- owner, contributor, viewer, guest

For local dev: use mock user/space switcher; no full auth yet.
