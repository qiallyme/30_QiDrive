---
layout: page
type: index
title: Projects Dashboard
slug: projects-dashboard
summary: Active projects, priorities, and next actions.
status: active
visibility: internal
publish_target: none
publish_url: ""
created_at: "2026-07-16"
updated_at: "2026-07-16"
author: Cody J. Rice-Velasquez
owner: Cody
nav_title: Projects
nav_group: dashboards
nav_order: 20
nav_hidden: false
is_index: true
parent_ref: "[[00_home]]"
sensitivity: internal
classification: business_internal
realm_label: ""
tags: [dashboard, projects]
keywords: [projects, priorities, next actions]
aliases: []
context: ""
uid: ""
canonical_ref: ""
source_type: manual
template_key: master-template
---

# Projects Dashboard

```dataview
TABLE WITHOUT ID file.link AS Project, status AS Status, priority AS Priority, next_action AS "Next action", due_date AS Due
FROM "40_projects"
WHERE type = "project" OR contains(tags, "project")
SORT choice(status = "active", 0, 1) ASC, priority ASC, due_date ASC
```

## Job launches

- [[../40_projects/jobs_apply_cody/_index|Cody job-search command center]]
- [[../40_projects/jobs_apply_zai/_index|Zaitullah job-launch command center]]

## Review questions

- Which three projects matter most this week?
- What is the next physical action for each?
- Which project should be paused, closed, or archived?
