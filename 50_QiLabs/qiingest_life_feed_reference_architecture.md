---
layout: page
title: "QiIngest and Life Feed Reference Architecture"
slug: "qiingest-life-feed-reference-architecture"
summary: "Reference architecture for local-first AI file intake, activity event capture, review, routing, indexing, and daily synthesis across QiOS."
status: active
created_at: "2026-07-18"
updated_at: "2026-07-18"
author: "Cody J. Rice-Velasquez"
owner: "Cody J. Rice-Velasquez"
tags: []
keywords:
  - QiIngest
  - Life Feed
  - file automation
  - local AI
  - event ledger
  - knowledge capture
aliases:
  - "QiIngest Reference"
  - "Life Feed Automation Reference"
context: "Reference architecture for future local AI-assisted file organization and digital activity synthesis. This document does not replace the established QiLabs tree, naming rules, frontmatter standard, or Housekeeping Console."
sensitivity: internal
classification: business_internal
realm_label: "QiLabs"
uid: ""
canonical_ref: ""
source_type: manual
template_key: master-template
---

# QiIngest and Life Feed Reference Architecture

## Overview

This document preserves the useful architectural concepts from earlier file-automation and Life Feed proposals without introducing another naming system, folder hierarchy, or source of truth.

The future system should provide one controlled path for introducing new material into QiOS:

> **Capture first. Classify once. Preserve identity.**

The system observes approved intake sources, extracts useful information, detects duplicates, proposes actions, applies approved changes, records every operation, and produces a searchable event history.

It must operate within the existing QiLabs structure rather than creating a parallel organizational model.

---

## System Responsibilities

### Housekeeping Console

Housekeeping maintains material that is already inside the organized system.

Responsibilities include:

* Validate filenames
* Validate frontmatter and tags
* Detect structural drift
* Rebuild folder indexes
* Update inventories, manifests, and trees
* Preview planned changes
* Apply approved plans
* Restore files through undo manifests

Housekeeping does not decide what newly captured material means.

### QiIngest

QiIngest processes new files and imported material.

Responsibilities include:

* Monitor approved intake locations
* Wait until files are stable and fully written
* Extract text, metadata, dates, entities, and document type
* Generate cryptographic and perceptual hashes
* Detect exact and probable duplicates
* Propose a descriptive filename
* Propose a destination in the existing QiLabs tree
* Request review when confidence or policy requires it
* Apply approved moves and renames safely
* Register the canonical item
* Emit a Life Feed event

### Life Feed

The Life Feed is an operational event ledger showing what occurred across approved sources.

It is not another copy of every file, message, screenshot, or database record.

It stores:

* A concise description of the event
* When it occurred
* Where it came from
* The canonical item or source reference
* Related people, projects, and topics
* Processing results
* Review and action status

### QiMemory and Knowledge Promotion

Most Life Feed events remain operational history.

Selected events may be promoted into durable knowledge when they contain:

* A decision
* A reusable insight
* A meaningful personal record
* A project milestone
* An important relationship event
* A legal or financial fact
* A recurring pattern
* Material suitable for a timeline or journal

Promotion creates or updates a canonical knowledge document. It does not blindly convert every event into a note.

### QiVault

QiVault remains the canonical home for durable notes, records, references, timelines, and personal knowledge.

### Local Registry

A local SQLite registry should serve as the operational database for QiIngest and the Life Feed.

Notion, Google Sheets, Zoho, or other services may display or receive selected information, but they are not the canonical registry.

---

## Core Principles

### 1. Existing structure is authoritative

QiIngest must use the established QiLabs tree, filename rules, metadata model, and protected-path configuration.

It must not introduce:

* Drive-letter classification
* Decimal identifiers in filenames
* A second domain map
* Status suffixes in filenames
* Mandatory underscore-ending folders
* A competing folder hierarchy

### 2. Identity is separate from location

A file's permanent identity must not depend on its filename or folder.

Identity should be maintained through:

* `uid`
* `canonical_ref`
* SHA-256 content hash
* Registry record ID

A file may move or be renamed without becoming a different item.

### 3. Filenames describe; metadata identifies

Filenames should remain readable and consistent with the established convention:

```text
2026-07-18_descriptive-file-title.pdf
descriptive-file-title.md
```

Use:

* Lowercase words
* Hyphens between title words
* An optional ISO date prefix when the date materially helps
* The correct original extension

Preserve structural filenames such as:

* `README.md`
* `_index.md`
* `index.md`
* `CHANGELOG.md`
* `LICENSE.md`

Do not use:

* Drive letters
* Decimal serial numbers
* Colons
* Status codes such as `_PEN`, `_TMP`, or `_DUP`
* Automatic `(1)`, `(2)`, or `(3)` duplicate suffixes

### 4. AI proposes; policy decides

AI may analyze content and propose actions.

Deterministic policies decide whether those actions may be:

* Applied automatically
* Presented for review
* Rejected
* Escalated
* Ignored

The AI is never an unrestricted filesystem operator.

### 5. Every mutation must be reversible

Every rename, move, metadata update, or generated file must have:

