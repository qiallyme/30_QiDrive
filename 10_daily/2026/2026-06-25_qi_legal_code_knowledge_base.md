---
layout: page
title: "Qi Legal-Code Knowledge Base"
slug: "qi_legal_code_knowledge_base"
created_at: "2026-06-25 19:04:56"
updated_at: "2026-07-16T06:49:34-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-009.json"
template_key: master-template
date: 2026-06-25
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a3dc210-f32c-83ea-b6ec-de8f7111ad0b"
canonical_ref: ""
---

# Qi Legal-Code Knowledge Base

## Overview
- **Date**: 2026-06-25 19:04:56
- **Conversation ID**: `6a3dc210-f32c-83ea-b6ec-de8f7111ad0b`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> if i wanted to organize my knowledge base like they do law books with qi legal codes what would taht outlien look like just top level.

### Assistant
> Yes. The move is **not** to literally mimic legal books with too much ceremony. The useful pattern is:
> 
> > **Title → Subtitle/Part → Chapter → Article/Section → Rule/Note/Source**
> 
> For Qi, I’d make it look like a **code system**: stable, numbered, referenceable, but still human-readable.
> 
> # Qi Legal-Code Style Knowledge Base
> 
> ```text
> Qi Code
> ├── Title 00 — General Provisions
> ├── Title 01 — Doctrine & Principles
> ├── Title 02 — System Architecture
> ├── Title 03 — Operations
> ├── Title 04 — Data & Records
> ├── Title 05 — Apps & Interfaces
> ├── Title 06 — Automation & Agents
> ├── Title 07 — Security & Access
> ├── Title 08 — Evidence & Audit
> ├── Title 09 — People, Roles & Governance
> ├── Title 10 — Finance & Assets
> ├── Title 11 — Legal & Compliance
> ├── Title 12 — Creative Works & Publications
> ├── Title 13 — Personal Systems / QiLife
> ├── Title 14 — Standards, Templates & Forms
> ├── Title 15 — Archive, Superseded & Deprecated
> └── Title 99 — Reserved / Experimental
> ```
> 
> ## Cleaner Qi-Specific Version
> 
> ```text
> QiCode
> ├── 00_general
> │   ├── scope
> │   ├── definitions
> │   └── naming_rules
> │
> ├── 01_doctrine
> │   ├── principles
> │   ├── decision_rules
> │   ├── operating_philosophy
> │   └── system_boundaries
> │
> ├── 02_architecture
> │   ├── qilabs
> │   ├── qispark
> │   ├── qiserver
> │   ├── qidrive
> │   ├── qiapps
> │   └── integrations
> │
> ├── 03_operations
> │   ├── workflows
> │   ├── sops
> │   ├── routines
> │   ├── incident_response
> │   └── maintenance
> │
> ├── 04_records
> │   ├── record_types
> │   ├── metadata
> │   ├── tags
> │   ├── evidence
> │   └── retention
> │
> ├── 05_applications
> │   ├── qilife
> │   ├── qidrive
> │   ├── qispark_site
> │   └── qiapps
> │
> ├── 06_automation
> │   ├── agents
> │   ├── scripts
> │   ├── prompts
> │   ├── pipelines
> │   └── scheduled_tasks
> │
> ├── 07_access_security
> │   ├── accounts
> │   ├── permissions
> │   ├── secrets
> │   ├── cloudflare
> │   └── backup_recovery
> │
> ├── 08_governance
> │   ├── roles
> │   ├── decisions
> │   ├── adr
> │   ├── change_control
> │   └── deprecation
> │
> ├── 09_finance_assets
> │   ├── accounts
> │   ├── inventory
> │   ├── reimbursements
> │   ├── debts
> │   └── reports
> │
> ├── 10_legal_compliance
> │   ├── contracts
> │   ├── notices
> │   ├── disputes
> │   ├── tenant_housing
> │   └── immigration_clients
> │
> ├── 11_creative_publication
> │   ├── essays
> │   ├── series
> │   ├── books
> │   ├── posts
> │   └── public_pages
> │
> ├── 12_qilife
> │   ├── planner
> │   ├── people
> │   ├── vendors
> │   ├── government
> │   ├── projects
> │   ├── journal
> │   └── activities
> │
> ├── 13_standards_templates
> │   ├── templates
> │   ├── naming
> │   ├── schemas
> │   ├── forms
> │   └── checklists
> │
> ├── 90_archive
> │   ├── superseded
> │   ├── deprecated
> │   ├── historical
> │   └── quarantine
> │
> └── 99_experimental
>     ├── drafts
>     ├── prototypes
>     ├── research
>     └── parking_lot
> ```
> 
> # The Law-Book Numbering Pattern
> 
> Each page can get a citation-style ID:
> 
> ```text
> QiCode § 02.03.001
> ```
> 
> Meaning:
> 
> ```text
> Title 02 — Architecture
> Chapter 03 — QiServer
> Section 001 — Purpose / Scope / Rule
> ```
> 
> Example:
> 
> ```text
> QiCode § 02.03.001 — QiServer Scope
> QiCode § 02.03.002 — Cloudflare Placement
> QiCode § 02.03.003 — Runtime Services
> QiCode § 04.02.001 — Record Metadata Standard
> QiCode § 08.03.001 — Architecture Decision Records
> ```
> 
> # My honest take
> 
> This is a **good structure** for you *only if* you keep it shallow.
> 
> Do **not** make 500 folders because “legal code aesthetic.” That becomes ADHD tax hell.
> 
> The better pattern:
> 
> ```text
> Top-level Titles = stable
> Pages inside = flexible
> Numbers = reference system
> Properties = specificity
> ```
> 
> So instead of creating too many folders, you’d have files like:
> 
> ```text
> 02.03.001_qiserver_scope.md
> 02.03.002_cloudflare_placement.md
> 08.03.001_adr_standard.md
> 12.01.001_qilife_planner_model.md
> ```
> 
> That gives you the law-book feel without building a bureaucratic haunted house.

### User
> yes, i like this way of using titles and having the very specific sections for things, what would a full outline look like, be srue not to create extra sections or pages where they can be merged to reduce the number of sections.

### Assistant
> I’d keep the “legal code” feel, but make the unit of organization **one page per chapter**, with numbered sections inside. That gives you precision without turning your vault into a filing cabinet from hell.

