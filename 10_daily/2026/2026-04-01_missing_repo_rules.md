---
layout: page
title: "Missing Repo Rules"
slug: "missing_repo_rules"
created_at: "2026-04-01 16:34:18"
updated_at: "2026-07-16T06:49:30-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-005.json"
template_key: master-template
date: 2026-04-01
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69cd8f54-e110-8333-83de-719c45e8488a"
canonical_ref: ""
---

# Missing Repo Rules

## Overview
- **Date**: 2026-04-01 16:34:18
- **Conversation ID**: `69cd8f54-e110-8333-83de-719c45e8488a`
- **Source**: `Chat-Export-28513-2026/conversations-005.json`

## Chat History

### User
> what rules are we missing here. rules:

>   - id: RR-001

>     name: Single Source of Truth

>     description: This repo is the single canonical source of truth for architecture.

> 

>   - id: RR-002

>     name: YAML Constraints

>     description: Machine-readable constraints must go in standards/ or registry/.

### Assistant
> I’m checking the blueprint against your two repo rules and pulling the missing rule classes, not just paraphrasing the obvious stuff. Then I’ll turn it into a clean add list you can drop straight into `repo_rules.yaml` or equivalent.

### Assistant
> You’re missing **both some repo-specific rules** and **a bunch of doctrine that should *not* live in `repo_rules.yaml`**.
> 
> ## What belongs in `repo_rules.yaml`
> 
> Your current two are fine, but too thin.
> 
> ### Add these as repo-level rules
> 
> ```yaml
> rules:
>   - id: RR-001
>     name: Blueprint Canonical Authority
>     description: This repo is the sole canonical home for QiOS constitutional doctrine, structure law, architecture law, schema/data/object law, operational map, and decision history.
> 
>   - id: RR-002
>     name: Machine-Readable Constraint Placement
>     description: Machine-readable constraints must live in standards/ or registry/; they must not be embedded only in prose docs.
> 
>   - id: RR-003
>     name: Canonical Repo Topology
>     description: Repos must follow the canonical topology. Approved root directories are /apps, /sites, /python/qiarchive, /workers, /packages, /infra, and /data.
> 
>   - id: RR-004
>     name: No Undocumented Root Directories
>     description: No undocumented root directory may be added without documentation and an ADR when required.
> 
>   - id: RR-005
>     name: Migration Required for Schema Changes
>     description: Every schema change must ship with a migration file and be applied through Supabase migration tooling.
> 
>   - id: RR-006
>     name: ADR Before Structural Change
>     description: Changes affecting namespace, schema, topology, runtime boundaries, delivery surfaces, or identity rules require an ADR before merge.
> 
>   - id: RR-007
>     name: Drift Must Be Flagged
>     description: Drift between formal architecture and implemented code must be identified and resolved; implementation may not silently diverge from doctrine.
> 
>   - id: RR-008
>     name: No Parallel Root Structures
>     description: New root structures must not be introduced when an approved canonical location already exists.
> 
>   - id: RR-009
>     name: Build Steps Must Be Documented
>     description: All build-critical setup, bootstrap, and execution steps must be documented in the canonical docs.
> 
>   - id: RR-010
>     name: Clarity Over Cleverness
>     description: Repository structure and naming must optimize for legibility, operational ownership, and maintainability over clever abstractions.
> ```
> 
> That set is the actual missing core if this file is supposed to govern the repo itself. The blueprint explicitly says the repo has a canonical topology, forbids undocumented root dirs, requires migrations for schema changes, and requires ADRs for namespace/schema/topology changes. It also says drift must be flagged and resolved, new root structures should be avoided without documentation, and build steps should be documented. fileciteturn2file0 fileciteturn2file1
> 
> ---
> 
> ## What you are probably tempted to put here, but should not
> 
> These are real rules in the blueprint, but they belong elsewhere:
> 
> ### `naming_rules.yaml`
> - max structural depth = 3
> - no sibling labels with semantic overlap
> - artifact filename contract
> - `.000/.010/.020` bucket behavior
> - no new top-level band without registry entry  
> fileciteturn2file0
> 
> ### `metadata_rules.yaml`
> - automation gate fields:
>   - canonical_id
>   - domain_prefix
>   - short_code
>   - source_path
>   - ingest_timestamp
>   - mime_type
>   - status  
> fileciteturn2file1
> 
> ### `schema` / domain / registry rules
> - one schema per domain
> - no domain logic in `public`
> - new domains require ADR
> - every new schema must be declared in `registry/band_registry.yaml`
> - domain tables require `tenant_id` and RLS  
> fileciteturn2file1 fileciteturn2file2
> 
> ### `pipeline` / `worker` / `api` rules
> - no frontend or integration API writes directly to `qiarchive`
> - workers always operate on canonical IDs
> - failures must be visible, stateful, retryable
> - integrations cannot bypass the registration pipeline  
> fileciteturn2file1 fileciteturn2file2
> 
> ---
> 
> ## The blunt read
> 
> Right now your file is basically saying:
> 
> - this repo matters
> - YAML goes in the right folders
> 
> That is nowhere near enough.
> 
> You are missing the rules that stop the repo from turning into the exact kind of drift machine the blueprint was written to prevent:
> - rogue roots
> - undocumented topology
> - schema edits with no migrations
> - implementation drifting from doctrine
> - structural changes with no ADR
> - duplicated structural homes
> 
> ## Best next move
> 
> Split it cleanly:
> 
> - keep `repo_rules.yaml` for **repo topology and contribution law**
> - keep `naming_rules.yaml` for **namespace/file/folder syntax**
> - keep `metadata_rules.yaml` for **automation gate + object minimums**
> - keep registry YAMLs for **band/domain/subdomain ownership**
> - keep ADR requirement explicit in repo rules
> 
> If you want, I’ll turn this into a **final locked `repo_rules.yaml` patch** in your exact house style.

### User
> now do these rules go into .agent/rules, then the rest inside standars and registery or is that separate.

### Assistant
> I’m separating three layers here: agent behavior, canonical doctrine, and machine-readable registries. The main trap is mixing “how assistants should behave” with “what the system is.”

### Assistant
> Yes — **separate**.
> 
> ## The clean split
> 
> ### 1. `standards/` and `registry/` = canonical source
> That is where the **real machine-readable truth** belongs. The blueprint is explicit: current governing truth lives in `docs/`, machine-readable constraints and standards go in `standards/` as YAML, canonical namespaces and tables go in `registry/` as YAML, and ADR history goes in `adr/`. fileciteturn4file0
> 
> So:
> 
> - `docs/` → prose doctrine, explanation, architecture law
> - `standards/` → enforceable technical rules
> - `registry/` → canonical maps of domains, bands, subdomains, prefixes
> - `adr/` → why structural decisions were made
> 
> ### 2. `.agent/rules/` = derived working layer for agents
> That should be a **consumer layer**, not the source of truth.
> 
> Use `.agent/rules/` for:
> - distilled agent instructions
> - implementation guardrails for Codex / IDE agents
> - “how to operate inside this repo without being stupid” summaries
> - checklists and execution prompts derived from the blueprint
> 
> Do **not** make `.agent/rules/` the place where canonical standards live, or you’ll create drift immediately. The blueprint already warns against silent duplication and says drift between formal architecture and implemented code must be flagged and resolved. fileciteturn4file1
> 
> ## The rule of thumb
> 
> If a rule is:
> 
> ### Canonical and machine-enforceable
> put it in `standards/`
> 
> Examples:
> - `repo_rules.yaml`
> - `naming_rules.yaml`
> - `metadata_rules.yaml`
> 
> The blueprint literally points to those as the machine-readable versions. fileciteturn4file1turn4file2
> 
> ### Canonical ownership / namespace / schema map
> put it in `registry/`
> 
> Examples:
> - `band_registry.yaml`
> - `domain_registry.yaml`
> - `subdomain_registry.yaml`
> - prefix registry YAML
> 
> The blueprint defines registry as the canonical namespace and domain ownership map. fileciteturn4file1
> 
> ### Decision logic / exceptions / structure changes
> put it in `adr/`
> 
> Because ADRs are required for changes affecting namespace, schema, topology, runtime boundaries, delivery surfaces, and identity rules. fileciteturn4file1
> 
> ### Agent behavior / shorthand / repo-operating instructions
> put it in `.agent/rules/`
> 
> But make it **derived from** the above, not independent.
> 
> ---
> 
> ## My recommendation
> 
> Do this:
> 
> ```text
> _qios_master_blueprint/
>   docs/
>   standards/
>     repo_rules.yaml
>     naming_rules.yaml
>     metadata_rules.yaml
>   registry/
>     band_registry.yaml
>     domain_registry.yaml
>     subdomain_registry.yaml
>     prefix_registry.yaml
>   adr/
> 
> _QiOne_MonoRepo/
>   .agent/
>     rules/
>       00_source_of_truth.md
>       10_repo_topology.md
>       20_naming_contract.md
>       30_metadata_gate.md
>       40_adr_triggers.md
> ```
> 
> ## Important constraint
> 
> Do **not** hand-maintain the same rule in both places.
> 
> That is how you get:
> - blueprint says one thing
> - agent rules say another
> - code does a third thing
> 
> Bad system. Waste of time.
> 
> ## Best practice
> 
> Make `.agent/rules/` a **compiled summary layer**:
> - short
> - operational
> - references canonical file paths
> - no independent doctrine
> 
> Example:
> 
> ```md
> Source of truth:
> - standards/repo_rules.yaml
> - standards/naming_rules.yaml
> - standards/metadata_rules.yaml
> - registry/domain_registry.yaml
> - adr/
> 
> If conflict exists, ignore this file and follow canonical source.
> ```
> 
> That is the right architecture.
> 
> ## Bottom line
> 
> - **Yes:** put canonical rules in `standards/` and `registry/`
> - **Yes:** use `.agent/rules/` separately for agent-facing distilled guidance
> - **No:** do not split canonical authority between them
> - **No:** do not let `.agent/rules/` become shadow governance
> 
> If you want, I’ll give you the exact starter tree and first 5 `.agent/rules/*.md` files next.

