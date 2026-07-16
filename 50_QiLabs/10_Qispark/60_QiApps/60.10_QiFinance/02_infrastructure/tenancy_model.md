---
layout: page
title: Tenancy Model
slug: tenancy-model
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
uid: 6860703e590c4cb6a1238a901fdd3f50
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Tenancy Model

## Early Model

Use static IDs until auth exists:

```text
workspace_id = default
user_id = cody
```

## Future Model

```text
Workspace
  └── Members
      └── Profiles
          └── Accounts
          └── Transactions
```

## Rule

Every durable user-owned record should include `workspace_id`.