### Assistant
> Yes. This is the right direction.
> 
> But here’s the discipline: **Titles are the big law-book buckets. Chapters are pages. Sections are headings inside pages.** Do **not** make every section its own file unless it becomes huge.
> 
> # Recommended Rule
> 
> ```text
> Title = folder
> Chapter = markdown page
> Section = heading inside the page
> Subsection = bullet/table/property, not another page
> ```
> 
> So instead of this mess:
> 
> ```text
> 02_architecture/
> ├── qiserver/
> │   ├── scope.md
> │   ├── services.md
> │   ├── cloudflare.md
> │   ├── cockpit.md
> │   └── runtime.md
> ```
> 
> Do this:
> 
> ```text
> 02_architecture/
> └── 02.03_qiserver_runtime.md
> ```
> 
> Inside that page:
> 
> ```markdown
> # QiCode § 02.03 — QiServer Runtime
> 
> ## § 02.03.001 — Scope
> ## § 02.03.002 — Cockpit
> ## § 02.03.003 — Runtime Services
> ## § 02.03.004 — Cloudflare Placement
> ## § 02.03.005 — Boundaries
> ```
> 
> That’s the sauce.
> 
> ---
> 
> # Full Lean QiCode Outline
> 
> ```text
> QiCode
> ├── 00_general_provisions
> │   ├── 00.01_scope_authority_citation.md
> │   ├── 00.02_definitions_naming_status.md
> │   └── 00.03_structure_numbering_conventions.md
> │
> ├── 01_doctrine_principles
> │   ├── 01.01_qi_doctrine.md
> │   ├── 01.02_operating_principles.md
> │   └── 01.03_decision_rules.md
> │
> ├── 02_system_architecture
> │   ├── 02.01_qilabs_root_model.md
> │   ├── 02.02_qispark_docs_landing.md
> │   ├── 02.03_qiserver_runtime.md
> │   ├── 02.04_qidrive_records_layer.md
> │   ├── 02.05_qiapps_application_layer.md
> │   └── 02.06_integrations_external_services.md
> │
> ├── 03_operations
> │   ├── 03.01_workflows_sops_routines.md
> │   ├── 03.02_maintenance_incidents_recovery.md
> │   └── 03.03_deployment_environments.md
> │
> ├── 04_data_records
> │   ├── 04.01_record_model.md
> │   ├── 04.02_metadata_tags_links.md
> │   ├── 04.03_evidence_audit_retention.md
> │   └── 04.04_import_export_standards.md
> │
> ├── 05_qispark
> │   ├── 05.01_navigation_information_architecture.md
> │   ├── 05.02_docs_publication_model.md
> │   └── 05.03_qidna_doctrine_section.md
> │
> ├── 06_qiserver
> │   ├── 06.01_server_services_cockpit.md
> │   ├── 06.02_qimemory_ingest_automation.md
> │   ├── 06.03_cloudflare_zero_trust.md
> │   └── 06.04_backups_secrets_recovery.md
> │
> ├── 07_qidrive
> │   ├── 07.01_drive_mirror_structure.md
> │   ├── 07.02_evidence_libraries.md
> │   └── 07.03_file_retention_export.md
> │
> ├── 08_qiapps
> │   ├── 08.01_app_registry.md
> │   ├── 08.02_project_standards.md
> │   ├── 08.03_interfaces_components.md
> │   └── 08.04_agents_automation_patterns.md
> │
> ├── 09_qilife
> │   ├── 09.01_planner.md
> │   ├── 09.02_erm_people_vendors_government.md
> │   ├── 09.03_workbench_projects_journal_creative.md
> │   └── 09.04_activities_routines.md
> │
> ├── 10_security_access
> │   ├── 10.01_identity_accounts_permissions.md
> │   ├── 10.02_devices_secrets_credentials.md
> │   └── 10.03_security_incidents_access_reviews.md
> │
> ├── 11_governance_change_control
> │   ├── 11.01_decision_records.md
> │   ├── 11.02_standards_templates_forms.md
> │   └── 11.03_change_control_deprecation.md
> │
> ├── 12_finance_assets
> │   ├── 12.01_accounts_transactions_exports.md
> │   ├── 12.02_inventory_assets_property.md
> │   └── 12.03_reimbursements_debts_reports.md
> │
> ├── 13_legal_compliance
> │   ├── 13.01_contracts_agreements_notices.md
> │   ├── 13.02_disputes_claims_evidence.md
> │   ├── 13.03_housing_tenant_records.md
> │   └── 13.04_client_matter_files.md
> │
> ├── 14_creative_publication
> │   ├── 14.01_publication_registry.md
> │   ├── 14.02_series_books_chapters.md
> │   └── 14.03_essays_posts_pages.md
> │
> ├── 90_archive
> │   ├── 90.01_superseded_deprecated.md
> │   ├── 90.02_historical_snapshots.md
> │   └── 90.03_quarantine.md
> │
> └── 99_experimental
>     ├── 99.01_prototypes_research.md
>     └── 99.02_parking_lot.md
> ```
> 
> This gives you **16 title folders** and **51 chapter pages**. That’s the upper bound. Realistically, you can start with fewer and let the rest appear only when needed.
> 
> ---
> 
> # Internal Section Outline
> 
> ## `00_general_provisions`
> 
> ```text
> 00.01 — Scope, Authority & Citation
> ├── § 00.01.001 — Purpose of QiCode
> ├── § 00.01.002 — What QiCode Governs
> ├── § 00.01.003 — Source of Authority
> ├── § 00.01.004 — Citation Format
> └── § 00.01.005 — When QiCode Overrides Notes
> 
> 00.02 — Definitions, Naming & Status
> ├── § 00.02.001 — Canonical Terms
> ├── § 00.02.002 — Retired Terms
> ├── § 00.02.003 — Renamed Systems
> ├── § 00.02.004 — Status Labels
> └── § 00.02.005 — Naming Rules
> 
> 00.03 — Structure, Numbering & Conventions
> ├── § 00.03.001 — Title Structure
> ├── § 00.03.002 — Chapter Structure
> ├── § 00.03.003 — Section Numbering
> ├── § 00.03.004 — File Naming
> └── § 00.03.005 — Cross-References
> ```
> 
> ---
> 
> ## `01_doctrine_principles`
> 
> ```text
> 01.01 — Qi Doctrine
> ├── § 01.01.001 — Core Doctrine
> ├── § 01.01.002 — System Purpose
> ├── § 01.01.003 — Modularity Principle
> ├── § 01.01.004 — Low-Bloat Rule
> └── § 01.01.005 — Human-First Operations
> 
> 01.02 — Operating Principles
> ├── § 01.02.001 — Leverage
> ├── § 01.02.002 — Clarity
> ├── § 01.02.003 — Traceability
> ├── § 01.02.004 — Reversibility
> └── § 01.02.005 — Minimum Viable Structure
> 
> 01.03 — Decision Rules
> ├── § 01.03.001 — Merge Before Splitting
> ├── § 01.03.002 — Properties Before Tables
> ├── § 01.03.003 — Folders Must Earn Existence
> ├── § 01.03.004 — No Placeholder Architecture
> └── § 01.03.005 — Archive Instead of Deleting
> ```
> 
> This is one of the most important titles. This is where you stop future-you from overbuilding nonsense.
> 
> ---
> 
> ## `02_system_architecture`
> 
> ```text
> 02.01 — QiLabs Root Model
> ├── § 02.01.001 — Canonical Root Structure
> ├── § 02.01.002 — Workspace Layer
> ├── § 02.01.003 — Docs Layer
> ├── § 02.01.004 — Runtime Layer
> ├── § 02.01.005 — Records Layer
> └── § 02.01.006 — Apps Layer
> 
> 02.02 — QiSpark Docs & Landing
> ├── § 02.02.001 — QiSpark Scope
> ├── § 02.02.002 — Docs Site Role
> ├── § 02.02.003 — Landing Page Role
> ├── § 02.02.004 — Navigation Model
> └── § 02.02.005 — QiDNA Placement
> 
> 02.03 — QiServer Runtime
> ├── § 02.03.001 — QiServer Scope
> ├── § 02.03.002 — Cockpit Role
> ├── § 02.03.003 — Runtime Services
> ├── § 02.03.004 — Cloudflare Placement
> └── § 02.03.005 — Boundaries
> 
> 02.04 — QiDrive Records Layer
> ├── § 02.04.001 — QiDrive Scope
> ├── § 02.04.002 — Drive Mirror
> ├── § 02.04.003 — Evidence Storage
> ├── § 02.04.004 — File Libraries
> └── § 02.04.005 — Export Rules
> 
> 02.05 — QiApps Application Layer
> ├── § 02.05.001 — QiApps Scope
> ├── § 02.05.002 — App Registry
> ├── § 02.05.003 — Project Boundaries
> ├── § 02.05.004 — Shared Components
> └── § 02.05.005 — Deployment Boundaries
> 
> 02.06 — Integrations & External Services
> ├── § 02.06.001 — Integration Registry
> ├── § 02.06.002 — Supabase
> ├── § 02.06.003 — Cloudflare
> ├── § 02.06.004 — Obsidian
> ├── § 02.06.005 — Google Drive
> └── § 02.06.006 — Future Services
> ```
> 
> Notice: Cloudflare appears in architecture **as placement**, but its operational details live under QiServer. That keeps it from becoming a random top-level beast.
> 
> ---
> 
> ## `03_operations`
> 
> ```text
> 03.01 — Workflows, SOPs & Routines
> ├── § 03.01.001 — Workflow Standard
> ├── § 03.01.002 — SOP Standard
> ├── § 03.01.003 — Routine Standard
> ├── § 03.01.004 — Checklist Standard
> └── § 03.01.005 — Runbook Standard
> 
> 03.02 — Maintenance, Incidents & Recovery
> ├── § 03.02.001 — Maintenance Types
> ├── § 03.02.002 — Incident Levels
> ├── § 03.02.003 — Recovery Process
> ├── § 03.02.004 — After-Action Notes
> └── § 03.02.005 — Escalation Rules
> 
> 03.03 — Deployment & Environments
> ├── § 03.03.001 — Local Environment
> ├── § 03.03.002 — Development Environment
> ├── § 03.03.003 — Production Environment
> ├── § 03.03.004 — Deployment Process
> └── § 03.03.005 — Rollback Process
> ```
> 
> Do **not** split workflows, SOPs, routines, and checklists into separate chapter pages yet. They’re siblings, not kingdoms.
> 
> ---
> 
> ## `04_data_records`
> 
> ```text
> 04.01 — Record Model
> ├── § 04.01.001 — Record Definition
> ├── § 04.01.002 — Record Types
> ├── § 04.01.003 — Record Status
> ├── § 04.01.004 — Record Ownership
> └── § 04.01.005 — Record Lifecycle
> 
> 04.02 — Metadata, Tags & Links
> ├── § 04.02.001 — Metadata Standard
> ├── § 04.02.002 — Tag Standard
> ├── § 04.02.003 — Link Standard
> ├── § 04.02.004 — Relationship Types
> └── § 04.02.005 — Searchability Rules
> 
> 04.03 — Evidence, Audit & Retention
> ├── § 04.03.001 — Evidence Definition
> ├── § 04.03.002 — Audit Trail
> ├── § 04.03.003 — Chain of Custody
> ├── § 04.03.004 — Retention Rules
> └── § 04.03.005 — Deletion Rules
> 
> 04.04 — Import, Export & Compatibility
> ├── § 04.04.001 — Import Standard
> ├── § 04.04.002 — Export Standard
> ├── § 04.04.003 — CSV Compatibility
> ├── § 04.04.004 — Markdown Compatibility
> └── § 04.04.005 — External System Mapping
> ```
> 
> This title becomes the “rules of records.” Good. Keep it clean.
> 
> ---
> 
> ## `05_qispark`
> 
> ```text
> 05.01 — Navigation & Information Architecture
> ├── § 05.01.001 — Homepage Structure
> ├── § 05.01.002 — Section Navigation
> ├── § 05.01.003 — Book/Series Navigation
> ├── § 05.01.004 — Tags and Collections
> └── § 05.01.005 — Search Pathways
> 
> 05.02 — Docs & Publication Model
> ├── § 05.02.001 — Public Docs
> ├── § 05.02.002 — Private Docs
> ├── § 05.02.003 — Drafts
> ├── § 05.02.004 — Published Pages
> └── § 05.02.005 — Update Rules
> 
> 05.03 — QiDNA Doctrine Section
> ├── § 05.03.001 — QiDNA Is Not a Separate Module
> ├── § 05.03.002 — Doctrine Docs
> ├── § 05.03.003 — Standards Docs
> ├── § 05.03.004 — Maps and Overviews
> └── § 05.03.005 — Canonical References
> ```
> 
> Important: **QiDNA stays here.** Do not resurrect it as its own thing. We are not summoning old ghosts.
> 
> ---
> 
> ## `06_qiserver`
> 
> ```text
> 06.01 — Server Services & Cockpit
> ├── § 06.01.001 — Cockpit Purpose
> ├── § 06.01.002 — Service Registry
> ├── § 06.01.003 — Runtime Dashboard
> ├── § 06.01.004 — Admin Links
> └── § 06.01.005 — Health Checks
> 
> 06.02 — QiMemory, Ingest & Automation
> ├── § 06.02.001 — QiMemory Scope
> ├── § 06.02.002 — Capture Rules
> ├── § 06.02.003 — Ingest Pipelines
> ├── § 06.02.004 — Processing Rules
> └── § 06.02.005 — Memory Boundaries
> 
> 06.03 — Cloudflare & Zero Trust
> ├── § 06.03.001 — Cloudflare Placement
> ├── § 06.03.002 — DNS
> ├── § 06.03.003 — Pages
> ├── § 06.03.004 — Zero Trust
> └── § 06.03.005 — Access Policies
> 
> 06.04 — Backups, Secrets & Recovery
> ├── § 06.04.001 — Backup Targets
> ├── § 06.04.002 — Secret Handling
> ├── § 06.04.003 — Recovery Procedure
> ├── § 06.04.004 — Rotation Rules
> └── § 06.04.005 — Failure Modes
> ```
> 
> This is where the actual server mess gets domesticated.
> 
> ---
> 
> ## `07_qidrive`
> 
> ```text
> 07.01 — Drive Mirror Structure
> ├── § 07.01.001 — QiDrive Scope
> ├── § 07.01.002 — Mirror Rules
> ├── § 07.01.003 — Folder Standards
> ├── § 07.01.004 — Sync Rules
> └── § 07.01.005 — Conflicts
> 
> 07.02 — Evidence Libraries
> ├── § 07.02.001 — Evidence Intake
> ├── § 07.02.002 — Evidence Categories
> ├── § 07.02.003 — Supporting Documents
> ├── § 07.02.004 — Matter Links
> └── § 07.02.005 — Review Status
> 
> 07.03 — File Retention & Export
> ├── § 07.03.001 — Retention Classes
> ├── § 07.03.002 — Archive Rules
> ├── § 07.03.003 — Export Bundles
> ├── § 07.03.004 — Naming Rules
> └── § 07.03.005 — Duplicate Handling
> ```
> 
> ---
> 
> ## `08_qiapps`
> 
> ```text
> 08.01 — App Registry
> ├── § 08.01.001 — App Definition
> ├── § 08.01.002 — Active Apps
> ├── § 08.01.003 — Experimental Apps
> ├── § 08.01.004 — Retired Apps
> └── § 08.01.005 — App Ownership
> 
> 08.02 — Project Standards
> ├── § 08.02.001 — Project Structure
> ├── § 08.02.002 — Source Control
> ├── § 08.02.003 — Environment Files
> ├── § 08.02.004 — Documentation
> └── § 08.02.005 — Release Rules
> 
> 08.03 — Interfaces & Components
> ├── § 08.03.001 — UI Standards
> ├── § 08.03.002 — Shared Components
> ├── § 08.03.003 — Layout Rules
> ├── § 08.03.004 — Design Tokens
> └── § 08.03.005 — Accessibility
> 
> 08.04 — Agents & Automation Patterns
> ├── § 08.04.001 — Agent Scope
> ├── § 08.04.002 — Prompt Assets
> ├── § 08.04.003 — Script Patterns
> ├── § 08.04.004 — Human Review
> └── § 08.04.005 — Failure Control
> ```
> 
> I’d keep agents here **only when they belong to apps/projects**. Server-side memory/ingest agents live under QiServer.
> 
> ---
> 
> ## `09_qilife`
> 
> ```text
> 09.01 — Planner
> ├── § 09.01.001 — Inbox
> ├── § 09.01.002 — Today
> ├── § 09.01.003 — Calendar
> ├── § 09.01.004 — Tasks
> ├── § 09.01.005 — Activities
> └── § 09.01.006 — Routines
> 
> 09.02 — ERM: People, Vendors & Government
> ├── § 09.02.001 — People
> ├── § 09.02.002 — Vendors
> ├── § 09.02.003 — Government
> ├── § 09.02.004 — Relationships
> └── § 09.02.005 — Communication History
> 
> 09.03 — Workbench: Projects, Journal & Creative
> ├── § 09.03.001 — Projects
> ├── § 09.03.002 — Notes
> ├── § 09.03.003 — Journal
> ├── § 09.03.004 — Creative Work
> └── § 09.03.005 — Research
> 
> 09.04 — Activities & Routines
> ├── § 09.04.001 — Activity Types
> ├── § 09.04.002 — Routine Types
> ├── § 09.04.003 — Frequency
> ├── § 09.04.004 — Status
> └── § 09.04.005 — Review
> ```
> 
> Minor warning: `09.01 Planner` and `09.04 Activities & Routines` overlap. That’s okay **only if** Planner is the interface and Activities/Routines is the data model. If that distinction gets fuzzy, merge `09.04` into `09.01`.
> 
> ---
> 
> ## `10_security_access`
> 
> ```text
> 10.01 — Identity, Accounts & Permissions
> ├── § 10.01.001 — Identity Model
> ├── § 10.01.002 — Account Registry
> ├── § 10.01.003 — Roles
> ├── § 10.01.004 — Permissions
> └── § 10.01.005 — Access Review
> 
> 10.02 — Devices, Secrets & Credentials
> ├── § 10.02.001 — Device Registry
> ├── § 10.02.002 — Password Rules
> ├── § 10.02.003 — API Keys
> ├── § 10.02.004 — Recovery Codes
> └── § 10.02.005 — Credential Rotation
> 
> 10.03 — Security Incidents & Access Reviews
> ├── § 10.03.001 — Incident Types
> ├── § 10.03.002 — Unauthorized Access
> ├── § 10.03.003 — Lockout Recovery
> ├── § 10.03.004 — Audit Review
> └── § 10.03.005 — Post-Incident Cleanup
> ```
> 
> Keep this lean. Security folders get bloated fast because every scary thing feels like it needs its own shrine. It does not.
> 
> ---
> 
> ## `11_governance_change_control`
> 
> ```text
> 11.01 — Decision Records
> ├── § 11.01.001 — ADR Standard
> ├── § 11.01.002 — Decision Status
> ├── § 11.01.003 — Decision Context
> ├── § 11.01.004 — Supersession
> └── § 11.01.005 — Review Cycle
> 
> 11.02 — Standards, Templates & Forms
> ├── § 11.02.001 — Standard Definition
> ├── § 11.02.002 — Template Definition
> ├── § 11.02.003 — Form Definition
> ├── § 11.02.004 — Required Fields
> └── § 11.02.005 — Template Versioning
> 
> 11.03 — Change Control & Deprecation
> ├── § 11.03.001 — Change Request
> ├── § 11.03.002 — Approval Rules
> ├── § 11.03.003 — Migration Rules
> ├── § 11.03.004 — Deprecation Rules
> └── § 11.03.005 — Archive Rules
> ```
> 
> This title is where you stop the system from mutating every 30 minutes because your brain got a new shiny idea. Useful. Necessary. Slightly annoying. Good.
> 
> ---
> 
> ## `12_finance_assets`
> 
> ```text
> 12.01 — Accounts, Transactions & Exports
> ├── § 12.01.001 — Account Types
> ├── § 12.01.002 — Transaction Types
> ├── § 12.01.003 — Split Transactions
> ├── § 12.01.004 — Categories
> └── § 12.01.005 — Export Compatibility
> 
> 12.02 — Inventory, Assets & Property
> ├── § 12.02.001 — Inventory Items
> ├── § 12.02.002 — Assets
> ├── § 12.02.003 — Property Records
> ├── § 12.02.004 — Receipts
> └── § 12.02.005 — Valuation
> 
> 12.03 — Reimbursements, Debts & Reports
> ├── § 12.03.001 — Reimbursements
> ├── § 12.03.002 — Rent Deductions
> ├── § 12.03.003 — Debts
> ├── § 12.03.004 — Claims
> └── § 12.03.005 — Reports
> ```
> 
> Since you’re not doing full finance yet, this title can exist as a skeleton, but don’t build it deeply until you need it.
> 
> ---
> 
> ## `13_legal_compliance`
> 
> ```text
> 13.01 — Contracts, Agreements & Notices
> ├── § 13.01.001 — Contract Records
> ├── § 13.01.002 — Agreements
> ├── § 13.01.003 — Notices
> ├── § 13.01.004 — Deadlines
> └── § 13.01.005 — Response Tracking
> 
> 13.02 — Disputes, Claims & Evidence
> ├── § 13.02.001 — Dispute Records
> ├── § 13.02.002 — Claim Records
> ├── § 13.02.003 — Evidence Links
> ├── § 13.02.004 — Timeline
> └── § 13.02.005 — Outcome
> 
> 13.03 — Housing & Tenant Records
> ├── § 13.03.001 — Lease Status
> ├── § 13.03.002 — Rent Payments
> ├── § 13.03.003 — Repairs
> ├── § 13.03.004 — Access Issues
> └── § 13.03.005 — Notices
> 
> 13.04 — Client Matter Files
> ├── § 13.04.001 — Matter Registry
> ├── § 13.04.002 — Client Records
> ├── § 13.04.003 — Forms
> ├── § 13.04.004 — Evidence Packets
> └── § 13.04.005 — Case Timeline
> ```
> 
> This is enough. Do **not** create separate titles for housing, immigration, disputes, contracts, etc. That would explode. They are all legal/compliance matter types.
> 
> ---
> 
> ## `14_creative_publication`
> 
> ```text
> 14.01 — Publication Registry
> ├── § 14.01.001 — Work Types
> ├── § 14.01.002 — Draft Status
> ├── § 14.01.003 — Publication Status
> ├── § 14.01.004 — Platforms
> └── § 14.01.005 — Canonical Versions
> 
> 14.02 — Series, Books & Chapters
> ├── § 14.02.001 — Series
> ├── § 14.02.002 — Books
> ├── § 14.02.003 — Chapters
> ├── § 14.02.004 — Sections
> └── § 14.02.005 — Reading Order
> 
> 14.03 — Essays, Posts & Pages
> ├── § 14.03.001 — Essays
> ├── § 14.03.002 — Posts
> ├── § 14.03.003 — Public Pages
> ├── § 14.03.004 — Draft Notes
> └── § 14.03.005 — Repurposing
> ```
> 
> This lets your creative work behave like a publishing catalog without needing a whole separate universe.
> 
> ---
> 
> ## `90_archive`
> 
> ```text
> 90.01 — Superseded & Deprecated
> ├── § 90.01.001 — Superseded Items
> ├── § 90.01.002 — Deprecated Items
> ├── § 90.01.003 — Replacement References
> ├── § 90.01.004 — Reason for Deprecation
> └── § 90.01.005 — Revival Rules
> 
> 90.02 — Historical Snapshots
> ├── § 90.02.001 — Snapshot Definition
> ├── § 90.02.002 — Snapshot Timing
> ├── § 90.02.003 — Snapshot Contents
> ├── § 90.02.004 — Restore Notes
> └── § 90.02.005 — Comparison Notes
> 
> 90.03 — Quarantine
> ├── § 90.03.001 — Quarantine Purpose
> ├── § 90.03.002 — Unknown Files
> ├── § 90.03.003 — Duplicates
> ├── § 90.03.004 — Pending Review
> └── § 90.03.005 — Cleanup Rules
> ```
> 
> Archive is not trash. Archive is controlled historical storage.
> 
> ---
> 
> ## `99_experimental`
> 
> ```text
> 99.01 — Prototypes & Research
> ├── § 99.01.001 — Prototype Definition
> ├── § 99.01.002 — Research Notes
> ├── § 99.01.003 — Evaluation Criteria
> ├── § 99.01.004 — Promotion Rules
> └── § 99.01.005 — Kill Rules
> 
> 99.02 — Parking Lot
> ├── § 99.02.001 — Unsorted Ideas
> ├── § 99.02.002 — Future Concepts
> ├── § 99.02.003 — Maybe Later
> ├── § 99.02.004 — Review Timing
> └── § 99.02.005 — Delete or Promote
> ```
> 
> This is the junk drawer, but with a leash.
> 
> ---
> 
> # Best Starting Version
> 
> Don’t create all 51 files today. That would be fake productivity.
> 
> Start with these **12 core pages**:
> 
> ```text
> 00.01_scope_authority_citation.md
> 00.02_definitions_naming_status.md
> 01.01_qi_doctrine.md
> 01.03_decision_rules.md
> 02.01_qilabs_root_model.md
> 02.02_qispark_docs_landing.md
> 02.03_qiserver_runtime.md
> 02.04_qidrive_records_layer.md
> 02.05_qiapps_application_layer.md
> 04.01_record_model.md
> 09.01_planner.md
> 11.01_decision_records.md
> ```
> 
> That gives you the constitution, the map, the core architecture, the record model, QiLife entry point, and decision control.
> 
> Everything else can be added when it earns its existence.
> 
> # File Naming Pattern
> 
> Use this:
> 
> ```text
> {title}.{chapter}_{short_slug}.md
> ```
> 
> Examples:
> 
> ```text
> 02.03_qiserver_runtime.md
> 04.02_metadata_tags_links.md
> 09.02_erm_people_vendors_government.md
> 13.03_housing_tenant_records.md
> ```
> 
> Inside each file:
> 
> ```markdown
> ---
> qicode: "02.03"
> title: "QiServer Runtime"
> status: active
> type: code_chapter
> updated: 2026-06-25
> ---
> 
> # QiCode § 02.03 — QiServer Runtime
> 
> ## § 02.03.001 — Scope
> 
> ## § 02.03.002 — Cockpit
> 
> ## § 02.03.003 — Runtime Services
> 
> ## § 02.03.004 — Cloudflare Placement
> 
> ## § 02.03.005 — Boundaries
> ```
> 
> # Final Structure Rule
> 
> The clean law-book version is:
> 
> ```text
> QiCode
> ├── Titles = stable categories
> ├── Chapters = actual files
> ├── Sections = precise rules/headings
> ├── Properties = detail
> └── Cross-references = glue
> ```
> 
> The trap is thinking every concept deserves a folder. It does not.
> 
> Your guiding rule should be:
> 
> > **If two things are usually edited together, reviewed together, or understood together, they belong in the same chapter page.**
> 
> That keeps the legal-code structure powerful instead of becoming a bureaucratic goblin nest.