### User
> {'asset_pointer': 'sediment://file_000000008b2471fba907c74194ebbd6c', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 930, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 45387, 'width': 360}so should my master blueprint actually just be inside docs/*
> 
> ```markdown

> . 📂 _qios_master_blueprint

> └── 📂 00_genesis/

> └── 📂 01_governance/

> │  ├── 📄 agent_rules.md

> │  ├── 📄 decisions.md

> │  ├── 📄 index.md

> │  ├── 📄 policies.md

> │  ├── 📄 principles.md

> │  ├── 📄 registry.md

> │  ├── 📄 standards.md

> └── 📂 02_architecture/

> │  ├── 📄 component_map.md

> │  ├── 📄 data_flow.md

> │  ├── 📄 device_model.md

> │  ├── 📄 identity.md

> │  ├── 📄 index.md

> │  ├── 📄 runtime_zones.md

> │  ├── 📄 service_boundaries.md

> │  ├── 📄 system_model.md

> └── 📂 03_structure/

> │  ├── 📄 bands.md

> │  ├── 📄 directory_tree.md

> │  ├── 📄 domains.md

> │  ├── 📄 index.md

> │  ├── 📄 namespace_registry.md

> │  ├── 📄 object_model.md

> │  ├── 📄 placement_rules.md

> │  ├── 📄 subdomains.md

> └── 📂 04_data/

> │  ├── 📄 exports.md

> │  ├── 📄 index.md

> │  ├── 📄 metadata.md

> │  ├── 📄 objects.md

> │  ├── 📄 qievidence.md

> │  ├── 📄 schema.md

> │  ├── 📄 storage.md

> └── 📂 05_compute/

> │  ├── 📄 apis.md

> │  ├── 📄 index.md

> │  ├── 📄 integrations.md

> │  ├── 📄 pipelines.md

> │  ├── 📄 runtime.md

> │  ├── 📄 tech_stack.md

> │  ├── 📄 workers.md

> └── 📂 06_applications/

> │  └── 📂 01_web/

> │  ├── 📄 admin.md

> │  ├── 📄 index.md

> │  ├── 📄 interfaces.md

> │  ├── 📄 portal.md

> │  ├── 📄 tools.md

> │  ├── 📄 web.md

> └── 📂 07_operations/

> │  ├── 📄 cases.md

> │  ├── 📄 clients.md

> │  ├── 📄 finance.md

> │  ├── 📄 index.md

> │  ├── 📄 products.md

> │  ├── 📄 templates.md

> └── 📂 adr/

> │  ├── 📄 ADR-0000_template.md

> │  ├── 📄 ADR-0001-blueprint-scope.md

> │  ├── 📄 ADR-0001_blueprint_scope.md

> │  ├── 📄 ADR-0002-single-domain-rule.md

> │  ├── 📄 ADR-0002_single_domain_rule.md

> │  ├── 📄 ADR-0003-band-model.md

> │  ├── 📄 ADR-0003_band_model.md

> │  ├── 📄 ADR-0004-qilabs-root.md

> │  ├── 📄 ADR-0004_qilabs_root.md

> │  ├── 📄 ADR-0005-hosted-fleet-orchestration.md

> │  ├── 📄 ADR-0005_fleet_orchestration.md

> │  ├── 📄 ADR-0006_narrative_and_knowledge_consolidation.md

> │  ├── 📄 update-adr.md

> └── 📂 appendices/

> │  ├── 📄 changelog.md

> │  ├── 📄 glossary.md

> │  ├── 📄 legacy_csv_inventory.json

> │  ├── 📄 legacy_csv_migration_plan.md

> │  ├── 📄 legacy_salvage.md

> │  ├── 📄 migration_notes.md

> └── 📂 assets/

> │  ├── 📄 _QiOS_Master_Document.jpg

> │  └── 📂 diagrams/

> │  └── 📂 tables/

> ├── 📄 index.md

> └── 📂 logs/

> ├── 📄 main.py

> ├── 📄 markmind.html

> ├── 📄 mkdocs.yml

> └── 📂 overrides/

> │  ├── 📄 home.html

> └── 📂 registry/

> │  ├── 📄 band_registry.yaml

> │  ├── 📄 deprecation_registry.yaml

> │  ├── 📄 domain_registry.yaml

> │  ├── 📄 folder_registry.yaml

> │  ├── 📄 qios_04_rules_and_readmes.canvas.canvas

> │  ├── 📄 qios_05_Cursor_and_naming.canvas

> │  ├── 📄 realms_registry.yaml

> │  ├── 📄 sensitivity_classification.yaml

> │  ├── 📄 subdomain_registry.yaml

> │  ├── 📄 workspace_realms.yaml

> └── 📂 schemas/

> │  ├── 📄 band_registry.schema.json

> │  ├── 📄 qievidence.sql

> └── 📂 scripts/

> │  ├── 📄 enforce_structure.py

> └── 📂 standards/

> │  ├── 📄 content_metadata_profile.yaml

> │  ├── 📄 metadata_rules.yaml

> │  ├── 📄 naming_rules.yaml

> │  ├── 📄 pdf_standards.yaml

> │  ├── 📄 repo_rules.yaml

> └── 📂 stylesheets/

> │  ├── 📄 extra.css

> └── 📂 templates/

> │  ├── 📄 README.md

> │  ├── 📄 artifact_template.md

> │  └── 📄 note_template.md

> ```
> 
> so lets do a quick alignment with the new subfolders etc.

### Assistant
> No. **The blueprint pages go in `docs/`. The blueprint system does not.**
> 
> That is the clean distinction.
> 
> # What lives in `docs/`
> 
> Anything that is **published prose / MkDocs content**:
> 
> - `index.md`
> - `00_genesis/`
> - `01_governance/`
> - `02_architecture/`
> - `03_structure/`
> - `04_data/`
> - `05_compute/`
> - `06_applications/`
> - `07_operations/`
> - appendices that should render on the site
> - doc images/diagrams used by the site
> 
> # What stays outside `docs/`
> 
> Anything that is **canonical machine-readable or support infrastructure**:
> 
> - `standards/`
> - `registry/`
> - `adr/`
> - `scripts/`
> - `schemas/` only if these are **schemas/specs**, not live runtime migrations
> - `mkdocs.yml`
> - `overrides/`
> - maybe `templates/` if these are repo assets, not published docs
> 
> ---
> 
> # So your answer is
> 
> ## **No, the master blueprint should not “just be inside docs.”**
> It should be:
> 
> - **`docs/` = rendered doctrine pages**
> - **top-level siblings = canonical rule files, registries, ADRs, tooling**
> 
> ---
> 
> # Best aligned structure for `_qios_master_blueprint`
> 
> This is the version I’d lock:
> 
> ```text
> _qios_master_blueprint/
> ├── README.md
> ├── mkdocs.yml
> ├── docs/
> │   ├── index.md
> │   ├── 00_genesis/
> │   ├── 01_governance/
> │   │   ├── index.md
> │   │   ├── principles.md
> │   │   ├── policies.md
> │   │   ├── standards.md
> │   │   ├── registry.md
> │   │   ├── decisions.md
> │   │   └── agent_rules.md
> │   ├── 02_architecture/
> │   ├── 03_structure/
> │   ├── 04_data/
> │   ├── 05_compute/
> │   ├── 06_applications/
> │   │   ├── index.md
> │   │   ├── web.md
> │   │   ├── portal.md
> │   │   ├── admin.md
> │   │   ├── tools.md
> │   │   └── interfaces.md
> │   ├── 07_operations/
> │   ├── 08_appendices/
> │   │   ├── changelog.md
> │   │   ├── glossary.md
> │   │   ├── migration_notes.md
> │   │   ├── legacy_csv_migration_plan.md
> │   │   └── legacy_salvage.md
> │   └── assets/
> │       ├── images/
> │       ├── diagrams/
> │       └── tables/
> ├── adr/
> │   ├── ADR-0000-template.md
> │   ├── ADR-0001-blueprint-scope.md
> │   ├── ADR-0002-single-domain-rule.md
> │   ├── ADR-0003-band-model.md
> │   ├── ADR-0004-qilabs-root.md
> │   ├── ADR-0005-hosted-fleet-orchestration.md
> │   └── ADR-0006-narrative-and-knowledge-consolidation.md
> ├── standards/
> │   ├── repo_rules.yaml
> │   ├── naming_rules.yaml
> │   ├── metadata_rules.yaml
> │   ├── pdf_standards.yaml
> │   └── content_metadata_profile.yaml
> ├── registry/
> │   ├── band_registry.yaml
> │   ├── domain_registry.yaml
> │   ├── subdomain_registry.yaml
> │   ├── folder_registry.yaml
> │   ├── deprecation_registry.yaml
> │   ├── realms_registry.yaml
> │   ├── workspace_realms.yaml
> │   └── sensitivity_classification.yaml
> ├── schemas/
> │   └── band_registry.schema.json
> ├── scripts/
> │   └── enforce_structure.py
> ├── overrides/
> │   └── home.html
> ├── templates/
> │   ├── README.md
> │   ├── artifact_template.md
> │   └── note_template.md
> └── stylesheets/
>     └── extra.css
> ```
> 
> ---
> 
> # Quick alignment fixes from your draft
> 
> ## 1. `06_applications/01_web/` is messy
> Right now it implies everything under applications is “web,” which is not true.
> 
> Use this instead:
> 
> - `docs/06_applications/web.md`
> - `docs/06_applications/portal.md`
> - `docs/06_applications/admin.md`
> - `docs/06_applications/tools.md`
> - `docs/06_applications/interfaces.md`
> 
> No `01_web/` folder needed unless you are doing a deeper multi-surface breakdown.
> 
> ---
> 
> ## 2. Kill duplicate ADR filenames
> You have both:
> 
> - `ADR-0001-blueprint-scope.md`
> - `ADR-0001_blueprint_scope.md`
> 
> That is garbage drift. Pick one format and delete the duplicate set.
> 
> Use:
> 
> - `ADR-0001-blueprint-scope.md`
> - `ADR-0002-single-domain-rule.md`
> - etc.
> 
> Hyphenated is cleaner.
> 
> ---
> 
> ## 3. `registry/` should not contain canvas junk
> These do **not** belong in `registry/`:
> 
> - `qios_04_rules_and_readmes.canvas.canvas`
> - `qios_05_Cursor_and_naming.canvas`
> 
> Registry should be **machine-readable canonical maps**, not visual scratch files.
> 
> Move those to something like:
> 
> - `docs/assets/diagrams/`
> - or `_working/`
> - or `appendices/visuals/`
> 
> But not `registry/`.
> 
> ---
> 
> ## 4. Be careful with `schemas/qievidence.sql`
> If that SQL is intended to be a **real executable schema authority**, it should **not** live in the blueprint as canonical truth.
> 
> Put live schema authority in the monorepo:
> - `supabase/migrations/...`
> 
> Blueprint can describe schema rules and maybe keep:
> - JSON schemas
> - interface contracts
> - example DDL
> - non-authoritative reference specs
> 
> But not a second competing source of truth for runtime SQL.
> 
> ---
> 
> ## 5. `main.py`, `markmind.html`, `logs/` probably do not belong here
> Unless they are explicitly part of the blueprint tooling, they are noise.
> 
> My blunt read:
> - `main.py` → move out
> - `markmind.html` → move out
> - `logs/` → move out or ignore
> - `nul` → delete immediately
> 
> That stuff muddies the constitutional repo.
> 
> ---
> 
> ## 6. `assets/` should probably be under `docs/`
> If the assets are for the MkDocs site, put them in:
> 
> - `docs/assets/images/`
> - `docs/assets/diagrams/`
> - `docs/assets/tables/`
> 
> That avoids weird relative path nonsense.
> 
> ---
> 
> # Where `.agent/rules` fits
> 
> Not inside the blueprint as canonical law.
> 
> Use:
> 
> ```text
> _QiOne_MonoRepo/.agent/rules/
> ```
> 
> Those files should be **derived operating instructions** for agents.
> 
> The blueprint may still have a prose page like:
> 
> - `docs/01_governance/agent_rules.md`
> 
> But that page is doctrine/explanation.
> The actual `.agent/rules/*` files are execution-facing summaries.
> 
> ---
> 
> # What I would do in your exact setup
> 
> Since `_qios_master_blueprint` is currently a folder inside the monorepo root, do this:
> 
> ## Keep:
> - `_qios_master_blueprint/docs/`
> - `_qios_master_blueprint/standards/`
> - `_qios_master_blueprint/registry/`
> - `_qios_master_blueprint/adr/`
> 
> ## Add:
> - `_QiOne_MonoRepo/.agent/rules/`
> 
> ## Avoid:
> - duplicating blueprint content again in root `/docs`
> 
> So either:
> - root `/docs` is for monorepo implementation docs only, **or**
> - delete/retire that root `/docs` if it is redundant
> 
> Because having:
> - monorepo `/docs`
> - blueprint `/docs`
> 
> without a hard boundary is a drift trap.
> 
> ---
> 
> # Clean decision
> 
> ## Use this rule:
> **Blueprint doctrine renders from `_qios_master_blueprint/docs/`.**
> **Canonical machine-readable law stays beside it, not inside it.**
> **Agent rules live in monorepo `.agent/rules/` as a derived layer.**
> 
> That’s the right architecture.
> 
> If you want, next I’ll give you the **exact moved/renamed folder map** from your current draft to the cleaned final structure.

### User
> ok so the root docs is redundant but there is a docs\integartion\qione portal endpoint manifest.json, what do i do wtiht aht.

### Assistant
> That file is **not blueprint doctrine**. So do **not** shove it into `_qios_master_blueprint/docs/`.
> 
> ## What it probably is
> 
> `docs/integration/qione portal endpoint manifest.json` sounds like one of these:
> 
> 1. **runtime integration artifact**  
>    actual endpoint contract / manifest consumed by code or tooling
> 
> 2. **implementation documentation asset**  
>    example manifest referenced by implementation docs
> 
> 3. **draft junk in the wrong folder**  
>    common enough
> 
> ## The rule
> 
> ### If the JSON is used by code, tooling, tests, deploy, or integration setup:
> move it **out of docs entirely**.
> 
> Best targets:
> 
> - `apps/qione/config/endpoint-manifest.json`
> - `packages/contracts/qione-portal-endpoint-manifest.json`
> - `infra/contracts/qione-portal-endpoint-manifest.json`
> - `data/manifests/qione-portal-endpoint-manifest.json`
> 
> Pick based on ownership:
> 
> - **app-owned contract** → `apps/qione/...`
> - **shared contract** → `packages/contracts/...`
> - **deployment/integration infra** → `infra/...`
> - **data artifact / export / manifest store** → `data/manifests/...`
> 
> ### If the JSON is just an example for humans:
> keep a **doc page** in docs, but move the actual JSON to a cleaner support location.
> 
> Example:
> 
> - doc page: `docs/integrations/qione-portal-endpoints.md`
> - source example: `templates/qione-portal-endpoint-manifest.example.json`
> 
> ### If it is canonical interface spec:
> it belongs in a **contracts/specs area**, not `docs/`.
> 
> Best option:
> - `packages/contracts/qione-portal-endpoint-manifest.json`
> 
> ---
> 
> # What I would do here
> 
> Based on the filename, I would **not** keep it under root `docs/`.
> 
> I would move it to:
> 
> ```text
> packages/contracts/qione-portal-endpoint-manifest.json
> ```
> 
> Then create a short doc page wherever implementation docs live that says:
> 
> - what it is
> - who owns it
> - whether it is example or canonical
> - what consumes it
> 
> ---
> 
> # Your bigger cleanup rule
> 
> ## Root `/docs` should only survive if it becomes:
> **monorepo implementation docs**, not blueprint docs.
> 
> So you have two choices:
> 
> ### Option A — kill root `/docs`
> Do this if it only has random leftovers.
> 
> Move useful files out:
> - implementation contracts → `packages/contracts/` or `infra/`
> - examples → `templates/`
> - architecture doctrine → `_qios_master_blueprint/docs/`
> 
> ### Option B — repurpose root `/docs`
> Keep it, but rename the purpose in your head:
> 
> - `_qios_master_blueprint/` = constitutional doctrine
> - `/docs` = implementation notes, integration docs, local developer docs
> 
> If you keep root `/docs`, it needs discipline. Otherwise it becomes the junk drawer.
> 
> ---
> 
> # My blunt recommendation
> 
> For **one stray manifest JSON**, do this:
> 
> ```text
> MOVE
> docs/integration/qione portal endpoint manifest.json
> 
> TO
> packages/contracts/qione-portal-endpoint-manifest.json
> ```
> 
> Also rename it. Spaces in a contract filename are sloppy.
> 
> Use:
> - `qione-portal-endpoint-manifest.json`
> 
> or if it is environment-specific:
> - `qione-portal-endpoints.manifest.json`
> 
> ---
> 
> # Simple decision filter
> 
> Ask this:
> 
> **Is this file doctrine, implementation doc, or executable/support artifact?**
> 
> - doctrine → `_qios_master_blueprint/docs/`
> - machine-readable law → `_qios_master_blueprint/standards/` or `registry/`
> - executable/support artifact → monorepo proper, not docs
> - human implementation notes → root `/docs` only if you intentionally keep `/docs` as implementation docs
> 
> If you want, I can give you a **full “what goes where” map** for every top-level folder in your current repo so you can stop second-guessing placement.

### User
> it looks like it is part of the home app for roommates.

### Assistant
> Then it definitely does **not** belong in blueprint docs, and probably not in root `/docs` either.
> 
> ## Put it with the app that owns it
> 
> If it is part of the roommate/home app, move it into the **QiHome/QiOne app area**.
> 
> Best fit depends on what it actually does:
> 
> ### If the app reads it at runtime
> Put it near the feature or in a public/config location.
> 
> Good options:
> 
> ```text
> apps/qione/src/features/qihome-hub/config/qione-portal-endpoint-manifest.json
> ```
> 
> or, if the browser needs to fetch it directly:
> 
> ```text
> apps/qione/public/manifests/qihome-roommate-endpoint-manifest.json
> ```
> 
> ### If it is just a developer reference/spec for that app
> Put it in app-local docs:
> 
> ```text
> apps/qione/docs/qihome-roommate-endpoint-manifest.md
> ```
> 
> and keep the JSON next to the feature:
> 
> ```text
> apps/qione/src/features/qihome-hub/contracts/qihome-roommate-endpoint-manifest.json
> ```
> 
> ## My recommendation
> 
> Since you said it looks like part of the home app for roommates, I would do this:
> 
> ```text
> apps/qione/src/features/qihome-hub/contracts/qihome-roommate-endpoint-manifest.json
> ```
> 
> If the frontend must fetch it directly in the browser, use:
> 
> ```text
> apps/qione/public/manifests/qihome-roommate-endpoint-manifest.json
> ```
> 
> ## Naming cleanup
> 
> Do **not** keep the old spaced name.
> 
> Rename:
> 
> ```text
> qione portal endpoint manifest.json
> ```
> 
> to something sane like:
> 
> ```text
> qihome-roommate-endpoint-manifest.json
> ```
> 
> or
> 
> ```text
> qihome-hub-endpoint-manifest.json
> ```
> 
> ## Simple rule
> 
> - blueprint docs = doctrine
> - root docs = implementation docs only, if intentionally kept
> - app-owned manifest = inside the app that uses it
> 
> So for this file: **move it into `apps/qione/...`**, not `_qios_master_blueprint/docs/`.
> 
> If you want, I’ll map the likely final home for the other stray top-level files in that screenshot too.

### User
> ok so back to the subfolders for blueprint docs, and we need to have templates for everything now so i dont have to think about it and we need to settle on teh front matter and metadata requirements becasue there are a few in here.

### Assistant
> Yes. Lock it now, because right now you have **multiple metadata patterns pretending to be normal**.
> 
> ## 1) Final blueprint docs subfolder structure
> 
> Use this and stop moving it around:
> 
> ```text
> _qios_master_blueprint/
> ├── docs/
> │   ├── index.md
> │   ├── 00_genesis/
> │   │   └── index.md
> │   ├── 01_governance/
> │   │   ├── index.md
> │   │   ├── principles.md
> │   │   ├── standards.md
> │   │   ├── policies.md
> │   │   ├── registry.md
> │   │   ├── decisions.md
> │   │   └── agent_rules.md
> │   ├── 02_architecture/
> │   ├── 03_structure/
> │   ├── 04_data/
> │   ├── 05_compute/
> │   ├── 06_applications/
> │   ├── 07_operations/
> │   ├── 08_appendices/
> │   └── assets/
> ├── adr/
> ├── standards/
> ├── registry/
> ├── schemas/
> ├── scripts/
> ├── templates/
> ├── overrides/
> ├── stylesheets/
> └── mkdocs.yml
> ```
> 
> Why: the blueprint already distinguishes between rendered doctrine in `docs/`, machine-readable constraints in `standards/` and `registry/`, and decision history in `adr/`. Your current MkDocs nav already follows the numbered doctrine sections plus separate ADR and template entries. fileciteturn7file0
> 
> ## 2) Where templates go
> 
> Do **not** scatter templates into every section.
> 
> Use one source location:
> 
> ```text
> templates/
>   adr_template.md
>   page_template.md
>   section_index_template.md
>   appendix_template.md
>   standard_template.md
>   registry_reference_template.md
>   operational_template.md
>   note_template.md
>   artifact_template.md
> ```
> 
> Then, if you want them visible in the site, either:
> - keep a `Templates` nav entry pointing at files in `templates/`, which you already do, or
> - add one `docs/08_appendices/templates_catalog.md` page that explains when to use each one. fileciteturn7file0turn6file2
> 
> ## 3) Settle the front matter problem with only **2 real profiles**
> 
> Do not make 8 different front matter dialects. That is drift bait.
> 
> ### Profile A — standard blueprint page
> Use for almost every doc page in `docs/`.
> 
> ```yaml
> ---
> title: ""
> document_type: "blueprint_page"
> status: "active"
> created_at: "YYYY-MM-DD"
> updated_at: "YYYY-MM-DD"
> owner: "cody"
> template_key: "page_template"
> summary: ""
> tags: []
> keywords: []
> classification: "business_internal"
> sensitivity: "internal"
> uid: ""
> ---
> ```
> 
> ### Profile B — ADR
> Use only in `adr/`.
> 
> ```yaml
> ---
> title: "ADR-0000: "
> document_type: "adr"
> status: "proposed"
> created_at: "YYYY-MM-DD"
> updated_at: "YYYY-MM-DD"
> author: ""
> adr_id: "ADR-0000"
> context_domain: ""
> supersedes: ""
> template_key: "adr_template"
> summary: ""
> tags: []
> classification: "business_internal"
> sensitivity: "internal"
> uid: ""
> ---
> ```
> 
> That’s it.
> 
> ## 4) What front matter is allowed to do
> 
> Front matter is **supportive metadata only**. It is not the system of record. The blueprint is explicit that canonical identity comes from QiArchive, placement comes from the pipeline, and front matter cannot change database relationships by itself. The existing content profile already frames front matter this way. fileciteturn6file0turn6file6
> 
> So for blueprint docs, front matter should help with:
> - rendering
> - filtering
> - search
> - classification
> - doc lifecycle
> 
> It should **not** pretend to issue identity, schema ownership, or routing truth. fileciteturn6file0turn7file0
> 
> ## 5) What metadata is actually required
> 
> The blueprint already settled the minimum automation gate. Before automation proceeds, these must exist:
> 
> - `canonical_id`
> - `domain_prefix`
> - `short_code`
> - `source_path`
> - `ingest_timestamp`
> - `mime_type`
> - `status` fileciteturn6file0turn7file0
> 
> And the full metadata model is already grouped into:
> - identity
> - source
> - structural
> - semantic
> - lifecycle metadata fileciteturn6file0turn6file5
> 
> So the move here is:
> 
> ### canonical/system metadata
> Lives in DB / pipeline / archive records.
> 
> ### supportive doc front matter
> Lives in markdown files.
> 
> Do not mix them.
> 
> ## 6) What to standardize in `content_metadata_profile.yaml`
> 
> Right now the content profile has useful supportive fields like `title`, `slug`, `aliases`, `tags`, `keywords`, `context`, `status`, `sensitivity`, `classification`, `summary`, and `realm_label`. That is the right lane for content metadata. fileciteturn6file6turn6file0
> 
> Add these missing doc-governance fields so the profile actually covers your blueprint pages cleanly:
> 
> ```yaml
> uid:
>   type: string
>   required: false
>   description: "Stable document-local identifier."
> 
> document_type:
>   type: string
>   required: false
>   description: "Doc class such as blueprint_page, adr, appendix, template."
> 
> template_key:
>   type: string
>   required: false
>   description: "Template used to create the page."
> 
> created_at:
>   type: string
>   required: false
>   description: "Document creation date."
> 
> updated_at:
>   type: string
>   required: false
>   description: "Last substantive update date."
> 
> owner:
>   type: string
>   required: false
>   description: "Maintainer or accountable owner."
> ```
> 
> ## 7) What to lock in `standards/metadata_rules.yaml`
> 
> This file needs to stop being a ghost. In the export, the prose metadata standard exists, but `standards/metadata_rules.yaml` is not carrying the locked machine-readable rule set yet. fileciteturn6file0turn6file6
> 
> Put this in it:
> 
> ```yaml
> standard: metadata_rules
> version: 1.0
> description: "Canonical machine-readable metadata requirements."
> 
> automation_gate:
>   required_fields:
>     - canonical_id
>     - domain_prefix
>     - short_code
>     - source_path
>     - ingest_timestamp
>     - mime_type
>     - status
> 
> metadata_classes:
>   identity:
>     - canonical_id
>     - domain_prefix
>     - short_code
>     - checksum
>   source:
>     - source_type
>     - source_path
>     - origin_event
>     - original_filename
>     - imported_by
>     - ingest_timestamp
>   structural:
>     - mime_type
>     - extension
>     - chunk_count
>     - page_count
>     - parser_method
>     - extraction_method
>   semantic:
>     - document_type
>     - inferred_entities
>     - tax_year
>     - matter_or_case
>     - tags
>     - confidence
>   lifecycle:
>     - status
>     - review_state
>     - route_state
>     - storage_path
>     - created_at
>     - updated_at
> 
> front_matter:
>   doctrine: "supportive_only"
>   allowed_profile: "content_front_matter"
>   forbidden_as_truth:
>     - canonical_identity
>     - schema_routing
>     - cross_domain_relationships
> ```
> 
> ## 8) The template set I would lock immediately
> 
> Create these now:
> 
> ```text
> templates/
>   page_template.md
>   section_index_template.md
>   adr_template.md
>   appendix_template.md
>   standard_template.md
>   registry_reference_template.md
>   operational_template.md
>   note_template.md
>   artifact_template.md
> ```
> 
> ### `page_template.md`
> For normal doctrine pages.
> 
> ### `section_index_template.md`
> For `index.md` inside each numbered section.
> 
> ### `adr_template.md`
> Replace the current ad hoc split and use one canonical ADR template. You already have the bones of this in `ADR-0000_template.md`. fileciteturn7file0turn6file4
> 
> ### `registry_reference_template.md`
> For docs that explain a registry file without becoming the registry.
> 
> ### `standard_template.md`
> For standards pages that point to machine-readable YAML.
> 
> ### `appendix_template.md`
> For salvage, migration notes, glossary, changelog, etc.
> 
> ## 9) My blunt call on the current mess
> 
> You currently have:
> - some pages with only `uid`
> - some with `template` and `title`
> - ADRs with a richer schema
> - a content metadata profile
> - a prose metadata doctrine
> - an apparently not-yet-locked machine-readable metadata rules file
> 
> That is exactly how systems turn into “I know what I meant” instead of “the repo enforces it.”
> 
> So the fix is simple:
> 
> ### lock this:
> - **2 front matter profiles**
> - **1 content profile**
> - **1 machine-readable metadata rules file**
> - **1 template source directory**
> - **1 consistent docs section tree**
> 
> That will stop the bleed.
> 
> ## 10) Final recommendation
> 
> Do this next, in order:
> 
> 1. lock the docs folder tree
> 2. create the 8 template files
> 3. update `content_metadata_profile.yaml` with the missing doc fields
> 4. populate `standards/metadata_rules.yaml`
> 5. normalize all blueprint pages to the standard page front matter
> 6. normalize all ADRs to the ADR front matter
> 
> If you want, I’ll draft the exact contents for:
> - `templates/page_template.md`
> - `templates/section_index_template.md`
> - `templates/adr_template.md`
> - `standards/metadata_rules.yaml`
> - updated `standards/content_metadata_profile.yaml`

### User
> and if the adr, standards, registry and scheasa nd all that is outside of docs i wont see it on my documentatino site? here is some front matter in this sections, --- id: ""                     # Canonical UUID/ULID short_code: ""             # Q + 6 hex (e.g., QX8B291) domain_prefix: "bbr4821" document_type: "artifact" artifact_kind: "implementation_plan" # walkthrough, task, architecture, other title: "Untitled Artifact" status: "active"           # active, superseded, archived target_system: ""          # Affected system/module (e.g., QiArchive, qione-portal) created_at: "" updated_at: "" author: "AI/System" source_type: "generated" ---  # {{title}}, and we have other taxonomies for front matter in earlier attempats at this.  also i dont like the idea of differnt front matter for things, im ok with maybe like a layout identifier more generally labeled front matter and the layout identifier is what confirms the meaning and purpose of the fields or a more conocial approach where all front matter fields are the same, but remember to keep it lien -- here was one system we had before thats from the qios constitution

### Assistant
> Not automatically.
> 
> ## Site visibility answer
> 
> By default, MkDocs builds from `docs_dir`, and the nav paths must be relative to `docs_dir`. The official docs say the source markdown files belong in the documentation directory and nav paths are relative to that directory. citeturn331533search0turn331533search5
> 
> So if `adr/`, `standards/`, `registry/`, and `schemas/` live **outside** `docs/`, they do **not** just appear on the site by magic.
> 
> ### Your current config has a mismatch
> Your current `mkdocs.yml` nav references:
> - `adr/ADR-0001_blueprint_scope.md`
> - `templates/artifact_template.md`
> - etc. fileciteturn9file1
> 
> But the blueprint doctrine also says:
> - doctrine lives in `docs/`
> - machine-readable constraints go in `standards/` and `registry/`
> - decision history goes in `adr/` fileciteturn9file3
> 
> That means you have two separate concerns:
> - **source-of-truth placement**
> - **site rendering**
> 
> Those are not the same thing.
> 
> ## Clean fix
> 
> Keep the canonical files where they belong:
> 
> ```text
> adr/
> standards/
> registry/
> schemas/
> ```
> 
> Then create **render pages inside `docs/`** that expose them.
> 
> ### Best pattern
> ```text
> docs/
>   01_governance/
>     standards.md
>     registry.md
>     decisions.md
>   08_appendices/
>     templates_catalog.md
> ```
> 
> Those pages can:
> - summarize the rule
> - embed YAML/JSON using macros/snippets
> - link to canonical file paths
> - show rendered tables from registry YAML
> 
> That keeps:
> - canonical source clean
> - docs site visible
> - no duplicate governance truth
> 
> That is the right architecture.
> 
> ## Do **not** do this
> Do not move `standards/` and `registry/` into `docs/` just so the site can see them. That weakens the structural separation the blueprint already established. fileciteturn9file3
> 
> ---
> 
> # Front matter: settle it once
> 
> I agree with you: **one canonical front matter schema** is better.
> 
> Not multiple incompatible schemas.
> 
> But the trick is this:
> 
> ## One schema, variable requirements by `layout`
> 
> So:
> - one field vocabulary
> - one YAML shape
> - one content metadata profile
> - `layout` determines which fields matter
> 
> That gives you consistency without chaos.
> 
> ---
> 
> # What to keep from the old constitution
> 
> The old front matter system had some good instincts:
> - `title`
> - `slug`
> - `keywords`
> - `tags`
> - `context`
> - `aliases`
> - `status`
> - `summary`
> - `sensitivity`
> - `classification` fileciteturn9file10turn9file13
> 
> ## What to demote or kill
> The blueprint already rejects old front-matter-as-identity logic and strips out graph-poetry / ornamental ontology:
> 
> - front matter as source of truth for relationships: **forbidden**
> - `qid_rpc`: retired
> - `qi_decimal`: retired as verbatim front matter law
> - `orbit`, `entangled`, `graph_weight`: retired from canonical governance
> - realms demoted to UI/workspace layer, not structural routing fileciteturn9file5
> 
> So do **not** resurrect those as canonical front matter just because they existed before.
> 
> ---
> 
> # My recommendation: one universal front matter schema
> 
> Use one schema like this:
> 
> ```yaml
> ---
> layout: ""                # home | section | page | adr | standard | registry | appendix | template | artifact
> title: ""
> slug: ""
> summary: ""
> status: "active"          # draft | active | superseded | archived
> created_at: ""
> updated_at: ""
> author: ""
> owner: ""
> tags: []
> keywords: []
> aliases: []
> context: ""
> sensitivity: "internal"
> classification: "business_internal"
> 
> uid: ""                   # doc-local stable id, not DB truth
> canonical_ref: ""         # optional reference to actual canonical object/archive/entity id
> source_type: "manual"     # manual | generated | imported
> template_key: ""
> 
> domain: ""                # optional doc subject area, not schema issuance
> subdomain: ""
> target_system: ""
> target_scope: ""          # optional: qione, qiarchive, qihome, etc.
> 
> artifact_kind: ""         # only meaningful when layout=artifact
> adr_id: ""                # only meaningful when layout=adr
> supersedes: ""            # optional for adr/page
> registry_key: ""          # only meaningful when layout=registry
> standard_key: ""          # only meaningful when layout=standard
> ---
> ```
> 
> ## Why this works
> Same front matter everywhere.
> 
> But:
> - `layout=adr` means `adr_id` matters
> - `layout=artifact` means `artifact_kind` matters
> - `layout=standard` means `standard_key` matters
> - `layout=registry` means `registry_key` matters
> 
> That gives you one universal schema without pretending every field is meaningful on every page.
> 
> ---
> 
> # Important correction to your current artifact front matter
> 
> This part is the problem:
> 
> ```yaml
> id: ""
> short_code: ""
> domain_prefix: "bbr4821"
> ```
> 
> For docs/front matter, that is too close to pretending the markdown file is issuing system identity.
> 
> The blueprint is explicit:
> front matter is supportive metadata, never the system of record; canonical identity comes from QiArchive, placement comes from the pipeline, and front matter must not change database relationships. fileciteturn9file0
> 
> ## So change it to this
> Use:
> 
> ```yaml
> uid: ""
> canonical_ref: ""
> domain: ""
> ```
> 
> instead of:
> 
> ```yaml
> id:
> short_code:
> domain_prefix:
> ```
> 
> unless the page is literally documenting an already-issued canonical record and `canonical_ref` is just a pointer.
> 
> ---
> 
> # Required vs optional fields
> 
> This is the part that keeps it sane.
> 
> ## Required on every markdown doc
> ```yaml
> layout
> title
> status
> created_at
> updated_at
> author
> uid
> source_type
> ```
> 
> ## Strongly recommended everywhere
> ```yaml
> summary
> tags
> keywords
> sensitivity
> classification
> template_key
> ```
> 
> ## Conditional by layout
> - `adr_id`, `supersedes` for ADRs
> - `artifact_kind`, `target_system` for artifacts
> - `standard_key` for standards
> - `registry_key` for registry docs
> 
> That gives you one schema and one enforcement model.
> 
> ---
> 
> # Canonical doctrine line you should lock
> 
> Use this exact rule in your metadata doctrine:
> 
> **Front matter is uniform across markdown assets.  
> Meaning is determined by `layout`.  
> Required fields may vary by `layout`, but the field vocabulary is singular.  
> Front matter is supportive metadata only and must not issue canonical identity, schema placement, or routing truth.**
> 
> That aligns with where the blueprint already landed on front matter and metadata. fileciteturn9file0turn9file5
> 
> ---
> 
> # My blunt recommendation
> 
> Do this:
> 
> 1. keep `adr/`, `standards/`, `registry/`, `schemas/` outside `docs/`
> 2. expose them on the site through `docs/` pages that render or summarize them
> 3. adopt **one universal front matter schema**
> 4. use `layout` as the discriminator
> 5. kill `qid`, `qi_decimal`, `orbit`, `entangled`, `graph_weight` from canonical markdown front matter
> 6. use `uid` + optional `canonical_ref`, not fake canonical identity in docs
> 
> That is the coherent version.
> 
> If you want, next I’ll draft the final locked:
> - `standards/content_metadata_profile.yaml`
> - `templates/page_template.md`
> - `templates/adr_template.md`
> - `templates/artifact_template.md`
> - `docs/01_governance/metadata_policy.md`

### User
> ok to confirm, there nothing in these file we should keep either i can remove them? prop_name,type,options,required,default,description

> title,string,,true,,Human-readable title of the node.

> slug,string,lowercase_underscored,true,,"Unique filename-safe identifier (lowercase, underscores)."

> realm,string,"QiPersonal|QiBusiness|QiClients|QiVault|QiPlayground|QiResearch|QiTemp|Archives|QiPublish|QiLegal",true,,Meaning universe this node belongs to.

> realm_slug,string,,false,,"Specific realm instance (e.g., inh, punchpro, qios, genesis)."

> qi_decimal,string,##.##.##-TYPE,false,,Sorting + categorical identity code.

> qid,string,,false,,"Autopopulated immutable node ID claimed from qid_counter via Layer 5 worker."

> type,string,"doc|asset|schema|workflow|worker|rule|site|project",true,doc,Object class in QiOS ontology.

> node,string,"concept|file|asset|rule|task|entity",true,concept,Graph classification.

> keywords,array[string],,false,[],Search and retrieval descriptors.

> tags,array[string],,false,[],Organizational tags for grouping/filtering.

> context,string,,false,,Short semantic context for routing/RAG.

> aliases,array[string],,false,[],Alternative names for lookup/backlinks.

> created,datetime,,true,,Creation timestamp (system-generated).

> updated,datetime,,true,,Last modification timestamp.

> version,string,semver,false,0.0.0,Semantic version number.

> status,string,"draft|active|canonical|archived",false,draft,Lifecycle state.

> system,string,"qinote|qios|qiclient|qipersonal|realm-local",false,realm-local,Logical subsystem grouping label.

> naming_strategy,string,"slug_only|qidecimal_slug",false,slug_only,Filename generation strategy.

> sort,number,,false,0,Manual sorting override for tables/lists.

> related,array[string],,false,[],QIDs of related nodes.

> parents,array[string],,false,[],Parent nodes in graph.

> children,array[string],,false,[],Child nodes in graph.

> siblings,array[string],,false,[],Peer nodes in graph.

> references,array[string],,false,[],External references or citations.

> graph_weight,number,1-10,false,1,Importance weighting in QiGraph.

> orbit,string,"core|inner|mid|outer",false,mid,Conceptual influence layer.

> entangled,array[string],,false,[],Nodes with intrinsically linked identity.

> summary,string,auto-generated,false,,"Auto-generated semantic summary (never manually edited)."

> sensitivity,string,"public|internal|confidential|restricted|secret",false,,Visibility/privacy level for access/redaction.

> classification,string,"personal_health|personal_finance|legal|immigration|client_confidential|business_internal|marketing_public|system_darkmatter|other",false,,Domain classification for routing boosts and safe views.  
> 
> and this is something tied to the new blueprint any changes to make here, # Content Metadata Profile (Front Matter Schema)

> #

> # DOCTRINE:

> # Content front matter is SUPPORTIVE METADATA, not the system of record.

> # Canonical identity, schema placement, and routing truth ALWAYS come from 

> # the database (QiArchive, qisys, qione, etc.). This profile normalizes the

> # structure for flat files, notes, and assets.

> 

> profile: content_front_matter

> version: 1.0.0

> description: "Standardized front matter properties for content assets and notes."

> 

> fields:

>   title:

>     type: string

>     description: "Human readable title"

>     required: false

>   slug:

>     type: string

>     description: "URL-friendly string. Does not override canonical Q-ID routing."

>     required: false

>   aliases:

>     type: array

>     items: string

>     description: "Alternative titles or natural language handles."

>     required: false

>   tags:

>     type: array

>     items: string

>     description: "Semantic markers for discovery."

>     required: false

>   keywords:

>     type: array

>     items: string

>     description: "SEO or deep search keywords."

>     required: false

>   context:

>     type: string

>     description: "Brief reasoning or context statement."

>     required: false

>   status:

>     type: string

>     description: "Content draft/review state. Does NOT override canonical pipeline status."

>     required: false

>   sensitivity:

>     type: string

>     description: "Must map to registry/sensitivity_classification.yaml"

>     required: false

>   classification:

>     type: string

>     description: "Must map to registry/sensitivity_classification.yaml"

>     required: false

>   summary:

>     type: string

>     description: "AI or human-generated summary. Explicitly non-canonical."

>     required: false

>   realm_label:

>     type: string

>     description: "UI/Workspace categorizer. Does not dictate band or physical domain placement."

>     required: false

### Assistant
> I’m checking the old front-matter list against the current blueprint doctrine so I can separate “salvageable” from “dead weight,” not just vibe it out. The likely answer is: keep a small subset, kill the old ontology baggage, and tighten the profile file.

### Assistant
> Not exactly. **Do not keep that old schema as active canon**, but there **are a few fields worth salvaging** into the new universal front matter.
> 
> ## Keep, but normalize
> 
> These are still useful under the new blueprint:
> 
> - `title`
> - `slug`
> - `aliases`
> - `tags`
> - `keywords`
> - `context`
> - `status`
> - `summary`
> - `sensitivity`
> - `classification`
> 
> Those fit the current doctrine for supportive front matter and align with what the current content metadata profile already preserves. fileciteturn10file1turn10file3turn10file12
> 
> ## Keep, but rename
> 
> These should survive only in the new naming style:
> 
> - `created` → `created_at`
> - `updated` → `updated_at`
> - `type` → **replace with** `layout`
> - `realm` / `realm_slug` → **replace with** `realm_label` only if you want a UI/workspace filter
> 
> Reason: realms were explicitly demoted to UI/workspace filtering and no longer control schema mapping, and front matter is not allowed to act as structural truth. fileciteturn10file1turn10file8
> 
> ## Drop from canonical front matter
> 
> These are legacy baggage and should be removed from the active profile:
> 
> - `qi_decimal`
> - `qid`
> - `node`
> - `system`
> - `naming_strategy`
> - `related`
> - `parents`
> - `children`
> - `siblings`
> - `graph_weight`
> - `orbit`
> - `entangled`
> 
> Why:
> - verbatim `qi_decimal` was retired as canonical front-matter law
> - legacy QID worker logic was stripped
> - graph-poetry fields like `orbit`, `entangled`, and `graph_weight` were explicitly excluded from governing doctrine
> - front matter as identity/relationship truth is forbidden now fileciteturn10file8turn10file13
> 
> ## Optional, but not necessary
> 
> These are not wrong, but I would not make them part of the core universal schema unless you have a real use case:
> 
> - `version`
> - `sort`
> - `references`
> 
> They are harmless, but they are not part of the currently stated supportive profile, so add them only if you know exactly why you need them. fileciteturn10file3
> 
> ---
> 
> # So can you remove the old file?
> 
> ## Yes, **after** you extract the salvageable pieces.
> Do **not** keep it as an active source of truth.
> 
> Best move:
> - migrate the useful fields into the new `content_metadata_profile.yaml`
> - archive the old constitution file as legacy reference
> - remove it from anything canonical or enforced
> 
> That is consistent with the blueprint’s salvage pass: useful parts were reframed, the rest was retired or demoted. fileciteturn10file8
> 
> ---
> 
> # Changes I would make to `content_metadata_profile.yaml`
> 
> Your current profile is close, but it is missing the fields needed to support a **single universal schema with a `layout` discriminator**.
> 
> ## Add these fields
> 
> ```yaml
> layout:
>   type: string
>   description: "Primary document/layout type. Determines intended use of optional fields."
>   required: true
> 
> uid:
>   type: string
>   description: "Document-local stable identifier. Not canonical system identity."
>   required: false
> 
> created_at:
>   type: string
>   description: "Creation timestamp for the document record."
>   required: false
> 
> updated_at:
>   type: string
>   description: "Last substantive update timestamp."
>   required: false
> 
> author:
>   type: string
>   description: "Human or system author."
>   required: false
> 
> template_key:
>   type: string
>   description: "Template used to create the document."
>   required: false
> 
> canonical_ref:
>   type: string
>   description: "Optional pointer to a canonical archive/entity/object ID. Referential only."
>   required: false
> 
> owner:
>   type: string
>   description: "Maintainer or accountable owner for the document."
>   required: false
> 
> references:
>   type: array
>   items: string
>   description: "Optional citations, external refs, or related document refs."
>   required: false
> ```
> 
> ## Rename this field
> 
> Replace:
> 
> ```yaml
> realm_label
> ```
> 
> with either:
> - keep `realm_label` if you want strict consistency with current doctrine, or
> - rename to `workspace_label` if you want clearer plain-English meaning
> 
> If you keep it as `realm_label`, that is already aligned with the current blueprint. fileciteturn10file1turn10file3
> 
> ## Tighten the doctrine header
> 
> I would revise the comment block to say:
> 
> ```yaml
> # DOCTRINE:
> # Front matter is supportive metadata only.
> # It may assist rendering, filtering, search, and lifecycle display.
> # It must not issue canonical identity, schema placement, routing truth,
> # graph relationships, or cross-domain ownership.
> # Meaning is determined by the `layout` field, but the field vocabulary is singular.
> ```
> 
> That matches the existing doctrine and your preference for one unified schema. fileciteturn10file1turn10file3
> 
> ---
> 
> # My recommended final universal field set
> 
> This is the lean version I’d lock:
> 
> ```yaml
> fields:
>   layout:
>   title:
>   slug:
>   summary:
>   status:
>   created_at:
>   updated_at:
>   author:
>   owner:
>   uid:
>   canonical_ref:
>   template_key:
>   aliases:
>   tags:
>   keywords:
>   context:
>   sensitivity:
>   classification:
>   realm_label:
>   references:
> ```
> 
> That gives you one schema, one mental model, and no old ontology contamination.
> 
> ---
> 
> # Blunt answer
> 
> - **No**, do not keep that old front-matter system as active canon.
> - **Yes**, salvage a subset of fields from it.
> - **Yes**, remove the old identity / graph / realm-control junk.
> - **Yes**, update `content_metadata_profile.yaml` to become the one universal schema with `layout` as the meaning switch.
> 
> The old file is useful as a **migration source**, not as ongoing doctrine. fileciteturn10file8turn10file7
> 
> If you want, I’ll write the exact final `content_metadata_profile.yaml` next.

### User
> can we group them in sections and have like always show, hidden if empty, always hidden, or just simple sections for quick human understanding and how can we enforce they stay in order it harder to know if the front matter is correct when it gets jumbled.

### Assistant
> I’m locking two things here: human readability and machine enforcement. The right move is a grouped universal schema plus a formatter/linter so the order stops drifting.

### Assistant
> Yes. That is the right move.
> 
> ## What to do
> 
> Use **one universal front matter schema**, but define:
> 
> 1. **sections** for human readability  
> 2. **display behavior** per field  
> 3. **one canonical field order**  
> 4. a **formatter + validator** so files get rewritten into the right order automatically
> 
> That keeps it lean and readable, and it stops the YAML soup problem.
> 
> The blueprint already frames front matter as **supportive metadata only**, not system truth, and the salvage pass already says the old front matter schema was kept only after being reframed as subordinate/non-canonical. It also explicitly demotes realms to UI/workspace labels and retires `qi_decimal`, `qid_rpc`, and graph-poetry fields like `orbit`, `entangled`, and `graph_weight`. fileciteturn11file0 fileciteturn11file1
> 
> ---
> 
> ## My recommendation
> 
> ### Section model
> 
> Use these sections, in this order:
> 
> ```yaml id="u1w8mk"
> sections:
>   core:
>   lifecycle:
>   classification:
>   context:
>   relations:
>   system:
>   layout_specific:
> ```
> 
> ### Display behaviors
> 
> Use three display modes:
> 
> - `always_show`
> - `hide_if_empty`
> - `always_hidden`
> 
> That gives you a clean mental model.
> 
> ---
> 
> ## Final universal front matter shape
> 
> These are the fields I’d lock.
> 
> ### 1. `core` — always first
> Humanly important. Always visible.
> 
> ```yaml id="clrz6u"
> layout
> title
> slug
> summary
> status
> ```
> 
> ### 2. `lifecycle`
> Usually visible, but lean.
> 
> ```yaml id="t8qr3m"
> created_at
> updated_at
> author
> owner
> ```
> 
> Recommended display:
> - `updated_at`: `always_show`
> - `created_at`, `author`, `owner`: `hide_if_empty`
> 
> ### 3. `classification`
> Useful, but not always relevant.
> 
> ```yaml id="76vcw3"
> sensitivity
> classification
> realm_label
> ```
> 
> Display:
> - all `hide_if_empty`
> 
> This matches current doctrine: `sensitivity` and `classification` are governed values, and `realm_label` is optional UI-layer labeling only. fileciteturn11file5 fileciteturn11file6
> 
> ### 4. `context`
> Good for search and humans.
> 
> ```yaml id="i7ry2h"
> context
> aliases
> tags
> keywords
> references
> ```
> 
> Display:
> - all `hide_if_empty`
> 
> ### 5. `relations`
> Only if needed.
> 
> ```yaml id="jwnjtz"
> target_system
> target_scope
> canonical_ref
> ```
> 
> Display:
> - `target_system`, `target_scope`: `hide_if_empty`
> - `canonical_ref`: `always_hidden`
> 
> Why hidden: it is useful for machine linkage, but front matter must not masquerade as canonical identity. fileciteturn11file5
> 
> ### 6. `system`
> Machine support fields. Hidden.
> 
> ```yaml id="38yqcp"
> uid
> template_key
> source_type
> ```
> 
> Display:
> - all `always_hidden`
> 
> ### 7. `layout_specific`
> Only meaningful for certain document types.
> 
> ```yaml id="7h0j2x"
> adr_id
> supersedes
> artifact_kind
> registry_key
> standard_key
> ```
> 
> Display:
> - all `hide_if_empty`
> - except maybe `adr_id` can be `always_show` when `layout=adr`
> 
> ---
> 
> ## What the profile file should become
> 
> Your current `content_metadata_profile.yaml` is too flat. Change it to include:
> 
> - field definitions
> - section membership
> - display behavior
> - canonical order
> - layout requirements
> 
> Here is the structure I’d use:
> 
> ```yaml id="tq4sul"
> profile: content_front_matter
> version: 2.0.0
> description: "Universal front matter profile for blueprint docs and related markdown assets."
> 
> doctrine:
>   system_of_record: false
>   notes:
>     - "Front matter is supportive metadata only."
>     - "Canonical identity comes from QiArchive or the owning system of record."
>     - "Schema placement and routing truth do not come from front matter."
>     - "Meaning is determined by layout, but the field vocabulary is singular."
> 
> sections:
>   - id: core
>     label: Core
>     order: 10
>   - id: lifecycle
>     label: Lifecycle
>     order: 20
>   - id: classification
>     label: Classification
>     order: 30
>   - id: context
>     label: Context
>     order: 40
>   - id: relations
>     label: Relations
>     order: 50
>   - id: system
>     label: System
>     order: 60
>   - id: layout_specific
>     label: Layout Specific
>     order: 70
> 
> display_modes:
>   - always_show
>   - hide_if_empty
>   - always_hidden
> 
> field_order:
>   - layout
>   - title
>   - slug
>   - summary
>   - status
>   - created_at
>   - updated_at
>   - author
>   - owner
>   - sensitivity
>   - classification
>   - realm_label
>   - context
>   - aliases
>   - tags
>   - keywords
>   - references
>   - target_system
>   - target_scope
>   - canonical_ref
>   - uid
>   - template_key
>   - source_type
>   - adr_id
>   - supersedes
>   - artifact_kind
>   - registry_key
>   - standard_key
> 
> fields:
>   layout:
>     type: string
>     required: true
>     section: core
>     display: always_show
>   title:
>     type: string
>     required: true
>     section: core
>     display: always_show
>   slug:
>     type: string
>     required: false
>     section: core
>     display: hide_if_empty
>   summary:
>     type: string
>     required: false
>     section: core
>     display: hide_if_empty
>   status:
>     type: string
>     required: true
>     section: core
>     display: always_show
> 
>   created_at:
>     type: string
>     required: false
>     section: lifecycle
>     display: hide_if_empty
>   updated_at:
>     type: string
>     required: false
>     section: lifecycle
>     display: always_show
>   author:
>     type: string
>     required: false
>     section: lifecycle
>     display: hide_if_empty
>   owner:
>     type: string
>     required: false
>     section: lifecycle
>     display: hide_if_empty
> 
>   sensitivity:
>     type: string
>     required: false
>     section: classification
>     display: hide_if_empty
>   classification:
>     type: string
>     required: false
>     section: classification
>     display: hide_if_empty
>   realm_label:
>     type: string
>     required: false
>     section: classification
>     display: hide_if_empty
> 
>   context:
>     type: string
>     required: false
>     section: context
>     display: hide_if_empty
>   aliases:
>     type: array
>     items: string
>     required: false
>     section: context
>     display: hide_if_empty
>   tags:
>     type: array
>     items: string
>     required: false
>     section: context
>     display: hide_if_empty
>   keywords:
>     type: array
>     items: string
>     required: false
>     section: context
>     display: hide_if_empty
>   references:
>     type: array
>     items: string
>     required: false
>     section: context
>     display: hide_if_empty
> 
>   target_system:
>     type: string
>     required: false
>     section: relations
>     display: hide_if_empty
>   target_scope:
>     type: string
>     required: false
>     section: relations
>     display: hide_if_empty
>   canonical_ref:
>     type: string
>     required: false
>     section: relations
>     display: always_hidden
> 
>   uid:
>     type: string
>     required: false
>     section: system
>     display: always_hidden
>   template_key:
>     type: string
>     required: false
>     section: system
>     display: always_hidden
>   source_type:
>     type: string
>     required: false
>     section: system
>     display: always_hidden
> 
>   adr_id:
>     type: string
>     required: false
>     section: layout_specific
>     display: hide_if_empty
>   supersedes:
>     type: string
>     required: false
>     section: layout_specific
>     display: hide_if_empty
>   artifact_kind:
>     type: string
>     required: false
>     section: layout_specific
>     display: hide_if_empty
>   registry_key:
>     type: string
>     required: false
>     section: layout_specific
>     display: hide_if_empty
>   standard_key:
>     type: string
>     required: false
>     section: layout_specific
>     display: hide_if_empty
> 
> layouts:
>   page:
>     required: [layout, title, status]
>   section:
>     required: [layout, title, status]
>   adr:
>     required: [layout, title, status, adr_id]
>   artifact:
>     required: [layout, title, status, artifact_kind]
>   standard:
>     required: [layout, title, status, standard_key]
>   registry:
>     required: [layout, title, status, registry_key]
>   appendix:
>     required: [layout, title, status]
>   template:
>     required: [layout, title, status]
> ```
> 
> ---
> 
> ## How to enforce order
> 
> Do **not** rely on humans to keep YAML in order. That will fail.
> 
> ### Use 3 levels of enforcement
> 
> #### 1. Formatter
> Create a script like:
> 
> ```text id="e5fmgp"
> scripts/normalize_front_matter.py
> ```
> 
> Its job:
> - parse front matter
> - reorder fields according to `field_order`
> - drop unknown fields or flag them
> - optionally group by sections with blank lines/comments between groups
> 
> #### 2. Validator
> Extend `enforce_structure.py` or add:
> 
> ```text id="knmbue"
> scripts/validate_front_matter.py
> ```
> 
> Checks:
> - field order matches canonical order
> - required fields exist for that `layout`
> - forbidden retired fields are not used
> - enum values match registry if applicable
> 
> #### 3. CI / pre-commit
> Run formatter and validator:
> - pre-commit for local correction
> - CI for blocking merge if drift remains
> 
> That aligns with the repo’s general direction of machine-enforced standards and the rule that drift between formal architecture and implementation must be flagged and resolved. fileciteturn11file8 fileciteturn11file2
> 
> ---
> 
> ## Best human-facing behavior
> 
> For site rendering or editor previews, use this rule:
> 
> ### Always show
> - `layout`
> - `title`
> - `summary` if present
> - `status`
> - `updated_at`
> 
> ### Show only if present
> - `slug`
> - `author`
> - `owner`
> - `sensitivity`
> - `classification`
> - `realm_label`
> - `context`
> - `aliases`
> - `tags`
> - `keywords`
> - `references`
> - `target_system`
> - `target_scope`
> - layout-specific fields
> 
> ### Always hide
> - `uid`
> - `canonical_ref`
> - `template_key`
> - `source_type`
> 
> That gives you quick human sanity without exposing internal scaffolding.
> 
> ---
> 
> ## Important retired fields
> 
> These should be blocked in validation, not just discouraged:
> 
> ```yaml id="i9cvwq"
> retired_fields:
>   - qi_decimal
>   - qid
>   - node
>   - system
>   - naming_strategy
>   - related
>   - parents
>   - children
>   - siblings
>   - graph_weight
>   - orbit
>   - entangled
>   - realm
>   - realm_slug
> ```
> 
> Why: the salvage pass explicitly says those older ontology/graph/identity patterns were rewritten, demoted, or stripped. fileciteturn11file1
> 
> ---
> 
> ## Blunt answer
> 
> Yes:
> - **group them into sections**
> - **add display behavior**
> - **lock one field order**
> - **enforce it with a formatter, not vibes**
> 
> That is the only way front matter stays readable once multiple tools start touching it.
> 
> The cleanest model is:
> - one universal schema
> - `layout` determines required fields
> - sections make it human-readable
> - formatter keeps order
> - validator kills drift
> 
> If you want, next I’ll draft:
> 1. the final `standards/content_metadata_profile.yaml`
> 2. `scripts/normalize_front_matter.py`
> 3. a tiny `templates/page_template.md` and `templates/adr_template.md` that already follow the locked order

### User
> yes please.

### Assistant
> I’ve got the shape. I’m turning it into one enforceable profile plus a formatter that rewrites front matter into canonical order instead of just complaining after the fact.

### Assistant
> Here’s the locked starter set.
> 
> The governing direction is: **front matter stays supportive, not canonical**, one unified field vocabulary, `layout` drives meaning, and retired legacy fields like `qid`, `qi_decimal`, `orbit`, and `entangled` stay dead. That matches the current blueprint doctrine and the salvage pass. fileciteturn5file0 fileciteturn8file0
> 
> ---
> 
> ## `standards/content_metadata_profile.yaml`
> 
> ```yaml
> # Content Metadata Profile (Front Matter Schema)
> #
> # DOCTRINE:
> # Front matter is supportive metadata only.
> # It may assist rendering, filtering, search, and lifecycle display.
> # It must not issue canonical identity, schema placement, routing truth,
> # graph relationships, or cross-domain ownership.
> # Meaning is determined by the `layout` field, but the field vocabulary is singular.
> 
> profile: content_front_matter
> version: 2.0.0
> description: "Universal front matter profile for blueprint docs and related markdown assets."
> 
> doctrine:
>   system_of_record: false
>   notes:
>     - "Canonical identity comes from QiArchive or the owning system of record."
>     - "Schema placement and routing truth do not come from front matter."
>     - "Front matter may not redefine ownership, graph truth, or cross-domain relationships."
>     - "Required fields vary by layout, but the field vocabulary remains singular."
> 
> display_modes:
>   - always_show
>   - hide_if_empty
>   - always_hidden
> 
> sections:
>   - id: core
>     label: Core
>     order: 10
>   - id: lifecycle
>     label: Lifecycle
>     order: 20
>   - id: classification
>     label: Classification
>     order: 30
>   - id: context
>     label: Context
>     order: 40
>   - id: relations
>     label: Relations
>     order: 50
>   - id: system
>     label: System
>     order: 60
>   - id: layout_specific
>     label: Layout Specific
>     order: 70
> 
> field_order:
>   - layout
>   - title
>   - slug
>   - summary
>   - status
> 
>   - created_at
>   - updated_at
>   - author
>   - owner
> 
>   - sensitivity
>   - classification
>   - realm_label
> 
>   - context
>   - aliases
>   - tags
>   - keywords
>   - references
> 
>   - target_system
>   - target_scope
>   - canonical_ref
> 
>   - uid
>   - template_key
>   - source_type
> 
>   - adr_id
>   - supersedes
>   - artifact_kind
>   - registry_key
>   - standard_key
> 
> fields:
>   layout:
>     type: string
>     required: true
>     section: core
>     display: always_show
>     description: "Document/layout type. Determines required conditional fields."
>     options:
>       - home
>       - section
>       - page
>       - adr
>       - standard
>       - registry
>       - appendix
>       - template
>       - artifact
> 
>   title:
>     type: string
>     required: true
>     section: core
>     display: always_show
>     description: "Human-readable title."
> 
>   slug:
>     type: string
>     required: false
>     section: core
>     display: hide_if_empty
>     description: "URL-friendly identifier. Does not control canonical identity."
> 
>   summary:
>     type: string
>     required: false
>     section: core
>     display: hide_if_empty
>     description: "Short summary for humans/search. Non-canonical."
> 
>   status:
>     type: string
>     required: true
>     section: core
>     display: always_show
>     description: "Document lifecycle state."
>     options:
>       - draft
>       - active
>       - proposed
>       - accepted
>       - superseded
>       - archived
> 
>   created_at:
>     type: string
>     required: false
>     section: lifecycle
>     display: hide_if_empty
>     description: "Creation date or timestamp."
> 
>   updated_at:
>     type: string
>     required: false
>     section: lifecycle
>     display: always_show
>     description: "Last substantive update date or timestamp."
> 
>   author:
>     type: string
>     required: false
>     section: lifecycle
>     display: hide_if_empty
>     description: "Human or system author."
> 
>   owner:
>     type: string
>     required: false
>     section: lifecycle
>     display: hide_if_empty
>     description: "Maintainer or accountable owner."
> 
>   sensitivity:
>     type: string
>     required: false
>     section: classification
>     display: hide_if_empty
>     description: "Must map to registry/sensitivity_classification.yaml."
> 
>   classification:
>     type: string
>     required: false
>     section: classification
>     display: hide_if_empty
>     description: "Must map to registry/sensitivity_classification.yaml."
> 
>   realm_label:
>     type: string
>     required: false
>     section: classification
>     display: hide_if_empty
>     description: "Optional UI/workspace filter label only. Does not dictate placement."
> 
>   context:
>     type: string
>     required: false
>     section: context
>     display: hide_if_empty
>     description: "Brief reasoning or context statement."
> 
>   aliases:
>     type: array
>     items: string
>     required: false
>     section: context
>     display: hide_if_empty
>     description: "Alternative titles or natural language handles."
> 
>   tags:
>     type: array
>     items: string
>     required: false
>     section: context
>     display: hide_if_empty
>     description: "Semantic grouping tags."
> 
>   keywords:
>     type: array
>     items: string
>     required: false
>     section: context
>     display: hide_if_empty
>     description: "Search descriptors."
> 
>   references:
>     type: array
>     items: string
>     required: false
>     section: context
>     display: hide_if_empty
>     description: "Related document refs or external references."
> 
>   target_system:
>     type: string
>     required: false
>     section: relations
>     display: hide_if_empty
>     description: "Primary system/module affected, if applicable."
> 
>   target_scope:
>     type: string
>     required: false
>     section: relations
>     display: hide_if_empty
>     description: "Optional narrower scope such as schema, app, or feature."
> 
>   canonical_ref:
>     type: string
>     required: false
>     section: relations
>     display: always_hidden
>     description: "Optional pointer to an external canonical ID. Referential only."
> 
>   uid:
>     type: string
>     required: false
>     section: system
>     display: always_hidden
>     description: "Document-local stable identifier. Not canonical system identity."
> 
>   template_key:
>     type: string
>     required: false
>     section: system
>     display: always_hidden
>     description: "Template used to create the document."
> 
>   source_type:
>     type: string
>     required: false
>     section: system
>     display: always_hidden
>     description: "manual | generated | imported"
>     options:
>       - manual
>       - generated
>       - imported
> 
>   adr_id:
>     type: string
>     required: false
>     section: layout_specific
>     display: hide_if_empty
>     description: "ADR identifier when layout=adr."
> 
>   supersedes:
>     type: string
>     required: false
>     section: layout_specific
>     display: hide_if_empty
>     description: "Document or ADR superseded by this file."
> 
>   artifact_kind:
>     type: string
>     required: false
>     section: layout_specific
>     display: hide_if_empty
>     description: "Artifact subtype when layout=artifact."
>     options:
>       - implementation_plan
>       - walkthrough
>       - task
>       - architecture
>       - report
>       - other
> 
>   registry_key:
>     type: string
>     required: false
>     section: layout_specific
>     display: hide_if_empty
>     description: "Registry identifier when layout=registry."
> 
>   standard_key:
>     type: string
>     required: false
>     section: layout_specific
>     display: hide_if_empty
>     description: "Standard identifier when layout=standard."
> 
> layouts:
>   home:
>     required:
>       - layout
>       - title
>       - status
>   section:
>     required:
>       - layout
>       - title
>       - status
>   page:
>     required:
>       - layout
>       - title
>       - status
>   adr:
>     required:
>       - layout
>       - title
>       - status
>       - adr_id
>   standard:
>     required:
>       - layout
>       - title
>       - status
>       - standard_key
>   registry:
>     required:
>       - layout
>       - title
>       - status
>       - registry_key
>   appendix:
>     required:
>       - layout
>       - title
>       - status
>   template:
>     required:
>       - layout
>       - title
>       - status
>   artifact:
>     required:
>       - layout
>       - title
>       - status
>       - artifact_kind
> 
> retired_fields:
>   - qi_decimal
>   - qid
>   - type
>   - node
>   - system
>   - naming_strategy
>   - sort
>   - related
>   - parents
>   - children
>   - siblings
>   - graph_weight
>   - orbit
>   - entangled
>   - realm
>   - realm_slug
>   - id
>   - short_code
>   - domain_prefix
> ```
> 
> ---
> 
> ## `scripts/normalize_front_matter.py`
> 
> ```python
> #!/usr/bin/env python3
> """
> Normalize Markdown front matter to the canonical field order defined in
> standards/content_metadata_profile.yaml.
> 
> What it does:
> - reads YAML front matter at the top of .md files
> - reorders keys according to the profile's field_order
> - groups keys by section with blank lines between groups
> - validates required fields based on layout
> - flags retired or unknown fields
> - can check-only or rewrite in place
> 
> Notes:
> - comments inside front matter are not preserved
> - body content is preserved
> """
> 
> from __future__ import annotations
> 
> import argparse
> import sys
> from pathlib import Path
> from typing import Dict, List, Tuple, Any
> 
> import yaml
> 
> 
> PROFILE_DEFAULT = Path("standards/content_metadata_profile.yaml")
> 
> 
> def load_yaml(path: Path) -> dict:
>     with path.open("r", encoding="utf-8") as f:
>         return yaml.safe_load(f) or {}
> 
> 
> def extract_front_matter(text: str) -> Tuple[dict | None, str]:
>     """
>     Return (front_matter_dict_or_none, remaining_body).
>     Only supports YAML front matter at the very top of the file.
>     """
>     if not text.startswith("---\n"):
>         return None, text
> 
>     parts = text.split("\n---\n", 1)
>     if len(parts) != 2:
>         return None, text
> 
>     fm_raw = parts[0][4:]  # strip leading "---\n"
>     body = parts[1]
> 
>     try:
>         data = yaml.safe_load(fm_raw) or {}
>         if not isinstance(data, dict):
>             return None, text
>         return data, body
>     except yaml.YAMLError:
>         return None, text
> 
> 
> def build_section_map(profile: dict) -> Dict[str, List[str]]:
>     fields = profile.get("fields", {})
>     sections = profile.get("sections", [])
>     section_order = [s["id"] for s in sorted(sections, key=lambda s: s.get("order", 999))]
>     section_map: Dict[str, List[str]] = {sid: [] for sid in section_order}
> 
>     for field_name in profile.get("field_order", []):
>         meta = fields.get(field_name, {})
>         section_id = meta.get("section")
>         if section_id in section_map:
>             section_map[section_id].append(field_name)
> 
>     return section_map
> 
> 
> def validate_front_matter(front_matter: dict, profile: dict) -> List[str]:
>     errors: List[str] = []
>     retired_fields = set(profile.get("retired_fields", []))
>     defined_fields = set(profile.get("fields", {}).keys())
> 
>     for key in front_matter:
>         if key in retired_fields:
>             errors.append(f"retired field present: {key}")
>         elif key not in defined_fields:
>             errors.append(f"unknown field present: {key}")
> 
>     layout = front_matter.get("layout")
>     if not layout:
>         errors.append("missing required field: layout")
>         return errors
> 
>     layouts = profile.get("layouts", {})
>     required = layouts.get(layout, {}).get("required", [])
>     for key in required:
>         value = front_matter.get(key)
>         if value is None or value == "" or value == []:
>             errors.append(f"missing required field for layout={layout}: {key}")
> 
>     return errors
> 
> 
> def order_front_matter(front_matter: dict, profile: dict) -> List[Tuple[str, Any]]:
>     ordered: List[Tuple[str, Any]] = []
>     field_order = profile.get("field_order", [])
>     seen = set()
> 
>     for key in field_order:
>         if key in front_matter:
>             ordered.append((key, front_matter[key]))
>             seen.add(key)
> 
>     # Preserve unknown keys at the end so the script is not destructive.
>     # Validation can still fail on them in check mode if you want.
>     for key, value in front_matter.items():
>         if key not in seen:
>             ordered.append((key, value))
> 
>     return ordered
> 
> 
> def split_into_section_blocks(
>     ordered_items: List[Tuple[str, Any]], profile: dict
> ) -> List[List[Tuple[str, Any]]]:
>     fields = profile.get("fields", {})
>     section_map = build_section_map(profile)
>     block_lookup: Dict[str, List[Tuple[str, Any]]] = {sid: [] for sid in section_map.keys()}
>     trailing: List[Tuple[str, Any]] = []
> 
>     field_to_section = {
>         field_name: meta.get("section")
>         for field_name, meta in fields.items()
>     }
> 
>     for key, value in ordered_items:
>         section_id = field_to_section.get(key)
>         if section_id in block_lookup:
>             block_lookup[section_id].append((key, value))
>         else:
>             trailing.append((key, value))
> 
>     blocks = [items for items in block_lookup.values() if items]
>     if trailing:
>         blocks.append(trailing)
>     return blocks
> 
> 
> def yaml_scalar(value: Any) -> str:
>     if isinstance(value, str):
>         # Always quote strings for consistency and easier diffing.
>         return yaml.safe_dump(value, default_flow_style=False, sort_keys=False).strip()
>     return yaml.safe_dump(value, default_flow_style=False, sort_keys=False).strip()
> 
> 
> def render_front_matter(front_matter: dict, profile: dict) -> str:
>     ordered_items = order_front_matter(front_matter, profile)
>     blocks = split_into_section_blocks(ordered_items, profile)
> 
>     lines: List[str] = ["---"]
>     for block_idx, block in enumerate(blocks):
>         for key, value in block:
>             dumped = yaml_scalar(value)
>             if "\n" not in dumped:
>                 lines.append(f"{key}: {dumped}")
>             else:
>                 lines.append(f"{key}:")
>                 for subline in dumped.splitlines():
>                     lines.append(f"  {subline}")
>         if block_idx < len(blocks) - 1:
>             lines.append("")
>     lines.append("---")
>     return "\n".join(lines)
> 
> 
> def normalize_file(path: Path, profile: dict, check_only: bool = False) -> Tuple[bool, List[str]]:
>     original = path.read_text(encoding="utf-8")
>     front_matter, body = extract_front_matter(original)
> 
>     if front_matter is None:
>         return False, ["no valid front matter found"]
> 
>     errors = validate_front_matter(front_matter, profile)
>     rendered = render_front_matter(front_matter, profile)
>     normalized = f"{rendered}\n{body if body.startswith(chr(10)) else body}"
> 
>     changed = normalized != original
> 
>     if not check_only and changed:
>         path.write_text(normalized, encoding="utf-8")
> 
>     return changed, errors
> 
> 
> def iter_markdown_files(paths: List[Path]) -> List[Path]:
>     results: List[Path] = []
>     for path in paths:
>         if path.is_file() and path.suffix.lower() == ".md":
>             results.append(path)
>         elif path.is_dir():
>             results.extend(sorted(path.rglob("*.md")))
>     return results
> 
> 
> def main() -> int:
>     parser = argparse.ArgumentParser(description="Normalize Markdown front matter.")
>     parser.add_argument("paths", nargs="+", help="Markdown files or directories")
>     parser.add_argument(
>         "--profile",
>         default=str(PROFILE_DEFAULT),
>         help="Path to content_metadata_profile.yaml",
>     )
>     parser.add_argument(
>         "--check",
>         action="store_true",
>         help="Check only; do not rewrite files",
>     )
>     args = parser.parse_args()
> 
>     profile_path = Path(args.profile)
>     if not profile_path.exists():
>         print(f"ERROR: profile not found: {profile_path}", file=sys.stderr)
>         return 2
> 
>     profile = load_yaml(profile_path)
>     files = iter_markdown_files([Path(p) for p in args.paths])
> 
>     if not files:
>         print("No markdown files found.")
>         return 0
> 
>     had_errors = False
>     had_changes = False
> 
>     for file_path in files:
>         changed, errors = normalize_file(file_path, profile, check_only=args.check)
> 
>         if errors:
>             had_errors = True
>             print(f"[FAIL] {file_path}")
>             for err in errors:
>                 print(f"  - {err}")
>         else:
>             status = "WOULD-FIX" if args.check and changed else "FIXED" if changed else "OK"
>             print(f"[{status}] {file_path}")
> 
>         if changed:
>             had_changes = True
> 
>     if args.check:
>         if had_errors or had_changes:
>             return 1
>         return 0
> 
>     return 1 if had_errors else 0
> 
> 
> if __name__ == "__main__":
>     raise SystemExit(main())
> ```
> 
> ### Suggested usage
> 
> ```bash
> python scripts/normalize_front_matter.py docs templates adr
> python scripts/normalize_front_matter.py docs templates adr --check
> ```
> 
> ---
> 
> ## `templates/page_template.md`
> 
> ```markdown
> ---
> layout: "page"
> title: ""
> slug: ""
> summary: ""
> status: "active"
> 
> created_at: ""
> updated_at: ""
> author: ""
> owner: ""
> 
> sensitivity: "internal"
> classification: "business_internal"
> realm_label: ""
> 
> context: ""
> aliases: []
> tags: []
> keywords: []
> references: []
> 
> target_system: ""
> target_scope: ""
> canonical_ref: ""
> 
> uid: ""
> template_key: "page_template"
> source_type: "manual"
> 
> adr_id: ""
> supersedes: ""
> artifact_kind: ""
> registry_key: ""
> standard_key: ""
> ---
> 
> # {{title}}
> 
> ## Purpose
> 
> ## Scope
> 
> ## Rules / Guidance
> 
> ## Notes
> ```
> 
> ---
> 
> ## `templates/adr_template.md`
> 
> ```markdown
> ---
> layout: "adr"
> title: "ADR-0000: "
> slug: ""
> summary: ""
> status: "proposed"
> 
> created_at: ""
> updated_at: ""
> author: ""
> owner: ""
> 
> sensitivity: "internal"
> classification: "business_internal"
> realm_label: ""
> 
> context: ""
> aliases: []
> tags: []
> keywords: []
> references: []
> 
> target_system: ""
> target_scope: ""
> canonical_ref: ""
> 
> uid: ""
> template_key: "adr_template"
> source_type: "manual"
> 
> adr_id: "ADR-0000"
> supersedes: ""
> artifact_kind: ""
> registry_key: ""
> standard_key: ""
> ---
> 
> # {{title}}
> 
> ## Status
> 
> ## Context
> 
> ## Decision
> 
> ## Consequences
> 
> ### Positive
> 
> ### Negative
> 
> ## Affected Documents
> 
> ## Notes
> ```
> 
> ---
> 
> ## Two implementation notes
> 
> First, the formatter will normalize order, but it will also strip inline YAML comments inside front matter because PyYAML does not preserve them. That is the tradeoff for deterministic ordering.
> 
> Second, if you want the canonical files outside `docs/` to still show on the documentation site, the clean pattern is to keep them outside `docs/` as source-of-truth and render them through `docs/` pages or macros/snippets, not duplicate them as second sources of truth. Your current blueprint already separates doctrine in `docs/` from machine-readable constraints in `standards/` and `registry/`, and decision history in `adr/`. fileciteturn5file0
> 
> Next step: wire `normalize_front_matter.py` into `enforce_structure.py` or a pre-commit hook so the order drift dies instead of recurring.

### User
> now we probably need to add a adr for all this stuff we just did, then im going to export it again and ahve you double check the work, but one this you are still missing is the sub folders int he blueprint, its getting big so we need to start devidign up the folders more and keep it in order so that way the reader doesnt have to hop around, each section builds on top of the past sections(s)

### Assistant
> You’re right — this needs an ADR, and the docs need a second layer of structure now. The current shape is fine for v0.4-ish content, but once standards, metadata policy, templates, and rendering rules get added, the reader starts ping-ponging.

### Assistant
> Yes. This needs an ADR.
> 
> And yes, the docs need a **second structural layer** now.
> 
> ## The call
> 
> You just changed three governance-level things:
> 
> - front matter doctrine
> - template doctrine
> - documentation topology / reading order
> 
> That is not a casual edit. It touches governance and topology, which is ADR territory. The blueprint already says ADRs are required for changes to namespace, schema, topology, runtime boundaries, delivery surfaces, and identity rules. fileciteturn5file0
> 
> ## Use this next ADR
> 
> ### `ADR-0007-unified-front-matter-and-progressive-doc-topology.md`
> 
> ```markdown
> ---
> layout: "adr"
> title: "ADR-0007: Unified Front Matter and Progressive Documentation Topology"
> slug: "adr-0007-unified-front-matter-and-progressive-doc-topology"
> summary: "Adopts one universal front matter schema with layout-based meaning, canonical field ordering, and a second-layer documentation topology so blueprint sections read progressively instead of as flat page buckets."
> status: "proposed"
> 
> created_at: "2026-04-01"
> updated_at: "2026-04-01"
> author: "Cody / AI"
> owner: "Cody"
> 
> sensitivity: "internal"
> classification: "business_internal"
> realm_label: ""
> 
> context: "The blueprint has grown large enough that flat section folders are creating navigation friction. Prior front matter attempts also produced overlapping taxonomies, retired ontology fields, and drift between human-readable metadata and canonical system truth."
> aliases: []
> tags: ["governance", "front-matter", "documentation", "templates", "topology"]
> keywords: ["front matter", "layout", "templates", "doc structure", "blueprint topology"]
> references: []
> 
> target_system: "QiOS Master Blueprint"
> target_scope: "docs, templates, standards, scripts, mkdocs navigation"
> canonical_ref: ""
> 
> uid: ""
> template_key: "adr_template"
> source_type: "manual"
> 
> adr_id: "ADR-0007"
> supersedes: ""
> artifact_kind: ""
> registry_key: ""
> standard_key: ""
> ---
> 
> # ADR-0007: Unified Front Matter and Progressive Documentation Topology
> 
> ## Status
> 
> Proposed
> 
> ## Context
> 
> The blueprint documentation has expanded beyond a comfortable flat structure. Several sections now contain enough material that readers must hop between sibling pages without a clear progressive path.
> 
> At the same time, earlier front matter systems introduced overlapping and now-retired concepts such as `qid`, `qi_decimal`, graph-poetry attributes, and realm-driven structural meaning. The current blueprint doctrine already establishes that front matter is supportive metadata only, not the system of record, and that canonical truth comes from governed system layers rather than file headers. fileciteturn5file0 fileciteturn8file0
> 
> A unified, lean, enforceable front matter profile is required, along with a documentation topology that preserves reading order and reduces cognitive load.
> 
> ## Decision
> 
> QiOS adopts the following documentation and metadata rules:
> 
> 1. **Universal Front Matter Vocabulary**
>    - All markdown documentation within the blueprint uses one shared front matter vocabulary.
>    - The `layout` field determines document intent and conditional requirements.
>    - Required fields may vary by `layout`, but the field vocabulary remains singular.
> 
> 2. **Front Matter Is Supportive Metadata Only**
>    - Front matter does not issue canonical identity.
>    - Front matter does not define schema placement, routing truth, or graph truth.
>    - Legacy fields tied to retired identity/ontology models are removed from active doctrine.
> 
> 3. **Canonical Field Order**
>    - Front matter fields must appear in a governed order.
>    - Fields are grouped into human-readable sections.
>    - A formatter/linter will normalize order and validate layout-specific requirements.
> 
> 4. **Progressive Documentation Topology**
>    - Each major blueprint section may contain ordered subfolders.
>    - Subfolders must support a progressive reading path from overview to model to rules to reference.
>    - Documentation should read linearly within a section rather than as a flat bucket of peer pages.
> 
> 5. **Canonical Source Separation**
>    - `docs/` remains the rendered doctrine layer.
>    - `standards/`, `registry/`, `adr/`, and `schemas/` remain canonical source layers outside `docs/`.
>    - The documentation site may render or summarize those sources through pages in `docs/`, but they do not move into `docs/` merely for visibility.
> 
> ## Consequences
> 
> ### Positive
> 
> - Reduces front matter drift and overlapping taxonomies.
> - Makes documentation easier to read in sequence.
> - Preserves separation between rendered doctrine and machine-readable source-of-truth files.
> - Creates a stable template and validation model for future growth.
> 
> ### Negative
> 
> - Existing docs will need normalization and partial folder moves.
> - MkDocs navigation must be updated to reflect second-layer section structure.
> - Some legacy front matter fields and earlier taxonomy experiments will be formally retired.
> 
> ## Affected Documents
> 
> - `standards/content_metadata_profile.yaml`
> - `standards/metadata_rules.yaml`
> - `templates/page_template.md`
> - `templates/adr_template.md`
> - `templates/artifact_template.md`
> - `scripts/normalize_front_matter.py`
> - `mkdocs.yml`
> - `docs/01_governance/*`
> - `docs/02_architecture/*`
> - `docs/03_structure/*`
> - `docs/04_data/*`
> - `docs/05_compute/*`
> - `docs/06_applications/*`
> - `docs/07_operations/*`
> ```
> 
> ## The missing piece: subfolders
> 
> You’re right. I was still treating sections too flat.
> 
> ### New rule
> Each major section gets a **progressive subfolder ladder**.
> 
> Not deep nesting everywhere. Just enough structure so the reader moves through the section in order.
> 
> ## Recommended pattern
> 
> Use this pattern inside each major section:
> 
> ```text
> section/
>   index.md
>   10_overview/
>   20_models/
>   30_rules/
>   40_reference/
> ```
> 
> Not every section needs every bucket, but the order stays stable.
> 
> ## Better blueprint shape
> 
> ```text
> docs/
>   01_governance/
>     index.md
>     10_foundation/
>       principles.md
>     20_policy/
>       policies.md
>       agent_rules.md
>     30_standards/
>       standards.md
>       metadata_policy.md
>       templates_policy.md
>     40_registry/
>       registry.md
>     50_decisions/
>       decisions.md
> 
>   02_architecture/
>     index.md
>     10_identity/
>       identity.md
>     20_system/
>       system_model.md
>       component_map.md
>     30_runtime/
>       runtime_zones.md
>       device_model.md
>       service_boundaries.md
>     40_flows/
>       data_flow.md
> 
>   03_structure/
>     index.md
>     10_bands/
>       bands.md
>     20_domains/
>       domains.md
>     30_namespaces/
>       namespace_registry.md
>       subdomains.md
>     40_objects/
>       object_model.md
>       placement_rules.md
>       directory_tree.md
> 
>   04_data/
>     index.md
>     10_schema/
>       schema.md
>       objects.md
>     20_metadata/
>       metadata.md
>     30_storage/
>       storage.md
>       exports.md
>     40_domain_addenda/
>       qievidence.md
> 
>   05_compute/
>     index.md
>     10_apis/
>       apis.md
>     20_workers/
>       workers.md
>     30_pipelines/
>       pipelines.md
>     40_runtime/
>       runtime.md
>       tech_stack.md
>     50_integrations/
>       integrations.md
> 
>   06_applications/
>     index.md
>     10_web/
>       web.md
>     20_portal/
>       portal.md
>     30_admin/
>       admin.md
>     40_tools/
>       tools.md
>     50_interfaces/
>       interfaces.md
> 
>   07_operations/
>     index.md
>     10_clients/
>       clients.md
>     20_cases/
>       cases.md
>     30_finance/
>       finance.md
>     40_products/
>       products.md
>     50_templates/
>       templates.md
> 
>   08_appendices/
>     index.md
>     10_reference/
>       changelog.md
>       glossary.md
>       migration_notes.md
>     20_legacy/
>       legacy_salvage.md
>       legacy_csv_migration_plan.md
> ```
> 
> ## Why this works
> 
> It gives you:
> 
> - stable reading order
> - less visual clutter per folder
> - clearer nav updates later
> - easier future growth
> - less hopping around inside a section
> 
> And it preserves the bigger doctrine split:
> - `docs/` = rendered/prose layer
> - `standards/`, `registry/`, `adr/`, `schemas/` = canonical support layers outside docs fileciteturn5file0
> 
> ## One rule to keep this sane
> 
> Do **not** let docs nesting get stupid.
> 
> ### Lock this:
> - max section depth under `docs/` = **2 topic levels plus file**
> - every section keeps an `index.md`
> - subfolders use numeric prefixes
> - folders represent reading sequence, not random taxonomy piles
> 
> ## Practical next moves
> 
> Do these in order:
> 
> 1. create `ADR-0007`
> 2. move docs into second-layer section subfolders
> 3. update `mkdocs.yml` nav to match
> 4. update templates to use the new universal front matter
> 5. run the front matter normalizer after the moves
> 6. export again and then I’ll audit the whole thing
> 
> One thing to watch: once you add the subfolders, the nav is going to break until `mkdocs.yml` is updated to the new paths, because your current nav is still pointing to the flat layout. fileciteturn5file0
> 
> After you export the updated tree, send it and I’ll do a hard alignment pass.

### User
> first just hte tree. ```markdown

> . 📂 _qios_master_blueprint

> ├── 📄 README.md

> └── 📂 adr/

> │  ├── 📄 ADR-0000_template.md

> │  ├── 📄 ADR-0001_blueprint_scope.md

> │  ├── 📄 ADR-0002_single_domain_rule.md

> │  ├── 📄 ADR-0003_band_model.md

> │  ├── 📄 ADR-0004_qilabs_root.md

> │  ├── 📄 ADR-0005_fleet_orchestration.md

> │  ├── 📄 ADR-0006_narrative_and_knowledge_consolidation.md

> │  ├── 📄 ADR-0007-unified-front-matter-and-progressive-doc-topology.md

> │  ├── 📄 update-adr.md

> └── 📂 docs/

> │  └── 📂 00_genesis/

> │    ├── 📄 index.md

> │  └── 📂 01_governance/

> │    └── 📂 10_foundation/

> │      ├── 📄 principles.md

> │    └── 📂 20_policy/

> │      ├── 📄 agent_rules.md

> │      ├── 📄 policies.md

> │    └── 📂 30_standards/

> │      ├── 📄 metadata_policy.md

> │      ├── 📄 standards.md

> │      ├── 📄 templates_policy.md

> │    └── 📂 40_registry/

> │      ├── 📄 registry.md

> │    └── 📂 50_decisions/

> │      ├── 📄 decisions.md

> │    ├── 📄 index.md

> │  └── 📂 02_architecture/

> │    └── 📂 10_identity/

> │      ├── 📄 identity.md

> │    └── 📂 20_system/

> │      ├── 📄 component_map.md

> │      ├── 📄 system_model.md

> │    └── 📂 30_runtime/

> │      ├── 📄 device_model.md

> │      ├── 📄 runtime_zones.md

> │      ├── 📄 service_boundaries.md

> │    └── 📂 40_flows/

> │      ├── 📄 data_flow.md

> │    ├── 📄 index.md

> │  └── 📂 03_structure/

> │    └── 📂 10_bands/

> │      ├── 📄 bands.md

> │    └── 📂 20_domains/

> │      ├── 📄 domains.md

> │    └── 📂 30_namespaces/

> │      ├── 📄 namespace_registry.md

> │      ├── 📄 subdomains.md

> │    └── 📂 40_objects/

> │      ├── 📄 directory_tree.md

> │      ├── 📄 object_model.md

> │      ├── 📄 placement_rules.md

> │    ├── 📄 index.md

> │  └── 📂 04_data/

> │    └── 📂 10_schema/

> │      ├── 📄 front_matter.md

> │      ├── 📄 objects.md

> │      ├── 📄 schema.md

> │    └── 📂 20_metadata/

> │      ├── 📄 metadata.md

> │    └── 📂 30_storage/

> │      ├── 📄 exports.md

> │      ├── 📄 storage.md

> │    └── 📂 40_domain_addenda/

> │      ├── 📄 qievidence.md

> │    ├── 📄 index.md

> │  └── 📂 05_compute/

> │    └── 📂 10_apis/

> │      ├── 📄 apis.md

> │    └── 📂 20_workers/

> │      ├── 📄 workers.md

> │    └── 📂 30_pipelines/

> │      ├── 📄 pipelines.md

> │    └── 📂 40_runtime/

> │      ├── 📄 runtime.md

> │    └── 📂 50_integrations/

> │      ├── 📄 integrations.md

> │    ├── 📄 index.md

> │  └── 📂 06_applications/

> │    └── 📂 10_web/

> │      ├── 📄 web.md

> │    └── 📂 20_portal/

> │      ├── 📄 portal.md

> │    └── 📂 30_admin/

> │      ├── 📄 admin.md

> │    └── 📂 40_tools/

> │      ├── 📄 tools.md

> │    └── 📂 50_interfaces/

> │      ├── 📄 interfaces.md

> │    ├── 📄 index.md

> │  └── 📂 07_operations/

> │    └── 📂 10_clients/

> │      ├── 📄 clients.md

> │    └── 📂 20_cases/

> │      ├── 📄 cases.md

> │    └── 📂 30_finance/

> │      ├── 📄 finance.md

> │    └── 📂 40_services/

> │      ├── 📄 products.md

> │    └── 📂 50_templates/

> │      ├── 📄 templates.md

> │    ├── 📄 index.md

> │  └── 📂 08_appendices/

> │    └── 📂 10_reference/

> │      ├── 📄 glossary.md

> │      ├── 📄 templates_catalog.md

> │    └── 📂 20_legacy/

> │      ├── 📄 legacy_csv_migration_plan.md

> │      ├── 📄 legacy_salvage.md

> │      ├── 📄 migration_notes.md

> │    └── 📂 30_tech_stack/

> │      ├── 📄 tech_stack.md

> │    └── 📂 40_labs/

> │  └── 📂 assets/

> │    └── 📂 diagrams/

> │      ├── 📄 qios_04_rules_and_readmes.canvas.canvas

> │      ├── 📄 qios_05_Cursor_and_naming.canvas

> │    └── 📂 images/

> │      ├── 📄 _QiOS_Master_Document.jpg

> │    └── 📂 tables/

> │  ├── 📄 index.md

> └── 📂 logs/

> │  ├── 📄 changelog.md

> ├── 📄 main.py

> ├── 📄 markmind.html

> ├── 📄 mkdocs.yml

> └── 📂 overrides/

> │  ├── 📄 home.html

> └── 📂 registry/

> │  ├── 📄 band_registry.yaml

> │  ├── 📄 deprecation_registry.yaml

> │  ├── 📄 domain_registry.yaml

> │  ├── 📄 folder_registry.yaml

> │  ├── 📄 realms_registry.yaml

> │  ├── 📄 sensitivity_classification.yaml

> │  ├── 📄 subdomain_registry.yaml

> │  ├── 📄 workspace_realms.yaml

> └── 📂 schemas/

> │  ├── 📄 band_registry.schema.json

> └── 📂 scripts/

> │  ├── 📄 enforce_structure.py

> └── 📂 standards/

> │  ├── 📄 content_metadata_profile.yaml

> │  ├── 📄 metadata_rules.yaml

> │  ├── 📄 naming_rules.yaml

> │  ├── 📄 pdf_standards.yaml

> │  ├── 📄 repo_rules.yaml

> └── 📂 stylesheets/

> │  ├── 📄 extra.css

> └── 📂 templates/

> │  ├── 📄 README.md

> │  ├── 📄 tmp_adr_template.md

> │  ├── 📄 tmp_appendix_template.md

> │  ├── 📄 tmp_artifact_template.md

> │  ├── 📄 tmp_note_template.md

> │  ├── 📄 tmp_operational_template.md

> │  ├── 📄 tmp_page_template.md

> │  ├── 📄 tmp_registry_reference_template.md

> │  └── 📂 tmp_section_folder/

> │    └── 📂 10_overview/

> │    └── 📂 20_models/

> │    └── 📂 30_rules/

> │    └── 📂 40_reference/

> │    ├── 📄 index.md

> │  ├── 📄 tmp_section_index_template.md

> │  └── 📄 tmp_standard_template.md

> ```

### Assistant
> Here’s the **cleaned tree only**. This is the version I’d use as the next locked shape.
> 
> Main fixes:
> - `logs/changelog.md` moved into appendices where it belongs
> - `tech_stack.md` moved back under **Compute**
> - `40_services/products.md` corrected to **40_products/products.md**
> - all `tmp_*` template names cleaned up
> - `tmp_section_folder/` renamed into an actual reusable section scaffold
> - `markmind.html` removed from root tree for now because it is not part of canonical doctrine structure
> 
> ```markdown
> . 📂 _qios_master_blueprint
> ├── 📄 README.md
> ├── 📄 mkdocs.yml
> ├── 📄 main.py
> ├── 📂 adr/
> │  ├── 📄 ADR-0000_template.md
> │  ├── 📄 ADR-0001_blueprint_scope.md
> │  ├── 📄 ADR-0002_single_domain_rule.md
> │  ├── 📄 ADR-0003_band_model.md
> │  ├── 📄 ADR-0004_qilabs_root.md
> │  ├── 📄 ADR-0005_fleet_orchestration.md
> │  ├── 📄 ADR-0006_narrative_and_knowledge_consolidation.md
> │  ├── 📄 ADR-0007_unified_front_matter_and_progressive_doc_topology.md
> │  └── 📄 update-adr.md
> ├── 📂 docs/
> │  ├── 📄 index.md
> │  ├── 📂 00_genesis/
> │  │  └── 📄 index.md
> │  ├── 📂 01_governance/
> │  │  ├── 📄 index.md
> │  │  ├── 📂 10_foundation/
> │  │  │  └── 📄 principles.md
> │  │  ├── 📂 20_policy/
> │  │  │  ├── 📄 agent_rules.md
> │  │  │  └── 📄 policies.md
> │  │  ├── 📂 30_standards/
> │  │  │  ├── 📄 metadata_policy.md
> │  │  │  ├── 📄 standards.md
> │  │  │  └── 📄 templates_policy.md
> │  │  ├── 📂 40_registry/
> │  │  │  └── 📄 registry.md
> │  │  └── 📂 50_decisions/
> │  │     └── 📄 decisions.md
> │  ├── 📂 02_architecture/
> │  │  ├── 📄 index.md
> │  │  ├── 📂 10_identity/
> │  │  │  └── 📄 identity.md
> │  │  ├── 📂 20_system/
> │  │  │  ├── 📄 component_map.md
> │  │  │  └── 📄 system_model.md
> │  │  ├── 📂 30_runtime/
> │  │  │  ├── 📄 device_model.md
> │  │  │  ├── 📄 runtime_zones.md
> │  │  │  └── 📄 service_boundaries.md
> │  │  └── 📂 40_flows/
> │  │     └── 📄 data_flow.md
> │  ├── 📂 03_structure/
> │  │  ├── 📄 index.md
> │  │  ├── 📂 10_bands/
> │  │  │  └── 📄 bands.md
> │  │  ├── 📂 20_domains/
> │  │  │  └── 📄 domains.md
> │  │  ├── 📂 30_namespaces/
> │  │  │  ├── 📄 namespace_registry.md
> │  │  │  └── 📄 subdomains.md
> │  │  └── 📂 40_objects/
> │  │     ├── 📄 directory_tree.md
> │  │     ├── 📄 object_model.md
> │  │     └── 📄 placement_rules.md
> │  ├── 📂 04_data/
> │  │  ├── 📄 index.md
> │  │  ├── 📂 10_schema/
> │  │  │  ├── 📄 front_matter.md
> │  │  │  ├── 📄 objects.md
> │  │  │  └── 📄 schema.md
> │  │  ├── 📂 20_metadata/
> │  │  │  └── 📄 metadata.md
> │  │  ├── 📂 30_storage/
> │  │  │  ├── 📄 exports.md
> │  │  │  └── 📄 storage.md
> │  │  └── 📂 40_domain_addenda/
> │  │     └── 📄 qievidence.md
> │  ├── 📂 05_compute/
> │  │  ├── 📄 index.md
> │  │  ├── 📂 10_apis/
> │  │  │  └── 📄 apis.md
> │  │  ├── 📂 20_workers/
> │  │  │  └── 📄 workers.md
> │  │  ├── 📂 30_pipelines/
> │  │  │  └── 📄 pipelines.md
> │  │  ├── 📂 40_runtime/
> │  │  │  ├── 📄 runtime.md
> │  │  │  └── 📄 tech_stack.md
> │  │  └── 📂 50_integrations/
> │  │     └── 📄 integrations.md
> │  ├── 📂 06_applications/
> │  │  ├── 📄 index.md
> │  │  ├── 📂 10_web/
> │  │  │  └── 📄 web.md
> │  │  ├── 📂 20_portal/
> │  │  │  └── 📄 portal.md
> │  │  ├── 📂 30_admin/
> │  │  │  └── 📄 admin.md
> │  │  ├── 📂 40_tools/
> │  │  │  └── 📄 tools.md
> │  │  └── 📂 50_interfaces/
> │  │     └── 📄 interfaces.md
> │  ├── 📂 07_operations/
> │  │  ├── 📄 index.md
> │  │  ├── 📂 10_clients/
> │  │  │  └── 📄 clients.md
> │  │  ├── 📂 20_cases/
> │  │  │  └── 📄 cases.md
> │  │  ├── 📂 30_finance/
> │  │  │  └── 📄 finance.md
> │  │  ├── 📂 40_products/
> │  │  │  └── 📄 products.md
> │  │  └── 📂 50_templates/
> │  │     └── 📄 templates.md
> │  ├── 📂 08_appendices/
> │  │  ├── 📄 index.md
> │  │  ├── 📂 10_reference/
> │  │  │  ├── 📄 changelog.md
> │  │  │  ├── 📄 glossary.md
> │  │  │  └── 📄 templates_catalog.md
> │  │  ├── 📂 20_legacy/
> │  │  │  ├── 📄 legacy_csv_migration_plan.md
> │  │  │  ├── 📄 legacy_salvage.md
> │  │  │  └── 📄 migration_notes.md
> │  │  └── 📂 40_labs/
> │  └── 📂 assets/
> │     ├── 📂 diagrams/
> │     │  ├── 📄 qios_04_rules_and_readmes.canvas.canvas
> │     │  └── 📄 qios_05_Cursor_and_naming.canvas
> │     ├── 📂 images/
> │     │  └── 📄 _QiOS_Master_Document.jpg
> │     └── 📂 tables/
> ├── 📂 overrides/
> │  └── 📄 home.html
> ├── 📂 registry/
> │  ├── 📄 band_registry.yaml
> │  ├── 📄 deprecation_registry.yaml
> │  ├── 📄 domain_registry.yaml
> │  ├── 📄 folder_registry.yaml
> │  ├── 📄 realms_registry.yaml
> │  ├── 📄 sensitivity_classification.yaml
> │  ├── 📄 subdomain_registry.yaml
> │  └── 📄 workspace_realms.yaml
> ├── 📂 schemas/
> │  └── 📄 band_registry.schema.json
> ├── 📂 scripts/
> │  ├── 📄 enforce_structure.py
> │  └── 📄 normalize_front_matter.py
> ├── 📂 standards/
> │  ├── 📄 content_metadata_profile.yaml
> │  ├── 📄 metadata_rules.yaml
> │  ├── 📄 naming_rules.yaml
> │  ├── 📄 pdf_standards.yaml
> │  └── 📄 repo_rules.yaml
> ├── 📂 stylesheets/
> │  └── 📄 extra.css
> └── 📂 templates/
>    ├── 📄 README.md
>    ├── 📄 adr_template.md
>    ├── 📄 appendix_template.md
>    ├── 📄 artifact_template.md
>    ├── 📄 note_template.md
>    ├── 📄 operational_template.md
>    ├── 📄 page_template.md
>    ├── 📄 registry_reference_template.md
>    ├── 📄 section_index_template.md
>    ├── 📄 standard_template.md
>    └── 📂 section_folder_template/
>       ├── 📄 index.md
>       ├── 📂 10_overview/
>       ├── 📂 20_models/
>       ├── 📂 30_rules/
>       └── 📂 40_reference/
> ```
> 
> ## Two small calls
> 
> `00_genesis/` is still thin. That is fine for now. Do not overbuild it yet.
> 
> `08_appendices/40_labs/` is okay as a holding area only if it stays explicitly non-canonical and sparse. Otherwise it becomes a junk drawer fast.
> 
> Send the next export after you move the actual folders and I’ll do the hard alignment pass.

### User
> so i think whtas left for the blueprint at this poing is to add soem automation and update a couple more things. like, i need one rebuild.bat int he master blueprint root that will normalize, enforce structure, update indexes, markmind, and then add. commit push. click and blueprint udpated. heres the files you need to see first. we need to udpate the readme and what is this main.py, and can we imrpove the navigation pane maybe tree like toggles and i would like to incorporate the markmind as a view in the mkdocs but the markmind needs to be auto updated when i run this automation.

### Assistant
> I’ve got enough to map the automation cleanly. I’m verifying the current MkDocs/Material navigation options against official docs before I lock recommendations so we don’t bake in stale config names.

### Assistant
> Yes. You’re at the point where the blueprint wants a **one-click publish pipeline**.
> 
> ## What `main.py` is
> 
> Right now `main.py` is **not random app code**. It is the local **MkDocs Macros module** loaded by the `macros` plugin. The official MkDocs Macros docs say a local module named `main.py` beside `mkdocs.yml` is the default place for `define_env(env)`, and that `define_env()` is the hook used to register macros, variables, and filters. citeturn990021search0
> 
> Your current `main.py` does exactly two things:
> - `read_yaml(filename)` renders YAML into code fences
> - `render_band_registry(filename)` turns the band registry into a markdown table fileciteturn12file2
> 
> So the blunt answer is:
> 
> **`main.py` is your MkDocs macro/hook file.**  
> It should stay, but it should be upgraded and probably renamed into a cleaner module package later.
> 
> ---
> 
> ## What is wrong right now
> 
> ### 1. `markmind.html` is static and stale
> It hardcodes `rawData` directly in the file, and that tree is already outdated relative to your actual blueprint. fileciteturn12file0
> 
> That means every structural change risks the mind map lying to you.
> 
> ### 2. `mkdocs.yml` nav is still flat and outdated
> Your current nav still points at the older flat section paths like `01_governance/principles.md` instead of the new second-layer subfolders, and it still lists ADR/template paths as if they were under the old structure. fileciteturn12file1
> 
> ### 3. `enforce_structure.py` is too weak now
> It only checks for the existence of the top-level numbered docs sections and validates `band_registry.yaml` against one JSON schema. It does not understand the new subfolder topology, templates, or front matter normalization flow. fileciteturn12file5
> 
> ### 4. `normalize_front_matter.py` is good, but isolated
> It already knows how to normalize front matter order and validate required fields by layout, but nothing currently orchestrates it with the rest of the publish flow. fileciteturn12file4
> 
> ---
> 
> # What I would build
> 
> ## Root automation flow
> 
> Create one root batch file:
> 
> ```text id="xxk65r"
> rebuild.bat
> ```
> 
> It should do this in order:
> 
> 1. normalize front matter
> 2. enforce structure
> 3. rebuild generated artifacts
>    - markmind HTML/data
>    - docs indexes/catalogs if applicable
> 4. run mkdocs build locally as a check
> 5. git add
> 6. git commit
> 7. git push
> 
> That gives you:
> **click once → blueprint updated**
> 
> ---
> 
> ## Recommended command flow for `rebuild.bat`
> 
> ```bat id="8q1xjt"
> @echo off
> setlocal enabledelayedexpansion
> 
> echo ========================================
> echo QiOS Blueprint Rebuild
> echo ========================================
> 
> REM 1. Normalize front matter
> python scripts\normalize_front_matter.py docs adr templates
> if errorlevel 1 goto :fail
> 
> REM 2. Enforce structure + registry/schema validation
> python scripts\enforce_structure.py
> if errorlevel 1 goto :fail
> 
> REM 3. Regenerate Markmind from actual tree/nav
> python scripts\generate_markmind.py
> if errorlevel 1 goto :fail
> 
> REM 4. Rebuild docs indexes/catalogs if you add that later
> REM python scripts\update_indexes.py
> REM if errorlevel 1 goto :fail
> 
> REM 5. Build site as validation
> mkdocs build
> if errorlevel 1 goto :fail
> 
> REM 6. Git add / commit / push
> git add .
> git commit -m "docs: rebuild blueprint"
> if errorlevel 1 echo No commit created (possibly no changes)
> 
> git push
> if errorlevel 1 goto :fail
> 
> echo.
> echo SUCCESS: Blueprint rebuilt and pushed.
> goto :eof
> 
> :fail
> echo.
> echo FAILED: Blueprint rebuild halted.
> exit /b 1
> ```
> 
> I would **not** make it auto-push without a local build check. That is how bad nav or broken pages slip through.
> 
> ---
> 
> # README update
> 
> Your `README.md` should stop being vague and become the **operator entry point**.
> 
> ## Add these sections
> 
> - what this repo is
> - repo anatomy
> - one-click rebuild
> - what `main.py` does
> - what `rebuild.bat` does
> - what is canonical vs rendered
> - contributor workflow
> 
> ## Short recommended README outline
> 
> ```text id="3zv1ix"
> README.md
>   1. What this repo is
>   2. Canonical layers
>      - docs/
>      - adr/
>      - standards/
>      - registry/
>      - schemas/
>   3. Automation entry points
>      - rebuild.bat
>      - scripts/normalize_front_matter.py
>      - scripts/enforce_structure.py
>      - scripts/generate_markmind.py
>   4. MkDocs / Macros
>      - mkdocs.yml
>      - main.py
>   5. Publish workflow
>   6. Troubleshooting
> ```
> 
> ---
> 
> # Navigation improvements
> 
> ## What you already have
> Your current Material config already enables:
> - `navigation.sections`
> - `navigation.indexes`
> - `navigation.expand`
> - `navigation.top`
> - `navigation.footer`
> - search helpers and ToC follow fileciteturn12file1
> 
> ## What I would add
> Material for MkDocs supports additional navigation features like `navigation.instant`, which gives SPA-style internal navigation. The official Material docs explicitly document `navigation.instant`. citeturn990021search2
> 
> ### Recommended additions
> Add:
> 
> ```yaml id="33g1yc"
> theme:
>   features:
>     - navigation.instant
>     - navigation.sections
>     - navigation.indexes
>     - navigation.expand
>     - navigation.top
>     - navigation.footer
>     - toc.follow
>     - search.suggest
>     - search.highlight
>     - search.share
>     - content.code.copy
>     - content.code.annotate
> ```
> 
> ## Tree-like toggles
> You already have a decent sidebar style in `extra.css`, but the actual nav behavior is still determined mostly by MkDocs Material’s nested nav plus your file structure. Your CSS is already styling section headers and nested page links in the sidebar. fileciteturn12file3
> 
> The biggest improvement is not more CSS tricks. It is:
> 
> ### fix the nav to match the new subfolder topology
> Once you point `mkdocs.yml` at the new nested paths, the sidebar will feel much more like a progressive tree because the structure itself is cleaner.
> 
> ---
> 
> # Markmind inside MkDocs
> 
> Yes, you can incorporate it.
> 
> ## Do not keep the current setup
> The current `markmind.html` is a static standalone page with hardcoded tree data. That is the wrong long-term model. fileciteturn12file0
> 
> ## Better model
> Generate the mind map from the actual repo/docs tree, then expose it inside MkDocs.
> 
> ### Best structure
> ```text id="7v3j79"
> scripts/generate_markmind.py
> docs/08_appendices/40_labs/markmind.md
> docs/assets/diagrams/markmind.html
> docs/assets/diagrams/markmind-data.json
> ```
> 
> ### `markmind.md`
> Embed it with an iframe:
> 
> ```markdown id="zjl1wi"
> # Markmind
> 
> <iframe src="../../assets/diagrams/markmind.html"
>         width="100%"
>         height="900"
>         style="border:none;border-radius:12px;"></iframe>
> ```
> 
> That is simple and stable.
> 
> ---
> 
> # How to auto-update Markmind
> 
> Do **not** use `main.py` for the whole job.
> 
> Why:
> The MkDocs Macros docs make clear that `define_env()` runs during config and is for macros/filters/variables, while post-build actions belong in hooks like `on_post_build`, or just a separate script if you want clean control. citeturn990021search0turn990021search3
> 
> ## Best practice
> Use a dedicated generator script:
> 
> ```text id="m74slo"
> scripts/generate_markmind.py
> ```
> 
> It should:
> 1. scan the current blueprint tree
> 2. output JSON tree data
> 3. write `docs/assets/diagrams/markmind-data.json`
> 4. write or update `docs/assets/diagrams/markmind.html` from a template that loads the JSON
> 
> That way the HTML shell stays stable and only the data refreshes.
> 
> ### Why this is better
> - cleaner separation
> - easier debugging
> - no hardcoded stale tree
> - works before `mkdocs build`
> - easy to call from `rebuild.bat`
> 
> ---
> 
> # What to do with `main.py`
> 
> ## Keep it, but upgrade it
> Current use is fine, but it should evolve into:
> - registry render helpers
> - standards render helpers
> - maybe reusable file loaders
> - maybe tree/nav helper macros for docs pages
> 
> ### Recommended next shape
> Either keep `main.py` for now, or convert it into a package, which the MkDocs Macros docs explicitly support. They document that instead of a single file you can implement the local module as a package with `__init__.py`, or point `module_name` at a different module path. citeturn990021search0
> 
> If you want less root clutter later:
> 
> ```text id="br5txy"
> hooks/
>   mkdocs_macros/
>     __init__.py
>     registry.py
>     renderers.py
>     loaders.py
> ```
> 
> and then in `mkdocs.yml`:
> 
> ```yaml id="w509pl"
> plugins:
>   - search:
>       lang: en
>   - macros:
>       module_name: hooks/mkdocs_macros
> ```
> 
> That is a cleaner end state.
> 
> ---
> 
> # My recommended next file additions
> 
> ```text id="85bytk"
> scripts/
>   normalize_front_matter.py
>   enforce_structure.py
>   generate_markmind.py
>   update_indexes.py        # optional second pass
> rebuild.bat
> docs/08_appendices/40_labs/markmind.md
> docs/assets/diagrams/markmind-data.json
> docs/assets/diagrams/markmind.html
> ```
> 
> ---
> 
> # The order I’d do this in
> 
> 1. update `mkdocs.yml` to the new nested nav
> 2. add `rebuild.bat`
> 3. replace static `markmind.html` with generated data model
> 4. add `scripts/generate_markmind.py`
> 5. update `README.md`
> 6. expand `enforce_structure.py` to understand:
>    - section subfolders
>    - required section indexes
>    - maybe template presence
> 7. wire it all together in the batch file
> 
> ---
> 
> # Blunt call on the current files
> 
> - **`main.py`**: keep, but it is too small and underused right now fileciteturn12file2
> - **`mkdocs.yml`**: definitely needs rewriting because nav paths are now stale relative to your new tree fileciteturn12file1
> - **`markmind.html`**: current version should be treated as a prototype, not final architecture fileciteturn12file0
> - **`extra.css`**: already solid; not the priority over nav correctness fileciteturn12file3
> - **`enforce_structure.py`**: needs to become smarter or it will lag behind the doctrine again fileciteturn12file5
> 
> Send the README and the rebuilt tree export after you make the next pass, and I’ll do the double-check.

### User
> # 🌌 QiOS Master Blueprint

> 

> > **The Constitutional Source of Truth for the QiLabs Ecosystem.**

> 

> This repository serves as the definitive, machine-enforceable blueprint for the **QiOS** architecture. It governs the relationship between Core, Platform, and Domain bands, ensuring strict tenant isolation, data integrity, and a unified narrative ontology across all projects.

> 

> ---

> 

> ## 🏗️ Canonical Layers

> 

> The blueprint is organized into specialized layers of authority:

> 

> - **[`docs/`](docs/)**: The rendered doctrine. Human-readable architectural guides, policies, and system models.

> - **[`adr/`](adr/)**: **Architecture Decision Records**. The historical log of "Why" decisions were made, superseding or informing current states.

> - **[`standards/`](standards/)**: Technical specifications and mandatory constraints (e.g., Metadata Profile, Naming Rules).

> - **[`registry/`](registry/)**: The system's flat-file "Database of Truth" for domains, bands, and workspace realms.

> - **[`schemas/`](schemas/)**: JSON/YAML schemas used to validate the registry and structure.

> 

> ---

> 

> ## ⚡ Automation & Enforcement

> 

> The blueprint is not just documentation; it is **actively enforced** through a suite of Python-based utilities:

> 

> - **[`rebuild.bat`](rebuild.bat)**: The primary entry point. Runs normalization, structural enforcement, and site builds in sequence.

> - **`scripts/normalize_front_matter.py`**: Ensures all Markdown files adhere to the [Universal Metadata Profile](standards/content_metadata_profile.yaml).

> - **`scripts/enforce_structure.py`**: Validates the physical file tree against the `registry/` and `schemas/`.

> - **`scripts/generate_markmind.py`**: Automatically updates the visual `markmind.html` map based on the current navigation.

> 

> ---

> 

> ## 🛠️ Development & Publishing

> 

> ### Prerequisites

> - Python 3.10+

> - MKDocs with the Material theme (`pip install mkdocs-material`)

> 

> ### The Rebuild Loop

> 1. **Modify**: Update docs, standards, or registry files.

> 2. **Execute**: Run `rebuild.bat` from the root.

> 3. **Verify**: Check the terminal output for validation errors.

> 4. **View**: Launch `mkdocs serve` to preview the modern, Apple-slick documentation site locally.

> 

> ---

> 

> ## 🧭 Navigation Reference

> 

> | Section | Description |

> | :--- | :--- |

> | **01 Governance** | Constitutional laws, policy, and human-AI interaction rules. |

> | **02 Architecture** | Identity models, system components, and runtime zones. |

> | **03 Structure** | The 3-Band model, Domain rules, and Namespace/Object registries. |

> | **04 Data** | Schema definitions, Storage doctrine, and Metadata standards. |

> | **05 Compute** | Worker logic, API patterns, and Ingestion pipelines. |

> | **06 Applications** | Portal, Admin, and Tooling interfaces. |

> | **07 Operations** | Client management, Case workflows, and Financial services. |

> 

> ---

> 

> ## ⚠️ Troubleshooting

> 

> - **Validation Fails**: If `enforce_structure.py` errors, check that your new files are registered in the appropriate `registry/*.yaml` file.

> - **Front Matter Drift**: Run the normalization script with the `--check` flag to identify files violating the metadata standard.

> - **Theme Issues**: Custom CSS is located in `stylesheets/extra.css`. Ensure `mkdocs.yml` hasn't been corrupted.

> 

> ---

> *© 2026 QiLabs. All rights reserved. Internal Use Only.*

### Assistant
> The README is **close**, but it is a little ahead of the repo in a few places.
> 
> ## What’s good
> 
> It correctly frames the repo as:
> - constitutional source of truth
> - layered by `docs/`, `adr/`, `standards/`, `registry/`, `schemas`
> - automation-driven, not passive docs
> 
> That part is solid and aligned.
> 
> ## What is still off
> 
> Based on the current tree, a few things are inconsistent or unfinished:
> 
> - you still have **`main.py` and `hooks/` together**, which means the macro/hook architecture is not settled yet fileciteturn13file0
> - you still have a **duplicate root `markmind.html`** while also having `docs/assets/diagrams/markmind.html` and `markmind-data.json` fileciteturn13file0
> - templates are still `tmp_*`, which means the template system is not actually finalized yet fileciteturn13file0
> - `07_operations/40_services/products.md` is still misnamed in the tree you exported; that folder should be `40_products/` if products are the concept being documented fileciteturn13file0
> - your README says `rebuild.bat` is the primary entry point, which is fine, but the repo still has both `rebuild.bat` and `scripts/normalize_front_matter.bat`, so the command surface is still a little messy fileciteturn13file0
> 
> ## Biggest architectural decision still not locked
> 
> You need to choose **one** of these:
> 
> ### Option A
> Keep `main.py` as the MkDocs macros entrypoint.
> 
> ### Option B
> Move fully to `hooks/` and configure MkDocs to use that module path.
> 
> Right now the repo looks like it is trying to do both. That is drift.
> 
> My recommendation: **move fully to `hooks/`** and kill root `main.py` once the config is updated.
> 
> ## README changes I would make
> 
> ### 1. Change this section
> Current:
> 
> > **`rebuild.bat`**: The primary entry point. Runs normalization, structural enforcement, and site builds in sequence.
> 
> Better:
> 
> ```md
> - **[`rebuild.bat`](rebuild.bat)**: The primary operator entry point. Runs front matter normalization, structure enforcement, generated artifact refresh (indexes / markmind), local MkDocs build validation, and Git publish steps in sequence.
> ```
> 
> Because “site builds in sequence” is too vague.
> 
> ### 2. Fix prerequisites
> Right now it only mentions MkDocs Material. That is incomplete.
> 
> You also need:
> - `mkdocs-macros-plugin`
> - Python deps used by your scripts
> - Git in PATH
> - probably `jsonschema` and `pyyaml`
> 
> ### 3. Remove fluffy phrasing
> This line:
> 
> > preview the modern, Apple-slick documentation site locally
> 
> Cut it. It sounds like marketing copy, not repo ops documentation.
> 
> ### 4. Add one section called `Current Automation Flow`
> Explicit step list:
> 1. normalize front matter
> 2. validate structure
> 3. regenerate markmind / indexes
> 4. build MkDocs
> 5. add / commit / push
> 
> That makes the rebuild contract explicit.
> 
> ### 5. Add one section called `Runtime Files`
> Explain:
> - `mkdocs.yml`
> - `hooks/` or `main.py`
> - `scripts/`
> - `docs/assets/diagrams/markmind.*`
> 
> Because right now a new reader will still ask “what is `main.py`?” just like you did.
> 
> ## Tree cleanup I would do before the next export
> 
> ### Remove or resolve
> - root `markmind.html`
> - one of `main.py` or `hooks/`
> - `scripts/normalize_front_matter.bat` if `rebuild.bat` replaces it
> - all `tmp_*` template names
> 
> ### Rename
> - `07_operations/40_services/` → `07_operations/40_products/`
> - `ADR-0007-unified-front-matter-and-progressive-doc-topology.md` → use the same filename style as the rest of your ADRs
> 
> ### Keep
> - `docs/assets/diagrams/markmind.html`
> - `docs/assets/diagrams/markmind-data.json`
> - `scripts/generate_markmind.py`
> - `scripts/update_indexes.py`
> - `rebuild.bat`
> 
> ## Blunt verdict
> 
> The README is **good enough to keep**, but it is describing the repo as if the automation and template cleanup are already finished.
> 
> They are not.
> 
> So I would:
> 1. clean the tree
> 2. settle `main.py` vs `hooks/`
> 3. rename the templates
> 4. then tighten the README to match reality exactly
> 
> If you want, send `rebuild.bat` next and I’ll tell you exactly what should be in it and what should be removed.

### User
> i want option b and you need to give me the updated markmind code, and the code for the others you have me create but did not give me the code.

### Assistant
> I’m locking the actual implementation path now: remove `main.py`, move fully to `hooks/`, wire MkDocs to that module, and make Markmind generated instead of hand-edited. Then I’ll hand you the full code blocks so you can paste them directly.

### Assistant
> Good. **Option B is the right move.** Your current tree still has both `hooks/` and `main.py`, plus a duplicate root `markmind.html`, so the hook architecture is not fully settled yet. fileciteturn13file0 Your current `main.py` is only acting as the MkDocs Macros entrypoint with two simple macros, so it is safe to replace with a proper package-based hook module. fileciteturn12file2 The macros plugin supports using a custom `module_name` path and also supports implementing the module as a package directory instead of a single `main.py` file. citeturn159120search0turn159120search1
> 
> Also, your current `markmind.html` is hardcoded with stale `rawData`, so it needs to become generated. fileciteturn12file0
> 
> ## First: remove these after you switch
> - `main.py`
> - root `markmind.html`
> - `scripts/normalize_front_matter.bat` if `rebuild.bat` becomes the only operator entrypoint
> 
> Your tree shows all three are still present. fileciteturn13file0
> 
> ---
> 
> # 1) `mkdocs.yml`
> 
> Replace your current file with this. It switches fully to `hooks/`, updates the nav to the new nested doc structure, and adds the Markmind page. Your current nav is still flat and outdated relative to the new folder structure. fileciteturn12file1
> 
> ```yaml
> site_name: QiOS Master Blueprint
> site_description: Canonical architecture and governance blueprint for the Qi ecosystem
> site_url: https://qiallyme.github.io/__QiOS_Master_Blueprint_v0.4/
> copyright: "QiOS © 2026 — Canonical"
> 
> theme:
>   name: material
>   custom_dir: overrides
>   palette:
>     - scheme: default
>       primary: custom
>       accent: custom
>       toggle:
>         icon: material/weather-night
>         name: Switch to dark mode
>     - scheme: slate
>       primary: custom
>       accent: custom
>       toggle:
>         icon: material/weather-sunny
>         name: Switch to light mode
>   font:
>     text: Inter
>     code: JetBrains Mono
>   features:
>     - navigation.instant
>     - navigation.sections
>     - navigation.indexes
>     - navigation.expand
>     - navigation.top
>     - navigation.footer
>     - search.suggest
>     - search.highlight
>     - search.share
>     - content.code.copy
>     - content.code.annotate
>     - toc.follow
>   icon:
>     logo: material/layers-outline
>     repo: fontawesome/brands/github
> 
> extra_css:
>   - stylesheets/extra.css
> 
> extra:
>   social:
>     - icon: fontawesome/brands/github
>       link: https://github.com/qiallyme/__QiOS_Master_Blueprint_v0.4
> 
> markdown_extensions:
>   - admonition
>   - pymdownx.details
>   - pymdownx.superfences:
>       custom_fences:
>         - name: mermaid
>           class: mermaid
>           format: !!python/name:pymdownx.superfences.fence_code_format
>   - pymdownx.highlight:
>       anchor_linenums: true
>   - pymdownx.inlinehilite
>   - pymdownx.snippets
>   - pymdownx.tabbed:
>       alternate_style: true
>   - attr_list
>   - md_in_html
>   - tables
>   - toc:
>       permalink: true
> 
> plugins:
>   - search:
>       lang: en
>   - macros:
>       module_name: hooks
> 
> nav:
>   - Home: index.md
> 
>   - Genesis:
>       - Overview: 00_genesis/index.md
> 
>   - Governance:
>       - Overview: 01_governance/index.md
>       - Foundation:
>           - Principles: 01_governance/10_foundation/principles.md
>       - Policy:
>           - Agent Rules: 01_governance/20_policy/agent_rules.md
>           - Policies: 01_governance/20_policy/policies.md
>       - Standards:
>           - Overview: 01_governance/30_standards/standards.md
>           - Metadata Policy: 01_governance/30_standards/metadata_policy.md
>           - Templates Policy: 01_governance/30_standards/templates_policy.md
>       - Registry:
>           - Registry Overview: 01_governance/40_registry/registry.md
>       - Decisions:
>           - Decisions Index: 01_governance/50_decisions/decisions.md
> 
>   - Architecture:
>       - Overview: 02_architecture/index.md
>       - Identity:
>           - Identity: 02_architecture/10_identity/identity.md
>       - System:
>           - System Model: 02_architecture/20_system/system_model.md
>           - Component Map: 02_architecture/20_system/component_map.md
>       - Runtime:
>           - Device Model: 02_architecture/30_runtime/device_model.md
>           - Runtime Zones: 02_architecture/30_runtime/runtime_zones.md
>           - Service Boundaries: 02_architecture/30_runtime/service_boundaries.md
>       - Flows:
>           - Data Flow: 02_architecture/40_flows/data_flow.md
> 
>   - Structure:
>       - Overview: 03_structure/index.md
>       - Bands:
>           - Bands: 03_structure/10_bands/bands.md
>       - Domains:
>           - Domains: 03_structure/20_domains/domains.md
>       - Namespaces:
>           - Namespace Registry: 03_structure/30_namespaces/namespace_registry.md
>           - Subdomains: 03_structure/30_namespaces/subdomains.md
>       - Objects:
>           - Directory Tree: 03_structure/40_objects/directory_tree.md
>           - Object Model: 03_structure/40_objects/object_model.md
>           - Placement Rules: 03_structure/40_objects/placement_rules.md
> 
>   - Data:
>       - Overview: 04_data/index.md
>       - Schema:
>           - Front Matter: 04_data/10_schema/front_matter.md
>           - Objects: 04_data/10_schema/objects.md
>           - Schema: 04_data/10_schema/schema.md
>       - Metadata:
>           - Metadata: 04_data/20_metadata/metadata.md
>       - Storage:
>           - Storage: 04_data/30_storage/storage.md
>           - Exports: 04_data/30_storage/exports.md
>       - Domain Addenda:
>           - QiEvidence: 04_data/40_domain_addenda/qievidence.md
> 
>   - Compute:
>       - Overview: 05_compute/index.md
>       - APIs:
>           - APIs: 05_compute/10_apis/apis.md
>       - Workers:
>           - Workers: 05_compute/20_workers/workers.md
>       - Pipelines:
>           - Pipelines: 05_compute/30_pipelines/pipelines.md
>       - Runtime:
>           - Runtime: 05_compute/40_runtime/runtime.md
>           - Tech Stack: 05_compute/40_runtime/tech_stack.md
>       - Integrations:
>           - Integrations: 05_compute/50_integrations/integrations.md
> 
>   - Applications:
>       - Overview: 06_applications/index.md
>       - Web:
>           - Web: 06_applications/10_web/web.md
>       - Portal:
>           - Portal: 06_applications/20_portal/portal.md
>       - Admin:
>           - Admin: 06_applications/30_admin/admin.md
>       - Tools:
>           - Tools: 06_applications/40_tools/tools.md
>       - Interfaces:
>           - Interfaces: 06_applications/50_interfaces/interfaces.md
> 
>   - Operations:
>       - Overview: 07_operations/index.md
>       - Clients:
>           - Clients: 07_operations/10_clients/clients.md
>       - Cases:
>           - Cases: 07_operations/20_cases/cases.md
>       - Finance:
>           - Finance: 07_operations/30_finance/finance.md
>       - Products:
>           - Products: 07_operations/40_products/products.md
>       - Templates:
>           - Templates: 07_operations/50_templates/templates.md
> 
>   - Appendices:
>       - Overview: 08_appendices/index.md
>       - Reference:
>           - Changelog: 08_appendices/10_reference/changelog.md
>           - Glossary: 08_appendices/10_reference/glossary.md
>           - Templates Catalog: 08_appendices/10_reference/templates_catalog.md
>       - Legacy:
>           - Legacy CSV Migration Plan: 08_appendices/20_legacy/legacy_csv_migration_plan.md
>           - Legacy Salvage: 08_appendices/20_legacy/legacy_salvage.md
>           - Migration Notes: 08_appendices/20_legacy/migration_notes.md
>       - Labs:
>           - Markmind: 08_appendices/40_labs/markmind.md
> ```
> 
> ---
> 
> # 2) `hooks/__init__.py`
> 
> ```python
> from pathlib import Path
> 
> from .loaders import load_json_file, load_text_file, load_yaml_file, resolve_repo_path
> from .registry import render_band_registry_table, render_domain_registry_table
> from .renderers import fenced_code_block, render_repo_tree
> 
> 
> def define_env(env):
>     repo_root = Path(env.project_dir).resolve()
> 
>     @env.macro
>     def read_yaml(path: str) -> str:
>         data = load_yaml_file(repo_root, path)
>         return fenced_code_block("yaml", data)
> 
>     @env.macro
>     def read_json(path: str) -> str:
>         data = load_json_file(repo_root, path)
>         return fenced_code_block("json", data)
> 
>     @env.macro
>     def read_text(path: str) -> str:
>         text = load_text_file(repo_root, path)
>         return fenced_code_block("", text)
> 
>     @env.macro
>     def render_band_registry(path: str = "registry/band_registry.yaml") -> str:
>         data = load_yaml_file(repo_root, path)
>         return render_band_registry_table(data)
> 
>     @env.macro
>     def render_domain_registry(path: str = "registry/domain_registry.yaml") -> str:
>         data = load_yaml_file(repo_root, path)
>         return render_domain_registry_table(data)
> 
>     @env.macro
>     def repo_tree(path: str = ".", max_depth: int = 3) -> str:
>         target = resolve_repo_path(repo_root, path)
>         return render_repo_tree(target, repo_root=repo_root, max_depth=max_depth)
> ```
> 
> ---
> 
> # 3) `hooks/loaders.py`
> 
> ```python
> import json
> from pathlib import Path
> 
> import yaml
> 
> 
> def resolve_repo_path(repo_root: Path, relative_path: str) -> Path:
>     path = (repo_root / relative_path).resolve()
>     if repo_root not in path.parents and path != repo_root:
>         raise ValueError(f"Path escapes repo root: {relative_path}")
>     if not path.exists():
>         raise FileNotFoundError(f"Missing file: {relative_path}")
>     return path
> 
> 
> def load_text_file(repo_root: Path, relative_path: str) -> str:
>     path = resolve_repo_path(repo_root, relative_path)
>     return path.read_text(encoding="utf-8")
> 
> 
> def load_yaml_file(repo_root: Path, relative_path: str):
>     path = resolve_repo_path(repo_root, relative_path)
>     with path.open("r", encoding="utf-8") as f:
>         return yaml.safe_load(f) or {}
> 
> 
> def load_json_file(repo_root: Path, relative_path: str):
>     path = resolve_repo_path(repo_root, relative_path)
>     with path.open("r", encoding="utf-8") as f:
>         return json.load(f)
> ```
> 
> ---
> 
> # 4) `hooks/registry.py`
> 
> ```python
> from typing import Iterable
> 
> 
> def _markdown_table(headers: list[str], rows: Iterable[list[str]]) -> str:
>     lines = [
>         "| " + " | ".join(headers) + " |",
>         "| " + " | ".join(["---"] * len(headers)) + " |",
>     ]
>     for row in rows:
>         lines.append("| " + " | ".join(row) + " |")
>     return "\n".join(lines)
> 
> 
> def render_band_registry_table(data: dict) -> str:
>     rows = []
>     for band in data.get("bands", []):
>         rows.append([
>             f"`{band.get('id', '')}`",
>             f"**{band.get('name', '')}**",
>             band.get("description", "").replace("\n", " ").strip(),
>             ", ".join(f"`{s}`" for s in band.get("schemas", [])),
>         ])
>     return _markdown_table(["ID", "Name", "Description", "Schemas"], rows)
> 
> 
> def render_domain_registry_table(data: dict) -> str:
>     rows = []
>     for domain in data.get("domains", []):
>         rows.append([
>             f"`{domain.get('schema', '')}`",
>             f"**{domain.get('name', '')}**",
>             f"`{domain.get('band', '')}`",
>             domain.get("status", ""),
>             ", ".join(f"`{t}`" for t in domain.get("tables", [])),
>         ])
>     return _markdown_table(["Schema", "Name", "Band", "Status", "Tables"], rows)
> ```
> 
> ---
> 
> # 5) `hooks/renderers.py`
> 
> ```python
> import json
> from pathlib import Path
> 
> 
> def fenced_code_block(language: str, value) -> str:
>     if isinstance(value, str):
>         text = value.rstrip()
>     else:
>         text = json.dumps(value, indent=2, ensure_ascii=False)
>     lang = language or ""
>     return f"```{lang}\n{text}\n```"
> 
> 
> def render_repo_tree(target: Path, repo_root: Path, max_depth: int = 3) -> str:
>     lines: list[str] = []
> 
>     def walk(path: Path, prefix: str = "", depth: int = 0):
>         if depth > max_depth:
>             return
> 
>         children = sorted(
>             path.iterdir(),
>             key=lambda p: (not p.is_dir(), p.name.lower())
>         )
> 
>         for idx, child in enumerate(children):
>             is_last = idx == len(children) - 1
>             connector = "└── " if is_last else "├── "
>             rel = child.relative_to(repo_root)
>             icon = "📂" if child.is_dir() else "📄"
>             lines.append(f"{prefix}{connector}{icon} {rel.name}")
> 
>             if child.is_dir():
>                 extension = "    " if is_last else "│   "
>                 walk(child, prefix + extension, depth + 1)
> 
>     root_label = f". 📂 {target.relative_to(repo_root) if target != repo_root else repo_root.name}"
>     lines.append(root_label)
>     walk(target, depth=1)
> 
>     return "```markdown\n" + "\n".join(lines) + "\n```"
> ```
> 
> ---
> 
> # 6) `scripts/generate_markmind.py`
> 
> This replaces the static hand-edited Markmind data source.
> 
> ```python
> #!/usr/bin/env python3
> from __future__ import annotations
> 
> import json
> from pathlib import Path
> from typing import Any
> 
> import yaml
> 
> 
> REPO_ROOT = Path(__file__).resolve().parents[1]
> MKDOCS_PATH = REPO_ROOT / "mkdocs.yml"
> OUTPUT_JSON = REPO_ROOT / "docs" / "assets" / "diagrams" / "markmind-data.json"
> 
> EXCLUDED_NAMES = {
>     ".git",
>     ".github",
>     ".obsidian",
>     ".venv",
>     "__pycache__",
>     "site",
>     "node_modules",
>     "dist",
>     "build",
> }
> 
> 
> def scan_directory(path: Path, max_depth: int = 3, depth: int = 0) -> dict[str, Any]:
>     node = {"name": path.name, "children": []}
>     if depth >= max_depth:
>         return node
> 
>     children = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
>     for child in children:
>         if child.name in EXCLUDED_NAMES:
>             continue
>         if child.is_dir():
>             node["children"].append(scan_directory(child, max_depth=max_depth, depth=depth + 1))
>         else:
>             node["children"].append({"name": child.name})
>     return node
> 
> 
> def load_mkdocs_nav() -> list:
>     with MKDOCS_PATH.open("r", encoding="utf-8") as f:
>         config = yaml.safe_load(f) or {}
>     return config.get("nav", [])
> 
> 
> def nav_entry_to_node(entry) -> dict[str, Any]:
>     if isinstance(entry, str):
>         return {"name": entry}
> 
>     if isinstance(entry, dict):
>         label, value = next(iter(entry.items()))
>         if isinstance(value, str):
>             return {"name": label, "path": value}
>         if isinstance(value, list):
>             return {
>                 "name": label,
>                 "children": [nav_entry_to_node(item) for item in value],
>             }
> 
>     return {"name": str(entry)}
> 
> 
> def build_docs_nav_node() -> dict[str, Any]:
>     nav = load_mkdocs_nav()
>     return {
>         "name": "docs (navigation)",
>         "children": [nav_entry_to_node(item) for item in nav],
>     }
> 
> 
> def build_root_tree() -> dict[str, Any]:
>     root = {"name": "_qios_master_blueprint", "children": []}
> 
>     top_level_entries = [
>         "README.md",
>         "mkdocs.yml",
>         "rebuild.bat",
>         "docs",
>         "adr",
>         "standards",
>         "registry",
>         "schemas",
>         "scripts",
>         "templates",
>         "hooks",
>         "overrides",
>         "stylesheets",
>     ]
> 
>     for name in top_level_entries:
>         path = REPO_ROOT / name
>         if not path.exists():
>             continue
> 
>         if name == "docs":
>             root["children"].append(build_docs_nav_node())
>         elif path.is_dir():
>             root["children"].append(scan_directory(path, max_depth=2))
>         else:
>             root["children"].append({"name": name})
> 
>     return root
> 
> 
> def main() -> int:
>     OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
>     data = build_root_tree()
>     OUTPUT_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
>     print(f"WROTE: {OUTPUT_JSON}")
>     return 0
> 
> 
> if __name__ == "__main__":
>     raise SystemExit(main())
> ```
> 
> ---
> 
> # 7) `docs/assets/diagrams/markmind.html`
> 
> This replaces the hardcoded stale version. Your current one embeds old static `rawData` directly in the file. fileciteturn12file0
> 
> ```html
> <!DOCTYPE html>
> <html lang="en">
> <head>
>   <meta charset="UTF-8" />
>   <title>QiOS Master Blueprint — Markmind</title>
>   <meta name="viewport" content="width=device-width, initial-scale=1" />
>   <style>
>     html, body {
>       margin: 0;
>       padding: 0;
>       width: 100%;
>       height: 100%;
>       overflow: hidden;
>       background: #0f172a;
>       font-family: Inter, system-ui, sans-serif;
>       color: #e2e8f0;
>     }
> 
>     #mindmap {
>       width: 100vw;
>       height: 100vh;
>       display: block;
>       background:
>         radial-gradient(circle at top left, rgba(99, 102, 241, 0.18), transparent 35%),
>         radial-gradient(circle at bottom right, rgba(16, 185, 129, 0.16), transparent 30%),
>         #0f172a;
>     }
> 
>     .controls {
>       position: absolute;
>       right: 16px;
>       bottom: 16px;
>       z-index: 10;
>       padding: 10px 12px;
>       border-radius: 12px;
>       background: rgba(15, 23, 42, 0.72);
>       border: 1px solid rgba(148, 163, 184, 0.2);
>       color: #cbd5e1;
>       font-size: 12px;
>       backdrop-filter: blur(10px);
>     }
>   </style>
> </head>
> <body>
>   <svg id="mindmap"></svg>
>   <div class="controls">Scroll to zoom · Drag to pan · Click nodes to expand</div>
> 
>   <script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
>   <script src="https://cdn.jsdelivr.net/npm/markmap-view"></script>
>   <script>
>     function transformData(node) {
>       return {
>         content: `<strong>${node.name}</strong>`,
>         children: node.children ? node.children.map(transformData) : []
>       };
>     }
> 
>     async function init() {
>       const res = await fetch("./markmind-data.json");
>       if (!res.ok) throw new Error(`Failed to load markmind-data.json (${res.status})`);
>       const rawData = await res.json();
> 
>       const { Markmap } = window.markmap;
>       const data = transformData(rawData);
> 
>       Markmap.create("#mindmap", {
>         autoFit: true,
>         duration: 350,
>         nodeMinHeight: 16,
>         spacingVertical: 10,
>         spacingHorizontal: 80,
>         paddingX: 16,
>         color: (node) => {
>           const colors = ["#10b981", "#6366f1", "#38bdf8", "#f59e0b", "#f472b6"];
>           return colors[node.depth % colors.length];
>         }
>       }, data);
>     }
> 
>     init().catch((err) => {
>       console.error(err);
>       document.body.insertAdjacentHTML(
>         "beforeend",
>         `<div style="position:absolute;top:16px;left:16px;padding:12px 14px;background:#7f1d1d;color:#fee2e2;border-radius:10px;font-size:13px;">
>           Markmind failed to load: ${err.message}
>         </div>`
>       );
>     });
>   </script>
> </body>
> </html>
> ```
> 
> ---
> 
> # 8) `docs/08_appendices/40_labs/markmind.md`
> 
> ```markdown
> ---
> layout: "page"
> title: "Markmind"
> slug: "markmind"
> summary: "Visual map of the current blueprint structure and navigation."
> status: "active"
> 
> created_at: "2026-04-01"
> updated_at: "2026-04-01"
> author: "System"
> owner: "Cody"
> 
> sensitivity: "internal"
> classification: "business_internal"
> realm_label: ""
> 
> context: "Generated visualization for blueprint navigation and structure."
> aliases: []
> tags: ["visualization", "navigation", "markmind"]
> keywords: ["markmind", "mind map", "blueprint structure"]
> references: []
> 
> target_system: "QiOS Master Blueprint"
> target_scope: "docs/assets/diagrams"
> canonical_ref: ""
> 
> uid: ""
> template_key: "page_template"
> source_type: "generated"
> 
> adr_id: ""
> supersedes: ""
> artifact_kind: ""
> registry_key: ""
> standard_key: ""
> ---
> 
> # Markmind
> 
> <iframe
>   src="../../assets/diagrams/markmind.html"
>   width="100%"
>   height="900"
>   style="border: none; border-radius: 12px; overflow: hidden;"
> ></iframe>
> ```
> 
> ---
> 
> # 9) `scripts/update_indexes.py`
> 
> This gives you the missing generated “indexes” step for the rebuild flow.
> 
> ```python
> #!/usr/bin/env python3
> from __future__ import annotations
> 
> import re
> from pathlib import Path
> 
> REPO_ROOT = Path(__file__).resolve().parents[1]
> ADR_DIR = REPO_ROOT / "adr"
> TEMPLATES_DIR = REPO_ROOT / "templates"
> 
> DECISIONS_MD = REPO_ROOT / "docs" / "01_governance" / "50_decisions" / "decisions.md"
> TEMPLATES_CATALOG_MD = REPO_ROOT / "docs" / "08_appendices" / "10_reference" / "templates_catalog.md"
> 
> 
> def read_text(path: Path) -> str:
>     return path.read_text(encoding="utf-8")
> 
> 
> def extract_heading(path: Path) -> str:
>     text = read_text(path)
>     for line in text.splitlines():
>       stripped = line.strip()
>       if stripped.startswith("# "):
>           return stripped[2:].strip()
>     return path.stem
> 
> 
> def list_adr_files() -> list[Path]:
>     return sorted(
>         [
>             p for p in ADR_DIR.glob("ADR-*.md")
>             if p.name != "ADR-0000_template.md"
>         ],
>         key=lambda p: p.name.lower()
>     )
> 
> 
> def list_template_files() -> list[Path]:
>     return sorted(
>         [
>             p for p in TEMPLATES_DIR.iterdir()
>             if p.is_file()
>             and p.suffix == ".md"
>             and p.name != "README.md"
>         ],
>         key=lambda p: p.name.lower()
>     )
> 
> 
> def render_decisions_md() -> str:
>     rows = []
>     for path in list_adr_files():
>         title = extract_heading(path)
>         rows.append(f"| `{path.name}` | {title} |")
> 
>     table = "\n".join(rows) if rows else "| _none_ | _none_ |"
> 
>     return f"""---
> layout: "page"
> title: "Decisions"
> slug: "decisions"
> summary: "Generated index of Architecture Decision Records."
> status: "active"
> 
> created_at: "2026-04-01"
> updated_at: "2026-04-01"
> author: "System"
> owner: "Cody"
> 
> sensitivity: "internal"
> classification: "business_internal"
> realm_label: ""
> 
> context: "Generated from the adr/ directory."
> aliases: []
> tags: ["adr", "decisions", "governance"]
> keywords: ["ADR", "architectural decision records", "governance"]
> references: []
> 
> target_system: "QiOS Master Blueprint"
> target_scope: "adr"
> canonical_ref: ""
> 
> uid: ""
> template_key: "page_template"
> source_type: "generated"
> 
> adr_id: ""
> supersedes: ""
> artifact_kind: ""
> registry_key: ""
> standard_key: ""
> ---
> 
> # Decisions
> 
> Architectural Decision Records (ADRs) capture **why** decisions were made, not just what was decided.
> 
> ## ADR Index
> 
> | File | Title |
> | --- | --- |
> {table}
> """
> 
> 
> def render_templates_catalog_md() -> str:
>     items = []
>     for path in list_template_files():
>         title = path.stem.replace("_", " ").replace("-", " ").title()
>         items.append(f"| `{path.name}` | {title} |")
> 
>     table = "\n".join(items) if items else "| _none_ | _none_ |"
> 
>     return f"""---
> layout: "page"
> title: "Templates Catalog"
> slug: "templates-catalog"
> summary: "Generated catalog of blueprint templates."
> status: "active"
> 
> created_at: "2026-04-01"
> updated_at: "2026-04-01"
> author: "System"
> owner: "Cody"
> 
> sensitivity: "internal"
> classification: "business_internal"
> realm_label: ""
> 
> context: "Generated from the templates/ directory."
> aliases: []
> tags: ["templates", "catalog"]
> keywords: ["templates", "blueprint templates"]
> references: []
> 
> target_system: "QiOS Master Blueprint"
> target_scope: "templates"
> canonical_ref: ""
> 
> uid: ""
> template_key: "page_template"
> source_type: "generated"
> 
> adr_id: ""
> supersedes: ""
> artifact_kind: ""
> registry_key: ""
> standard_key: ""
> ---
> 
> # Templates Catalog
> 
> This page is generated from the `templates/` directory.
> 
> ## Available Templates
> 
> | File | Template |
> | --- | --- |
> {table}
> """
> 
> 
> def main() -> int:
>     DECISIONS_MD.parent.mkdir(parents=True, exist_ok=True)
>     TEMPLATES_CATALOG_MD.parent.mkdir(parents=True, exist_ok=True)
> 
>     DECISIONS_MD.write_text(render_decisions_md(), encoding="utf-8")
>     TEMPLATES_CATALOG_MD.write_text(render_templates_catalog_md(), encoding="utf-8")
> 
>     print(f"WROTE: {DECISIONS_MD}")
>     print(f"WROTE: {TEMPLATES_CATALOG_MD}")
>     return 0
> 
> 
> if __name__ == "__main__":
>     raise SystemExit(main())
> ```
> 
> ---
> 
> # 10) `scripts/enforce_structure.py`
> 
> Your current one only checks the old top-level section folders and one schema validation. fileciteturn12file5 This version matches the new topology and the Option B hook setup.
> 
> ```python
> #!/usr/bin/env python3
> from __future__ import annotations
> 
> import json
> from pathlib import Path
> 
> import jsonschema
> import yaml
> 
> 
> REPO_ROOT = Path(__file__).resolve().parents[1]
> DOCS_DIR = REPO_ROOT / "docs"
> 
> 
> REQUIRED_ROOTS = [
>     "docs",
>     "adr",
>     "standards",
>     "registry",
>     "schemas",
>     "scripts",
>     "templates",
>     "hooks",
>     "overrides",
>     "stylesheets",
> ]
> 
> REQUIRED_DOC_SECTIONS = [
>     "00_genesis",
>     "01_governance",
>     "02_architecture",
>     "03_structure",
>     "04_data",
>     "05_compute",
>     "06_applications",
>     "07_operations",
>     "08_appendices",
> ]
> 
> REQUIRED_FILES = [
>     "mkdocs.yml",
>     "rebuild.bat",
>     "standards/content_metadata_profile.yaml",
>     "standards/metadata_rules.yaml",
>     "standards/naming_rules.yaml",
>     "standards/repo_rules.yaml",
>     "hooks/__init__.py",
>     "scripts/normalize_front_matter.py",
>     "scripts/generate_markmind.py",
>     "scripts/update_indexes.py",
>     "docs/assets/diagrams/markmind.html",
>     "docs/assets/diagrams/markmind-data.json",
>     "docs/08_appendices/40_labs/markmind.md",
> ]
> 
> 
> def load_yaml(path: Path):
>     with path.open("r", encoding="utf-8") as f:
>         return yaml.safe_load(f) or {}
> 
> 
> def load_json(path: Path):
>     with path.open("r", encoding="utf-8") as f:
>         return json.load(f)
> 
> 
> def validate_schema(yaml_path: Path, schema_path: Path) -> tuple[bool, str]:
>     if not yaml_path.exists():
>         return False, f"missing YAML file: {yaml_path.relative_to(REPO_ROOT)}"
>     if not schema_path.exists():
>         return False, f"missing schema file: {schema_path.relative_to(REPO_ROOT)}"
> 
>     data = load_yaml(yaml_path)
>     schema = load_json(schema_path)
> 
>     try:
>         jsonschema.validate(instance=data, schema=schema)
>         return True, f"PASS schema: {yaml_path.relative_to(REPO_ROOT)}"
>     except jsonschema.exceptions.ValidationError as e:
>         return False, f"FAIL schema: {yaml_path.relative_to(REPO_ROOT)} — {e.message}"
> 
> 
> def check_required_roots() -> list[str]:
>     messages = []
>     for root_name in REQUIRED_ROOTS:
>         path = REPO_ROOT / root_name
>         if not path.exists():
>             messages.append(f"FAIL root missing: {root_name}")
>         else:
>             messages.append(f"PASS root: {root_name}")
>     return messages
> 
> 
> def check_required_files() -> list[str]:
>     messages = []
>     for rel in REQUIRED_FILES:
>         path = REPO_ROOT / rel
>         if not path.exists():
>             messages.append(f"FAIL file missing: {rel}")
>         else:
>             messages.append(f"PASS file: {rel}")
>     return messages
> 
> 
> def check_docs_sections() -> list[str]:
>     messages = []
> 
>     if not (DOCS_DIR / "index.md").exists():
>         messages.append("FAIL docs/index.md missing")
>     else:
>         messages.append("PASS docs/index.md")
> 
>     for section in REQUIRED_DOC_SECTIONS:
>         section_path = DOCS_DIR / section
>         if not section_path.exists():
>             messages.append(f"FAIL docs section missing: {section}")
>             continue
> 
>         index_path = section_path / "index.md"
>         if not index_path.exists():
>             messages.append(f"FAIL section index missing: docs/{section}/index.md")
>         else:
>             messages.append(f"PASS section index: docs/{section}/index.md")
> 
>         for child in sorted(section_path.iterdir()):
>             if child.is_dir():
>                 if not child.name[:2].isdigit() or child.name[2] != "_":
>                     messages.append(
>                         f"FAIL subsection naming: docs/{section}/{child.name} "
>                         "(expected NN_name)"
>                     )
>                 else:
>                     messages.append(f"PASS subsection: docs/{section}/{child.name}")
> 
>     return messages
> 
> 
> def check_option_b_cleanup() -> list[str]:
>     messages = []
> 
>     if (REPO_ROOT / "main.py").exists():
>         messages.append("FAIL root main.py still exists; Option B expects hooks/ only")
>     else:
>         messages.append("PASS no root main.py")
> 
>     if (REPO_ROOT / "markmind.html").exists():
>         messages.append("FAIL root markmind.html still exists; use docs/assets/diagrams/markmind.html")
>     else:
>         messages.append("PASS no root markmind.html")
> 
>     return messages
> 
> 
> def main() -> int:
>     all_messages = []
>     failures = 0
> 
>     checks = []
>     checks.extend(check_required_roots())
>     checks.extend(check_required_files())
>     checks.extend(check_docs_sections())
>     checks.extend(check_option_b_cleanup())
> 
>     schema_ok, schema_msg = validate_schema(
>         REPO_ROOT / "registry" / "band_registry.yaml",
>         REPO_ROOT / "schemas" / "band_registry.schema.json",
>     )
>     checks.append(schema_msg)
> 
>     for msg in checks:
>         print(msg)
>         if msg.startswith("FAIL"):
>             failures += 1
> 
>     if not schema_ok:
>         failures += 1
> 
>     if failures:
>         print(f"\nFAILED: {failures} issue(s) found.")
>         return 1
> 
>     print("\nAll structure checks passed.")
>     return 0
> 
> 
> if __name__ == "__main__":
>     raise SystemExit(main())
> ```
> 
> ---
> 
> # 11) `rebuild.bat`
> 
> ```bat
> @echo off
> setlocal enabledelayedexpansion
> 
> echo ========================================
> echo QiOS Blueprint Rebuild
> echo ========================================
> 
> echo.
> echo [1/6] Normalize front matter...
> python scripts\normalize_front_matter.py docs adr templates
> if errorlevel 1 goto :fail
> 
> echo.
> echo [2/6] Update generated indexes...
> python scripts\update_indexes.py
> if errorlevel 1 goto :fail
> 
> echo.
> echo [3/6] Generate Markmind data...
> python scripts\generate_markmind.py
> if errorlevel 1 goto :fail
> 
> echo.
> echo [4/6] Enforce structure...
> python scripts\enforce_structure.py
> if errorlevel 1 goto :fail
> 
> echo.
> echo [5/6] Build MkDocs site...
> mkdocs build
> if errorlevel 1 goto :fail
> 
> echo.
> echo [6/6] Git add / commit / push...
> git add .
> 
> git diff --cached --quiet
> if %errorlevel%==0 (
>   echo No staged changes to commit.
>   goto :done
> )
> 
> for /f "tokens=1-3 delims=/ " %%a in ("%date%") do set TODAY=%%c-%%a-%%b
> git commit -m "docs: rebuild blueprint %TODAY%"
> if errorlevel 1 goto :fail
> 
> git push
> if errorlevel 1 goto :fail
> 
> :done
> echo.
> echo SUCCESS: Blueprint rebuilt and published.
> exit /b 0
> 
> :fail
> echo.
> echo FAILED: Blueprint rebuild halted.
> exit /b 1
> ```
> 
> ---
> 
> # 12) Rename these template files now
> 
> Your tree still shows `tmp_*` template filenames. fileciteturn13file0 Rename them to:
> 
> ```text
> tmp_adr_template.md                  -> adr_template.md
> tmp_appendix_template.md             -> appendix_template.md
> tmp_artifact_template.md             -> artifact_template.md
> tmp_note_template.md                 -> note_template.md
> tmp_operational_template.md          -> operational_template.md
> tmp_page_template.md                 -> page_template.md
> tmp_registry_reference_template.md   -> registry_reference_template.md
> tmp_section_index_template.md        -> section_index_template.md
> tmp_standard_template.md             -> standard_template.md
> tmp_section_folder/                  -> section_folder_template/
> ```
> 
> Also rename this folder in docs:
> 
> ```text
> docs/07_operations/40_services/ -> docs/07_operations/40_products/
> ```
> 
> Your current export still has `40_services/products.md`, which is structurally wrong for the actual subject matter. fileciteturn13file0
> 
> ---
> 
> # 13) Final cleanup after pasting these
> 
> Do these in this order:
> 
> 1. replace `mkdocs.yml`
> 2. create the `hooks/` files above
> 3. create `generate_markmind.py`, `update_indexes.py`, and updated `enforce_structure.py`
> 4. replace `docs/assets/diagrams/markmind.html`
> 5. add `docs/08_appendices/40_labs/markmind.md`
> 6. rename the template files
> 7. delete:
>    - `main.py`
>    - root `markmind.html`
>    - `scripts/normalize_front_matter.bat`
> 8. run `rebuild.bat`
> 
> If you send the next export after that, I’ll do the hard alignment pass against the final tree and config.
