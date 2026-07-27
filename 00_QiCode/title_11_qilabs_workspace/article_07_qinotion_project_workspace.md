---
layout: article
title: Article 7. QiNotion Project Workspace
slug: qicode-title-11-article-07-qinotion-project-workspace
summary: "Defines the Notion-only project workspace architecture, preventing unnecessary filesystem mirroring."
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
  - QiLabs
  - Workspace
  - Notion
  - Projects
  - Operations
qicode_title: 11
qicode_article: 7
parent_title: Title 11. QiLabs Workspace
canonical_ref: QiCode T11.A07
source_type: manual
---

## Article 7. QiNotion Project Workspace

Stable ID: `T11.A07`

### Sec. 11.07.010. Purpose and System Boundaries

Stable ID: `T11.A07.S010`

- `Line 1` QiNotion provides a lightweight workspace for projects currently being managed in Notion. (`Sec. 11.07.010.L001`; stable ID `T11.A07.S010.L001`)
- `Line 2` It does not reproduce the full QiLabs ecosystem hierarchy. Only active or intentionally tracked projects should exist in the Notion Projects database. Systems that are not being managed in Notion do not need corresponding pages, folders, or placeholder records. (`Sec. 11.07.010.L002`; stable ID `T11.A07.S010.L002`)
- `Line 3` Notion provides project coordination, shared databases, active workspace views, and temporary capture. (`Sec. 11.07.010.L003`; stable ID `T11.A07.S010.L003`)
- `Line 4` GitHub provides software source code, technical implementation, issues, releases, and repository truth. (`Sec. 11.07.010.L004`; stable ID `T11.A07.S010.L004`)
- `Line 5` QiCode provides canonical ecosystem doctrine, architecture, naming, governance, and system definitions. (`Sec. 11.07.010.L005`; stable ID `T11.A07.S010.L005`)
- `Line 6` Obsidian / QiVault provides durable documentation, research, knowledge, decisions, timelines, and long-term records. (`Sec. 11.07.010.L006`; stable ID `T11.A07.S010.L006`)
- `Line 7` QiLife will be the future primary operating interface for projects, tasks, people, events, knowledge, and life operations. (`Sec. 11.07.010.L007`; stable ID `T11.A07.S010.L007`)
- `Line 8` Notion is a temporary and focused project-management surface until the relevant capabilities are implemented in QiLife and QiVault, and it is not the permanent source of truth for the entire QiLabs ecosystem. (`Sec. 11.07.010.L008`; stable ID `T11.A07.S010.L008`)

### Sec. 11.07.020. Non-Goals

Stable ID: `T11.A07.S020`

- `Line 1` QiNotion does not mirror every QiLabs folder or contain a page for every QiLabs system. (`Sec. 11.07.020.L001`; stable ID `T11.A07.S020.L001`)
- `Line 2` QiNotion does not replace QiCode, GitHub, or QiVault, nor does it act as a second Life OS. (`Sec. 11.07.020.L002`; stable ID `T11.A07.S020.L002`)
- `Line 3` QiNotion does not use navigation pages as workflow statuses, create separate databases for every project, or require projects to be physically moved when their state changes. (`Sec. 11.07.020.L003`; stable ID `T11.A07.S020.L003`)
- `Line 4` QiNotion does not dictate or control the canonical QiLabs filesystem. (`Sec. 11.07.020.L004`; stable ID `T11.A07.S020.L004`)

### Sec. 11.07.030. Canonical Notion Structure

Stable ID: `T11.A07.S030`

- `Line 1` The canonical Notion structure comprises the following five databases (not filesystem directories): Projects, Tasks, People, Insights, and Timeline. (`Sec. 11.07.030.L001`; stable ID `T11.A07.S030.L001`)
- `Line 2` The only permanent top-level Notion page required is named `QiLabs Workspace`. The five databases may exist directly inside or beneath that page. (`Sec. 11.07.030.L002`; stable ID `T11.A07.S030.L002`)
- `Line 3` Pages and database records represent stable entities. Properties represent changing conditions. Views represent temporary perspectives. (`Sec. 11.07.030.L003`; stable ID `T11.A07.S030.L003`)
- `Line 4` Statuses (such as Active, Paused, Waiting, Now, Next, Later, This Week, Completed, Archived) must never become navigation pages or folders. Status, priority, stage, scheduling, and similar workflow concepts belong in database properties and filtered views. (`Sec. 11.07.030.L004`; stable ID `T11.A07.S030.L004`)
- `Line 5` Records do not move between folders when their status changes. (`Sec. 11.07.030.L005`; stable ID `T11.A07.S030.L005`)

### Sec. 11.07.040. Projects Database