### User
> that seems like alot of seperate sections, can you reduce it by half.

### Assistant
> Yes — you’re right. The last version was **too many chapter pages**. It had legal-code clarity, but it was creeping toward bureaucracy. Kill the bloat.
> 
> Here’s the reduced version: **same legal-code structure, about half the pages.**
> 
> # Lean QiCode Outline
> 
> ```text
> QiCode
> ├── 00_general
> │   ├── 00.01_scope_definitions_numbering.md
> │   └── 00.02_naming_status_conventions.md
> │
> ├── 01_doctrine
> │   ├── 01.01_qi_doctrine_principles.md
> │   └── 01.02_decision_rules.md
> │
> ├── 02_architecture
> │   ├── 02.01_qilabs_root_model.md
> │   ├── 02.02_qispark_docs_landing.md
> │   ├── 02.03_qiserver_runtime_cloudflare.md
> │   ├── 02.04_qidrive_records_evidence.md
> │   └── 02.05_qiapps_projects_integrations.md
> │
> ├── 03_operations
> │   ├── 03.01_workflows_sops_routines.md
> │   └── 03.02_maintenance_incidents_deployment.md
> │
> ├── 04_data_records
> │   ├── 04.01_records_metadata_links.md
> │   └── 04.02_evidence_audit_import_export.md
> │
> ├── 05_qilife
> │   ├── 05.01_planner_activities_routines.md
> │   ├── 05.02_erm_people_vendors_government.md
> │   └── 05.03_workbench_projects_journal_creative.md
> │
> ├── 06_security_access
> │   ├── 06.01_accounts_permissions_devices.md
> │   └── 06.02_secrets_incidents_recovery.md
> │
> ├── 07_governance
> │   ├── 07.01_decisions_standards_templates.md
> │   └── 07.02_change_control_deprecation.md
> │
> ├── 08_finance_assets
> │   ├── 08.01_finance_inventory_reimbursements.md
> │   └── 08.02_assets_debts_reports.md
> │
> ├── 09_legal_matters
> │   ├── 09.01_contracts_notices_housing.md
> │   └── 09.02_disputes_claims_client_matters.md
> │
> ├── 10_publication
> │   ├── 10.01_publication_registry.md
> │   └── 10.02_series_books_posts_pages.md
> │
> ├── 90_archive
> │   └── 90.01_archive_deprecated_quarantine.md
> │
> └── 99_experimental
>     └── 99.01_prototypes_research_parking_lot.md
> ```
> 
> That’s **27 chapter pages** instead of 51.
> 
> Much better.
> 
> ---
> 
> # Even Cleaner: Top-Level Only
> 
> If we’re being ruthless, the top-level titles become:
> 
> ```text
> 00_general
> 01_doctrine
> 02_architecture
> 03_operations
> 04_data_records
> 05_qilife
> 06_security_access
> 07_governance
> 08_finance_assets
> 09_legal_matters
> 10_publication
> 90_archive
> 99_experimental
> ```
> 
> That’s **13 title folders**.
> 
> I would **not** go much lower than this, because then unrelated things start getting shoved together and the system gets muddy.
> 
> ---
> 
> # Reduced Internal Outline
> 
> ## `00_general`
> 
> ```text
> 00.01 — Scope, Definitions & Numbering
> ├── § 00.01.001 — Purpose
> ├── § 00.01.002 — Scope
> ├── § 00.01.003 — Definitions
> ├── § 00.01.004 — Citation Format
> └── § 00.01.005 — Numbering Rules
> 
> 00.02 — Naming, Status & Conventions
> ├── § 00.02.001 — Naming Rules
> ├── § 00.02.002 — Canonical Terms
> ├── § 00.02.003 — Retired Terms
> ├── § 00.02.004 — Status Labels
> └── § 00.02.005 — File Conventions
> ```
> 
> ---
> 
> ## `01_doctrine`
> 
> ```text
> 01.01 — Qi Doctrine & Principles
> ├── § 01.01.001 — Core Doctrine
> ├── § 01.01.002 — System Purpose
> ├── § 01.01.003 — Modularity
> ├── § 01.01.004 — Minimum Viable Structure
> └── § 01.01.005 — Human-First Operations
> 
> 01.02 — Decision Rules
> ├── § 01.02.001 — Merge Before Splitting
> ├── § 01.02.002 — Properties Before New Tables
> ├── § 01.02.003 — Folders Must Earn Existence
> ├── § 01.02.004 — No Placeholder Architecture
> └── § 01.02.005 — Archive Instead of Deleting
> ```
> 
> This is the control layer. Keep it.
> 
> ---
> 
> ## `02_architecture`
> 
> ```text
> 02.01 — QiLabs Root Model
> ├── § 02.01.001 — Canonical Root Structure
> ├── § 02.01.002 — Workspace Layer
> ├── § 02.01.003 — Docs Layer
> ├── § 02.01.004 — Runtime Layer
> ├── § 02.01.005 — Records Layer
> └── § 02.01.006 — Apps Layer
> 
> 02.02 — QiSpark Docs & Landing
> ├── § 02.02.001 — QiSpark Scope
> ├── § 02.02.002 — Docs Site Role
> ├── § 02.02.003 — Landing Page Role
> ├── § 02.02.004 — QiDNA Placement
> └── § 02.02.005 — Navigation Model
> 
> 02.03 — QiServer Runtime & Cloudflare
> ├── § 02.03.001 — QiServer Scope
> ├── § 02.03.002 — Cockpit
> ├── § 02.03.003 — Runtime Services
> ├── § 02.03.004 — Cloudflare / Zero Trust
> └── § 02.03.005 — Backups, Secrets & Recovery
> 
> 02.04 — QiDrive Records & Evidence
> ├── § 02.04.001 — QiDrive Scope
> ├── § 02.04.002 — Drive Mirror
> ├── § 02.04.003 — Evidence Libraries
> ├── § 02.04.004 — Retention
> └── § 02.04.005 — Export Bundles
> 
> 02.05 — QiApps, Projects & Integrations
> ├── § 02.05.001 — QiApps Scope
> ├── § 02.05.002 — App Registry
> ├── § 02.05.003 — Project Standards
> ├── § 02.05.004 — Shared Components
> └── § 02.05.005 — External Integrations
> ```
> 
> This is the heart of the system. Five pages is reasonable.
> 
> ---
> 
> ## `03_operations`
> 
> ```text
> 03.01 — Workflows, SOPs & Routines
> ├── § 03.01.001 — Workflow Standard
> ├── § 03.01.002 — SOP Standard
> ├── § 03.01.003 — Routine Standard
> ├── § 03.01.004 — Checklist Standard
> └── § 03.01.005 — Runbook Standard
> 
> 03.02 — Maintenance, Incidents & Deployment
> ├── § 03.02.001 — Maintenance
> ├── § 03.02.002 — Incident Levels
> ├── § 03.02.003 — Recovery Process
> ├── § 03.02.004 — Deployment Process
> └── § 03.02.005 — Rollback Process
> ```
> 
> Good merge. No need for separate deployment page yet.
> 
> ---
> 
> ## `04_data_records`
> 
> ```text
> 04.01 — Records, Metadata & Links
> ├── § 04.01.001 — Record Definition
> ├── § 04.01.002 — Record Types
> ├── § 04.01.003 — Metadata
> ├── § 04.01.004 — Tags
> └── § 04.01.005 — Links & Relationships
> 
> 04.02 — Evidence, Audit, Import & Export
> ├── § 04.02.001 — Evidence Definition
> ├── § 04.02.002 — Audit Trail
> ├── § 04.02.003 — Retention Rules
> ├── § 04.02.004 — Import Standard
> └── § 04.02.005 — Export Standard
> ```
> 
> Records and metadata belong together. Evidence and import/export can live together for now.
> 
> ---
> 
> ## `05_qilife`
> 
> ```text
> 05.01 — Planner, Activities & Routines
> ├── § 05.01.001 — Inbox
> ├── § 05.01.002 — Today
> ├── § 05.01.003 — Calendar
> ├── § 05.01.004 — Tasks
> ├── § 05.01.005 — Activities
> └── § 05.01.006 — Routines
> 
> 05.02 — ERM: People, Vendors & Government
> ├── § 05.02.001 — People
> ├── § 05.02.002 — Vendors
> ├── § 05.02.003 — Government
> ├── § 05.02.004 — Relationships
> └── § 05.02.005 — Communication History
> 
> 05.03 — Workbench: Projects, Journal & Creative
> ├── § 05.03.001 — Projects
> ├── § 05.03.002 — Notes
> ├── § 05.03.003 — Journal
> ├── § 05.03.004 — Creative Work
> └── § 05.03.005 — Research
> ```
> 
> This is tight. Planner, ERM, Workbench. That matches your actual mental model.
> 
> ---
> 
> ## `06_security_access`
> 
> ```text
> 06.01 — Accounts, Permissions & Devices
> ├── § 06.01.001 — Account Registry
> ├── § 06.01.002 — Roles
> ├── § 06.01.003 — Permissions
> ├── § 06.01.004 — Devices
> └── § 06.01.005 — Access Review
> 
> 06.02 — Secrets, Incidents & Recovery
> ├── § 06.02.001 — Passwords
> ├── § 06.02.002 — API Keys
> ├── § 06.02.003 — Recovery Codes
> ├── § 06.02.004 — Security Incidents
> └── § 06.02.005 — Credential Rotation
> ```
> 
> Two pages. Enough.
> 
> ---
> 
> ## `07_governance`
> 
> ```text
> 07.01 — Decisions, Standards & Templates
> ├── § 07.01.001 — Decision Records
> ├── § 07.01.002 — Standards
> ├── § 07.01.003 — Templates
> ├── § 07.01.004 — Forms
> └── § 07.01.005 — Versioning
> 
> 07.02 — Change Control & Deprecation
> ├── § 07.02.001 — Change Requests
> ├── § 07.02.002 — Migration Rules
> ├── § 07.02.003 — Deprecation Rules
> ├── § 07.02.004 — Supersession
> └── § 07.02.005 — Review Cycle
> ```
> 
> Decision records, standards, and templates are all governance tools. One page. Done.
> 
> ---
> 
> ## `08_finance_assets`
> 
> ```text
> 08.01 — Finance, Inventory & Reimbursements
> ├── § 08.01.001 — Accounts
> ├── § 08.01.002 — Transactions
> ├── § 08.01.003 — Receipts
> ├── § 08.01.004 — Inventory
> └── § 08.01.005 — Reimbursements
> 
> 08.02 — Assets, Debts & Reports
> ├── § 08.02.001 — Assets
> ├── § 08.02.002 — Property
> ├── § 08.02.003 — Debts
> ├── § 08.02.004 — Claims
> └── § 08.02.005 — Reports
> ```
> 
> This is enough until finance becomes a full app.
> 
> ---
> 
> ## `09_legal_matters`
> 
> ```text
> 09.01 — Contracts, Notices & Housing
> ├── § 09.01.001 — Contracts
> ├── § 09.01.002 — Agreements
> ├── § 09.01.003 — Notices
> ├── § 09.01.004 — Housing Records
> └── § 09.01.005 — Deadlines
> 
> 09.02 — Disputes, Claims & Client Matters
> ├── § 09.02.001 — Disputes
> ├── § 09.02.002 — Claims
> ├── § 09.02.003 — Evidence Packets
> ├── § 09.02.004 — Client Matters
> └── § 09.02.005 — Case Timelines
> ```
> 
> This is cleaner than separate housing/client/dispute pages.
> 
> ---
> 
> ## `10_publication`
> 
> ```text
> 10.01 — Publication Registry
> ├── § 10.01.001 — Work Types
> ├── § 10.01.002 — Draft Status
> ├── § 10.01.003 — Publication Status
> ├── § 10.01.004 — Platforms
> └── § 10.01.005 — Canonical Versions
> 
> 10.02 — Series, Books, Posts & Pages
> ├── § 10.02.001 — Series
> ├── § 10.02.002 — Books
> ├── § 10.02.003 — Chapters
> ├── § 10.02.004 — Essays / Posts
> └── § 10.02.005 — Public Pages
> ```
> 
> This handles your blog/book/series idea without creating a whole separate library monster.
> 
> ---
> 
> ## `90_archive`
> 
> ```text
> 90.01 — Archive, Deprecated & Quarantine
> ├── § 90.01.001 — Archive Rules
> ├── § 90.01.002 — Superseded Items
> ├── § 90.01.003 — Deprecated Items
> ├── § 90.01.004 — Quarantine
> └── § 90.01.005 — Cleanup Rules
> ```
> 
> One archive page. Perfect.
> 
> ---
> 
> ## `99_experimental`
> 
> ```text
> 99.01 — Prototypes, Research & Parking Lot
> ├── § 99.01.001 — Prototypes
> ├── § 99.01.002 — Research
> ├── § 99.01.003 — Future Concepts
> ├── § 99.01.004 — Evaluation
> └── § 99.01.005 — Promote / Kill Rules
> ```
> 
> One experimental page. Also perfect.
> 
> ---
> 
> # Better Starting Set
> 
> Start with only these **10 pages**:
> 
> ```text
> 00.01_scope_definitions_numbering.md
> 00.02_naming_status_conventions.md
> 01.01_qi_doctrine_principles.md
> 01.02_decision_rules.md
> 02.01_qilabs_root_model.md
> 02.02_qispark_docs_landing.md
> 02.03_qiserver_runtime_cloudflare.md
> 02.04_qidrive_records_evidence.md
> 02.05_qiapps_projects_integrations.md
> 05.01_planner_activities_routines.md
> ```
> 
> Then add these next:
> 
> ```text
> 04.01_records_metadata_links.md
> 07.01_decisions_standards_templates.md
> 09.01_contracts_notices_housing.md
> 10.02_series_books_posts_pages.md
> 90.01_archive_deprecated_quarantine.md
> ```
> 
> That gives you a powerful system with **15 useful pages**, not 50 pretend-important ones.
> 
> # My Recommendation
> 
> Use this reduced model:
> 
> ```text
> 13 title folders
> 27 possible pages
> 10–15 pages created first
> sections inside pages only
> ```
> 
> That’s the right balance.
> 
> The legal-code style is useful because it gives you **referenceable authority**:
> 
> ```text
> QiCode § 01.02.003 — Folders Must Earn Existence
> QiCode § 02.03.004 — Cloudflare / Zero Trust
> QiCode § 05.01.005 — Activities
> QiCode § 09.01.004 — Housing Records
> ```
> 
> But the actual filesystem stays lean. That’s the win.