* A previewed action
* The expected pre-change hash
* The expected post-change hash
* A timestamp
* A reason
* A backup or reversal instruction
* An apply result
* An audit record

### 6. Privacy is the default

Only approved sources may be monitored.

The system must not indiscriminately record:

* Every screen
* Every browser tab
* Password fields
* Private messages
* Medical portals
* Financial credentials
* Evidence directories
* Legal records
* Source-code repositories

Sensitive integrations require explicit allowlists and retention rules.

### 7. Capture is not permanent retention

The system may observe or temporarily stage information without storing the full raw content forever.

Where possible, retain:

* A summary
* A canonical source reference
* Extracted entities
* Relevant dates
* Action candidates
* Processing metadata

Do not create uncontrolled copies of source content.

### 8. One canonical destination per function

Each type of output must have one primary destination.

Examples:

* Durable knowledge → QiVault
* Operational registry → local SQLite
* Tasks → one selected task system
* Calendar events → primary calendar
* Financial transactions → QiFinance
* File audit history → QiIngest registry and manifests

Other platforms may receive synchronized views, but they must not independently become competing masters.

---

## Processing Pipeline

```text
Observe
  ↓
Stabilize
  ↓
Extract
  ↓
Hash and compare
  ↓
Classify and link
  ↓
Create action plan
  ↓
Policy and confidence check
  ↓
Review or approve
  ↓
Apply atomically
  ↓
Register canonical item
  ↓
Emit Life Feed event
  ↓
Verify result
```

### 1. Observe

Monitor only configured intake sources.

Examples:

* A dedicated local intake folder
* A synced Google Drive intake folder
* A screenshot import folder
* Approved email labels
* Approved calendar accounts
* Approved task lists

Filesystem monitoring should be supplemented by periodic reconciliation because operating-system events may be missed.

### 2. Stabilize

Before reading or moving a file, confirm that:

* Its size has stopped changing
* It is not locked by another program
* Its sync operation is complete
* It is not a temporary download
* Its extension is final

### 3. Extract

Depending on file type, extract:

* Embedded text
* OCR text
* Creation and modification dates
* Document dates
* Sender or creator
* People and organizations
* Titles and subjects
* File type
* Application metadata
* Links
* Language
* Relevant project or matter

Extraction should not change the original item.

### 4. Detect duplicates

Use SHA-256 for exact duplicate detection.

For images, optional perceptual hashing may identify likely visual duplicates.

Duplicate results should be classified as:

* Exact duplicate
* Probable duplicate
* Related version
* Independent item

Do not silently delete duplicates.

### 5. Classify and link

Determine:

* Content type
* Proposed destination
* Proposed filename
* Related project
* Related people
* Relevant dates
* Sensitivity
* Classification
* Whether the item belongs in an excluded or protected category

### 6. Create an action plan

The plan should state:

* Current path and filename
* Proposed path and filename
* Reason
* Confidence
* Detected metadata
* Duplicate findings
* Policy checks
* Required review level

### 7. Apply confidence and policy rules

#### High confidence

Automatic processing may occur only when:

* The source is approved
* The destination is unambiguous
* No protected-path rule applies
* No conflicting item exists
* The filename is valid
* The action is reversible

#### Medium confidence

Present the proposed action for review.

#### Low confidence

Leave the original item unchanged and place the decision in the review queue.

#### Protected or excluded

Do not move, rename, OCR, summarize, or index the item beyond what its specific policy allows.

### 8. Apply atomically

Actions should avoid partial completion.

When possible:

1. Create required directories
2. Confirm the source hash
3. Move or rename the item
4. Confirm the destination hash
5. Update metadata or registry
6. Emit the event
7. Mark the operation complete

A failed operation must either roll back or remain clearly marked as incomplete.

### 9. Register

A minimal canonical file record should include:

```text
uid
canonical_ref
title
current_path
original_path
content_hash
perceptual_hash
source_type
document_type
status
classification
sensitivity
duplicate_of
confidence
created_at
observed_at
updated_at
```

### 10. Emit an event

After processing, emit a Life Feed event describing what occurred.

---

## Life Feed Event Model

A practical event record should include:

```text
event_id
event_type
occurred_at
observed_at
source
source_ref
summary
canonical_ref
related_people
related_projects
related_topics
action_status
confidence
metadata
```

Useful event types include:

* `file_observed`
* `file_processed`
* `file_review_required`
* `file_duplicate_detected`
* `email_received`
* `calendar_event`
* `task_created`
* `task_completed`
* `decision_recorded`
* `knowledge_promoted`
* `digest_created`
* `processing_failed`

Events should reference source material rather than duplicating it.

---

## Daily Digest

The daily digest should convert the event stream into a useful operational summary.

It may include:

### What happened

A concise account of meaningful activity.

### What was completed

Files processed, tasks completed, decisions made, and milestones reached.

### Open loops

Unresolved tasks, unanswered messages, pending reviews, and incomplete processing.

### People and projects

Important activity grouped by relevant person or project.

### Decisions and facts

Items worth preserving in durable knowledge.

### Exceptions

Failures, unusual activity, duplicate conflicts, or protected items encountered.

### Next three actions

