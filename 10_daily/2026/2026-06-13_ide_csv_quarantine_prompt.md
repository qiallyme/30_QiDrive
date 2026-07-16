---
layout: page
title: "IDE CSV Quarantine Prompt"
slug: "ide_csv_quarantine_prompt"
created_at: "2026-06-13 10:33:22"
updated_at: "2026-06-13 10:33:22"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-009.json"
template_key: master-template
date: 2026-06-13
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a2d783c-2f00-83ea-90e3-e79e342d8b15"
canonical_ref: ""
---

# IDE CSV Quarantine Prompt

## Overview
- **Date**: 2026-06-13 10:33:22
- **Conversation ID**: `6a2d783c-2f00-83ea-90e3-e79e342d8b15`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> i need to make a better promnpt for my ide. please read a little bit of C:\QiLabs\20_QiSystem, there are a ton of tempalte csv tables, those need to be quuarnteend. some need merged, other s need the file name updated and some need to be preserved forrectoed.

### Assistant
> Absolutely. Here’s a stronger IDE/Codex prompt you can paste in.
> 
> ---
> 
> ## IDE Prompt: Quarantine and Reconcile Template CSV Tables
> 
> We need to clean up the CSV/template-table situation inside:
> 
> `C:\QiLabs\20_QiSystem`
> 
> There are many temporary/template CSV files in this tree. Do **not** delete anything yet. First, quarantine and inventory them so we can decide what becomes canonical, what gets merged, what gets renamed, and what gets preserved as historical/reference material.
> 
> ### Goal
> 
> Create a safe reconciliation workflow for all CSV/template-table files under `C:\QiLabs\20_QiSystem`.
> 
> The priority is:
> 
> 1. **Preserve everything**
> 2. **Identify duplicate / overlapping template tables**
> 3. **Quarantine non-canonical or temporary CSVs**
> 4. **Merge tables where appropriate**
> 5. **Rename files where the filename does not match the table purpose**
> 6. **Keep corrected/preserved versions where needed**
> 7. **Produce a clear inventory and recommendation report before making destructive changes**
> 
> ---
> 
> ## Rules
> 
> ### Hard rule: no deletion
> 
> Do **not delete any CSV, template, or generated table file.**
> 
> Anything uncertain should be moved or copied into a quarantine area, not removed.
> 
> ### Create quarantine structure
> 
> Inside `C:\QiLabs\20_QiSystem`, create something like:
> 
> `_quarantine\csv_templates\`
> 
> With subfolders:
> 
> - `00_originals_snapshot`
> - `10_temp_or_generated`
> - `20_duplicates_or_superseded`
> - `30_needs_merge`
> - `40_needs_rename`
> - `50_preserve_reference`
> - `60_corrected_versions`
> - `99_review_notes`
> 
> If a better structure already exists in the repo, use the existing convention.
> 
> ---
> 
> ## What to scan
> 
> Scan recursively for:
> 
> - `.csv`
> - `.tsv`
> - `.xlsx` if present
> - files with names containing:
>   - `template`
>   - `temp`
>   - `sample`
>   - `draft`
>   - `copy`
>   - `backup`
>   - `old`
>   - `generated`
>   - `seed`
>   - `schema`
>   - `fields`
>   - `table`
> 
> Also inspect nearby README, markdown, JSON, YAML, or schema files that explain what these tables are supposed to represent.
> 
> ---
> 
> ## Inventory required
> 
> Create an inventory file:
> 
> `C:\QiLabs\20_QiSystem\_quarantine\csv_templates\99_review_notes\csv_template_inventory.md`
> 
> For every relevant file, include:
> 
> - Original path
> - Filename
> - File type
> - Row count
> - Column count
> - Column names
> - Apparent purpose
> - Whether it appears canonical, temporary, duplicate, generated, obsolete, or reference-only
> - Similar/overlapping files
> - Recommended action:
>   - preserve
>   - quarantine
>   - merge
>   - rename
>   - correct
>   - promote to canonical
>   - needs human review
> 
> Also create a machine-readable version:
> 
> `csv_template_inventory.json`
> 
> ---
> 
> ## Classification logic
> 
> Classify files into these categories:
> 
> ### 1. Canonical candidates
> 
> Files that appear intentionally designed, complete, and aligned with QiSystem/QiOS/QiLife naming.
> 
> These should not be moved yet unless there is a clear canonical destination.
> 
> ### 2. Temporary/generated files
> 
> Files that look like intermediate exports, test data, generated drafts, mock data, or one-off staging files.
> 
> Move or copy these to:
> 
> `10_temp_or_generated`
> 
> ### 3. Duplicate or superseded files
> 
> Files with overlapping columns/purpose where one appears newer, cleaner, or more complete.
> 
> Move or copy weaker versions to:
> 
> `20_duplicates_or_superseded`
> 
> ### 4. Needs merge
> 
> Files that represent the same conceptual table but contain different useful fields or records.
> 
> Place copies in:
> 
> `30_needs_merge`
> 
> Then propose a merged schema, but do not overwrite the originals.
> 
> ### 5. Needs rename
> 
> Files whose names are vague, misleading, outdated, or inconsistent.
> 
> Place notes in:
> 
> `40_needs_rename`
> 
> Recommend new names using consistent QiSystem naming.
> 
> ### 6. Preserve reference
> 
> Files that should not become active tables but may contain useful historical structure, old assumptions, or source material.
> 
> Place copies in:
> 
> `50_preserve_reference`
> 
> ### 7. Corrected versions
> 
> If a file has obvious structural issues, create a corrected copy in:
> 
> `60_corrected_versions`
> 
> Do not overwrite the original.
> 
> ---
> 
> ## Naming standards
> 
> Use clear canonical names.
> 
> Prefer names like:
> 
> - `qisystem_entity_catalog.csv`
> - `qisystem_field_registry.csv`
> - `qisystem_table_registry.csv`
> - `qisystem_relationship_registry.csv`
> - `qisystem_status_registry.csv`
> - `qisystem_route_registry.csv`
> - `qisystem_view_registry.csv`
> - `qisystem_source_registry.csv`
> - `qisystem_data_ownership_matrix.csv`
> 
> Avoid vague names like:
> 
> - `template.csv`
> - `fields.csv`
> - `data.csv`
> - `table1.csv`
> - `master.csv`
> - `copy.csv`
> - `new.csv`
> - `test.csv`
> 
> If a file is QiLife-specific, name it accordingly:
> 
> - `qilife_entity_catalog.csv`
> - `qilife_screen_registry.csv`
> - `qilife_capture_field_registry.csv`
> 
> If it is global/canonical, use:
> 
> - `qios_...`
> - `qisystem_...`
> 
> ---
> 
> ## Merge requirements
> 
> Where files need to be merged:
> 
> 1. Compare columns.
> 2. Detect duplicate rows.
> 3. Preserve unique fields from each source.
> 4. Keep source provenance columns:
>    - `source_file`
>    - `source_path`
>    - `source_row_number`
>    - `merge_notes`
> 5. Do not silently discard data.
> 6. Produce proposed merged files in a separate output folder.
> 
> Suggested folder:
> 
> `_quarantine\csv_templates\60_corrected_versions\merged_proposals\`
> 
> ---
> 
> ## Output report
> 
> Create a final report:
> 
> `C:\QiLabs\20_QiSystem\_quarantine\csv_templates\99_review_notes\csv_template_reconciliation_report.md`
> 
> The report should include:
> 
> ### Executive summary
> 
> - Total CSV/template files found
> - How many appear canonical
> - How many quarantined
> - How many duplicates
> - How many need merge
> - How many need rename
> - How many should be preserved only as reference
> 
> ### Recommended canonical table set
> 
> List the final recommended active tables.
> 
> ### Merge recommendations
> 
> For each merge group:
> 
> - Files involved
> - Why they overlap
> - Proposed canonical output name
> - Proposed schema
> - Risks / uncertainties
> 
> ### Rename recommendations
> 
> For each rename:
> 
> - Current filename
> - Proposed filename
> - Reason
> 
> ### Human review needed
> 
> List anything ambiguous.
> 
> ---
> 
> ## Important behavior
> 
> Work carefully.
> 
> Before moving files, create a snapshot copy of all discovered CSV/template files in:
> 
> `00_originals_snapshot`
> 
> Use relative paths inside the snapshot so original locations can be reconstructed.
> 
> After snapshotting, quarantine copies or move only files that are clearly temporary/generated/superseded. If there is any uncertainty, copy instead of move and mark as `needs_human_review`.
> 
> Do not change application code yet unless there are imports or references that obviously need a path update. If path references are found, list them in the report instead of editing them immediately.
> 
> ---
> 
> ## Final deliverables
> 
> Produce:
> 
> 1. `csv_template_inventory.md`
> 2. `csv_template_inventory.json`
> 3. `csv_template_reconciliation_report.md`
> 4. Any proposed corrected or merged CSVs in `60_corrected_versions`
> 5. A list of exact recommended next actions
> 
> ---
> 
> ## Core instruction
> 
> Treat this as a **governance cleanup**, not a quick file shuffle.
> 
> The purpose is to separate:
> 
> - active canonical schema material
> - temporary generated junk
> - duplicate drafts
> - useful historical reference
> - merge candidates
> - rename candidates
> 
> Preserve first. Classify second. Modify third. Delete never.

### User
> also i feel like this file tree needs to be flattened and merged, can you help me do that. {
>   "name": "_QiOS_DNA",
>   "path": "c:\\QiLabs\\_QiOS_DNA",
>   "type": "directory",
>   "children": [
>     {
>       "name": "00_QiEOS",
>       "type": "folder",
>       "children": [
>         {
>           "name": "10_governance",
>           "type": "folder",
>           "children": [
>             {
>               "name": "10_principles",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "20_rules",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "30_standards",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "content_metadata_profile.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "metadata_rules.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "naming_rules.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "pdf_standards.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "repo_rules.yaml",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "40_policies",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "agents",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "agent_governance_policy.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "architecture",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "active_runtime_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "placement_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "registry_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "root_navigation_policy.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "development",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "bootstrap_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "contribution_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "merge_policy.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "operations",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "legacy_quarantine_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "lifecycle_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "qinexus_freeze_policy.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "security",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "security_data_access_policy.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "50_decisions",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ADR-0000_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0001_QiOS_DNA_As_Master_Doctrine_Repo.mdx",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0001_blueprint_scope.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0002_single_domain_rule.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0003_band_model.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0004_single_account_modular_mode.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0005_fleet_orchestration.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0006_narrative_and_knowledge_consolidation.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0007_unified_front_matter_and_progressive_doc_topology.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0008_qilabs_root.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0009_backup_server_control_plane_and_public_edge_pattern.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0010_qios_namespace_as_routing_metadata_layer.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "60_registry",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "namespace_registry",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "2026-05-18_qios_namespace_registry_merged_v2.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "schemas",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "band_registry.schema.json",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "100_metadata.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "10_infrastructure_layout.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "110_front_matter.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "120_storage.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "130_placement_rules.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "140_exports.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "150_qievidence.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "160_vectorization_pipeline.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "20_bands.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "30_domains.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "40_subdomains.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "60_directory_tree.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "70_object_model.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "80_objects.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "90_schema.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "band_registry.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "band_registry_v2.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "deprecation_registry.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "domain_registry.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "folder_registry.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "infrastructure_registry.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "realms_registry.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "sensitivity_classification.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "subdomain_registry.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "workspace_realms.yaml",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "_index.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "20_structure",
>           "type": "folder",
>           "children": [
>             {
>               "name": "10_identity.md",
>               "type": "file"
>             },
>             {
>               "name": "20_system_model.md",
>               "type": "file"
>             },
>             {
>               "name": "30_component_map.md",
>               "type": "file"
>             },
>             {
>               "name": "40_service_boundaries.md",
>               "type": "file"
>             },
>             {
>               "name": "50_data_flow.md",
>               "type": "file"
>             },
>             {
>               "name": "60_device_model.md",
>               "type": "file"
>             },
>             {
>               "name": "70_runtime_zones.md",
>               "type": "file"
>             },
>             {
>               "name": "_index.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "30_service_map",
>           "type": "folder",
>           "children": [
>             {
>               "name": "100_integrations",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "external_integrations.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "10_infrastructure",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "cockpit",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "cockpit_command_menu.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "cloudflare.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "docker_compose.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "gethomepage.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "portainer.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "tailscale.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "uptime_kuma.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "110_qiserver",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "Service_Map.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "runtime.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "runtime_profile.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "120_applications",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "CareLite",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "qinote",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "qinote_salvage_extract.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "admin.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "carelite.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "firefly.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "portal.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "roadmap.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "130_GINA",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "20_ai_compute",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "aider.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "neo4j.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ollama.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "open_webui.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qdrant.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "30_capture",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "paperless",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "nocodb.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "obsidian_qidocs.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "wikijs.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "40_productivity",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "activitywatch.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "n8n.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qiledger.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "solidtime.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "50_apis",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "portal_api.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "60_workers",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "system_workers.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "70_pipelines",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_pipelines.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "80_tools",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "operator_tools.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "90_interfaces",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "public_interfaces.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "_index.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "40_operations",
>           "type": "folder",
>           "children": [
>             {
>               "name": "10_cases",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "20_qiserver",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "QiAccess_Server_Runbook.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "30_dev_history",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "2026-05-16_dev_session_directory_markmind_mapper.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "2026-05-17_open_loop_reset_paperless_ingestion_runbook.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "40_dev_testing",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "momscare",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "2026-05-17_momcare_app_qa_checklist.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "qiaccessstart",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "2026-05-17_qiaccess_start_qa_checklist.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "Access_And_Exposure_Rules.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "_index.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "50_knowledge",
>           "type": "folder",
>           "children": [
>             {
>               "name": "90_superseded_sources",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "2025-11-18_qicodex_protocol_batch_overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "QiAccess_Start_Blueprint.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "README.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qi_os_home_blueprint.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "tech_stack_markmind.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "20_glossary.md",
>               "type": "file"
>             },
>             {
>               "name": "30_migration_notes.md",
>               "type": "file"
>             },
>             {
>               "name": "40_legacy_csv_migration_plan.md",
>               "type": "file"
>             },
>             {
>               "name": "50_legacy_salvage.md",
>               "type": "file"
>             },
>             {
>               "name": "60_qiaccess_start_legacy_quarantine.md",
>               "type": "file"
>             },
>             {
>               "name": "70_repo_sync_status_20260516.md",
>               "type": "file"
>             },
>             {
>               "name": "_index.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "60_assets",
>           "type": "folder",
>           "children": [
>             {
>               "name": "diagrams",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "2026-05-17_supabase_markmind.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "blueprint_map.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "diagrams.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "markmind-data.json",
>                   "type": "file"
>                 },
>                 {
>                   "name": "markmind.html",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "images",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_QiOS_Master_Document.jpg",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "templates",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "2026-05-16_dev_session_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "README.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "adr_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "appendix_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "artifact_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "note_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "operational_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "page_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "registry_reference_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "section_index_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "standard_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "templates.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "assets.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "90_receipts",
>           "type": "folder",
>           "children": [
>             {
>               "name": "10_logs",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "20_audits",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "30_backups",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "40_health_checks",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "50_generated_reports",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "current_project_state.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qilabs_structure_check.csv",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qilabs_structure_check.json",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qilabs_structure_check.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "60_generated_indexes",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "70_maintenance",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "_audit",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "2026-05-24_qiaccess_homepage_conversion_report.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "2026-05-24_qiaccess_homepage_local_validation_report.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "2026-05-24_qilinks_admin_and_visual_map_plan.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qiaccess_map.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qiaccess_map.mmd",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "10_changelog.md",
>               "type": "file"
>             },
>             {
>               "name": "Current_Project_State.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "doctrine",
>           "type": "folder",
>           "children": [
>             {
>               "name": "QiOS_Core_Doctrine.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "exports",
>           "type": "folder",
>           "children": [
>             {
>               "name": "QiOS_DNA_Chronicle.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "reconciliation",
>           "type": "folder",
>           "children": [
>             {
>               "name": "2026-06-09_codex_reconciliation_brief.md",
>               "type": "file"
>             },
>             {
>               "name": "2026-06-09_initial_reconciliation.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "system_map",
>           "type": "folder",
>           "children": [
>             {
>               "name": "QiOS_Master_Map.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "QiAccess_Start_Blueprint.md",
>           "type": "file"
>         },
>         {
>           "name": "README.md",
>           "type": "file"
>         },
>         {
>           "name": "_QiEOS.md",
>           "type": "file"
>         },
>         {
>           "name": "_index.md",
>           "type": "file"
>         },
>         {
>           "name": "file-index.json",
>           "type": "file"
>         },
>         {
>           "name": "rebuild.bat",
>           "type": "file"
>         },
>         {
>           "name": "vizvibe.mmd",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "10_QiAccess",
>       "type": "folder",
>       "children": [
>         {
>           "name": "_10_QiAccess.md",
>           "type": "file"
>         },
>         {
>           "name": "index.mdx",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "20_QiSystem",
>       "type": "folder",
>       "children": [
>         {
>           "name": "50_Generated_Reports",
>           "type": "folder",
>           "children": [
>             {
>               "name": "2026-06-08_qilife_governance_audit.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "50_modules",
>           "type": "folder",
>           "children": [
>             {
>               "name": "calendar",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "capture",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "documents",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ai_behaviors.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "context_dock.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_dependencies.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "inbox",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ai_behaviors.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "context_dock.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_dependencies.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "ingestion",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "knowledge",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ai_behaviors.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "context_dock.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_dependencies.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "money",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ai_behaviors.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "context_dock.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_dependencies.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "people",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ai_behaviors.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "context_dock.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_dependencies.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "qibits",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ai_behaviors.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "context_dock.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_dependencies.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "review",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "spaces",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "storage",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "threads",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ai_behaviors.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "context_dock.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_dependencies.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "timeline",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ai_behaviors.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "context_dock.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_dependencies.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             }
>           ]
>         },
>         {
>           "name": "60_ai_layer",
>           "type": "folder",
>           "children": [
>             {
>               "name": "00_ai_layer_blueprint.md",
>               "type": "file"
>             },
>             {
>               "name": "01_ai_service_contracts.md",
>               "type": "file"
>             },
>             {
>               "name": "02_ai_review_workflow.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "70_deployment",
>           "type": "folder",
>           "children": [
>             {
>               "name": "00_local_dev.md",
>               "type": "file"
>             },
>             {
>               "name": "01_future_docker.md",
>               "type": "file"
>             },
>             {
>               "name": "02_future_qiserver.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "80_prompts",
>           "type": "folder",
>           "children": [
>             {
>               "name": "00_codex_build_prompt_v1.md",
>               "type": "file"
>             },
>             {
>               "name": "01_codex_review_prompt.md",
>               "type": "file"
>             },
>             {
>               "name": "02_will_be_done_research_prompt.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "manifests",
>           "type": "folder",
>           "children": [
>             {
>               "name": "QiOS_DNA_File_Manifest.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "rules",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Source_of_Truth_Rules.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "schemas",
>           "type": "folder",
>           "children": [
>             {
>               "name": "QiLife_Data_Spine.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "_20_QiSystem.md",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "30_QiServer",
>       "type": "folder",
>       "children": [
>         {
>           "name": "_30_QiServer.md",
>           "type": "file"
>         },
>         {
>           "name": "index.mdx",
>           "type": "file"
>         },
>         {
>           "name": "qiserver_runbook.md",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "40_QiCapture",
>       "type": "folder",
>       "children": [
>         {
>           "name": "_40_QiCapture.md",
>           "type": "file"
>         },
>         {
>           "name": "index.mdx",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "50_QiNexus",
>       "type": "folder",
>       "children": [
>         {
>           "name": "My_Drive_Model",
>           "type": "folder",
>           "children": [
>             {
>               "name": "index.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "_50_QiNexus.md",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "60_QiApp_QiLife",
>       "type": "folder",
>       "children": [
>         {
>           "name": "_60_QiApp_QiLife.md",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "60_QiApps",
>       "type": "folder",
>       "children": [
>         {
>           "name": "QiJourney",
>           "type": "folder",
>           "children": [
>             {
>               "name": "index.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "QiLife",
>           "type": "folder",
>           "children": [
>             {
>               "name": "index.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "qiaccess_start",
>           "type": "folder",
>           "children": [
>             {
>               "name": "overview.md",
>               "type": "file"
>             },
>             {
>               "name": "wiki_publish_plan.md",
>               "type": "file"
>             }
>           ]
>         }
>       ]
>     },
>     {
>       "name": "70_QiConnect",
>       "type": "folder",
>       "children": [
>         {
>           "name": "06_workflows",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Automation_Backlog.md",
>               "type": "file"
>             },
>             {
>               "name": "Core_Workflows.md",
>               "type": "file"
>             },
>             {
>               "name": "QiIngest_Pipeline.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "_70_QiConnect.md",
>           "type": "file"
>         },
>         {
>           "name": "index.mdx",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "PART XI - Manual to Me",
>       "type": "folder",
>       "children": [
>         {
>           "name": "00 CLIFF NOTES Manual to Me - Cody's Guide 203f84a04402802cbf08d7edabcd80c1",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "01 Who I Am Core Identity & Values 203f84a0440280649bd1d30bffb5edfc",
>           "type": "folder",
>           "children": [
>             {
>               "name": "94d60b86-a732-4d2c-b2dc-1ddd74c96dce.jfif",
>               "type": "file"
>             },
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_-_01_Who_I_Am_Core_Identity__Values.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "02 How I Work Focus, Flow, Boundaries 203f84a04402806fb95fc0862c0556e8",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_-_02__How_I_Work_Focus_Flow_Boundaries.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "03 How I Relate Communication & Boundaries 203f84a044028063a81ae8e5867e8618",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "04 How I Feel Emotional Landscape 203f84a0440280e6927af392a916c6bf",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_04__How_I_Feel_Emotional_Landscape.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "05 How I Grow Learning & Creativity 203f84a044028098a2dbec92694a4358",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_05__How_I_Grow_Learning__Creativity.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "06 How I Operate Routines & Energy Management 203f84a04402803fa35cffab28a6ee91",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_-_06__How_I_Operate_Routines__Energy_Management.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "07 How to Support Me Needs & Triggers 203f84a0440280cc8f5ece450f21978f",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_-_07__How_to_Support_Me_Needs__Triggers.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "08 When I Struggle Overwhelm, Shutdown, Recovery 203f84a0440280e2bd8bdb18da258847",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_-_08__When_I_Struggle_Overwhelm_Shutdown_Recovery.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "09 Building Bridges Mutual Understanding 203f84a0440280dfb159f34e6b6c7ecb",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_-_09__Building_Bridges_Mutual_Understanding.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "10 Learn More About… 203f84a044028017ab5bfc6269a4b4ac",
>           "type": "folder",
>           "children": [
>             {
>               "name": "10 9 ADHD 203f84a0440280a7abc8dafbd78ac3e1",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "10 9a Time Management Challenges in Neurodivergent 203f84a04402800bb533fa5e22a971c0.pdf",
>                   "type": "file"
>                 },
>                 {
>                   "name": "10 9b Focus Irregularities and How They Impact Dai 203f84a0440280a79100d36b85f803f8.pdf",
>                   "type": "file"
>                 },
>                 {
>                   "name": "10 9c The Invisible Weight of Executive Function C 203f84a04402806b8c40f3e83a2a9b5d.pdf",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "10 1 Transgender 203f84a044028084bdbfec332d881b7c.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 10 Correspondence Anxiety 203f84a044028022ae12cfc1e77fa7c3.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 2 Sleep inertia 203f84a0440280efbebce629dd529f36.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 3 Delayed sleep phase 203f84a04402807ba39ccbec0500a164.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 4 Person of Color 203f84a0440280218544fb4d96808b5b.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 5 Phonophobia 203f84a0440280a49d46ea1d2121a02d.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 6 Depression 203f84a044028046a765cb0568eac83a.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 7 PTSD 203f84a0440280628a38e26e5e7cb1bc.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 8 Anxiety 203f84a0440280fa9a97cd796ee8fe0c.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 9 ADHD 203f84a0440280a7abc8dafbd78ac3e1.pdf",
>               "type": "file"
>             },
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_-_10__Learn_More_About.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "00 CLIFF NOTES Manual to Me - Cody's Guide 203f84a04402802cbf08d7edabcd80c1.pdf",
>           "type": "file"
>         },
>         {
>           "name": "01 Who I Am Core Identity & Values 203f84a0440280649bd1d30bffb5edfc.pdf",
>           "type": "file"
>         },
>         {
>           "name": "02 How I Work Focus, Flow, Boundaries 203f84a04402806fb95fc0862c0556e8.pdf",
>           "type": "file"
>         },
>         {
>           "name": "03 How I Relate Communication & Boundaries 203f84a044028063a81ae8e5867e8618.pdf",
>           "type": "file"
>         },
>         {
>           "name": "04 How I Feel Emotional Landscape 203f84a0440280e6927af392a916c6bf.pdf",
>           "type": "file"
>         },
>         {
>           "name": "05 How I Grow Learning & Creativity 203f84a044028098a2dbec92694a4358.pdf",
>           "type": "file"
>         },
>         {
>           "name": "06 How I Operate Routines & Energy Management 203f84a04402803fa35cffab28a6ee91.pdf",
>           "type": "file"
>         },
>         {
>           "name": "07 How to Support Me Needs & Triggers 203f84a0440280cc8f5ece450f21978f.pdf",
>           "type": "file"
>         },
>         {
>           "name": "08 When I Struggle Overwhelm, Shutdown, Recovery 203f84a0440280e2bd8bdb18da258847.pdf",
>           "type": "file"
>         },
>         {
>           "name": "09 Building Bridges Mutual Understanding 203f84a0440280dfb159f34e6b6c7ecb.pdf",
>           "type": "file"
>         },
>         {
>           "name": "1 5 Personality NTFJ 295f84a0440280f396e7cddbaf3c905b.pdf",
>           "type": "file"
>         },
>         {
>           "name": "10 Learn More About… 203f84a044028017ab5bfc6269a4b4ac.pdf",
>           "type": "file"
>         },
>         {
>           "name": "Codys_Guide_to_Understanding_and_Connection_(1).wav",
>           "type": "file"
>         },
>         {
>           "name": "Codys_Guide_to_Understanding_and_Connection_-_An_Overview.wav",
>           "type": "file"
>         },
>         {
>           "name": "Compass-Icon.png",
>           "type": "file"
>         },
>         {
>           "name": "Thank You for Taking This Journey 203f84a0440280efbc16d8451dc9cda1.pdf",
>           "type": "file"
>         },
>         {
>           "name": "ZwC7IC_S4_GX9Z6--2mx7.png",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "Reconciliation",
>       "type": "folder",
>       "children": [
>         {
>           "name": "2026-06-10_blueprint_readiness_and_decision_gate.md",
>           "type": "file"
>         },
>         {
>           "name": "2026-06-10_database_blueprint_gap_report.md",
>           "type": "file"
>         },
>         {
>           "name": "2026-06-10_documentation_status_map.md",
>           "type": "file"
>         },
>         {
>           "name": "2026-06-10_non_destructive_reconciliation_plan.md",
>           "type": "file"
>         },
>         {
>           "name": "2026-06-10_qidna_implementation_reconciliation.md",
>           "type": "file"
>         },
>         {
>           "name": "2026-06-10_qilife_schema_source_report.md",
>           "type": "file"
>         },
>         {
>           "name": "2026-06-10_site_coverage_report.md",
>           "type": "file"
>         },
>         {
>           "name": "2026-06-10_ui_blueprint_gap_report.md",
>           "type": "file"
>         },
>         {
>           "name": "_Reconciliation.md",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "Schema",
>       "type": "folder",
>       "children": [
>         {
>           "name": "_Schema.md",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "decisions",
>       "type": "folder",
>       "children": [
>         {
>           "name": "0001_personal_lifedesk_model.md",
>           "type": "file"
>         },
>         {
>           "name": "0002_qibit_as_atomic_unit.md",
>           "type": "file"
>         },
>         {
>           "name": "0003_timeline_as_spine.md",
>           "type": "file"
>         },
>         {
>           "name": "0004_context_dock_over_wiki.md",
>           "type": "file"
>         },
>         {
>           "name": "0005_repo_docs_indexed_in_app.md",
>           "type": "file"
>         },
>         {
>           "name": "0006_clean_core_with_legacy_bridge.md",
>           "type": "file"
>         },
>         {
>           "name": "0007_app_managed_storage_and_sync.md",
>           "type": "file"
>         },
>         {
>           "name": "0008_managed_document_vault_dup_allergic.md",
>           "type": "file"
>         },
>         {
>           "name": "0009_agent_first_copilot_cockpit.md",
>           "type": "file"
>         },
>         {
>           "name": "0010_spaces_for_scoped_shared_access.md",
>           "type": "file"
>         },
>         {
>           "name": "ADR-0011_homepage_powered_qiaccess.md",
>           "type": "file"
>         },
>         {
>           "name": "ADR-0012_data_strategy.md",
>           "type": "file"
>         },
>         {
>           "name": "ADR-0013_folder_documentation_model.md",
>           "type": "file"
>         },
>         {
>           "name": "ADR-0014_topology_constraints.md",
>           "type": "file"
>         },
>         {
>           "name": "ADR-0015_build_strategy.md",
>           "type": "file"
>         },
>         {
>           "name": "ADR-0016_ai_auditor_role.md",
>           "type": "file"
>         },
>         {
>           "name": "ADR-0017_canonical_vocabulary_and_v1_direction.md",
>           "type": "file"
>         },
>         {
>           "name": "_Decisions.md",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "site",
>       "type": "folder",
>       "children": [
>         {
>           "name": "_site.md",
>           "type": "file"
>         },
>         {
>           "name": "index.html",
>           "type": "file"
>         },
>         {
>           "name": "script.js",
>           "type": "file"
>         },
>         {
>           "name": "style.css",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": ".gitignore",
>       "type": "file"
>     },
>     {
>       "name": "CNAME",
>       "type": "file"
>     },
>     {
>       "name": "Current_Project_State.md",
>       "type": "file"
>     },
>     {
>       "name": "Folder_Canvas.canvas",
>       "type": "file"
>     },
>     {
>       "name": "README.md",
>       "type": "file"
>     },
>     {
>       "name": "_01_QiDNA.md",
>       "type": "file"
>     },
>     {
>       "name": "_Architecture.md",
>       "type": "file"
>     },
>     {
>       "name": "build.js",
>       "type": "file"
>     },
>     {
>       "name": "code_extractor.py",
>       "type": "file"
>     },
>     {
>       "name": "codex.md",
>       "type": "file"
>     },
>     {
>       "name": "docs.json",
>       "type": "file"
>     },
>     {
>       "name": "fix_folder_names.sh",
>       "type": "file"
>     },
>     {
>       "name": "index.md",
>       "type": "file"
>     },
>     {
>       "name": "package-lock.json",
>       "type": "file"
>     },
>     {
>       "name": "package.json",
>       "type": "file"
>     },
>     {
>       "name": "qilinks_bookmark_admin_plan.md",
>       "type": "file"
>     }
>   ],
>   "metadata": {
>     "generated": "2026-06-13T15:43:35.846Z",
>     "generator": "FileTree Pro Extension",
>     "version": "0.2.0",
>     "showIcons": false,
>     "maxDepth": 10
>   }
> }

### Assistant
> You’re right: this tree is doing too much nesting, and some folders are conceptually duplicated. The move is **not “flatten everything”**; it’s **flatten by function while preserving doctrine/history/assets separately**.

### Assistant
> Yes. The problem is real:
> 
> - `00_QiEOS` is acting like **doctrine + architecture + service map + operations + receipts + assets**
> - Root `_QiOS_DNA` also has **decisions, reconciliation, schema, site, current state**
> - `20_QiSystem` has newer app/schema/prompts/module docs
> - `60_QiApp_QiLife` and `60_QiApps/QiLife` are duplicated conceptually
> - `Reconciliation` exists both at root and inside `00_QiEOS`
> - `Current_Project_State.md` exists in multiple places
> - `QiAccess_Start_Blueprint.md` exists in canonical-ish and superseded-ish locations
> 
> So yes: **flatten and merge**, but with a governance-safe process.
> 
> Here’s the stronger IDE prompt.
> 
> :::writing{variant="standard" id="48291"}
> You are working in the repository:
> 
> `C:\QiLabs\_QiOS_DNA`
> 
> The current file tree is too deep, partially duplicated, and contains overlapping doctrine, decisions, reconciliation notes, schema files, generated reports, legacy sources, app documentation, and system documentation.
> 
> We need a **non-destructive file-tree flattening and reconciliation pass**.
> 
> Do not delete anything. Do not overwrite anything. Do not make destructive changes without first creating an inventory, migration map, and rollback plan.
> 
> ## Primary Goal
> 
> Flatten and merge the QiOS DNA documentation tree into a cleaner canonical structure while preserving all historical, legacy, generated, and reference material.
> 
> This is not a cosmetic rename pass. This is a governance cleanup.
> 
> The new tree should make it obvious where each document belongs:
> 
> - doctrine
> - decisions / ADRs
> - architecture
> - registry / schema
> - system modules
> - applications
> - services / infrastructure
> - operations / runbooks
> - reconciliation / audits
> - generated reports
> - assets
> - templates
> - legacy / superseded material
> - personal/manual-to-me material
> - site build files
> 
> ## Hard Rules
> 
> 1. Do not delete anything.
> 2. Do not overwrite any file.
> 3. Create a full migration plan before moving files.
> 4. Preserve provenance for every moved or copied file.
> 5. If two files appear duplicated, compare content before deciding.
> 6. If unsure, classify as `needs_human_review`.
> 7. Keep legacy/superseded files available but clearly separated from canonical docs.
> 8. Do not flatten assets, audio, PDFs, images, or generated site files into doctrine folders.
> 9. Do not mix active canonical source docs with generated output.
> 10. Prefer fewer top-level folders with clear purpose.
> 
> ## Current Problem Areas to Reconcile
> 
> Pay special attention to these overlaps:
> 
> ### 1. Duplicate decision locations
> 
> There are decisions/ADRs in:
> 
> - `00_QiEOS/10_governance/50_decisions`
> - `decisions`
> 
> These need to be compared and reconciled into one canonical decision/ADR location.
> 
> Recommended canonical destination:
> 
> `00_governance/decisions`
> 
> Legacy or duplicate versions should go to:
> 
> `90_archive/decisions_superseded`
> 
> ### 2. Duplicate reconciliation locations
> 
> There are reconciliation documents in:
> 
> - `00_QiEOS/reconciliation`
> - `Reconciliation`
> 
> These should be merged into one canonical location.
> 
> Recommended destination:
> 
> `80_reconciliation`
> 
> ### 3. Duplicate generated/current-state reports
> 
> There are generated/current state docs in:
> 
> - root `Current_Project_State.md`
> - `00_QiEOS/90_receipts/Current_Project_State.md`
> - `00_QiEOS/90_receipts/50_generated_reports/current_project_state.md`
> - `20_QiSystem/50_Generated_Reports`
> 
> These need to be compared, classified, and routed.
> 
> Recommended destinations:
> 
> - Active manually maintained status: `80_reconciliation/current_state`
> - Generated reports: `90_receipts/generated_reports`
> - Superseded reports: `90_archive/generated_reports_superseded`
> 
> ### 4. QiLife / QiApps duplication
> 
> There are overlapping folders:
> 
> - `60_QiApp_QiLife`
> - `60_QiApps/QiLife`
> - `20_QiSystem/50_modules`
> - `20_QiSystem/schemas/QiLife_Data_Spine.mdx`
> 
> These need to be reconciled.
> 
> Recommended canonical model:
> 
> - System-level module docs stay under `30_system/modules`
> - Application-level QiLife docs go under `40_applications/QiLife`
> - Data spine/schema docs go under `20_architecture/schema`
> 
> ### 5. QiAccess duplication
> 
> QiAccess appears in:
> 
> - `10_QiAccess`
> - `60_QiApps/qiaccess_start`
> - `00_QiEOS/QiAccess_Start_Blueprint.md`
> - `00_QiEOS/50_knowledge/90_superseded_sources/QiAccess_Start_Blueprint.md`
> 
> Determine which file is canonical, which is legacy, and which belongs as app documentation.
> 
> Recommended destinations:
> 
> - Active QiAccess docs: `40_applications/QiAccess`
> - Legacy QiAccess docs: `90_archive/legacy_qiaccess`
> - Historical blueprint if still useful: `80_reconciliation/legacy_bridge`
> 
> ### 6. Schema / registry split
> 
> Schema and registry material appears in:
> 
> - `00_QiEOS/10_governance/60_registry`
> - `20_QiSystem/schemas`
> - root `Schema`
> 
> These need to be merged conceptually.
> 
> Recommended destinations:
> 
> - `20_architecture/registry`
> - `20_architecture/schema`
> - `20_architecture/data_model`
> 
> ### 7. Operations / service map split
> 
> Operations and service documentation appears in:
> 
> - `00_QiEOS/30_service_map`
> - `00_QiEOS/40_operations`
> - `30_QiServer`
> - `70_QiConnect`
> 
> Reconcile into:
> 
> - `50_services`
> - `60_operations`
> - `40_applications`
> - `30_system`
> 
> ### 8. Assets/templates/generated site files
> 
> Assets and templates should remain separate from doctrine and architecture.
> 
> Recommended destinations:
> 
> - `70_assets/templates`
> - `70_assets/images`
> - `70_assets/diagrams`
> - `site`
> 
> Generated site/build files should remain isolated and should not be treated as source doctrine.
> 
> ### 9. Manual-to-Me material
> 
> The folder:
> 
> `PART XI - Manual to Me`
> 
> contains personal manual PDFs/audio/images. It should not be mixed into QiOS doctrine.
> 
> Recommended destination:
> 
> `75_personal_manual`
> 
> Preserve it as its own material set.
> 
> ## Proposed Flattened Canonical Tree
> 
> Create a proposed migration plan toward this structure:
> 
> ```text
> _QiOS_DNA/
>   00_root/
>     README.md
>     index.md
>     codex.md
>     Current_Project_State.md
> 
>   00_governance/
>     principles/
>     rules/
>     standards/
>     policies/
>     decisions/
> 
>   10_doctrine/
>     QiOS_Core_Doctrine.mdx
>     QiOS_Master_Map.mdx
>     QiOS_DNA_Chronicle.md
> 
>   20_architecture/
>     identity/
>     system_model/
>     component_map/
>     service_boundaries/
>     data_flow/
>     device_model/
>     runtime_zones/
>     registry/
>     schema/
>     data_model/
> 
>   30_system/
>     modules/
>     ai_layer/
>     deployment/
>     prompts/
>     manifests/
>     rules/
> 
>   40_applications/
>     QiAccess/
>     QiLife/
>     QiJourney/
>     QiCapture/
>     QiNexus/
> 
>   50_services/
>     infrastructure/
>     ai_compute/
>     capture_services/
>     productivity/
>     apis/
>     workers/
>     pipelines/
>     tools/
>     interfaces/
>     integrations/
>     qiserver/
>     qiconnect/
> 
>   60_operations/
>     runbooks/
>     cases/
>     dev_history/
>     dev_testing/
>     maintenance/
> 
>   70_assets/
>     diagrams/
>     images/
>     templates/
> 
>   75_personal_manual/
>     Manual_to_Me/
> 
>   80_reconciliation/
>     current_state/
>     audits/
>     gap_reports/
>     migration_plans/
>     site_coverage/
>     implementation_reviews/
> 
>   90_receipts/
>     logs/
>     audits/
>     backups/
>     health_checks/
>     generated_reports/
>     generated_indexes/
>     changelog/
> 
>   90_archive/
>     superseded_sources/
>     legacy_qiaccess/
>     decisions_superseded/
>     generated_reports_superseded/
>     old_tree_snapshots/
> 
>   site/
>     index.html
>     script.js
>     style.css
> 
>   package.json
>   package-lock.json
>   build.js
>   docs.json
>   CNAME
>   .gitignore
> ```
> 
> This structure is a proposal. Before applying it, generate a migration report and highlight any conflicts.
> 
> ## Required Deliverables
> 
> Create these files first:
> 
> ### 1. Tree inventory
> 
> `80_reconciliation/tree_flattening/file_inventory.json`
> 
> Include every file with:
> 
> - current path
> - filename
> - extension
> - size if available
> - inferred category
> - inferred canonical destination
> - duplicate candidates
> - confidence score
> - recommended action
> 
> ### 2. Human-readable inventory
> 
> `80_reconciliation/tree_flattening/file_inventory.md`
> 
> Summarize files by category and destination.
> 
> ### 3. Migration map
> 
> `80_reconciliation/tree_flattening/migration_map.csv`
> 
> Columns:
> 
> - current_path
> - proposed_path
> - action
> - reason
> - confidence
> - needs_human_review
> - notes
> 
> Allowed actions:
> 
> - keep
> - move
> - copy
> - rename
> - merge
> - archive
> - preserve_reference
> - needs_human_review
> 
> ### 4. Duplicate and merge report
> 
> `80_reconciliation/tree_flattening/duplicate_merge_report.md`
> 
> For each duplicate/overlap group, include:
> 
> - files involved
> - why they overlap
> - whether content appears identical, partially overlapping, or different
> - recommended canonical file
> - recommended archive file
> - recommended merge strategy
> 
> ### 5. Proposed new tree
> 
> `80_reconciliation/tree_flattening/proposed_tree.md`
> 
> Show the final target structure.
> 
> ### 6. Rollback plan
> 
> `80_reconciliation/tree_flattening/rollback_plan.md`
> 
> Include how to undo moves using the migration map.
> 
> ## Execution Phases
> 
> ### Phase 1 — Inventory only
> 
> Scan the full tree. Produce inventory files. Do not move files yet.
> 
> ### Phase 2 — Detect duplicates and overlaps
> 
> Compare files by:
> 
> - filename similarity
> - normalized title similarity
> - content similarity
> - front matter similarity
> - heading similarity
> - date/version indicators
> - path/category context
> 
> Flag duplicate candidates. Do not assume identical names mean identical content.
> 
> ### Phase 3 — Build migration map
> 
> Map every file to a proposed canonical destination.
> 
> Files should be categorized as:
> 
> - canonical_source
> - doctrine
> - governance
> - adr_decision
> - architecture
> - registry
> - schema
> - module_doc
> - app_doc
> - service_doc
> - operation_runbook
> - reconciliation_report
> - generated_report
> - receipt_log
> - asset
> - template
> - site_build_file
> - legacy_reference
> - personal_manual
> - unknown
> 
> ### Phase 4 — Create snapshot
> 
> Before any move/copy operation, create a snapshot manifest:
> 
> `90_archive/old_tree_snapshots/pre_flatten_snapshot_manifest.json`
> 
> This should record the original tree paths.
> 
> ### Phase 5 — Apply only safe moves
> 
> Only move files with high confidence.
> 
> If a file has duplicate candidates, unclear canonical status, or conflicting possible destinations, do not move it. Mark it as `needs_human_review`.
> 
> ### Phase 6 — Update indexes
> 
> After safe moves, update or create `_index.md` files for each top-level canonical folder.
> 
> Each index should explain:
> 
> - what belongs here
> - what does not belong here
> - notable migrated files
> - pending review items
> 
> ### Phase 7 — Final report
> 
> Create:
> 
> `80_reconciliation/tree_flattening/final_tree_reconciliation_report.md`
> 
> Include:
> 
> - number of files scanned
> - number moved
> - number copied
> - number archived
> - number needing review
> - unresolved duplicates
> - recommended next actions
> 
> ## Important Classification Guidance
> 
> Use this logic:
> 
> ### Governance
> 
> Rules, standards, policies, principles, and ADRs belong under:
> 
> `00_governance`
> 
> ### Doctrine
> 
> Core philosophy, master doctrine, system doctrine, and canonical narrative belong under:
> 
> `10_doctrine`
> 
> ### Architecture
> 
> System model, data model, registry, schema, component maps, service boundaries, object models, and runtime zones belong under:
> 
> `20_architecture`
> 
> ### System
> 
> QiSystem, modules, AI layer, prompts, deployment, manifests, and source-of-truth rules belong under:
> 
> `30_system`
> 
> ### Applications
> 
> QiAccess, QiLife, QiJourney, QiCapture, and QiNexus app/product docs belong under:
> 
> `40_applications`
> 
> ### Services
> 
> Infrastructure, qiserver, qiconnect, integrations, APIs, pipelines, workers, tools, interfaces, and hosted services belong under:
> 
> `50_services`
> 
> ### Operations
> 
> Runbooks, operational cases, dev history, testing, maintenance, and support docs belong under:
> 
> `60_operations`
> 
> ### Assets
> 
> Diagrams, images, media, templates, markmind exports, and visual files belong under:
> 
> `70_assets`
> 
> ### Personal manual
> 
> The “Manual to Me” folder and related PDFs/audio/images belong under:
> 
> `75_personal_manual`
> 
> Do not mix these with QiOS doctrine.
> 
> ### Reconciliation
> 
> Audits, gap reports, migration plans, implementation reviews, site coverage reports, blueprint readiness reports, and non-destructive reconciliation plans belong under:
> 
> `80_reconciliation`
> 
> ### Receipts
> 
> Logs, generated reports, generated indexes, backups, changelogs, validation reports, and audit artifacts belong under:
> 
> `90_receipts`
> 
> ### Archive
> 
> Superseded sources, legacy blueprints, obsolete drafts, duplicate ADRs, older generated reports, and old snapshots belong under:
> 
> `90_archive`
> 
> ## Special Warnings
> 
> The following files/folders require extra caution:
> 
> - `QiAccess_Start_Blueprint.md`
> - `Current_Project_State.md`
> - `README.md`
> - `_index.md`
> - `index.mdx`
> - `file-index.json`
> - `docs.json`
> - anything under `decisions`
> - anything under `00_QiEOS/10_governance/50_decisions`
> - anything under `Reconciliation`
> - anything under `00_QiEOS/reconciliation`
> - anything under `20_QiSystem`
> - anything under `PART XI - Manual to Me`
> 
> Do not blindly move these without checking content and destination.
> 
> ## Naming Rules
> 
> Normalize folder and file names only when safe.
> 
> Preferred style:
> 
> - lowercase folders unless existing Qi-branded names are meaningful
> - snake_case for files
> - ADR files should use `ADR-####_short_title.md`
> - dated reports should use `YYYY-MM-DD_short_title.md`
> - indexes should remain `_index.md` or `index.md` depending on current site generator expectations
> 
> Do not rename files if the site/build system depends on exact filenames until references are checked.
> 
> ## Reference Checking
> 
> Before moving or renaming any Markdown/MDX file, search for references to its old path or filename in:
> 
> - Markdown links
> - MDX imports
> - `docs.json`
> - `file-index.json`
> - build scripts
> - navigation files
> - README files
> - site generator config
> 
> If references exist, list them in the migration report. Do not update references automatically unless the move is high-confidence and easy to verify.
> 
> ## Final Instruction
> 
> Treat this as a controlled tree refactor.
> 
> Do not try to “make it pretty” at the expense of traceability.
> 
> The correct outcome is:
> 
> 1. fewer top-level concepts,
> 2. clearer canonical homes,
> 3. legacy material preserved but not confused with active doctrine,
> 4. duplicate docs identified,
> 5. generated outputs separated from source docs,
> 6. a migration map that allows rollback,
> 7. unresolved ambiguity surfaced instead of guessed away.
> :::
> 
> ## My actual recommendation
> 
> Don’t let Codex move everything in one shot. That’s how you make a beautiful catastrophe.
> 
> Use this sequence:
> 
> 1. **Inventory only**
> 2. **Migration map only**
> 3. Review the migration map
> 4. Then run “safe moves only”
> 5. Then handle duplicates/merges manually or in small batches
> 
> The clean target model is basically:
> 
> | Layer | Purpose |
> |---|---|
> | `00_governance` | rules, policies, ADRs |
> | `10_doctrine` | master philosophy / canonical doctrine |
> | `20_architecture` | system shape, schema, registry |
> | `30_system` | QiSystem implementation docs |
> | `40_applications` | QiLife, QiAccess, QiJourney, etc. |
> | `50_services` | server, infra, integrations |
> | `60_operations` | runbooks and dev/testing ops |
> | `70_assets` | images, diagrams, templates |
> | `75_personal_manual` | Manual-to-Me material |
> | `80_reconciliation` | audits, gap reports, migration plans |
> | `90_receipts` | generated reports/logs/changelog |
> | `90_archive` | superseded/legacy/reference junk drawer, but labeled |
> 
> The key principle: **flatten by responsibility, not by impatience.**

