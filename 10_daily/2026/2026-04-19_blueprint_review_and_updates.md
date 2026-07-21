---
layout: page
title: "Blueprint Review and Updates"
slug: "blueprint_review_and_updates"
created_at: "2026-04-19 07:45:07"
updated_at: "2026-07-18T11:03:14-04:00"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-006.json"
template_key: master-template
date: 2026-04-19
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69e4ce52-0e00-83ea-a154-bf9c9ff0d13e"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Blueprint Review and Updates

## Overview
- **Date**: 2026-04-19 07:45:07
- **Conversation ID**: `69e4ce52-0e00-83ea-a154-bf9c9ff0d13e`
- **Source**: `Chat-Export-28513-2026/conversations-006.json`

## Chat History

### User
> we need to make updats to this review the projects conversations and advise on what is now outdated or incorrect in this blueprint for correction.

### Assistant
> I’m comparing the blueprint against what you’ve actually locked in across the recent QiOne/QiArchive/QiServer/QiNote work. I’m not treating wishlist doctrine as truth if the stack decisions moved.

### Assistant
> I found the biggest drift already: the blueprint is internally contradicting itself on the runtime model. One part still says multi-tenant `tenant_id` everywhere, while ADR-0004 says current runtime is single-account with `owner_user_id`. That needs to be resolved first because it infects schema, RLS, docs, and app assumptions. fileciteturn3file0 fileciteturn3file3