Stable ID: `T11.A07.S040`

- `Line 1` One shared Notion database conceptually named `Projects` shall exist. Each record represents a project currently being managed through Notion. (`Sec. 11.07.040.L001`; stable ID `T11.A07.S040.L001`)
- `Line 2` Recommended properties include: Project, QiCode, System, Project Type, Status, Priority, Repository, Obsidian Path, Started, and Target. (`Sec. 11.07.040.L002`; stable ID `T11.A07.S040.L002`)
- `Line 3` The `System` property links the project conceptually to the QiLabs ecosystem (e.g., QiLabs, QiSpark, QiServer, QiWorkers, QiDrive, QiVault, QiApps, QiSites) without recreating the ecosystem as Notion folders. These values are classifications only and must not generate filesystem changes. (`Sec. 11.07.040.L003`; stable ID `T11.A07.S040.L003`)

### Sec. 11.07.050. Canonical Project Page Template

Stable ID: `T11.A07.S050`

- `Line 1` Every Projects database record should use the same stable page template. (`Sec. 11.07.050.L001`; stable ID `T11.A07.S050.L001`)
- `Line 2` The template includes a "Project Brief" (Purpose, Outcome, Current Architecture, Source Systems) and linked views of Tasks, Insights, Timeline, and People, all filtered to the current project. (`Sec. 11.07.050.L002`; stable ID `T11.A07.S050.L002`)
- `Line 3` A unique page architecture must not be created for each project. The template must remain stable so projects can be created and used without redesigning Notion. (`Sec. 11.07.050.L003`; stable ID `T11.A07.S050.L003`)

### Sec. 11.07.060. Tasks Database

Stable ID: `T11.A07.S060`

- `Line 1` One shared Notion database conceptually named `Tasks` shall exist for all projects. (`Sec. 11.07.060.L001`; stable ID `T11.A07.S060.L001`)
- `Line 2` Recommended properties include: Task, Project, Parent Task, Status, Priority, Due, Scheduled, and Context. (`Sec. 11.07.060.L002`; stable ID `T11.A07.S060.L002`)
- `Line 3` Project pages display filtered linked views where `Project = Current Project`. Separate task databases for individual projects must not be created. (`Sec. 11.07.060.L003`; stable ID `T11.A07.S060.L003`)

### Sec. 11.07.070. People Database

Stable ID: `T11.A07.S070`

- `Line 1` One shared Notion database conceptually named `People` shall exist. (`Sec. 11.07.070.L001`; stable ID `T11.A07.S070.L001`)
- `Line 2` Recommended properties include: Name, Relationship, Organization, Role, Projects, Contact Information, Notes, and Last Contact. (`Sec. 11.07.070.L002`; stable ID `T11.A07.S070.L002`)
- `Line 3` This database serves as a temporary shared directory until the information is migrated into the appropriate long-term QiLife or QiVault structure. (`Sec. 11.07.070.L003`; stable ID `T11.A07.S070.L003`)

### Sec. 11.07.080. Insights Database

Stable ID: `T11.A07.S080`

- `Line 1` One shared Notion database conceptually named `Insights` shall exist, allowing discoveries and thoughts to be captured without changing project structure. (`Sec. 11.07.080.L001`; stable ID `T11.A07.S080.L001`)
- `Line 2` Recommended properties include: Insight, Type, Project, People, Source, Created, Promoted to Obsidian, and Obsidian Path. (`Sec. 11.07.080.L002`; stable ID `T11.A07.S080.L002`)
- `Line 3` Once an insight becomes durable doctrine, documentation, research, or knowledge, it should be promoted to Obsidian/QiVault and linked back from Notion. (`Sec. 11.07.080.L003`; stable ID `T11.A07.S080.L003`)

### Sec. 11.07.090. Timeline Database

Stable ID: `T11.A07.S090`

- `Line 1` One shared Notion database conceptually named `Timeline` shall exist to record meaningful historical events. (`Sec. 11.07.090.L001`; stable ID `T11.A07.S090.L001`)
- `Line 2` Recommended properties include: Event, Date, Project, People, Event Type, Summary, Source, Promoted to Obsidian, and Obsidian Path. (`Sec. 11.07.090.L002`; stable ID `T11.A07.S090.L002`)
- `Line 3` Timeline is not a duplicate task completion log. Do not create timeline entries for every minor task unless the event has historical, operational, or analytical value. (`Sec. 11.07.090.L003`; stable ID `T11.A07.S090.L003`)
- `Line 4` Timeline content is expected to move into Obsidian/QiVault later. (`Sec. 11.07.090.L004`; stable ID `T11.A07.S090.L004`)