### User
> if you look at the whole file tree, im sure some of the items inside qieos acutally belong in there domain folders instead. {
>   "name": "_QiOS_DNA",
>   "path": "c:\\QiLabs\\_QiOS_DNA",
>   "type": "directory",
>   "children": [
>     {
>       "name": "00_QiEOS",
>       "type": "folder",
>       "children": [
>         {
>           "name": "10_governance",
>           "type": "folder",
>           "children": [
>             {
>               "name": "10_principles",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "20_rules",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "30_standards",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "content_metadata_profile.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "metadata_rules.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "naming_rules.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "pdf_standards.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "repo_rules.yaml",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "40_policies",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "agents",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "agent_governance_policy.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "architecture",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "active_runtime_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "placement_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "registry_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "root_navigation_policy.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "development",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "bootstrap_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "contribution_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "merge_policy.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "operations",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "legacy_quarantine_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "lifecycle_policy.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "qinexus_freeze_policy.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "security",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "security_data_access_policy.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "50_decisions",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ADR-0000_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0001_QiOS_DNA_As_Master_Doctrine_Repo.mdx",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0001_blueprint_scope.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0002_single_domain_rule.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0003_band_model.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0004_single_account_modular_mode.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0005_fleet_orchestration.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0006_narrative_and_knowledge_consolidation.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0007_unified_front_matter_and_progressive_doc_topology.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0008_qilabs_root.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0009_backup_server_control_plane_and_public_edge_pattern.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ADR-0010_qios_namespace_as_routing_metadata_layer.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "60_registry",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "namespace_registry",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "2026-05-18_qios_namespace_registry_merged_v2.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "schemas",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "band_registry.schema.json",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "100_metadata.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "10_infrastructure_layout.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "110_front_matter.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "120_storage.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "130_placement_rules.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "140_exports.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "150_qievidence.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "160_vectorization_pipeline.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "20_bands.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "30_domains.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "40_subdomains.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "60_directory_tree.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "70_object_model.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "80_objects.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "90_schema.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "band_registry.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "band_registry_v2.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "deprecation_registry.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "domain_registry.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "folder_registry.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "infrastructure_registry.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "realms_registry.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "sensitivity_classification.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "subdomain_registry.yaml",
>                   "type": "file"
>                 },
>                 {
>                   "name": "workspace_realms.yaml",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "_index.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "20_structure",
>           "type": "folder",
>           "children": [
>             {
>               "name": "10_identity.md",
>               "type": "file"
>             },
>             {
>               "name": "20_system_model.md",
>               "type": "file"
>             },
>             {
>               "name": "30_component_map.md",
>               "type": "file"
>             },
>             {
>               "name": "40_service_boundaries.md",
>               "type": "file"
>             },
>             {
>               "name": "50_data_flow.md",
>               "type": "file"
>             },
>             {
>               "name": "60_device_model.md",
>               "type": "file"
>             },
>             {
>               "name": "70_runtime_zones.md",
>               "type": "file"
>             },
>             {
>               "name": "_index.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "30_service_map",
>           "type": "folder",
>           "children": [
>             {
>               "name": "100_integrations",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "external_integrations.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "10_infrastructure",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "cockpit",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     },
>                     {
>                       "name": "cockpit_command_menu.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "cloudflare.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "docker_compose.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "gethomepage.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "portainer.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "tailscale.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "uptime_kuma.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "110_qiserver",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "Service_Map.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "runtime.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "runtime_profile.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "120_applications",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "CareLite",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "qinote",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "qinote_salvage_extract.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "admin.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "carelite.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "firefly.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "portal.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "roadmap.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "130_GINA",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "20_ai_compute",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "aider.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "neo4j.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ollama.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "open_webui.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qdrant.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "30_capture",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "paperless",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "_index.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "nocodb.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "obsidian_qidocs.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "wikijs.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "40_productivity",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "activitywatch.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "n8n.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qiledger.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "solidtime.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "50_apis",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "portal_api.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "60_workers",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "system_workers.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "70_pipelines",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_pipelines.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "80_tools",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "operator_tools.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "90_interfaces",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "public_interfaces.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "_index.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "40_operations",
>           "type": "folder",
>           "children": [
>             {
>               "name": "10_cases",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "20_qiserver",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "QiAccess_Server_Runbook.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "30_dev_history",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "2026-05-16_dev_session_directory_markmind_mapper.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "2026-05-17_open_loop_reset_paperless_ingestion_runbook.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "40_dev_testing",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "momscare",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "2026-05-17_momcare_app_qa_checklist.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "qiaccessstart",
>                   "type": "folder",
>                   "children": [
>                     {
>                       "name": "2026-05-17_qiaccess_start_qa_checklist.md",
>                       "type": "file"
>                     }
>                   ]
>                 },
>                 {
>                   "name": "Access_And_Exposure_Rules.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "_index.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "50_knowledge",
>           "type": "folder",
>           "children": [
>             {
>               "name": "90_superseded_sources",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "2025-11-18_qicodex_protocol_batch_overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "QiAccess_Start_Blueprint.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "README.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qi_os_home_blueprint.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "tech_stack_markmind.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "20_glossary.md",
>               "type": "file"
>             },
>             {
>               "name": "30_migration_notes.md",
>               "type": "file"
>             },
>             {
>               "name": "40_legacy_csv_migration_plan.md",
>               "type": "file"
>             },
>             {
>               "name": "50_legacy_salvage.md",
>               "type": "file"
>             },
>             {
>               "name": "60_qiaccess_start_legacy_quarantine.md",
>               "type": "file"
>             },
>             {
>               "name": "70_repo_sync_status_20260516.md",
>               "type": "file"
>             },
>             {
>               "name": "_index.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "60_assets",
>           "type": "folder",
>           "children": [
>             {
>               "name": "diagrams",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "2026-05-17_supabase_markmind.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "blueprint_map.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "diagrams.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "markmind-data.json",
>                   "type": "file"
>                 },
>                 {
>                   "name": "markmind.html",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "images",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_QiOS_Master_Document.jpg",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "templates",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "2026-05-16_dev_session_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "README.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "adr_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "appendix_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "artifact_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "note_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "operational_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "page_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "registry_reference_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "section_index_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "standard_template.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "templates.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "assets.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "90_receipts",
>           "type": "folder",
>           "children": [
>             {
>               "name": "10_logs",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "20_audits",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "30_backups",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "40_health_checks",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "50_generated_reports",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "current_project_state.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qilabs_structure_check.csv",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qilabs_structure_check.json",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qilabs_structure_check.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "60_generated_indexes",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "70_maintenance",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "_index.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "_audit",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "2026-05-24_qiaccess_homepage_conversion_report.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "2026-05-24_qiaccess_homepage_local_validation_report.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "2026-05-24_qilinks_admin_and_visual_map_plan.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qiaccess_map.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "qiaccess_map.mmd",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "10_changelog.md",
>               "type": "file"
>             },
>             {
>               "name": "Current_Project_State.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "doctrine",
>           "type": "folder",
>           "children": [
>             {
>               "name": "QiOS_Core_Doctrine.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "exports",
>           "type": "folder",
>           "children": [
>             {
>               "name": "QiOS_DNA_Chronicle.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "reconciliation",
>           "type": "folder",
>           "children": [
>             {
>               "name": "2026-06-09_codex_reconciliation_brief.md",
>               "type": "file"
>             },
>             {
>               "name": "2026-06-09_initial_reconciliation.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "system_map",
>           "type": "folder",
>           "children": [
>             {
>               "name": "QiOS_Master_Map.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "QiAccess_Start_Blueprint.md",
>           "type": "file"
>         },
>         {
>           "name": "README.md",
>           "type": "file"
>         },
>         {
>           "name": "_QiEOS.md",
>           "type": "file"
>         },
>         {
>           "name": "_index.md",
>           "type": "file"
>         },
>         {
>           "name": "file-index.json",
>           "type": "file"
>         },
>         {
>           "name": "rebuild.bat",
>           "type": "file"
>         },
>         {
>           "name": "vizvibe.mmd",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "10_QiAccess",
>       "type": "folder",
>       "children": [
>         {
>           "name": "_10_QiAccess.md",
>           "type": "file"
>         },
>         {
>           "name": "index.mdx",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "20_QiSystem",
>       "type": "folder",
>       "children": [
>         {
>           "name": "50_Generated_Reports",
>           "type": "folder",
>           "children": [
>             {
>               "name": "2026-06-08_qilife_governance_audit.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "50_modules",
>           "type": "folder",
>           "children": [
>             {
>               "name": "calendar",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "capture",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "documents",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ai_behaviors.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "context_dock.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_dependencies.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "inbox",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ai_behaviors.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "context_dock.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_dependencies.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "ingestion",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "knowledge",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ai_behaviors.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "context_dock.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_dependencies.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "money",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ai_behaviors.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "context_dock.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_dependencies.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "people",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ai_behaviors.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "context_dock.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_dependencies.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "qibits",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ai_behaviors.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "context_dock.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_dependencies.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "review",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "spaces",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "storage",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "threads",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ai_behaviors.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "context_dock.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_dependencies.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "timeline",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "ai_behaviors.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "context_dock.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "data_dependencies.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "overview.md",
>                   "type": "file"
>                 },
>                 {
>                   "name": "ui_flow.md",
>                   "type": "file"
>                 }
>               ]
>             }
>           ]
>         },
>         {
>           "name": "60_ai_layer",
>           "type": "folder",
>           "children": [
>             {
>               "name": "00_ai_layer_blueprint.md",
>               "type": "file"
>             },
>             {
>               "name": "01_ai_service_contracts.md",
>               "type": "file"
>             },
>             {
>               "name": "02_ai_review_workflow.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "70_deployment",
>           "type": "folder",
>           "children": [
>             {
>               "name": "00_local_dev.md",
>               "type": "file"
>             },
>             {
>               "name": "01_future_docker.md",
>               "type": "file"
>             },
>             {
>               "name": "02_future_qiserver.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "80_prompts",
>           "type": "folder",
>           "children": [
>             {
>               "name": "00_codex_build_prompt_v1.md",
>               "type": "file"
>             },
>             {
>               "name": "01_codex_review_prompt.md",
>               "type": "file"
>             },
>             {
>               "name": "02_will_be_done_research_prompt.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "manifests",
>           "type": "folder",
>           "children": [
>             {
>               "name": "QiOS_DNA_File_Manifest.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "rules",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Source_of_Truth_Rules.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "schemas",
>           "type": "folder",
>           "children": [
>             {
>               "name": "QiLife_Data_Spine.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "_20_QiSystem.md",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "30_QiServer",
>       "type": "folder",
>       "children": [
>         {
>           "name": "_30_QiServer.md",
>           "type": "file"
>         },
>         {
>           "name": "index.mdx",
>           "type": "file"
>         },
>         {
>           "name": "qiserver_runbook.md",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "40_QiCapture",
>       "type": "folder",
>       "children": [
>         {
>           "name": "_40_QiCapture.md",
>           "type": "file"
>         },
>         {
>           "name": "index.mdx",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "50_QiNexus",
>       "type": "folder",
>       "children": [
>         {
>           "name": "My_Drive_Model",
>           "type": "folder",
>           "children": [
>             {
>               "name": "index.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "_50_QiNexus.md",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "60_QiApp_QiLife",
>       "type": "folder",
>       "children": [
>         {
>           "name": "_60_QiApp_QiLife.md",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "60_QiApps",
>       "type": "folder",
>       "children": [
>         {
>           "name": "QiJourney",
>           "type": "folder",
>           "children": [
>             {
>               "name": "index.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "QiLife",
>           "type": "folder",
>           "children": [
>             {
>               "name": "index.mdx",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "qiaccess_start",
>           "type": "folder",
>           "children": [
>             {
>               "name": "overview.md",
>               "type": "file"
>             },
>             {
>               "name": "wiki_publish_plan.md",
>               "type": "file"
>             }
>           ]
>         }
>       ]
>     },
>     {
>       "name": "70_QiConnect",
>       "type": "folder",
>       "children": [
>         {
>           "name": "06_workflows",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Automation_Backlog.md",
>               "type": "file"
>             },
>             {
>               "name": "Core_Workflows.md",
>               "type": "file"
>             },
>             {
>               "name": "QiIngest_Pipeline.md",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "_70_QiConnect.md",
>           "type": "file"
>         },
>         {
>           "name": "index.mdx",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "PART XI - Manual to Me",
>       "type": "folder",
>       "children": [
>         {
>           "name": "00 CLIFF NOTES Manual to Me - Cody's Guide 203f84a04402802cbf08d7edabcd80c1",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "01 Who I Am Core Identity & Values 203f84a0440280649bd1d30bffb5edfc",
>           "type": "folder",
>           "children": [
>             {
>               "name": "94d60b86-a732-4d2c-b2dc-1ddd74c96dce.jfif",
>               "type": "file"
>             },
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_-_01_Who_I_Am_Core_Identity__Values.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "02 How I Work Focus, Flow, Boundaries 203f84a04402806fb95fc0862c0556e8",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_-_02__How_I_Work_Focus_Flow_Boundaries.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "03 How I Relate Communication & Boundaries 203f84a044028063a81ae8e5867e8618",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "04 How I Feel Emotional Landscape 203f84a0440280e6927af392a916c6bf",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_04__How_I_Feel_Emotional_Landscape.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "05 How I Grow Learning & Creativity 203f84a044028098a2dbec92694a4358",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_05__How_I_Grow_Learning__Creativity.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "06 How I Operate Routines & Energy Management 203f84a04402803fa35cffab28a6ee91",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_-_06__How_I_Operate_Routines__Energy_Management.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "07 How to Support Me Needs & Triggers 203f84a0440280cc8f5ece450f21978f",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_-_07__How_to_Support_Me_Needs__Triggers.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "08 When I Struggle Overwhelm, Shutdown, Recovery 203f84a0440280e2bd8bdb18da258847",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_-_08__When_I_Struggle_Overwhelm_Shutdown_Recovery.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "09 Building Bridges Mutual Understanding 203f84a0440280dfb159f34e6b6c7ecb",
>           "type": "folder",
>           "children": [
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_-_09__Building_Bridges_Mutual_Understanding.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "10 Learn More About… 203f84a044028017ab5bfc6269a4b4ac",
>           "type": "folder",
>           "children": [
>             {
>               "name": "10 9 ADHD 203f84a0440280a7abc8dafbd78ac3e1",
>               "type": "folder",
>               "children": [
>                 {
>                   "name": "10 9a Time Management Challenges in Neurodivergent 203f84a04402800bb533fa5e22a971c0.pdf",
>                   "type": "file"
>                 },
>                 {
>                   "name": "10 9b Focus Irregularities and How They Impact Dai 203f84a0440280a79100d36b85f803f8.pdf",
>                   "type": "file"
>                 },
>                 {
>                   "name": "10 9c The Invisible Weight of Executive Function C 203f84a04402806b8c40f3e83a2a9b5d.pdf",
>                   "type": "file"
>                 }
>               ]
>             },
>             {
>               "name": "10 1 Transgender 203f84a044028084bdbfec332d881b7c.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 10 Correspondence Anxiety 203f84a044028022ae12cfc1e77fa7c3.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 2 Sleep inertia 203f84a0440280efbebce629dd529f36.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 3 Delayed sleep phase 203f84a04402807ba39ccbec0500a164.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 4 Person of Color 203f84a0440280218544fb4d96808b5b.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 5 Phonophobia 203f84a0440280a49d46ea1d2121a02d.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 6 Depression 203f84a044028046a765cb0568eac83a.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 7 PTSD 203f84a0440280628a38e26e5e7cb1bc.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 8 Anxiety 203f84a0440280fa9a97cd796ee8fe0c.pdf",
>               "type": "file"
>             },
>             {
>               "name": "10 9 ADHD 203f84a0440280a7abc8dafbd78ac3e1.pdf",
>               "type": "file"
>             },
>             {
>               "name": "Codys_Guide_to_Understanding_and_Connection_-_10__Learn_More_About.wav",
>               "type": "file"
>             }
>           ]
>         },
>         {
>           "name": "00 CLIFF NOTES Manual to Me - Cody's Guide 203f84a04402802cbf08d7edabcd80c1.pdf",
>           "type": "file"
>         },
>         {
>           "name": "01 Who I Am Core Identity & Values 203f84a0440280649bd1d30bffb5edfc.pdf",
>           "type": "file"
>         },
>         {
>           "name": "02 How I Work Focus, Flow, Boundaries 203f84a04402806fb95fc0862c0556e8.pdf",
>           "type": "file"
>         },
>         {
>           "name": "03 How I Relate Communication & Boundaries 203f84a044028063a81ae8e5867e8618.pdf",
>           "type": "file"
>         },
>         {
>           "name": "04 How I Feel Emotional Landscape 203f84a0440280e6927af392a916c6bf.pdf",
>           "type": "file"
>         },
>         {
>           "name": "05 How I Grow Learning & Creativity 203f84a044028098a2dbec92694a4358.pdf",
>           "type": "file"
>         },
>         {
>           "name": "06 How I Operate Routines & Energy Management 203f84a04402803fa35cffab28a6ee91.pdf",
>           "type": "file"
>         },
>         {
>           "name": "07 How to Support Me Needs & Triggers 203f84a0440280cc8f5ece450f21978f.pdf",
>           "type": "file"
>         },
>         {
>           "name": "08 When I Struggle Overwhelm, Shutdown, Recovery 203f84a0440280e2bd8bdb18da258847.pdf",
>           "type": "file"
>         },
>         {
>           "name": "09 Building Bridges Mutual Understanding 203f84a0440280dfb159f34e6b6c7ecb.pdf",
>           "type": "file"
>         },
>         {
>           "name": "1 5 Personality NTFJ 295f84a0440280f396e7cddbaf3c905b.pdf",
>           "type": "file"
>         },
>         {
>           "name": "10 Learn More About… 203f84a044028017ab5bfc6269a4b4ac.pdf",
>           "type": "file"
>         },
>         {
>           "name": "Codys_Guide_to_Understanding_and_Connection_(1).wav",
>           "type": "file"
>         },
>         {
>           "name": "Codys_Guide_to_Understanding_and_Connection_-_An_Overview.wav",
>           "type": "file"
>         },
>         {
>           "name": "Compass-Icon.png",
>           "type": "file"
>         },
>         {
>           "name": "Thank You for Taking This Journey 203f84a0440280efbc16d8451dc9cda1.pdf",
>           "type": "file"
>         },
>         {
>           "name": "ZwC7IC_S4_GX9Z6--2mx7.png",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "Reconciliation",
>       "type": "folder",
>       "children": [
>         {
>           "name": "2026-06-10_blueprint_readiness_and_decision_gate.md",
>           "type": "file"
>         },
>         {
>           "name": "2026-06-10_database_blueprint_gap_report.md",
>           "type": "file"
>         },
>         {
>           "name": "2026-06-10_documentation_status_map.md",
>           "type": "file"
>         },
>         {
>           "name": "2026-06-10_non_destructive_reconciliation_plan.md",
>           "type": "file"
>         },
>         {
>           "name": "2026-06-10_qidna_implementation_reconciliation.md",
>           "type": "file"
>         },
>         {
>           "name": "2026-06-10_qilife_schema_source_report.md",
>           "type": "file"
>         },
>         {
>           "name": "2026-06-10_site_coverage_report.md",
>           "type": "file"
>         },
>         {
>           "name": "2026-06-10_ui_blueprint_gap_report.md",
>           "type": "file"
>         },
>         {
>           "name": "_Reconciliation.md",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "Schema",
>       "type": "folder",
>       "children": [
>         {
>           "name": "_Schema.md",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "decisions",
>       "type": "folder",
>       "children": [
>         {
>           "name": "0001_personal_lifedesk_model.md",
>           "type": "file"
>         },
>         {
>           "name": "0002_qibit_as_atomic_unit.md",
>           "type": "file"
>         },
>         {
>           "name": "0003_timeline_as_spine.md",
>           "type": "file"
>         },
>         {
>           "name": "0004_context_dock_over_wiki.md",
>           "type": "file"
>         },
>         {
>           "name": "0005_repo_docs_indexed_in_app.md",
>           "type": "file"
>         },
>         {
>           "name": "0006_clean_core_with_legacy_bridge.md",
>           "type": "file"
>         },
>         {
>           "name": "0007_app_managed_storage_and_sync.md",
>           "type": "file"
>         },
>         {
>           "name": "0008_managed_document_vault_dup_allergic.md",
>           "type": "file"
>         },
>         {
>           "name": "0009_agent_first_copilot_cockpit.md",
>           "type": "file"
>         },
>         {
>           "name": "0010_spaces_for_scoped_shared_access.md",
>           "type": "file"
>         },
>         {
>           "name": "ADR-0011_homepage_powered_qiaccess.md",
>           "type": "file"
>         },
>         {
>           "name": "ADR-0012_data_strategy.md",
>           "type": "file"
>         },
>         {
>           "name": "ADR-0013_folder_documentation_model.md",
>           "type": "file"
>         },
>         {
>           "name": "ADR-0014_topology_constraints.md",
>           "type": "file"
>         },
>         {
>           "name": "ADR-0015_build_strategy.md",
>           "type": "file"
>         },
>         {
>           "name": "ADR-0016_ai_auditor_role.md",
>           "type": "file"
>         },
>         {
>           "name": "ADR-0017_canonical_vocabulary_and_v1_direction.md",
>           "type": "file"
>         },
>         {
>           "name": "_Decisions.md",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": "site",
>       "type": "folder",
>       "children": [
>         {
>           "name": "_site.md",
>           "type": "file"
>         },
>         {
>           "name": "index.html",
>           "type": "file"
>         },
>         {
>           "name": "script.js",
>           "type": "file"
>         },
>         {
>           "name": "style.css",
>           "type": "file"
>         }
>       ]
>     },
>     {
>       "name": ".gitignore",
>       "type": "file"
>     },
>     {
>       "name": "CNAME",
>       "type": "file"
>     },
>     {
>       "name": "Current_Project_State.md",
>       "type": "file"
>     },
>     {
>       "name": "Folder_Canvas.canvas",
>       "type": "file"
>     },
>     {
>       "name": "README.md",
>       "type": "file"
>     },
>     {
>       "name": "_01_QiDNA.md",
>       "type": "file"
>     },
>     {
>       "name": "_Architecture.md",
>       "type": "file"
>     },
>     {
>       "name": "build.js",
>       "type": "file"
>     },
>     {
>       "name": "code_extractor.py",
>       "type": "file"
>     },
>     {
>       "name": "codex.md",
>       "type": "file"
>     },
>     {
>       "name": "docs.json",
>       "type": "file"
>     },
>     {
>       "name": "fix_folder_names.sh",
>       "type": "file"
>     },
>     {
>       "name": "index.md",
>       "type": "file"
>     },
>     {
>       "name": "package-lock.json",
>       "type": "file"
>     },
>     {
>       "name": "package.json",
>       "type": "file"
>     },
>     {
>       "name": "qilinks_bookmark_admin_plan.md",
>       "type": "file"
>     }
>   ],
>   "metadata": {
>     "generated": "2026-06-13T15:45:34.446Z",
>     "generator": "FileTree Pro Extension",
>     "version": "0.2.0",
>     "showIcons": false,
>     "maxDepth": 10
>   }
> }

### Assistant
> Yes — exactly. `00_QiEOS` should not be a dumping ground. It should hold **QiEOS-specific doctrine/governance**, while app/server/capture/nexus/connect docs should migrate back into their domain homes.

### Assistant
> You’re seeing the real architecture problem:
> 
> ## The mistake in the current tree
> 
> `00_QiEOS` is currently behaving like:
> 
> > “the place where important things go”
> 
> That’s wrong.
> 
> It should behave like:
> 
> > “the constitutional/governance layer that defines how the rest of the system is organized.”
> 
> So yes: a bunch of things inside `00_QiEOS` likely belong in domain folders:
> 
> | Current inside `00_QiEOS` | Better home |
> |---|---|
> | `30_service_map/10_infrastructure/cloudflare.md` | `30_QiServer` or `70_QiConnect`, depending on whether it is runtime infra or connection layer |
> | `30_service_map/10_infrastructure/portainer.md` | `30_QiServer` |
> | `30_service_map/10_infrastructure/tailscale.md` | `30_QiServer` / `70_QiConnect` |
> | `30_service_map/20_ai_compute/ollama.md` | `20_QiSystem` or `30_QiServer`, depending on whether it describes system AI layer or server runtime |
> | `30_service_map/30_capture/paperless` | `40_QiCapture` |
> | `30_service_map/30_capture/wikijs.md` | probably `50_QiNexus` or docs/capture depending on role |
> | `30_service_map/40_productivity/firefly/qiledger/etc.` | likely app/service domain, not QiEOS |
> | `30_service_map/120_applications/carelite.md` | app domain |
> | `40_operations/20_qiserver/QiAccess_Server_Runbook.md` | `30_QiServer` or `10_QiAccess`, depending on content |
> | `40_operations/40_dev_testing/qiaccessstart` | `10_QiAccess` or `60_QiApps/qiaccess_start` |
> | `50_knowledge/60_qiaccess_start_legacy_quarantine.md` | QiAccess archive |
> | `60_assets/templates/adr_template.md` | governance templates, yes, maybe stays near governance |
> | `60_assets/images` | root assets, not QiEOS-specific |
> | `90_receipts` | root `90_receipts`, not inside QiEOS |
> | `reconciliation` | root `Reconciliation` / `80_reconciliation` |
> | `system_map/QiOS_Master_Map.mdx` | doctrine/architecture, maybe QiEOS if master map governs all |
> 
> The rule is simple:
> 
> > **QiEOS owns the rules of the system. Domains own the operational facts of their domain.**
> 
> Here’s the improved prompt to give your IDE/Codex.
> 
> :::writing{variant="standard" id="31874"}
> We need to reconcile the `_QiOS_DNA` file tree with special attention to the fact that many files currently inside `00_QiEOS` likely belong in their actual domain folders.
> 
> Repository root:
> 
> `C:\QiLabs\_QiOS_DNA`
> 
> ## Core Correction
> 
> `00_QiEOS` should not be a general-purpose home for everything important.
> 
> `00_QiEOS` should contain only system-wide constitutional material:
> 
> - doctrine
> - governance
> - principles
> - rules
> - standards
> - policies
> - architecture decisions
> - canonical registries
> - cross-domain system model
> - source-of-truth rules
> - topology rules
> - naming rules
> - lifecycle rules
> 
> Domain-specific operational documents should live in their domain folders.
> 
> For example:
> 
> - QiAccess docs belong in `10_QiAccess`
> - QiSystem docs belong in `20_QiSystem`
> - QiServer docs belong in `30_QiServer`
> - QiCapture docs belong in `40_QiCapture`
> - QiNexus docs belong in `50_QiNexus`
> - QiLife / QiJourney docs belong in `60_QiApps`
> - QiConnect docs belong in `70_QiConnect`
> - Reconciliation docs belong in `Reconciliation` or proposed `80_reconciliation`
> - Receipts/generated reports/logs belong in a root receipts/archive area
> - Personal “Manual to Me” material should remain separate from QiEOS doctrine
> 
> ## Task
> 
> Perform a non-destructive domain-placement audit of all files currently inside:
> 
> `00_QiEOS`
> 
> Determine which files truly belong in `00_QiEOS` and which should be moved, copied, merged, archived, or reviewed under their correct domain folder.
> 
> Do not delete anything.
> 
> Do not overwrite anything.
> 
> Do not move anything until after producing the audit report and migration map.
> 
> ## Required Output Files
> 
> Create a new folder:
> 
> `Reconciliation\qieos_domain_placement_audit`
> 
> Create these files:
> 
> 1. `qieos_domain_placement_inventory.md`
> 2. `qieos_domain_placement_inventory.json`
> 3. `qieos_domain_migration_map.csv`
> 4. `qieos_keep_vs_move_report.md`
> 5. `qieos_domain_conflicts.md`
> 6. `qieos_safe_moves_plan.md`
> 
> ## Classification Rules
> 
> For every file under `00_QiEOS`, classify it as one of:
> 
> - `keep_in_qieos`
> - `move_to_qiaccess`
> - `move_to_qisystem`
> - `move_to_qiserver`
> - `move_to_qicapture`
> - `move_to_qinexus`
> - `move_to_qiapps`
> - `move_to_qiconnect`
> - `move_to_reconciliation`
> - `move_to_receipts`
> - `move_to_assets`
> - `move_to_archive`
> - `merge_with_existing_domain_file`
> - `needs_human_review`
> 
> ## What Belongs in QiEOS
> 
> Keep in `00_QiEOS` only if the file is genuinely system-wide and constitutional.
> 
> Examples that likely belong in QiEOS:
> 
> - principles
> - rules
> - standards
> - policies
> - ADRs
> - doctrine
> - master system map
> - domain registry
> - band registry
> - namespace registry
> - naming rules
> - metadata rules
> - repo rules
> - source-of-truth rules
> - placement rules
> - lifecycle rules
> - deprecation rules
> - sensitivity classification
> - cross-domain object model
> - cross-domain schema model
> 
> ## What Does Not Belong in QiEOS
> 
> Move or propose moving files that are operational, app-specific, server-specific, or implementation-specific.
> 
> Examples:
> 
> ### QiServer domain
> 
> Files about:
> 
> - Cloudflare tunnels
> - Docker Compose
> - Portainer
> - Cockpit
> - Tailscale
> - Uptime Kuma
> - runtime profiles
> - server runbooks
> - server service maps
> 
> Likely destination:
> 
> `30_QiServer`
> 
> ### QiAccess domain
> 
> Files about:
> 
> - QiAccess Start
> - QiAccess homepage
> - QiAccess command menu
> - QiAccess QA/testing
> - QiAccess blueprint
> - QiAccess publishing plan
> 
> Likely destination:
> 
> `10_QiAccess` or `60_QiApps\qiaccess_start`, depending on whether QiAccess remains its own domain or app module.
> 
> ### QiCapture domain
> 
> Files about:
> 
> - Paperless
> - NocoDB capture
> - Obsidian capture
> - document ingestion
> - intake pipeline
> - capture workflows
> 
> Likely destination:
> 
> `40_QiCapture`
> 
> ### QiNexus domain
> 
> Files about:
> 
> - storage
> - My Drive model
> - app-managed storage
> - document vault
> - Wiki.js if used as knowledge/document surface
> - storage freeze policy if domain-specific
> 
> Likely destination:
> 
> `50_QiNexus`
> 
> ### QiSystem domain
> 
> Files about:
> 
> - QiLife data spine
> - system modules
> - AI layer
> - prompts
> - deployment
> - source-of-truth rules
> - data dependencies
> - module contracts
> - implementation blueprint
> 
> Likely destination:
> 
> `20_QiSystem`
> 
> ### QiApps domain
> 
> Files about:
> 
> - QiLife
> - QiJourney
> - CareLite
> - qinote
> - app-specific UI flows
> - app-specific context docks
> - app-specific AI behaviors
> 
> Likely destination:
> 
> `60_QiApps`
> 
> ### QiConnect domain
> 
> Files about:
> 
> - integrations
> - external integrations
> - APIs
> - workflows
> - n8n
> - automation backlog
> - QiIngest pipeline
> - external service connection patterns
> 
> Likely destination:
> 
> `70_QiConnect`
> 
> ### Reconciliation
> 
> Files about:
> 
> - audits
> - gap reports
> - migration plans
> - implementation reconciliation
> - site coverage
> - blueprint readiness
> - Codex reconciliation
> 
> Likely destination:
> 
> `Reconciliation`
> 
> ### Receipts
> 
> Files about:
> 
> - generated reports
> - logs
> - validation reports
> - health checks
> - structure checks
> - changelog
> - generated indexes
> 
> Likely destination:
> 
> root-level `90_receipts` if created, or existing receipts location after audit.
> 
> ### Assets
> 
> Files about:
> 
> - diagrams
> - images
> - Markmind exports
> - templates
> - icons
> - visual maps
> 
> Likely destination:
> 
> root-level `assets` or proposed `70_assets`.
> 
> ### Archive
> 
> Files that are:
> 
> - superseded
> - legacy
> - old blueprints
> - previous README copies
> - obsolete protocols
> - historical extracts
> 
> Likely destination:
> 
> `90_archive` or `Reconciliation\archive_candidates`.
> 
> ## Specific `00_QiEOS` Folders To Audit
> 
> Audit these carefully:
> 
> ### `00_QiEOS\30_service_map`
> 
> This folder appears to contain many domain-specific service docs that probably should not live under QiEOS.
> 
> Classify each subfolder:
> 
> - `10_infrastructure` likely belongs to `30_QiServer`
> - `20_ai_compute` may belong to `20_QiSystem` or `30_QiServer`
> - `30_capture` likely belongs to `40_QiCapture`
> - `40_productivity` may belong to QiApps, QiSystem, or QiConnect depending on content
> - `50_apis` likely belongs to `70_QiConnect` or `20_QiSystem`
> - `60_workers` likely belongs to `20_QiSystem` or `70_QiConnect`
> - `70_pipelines` likely belongs to `40_QiCapture`, `20_QiSystem`, or `70_QiConnect`
> - `80_tools` likely belongs to `20_QiSystem` or operations
> - `90_interfaces` likely belongs to QiAccess/QiApps/QiConnect depending on content
> - `100_integrations` likely belongs to `70_QiConnect`
> - `110_qiserver` belongs to `30_QiServer`
> - `120_applications` belongs to `60_QiApps`
> - `130_GINA` needs review
> 
> ### `00_QiEOS\40_operations`
> 
> This likely contains mixed operations history.
> 
> Classify:
> 
> - qiserver runbooks -> `30_QiServer`
> - QiAccess server runbook -> either `10_QiAccess` or `30_QiServer`
> - dev history -> `Reconciliation` or `90_receipts`
> - dev testing -> relevant app/domain folder or `Reconciliation`
> - access/exposure rules -> governance/security if system-wide; otherwise QiAccess/QiConnect
> 
> ### `00_QiEOS\50_knowledge`
> 
> This appears to include glossary, migration notes, legacy salvage, and superseded sources.
> 
> Classify:
> 
> - glossary may stay in doctrine/knowledge if system-wide
> - migration notes -> `Reconciliation`
> - legacy CSV migration plan -> `Reconciliation` or archive
> - legacy salvage -> archive
> - QiAccess legacy quarantine -> QiAccess archive
> - repo sync status -> receipts/reconciliation
> - superseded sources -> archive
> 
> ### `00_QiEOS\60_assets`
> 
> Assets should probably not be inside QiEOS unless they are QiEOS-only assets.
> 
> Classify:
> 
> - diagrams -> root assets or architecture diagrams
> - images -> root assets
> - templates -> governance/templates or root templates depending on type
> - ADR template -> governance/decisions/templates
> - operational template -> operations/templates
> - registry template -> architecture/registry/templates
> 
> ### `00_QiEOS\90_receipts`
> 
> Receipts should not be nested under QiEOS unless they are QiEOS-only receipts.
> 
> Move/propose moving to root receipts:
> 
> `90_receipts`
> 
> Generated reports must not be mixed with source doctrine.
> 
> ### `00_QiEOS\reconciliation`
> 
> Move/propose moving into root `Reconciliation`.
> 
> ### `00_QiEOS\doctrine`
> 
> Likely keep in QiEOS or move to root doctrine, depending on chosen final topology.
> 
> ### `00_QiEOS\system_map`
> 
> Likely keep in QiEOS if it is a master map. If it is implementation-specific, move to architecture.
> 
> ## Migration Map Requirements
> 
> For each file currently under `00_QiEOS`, produce one row in:
> 
> `qieos_domain_migration_map.csv`
> 
> Columns:
> 
> - current_path
> - filename
> - inferred_domain
> - current_category
> - proposed_action
> - proposed_destination
> - reason
> - confidence
> - duplicate_candidates
> - reference_risk
> - needs_human_review
> - notes
> 
> Allowed proposed actions:
> 
> - keep
> - move
> - copy
> - merge
> - archive
> - rename
> - review
> 
> ## Confidence Rules
> 
> Use confidence levels:
> 
> - `high`
> - `medium`
> - `low`
> 
> High confidence examples:
> 
> - `00_QiEOS\30_service_map\110_qiserver\runtime.md` -> `30_QiServer`
> - `00_QiEOS\30_service_map\30_capture\paperless` -> `40_QiCapture`
> - `00_QiEOS\reconciliation\...` -> `Reconciliation`
> - `00_QiEOS\90_receipts\50_generated_reports\...` -> root receipts/generated reports
> 
> Medium confidence examples:
> 
> - AI compute docs may be QiSystem or QiServer depending on whether they describe capability or runtime
> - API docs may be QiSystem or QiConnect depending on whether internal or external
> - interface docs may be QiAccess, QiApps, or QiConnect depending on content
> 
> Low confidence examples:
> 
> - generic README files
> - `_index.md`
> - files with ambiguous names
> - files whose destination depends on content
> - files referenced by build/navigation config
> 
> ## Reference Checking
> 
> Before recommending moves, search for references to each file in:
> 
> - `docs.json`
> - `file-index.json`
> - `README.md`
> - `index.md`
> - `build.js`
> - markdown links
> - MDX imports
> - site navigation files
> 
> If references exist, mark `reference_risk=true` and include references in the report.
> 
> Do not update references yet unless explicitly asked.
> 
> ## Final Output Summary
> 
> In `qieos_keep_vs_move_report.md`, include:
> 
> 1. Number of files scanned under `00_QiEOS`
> 2. Files that should stay in QiEOS
> 3. Files that clearly belong in another domain
> 4. Files that are ambiguous
> 5. Duplicate or overlapping files found outside QiEOS
> 6. Recommended new domain destinations
> 7. Safe first moves
> 8. Moves requiring human review
> 9. Proposed final meaning of `00_QiEOS`
> 
> ## Final Meaning of QiEOS
> 
> Propose a clean definition for `00_QiEOS`.
> 
> Suggested definition:
> 
> `00_QiEOS` is the constitutional layer of QiOS DNA. It defines the system-wide doctrine, governance, registries, naming rules, lifecycle rules, and architectural decisions that other domains must follow. It does not own app docs, server runbooks, service implementation details, generated reports, or legacy project debris.
> 
> Use that definition to decide what stays and what moves.
> 
> ## Do Not Do Yet
> 
> Do not actually move files until the reports are created.
> 
> Do not delete files.
> 
> Do not rename files.
> 
> Do not edit links.
> 
> Do not consolidate duplicates.
> 
> This pass is for classification, migration planning, and safe domain placement only.
> :::
> 
> ## The better model
> 
> Your root domains are already trying to exist:
> 
> ```text
> 00_QiEOS      = constitutional/governance layer
> 10_QiAccess   = access/front-door/interface layer
> 20_QiSystem   = system/application logic layer
> 30_QiServer   = runtime/server/infrastructure layer
> 40_QiCapture  = ingestion/capture layer
> 50_QiNexus    = storage/knowledge/document vault layer
> 60_QiApps     = product/app layer
> 70_QiConnect  = integrations/workflows/API connection layer
> ```
> 
> So the cleanup should **not** just create generic folders like `50_services` unless you’re intentionally replacing the domain model.
> 
> The sharper move is:
> 
> > **Use the existing Qi domains as the destination map.**
> 
> That means:
> 
> - Don’t move `cloudflare.md` to generic `services`; move it to `30_QiServer`.
> - Don’t move `paperless` to generic `capture_services`; move it to `40_QiCapture`.
> - Don’t move `external_integrations.md` to generic `services`; move it to `70_QiConnect`.
> - Don’t leave `QiAccess_Start_Blueprint.md` in QiEOS; move or merge it into `10_QiAccess` / `60_QiApps/qiaccess_start`.
> - Don’t leave generated reports under QiEOS unless they are specifically QiEOS audit receipts.
> 
> ## Clean rule
> 
> Use this as the sorting law:
> 
> > **If the file defines the rules, it stays in QiEOS.  
> > If the file describes a working thing, it belongs to the domain that owns that thing.**
> 
> That one sentence will save you from another folder swamp.