### User
> thats better is everything properly grouped and build upon eacher, it important that one not have to jump between sections it should each topic builds upon the last, you know?

### Assistant
> Yes — **mostly**, but not perfectly.
> 
> The reduced version is grouped well by topic, but the **sequence needs tightening** so each section builds on the previous one instead of making you jump around.
> 
> The main issue:
> 
> > `04_data_records` should come **before** QiDrive, QiLife, legal matters, finance, and publication because records are the common substrate.
> 
> Also:
> 
> > `governance` should come earlier than finance/legal/publication because decisions, standards, and templates control how those later systems behave.
> 
> So I’d reorder the code like this.
> 
> # Better Build Order
> 
> ```text id="ef3a3c"
> QiCode
> ├── 00_general
> ├── 01_doctrine
> ├── 02_governance
> ├── 03_architecture
> ├── 04_data_records
> ├── 05_operations
> ├── 06_qispark
> ├── 07_qiserver
> ├── 08_qidrive
> ├── 09_qiapps
> ├── 10_qilife
> ├── 11_security_access
> ├── 12_finance_assets
> ├── 13_legal_matters
> ├── 14_publication
> ├── 90_archive
> └── 99_experimental
> ```
> 
> This reads more naturally:
> 
> ```text id="chpy4r"
> What is this?           → General
> Why does it exist?      → Doctrine
> How are decisions made? → Governance
> What is the system?     → Architecture
> What are records?       → Data/Records
> How does work happen?   → Operations
> Where do docs live?     → QiSpark
> Where does runtime live?→ QiServer
> Where do files live?    → QiDrive
> Where do apps live?     → QiApps
> How does life run?      → QiLife
> How is access secured?  → Security
> How is money tracked?   → Finance
> How are legal matters tracked? → Legal
> How is work published?  → Publication
> What is old/unsafe?     → Archive / Experimental
> ```
> 
> That’s cleaner.
> 
> ---
> 
> # Revised Lean Outline
> 
> ```text id="uk34e4"
> QiCode
> ├── 00_general
> │   ├── 00.01_scope_definitions_numbering.md
> │   └── 00.02_naming_status_conventions.md
> │
> ├── 01_doctrine
> │   ├── 01.01_qi_doctrine_principles.md
> │   └── 01.02_decision_rules.md
> │
> ├── 02_governance
> │   ├── 02.01_decisions_standards_templates.md
> │   └── 02.02_change_control_deprecation.md
> │
> ├── 03_architecture
> │   ├── 03.01_qilabs_root_model.md
> │   ├── 03.02_qispark_docs_landing.md
> │   ├── 03.03_qiserver_runtime_cloudflare.md
> │   ├── 03.04_qidrive_records_evidence.md
> │   └── 03.05_qiapps_projects_integrations.md
> │
> ├── 04_data_records
> │   ├── 04.01_records_metadata_links.md
> │   └── 04.02_evidence_audit_import_export.md
> │
> ├── 05_operations
> │   ├── 05.01_workflows_sops_routines.md
> │   └── 05.02_maintenance_incidents_deployment.md
> │
> ├── 06_qilife
> │   ├── 06.01_planner_activities_routines.md
> │   ├── 06.02_erm_people_vendors_government.md
> │   └── 06.03_workbench_projects_journal_creative.md
> │
> ├── 07_security_access
> │   ├── 07.01_accounts_permissions_devices.md
> │   └── 07.02_secrets_incidents_recovery.md
> │
> ├── 08_finance_assets
> │   ├── 08.01_finance_inventory_reimbursements.md
> │   └── 08.02_assets_debts_reports.md
> │
> ├── 09_legal_matters
> │   ├── 09.01_contracts_notices_housing.md
> │   └── 09.02_disputes_claims_client_matters.md
> │
> ├── 10_publication
> │   ├── 10.01_publication_registry.md
> │   └── 10.02_series_books_posts_pages.md
> │
> ├── 90_archive
> │   └── 90.01_archive_deprecated_quarantine.md
> │
> └── 99_experimental
>     └── 99.01_prototypes_research_parking_lot.md
> ```
> 
> This is **better than the previous version** because it has a stronger learning path.
> 
> ---
> 
> # One Important Correction
> 
> I would **not** separate QiSpark, QiServer, QiDrive, and QiApps into their own title folders yet.
> 
> Why?
> 
> Because they are already explained under `03_architecture`.
> 
> If you split them into their own full titles right now, the user has to jump:
> 
> ```text id="ehf3xm"
> 03_architecture says QiServer exists
> then later 07_qiserver explains QiServer again
> ```
> 
> That creates cross-reference hell.
> 
> For now, keep them as **architecture chapters**, not separate title folders.
> 
> Later, if one grows huge, promote it.
> 
> So this is better:
> 
> ```text id="0kiurn"
> 03_architecture/
> ├── 03.01_qilabs_root_model.md
> ├── 03.02_qispark_docs_landing.md
> ├── 03.03_qiserver_runtime_cloudflare.md
> ├── 03.04_qidrive_records_evidence.md
> └── 03.05_qiapps_projects_integrations.md
> ```
> 
> Not this yet:
> 
> ```text id="llxepj"
> 06_qispark/
> 07_qiserver/
> 08_qidrive/
> 09_qiapps/
> ```
> 
> That would be premature folder multiplication. Classic little goblin move. We are not doing that.
> 
> ---
> 
> # Does Each Topic Build Properly?
> 
> ## Yes, with this flow:
> 
> ### `00_general`
> Defines the whole code system.
> 
> ### `01_doctrine`
> Explains the operating philosophy.
> 
> ### `02_governance`
> Explains how decisions, standards, templates, and changes are controlled.
> 
> ### `03_architecture`
> Explains the system map: QiLabs, QiSpark, QiServer, QiDrive, QiApps.
> 
> ### `04_data_records`
> Explains the information substrate: records, metadata, tags, links, evidence.
> 
> ### `05_operations`
> Explains how work happens: workflows, SOPs, routines, maintenance, incidents, deployment.
> 
> ### `06_qilife`
> Applies the system to daily/life operations.
> 
> ### `07_security_access`
> Secures the system after the structure is understood.
> 
> ### `08_finance_assets`
> Uses records + operations for money, assets, inventory, reimbursements.
> 
> ### `09_legal_matters`
> Uses records + evidence + timelines for disputes, housing, client matters.
> 
> ### `10_publication`
> Uses QiSpark + records + creative work to publish essays, posts, books, pages.
> 
> ### `90_archive`
> Handles old/superseded/deprecated/quarantined material.
> 
> ### `99_experimental`
> Captures ideas before they deserve promotion.
> 
> That builds correctly.
> 
> ---
> 
> # Best Final Top-Level Version
> 
> This is the one I’d use:
> 
> ```text id="19t06n"
> QiCode
> ├── 00_general
> ├── 01_doctrine
> ├── 02_governance
> ├── 03_architecture
> ├── 04_data_records
> ├── 05_operations
> ├── 06_qilife
> ├── 07_security_access
> ├── 08_finance_assets
> ├── 09_legal_matters
> ├── 10_publication
> ├── 90_archive
> └── 99_experimental
> ```
> 
> # Better Starting Pages
> 
> Start with these **12**, in this exact order:
> 
> ```text id="ey1yi7"
> 00.01_scope_definitions_numbering.md
> 00.02_naming_status_conventions.md
> 
> 01.01_qi_doctrine_principles.md
> 01.02_decision_rules.md
> 
> 02.01_decisions_standards_templates.md
> 02.02_change_control_deprecation.md
> 
> 03.01_qilabs_root_model.md
> 03.02_qispark_docs_landing.md
> 03.03_qiserver_runtime_cloudflare.md
> 03.04_qidrive_records_evidence.md
> 03.05_qiapps_projects_integrations.md
> 
> 04.01_records_metadata_links.md
> ```
> 
> Then stop.
> 
> Do **not** build the rest until needed.
> 
> # Final Verdict
> 
> The grouping is now coherent.
> 
> The build path is:
> 
> ```text id="ayvznm"
> Rules → Principles → Governance → Architecture → Records → Operations → Applications
> ```
> 
> That is the right spine.
> 
> The previous version was organized by category.  
> This version is organized by **dependency**.
> 
> That’s the difference.

