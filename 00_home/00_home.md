---
layout: home
type: index
title: QiVault Home
slug: qivault-home
summary: Primary command center for navigating, capturing, reviewing, and acting across QiVault.
status: active
visibility: internal
publish_target: none
publish_url: ""
created_at: "2026-07-01T23:17:15-05:00"
updated_at: "2026-07-16"
author: Cody J. Rice-Velasquez
owner: Cody
nav_title: Home
nav_group: home
nav_order: 1
nav_hidden: false
is_index: true
parent_ref: ""
sensitivity: internal
classification: business_internal
realm_label: ""
tags: [moc, home, dashboard]
keywords: [home, navigation, command center]
aliases: [Home, Command Center]
context: ""
uid: 252a5e4e74c349cbad8b64f3b35854e6
canonical_ref: ""
source_type: manual
template_key: master-template
---

# QiVault Home

> [!tip] Start here
> Capture quickly, see what needs attention, and move into the right part of the vault without remembering folder paths.

## Right now

| Action | Destination |
|---|---|
| Capture something new | [[01_inbox/_index|Inbox]] |
| Review tasks and schedule | [[TaskNotes/start_here|Tasks and agenda]] |
| Continue active work | [[projects_dashboard|Projects dashboard]] |
| Understand what happened | [[timeline_dashboard|Timeline dashboard]] |
| Find a person | [[02_directory/10_people/_index|People directory]] |
| Open QiLabs knowledge | [[50_QiLabs/_index|QiLabs]] |

## Active projects

```dataview
TABLE WITHOUT ID file.link AS Project, status AS Status, priority AS Priority, next_action AS "Next action"
FROM "40_projects"
WHERE type = "project" AND status != "complete" AND status != "archived"
SORT priority ASC, file.mtime DESC
LIMIT 12
```

## Recent work

```dataview
TABLE WITHOUT ID file.link AS Note, file.folder AS Area, file.mtime AS Updated
FROM ""
WHERE !contains(file.path, ".obsidian/")
  AND !contains(file.path, ".trash/")
  AND !contains(file.path, "99_archive/")
  AND !contains(file.path, "_qiconfig/")
SORT file.mtime DESC
LIMIT 10
```

## Major spaces

- [[01_inbox/_index|01 · Inbox]] — unprocessed captures and imported material
- [[02_directory/_index|02 · Directory]] — people, organizations, and relationships
- [[10_daily/_index|10 · Daily and timeline]] — chronological events and daily records
- [[20_life/_index|20 · Life]] — personal operating areas and life administration
- [[30_empowerqnow713/_index|30 · EmpowerQNow713]] — writing, series, and public knowledge
- [[40_projects/_index|40 · Projects]] — active outcome-oriented work
- [[50_QiLabs/_index|50 · QiLabs]] — products, systems, architecture, and technical knowledge
- [[60_cases/_index|60 · Cases]] — structured case work
- [[70_Knowledge/_index|70 · Knowledge]] — reference and research material
- [[80_records/_index|80 · Records]] — durable records
- [[90_outputs/_index|90 · Outputs]] — generated and delivered artifacts
- [[99_archive/_index|99 · Archive]] — inactive and superseded material

## Where should this go?

- Not sure yet → `01_inbox`
- Something that happened on a date → `10_daily`, using `type: event`
- A person or organization → `02_directory`
- Work with a defined outcome → `40_projects`
- Durable factual evidence → `80_records` or the relevant case
- Reusable explanation or research → `70_Knowledge`
- Finished deliverable → `90_outputs`

## System health

- [[missing_metadata|Missing metadata]]
- [[../_qiconfig/_index|Templates and configuration]]
- [[../_system/codex_agent_workflow|Agent workflow]]
