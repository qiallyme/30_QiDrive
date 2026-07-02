---
layout: page
title: QiServer
slug: qiserver
status: active
updated_at: "2026-06-29"
tags:
  - qispark
source_type: manual
summary: ""
created_at: ""
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
template_key: master-template
---

# QiServer

## Overview

QiServer is the protected runtime host for internal services. It contains live Docker Compose stacks, system services, private access routes, public restricted routes, and runtime configuration paths.

Verified runtime facts win over repo planning notes.

## Responsibilities

- Host protected runtime services.
- Keep runtime stack paths and service facts clear.
- Separate public restricted access from private-only access.
- Run Docker Compose stacks and systemd services.
- Verify local, tailnet, and public routes after changes.

## Flows

```text
Inspect qiserver
  -> confirm repo, branch, remote, stack, ports, and working tree
  -> pull only from the confirmed repo
  -> back up runtime config before overwriting
  -> deploy or restart only the needed stack
  -> verify routes
```

## Folder Structure & Table of Contents

### Primary Documents

- [Service Map](10_qispark/01_QiInfra-Global/20_QiServer/Service_Map.md): Configuration mappings, ports, and route definitions for services.
- [QiServer Runbook](10_qispark/01_QiInfra-Global/20_QiServer/qiserver_runbook.md): Manual procedures, commands, and backup/restore steps.
- [Runtime Environment](10_qispark/01_QiInfra-Global/20_QiServer/runtime.md): Paths, locations, and setup details for runtime containers.
- [Runtime Profile](10_qispark/01_QiInfra-Global/20_QiServer/runtime_profile.md): Hardware, specs, and environment facts of host servers.