### User
> also dont forget to include the life sections like the jorunalling and timeline those are like the spine almsot of all this.

### Assistant
> Yes — good catch. That was the missing spine.
> 
> The correction is:
> 
> > **Timeline + Journal should not be buried under QiLife Workbench.**  
> > They are not just “life app features.” They are the **chronological memory layer** for everything.
> 
> So we should replace `04_data_records` with:
> 
> ```text id="yfmd1e"
> 04_chronicle_records
> ```
> 
> Because the real order is:
> 
> ```text id="0c6m0m"
> What happened?      → Timeline / Journal
> What proves it?     → Records / Evidence
> What do we do next? → Operations / Planner
> ```
> 
> That’s much stronger.
> 
> # Revised Build Order
> 
> ```text id="de4hzx"
> QiCode
> ├── 00_general
> ├── 01_doctrine
> ├── 02_governance
> ├── 03_architecture
> ├── 04_chronicle_records
> ├── 05_operations
> ├── 06_qilife
> ├── 07_security_access
> ├── 08_finance_assets
> ├── 09_legal_matters
> ├── 10_publication
> ├── 90_archive
> └── 99_experimental
> ```
> 
> This keeps the system lean, but now the emotional/legal/life/logging spine is in the right place.
> 
> ---
> 
> # The Key Distinction
> 
> ## `04_chronicle_records`
> 
> This is the **source-of-truth memory layer**.
> 
> It answers:
> 
> ```text id="evsbti"
> What happened?
> When did it happen?
> Who was involved?
> What records support it?
> What evidence proves it?
> What changed afterward?
> ```
> 
> ## `06_qilife`
> 
> This is the **life operating interface**.
> 
> It answers:
> 
> ```text id="xu5h6k"
> What do I need to do today?
> Who am I managing relationships with?
> What projects am I working on?
> What routines keep life stable?
> ```
> 
> So:
> 
> ```text id="xlfp1c"
> Timeline / Journal = spine
> QiLife = dashboard
> Records = proof
> Operations = action
> ```
> 
> That’s the clean model.
> 
> ---
> 
> # Updated Lean Outline
> 
> ```text id="yh4ld8"
> QiCode
> ├── 00_general
> │   ├── 00.01_scope_definitions_numbering.md
> │   └── 00.02_naming_status_conventions.md
> │
> ├── 01_doctrine
> │   ├── 01.01_qi_doctrine_principles.md
> │   └── 01.02_decision_rules.md
> │
> ├── 02_governance
> │   ├── 02.01_decisions_standards_templates.md
> │   └── 02.02_change_control_deprecation.md
> │
> ├── 03_architecture
> │   ├── 03.01_qilabs_root_model.md
> │   ├── 03.02_qispark_docs_landing.md
> │   ├── 03.03_qiserver_runtime_cloudflare.md
> │   ├── 03.04_qidrive_records_evidence.md
> │   └── 03.05_qiapps_projects_integrations.md
> │
> ├── 04_chronicle_records
> │   ├── 04.01_timeline_journal_chronicle.md
> │   ├── 04.02_records_metadata_links.md
> │   └── 04.03_evidence_audit_import_export.md
> │
> ├── 05_operations
> │   ├── 05.01_workflows_sops_routines.md
> │   └── 05.02_maintenance_incidents_deployment.md
> │
> ├── 06_qilife
> │   ├── 06.01_planner_activities_routines.md
> │   ├── 06.02_erm_people_vendors_government.md
> │   └── 06.03_workbench_projects_creative.md
> │
> ├── 07_security_access
> │   ├── 07.01_accounts_permissions_devices.md
> │   └── 07.02_secrets_incidents_recovery.md
> │
> ├── 08_finance_assets
> │   ├── 08.01_finance_inventory_reimbursements.md
> │   └── 08.02_assets_debts_reports.md
> │
> ├── 09_legal_matters
> │   ├── 09.01_contracts_notices_housing.md
> │   └── 09.02_disputes_claims_client_matters.md
> │
> ├── 10_publication
> │   ├── 10.01_publication_registry.md
> │   └── 10.02_series_books_posts_pages.md
> │
> ├── 90_archive
> │   └── 90.01_archive_deprecated_quarantine.md
> │
> └── 99_experimental
>     └── 99.01_prototypes_research_parking_lot.md
> ```
> 
> That’s **still lean**: 12 title folders, 27 pages max.
> 
> ---
> 
> # New Core Page: `04.01_timeline_journal_chronicle.md`
> 
> This page matters. It should come before normal records because it explains how lived events become structured memory.
> 
> ```text id="i0fdc6"
> 04.01 — Timeline, Journal & Chronicle
> ├── § 04.01.001 — Chronicle Purpose
> ├── § 04.01.002 — Timeline Events
> ├── § 04.01.003 — Journal Entries
> ├── § 04.01.004 — Daily Logs
> ├── § 04.01.005 — Incident Logs
> ├── § 04.01.006 — Relationship Notes
> ├── § 04.01.007 — Decision Notes
> ├── § 04.01.008 — Evidence Links
> └── § 04.01.009 — Review / Reconstruction
> ```
> 
> That gives you the spine without creating 12 separate diary/timeline/log folders.
> 
> ---
> 
> # How It Builds Now
> 
> ```text id="j2zv6d"
> 00_general
> Defines the code system.
> 
> 01_doctrine
> Defines the principles.
> 
> 02_governance
> Defines how decisions and changes are controlled.
> 
> 03_architecture
> Defines the system map.
> 
> 04_chronicle_records
> Defines how life/events/records become memory.
> 
> 05_operations
> Defines how actions happen from that memory.
> 
> 06_qilife
> Defines the daily dashboard built on top of the memory layer.
> 
> 07_security_access
> Protects the system.
> 
> 08_finance_assets
> Applies the record/timeline model to money and property.
> 
> 09_legal_matters
> Applies the record/timeline/evidence model to disputes, housing, and clients.
> 
> 10_publication
> Turns selected knowledge into public work.
> 
> 90_archive
> Controls old material.
> 
> 99_experimental
> Captures unproven ideas.
> ```
> 
> This now builds correctly.
> 
> ---
> 
> # The Clean Mental Model
> 
> Use this:
> 
> ```text id="txoiu3"
> Chronicle = what happened
> Records = what exists
> Evidence = what proves it
> Operations = what to do
> QiLife = how I live with it
> Governance = how it changes
> Publication = what gets shared
> ```
> 
> That’s the actual system.
> 
> # Final Verdict
> 
> Yes — timeline and journaling should be **promoted**.
> 
> Not as extra bloat. As the center spine.
> 
> So the best correction is:
> 
> ```text id="7gk30s"
> 04_data_records
> ```
> 
> becomes:
> 
> ```text id="olnlug"
> 04_chronicle_records
> ```
> 
> And `journal` comes out of `06.03_workbench_projects_journal_creative.md`, because it is too important to be tucked away like a side notebook.
> 
> Revised:
> 
> ```text id="s66z1f"
> 06.03_workbench_projects_creative.md
> ```
> 
> No journal there. Journal belongs in the Chronicle.

