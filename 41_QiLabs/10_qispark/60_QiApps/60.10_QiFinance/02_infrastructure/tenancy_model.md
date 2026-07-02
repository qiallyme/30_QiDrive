---
layout: page
title: Tenancy Model
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