A deliberately limited list of the three highest-value next actions.

The digest may propose tasks, but it should not automatically create large numbers of tasks without review.

---

## Source Adapters

Each external source should use its own adapter.

Examples:

```text
adapters/
├── filesystem
├── google-drive
├── gmail
├── google-calendar
├── task-system
├── screenshot-import
└── manual-capture
```

Adapters should convert source-specific data into the common event and intake models.

This keeps Gmail logic, filesystem logic, calendar logic, and task logic out of the core pipeline.

---

## Safety Requirements

The system must support:

* Dry-run previews
* Content-hash verification
* Saved action plans
* Backups
* Apply manifests
* Undo manifests
* Idempotent processing
* Restart recovery
* Atomic operations where possible
* Duplicate protection
* Filename collision protection
* Source allowlists
* Protected-path exclusions
* Structured audit logging
* Human review queues

The same item processed twice should not create two independent canonical records or repeat the same action.

---

## Exclusions and Protected Areas

The default policy should exclude or require special handling for:

* Git repositories
* Application source code
* Build output
* Dependency directories
* Environment and secret files
* Evidence directories
* Records directories
* Legal matter directories
* Encrypted storage
* Password or credential files
* Database internals
* System-generated cache files

These areas should not be treated as ordinary documents.

---

## Minimal Implementation Structure

```text
qiingest/
├── config/
│   ├── settings.json
│   ├── source-policies.json
│   └── destination-rules.json
├── src/
│   ├── adapters/
│   ├── extractors/
│   ├── classifiers/
│   ├── policies/
│   ├── pipeline/
│   ├── registry/
│   ├── review/
│   ├── events/
│   └── digest/
├── data/
│   ├── qiingest.sqlite
│   ├── staging/
│   └── review/
├── logs/
├── plans/
├── manifests/
└── tests/
```

This is a conceptual structure, not a mandatory repository tree.

---

## MVP Scope

The first version should remain intentionally narrow.

### Inputs

* One local intake folder
* A limited set of document and image types

### Processing

* File stabilization
* SHA-256 hashing
* Exact duplicate detection
* Text extraction
* OCR where required
* Metadata extraction
* Filename proposal
* Destination proposal
* Review queue

### Application

* Approved rename or move
* Registry update
* Life Feed event creation
* Reversible operation manifest

### Output

* Local review screen or report
* Local event ledger
* Daily digest generated from processed events

Notion, email ingestion, calendar ingestion, task synchronization, graph relationships, and continuous screenshot monitoring are not required for the MVP.

---

## MVP Acceptance Criteria

The MVP is acceptable when:

* No file can be overwritten silently
* Every applied change is logged
* Every applied change has a defined reversal path
* Protected and excluded paths receive no unauthorized mutations
* Reprocessing the same item is idempotent
* Exact duplicates are consistently identified
* Failed actions remain recoverable
* Review-required items remain unchanged until approved
* The registry matches the actual filesystem after processing
* A daily digest can be generated from the event ledger

Classification accuracy should be measured, but accuracy alone must not authorize automatic actions.

---

## Future Capabilities

After the MVP is stable, optional additions may include:

* Gmail and Zoho email adapters
* Google and Zoho calendar adapters
* A selected task-system adapter
* Selective screenshot imports
* Audio transcription
* Semantic search
* Project and person linking
* Timeline generation
* Knowledge promotion suggestions
* Local model summarization
* Cloud-model escalation for approved material
* Optional Notion or dashboard synchronization
* QiFinance receipt and transaction routing

Each capability should be added as an isolated adapter or service rather than expanding one monolithic script.

---

## Explicit Non-Goals

QiIngest and the Life Feed will not:

* Replace Housekeeping
* Replace the established QiLabs tree
* Introduce another naming system
* Record every digital action indiscriminately
* Store permanent copies of every observed item
* Treat Notion as the central source of truth
* Push the same task into several task systems
* Allow AI to mutate files without policy checks
* Automatically restructure protected records
* Convert every event into a permanent note
* Archive all processed material into daily ZIP files
* Use filenames as permanent database identifiers

---

## Decision Summary

Retained concepts:

* Controlled intake
* Local file monitoring
* OCR and metadata extraction
* Hash-based duplicate detection
* Review queues
* Confidence-based routing
* Action manifests and rollback
* Unified event records
* Daily synthesis
* Modular source adapters
* Selective knowledge promotion
* Local-first processing

Rejected concepts:

* Drive-letter filenames
* Decimal identifiers embedded in filenames
* `::` filename separators
* Status flags embedded in filenames
* Notion as the central source of truth
* Unrestricted screenshot surveillance
* Duplicate task systems
* Automatic duplicate suffixes
* Mandatory daily ZIP archives
* Parallel folder taxonomies

---

## Operating Doctrine

> New material enters through controlled intake.
>
> The system observes without immediately mutating.
>
> Identity is established before location changes.
>
> AI proposes meaning; policy controls action.
>
> Uncertainty produces review, not guessing.
>
> Canonical files remain singular.
>
> Events provide history without creating duplicate content.
>
> Every automated operation is visible, verifiable, and reversible.