### User
> ok can you give me all the sections in csv so i can import them into notion

### Assistant
> Yep. I’ll give you a Notion-friendly CSV with one row per **section**, plus hierarchy fields so you can sort/filter without creating chaos.

### Assistant
> Done — I made the Notion-ready CSV:
> 
> [Download the QiCode sections CSV](sandbox:/mnt/data/qicode_sections_notion_import.csv)
> 
> It has **151 section rows** with columns for:
> 
> ```text
> Sort Key
> QiCode
> Title Number
> Title
> Chapter Code
> Chapter
> Section Code
> Section
> Level
> Parent Code
> Path
> Status
> Notes
> ```
> 
> The important part for Notion is that you can sort by **Sort Key** and group by **Title** or **Chapter**. That keeps the law-code order intact without forcing nested folders.

### User
> what would the title of this book be?

### Assistant
> The strongest title is:
> 
> # **QiCode**
> 
> Subtitle:
> 
> ## **The Operating Code of the Qi System**
> 
> That’s clean, durable, and flexible. It sounds like a legal code, a doctrine book, and a technical manual without trying too hard.
> 
> Full cover-style title:
> 
> ```text
> QiCode
> The Operating Code of the Qi System
> ```
> 
> # Best Alternatives
> 
> ## **QiCode: The Canon**
> Good if you want it to feel more sacred/doctrinal.
> 
> ## **QiCode: General Laws of the Qi System**
> More law-book energy, but a little stiff.
> 
> ## **QiCode: The Qi Operating Canon**
> Nice blend of operating system + doctrine.
> 
> ## **The Qi Code**
> More readable to outsiders, but slightly less branded than `QiCode`.
> 
> ## **QiCode: The Living System Manual**
> Clearer and more practical, but less elegant.
> 
> # My Pick
> 
> Use:
> 
> ```text
> QiCode
> The Operating Code of the Qi System
> ```
> 
> And internally, refer to it like:
> 
> ```text
> QiCode § 04.01.002 — Timeline Events
> ```
> 
> That gives you the exact vibe: **law book + operating manual + doctrine spine**.

