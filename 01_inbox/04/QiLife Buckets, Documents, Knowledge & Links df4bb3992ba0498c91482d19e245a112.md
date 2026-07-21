# QiLife Buckets, Documents, Knowledge & Links

Notes: Merged bucket model, document metadata model, knowledge item model, and polymorphic links doctrine.
QiCode: § 04.02.006
Sort Key: 04.02.006
Status: active
Tags: Core, KB/SOPs, Registry/Archive
Type: Standard
Version: Reconciled V1

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

## Records, Metadata, and Links

QiLife records should clarify what something is, where it belongs, and what it relates to before creating new structures.

## Buckets

Buckets are the top-level operating domains aligned to QiDrive.

Use stable keys matching the folder names.

```
buckets
├── key
├── name
├── slug
├── folder_path
├── sort_order
├── description
├── is_system
├── created_at
└── updated_at
```

## Seed Buckets

```
00_inbox
01_workbench
02_timeline
03_life
04_people
05_business
06_finance
07_legal
08_tech
09_assets
10_data
11_reference
12_archive
13_system
```

## Bucket Meanings

| Bucket | Meaning |
| --- | --- |
| `00_inbox` | Temporary unprocessed capture |
| `01_workbench` | Active projects, drafts, builds, work |
| `02_timeline` | Daily logs, chronology, events, summaries |
| `03_life` | Household, wellness, routines, personal operations |
| `04_people` | People, vendors, agencies, relationships |
| `05_business` | Ventures, brand, client-adjacent material |
| `06_finance` | Finance references, exports, planning, bridge data |
| `07_legal` | Legal matters, evidence, research, filings |
| `08_tech` | Systems, servers, apps, config, code notes |
| `09_assets` | Media, templates, reusable visual/design assets |
| `10_data` | Datasets, CSVs, schemas, logs, exports |
| `11_reference` | Guides, examples, laws, research, outside references |
| `12_archive` | Inactive or completed material |
| `13_system` | Manifests, indexes, rules, automation records |

## Documents

Documents are metadata records for files stored in QiDrive.

QiLife does not store the file itself unless there is a specific technical reason.

```
documents
├── id
├── title
├── file_path
├── drive_url
├── source
├── document_type
├── bucket_key
├── thread_id
├── file_hash
├── mime_type
├── size_bytes
├── notes
├── extracted_text
├── summary
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

## Document Rule

QiDrive stores the file.

QiLife stores:

- what it is
- where it is
- what it relates to
- whether it matters
- how to retrieve it

## Knowledge Items

Durable reference material, templates, guides, and reusable notes.

```
knowledge_items
├── id
├── title
├── body_markdown
├── bucket_key
├── module_key
├── knowledge_type
├── source_type
├── source_path
├── confidence
├── visibility
├── tags_json
├── metadata_json
├── last_synced_at
├── sync_hash
├── created_at
├── updated_at
├── archived_at
└── deleted_at
```

## Knowledge Types

```
guide
template
checklist
reference
rule
note
summary
external_source
```

## Repo Docs Rule

Docs imported from QiSpark or app repos are read-only in QiLife unless edited at their source.

QiLife can index and reference docs, but it should not silently fork doctrine.

## Links

The polymorphic relationship table.

Links connect anything to anything.

```
links
├── id
├── source_type
├── source_id
├── target_type
├── target_id
├── relationship
├── created_at
└── updated_at
```

## Common Relationships

```
relates_to
belongs_to
caused_by
evidence_for
follow_up_to
blocks
blocked_by
mentions
supports
contradicts
duplicates
derived_from
stored_at
assigned_to
```

## Link Rule

Use links before duplicating data.