---
layout: page
type: index
title: Timeline Dashboard
slug: timeline-dashboard
summary: Curated entry point for canonical events and chronological review.
status: active
visibility: internal
publish_target: none
publish_url: ""
created_at: "2026-07-16"
updated_at: "2026-07-16"
author: Cody J. Rice-Velasquez
owner: Cody
nav_title: Timeline
nav_group: dashboards
nav_order: 30
nav_hidden: false
is_index: true
parent_ref: "[[00_home]]"
sensitivity: internal
classification: business_internal
realm_label: ""
tags: [dashboard, timeline]
keywords: [timeline, events, chronology]
aliases: []
context: ""
uid: ""
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Timeline Dashboard

> [!info] Timeline rule
> The curated timeline uses `type: event`, `timeline_include: true`, and `canonical: true`. Imported or duplicate records remain searchable without competing as equal events.

## Canonical events

```dataview
TABLE WITHOUT ID date AS Date, file.link AS Event, event_type AS Type, people AS People, significance AS Significance
FROM "10_daily"
WHERE type = "event" AND timeline_include = true AND canonical = true
SORT date DESC
LIMIT 40
```

## Events awaiting review

```dataview
TABLE WITHOUT ID date AS Date, file.link AS Event, category AS "Legacy category", involved AS "Legacy people"
FROM "10_daily"
WHERE type = "event" AND (timeline_status = "unreviewed" OR !timeline_status)
SORT date DESC
LIMIT 40
```

## Timeline views

- Open **Vault Timeline** for broad chronological exploration.
- Open the `Markwhen/` folder for intentionally curated presentation timelines.
- Use this dashboard for trustworthy canonical history.