### User
> what woudl the chapter templates or page tempaltes be.

### Assistant
> Yes. Don’t make a separate template for every title. That’s how Notion becomes a glitter-covered landfill.
> 
> Use **three templates only**:
> 
> 1. **Title Landing Page** — for `04_chronicle_records`, `06_qilife`, etc.
> 2. **Chapter Page** — for pages like `04.01_timeline_journal_chronicle`
> 3. **Section / Code Entry** — for individual Notion database rows like `§ 04.01.002 — Timeline Events`
> 
> # Template 1 — Title Landing Page
> 
> Use this for each major folder/title.
> 
> :::writing{variant="document" id="72184"}
> ---
> qicode_title: "04"
> title: "Chronicle & Records"
> status: active
> type: title_landing
> owner: Cody
> updated: 2026-06-25
> ---
> 
> # Title 04 — Chronicle & Records
> 
> ## Purpose
> 
> This title governs how lived events, journal entries, timelines, records, evidence, and supporting materials are captured, linked, reviewed, and preserved inside the Qi system.
> 
> ## Scope
> 
> This title covers:
> 
> - Timeline events
> - Journal entries
> - Daily logs
> - Incident logs
> - Relationship notes
> - Decision notes
> - Records
> - Metadata
> - Evidence
> - Audit trails
> - Import/export standards
> 
> ## Dependency
> 
> This title depends on:
> 
> - Title 00 — General
> - Title 01 — Doctrine
> - Title 02 — Governance
> - Title 03 — Architecture
> 
> This title supports:
> 
> - Title 05 — Operations
> - Title 06 — QiLife
> - Title 08 — Finance & Assets
> - Title 09 — Legal Matters
> - Title 10 — Publication
> 
> ## Chapters
> 
> | Chapter | Name | Purpose | Status |
> |---|---|---|---|
> | 04.01 | Timeline, Journal & Chronicle | Defines the chronological spine of the system. | draft |
> | 04.02 | Records, Metadata & Links | Defines structured records and relationships. | draft |
> | 04.03 | Evidence, Audit, Import & Export | Defines proof, audit trails, retention, and portability. | draft |
> 
> ## Rules of This Title
> 
> 1. Chronicle entries capture what happened.
> 2. Records structure what exists.
> 3. Evidence proves or supports what happened.
> 4. Operations act on chronicle and record data.
> 5. No record exists without a clear purpose, status, and relationship to the system.
> 
> ## Open Questions
> 
> - What needs to be clarified?
> - What sections are incomplete?
> - What should be merged or removed?
> 
> ## Related References
> 
> - QiCode § 01.02.001 — Merge Before Splitting
> - QiCode § 01.02.003 — Folders Must Earn Existence
> - QiCode § 04.01.001 — Chronicle Purpose
> :::
> 
> ---
> 
> # Template 2 — Chapter Page
> 
> This is the main one. Most of your actual work should live here.
> 
> :::writing{variant="document" id="52906"}
> ---
> qicode: "04.01"
> title: "Timeline, Journal & Chronicle"
> status: draft
> type: code_chapter
> parent_title: "04_chronicle_records"
> owner: Cody
> updated: 2026-06-25
> ---
> 
> # QiCode § 04.01 — Timeline, Journal & Chronicle
> 
> ## Chapter Purpose
> 
> This chapter defines the chronological memory spine of the Qi system: how events, journal entries, logs, decisions, incidents, relationships, and evidence links are captured and reviewed.
> 
> ## Plain-English Summary
> 
> The Chronicle answers:
> 
> - What happened?
> - When did it happen?
> - Who was involved?
> - What changed?
> - What evidence supports it?
> - What needs to happen next?
> 
> ## Scope
> 
> This chapter covers:
> 
> - Timeline events
> - Journal entries
> - Daily logs
> - Incident logs
> - Relationship notes
> - Decision notes
> - Evidence links
> - Review and reconstruction
> 
> This chapter does not cover:
> 
> - Full evidence storage rules
> - Financial accounting rules
> - Legal matter strategy
> - Publication formatting
> 
> Those belong in their own chapters.
> 
> ## Dependency
> 
> Before this chapter:
> 
> - QiCode § 00 — General
> - QiCode § 01 — Doctrine
> - QiCode § 02 — Governance
> - QiCode § 03 — Architecture
> 
> After this chapter:
> 
> - QiCode § 04.02 — Records, Metadata & Links
> - QiCode § 05.01 — Workflows, SOPs & Routines
> - QiCode § 06.01 — Planner, Activities & Routines
> 
> ---
> 
> ## § 04.01.001 — Chronicle Purpose
> 
> ### Rule
> 
> The Chronicle is the chronological memory spine of the Qi system.
> 
> ### Meaning
> 
> It captures lived events, observations, decisions, incidents, and relevant context before they become tasks, legal records, financial claims, publications, or archived knowledge.
> 
> ### Use When
> 
> Use this section when deciding whether something belongs in the timeline, journal, daily log, incident log, or another structured record.
> 
> ### Related Sections
> 
> - QiCode § 04.02.001 — Record Definition
> - QiCode § 04.03.001 — Evidence Definition
> - QiCode § 05.01.001 — Workflow Standard
> 
> ---
> 
> ## § 04.01.002 — Timeline Events
> 
> ### Rule
> 
> A timeline event records something that happened at a specific or approximate time and may later need to be reconstructed, searched, proven, reviewed, or acted on.
> 
> ### Meaning
> 
> Timeline events are not only legal events. They can include life events, operational events, relationship events, health events, financial events, housing events, project events, and system events.
> 
> ### Minimum Fields
> 
> - Date
> - Approximate time, if known
> - Event summary
> - People involved
> - Location or context
> - Related records
> - Related evidence
> - Follow-up needed
> - Status
> 
> ### Related Sections
> 
> - QiCode § 04.01.005 — Incident Logs
> - QiCode § 04.02.005 — Links & Relationships
> - QiCode § 09.02.005 — Case Timelines
> 
> ---
> 
> ## § 04.01.003 — Journal Entries
> 
> ### Rule
> 
> A journal entry captures subjective processing, reflection, emotional context, interpretation, or unresolved thoughts.
> 
> ### Meaning
> 
> Journal entries are allowed to be messy. They are not automatically evidence, tasks, or final truth. They are raw context that can later be distilled.
> 
> ### Use When
> 
> Use journal entries when the purpose is reflection, emotional processing, pattern recognition, or meaning-making.
> 
> ### Related Sections
> 
> - QiCode § 04.01.008 — Review / Reconstruction
> - QiCode § 06.03.002 — Notes
> - QiCode § 10.02.004 — Essays / Posts
> 
> ---
> 
> ## § 04.01.004 — Daily Logs
> 
> ### Rule
> 
> A daily log captures the operational reality of a day.
> 
> ### Meaning
> 
> Daily logs summarize what happened, what got done, what got blocked, what changed, and what needs to move forward.
> 
> ### Minimum Fields
> 
> - Date
> - Main events
> - Tasks completed
> - Blockers
> - Money/health/legal/housing notes, if relevant
> - Follow-up actions
> - Review status
> 
> ---
> 
> ## § 04.01.005 — Incident Logs
> 
> ### Rule
> 
> An incident log captures a disruptive, risky, harmful, confusing, or high-consequence event that may require review, response, evidence, or escalation.
> 
> ### Meaning
> 
> Not every bad day is an incident. An incident is something that may require reconstruction, proof, decision-making, protection, or corrective action.
> 
> ### Minimum Fields
> 
> - Date/time
> - What happened
> - People involved
> - Immediate impact
> - Evidence
> - Response taken
> - Follow-up needed
> - Status
> 
> ---
> 
> ## § 04.01.006 — Relationship Notes
> 
> ### Rule
> 
> Relationship notes capture relevant context about people, vendors, agencies, clients, family, collaborators, or institutions.
> 
> ### Meaning
> 
> Relationship notes should help preserve context without turning every feeling into a permanent judgment.
> 
> ### Use When
> 
> Use this for communication history, trust signals, obligations, boundaries, promises, conflicts, and important context.
> 
> ---
> 
> ## § 04.01.007 — Decision Notes
> 
> ### Rule
> 
> A decision note captures why a choice was made.
> 
> ### Meaning
> 
> Decision notes prevent future confusion, re-litigation, and repeated mental loops.
> 
> ### Minimum Fields
> 
> - Decision
> - Date
> - Context
> - Options considered
> - Reason chosen
> - Tradeoffs
> - Review date, if needed
> 
> ---
> 
> ## § 04.01.008 — Evidence Links
> 
> ### Rule
> 
> Chronicle entries may link to evidence, but they are not themselves the evidence repository.
> 
> ### Meaning
> 
> The Chronicle tells the story. Evidence supports the story. Keep those connected but not confused.
> 
> ---
> 
> ## § 04.01.009 — Review / Reconstruction
> 
> ### Rule
> 
> Chronicle entries should be reviewable and reconstructable.
> 
> ### Meaning
> 
> The system should allow a person to rebuild what happened without relying only on memory.
> 
> ### Review Questions
> 
> - What happened?
> - What proves it?
> - What is still unclear?
> - What changed afterward?
> - What action is needed?
> - Should this become a task, record, claim, publication, or archive item?
> :::
> 
> ---
> 
> # Template 3 — Section / Code Entry
> 
> Use this if each section becomes a Notion database item.
> 
> :::writing{variant="document" id="38471"}
> # § 04.01.002 — Timeline Events
> 
> ## Rule
> 
> A timeline event records something that happened at a specific or approximate time and may later need to be reconstructed, searched, proven, reviewed, or acted on.
> 
> ## Meaning
> 
> Timeline events are the chronological building blocks of the Qi system. They capture what happened before the system decides whether it becomes a task, record, incident, claim, publication, or archive item.
> 
> ## Use When
> 
> Use this section when logging:
> 
> - Life events
> - Legal or housing events
> - Financial events
> - Relationship events
> - Project events
> - Health or care events
> - System events
> - Incidents or conflicts
> 
> ## Minimum Fields
> 
> | Field | Purpose |
> |---|---|
> | Date | Anchors the event in time. |
> | Time | Adds precision when known. |
> | Summary | States what happened. |
> | People | Identifies who was involved. |
> | Location / Context | Explains where or under what circumstances it happened. |
> | Related Records | Links structured records. |
> | Related Evidence | Links proof or supporting material. |
> | Follow-Up Needed | Identifies next action. |
> | Status | Shows whether the event is raw, reviewed, resolved, archived, or escalated. |
> 
> ## Related Sections
> 
> - QiCode § 04.01.003 — Journal Entries
> - QiCode § 04.01.005 — Incident Logs
> - QiCode § 04.02.005 — Links & Relationships
> - QiCode § 09.02.005 — Case Timelines
> 
> ## Notes
> 
> Use timeline events for factual reconstruction. Use journal entries for processing and interpretation. Do not mix them unless the distinction is clearly marked.
> :::
> 
> ---
> 
> # Notion Property Setup
> 
> For the Notion database, I’d use this:
> 
> ```text
> Name
> QiCode
> Sort Key
> Title
> Chapter
> Section
> Type
> Status
> Parent Code
> Related Sections
> Applies To
> Priority
> Review Date
> Last Updated
> Notes
> ```
> 
> ## Best `Type` Options
> 
> ```text
> Title
> Chapter
> Section
> Rule
> Template
> Standard
> Record Type
> Workflow
> Reference
> Archive
> ```
> 
> ## Best `Status` Options
> 
> ```text
> draft
> active
> needs_review
> superseded
> deprecated
> archived
> ```
> 
> # My Recommendation
> 
> Use the **Chapter Page Template** as your main template.
> 
> The section template is useful only if you want every section to be its own Notion item. That’s powerful, but it can also become click-fatigue.
> 
> Best setup:
> 
> ```text
> Notion database = index of sections
> Actual content = chapter pages
> ```
> 
> That gives you structure without making you open 151 tiny pages like a cursed legal Advent calendar.

