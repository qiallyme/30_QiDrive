---
layout: adr
title: ADR-0005: Hosted Fleet Orchestration with Enrolled Edge Nodes
slug: adr-0005-hosted-fleet-orchestration-with-enrolled-edge-nodes
status: publish
updated_at: "2026-06-29"
tags:
  - qispark
  - decisions
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

# ADR-0005: Hosted Fleet Orchestration with Enrolled Edge Nodes

## Context

The documentation previously outlined a "Local Admin Control Plane" consisting of a local fastAPI server running on the developer workstation directing jobs and controlling files. As the system scales to ingest files and run jobs across multiple nodes, keeping the control plane tied to the individual local machine becomes an operational bottleneck and architectural flaw.

## Decision

* **Hosted Admin** is the singular orchestration authority and fleet control plane.
* **Local Nodes** are redefined as agents/runtimes for execution only, not as orchestration centers.
* Devices are conceptually "enrolled". Devices ingest data strictly from their assigned paths or a drop zone.
* All promoted records must still enter the system through explicitly governed `QiArchive` processes.
* Local APIs are strictly internal agent execution endpoints, no longer the primary administration control plane.

## Rationale

This establishes a cleaner separation of concerns. The server-side Admin dictates jobs, configurations, and fleet monitoring, whilst multiple generic edge nodes simply report health and ingest content from their given assignments. This formalizes a master/worker "control model flip", solving discrepancies between the local-control phrasing and the actual fleet needs.