### Assistant
> I reviewed the current export and compared it against the direction you’ve actually been taking in the recent QiOne/QiArchive/QiServer/QiNote conversations. The blunt answer: the blueprint is **not one thing right now**. It is a mix of current truth, near-term target state, and old overbuilt architecture. fileciteturn0file0
> 
> Here’s what is outdated or incorrect enough to correct now.
> 
> ## 1) The runtime model is still contradicting itself
> 
> This is the biggest problem.
> 
> Parts of the blueprint still describe the active runtime as **multi-tenant**, with `tenant_id`, `qione.tenants`, `qione.tenant_members`, and even `public.organizations` / `public.tenant_members`. fileciteturn3file2 fileciteturn3file3
> 
> But ADR-0004 says the current implementation is **single-account / user-scoped**, and that current domain records should use `owner_user_id`, with multi-tenancy deferred. fileciteturn3file0
> 
> That means the blueprint is presently lying to the implementer unless ADR-0004 is accepted and the rest of the docs are swept.
> 
> **Correction:**
> - Pick one active runtime model.
> - Based on your recent project work, the honest answer is: **current runtime = single-account modular mode**.
> - Move multi-tenant portal language to **future-state** only.
> - Replace active-runtime `tenant_id` rules with `owner_user_id` rules everywhere they still survive.
> 
> ## 2) The stack is still overdeclared and partially fictional as “current”
> 
> The export still presents Redis, Neo4j, and NocoDB as part of the active runtime stack, and the runtime env list still requires `REDIS_URL`. fileciteturn3file1 fileciteturn4file1
> 
> That does not match the practical direction from recent project work:
> - Supabase is real and central.
> - Cloudflare is a real architecture choice and is underrepresented.
> - Google Drive is part of the actual storage strategy.
> - Railway is more “specific utility host / n8n / maybe Postgres candidate,” not universal canon.
> - Neo4j and NocoDB have not shown up as real, current build lanes the way the blueprint implies.
> 
> **Correction:**
> Split stack docs into:
> - **Active stack**
> - **Deferred stack**
> - **Experimental/optional stack**
> 
> Right now, the blueprint keeps presenting optional infrastructure as if it’s already part of the committed build.
> 
> ## 3) Old Railway-first doctrine is still contaminating the architecture
> 
> The older blueprint/PDF still says things like:
> - “Why Railway-First”
> - canonical backend stack = Railway Postgres / Redis / Neo4j / NocoDB
> - first milestone flows into Railway Postgres/pgvector. fileciteturn4file8 fileciteturn4file5 fileciteturn4file7
> 
> That is stale.
> 
> The export partially corrects this by saying Supabase is canonical, but the old assumptions are still visibly embedded in the larger blueprint family. fileciteturn3file1
> 
> **Correction:**
> - Archive the Railway-first blueprint as **historical**.
> - Remove all “canonical backend stack = Railway…” language from anything still live.
> - Reframe Railway as a **selective deployment utility**, not doctrine.
> 
> ## 4) Repo topology is internally inconsistent and no longer trustworthy as “the” structure
> 
> The older blueprint says canonical top-level structure includes `/sites`, `/python_local`, and a transitional `/supabase`, and references “Railway services.” fileciteturn4file5 fileciteturn4file7
> 
> The current export’s system model says the canonical hierarchy is `/apps`, `/packages`, `/workers`, `/python_core`, `/docs`. fileciteturn2file0
> 
> That is a direct internal conflict.
> 
> Also, based on recent work, your real repo includes more nuanced reality: apps, experiments, Python tooling, scripts, infrastructure, and module-specific code that do not cleanly match one frozen diagram.
> 
> **Correction:**
> Make a clean distinction between:
> - **actual repo snapshot**
> - **approved target topology**
> - **legacy layout references**
> 
> Do not keep presenting one idealized tree as if it already matches reality.
> 
> ## 5) Windows-only path doctrine is now wrong as a universal rule
> 
> The blueprint still treats `C:/QiLabs` and `C:/QiLabs/QiData` as canonical roots, and runtime docs still anchor on Windows-style env/path assumptions. fileciteturn3file1 fileciteturn2file0
> 
> That made sense when everything centered on the local Windows workstation. It does **not** hold cleanly now that you have a real Ubuntu/Tailscale/Ollama server in play.
> 
> **Correction:**
> Change path doctrine to:
> - **logical root names**
> - OS-specific path mappings
> 
> Example:
> - `QILABS_HOME` = logical root
> - Windows mapping: `C:/QiLabs`
> - Linux mapping: `/opt/qilabs` or whatever you standardize on
> 
> Right now the blueprint acts like Windows is the ontology. It’s not.
> 
> ## 6) “System family” is mixing real modules with conceptual names
> 
> The architecture still lists `QiNode`, `QiHistory`, and `QiPortals / QiSuite` as if they are established system-family members alongside QiOne, QiArchive, and QiNote. fileciteturn4file1
> 
> That is too loose now.
> 
> From recent project work:
> - **QiOne** is real.
> - **QiArchive** is real.
> - **QiNote** is a real planned module, but still under development and near-term partially offset by external tooling.
> - `QiNode`, `QiHistory`, `QiPortals / QiSuite` read more like conceptual labels or future packaging than current locked systems.
> 
> **Correction:**
> Split system family into:
> - **Active systems**
> - **Planned modules**
> - **Conceptual/future labels**
> 
> Otherwise the blueprint keeps inflating its own maturity.
> 
> ## 7) The admin/control-plane story is overstated
> 
> The blueprint still carries a pretty heavy story around a Local Admin Control Plane, FastAPI local control server, status UI, hosted fleet orchestration, etc. fileciteturn4file8
> 
> Some of that may still be strategically valid, but based on recent conversations it is **not** the clean center of gravity anymore. Your actual motion has been more pragmatic:
> - direct Supabase apps
> - Cloudflare delivery
> - interim Zoho-based portal aggregation
> - local/server utilities where useful
> - avoiding extra moving parts when not needed
> 
> **Correction:**
> Reclassify the control plane as either:
> - **experimental infra pattern**, or
> - **phase-2 operations surface**
> 
> Do not present it as core current architecture unless you are actively building it right now.
> 
> ## 8) The blueprint underrepresents Cloudflare and overrepresents old app assumptions
> 
> Your recent project direction is Cloudflare-first for hosting/backend surfaces, but Cloudflare is barely carrying doctrine weight in the blueprint. Meanwhile the stack still references Next.js/FastAPI cloud components and older service assumptions. fileciteturn3file1
> 
> **Correction:**
> Add an explicit section for:
> - **Cloudflare role in delivery, edge access, and portal surfaces**
> - what belongs on Cloudflare vs Supabase vs local/server nodes
> 
> That choice is now strategic enough that it should be in doctrine, not just in chat history.
> 
> ## 9) “Filesystem truth” is too absolute for the stack you’re actually building
> 
> The registry still says `filesystem_truth: true` and `db_as_index: true`, meaning the filesystem is the truth of what exists and the DB indexes it. fileciteturn4file3
> 
> That is too rigid now that your actual storage strategy is mixed:
> - local node storage
> - Google Drive backbone
> - Paperless/QiArchive-related flows
> - cloud-hosted app metadata
> 
> **Correction:**
> Replace that with something closer to:
> - **file substrate truth may live in an approved storage layer**
> - **QiArchive / canonical DB registration is the governance truth for tracked objects**
> 
> Otherwise the blueprint keeps pretending everything bottoms out in a local filesystem, and that is no longer cleanly true.
> 
> ## 10) Some domains/components are being treated as live when they are really addenda or proposals
> 
> `qievidence` appears as a domain addendum with its own schema/tables, but it is not in the live domain registry. fileciteturn4file0 fileciteturn4file3
> 
> That is not fatal, but it needs labeling discipline.
> 
> **Correction:**
> Mark it clearly as:
> - **proposed domain addendum**
> - not live schema doctrine
> 
> Same treatment should apply anywhere else a planned module is described with more certainty than the current implementation justifies.
> 
> ## 11) There are smaller internal cleanup errors too
> 
> These are not strategic, but they make the blueprint look sloppy:
> 
> - Governance index says “the 10 founding rules,” while the principles doc says **7 founding principles**. fileciteturn2file0
> - `qilly.memory_embeddings` appears in component relationships instead of `qially.memory_embeddings`. fileciteturn2file0
> - Some docs still describe platform/band dependency logic in older multi-tenant language while others already softened that toward single-account mode. fileciteturn3file0 fileciteturn4file6
> 
> Those are easy fixes, but fix them.
> 
> ---
> 
> ## What I would mark as the priority correction order
> 
> **Priority 1**
> Resolve the active runtime model:
> - accept or reject ADR-0004
> - sweep `tenant_id` vs `owner_user_id`
> - move hosted multi-tenant language to future-state if deferred
> 
> **Priority 2**
> Replace fake-canonical stack claims with three buckets:
> - active
> - deferred
> - experimental
> 
> **Priority 3**
> Rewrite repo/path doctrine:
> - actual repo snapshot vs target topology
> - OS-agnostic path doctrine
> - Linux server reality included
> 
> **Priority 4**
> Demote conceptual systems and proposals:
> - QiNode
> - QiHistory
> - QiPortals / QiSuite
> - qievidence
> - NocoDB/Neo4j/Redis if not actively committed
> 
> ---
> 
> ## Bottom line
> 
> The blueprint’s strongest flaw right now is not that it is “wrong everywhere.” It is that it keeps mixing:
> - current truth
> - architectural aspiration
> - old design baggage
> 
> That is why it feels bloated and slippery.
> 
> The correction is not just editing facts. It is adding **status discipline** to the whole document:
> - **Active**
> - **Target**
> - **Future**
> - **Historical/archived**
> 
> That one move would clean up most of the confusion fast.
> 
> Next move should be a **file-by-file correction matrix** with: current statement, why it’s wrong, replacement text, and status label.