### User
> what is the title of this book, and what should each major section title say?

### Assistant
> The book title should be:
> 
> # **QiCode**
> 
> ## **The Chronicle and Operating Code of the Qi System**
> 
> That’s the best version now.
> 
> It keeps the legal-code feel, but it also acknowledges that this is not just a tech manual. It is part doctrine, part operating system, part life chronicle, part evidence spine.
> 
> Full title page:
> 
> ```text
> QiCode
> The Chronicle and Operating Code of the Qi System
> ```
> 
> Optional formal version:
> 
> ```text
> QiCode
> The Chronicle, Doctrine, and Operating Code of the Qi System
> ```
> 
> I’d use the shorter one. Cleaner. Less try-hard.
> 
> ---
> 
> # Major Section Titles
> 
> Use legal-book style:
> 
> ```text
> Title 00 — General Provisions
> Title 01 — Doctrine & Principles
> Title 02 — Governance & Standards
> Title 03 — System Architecture
> Title 04 — Chronicle & Records
> Title 05 — Operations & Workflows
> Title 06 — QiLife
> Title 07 — Security & Access
> Title 08 — Finance & Assets
> Title 09 — Legal Matters
> Title 10 — Publication & Works
> Title 90 — Archive & Quarantine
> Title 99 — Experimental
> ```
> 
> That’s the clean set.
> 
> ---
> 
> # What Each Major Section Should Say
> 
> | Code | Major Title | What It Means |
> |---:|---|---|
> | **Title 00** | **General Provisions** | Defines the purpose, scope, terms, numbering, citation style, naming rules, and status labels for the entire QiCode. |
> | **Title 01** | **Doctrine & Principles** | States the core philosophy of Qi: why it exists, how it thinks, what it values, and what rules prevent bloat. |
> | **Title 02** | **Governance & Standards** | Defines how decisions are made, how standards/templates are created, how changes happen, and how old decisions get superseded. |
> | **Title 03** | **System Architecture** | Explains the structure of QiLabs, QiSpark, QiServer, QiDrive, QiApps, and the major system layers. |
> | **Title 04** | **Chronicle & Records** | The spine. Defines timeline, journal, daily logs, incident logs, records, metadata, evidence, audit, import, and export. |
> | **Title 05** | **Operations & Workflows** | Defines how work happens: workflows, SOPs, routines, checklists, maintenance, incidents, deployment, and rollback. |
> | **Title 06** | **QiLife** | Defines the life operating interface: planner, activities, routines, people, vendors, government, projects, creative work, and research. |
> | **Title 07** | **Security & Access** | Defines accounts, permissions, devices, secrets, recovery codes, security incidents, and credential rotation. |
> | **Title 08** | **Finance & Assets** | Defines money, transactions, receipts, inventory, reimbursements, assets, property, debts, claims, and reports. |
> | **Title 09** | **Legal Matters** | Defines contracts, notices, housing records, disputes, claims, evidence packets, client matters, and case timelines. |
> | **Title 10** | **Publication & Works** | Defines creative/public output: series, books, chapters, essays, posts, public pages, platforms, and canonical versions. |
> | **Title 90** | **Archive & Quarantine** | Defines what happens to old, deprecated, superseded, duplicate, unsafe, or unresolved materials. |
> | **Title 99** | **Experimental** | Holds prototypes, research, future ideas, parking-lot concepts, and promote/kill rules. |
> 
> ---
> 
> # My Recommended Final Naming
> 
> This is the version I’d lock:
> 
> ```text
> QiCode
> The Chronicle and Operating Code of the Qi System
> 
> Title 00 — General Provisions
> Title 01 — Doctrine & Principles
> Title 02 — Governance & Standards
> Title 03 — System Architecture
> Title 04 — Chronicle & Records
> Title 05 — Operations & Workflows
> Title 06 — QiLife
> Title 07 — Security & Access
> Title 08 — Finance & Assets
> Title 09 — Legal Matters
> Title 10 — Publication & Works
> Title 90 — Archive & Quarantine
> Title 99 — Experimental
> ```
> 
> # Tiny Correction
> 
> I would **not** call Title 06 “Personal Systems” anymore.
> 
> Use:
> 
> ```text
> Title 06 — QiLife
> ```
> 
> Then the subtitle/description can say:
> 
> ```text
> Life Operations, Planner, Relationships, Projects, and Routines
> ```
> 
> Because `QiLife` is already the brand. Don’t over-explain in the title. Put the explanation under it.

### User
> question so rules and sections are part of charpters so in thory in the chapter pages we need a database biew that shows thats chapters sections and the seciont pages show that sections lines or do i just leave them nested they way the are.

### Assistant
> Yes, you’re thinking correctly — but **do not over-normalize this**.
> 
> The clean answer:
> 
> > **Use the database as the index. Keep the actual section text nested inside the chapter page.**
> 
> Do **not** make every section page open to another database of “lines.” That is bureaucratic goblin behavior. It will look powerful for 20 minutes and then become click-hell.
> 
> # Best Structure
> 
> ```text
> QiCode
> ├── Title pages
> │   └── show chapter list
> │
> ├── Chapter pages
> │   ├── show filtered database view of that chapter’s sections
> │   └── contain the actual written sections as headings
> │
> └── Section database
>     └── index / status / reference only
> ```
> 
> So yes, inside each chapter page you can have a database view like:
> 
> ```text
> Sections in this Chapter
> Filtered where Chapter Code = 04.01
> Sorted by Sort Key
> ```
> 
> Then underneath that, keep the actual content nested:
> 
> ```markdown
> # QiCode § 04.01 — Timeline, Journal & Chronicle
> 
> ## § 04.01.001 — Chronicle Purpose
> 
> ### Rule
> The Chronicle is the chronological memory spine of the Qi system.
> 
> ### Meaning
> ...
> 
> ## § 04.01.002 — Timeline Events
> 
> ### Rule
> ...
> ```
> 
> That gives you both:
> 
> ```text
> Database = map / index / status
> Chapter page = readable book
> ```
> 
> # Do Not Do This Yet
> 
> Avoid this structure:
> 
> ```text
> Chapter page
> └── Section database view
>     └── Section page
>         └── Lines database view
>             └── Line page
> ```
> 
> That is too many doors. You’ll spend more time navigating than writing.
> 
> # Better Rule
> 
> Use this hierarchy:
> 
> ```text
> Title = major division
> Chapter = page
> Section = heading inside chapter
> Rule / Meaning / Notes = content blocks inside section
> ```
> 
> The database should track the sections, but the chapter should **read like a book**.
> 
> # When Should a Section Become Its Own Page?
> 
> Only promote a section to its own page when it becomes one of these:
> 
> | Promote section to page when… | Example |
> |---|---|
> | It gets long | `§ 04.01.002 — Timeline Events` becomes a full spec |
> | It has templates | Timeline Event template, Incident Log template |
> | It has active implementation details | Supabase fields, Notion properties, UI behavior |
> | It has many related references | Legal timeline model, evidence model |
> | It is reused across many areas | Decision Notes, Evidence Links, Status Labels |
> 
> Otherwise, leave it nested.
> 
> # My Recommended Notion Setup
> 
> ## Database: `QiCode Index`
> 
> Rows include:
> 
> ```text
> Title
> Chapter
> Section
> QiCode
> Sort Key
> Status
> Type
> Owner
> Related Sections
> Content Location
> ```
> 
> Types:
> 
> ```text
> Title
> Chapter
> Section
> Template
> Standard
> Reference
> ```
> 
> ## Chapter Page Layout
> 
> Each chapter page should look like this:
> 
> ```markdown
> # QiCode § 04.01 — Timeline, Journal & Chronicle
> 
> ## Chapter Purpose
> 
> ## Plain-English Summary
> 
> ## Scope
> 
> ## Sections
> [linked database view filtered to Chapter Code = 04.01]
> 
> ---
> 
> ## § 04.01.001 — Chronicle Purpose
> 
> ### Rule
> 
> ### Meaning
> 
> ### Use When
> 
> ### Related Sections
> 
> ---
> 
> ## § 04.01.002 — Timeline Events
> 
> ### Rule
> 
> ### Meaning
> 
> ### Minimum Fields
> 
> ### Related Sections
> ```
> 
> That’s the sweet spot.
> 
> # The Spine Logic
> 
> Think of it like this:
> 
> ```text
> Database view = table of contents
> Nested headings = actual book
> Section pages = only for expanded doctrine/specs
> Line-level databases = no, unless you are building actual legislation/software parser later
> ```
> 
> # Final Call
> 
> For now:
> 
> ```text
> Leave sections nested inside chapter pages.
> Use the database view only as an index/status tracker.
> Promote sections to standalone pages only when they earn it.
> Do not create a “section lines” database.
> ```
> 
> That keeps QiCode readable, referenceable, and not annoying as hell.