### User
> well based on our conversation today, we are no longer building this monolith rather we are going inward and concentrating on my conocial second brain ai so what stays and what goes, concentration is simplie life in service but safe and health and room to be creative. without adhd ensureing i can remember anything lol

### Assistant
> I’m narrowing this to a salvage pass, not a rebuild. Goal is to strip the blueprint down to the parts that still serve your actual direction: memory, safety, health, household stability, and creative output.

### Assistant
> Yes. That changes the blueprint a lot.
> 
> You are **not** building QiOS-as-ecosystem right now. You are building a **personal cognitive support system**: memory, grounding, safety, health, household stability, and creative output.
> 
> So the rule becomes:
> 
> **If it does not help Cody remember, stabilize, decide, or create, it goes.**
> 
> The good news: the blueprint already has one part worth keeping almost intact — the **Spine** idea: intake → register → extract → embed → retrieve. That still matches your second-brain direction exactly. The “Spine alive” milestone is still valid. The “Portals alive” / platform expansion stuff is not. fileciteturn5file3 fileciteturn5file5
> 
> ## What stays
> 
> ### 1. QiArchive stays
> Keep it.
> 
> This is the part that gives you:
> - stable identity
> - lineage
> - search continuity
> - deduping
> - trust in your own records
> 
> That matters for ADHD because if things are not stably captured, they may as well not exist. The blueprint is right that registration, lineage, and retrieval continuity are the backbone. fileciteturn5file3
> 
> **Keep QiArchive as:**
> - inbox for anything important
> - canonical file registry
> - OCR/extraction
> - embeddings
> - searchable archive
> 
> ### 2. QiNote / QiKnowledge stays
> Keep it, but make it the center.
> 
> The blueprint calls QiNote the local-first note and knowledge layer and qiknowledge the notes/writing domain. That is exactly the heart of the new direction. fileciteturn5file3 fileciteturn5file6
> 
> **This becomes your actual second brain**, not just “notes”:
> - daily capture
> - project notes
> - household operating memory
> - health logs
> - symptom logs
> - creative fragments
> - decisions
> - prompts to self
> - restart points
> 
> ### 3. QiAlly stays
> Keep it, but narrow it hard.
> 
> The blueprint describes `qially` as AI sessions + memory embeddings. That still belongs. fileciteturn5file1 fileciteturn5file6
> 
> But in the new model, QiAlly is **not** “AI platform.”
> It is:
> 
> - your retrieval assistant
> - your memory bridge
> - your pattern spotter
> - your grounded planner
> - your creative co-pilot
> 
> No big AI governance theater. Just useful cognition support.
> 
> ### 4. QiVault stays
> Keep it.
> 
> You still need a secure records home:
> - IDs
> - legal docs
> - medical docs
> - insurance
> - passwords/passkeys adjacent reference docs
> - household agreements
> - core personal records
> 
> The blueprint already treats `qivault` as secure docs. That still fits. fileciteturn5file2 fileciteturn5file6
> 
> ### 5. QiHome stays
> Keep it, but narrow it to real life support.
> 
> This one matters because your life is not abstract productivity. It is:
> - bills
> - groceries
> - pets
> - chores
> - home setup
> - appointments
> - maintenance
> - who handles what
> 
> The blueprint’s `qihome` as household/finance still fits, but only as a support module, not a giant domain. fileciteturn5file2 fileciteturn5file6
> 
> ### 6. Safety / health / symptom tracking stays
> This is not a vanity add-on. It is part of the new center.
> 
> There is no perfect existing blueprint module for this except maybe health-oriented namespace doctrine and pieces of Chronicle/Home/Knowledge. That means for now:
> - keep the **function**
> - do **not** keep a bloated dedicated architecture
> 
> Make this a practical layer inside QiNote + QiVault + QiHome first.
> 
> ---
> 
> ## What goes
> 
> ### 1. QiOne as monorepo centerpiece goes
> This is the biggest cut.
> 
> The blueprint still frames QiOne as the primary implementation platform and monorepo. That is not your current priority anymore. fileciteturn5file3
> 
> You do not need to organize your life around a future software company architecture.
> That is overhead.
> It is also bait for ADHD spiraling into system design instead of support.
> 
> **QiOne stops being the center.**
> At most it becomes:
> - a repo/container name
> - a later shell
> - not the product you are actively optimizing now
> 
> ### 2. Multi-tenant platform architecture goes
> Kill it from active scope.
> 
> The blueprint still spends a ton of energy on:
> - `qione.tenants`
> - `tenant_members`
> - `member_roles`
> - portal modules
> - platform RBAC
> - multi-tenant identity design fileciteturn5file2 fileciteturn5file7
> 
> That is not your life right now.
> That is startup architecture cosplay.
> 
> You need **one trusted user system for you**, maybe with selective household sharing later. Not tenant doctrine.
> 
> ### 3. Portal / client delivery layer goes
> Cut it.
> 
> The blueprint’s portal/admin/web layers are about delivery surfaces, tenants, modules, onboarding, admin dashboards, etc. fileciteturn5file2 fileciteturn5file8
> 
> That is not what you need to survive and function.
> You need:
> - capture
> - retrieval
> - structure
> - reminders
> - secure storage
> - easy review
> 
> Not a portal stack.
> 
> ### 4. Admin control plane goes
> Cut it from active scope.
> 
> The FastAPI local control server, status UI, local admin control plane, fleet concepts — all of that is too much unless it is directly necessary for file ingest. fileciteturn5file2 fileciteturn5file8
> 
> Keep only the invisible pieces required to:
> - watch an inbox
> - process files
> - surface errors
> 
> No separate “operator dashboard” unless the lack of one is actually blocking use.
> 
> ### 5. qicase, qitax, qicms, products, templates go
> These are not your center anymore.
> 
> They may matter later, but they are not part of the simplified second-brain core.
> 
> So:
> - `qicase` = park
> - `qitax` = park
> - `qicms` = park
> - products/templates = cut entirely from active blueprint
> 
> If needed, their docs live in Vault/Archive as records, not as active architecture.
> 
> ### 6. qigraph goes from active to optional
> This is important.
> 
> The blueprint keeps graph projection in the core stack. fileciteturn5file1 fileciteturn5file6
> 
> For your actual use case, a graph is nice, not required.
> You do **not** need graph complexity to get value from:
> - good notes
> - good tags
> - linked records
> - embeddings
> - reliable search
> 
> So:
> - **active scope:** no graph dependency
> - **future optional:** qigraph if recall actually needs it
> 
> ### 7. qisys gets demoted
> Do not delete the concept. Shrink it.
> 
> You still need jobs/workers/events in some form.
> But it should be an internal plumbing bucket, not a first-class product area.
> 
> So:
> - keep background jobs
> - kill the grand orchestration language
> 
> ---
> 
> ## What gets folded instead of kept as its own domain
> 
> ### QiChronicle gets folded into the second brain
> Do not keep a separate timeline/event platform right now.
> 
> Instead fold it into:
> - daily note
> - memory timeline
> - symptom log
> - important life events
> - appointments and reminders
> 
> ### QiEvidence gets folded, not expanded
> This is the smart move.
> 
> QiEvidence is powerful, but as a whole standalone domain it is too much right now. The blueprint treats it like a serious evidence intelligence engine. fileciteturn4file0
> 
> You do not need a separate evidence platform today.
> You need:
> - reliable storage of photos/videos/docs
> - OCR/transcription when useful
> - extraction
> - timelines when necessary
> 
> So make it a **mode** inside Archive/Vault, not its own domain.
> 
> ---
> 
> ## The new center
> 
> Your blueprint should stop being “QiOS operating system for everything.”
> 
> It should become something more like this:
> 
> ## QiCore Personal System
> **Purpose:** reduce cognitive load, preserve memory, support safety and health, stabilize home operations, and protect creative space.
> 
> ### Core modules
> - **Archive** — capture and register everything important
> - **Note** — think, remember, reflect, organize
> - **Ally** — ask, retrieve, summarize, restart
> - **Vault** — secure records
> - **Home** — routines, bills, groceries, tasks, contacts
> - **Health** — logs, symptoms, meds, appointments, red flags
> - **Studio** — creative ideas, drafts, story fragments, concepts
> 
> That’s it.
> 
> Not 12 schemas.
> Not tenants.
> Not platform RBAC.
> Not an app empire.
> 
> ---
> 
> ## Best keep / go / park map
> 
> ### Keep now
> - QiArchive
> - QiNote / qiknowledge
> - QiAlly
> - QiVault
> - QiHome
> - symptom / health tracking
> - local-first capture and retrieval
> - spine doctrine
> 
> ### Park for later
> - qigraph
> - qievidence as separate domain
> - qichronicle as separate domain
> - cloud-heavy orchestration
> - public web/docs polish
> - selective sharing / household access
> 
> ### Remove from active blueprint
> - qione as platform center
> - tenants / tenant_members / member_roles
> - portal modules
> - admin surface as product area
> - client delivery model
> - qicase
> - qitax
> - qicms
> - products
> - templates
> - fleet/device empire language
> 
> ---
> 
> ## The ADHD-safe rule set
> 
> This part matters most.
> 
> Your system should do four things well:
> 
> 1. **Catch it fast**
>    - voice note
>    - quick note
>    - file drop
>    - simple inbox
> 
> 2. **Store it once**
>    - one canonical place
>    - one naming rule
>    - one retrieval path
> 
> 3. **Bring it back when needed**
>    - search
>    - summaries
>    - restart prompts
>    - “what was I doing?”
> 
> 4. **Reduce active remembering**
>    - checklists
>    - routines
>    - decision logs
>    - reminders
>    - weekly review
>    - household references
> 
> If a feature does not help one of those four, it is probably noise.
> 
> ---
> 
> ## My clean recommendation
> 
> Rewrite the blueprint around this sentence:
> 
> **QiOS is no longer an ecosystem blueprint first. It is Cody’s local-first cognitive support system for memory, safety, health, home stability, and creative work.**
> 
> Everything else becomes secondary.
> 
> So the official answer is:
> 
> - **Keep the Spine**
> - **Keep Archive, Note, Ally, Vault, Home**
> - **Fold health and creativity into the core**
> - **Demote or kill platform/tenant/portal/admin complexity**
> - **Stop designing for scale before designing for relief**
> 
> That is the right move.
> 
> I can turn this into a **replacement “v0.5 simplified blueprint direction” section** you can paste straight into the doc.
