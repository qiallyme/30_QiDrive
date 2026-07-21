---
layout: page
title: "QIDs and QiNote Vault"
slug: "qids_and_qinote_vault"
created_at: "2026-01-07 19:57:22"
updated_at: "2026-07-18T11:03:13-04:00"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-003.json"
template_key: master-template
date: 2026-01-07
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "695f0ef4-fe24-832c-be60-6ac39904383b"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# QIDs and QiNote Vault

## Overview
- **Date**: 2026-01-07 19:57:22
- **Conversation ID**: `695f0ef4-fe24-832c-be60-6ac39904383b`
- **Source**: `Chat-Export-28513-2026/conversations-003.json`

## Chat History

### User
> quick question do we apply qids to the cononical storage or just to the actual modules in teh qinote vault

### Assistant
> Short answer: **QIDs apply to the actual modules in the QiNote vault — not the canonical storage.**
> 
> Here’s the clean rule set so you don’t second-guess this later.
> 
> ---
> 
> ## The Correct Model (Don’t Deviate)
> 
> ### 1. Canonical Storage = **Dumb, Stable, ID-Free**
> Think of canonical storage as **cold truth**.
> 
> - Purpose: preservation, auditability, provenance
> - Characteristics:
>   - Raw
>   - Immutable (or append-only)
>   - Human-named, date-based, source-based
> - **No QIDs**
> - No semantic opinion
> - No re-numbering ever
> 
> Example:
> ```
> /Canonical/AES/2024-11-02_Bill_Statement.pdf
> /Canonical/Court/2025-01-09_Hearing_Transcript.pdf
> ```
> 
> If you put QIDs here, you **pollute the source of truth** and lock yourself into future refactors. Bad trade.
> 
> ---
> 
> ### 2. QiNote Vault Modules = **Semantic, Addressable, QID-Backed**
> QiNote is where meaning lives. Meaning requires identifiers.
> 
> - Purpose: reasoning, recall, linking, AI retrieval
> - Characteristics:
>   - Curated
>   - Interpreted
>   - Cross-linked
> - **QIDs REQUIRED**
> - QIDs are permanent once assigned
> 
> Example:
> ```
> QID-2.1.4_AES_Billing_Anomaly.md
> QID-5.3.2_Court_Hearing_Summary.md
> ```
> 
> These modules may:
> - Reference multiple canonical files
> - Be rewritten, merged, expanded
> - Outlive any single source document
> 
> That’s exactly why they need QIDs.
> 
> ---
> 
> ### 3. The One-Way Flow (This Matters)
> ```
> Canonical Storage
>    ↓ (reference only)
> QiNote Modules (QIDs live here)
>    ↓
> Derived outputs (briefs, exhibits, filings, posts)
> ```
> 
> Never reverse this.
> Never assign identity upstream.
> 
> ---
> 
> ## Hard Rule (Memorize This)
> > **Canonical storage answers: “What exists?”**  
> > **QiNote answers: “What does it mean?”**  
> > **Only meaning gets a QID.**
> 
> ---
> 
> ## Edge Case (So You Don’t Ask Later)
> **What about indexes, manifests, or catalogs of canonical files?**
> 
> - The *index document* gets a QID
> - The *files listed inside it* do not
> 
> Example:
> ```
> QID-1.0.0_AES_Canonical_File_Index.md
> ```
> Inside:
> ```
> - 2024-11-02_Bill_Statement.pdf
> - 2024-12-01_Usage_Report.csv
> ```
> 
> Still clean. Still correct.
> 
> ---
> 
> ## Final Verdict
> - Canonical storage: **NO QIDs**
> - QiNote modules: **YES QIDs**
> - Any other approach creates tech debt, cognitive debt, and AI confusion
> 
> You were right to pause. This is one of those foundational calls that quietly determines whether the system scales or collapses.

### User
> i wish there was a script or an addition to qid that like watches the vault folder and when ever a folder is created it would assign the qid based on the rules nad location the folder is in or somethign but i guess it would be hard for it to know what is the root and what are just children of the folder. unless we define it in the way folders are labeled.

### Assistant
> You’re not wrong — it’s only “hard” if you leave the system ambiguous. If you make root vs child *machine-detectable*, this becomes very doable.
> 
> Here are three solid approaches, from simplest to most robust.
> 
> ---
> 
> ## Option A (Best ROI): “Root markers” + watcher
> Make “module roots” unambiguous by dropping a marker file in any folder that should receive a QID.
> 
> **Rule:**
> - A folder is a *module root* if it contains `qiroot.json` (or `.qiroot`)
> - Anything else is just a child folder and does not get a new QID unless it also has its own marker
> 
> Example:
> ```
> QiNote_Vault/
>   02_Cases/
>     AES_Dispute/               <-- has qiroot.json  ✅ assign QID
>       Exhibits/                <-- no marker        ❌ no QID
>       Notes/                   <-- no marker        ❌ no QID
>       Motion_To_Stay/          <-- has qiroot.json  ✅ assign QID (sub-module)
> ```
> 
> **Why this works:**
> - Zero guessing
> - You explicitly declare “this folder is a module”
> - The watcher can safely assign QIDs only where it’s allowed
> 
> ---
> 
> ## Option B: Naming convention triggers (fast but brittle)
> You encode intent in the folder name.
> 
> Examples:
> - `M__AES_Dispute` = module root
> - `_` prefix for child folders
> - `@` for special folders
> 
> Example:
> ```
> 02_Cases/
>   M__AES_Dispute/     ✅ assign QID
>     _Exhibits/        ❌
>     _Notes/           ❌
> ```
> 
> **Downside:** people forget prefixes, typos happen, and now the system misbehaves.
> 
> ---
> 
> ## Option C (Most powerful): Manifest-driven vault topology
> You keep a single vault config file that defines what paths are “QID domains” and how numbering works.
> 
> Example file:
> `vault_rules.yml` (or json)
> - “Assign QID to any new folder created under `02_Cases/*` only if it contains `README.md` OR `qiroot.json`”
> - Different numbering schemes per top-level domain
> 
> **Upside:** extremely consistent at scale  
> **Downside:** more setup
> 
> ---
> 
> ## The “Root vs Child” Problem You Mentioned
> You nailed it: the watcher can’t infer intent reliably without a signal.
> 
> So give it a signal. Choose one:
> 
> ### My recommendation: **marker file + minimal metadata**
> Put this in every new module root:
> 
> `qiroot.json`
> ```json
> {
>   "type": "module_root",
>   "qid_domain": "Cases",
>   "title": "AES Dispute",
>   "create_readme": true
> }
> ```
> 
> Then the automation can:
> - Assign the QID
> - Rename folder (optional)
> - Generate `README.md` and `index.md` (optional)
> - Write the QID into front matter
> 
> No guessing. No chaos.
> 
> ---
> 
> ## Practical Workflow (ADHD-proof)
> 1) You create a folder anywhere.
> 2) If it’s a real module root, you drop `qiroot.json` in it (or run a tiny “init module” command).
> 3) The watcher sees the marker and does the rest.
> 
> This reduces “decisions per folder” to one binary choice:
> - Is this a module root? Yes/No.
> 
> ---
> 
> ## What I’d Build First (Minimal Viable Watcher)
> **Behavior:**
> - Watch the vault root
> - On folder creation:
>   - if `qiroot.json` exists OR appears within 5 minutes:
>     - assign QID
>     - write `qid.txt`
>     - optionally rename folder to `QID_TitleSlug`
>     - generate `README.md` with YAML front matter
> 
> This handles your “I created the folder, forgot the marker” reality.
> 
> ---
> 
> ## If you want, I’ll write the script
> I can give you a Windows-friendly Python watcher (no weird dependencies, or using `watchdog` if you’re okay installing one package), plus:
> - `init_module.ps1` helper
> - `qiroot.json` templates
> - a predictable QID allocator that won’t collide
> 
> If you tell me just one thing: **do you want QIDs to be global (single sequence) or per-domain (Cases, People, Ops each has its own sequence)?**

### User
> ok, that makes sense, um questions now, do we prefix the assigned qid or suffix the folders.

### Assistant
> Short answer: **prefix the folder name with the QID. Always. No exceptions.**
> 
> Now the why — and this is one of those decisions you do *once* and never revisit.
> 
> ---
> 
> ## The Correct Pattern
> 
> **`QID-<id>_<Human_Title>`**
> 
> Example:
> ```
> QID-2.1.4_AES_Dispute/
> QID-5.3.2_Court_Hearing_Jan09/
> QID-1.0.0_QiNote_System_Rules/
> ```
> 
> ---
> 
> ## Why PREFIX Wins (Objectively)
> 
> ### 1. Sorting Works Everywhere
> Prefixing guarantees:
> - Correct lexical order in:
>   - Windows Explorer
>   - macOS Finder
>   - GitHub
>   - ZIP archives
>   - Command line
> - You don’t need special views or tooling
> 
> Suffixing does **not** sort by identity — it sorts by vibes.
> 
> ---
> 
> ### 2. Identity Is Seen Instantly
> You want the QID to be the **first thing your eyes and tools see**.
> 
> This:
> ```
> QID-3.2.1_AES_Usage_Analysis
> ```
> 
> Not this:
> ```
> AES_Usage_Analysis_QID-3.2.1
> ```
> 
> The second hides the system signal at the end where it’s least useful.
> 
> ---
> 
> ### 3. Prefix = Immutable, Suffix = Decorative
> - Prefix says: *this is the authoritative identity*
> - Suffix feels like metadata you might “clean up later”
> 
> You won’t — but your brain will treat it as optional.
> 
> ---
> 
> ### 4. Renames Stay Cheap
> Titles evolve. QIDs don’t.
> 
> With prefixing:
> - You can freely rename the title portion
> - The identity stays anchored
> 
> Example:
> ```
> QID-2.1.4_AES_Dispute
> → QID-2.1.4_AES_Dispute_Federal_Appeal
> ```
> 
> No links break. No confusion.
> 
> ---
> 
> ## Hard Rule
> > **If a folder has a QID, the QID is the prefix.**  
> > **If it doesn’t, it never gets one later.**
> 
> No retroactive guessing.
> 
> ---
> 
> ## Children Folders (Important)
> Child folders **do not** get QIDs unless they are declared module roots.
> 
> Example:
> ```
> QID-2.1.4_AES_Dispute/
>   Exhibits/
>   Notes/
>   Drafts/
> ```
> 
> If a child *becomes* a real module later:
> ```
> QID-2.1.4_AES_Dispute/
>   QID-2.1.4.1_Motion_To_Stay/
> ```
> 
> Still prefix. Still consistent.
> 
> ---
> 
> ## What the Automation Should Do
> When assigning a QID:
> 1) Generate QID
> 2) Slugify title
> 3) Rename folder to:
>    ```
>    QID-<id>_<slug>
>    ```
> 4) Write QID into:
>    - `qiroot.json`
>    - `README.md` front matter
>    - optional `qid.txt` for dumb tools
> 
> ---
> 
> ## Final Call
> - Prefixing is not aesthetic — it’s structural.
> - Suffixing will cost you clarity later.
> - Mixed approaches are forbidden.
> 
> This is one of those “boring but foundational” calls. You picked the right direction.

### User
> we almost need the qid tool to be more integrated somehow in the file system, like right click a folder, option assign qid, with options, then bam its updated, or am i doing to much.

### Assistant
> Short answer: **you’re not doing too much — but you *are* at the fork where people either stop or build the thing that actually sticks.**  
> This is exactly the right instinct. The trick is **how far to go, and in what order.**
> 
> Let’s ground this and prevent over-engineering.
> 
> ---
> 
> ## Reality Check (Truth Mode)
> You are not asking for anything exotic.
> 
> What you’re describing is **how serious systems actually work**:
> - Git → right-click → “Git Bash here”
> - Dropbox → “Share”
> - Notion → “Turn into database”
> - Obsidian → “New note”
> 
> **QiNote without frictionless QID assignment will eventually decay.**  
> Not catastrophically — but enough to annoy you and create inconsistency.
> 
> So: *the idea is correct*.  
> The question is **what’s the smallest irreversible win**.
> 
> ---
> 
> ## The Correct Phased Approach (Do Not Skip Steps)
> 
> ### Phase 1 (Build this NOW): CLI + Script = Source of Truth
> Before UI candy, you need a rock-solid engine.
> 
> **Command:**
> ```
> qid assign .
> ```
> 
> Or:
> ```
> qid init "AES Dispute"
> ```
> 
> This:
> - Assigns QID
> - Renames folder (prefix)
> - Writes `qiroot.json`
> - Generates `README.md`
> 
> This becomes the **only authority** for QID logic.
> 
> If this isn’t perfect, a right-click menu will just automate mistakes faster.
> 
> ---
> 
> ### Phase 2 (Very doable): Windows Explorer Right-Click
> This is where your instinct is pointing — and yes, it’s legit.
> 
> **Right-click folder → “QiNote → Assign QID”**
> 
> Behind the scenes, it just calls:
> ```
> qid assign "C:\Path\To\Folder"
> ```
> 
> Implementation options (Windows):
> - PowerShell + Registry entry (classic, stable)
> - Windows 11 context menu via `shell\open\command`
> - Optional submenu:
>   - Assign QID (default)
>   - Assign QID → Case
>   - Assign QID → Person
>   - Assign QID → System
> 
> **Key rule:**  
> The context menu does *nothing clever*. It delegates to the CLI.
> 
> ---
> 
> ### Phase 3 (Optional, later): Watcher + Suggestions
> At this point, you can add:
> - Folder watcher that *suggests* QID assignment
> - Notifications like:
>   > “New folder detected in 02_Cases. Assign QID?”
> 
> Important: **suggest, don’t auto-assign**.  
> Automation without intent is how you corrupt meaning.
> 
> ---
> 
> ## What You Should NOT Build (Yet)
> Let me stop you from a trap:
> 
> ❌ A smart watcher that guesses roots  
> ❌ AI-based folder intent inference  
> ❌ Auto-assign on every folder creation  
> ❌ GUI before rules are frozen  
> 
> Those all sound nice and will absolutely cause regret.
> 
> ---
> 
> ## The Ideal UX (What You’re Actually Imagining)
> You right-click a folder and see:
> 
> ```
> QiNote
>  ├─ Assign QID
>  ├─ Assign QID (Case)
>  ├─ Assign QID (Person)
>  ├─ Assign QID (System)
>  └─ Mark as Child (no QID)
> ```
> 
> You click once.
> It’s done.
> No thinking.
> No naming stress.
> 
> That’s not overkill.  
> That’s **respecting your cognitive load**.
> 
> ---
> 
> ## The Principle to Lock In
> > **QID assignment must be easier than not assigning one.**
> 
> If it’s buried behind ceremony, you’ll skip it when tired.
> If it’s one right-click, you won’t.
> 
> ---
> 
> ## My Recommendation (Clear Decision)
> - You are **not** doing too much conceptually
> - You **should not** start with the UI
> - Build in this order:
>   1. `qid` CLI (rock solid)
>   2. Right-click integration (thin wrapper)
>   3. Watcher (optional, advisory only)
> 
> If you want, next step I’ll:
> - Define the exact CLI commands
> - Give you the PowerShell + registry snippet for right-click
> - Design the `qiroot.json` schema so this never needs changing
> 
> Say the word.

### User
> tell me the files you want to see to get this locked in. ```markdown

> . 📂 app_QiNoteOS_ph03_QiD-cli

> ├── 📄 LICENSE

> ├── 📄 README.md

> └── 📂 _assets/

> │  └── 📂 _generated_icons/

> │    ├── 📄 qid_128.png

> │    ├── 📄 qid_16.png

> │    ├── 📄 qid_24.png

> │    ├── 📄 qid_256.png

> │    ├── 📄 qid_32.png

> │    ├── 📄 qid_48.png

> │    ├── 📄 qid_64.png

> │  ├── 📄 make_ico.py

> │  ├── 📄 qid-3d.jpg

> │  ├── 📄 qid-barcode.jpg

> │  ├── 📄 qid-complex.jpg

> │  ├── 📄 qid-complex.mp4

> │  ├── 📄 qid-gradient.jpg

> │  ├── 📄 qid-inverted.svg

> │  ├── 📄 qid-led.jpg

> │  ├── 📄 qid-qr-code.jpg

> │  ├── 📄 qid.ico

> │  ├── 📄 qid.ico.txt

> │  ├── 📄 qid.jpg

> │  ├── 📄 qid.png

> │  ├── 📄 qid.svg

> └── 📂 _backups/

> │  └── 📂 daily/

> │  └── 📂 rolling/

> │    ├── 📄 registry.prev.json

> │    ├── 📄 state.prev.json

> └── 📂 _logs/

> │  ├── 📄 qid_activity.jsonl

> ├── 📄 _qid_registry.json

> ├── 📄 _qid_state.json

> └── 📂 _wal/

> │  ├── 📄 qid_wal.jsonl

> ├── 📄 build_windows.ps1

> └── 📂 desktop/

> │  ├── 📄 create_shortcut.ps1

> │  ├── 📄 create_shortcut.vbs

> │  ├── 📄 qid_launcher.bat

> │  ├── 📄 qid_ui.bat

> └── 📂 docs/

> │  ├── 📄 DEV_DOC.md

> │  ├── 📄 gid_rules.md

> ├── 📄 pyproject.toml

> ├── 📄 qid.py

> └── 📄 requirements.txt

> ```

### Assistant
> Good — this tree is already 80% of what I’d want. To “lock it in” (rules + behavior + Windows integration) I need to see a very specific subset, in this order. Anything else is noise.
> 
> ## Tier 1: Must-have (to validate core logic + safety)
> 1) **`qid.py`**  
>    - I need to see the command interface, the allocation algorithm, rename rules, error handling, and idempotency.
> 
> 2) **`docs/gid_rules.md`** (and/or wherever the authoritative rules actually live)  
>    - This is where we confirm: what is a module root, what gets a QID, naming format, child rules, reserved folders, etc.
> 
> 3) **`_qid_registry.json`**  
>    - Confirms the canonical registry structure: keys, uniqueness guarantees, metadata stored, how you track assigned paths.
> 
> 4) **`_qid_state.json`**  
>    - Confirms the allocator state model: last issued IDs, per-domain counters (if any), locking, and recovery rules.
> 
> 5) **`_wal/qid_wal.jsonl`**  
>    - I’m checking durability: how you recover from a crash mid-rename, and whether operations are replayable/rollbackable.
> 
> If these five are solid, the system is already “real.”
> 
> ---
> 
> ## Tier 2: Windows integration (to make right-click real)
> 6) **`build_windows.ps1`**  
>    - This should be responsible for packaging/install and (ideally) context menu registration.
> 
> 7) **`desktop/qid_launcher.bat`** and **`desktop/qid_ui.bat`**  
>    - I need to see how you’re invoking Python, how you pass the target folder, and whether paths with spaces are safe.
> 
> 8) **`desktop/create_shortcut.ps1`** (VBS optional)  
>    - Only if you’re doing desktop shortcuts as part of install.
> 
> Also: if you already have any registry installer logic, show it. If you don’t, we’ll add it.
> 
> ---
> 
> ## Tier 3: Packaging + reproducibility (so it doesn’t rot)
> 9) **`pyproject.toml`**  
>    - I want to verify entrypoints (e.g. `qid=...`), versioning, dependency pinning, and build target.
> 
> 10) **`requirements.txt`**  
>    - Quick sanity check: are you using `watchdog`, `typer/click`, `portalocker`, etc., and are they pinned appropriately?
> 
> ---
> 
> ## Tier 4: Evidence (optional, but helpful)
> 11) **`_logs/qid_activity.jsonl`**  
>    - Not required, but it tells me what the tool *actually* does today vs. what we think it does.
> 
> 12) **`docs/DEV_DOC.md`**  
>    - Only if it explains install + usage beyond what’s in README.
> 
> ---
> 
> ## What I do NOT need right now
> - `_assets/*` (icons are great, but irrelevant to correctness)
> - `_backups/*` (unless you suspect corruption issues)
> - `LICENSE` (not for behavior)
> - `README.md` (nice-to-have; not decisive)
> 
> ---
> 
> ## One critical note (you have a naming inconsistency)
> You have `gid_rules.md` under `docs/` but this is the **QiD** tool. If that file is actually the rules source, rename it to **`qid_rules.md`**. If “GID” is a different concept, we need to separate them now before it becomes technical debt.
> 
> ---
> 
> ## Minimal “send me these” list
> If you want the tightest possible bundle, send:
> 
> - `qid.py`
> - `docs/gid_rules.md`
> - `_qid_registry.json`
> - `_qid_state.json`
> - `_wal/qid_wal.jsonl`
> - `build_windows.ps1`
> - `desktop/qid_launcher.bat`
> - `pyproject.toml`
> 
> That’s enough for me to lock rules, confirm allocator integrity, and spec the right-click integration without guessing.

### Assistant
> Good — thanks for dropping the files. I’ve reviewed the core pieces you uploaded, and here’s the straight, no-fluff verdict.
> 
> ---
> 
> # Executive Verdict
> 
> **You are not overthinking this.**  
> You’ve already built ~70% of a *production-grade* QID engine.
> 
> What you have is **sound**, but there are **three architectural misalignments** that must be corrected *now* before you wire this into right-click / filesystem workflows.
> 
> If you fix these, the system will lock in cleanly and scale.  
> If you don’t, it will slowly fight you.
> 
> I’ll break this into:
> 1. What is solid (don’t touch)
> 2. What must change (non-negotiable)
> 3. What to add to support “right-click Assign QID”
> 4. The exact next steps to lock it in
> 
> ---
> 
> ## 1. What’s Already Solid (Keep This)
> 
> ### ✅ Registry + State Separation
> - `_qid_registry.json` = immutable history of issued roots
> - `_qid_state.json` = allocator cursor per band
> 
> This is correct and professional. fileciteturn0file2turn0file3
> 
> ### ✅ Banding Model (COA-style)
> Your band ranges and exhaustion checks are correct and defensible.  
> This will scale to millions without rework. fileciteturn0file1
> 
> ### ✅ Locking + Atomic Writes
> - `.lock` file
> - temp file + `os.replace`
> - rolling + daily backups
> - WAL
> 
> This is **better than many commercial tools**. Keep it. fileciteturn0file0
> 
> ### ✅ Immutability Principle
> Your rules doc gets this exactly right:
> > IDs are burnt, never reused, never modified.
> 
> Do not relax this. Ever. fileciteturn0file1
> 
> ---
> 
> ## 2. Critical Misalignments (Fix These Now)
> 
> ### ❌ 1. QID vs QiNote Module Roots (Concept Leak)
> 
> Right now, the tool **does not distinguish** between:
> - a *conceptual module root* (QiNote meaning)
> - a *generic ID root* (any file, any path)
> 
> That’s fine for stamping files,  
> but **insufficient for folder-based module assignment**, which is what you want next.
> 
> **Required fix:**
> Introduce an explicit concept of **module root intent**.
> 
> This cannot be inferred reliably from paths alone.
> 
> ---
> 
> ### ❌ 2. Path inference is too implicit for filesystem automation
> 
> This function is dangerous at scale:
> 
> ```python
> infer_band_from_path(path_str)
> ```
> 
> Why:
> - Right-click context menus do not convey semantic intent
> - Folder names lie
> - Paths get refactored
> 
> **Path inference is acceptable only as a fallback**, never as the deciding signal.
> 
> ---
> 
> ### ❌ 3. No “assign to folder” primitive yet
> 
> You do *file stamping* very well.
> 
> But for your stated goal (“right click a folder → assign QID”), you are missing:
> 
> - a folder-level command
> - a clear rule for:
>   - rename vs not rename
>   - where metadata lives
>   - how child folders are treated
> 
> Right now, the tool has no opinion — which is dangerous.
> 
> ---
> 
> ## 3. What You Need to Add (Minimal, Surgical)
> 
> This is the key insight:
> 
> > **The filesystem needs an explicit marker for “this folder is a QID module root.”**
> 
> ### Add exactly ONE new concept
> 
> #### `qiroot.json` (or `.qiroot`)
> Placed inside a folder *by intent*, not inference.
> 
> Example:
> ```json
> {
>   "type": "qinote_module",
>   "title": "AES Dispute",
>   "band": "CLIENT",
>   "rename": true
> }
> ```
> 
> This solves:
> - root vs child ambiguity
> - watcher automation
> - right-click behavior
> - future refactors
> 
> No guessing. No heuristics.
> 
> ---
> 
> ### Add ONE new command
> 
> #### `qid assign-folder <path>`
> 
> Behavior:
> 1. Validate folder
> 2. Require `qiroot.json` (or prompt to create it)
> 3. Issue root QID
> 4. Rename folder to:
>    ```
>    QID-0400003_AES_Dispute/
>    ```
> 5. Write:
>    - `qiroot.json` (with QID injected)
>    - optional `README.md`
> 
> This becomes the **only** thing the right-click menu calls.
> 
> ---
> 
> ## 4. Right-Click Integration (You’re Not Doing Too Much)
> 
> You were right earlier: this belongs in the filesystem.
> 
> But — and this matters —  
> **the right-click menu must be dumb.**
> 
> It should do exactly this:
> 
> ```bat
> qid assign-folder "%1"
> ```
> 
> No logic.
> No guessing.
> No UI decisions.
> 
> All intelligence stays in Python.
> 
> ---
> 
> ## 5. Naming / Documentation Cleanup (Small but Important)
> 
> - `gid_rules.md` → **rename to `qid_rules.md`**
>   - GID vs QID ambiguity will hurt you later.
> - Update rules doc to explicitly state:
>   - QIDs apply to **QiNote module roots**
>   - Canonical storage never gets QIDs
>   - Folders only get QIDs if marked
> 
> Your DEV_DOC is otherwise solid. fileciteturn0file4
> 
> ---
> 
> ## Final Lock-In Recommendation (Do This in Order)
> 
> **Do not jump ahead. Follow this sequence.**
> 
> 1. Add `qiroot.json` spec (tiny file, big payoff)
> 2. Add `assign-folder` command
> 3. Update rules doc to reflect folder semantics
> 4. Wire right-click menu → `assign-folder`
> 5. (Optional) later add watcher that *suggests* assignment
> 
> At that point:
> - QIDs will be frictionless
> - The system will be self-documenting
> - You will not paint yourself into a corner
> 
> ---
> 
> ### Bottom line
> 
> You are not overengineering.  
> You are **one explicit intent marker away** from a very clean, durable system.
> 
> If you want, next step I can:
> - Draft the `qiroot.json` schema
> - Spec the exact folder rename rules
> - Sketch the PowerShell registry entry for Windows Explorer
> 
> Say which one you want first.

### User
> you can give me the gemini prompt for this to do it. and fyi here is the module directory so far that i have been building. ```markdown

> . 📂 04_PRIMARY

> └── 📂 10_datasets/

> │  └── 📂 10_banking/

> │    └── 📂 10_CashApp/

> │      ├── 📄 10_CashApp.gsheet

> │      ├── 📄 cash_app_report_2013-2015.csv

> │      ├── 📄 cash_app_report_2019.csv

> │      ├── 📄 cash_app_report_2020.csv

> │      ├── 📄 cash_app_report_2021.csv

> │      ├── 📄 cash_app_report_2022.csv

> │      ├── 📄 cash_app_report_2023.csv

> │      ├── 📄 cash_app_report_2024.csv

> │      ├── 📄 cash_app_report_2025.csv

> │      ├── 📄 cash_app_report_2026.csv

> │  └── 📂 20_rules/

> │    └── 📂 10_quickbooks/

> │      ├── 📄 QIALLY_LLC_Bank_Feed_Rules_UPDATED_v2.csv

> │      ├── 📄 QIALLY_LLC_Bank_Feed_Rules_v1.csv

> │  └── 📂 30_mappings/

> │    ├── 📄 statement mapping.csv

> └── 📂 20_modules/

> │  └── 📂 10_cases/

> │    └── 📂 FCFCU/

> │      ├── 📄 01_motion_vacate (1).pdf

> │      ├── 📄 01_motion_vacate (2).pdf

> │      ├── 📄 02_Motion_Quash_Stay.pdf

> │      ├── 📄 02_emergency_motion_quash_stay.pdf

> │      ├── 📄 03_Proposed_Order_Vacate.pdf

> │      ├── 📄 04_Proposed_Order_Quash_Stay.pdf

> │      ├── 📄 06_Exhibits_Combined.pdf

> │      ├── 📄 2025-12-21_Exhibit_V-03-02_DECLARATION RE PRIOR LAW ENFORCEMENT CONTACTS, AUDIBILITY LIMITATIONS, AND SAFETY CONTEXT_crice4485@gmail.com.pdf

> │      ├── 📄 2025-12-22_DOJ_Civil_Rights_Report_688619-FXN.pdf

> │      └── 📂 65_immutable_evidence_copies/

> │        └── 📂 12092025-mayberemovalday/

> │          ├── 📄 00-06-23_2a.mkv

> │          ├── 📄 00-16-23_2a.mkv

> │          ├── 📄 00-26-23_2a.mkv

> │          ├── 📄 00-36-23_2a.mkv

> │          ├── 📄 00-46-23_2a.mkv

> │          ├── 📄 00-56-23_2a.mkv

> │          ├── 📄 01-06-23_2a.mkv

> │          ├── 📄 01-16-23_2a.mkv

> │          ├── 📄 01-26-22_2a.mkv

> │          ├── 📄 01-36-22_2a.mkv

> │          ├── 📄 01-46-22_2a.mkv

> │          ├── 📄 01-56-22_2a.mkv

> │          ├── 📄 02-06-22_2a.mkv

> │          ├── 📄 02-16-22_2a.mkv

> │          ├── 📄 02-26-22_2a.mkv

> │          ├── 📄 02-36-22_2a.mkv

> │          ├── 📄 02-46-22_2a.mkv

> │          ├── 📄 02-56-21_2a.mkv

> │          ├── 📄 03-06-21_2a.mkv

> │          ├── 📄 03-16-21_2a.mkv

> │          ├── 📄 03-26-21_2a.mkv

> │          ├── 📄 03-36-21_2a.mkv

> │          ├── 📄 03-46-21_2a.mkv

> │          ├── 📄 03-56-21_2a.mkv

> │          ├── 📄 04-06-21_2a.mkv

> │          ├── 📄 04-16-21_2a.mkv

> │          ├── 📄 04-26-21_2a.mkv

> │          ├── 📄 04-36-21_2a.mkv

> │          ├── 📄 04-46-20_2a.mkv

> │          ├── 📄 04-56-20_2a.mkv

> │          ├── 📄 05-06-20_2a.mkv

> │          ├── 📄 05-16-20_2a.mkv

> │          ├── 📄 05-26-20_2a.mkv

> │          ├── 📄 05-36-20_2a.mkv

> │          ├── 📄 05-46-20_2a.mkv

> │          ├── 📄 05-56-20_2a.mkv

> │          ├── 📄 06-06-20_2a.mkv

> │          ├── 📄 06-16-20_2a.mkv

> │          ├── 📄 06-26-20_2a.mkv

> │          ├── 📄 06-36-19_2a.mkv

> │          ├── 📄 06-46-19_2a.mkv

> │          ├── 📄 06-56-19_2a.mkv

> │          ├── 📄 07-06-19_2a.mkv

> │          ├── 📄 07-16-19_2a.mkv

> │          ├── 📄 07-26-19_2a.mkv

> │          ├── 📄 07-36-19_2a.mkv

> │          ├── 📄 07-46-19_2a.mkv

> │          ├── 📄 07-56-19_2a.mkv

> │          ├── 📄 08-06-19_2a.mkv

> │          ├── 📄 08-16-18_2a.mkv

> │          ├── 📄 08-26-18_2a.mkv

> │          ├── 📄 08-36-18_2a.mkv

> │          ├── 📄 08-46-18_2a.mkv

> │          ├── 📄 08-56-18_2a.mkv

> │          ├── 📄 09-06-18_2a.mkv

> │          ├── 📄 09-16-18_2a.mkv

> │          ├── 📄 09-26-18_2a.mkv

> │          ├── 📄 09-36-18_2a.mkv

> │          ├── 📄 09-46-18_2a.mkv

> │          ├── 📄 09-56-18_2a.mkv

> │          ├── 📄 10-06-17_2a.mkv

> │          ├── 📄 10-16-17_2a.mkv

> │          ├── 📄 10-26-17_2a.mkv

> │          ├── 📄 10-36-17_2a.mkv

> │          ├── 📄 10-46-17_2a.mkv

> │          ├── 📄 10-56-17_2a.mkv

> │      ├── 📄 CPR certification (1).pdf

> │      ├── 📄 CPR certification (2).pdf

> │      ├── 📄 Exhibit X — Inventory of Jurisdictional, Execution, and Civil Rights Violations.pdf

> │      ├── 📄 Inventory of Civil and Fair Housing Rights Violations.gsheet

> │      ├── 📄 Orientation_and_Onboardin_signed_pages_Copy (1).pdf

> │      ├── 📄 Orientation_and_Onboardin_signed_pages_Copy.pdf

> │      ├── 📄 Zoho One - Subscription Renewal - Final Reminder!.pdf

> │      ├── 📄 cody_rice_velasquez-fullstack (1).pdf

> │      ├── 📄 cody_rice_velasquez-fullstack (2).pdf

> │      ├── 📄 direct-deposit-form-CASHAPP.PDF

> │      ├── 📄 id-card (3).pdf

> │      ├── 📄 vehicle-insurance-id-card (1).pdf

> │      ├── 📄 vehicle-insurance-id-card.pdf

> │  └── 📂 20_clients/

> │    └── 📂 _others/

> │      ├── 📄 023-53-0573 1d5f84a0440280c684b4cdce99fcb32b.md

> │      ├── 📄 025-35-0805 1b6f84a0440280d79d9cec2edbdfc5f2.md

> │      ├── 📄 025-35-0805 1d5f84a044028074ada3c801fc706209.md

> │      ├── 📄 061-55-5002 1d5f84a0440280bd81e0db3cfa70f211.md

> │      ├── 📄 063-89-2881 1d5f84a0440280e7add8c62b9f93c134.md

> │      ├── 📄 086-64-7349 1d5f84a0440280e086f2e9f3e14168ed.md

> │      ├── 📄 09212025_QiAlly LLC.pdf

> │      ├── 📄 093-53-8700 1d5f84a044028011a3c0e18359bc735c.md

> │      ├── 📄 186-61-3456 1d5f84a04402802bb9c9eecbaa82cc4b.md

> │      ├── 📄 186-81-1826 1d5f84a0440280e9828ef821b93e5535.md

> │      ├── 📄 2021 - LUIS E MUNOZ ALTAMIRANO TAX RETURN 1b0f84a044028021bdbfd9ac11126386.md

> │      ├── 📄 2022 - LUIS E MUNOZ ALTAMIRANO TAX RETURN 1b0f84a044028054aadaf4e5d6b71576.md

> │      ├── 📄 2022 1040X - LUIS E MUNOZ ALTAMIRANO TAX RETURN 1b0f84a044028028a807f5b4df8fc757.md

> │      ├── 📄 2023 - LUIS E MUNOZ ALTAMIRANO TAX RETURN 1b0f84a0440280019254ce93da530ca1.md

> │      ├── 📄 2024 - LUIS E MUNOZ ALTAMIRANO TAX RETURN 1b0f84a044028007a4e7fdae7c8a1441.md

> │      ├── 📄 2024 - TACOPOLIS TAX RETURN 1c4f84a0440280d0be3ce5e90b7841b7.md

> │      ├── 📄 2024 - TACOPOLIS TAX RETURN.md

> │      ├── 📄 2024 - TOBAR RODRIGUEZ, RAFAEL 1d3f84a04402808ba361c8a1d206e14f.md

> │      ├── 📄 2024 - TOBAR RODRIGUEZ, RAFAEL.md

> │      ├── 📄 2024 - Zaitullah Jan Khebarkhil 1b6f84a04402805e812fca7b92cdba09.md

> │      ├── 📄 202412-manmeet.pdf

> │      ├── 📄 2024_1099_NEC_from_Dustys_All_Star_Circus_LLC_(1).pdf

> │      ├── 📄 273-57-5392 1d5f84a04402802a8020fad576d2ef0b.md

> │      ├── 📄 276-61-7638 1d5f84a04402800fb641e99a2d1d4231.md

> │      ├── 📄 285-87-9961 1d5f84a044028017a995c736212b15e2.md

> │      ├── 📄 308-33-3727 1d5f84a0440280738503dff35d876b37.md

> │      ├── 📄 311-17-8442 1d5f84a0440280349a73e95b25400090.md

> │      ├── 📄 312-66-8512 1d5f84a04402803d93f2e8f1469bf859.md

> │      ├── 📄 312-66-8523 1d5f84a0440280c9a4e5c716f57bd7ad.md

> │      ├── 📄 316-23-8071 1d5f84a0440280ce88f9fd6d1d8b1f9f.md

> │      ├── 📄 324-83-9800 1d5f84a0440280978890c76d3083078b.md

> │      ├── 📄 327-02-6239 1d5f84a044028030b077d40d5aabe0a2.md

> │      ├── 📄 377-89-7143 1d5f84a04402807a8f9dc47efd4011ed.md

> │      ├── 📄 518-39-5169 1d5f84a044028085813fc5c50b7ae768.md

> │      ├── 📄 519-31-2420 1d5f84a04402807585cdf005bf7e6184.md

> │      ├── 📄 534-39-9694 1d5f84a0440280ceab6bca5d47e5533a.md

> │      ├── 📄 546-25-8594 1d5f84a044028078b5a6d829ae697679.md

> │      ├── 📄 559-65-6876 1d5f84a04402800e8784e305a8afb2b2.md

> │      ├── 📄 592-54-9993 1d5f84a0440280ca8464eec2c290fd23.md

> │      ├── 📄 597-87-9585 1d5f84a044028051ad47dcc74a9a02c2.md

> │      ├── 📄 5e0fe1b2-7983-41af-ba0a-1f48b21dfcc9.png

> │      ├── 📄 618-19-2300 1d5f84a044028054926dd298cbe21800.md

> │      ├── 📄 620-31-0445 1d5f84a04402809fa5f9c589e994a117.md

> │      ├── 📄 638-98-6281 1d5f84a044028021bb85e336b07d3306.md

> │      ├── 📄 641-18-9895 1d5f84a04402808dbe84eebca8d61661.md

> │      ├── 📄 647-69-5836 1d5f84a044028096932ffc700ac0406b.md

> │      ├── 📄 671-52-2719 1d5f84a04402809582b0e7311d37a31b.md

> │      ├── 📄 674-28-2585 1d5f84a0440280cfba4cd9ea696fb334.md

> │      ├── 📄 674-92-6457 1d5f84a044028019b7e9c3a8ef126b08.md

> │      ├── 📄 687-39-6121 1d5f84a04402807b93dcc236c5a598fc.md

> │      ├── 📄 707-82-2114 1d5f84a044028018bb3bca6368e9572a.md

> │      ├── 📄 732-87-7601 1d5f84a0440280bba6a1c8ff9f0fafe5.md

> │      ├── 📄 737-25-3624 1d5f84a0440280679c59ef7a86233216.md

> │      ├── 📄 747-22-0748 1d5f84a0440280c5b693e130ebeb88ae.md

> │      ├── 📄 763-11-8646 1d5f84a04402808795c7eabb403044c5.md

> │      ├── 📄 782-83-4329 1d5f84a04402804cbbbeefe863442bdd.md

> │      ├── 📄 805-22-2952 1d5f84a04402807493e2e2cad19d51da.md

> │      ├── 📄 806-97-9023 1d5f84a0440280d6b378fa887ed449e9.md

> │      ├── 📄 817-79-3234 1d5f84a0440280528d5cf7e70b9f8a04.md

> │      ├── 📄 846-18-6530 1d5f84a0440280e2b869e025c7703863.md

> │      ├── 📄 909-86-8729 1d5f84a044028070bf8fdb897491f8d2.md

> │      ├── 📄 912-91-5108 1d5f84a0440280d9add4c75ba065667d.md

> │      ├── 📄 922-86-9817 1d5f84a04402805d88adfae92d99f82c.md

> │      ├── 📄 927-81-0530 1d5f84a04402807ab0f0e7cee5e1750a.md

> │      ├── 📄 929-92-1015 1d5f84a04402807084a7e9b68d785c53.md

> │      ├── 📄 930-71-1012 1d5f84a0440280d1ae04e30957cfdd16.md

> │      ├── 📄 932-73-5548 1d5f84a04402800aa17fca885730580b.md

> │      ├── 📄 932-83-1329 1d5f84a044028028a757fe2fcbf4f751.md

> │      ├── 📄 938-94-6732 1d5f84a0440280feb394c32116c33052.md

> │      ├── 📄 940-86-2566 1d5f84a04402807ea05ce0e1997756f7.md

> │      ├── 📄 948-75-4932 1d5f84a0440280709079e7541afd06b5.md

> │      ├── 📄 970-95-9852 1d5f84a04402804bb122f209b7a30432.md

> │      ├── 📄 975-74-7087 1d5f84a04402802c93eefe7141c649a5.md

> │      ├── 📄 976-82-4854 1d5f84a04402800db34ee8521c66fcae.md

> │      ├── 📄 982-95-9353 1d5f84a044028058b1f8df224b84469d.md

> │      ├── 📄 982-98-8820 1d5f84a0440280128017d336df0809a0.md

> │      ├── 📄 986-94-6900 1d5f84a0440280fe9d58e89730ff015f.md

> │      ├── 📄 986-95-3278 1d5f84a0440280779970df52ee6e243e.md

> │      ├── 📄 987-91-1556 1d5f84a044028090b031ca6d77fdbfcb.md

> │      ├── 📄 991-84-0372 1d5f84a0440280cf9089dbf6fc94940a.md

> │      ├── 📄 992-86-6614 1d5f84a0440280c2901acd915d33f3ed.md

> │      ├── 📄 994-74-9380 1d5f84a0440280c5a405c8b8f94398fa.md

> │      ├── 📄 998-78-5543 1d5f84a044028087acd9d2b8544dde2f.md

> │      ├── 📄 999-99-9993 1d5f84a044028046ace2dc7af919f370.md

> │      ├── 📄 999-99-9998 1d5f84a0440280008de0ca2cba125099.md

> │    └── 📂 c.bbr/

> │      └── 📂 00_Start/

> │        ├── 📄 10_welcome.md

> │        ├── 📄 20_onboarding.md

> │        └── 📂 40_Scope/

> │          ├── 📄 10_services.md

> │          ├── 📄 20_scope.md

> │          ├── 📄 30_policies.md

> │          ├── 📄 40_expectations.md

> │          ├── 📄 50_agreements.md

> │          ├── 📄 _index.md

> │        └── 📂 50_Investment/

> │          ├── 📄 10_pricing.md

> │          ├── 📄 20_proposal.md

> │          ├── 📄 _index.md

> │        └── 📂 60_Onboarding/

> │          ├── 📄 10_onboarding.md

> │          ├── 📄 20_checklist.md

> │          ├── 📄 30_data-request.md

> │          ├── 📄 40_access-credentials.md

> │          ├── 📄 50_kickoff.md

> │          ├── 📄 _index.md

> │        ├── 📄 _index.md

> │      └── 📂 10_profile/

> │        └── 📂 30_ids-and-documents/

> │      └── 📂 202510-bbrays-site-reports/

> │        ├── 📄 Analytics & logs _ Web analytics _ builtbyrays.com _ QiAlly _ Cloudflare.pdf

> │        ├── 📄 _202510-bbrays-site-reports.md

> │        ├── 📄 data_cached_2025-11-02T22_54_34.390Z.csv

> │        ├── 📄 official_tags_flat.csv

> │        ├── 📄 percent_cached_2025-11-02T22_54_34.395Z.csv

> │        ├── 📄 total_data_served_2025-11-02T22_54_34.393Z.csv

> │        ├── 📄 total_requests_2025-11-02T22_54_34.421Z.csv

> │        ├── 📄 unique_visitors_2025-11-02T22_54_34.424Z.csv

> │      └── 📂 20_Company/

> │        ├── 📄 10_org-chart.md

> │        ├── 📄 20_profile.md

> │        ├── 📄 30_strategy.md

> │        ├── 📄 _index.md

> │      ├── 📄 Parcel_8008931_PRC_Page2.png

> │      ├── 📄 Parcel_8008931_PRC_Page3.png

> │      ├── 📄 QiAlly (1).png

> │      ├── 📄 QiAlly.png

> │      ├── 📄 README.md

> │      ├── 📄 Rays Construction LLC_Profit and Loss by Month.csv

> │      └── 📂 _assets/

> │        ├── 📄 familyphoto.jpg

> │        ├── 📄 favicon.png

> │        ├── 📄 file-4zYJAJB7JJrkgF8h9PtYN6-DJI_20250911_202708_760.JPG

> │        ├── 📄 file-7insGsjzNq93fNr6He9Rjw-IMG_0511.PNG

> │        ├── 📄 file-91yW2FUHWWCYrjueTUrGD5-IMG_0509.jpg

> │        ├── 📄 file-Ai7MWuf9T2tEdeDWbQDosR-DJI_20250911_202316_260.JPG

> │        ├── 📄 file-BzLD23JwAy4m6RtPHAZy5L-IMG_0514.jpg

> │        ├── 📄 file-HHcteYMBp4Jby5wWPjYVcA-DJI_20250911_202435_604.JPG

> │        ├── 📄 file-K5ACsbXZzAMjQQkC98hUPk-DJI_20250911_202245_541.JPG

> │        ├── 📄 file-QAmyeKgAhuDt5xqh45Ndnc-DJI_20250911_202424_237.JPG

> │        ├── 📄 file-QWZJ7r91wSnYNozHNeaL7H-DJI_20250911_202424_237.JPG

> │        ├── 📄 file-Vuhpin827hMxucUVPkJW6N-DJI_20250911_202435_604.JPG

> │        ├── 📄 file-Y71Hezp1ZF5nGazAPAeYFF-DJI_20250911_202751_719.JPG

> │      ├── 📄 _index.md

> │      └── 📂 _intake/

> │      └── 📂 _system/

> │        ├── 📄 LICENSE

> │        └── 📂 logs/

> │          ├── 📄 Business_Notes.md

> │        └── 📂 templates/

> │          ├── 📄 _index.md

> │        └── 📂 tools/

> │          ├── 📄 _scripts.md

> │          ├── 📄 sync-kb-to-starlight.mjs

> │        └── 📂 workers/

> │      └── 📂 apps/

> │      └── 📂 c.builtbyrays-com-v2.0/

> │      └── 📂 components/

> │      └── 📂 data/

> │        └── 📂 202510-bbrays-site-reports/

> │          ├── 📄 Analytics & logs _ Web analytics _ builtbyrays.com _ QiAlly _ Cloudflare.pdf

> │          ├── 📄 _202510-bbrays-site-reports.md

> │          ├── 📄 data_cached_2025-11-02T22_54_34.390Z.csv

> │          ├── 📄 official_tags_flat.csv

> │          ├── 📄 percent_cached_2025-11-02T22_54_34.395Z.csv

> │          ├── 📄 total_data_served_2025-11-02T22_54_34.393Z.csv

> │          ├── 📄 total_requests_2025-11-02T22_54_34.421Z.csv

> │          ├── 📄 unique_visitors_2025-11-02T22_54_34.424Z.csv

> │        ├── 📄 _70_exports.md

> │        ├── 📄 _index.md

> │      └── 📂 docs/

> │      └── 📂 engagements/

> │        └── 📂 Contracts_and_Agreements/

> │          ├── 📄 Drafts_and_Templates.md

> │          ├── 📄 Signed_Contracts.md

> │          ├── 📄 _Contracts_and_Agreements.md

> │        ├── 📄 Project_Notes.md

> │        └── 📂 Proposals_and_Offers/

> │          ├── 📄 Active_Proposals.md

> │          ├── 📄 Archived_Proposals.md

> │          ├── 📄 _Proposals_and_Offers.md

> │        └── 📂 Work_Summaries/

> │          ├── 📄 Deliverables_and_Results.md

> │          ├── 📄 Monthly_Summary.md

> │          ├── 📄 _Work_Summaries.md

> │        ├── 📄 _02_Engagements.md

> │      └── 📂 kb_vault/

> │        └── 📂 _start/

> │          ├── 📄 00.10.10_Welcome.md

> │          ├── 📄 10_Welcome.md

> │          ├── 📄 20_About_QiAlly.md

> │          ├── 📄 20_onboarding.md

> │          ├── 📄 30_Value_and_Scope.md

> │          ├── 📄 40_Policies_and_Procedures.md

> │          ├── 📄 50_Onboarding.md

> │          ├── 📄 60_How_To.md

> │          ├── 📄 70_FAQ_and_Glossary.md

> │          ├── 📄 About_QiAlly.md

> │          ├── 📄 FAQ_and_Glossary.md

> │          ├── 📄 Onboarding_Guide.md

> │          ├── 📄 Policies_and_Procedures.md

> │          ├── 📄 Using_This_System.md

> │          ├── 📄 Value_and_Scope.md

> │          ├── 📄 _00_Start.md

> │          ├── 📄 _01_EOS.md

> │          ├── 📄 _index.md

> │          └── 📂 about/

> │            ├── 📄 10_about-qially.md

> │            ├── 📄 20_about-qisuite.md

> │            ├── 📄 _30_About.md

> │            ├── 📄 _index.md

> │          └── 📂 investment/

> │            ├── 📄 10_pricing.md

> │            ├── 📄 20_proposal.md

> │            ├── 📄 _50_Investment.md

> │            ├── 📄 _index.md

> │          └── 📂 onboarding/

> │            ├── 📄 10_onboarding.md

> │            ├── 📄 20_checklist.md

> │            ├── 📄 30_data-request.md

> │            ├── 📄 40_access-credentials.md

> │            ├── 📄 50_kickoff.md

> │            ├── 📄 _60_Onboarding.md

> │            ├── 📄 _index.md

> │          └── 📂 scope/

> │            ├── 📄 10_services.md

> │            ├── 📄 20_scope.md

> │            ├── 📄 30_policies.md

> │            ├── 📄 40_expectations.md

> │            ├── 📄 50_agreements.md

> │            ├── 📄 _40_Scope.md

> │            ├── 📄 _index.md

> │        └── 📂 brand/

> │          ├── 📄 _10_Brand-Assets.md

> │          ├── 📄 _Compliance_and_Regulations.md

> │          ├── 📄 _index.md

> │        └── 📂 finance/

> │          ├── 📄 Finance_Notes.md

> │          ├── 📄 _index.md

> │          └── 📂 assets/

> │            ├── 📄 MNT_OS - 2. Mileage & Vehicle Info.pdf

> │            ├── 📄 _40_Assets.md

> │            ├── 📄 _index.md

> │          └── 📂 auths/

> │            ├── 📄 10_info-release-template.md

> │            └── 📂 20_Consent-Forms/

> │              ├── 📄 _20_Consent-Forms.md

> │              ├── 📄 _index.md

> │            ├── 📄 Document Authorization to Represent General Liability Audit has been completed.pdf

> │            ├── 📄 _40_Authorizations.md

> │            ├── 📄 _index.md

> │          └── 📂 banking/

> │            ├── 📄 _70_Banking.md

> │            ├── 📄 _Banking_and_Credit.md

> │            ├── 📄 _index.md

> │            └── 📂 check-images/

> │              ├── 📄 _check-images.md

> │              ├── 📄 _index.md

> │          └── 📂 compliance/

> │            ├── 📄 _50_Compliance.md

> │            ├── 📄 _index.md

> │          └── 📂 contracts/

> │            ├── 📄 10_msa.md

> │            ├── 📄 _20_contracts.md

> │            ├── 📄 _index.md

> │          └── 📂 expense/

> │            ├── 📄 Parcel_8008931_Detail_History.pdf

> │            ├── 📄 Parcel_8008931_PRC.pdf

> │            ├── 📄 Parcel_8008931_PRC_Page1.png

> │            ├── 📄 Parcel_8008931_PRC_Page2.png

> │            ├── 📄 Parcel_8008931_PRC_Page3.png

> │            ├── 📄 _30_Expenses.md

> │            ├── 📄 _index.md

> │          └── 📂 immigration/

> │            └── 📂 00_Drafts_and_Strategy/

> │              ├── 📄 2025-09-01_QiAlly_Leg_Strat_v01_final.pdf

> │              ├── 📄 2025-09-05_QiAlly_Leg_Timeline_v01_final.pdf

> │              ├── 📄 2025-09-10_QiAlly_Leg_Draft_v01_Aff_draft.pdf

> │              ├── 📄 2025-09-15_QiAlly_Leg_Timeline_v01_review_final.pdf

> │              ├── 📄 _00_Drafts_and_Strategy.md

> │            └── 📂 10_Bio_and_IDs/

> │              ├── 📄 2025-09-28_QiAlly_Leg_Bio_BC.pdf

> │              ├── 📄 2025-09-28_QiAlly_Leg_Bio_ID.pdf

> │              ├── 📄 2025-09-28_QiAlly_Leg_Bio_MC.pdf

> │              ├── 📄 2025-09-28_QiAlly_Leg_Bio_PC.pdf

> │              ├── 📄 _10_Bio_and_IDs.md

> │            ├── 📄 10_case-overview.md

> │            └── 📂 20_Employment/

> │              ├── 📄 2025-09-28_QiAlly_Leg_Emp_OL.pdf

> │              ├── 📄 2025-09-28_QiAlly_Leg_Emp_PS.pdf

> │              ├── 📄 2025-09-28_QiAlly_Leg_Emp_W2.pdf

> │              ├── 📄 _20_Employment.md

> │            └── 📂 30_Financial/

> │              ├── 📄 2025-09-28_QiAlly_Leg_Fin_BS.pdf

> │              ├── 📄 2025-09-28_QiAlly_Leg_Fin_EIS.pdf

> │              ├── 📄 2025-09-28_QiAlly_Leg_Fin_Tax.pdf

> │              ├── 📄 _30_Financial.md

> │            └── 📂 40_Other_Evidence/

> │              ├── 📄 2025-09-28_QiAlly_Leg_Other_LOS.pdf

> │              ├── 📄 2025-09-28_QiAlly_Leg_Other_PR.pdf

> │              ├── 📄 2025-09-28_QiAlly_Leg_Other_UB.pdf

> │              ├── 📄 _40_Other_Evidence.md

> │            └── 📂 50_Form_Filings/

> │              └── 📂 10_I-589 (Asylum)/

> │                ├── 📄 2025-09-28_QiAlly_Leg_i589_Aff_v01_draft.pdf

> │                ├── 📄 2025-09-28_QiAlly_Leg_i589_CL_v01_final.pdf

> │                ├── 📄 2025-09-28_QiAlly_Leg_i589_EOS.pdf

> │                ├── 📄 2025-09-28_QiAlly_Leg_i589_SD.pdf

> │                ├── 📄 2025-09-28_QiAlly_Leg_i589_form.pdf

> │                ├── 📄 _10_I-589 (Asylum).md

> │              └── 📂 20_I-360 (Special Immigrant)/

> │                ├── 📄 2025-09-28_QiAlly_Leg_i360_CL_v01_final.pdf

> │                ├── 📄 2025-09-28_QiAlly_Leg_i360_EOSvc.pdf

> │                ├── 📄 2025-09-28_QiAlly_Leg_i360_PS_v01_final.pdf

> │                ├── 📄 2025-09-28_QiAlly_Leg_i360_form.pdf

> │                ├── 📄 _20_I-360 (Special Immigrant).md

> │              └── 📂 30_I-130 (Family Sponsorship)/

> │                ├── 📄 2025-09-28_QiAlly_Leg_i130_CL_v01_final.pdf

> │                ├── 📄 2025-09-28_QiAlly_Leg_i130_EOR_v01_final.pdf

> │                ├── 📄 2025-09-28_QiAlly_Leg_i130_SP.pdf

> │                ├── 📄 2025-09-28_QiAlly_Leg_i130_form.pdf

> │                ├── 📄 _30_I-130 (Family Sponsorship).md

> │              ├── 📄 _50_Form_Filings.md

> │            ├── 📄 _60_Immigration.md

> │            ├── 📄 _Immigration.md

> │            ├── 📄 _index.md

> │          └── 📂 income/

> │            └── 📂 10_Invoices/

> │              ├── 📄 _10_Invoices.md

> │              ├── 📄 _index.md

> │              ├── 📄 sample-invoice.json

> │            ├── 📄 _20_Income.md

> │            ├── 📄 _index.md

> │          └── 📂 liabilities/

> │            ├── 📄 _50_Liabilities.md

> │            ├── 📄 _index.md

> │          └── 📂 policies/

> │            ├── 📄 _Contracts_and_Policies.md

> │          └── 📂 receipts/

> │            ├── 📄 _Receipts_and_Invoices.md

> │            ├── 📄 rays_construction_billing_statement_single_file_html.html

> │          └── 📂 reports/

> │            └── 📂 10_budgets-forecasts/

> │              ├── 📄 10_2025-q4-budget.md

> │              ├── 📄 _10_budgets-forecasts.md

> │              ├── 📄 _index.md

> │            ├── 📄 Rays Construction LLC_Account List.xlsx

> │            ├── 📄 _90_Reports.md

> │            ├── 📄 _Reports_and_Statements.md

> │            ├── 📄 _index.md

> │          └── 📂 tax/

> │            ├── 📄 10_1040_federal_return.md

> │            ├── 📄 20_schedule_c.md

> │            ├── 📄 Blanca_Refund_Forecast.pdf

> │            ├── 📄 Rays Construction LLC_Profit and Loss by Month.csv

> │            ├── 📄 _10_Tax-Returns.md

> │            ├── 📄 _Tax_Returns.md

> │            ├── 📄 _index.md

> │            ├── 📄 _tax.md

> │            ├── 📄 sch C.pdf

> │        └── 📂 hr/

> │          ├── 📄 _40_Human-Resources.md

> │          ├── 📄 _index.md

> │        ├── 📄 marketing.md

> │        └── 📂 personal/

> │          └── 📂 Education_and_Certificates/

> │            ├── 📄 _Education_and_Certificates.md

> │          └── 📂 Health_and_Wellness/

> │            ├── 📄 _Health_and_Wellness.md

> │          └── 📂 IDs_and_Documents/

> │            ├── 📄 _IDs_and_Documents.md

> │          └── 📂 Immigration_and_Travel/

> │            ├── 📄 _Immigration_and_Travel.md

> │          ├── 📄 Personal_Notes.md

> │          ├── 📄 _Personal.md

> │        └── 📂 resources/

> │          ├── 📄 _60_Resources.md

> │          ├── 📄 _Resources.md

> │          ├── 📄 _index.md

> │          └── 📂 guides/

> │            └── 📂 10_Onboarding_Guides/

> │              ├── 📄 _10_Onboarding_Guides.md

> │              ├── 📄 _index.md

> │            └── 📂 20_Training_Resources/

> │              ├── 📄 _20_Training_Resources.md

> │              ├── 📄 _index.md

> │            └── 📂 30_System_Documentation/

> │              ├── 📄 _30_System_Documentation.md

> │              ├── 📄 _index.md

> │            ├── 📄 _Checklists_and_Guides.md

> │            ├── 📄 _Guides.md

> │            ├── 📄 _index.md

> │          └── 📂 legal/

> │            ├── 📄 _10_Legal_Resources.md

> │            ├── 📄 _index.md

> │          └── 📂 marketing/

> │            ├── 📄 _20_Marketing_Assets.md

> │            ├── 📄 _index.md

> │          └── 📂 media/

> │            ├── 📄 _Media_and_Visuals.md

> │          └── 📂 misc/

> │            ├── 📄 _Misc_References.md

> │          └── 📂 sample/

> │            └── 📂 10_Client_Samples/

> │              ├── 📄 _10_Client_Samples.md

> │              ├── 📄 _index.md

> │            └── 📂 20_Project_Samples/

> │              ├── 📄 _20_Project_Samples.md

> │              ├── 📄 _index.md

> │            ├── 📄 _Samples.md

> │            ├── 📄 _index.md

> │          └── 📂 sops/

> │            ├── 📄 10_incident-001.md

> │            ├── 📄 20_release.md

> │            ├── 📄 _60_Processes.md

> │            ├── 📄 _Procedures_and_SOPs.md

> │            ├── 📄 _index.md

> │        └── 📂 tech/

> │          ├── 📄 _50_Technology.md

> │          ├── 📄 _index.md

> │      └── 📂 projects/

> │        └── 📂 10_Active/

> │          ├── 📄 _10_Active.md

> │          ├── 📄 _index.md

> │          ├── 📄 example-project.md

> │          ├── 📄 project-alpha.md

> │        └── 📂 20_Completed/

> │          ├── 📄 _20_Completed.md

> │          ├── 📄 _index.md

> │        ├── 📄 _10_Projects.md

> │        ├── 📄 _index.md

> │      ├── 📄 qios_agent.py

> │      ├── 📄 rays_construction_billing_statement_single_file_html.html

> │      └── 📂 sites/

> │        ├── 📄 README.md

> │        ├── 📄 _04_Site.md

> │        ├── 📄 _30_Websites.md

> │        ├── 📄 _index.md

> │        └── 📂 portal/

> │          ├── 📄 _portal.md

> │          ├── 📄 astro.config.mjs

> │          ├── 📄 package-lock.json

> │          ├── 📄 package.json

> │          └── 📂 public/

> │            ├── 📄 _public.md

> │            ├── 📄 favicon.svg

> │            ├── 📄 index.html

> │          └── 📂 src/

> │            ├── 📄 _src.md

> │            └── 📂 assets/

> │              ├── 📄 _assets.md

> │              ├── 📄 houston.webp

> │            └── 📂 content/

> │              ├── 📄 _content.md

> │              ├── 📄 content.config.ts

> │              └── 📂 docs/

> │                └── 📂 Client/

> │                  └── 📂 Business_and_Operations/

> │                    ├── 📄 Business_Notes.mdx

> │                    └── 📂 Company_Info/

> │                      ├── 📄 _Company_Info.mdx

> │                    └── 📂 Compliance_and_Regulations/

> │                      ├── 📄 _Compliance_and_Regulations.mdx

> │                    └── 📂 Procedures_and_SOPs/

> │                      ├── 📄 _Procedures_and_SOPs.mdx

> │                    └── 📂 Templates_and_Guides/

> │                      ├── 📄 _Templates_and_Guides.mdx

> │                    ├── 📄 _Business_and_Operations.mdx

> │                  └── 📂 Finance_and_Legal/

> │                    └── 📂 Banking_and_Credit/

> │                      ├── 📄 _Banking_and_Credit.mdx

> │                    └── 📂 Contracts_and_Policies/

> │                      ├── 📄 _Contracts_and_Policies.mdx

> │                    ├── 📄 Finance_Notes.mdx

> │                    └── 📂 Receipts_and_Invoices/

> │                      ├── 📄 _Receipts_and_Invoices.mdx

> │                    └── 📂 Reports_and_Statements/

> │                      ├── 📄 _Reports_and_Statements.mdx

> │                    └── 📂 Tax_Returns/

> │                      ├── 📄 _Tax_Returns.mdx

> │                    ├── 📄 _Finance_and_Legal.mdx

> │                  └── 📂 Personal/

> │                    └── 📂 Education_and_Certificates/

> │                      ├── 📄 _Education_and_Certificates.mdx

> │                    └── 📂 Health_and_Wellness/

> │                      ├── 📄 _Health_and_Wellness.mdx

> │                    └── 📂 IDs_and_Documents/

> │                      ├── 📄 _IDs_and_Documents.mdx

> │                    └── 📂 Immigration_and_Travel/

> │                      ├── 📄 _Immigration_and_Travel.mdx

> │                    ├── 📄 Personal_Notes.mdx

> │                    ├── 📄 _Personal.mdx

> │                  └── 📂 Resources/

> │                    └── 📂 Checklists_and_Guides/

> │                      ├── 📄 _Checklists_and_Guides.mdx

> │                    └── 📂 Media_and_Visuals/

> │                      ├── 📄 _Media_and_Visuals.mdx

> │                    └── 📂 Misc_References/

> │                      ├── 📄 _Misc_References.mdx

> │                    └── 📂 Templates_and_Forms/

> │                      ├── 📄 _Templates_and_Forms.mdx

> │                    ├── 📄 _Resources.mdx

> │                  ├── 📄 _03_Client.mdx

> │                └── 📂 EOS/

> │                  ├── 📄 About_QiAlly.mdx

> │                  ├── 📄 FAQ_and_Glossary.mdx

> │                  ├── 📄 Onboarding_Guide.mdx

> │                  ├── 📄 Policies_and_Procedures.mdx

> │                  ├── 📄 Using_This_System.mdx

> │                  ├── 📄 Value_and_Scope.mdx

> │                  ├── 📄 _01_EOS.mdx

> │                └── 📂 Engagements/

> │                  └── 📂 Contracts_and_Agreements/

> │                    ├── 📄 Drafts_and_Templates.mdx

> │                    ├── 📄 Signed_Contracts.mdx

> │                    ├── 📄 _Contracts_and_Agreements.mdx

> │                  ├── 📄 Project_Notes.mdx

> │                  └── 📂 Proposals_and_Offers/

> │                    ├── 📄 Active_Proposals.mdx

> │                    ├── 📄 Archived_Proposals.mdx

> │                    ├── 📄 _Proposals_and_Offers.mdx

> │                  └── 📂 Work_Summaries/

> │                    ├── 📄 Deliverables_and_Results.mdx

> │                    ├── 📄 Monthly_Summary.mdx

> │                    ├── 📄 _Work_Summaries.mdx

> │                  ├── 📄 _02_Engagements.mdx

> │                └── 📂 Tech/

> │                  ├── 📄 Portal_Info.mdx

> │                  ├── 📄 _Tech.md

> │                ├── 📄 _docs.md

> │                ├── 📄 index.mdx

> │          ├── 📄 tsconfig.json

> │        └── 📂 scripts/

> │          ├── 📄 _scripts.md

> │          ├── 📄 sync-kb-to-starlight.mjs

> │    └── 📂 c.dss/

> │      ├── 📄 LICENSE

> │      ├── 📄 README.md

> │      └── 📂 assets/

> │        ├── 📄 Gemini_Generated_Image_wos2aawos2aawos2.png

> │      └── 📂 docs/

> │        ├── 📄 000021-001.pdf

> │        ├── 📄 20251102_Statement.pdf

> │        ├── 📄 436873-000017.pdf

> │        ├── 📄 436873-000018.pdf

> │        ├── 📄 436873-000020.pdf

> │        ├── 📄 CP_575_G (1).pdf

> │        ├── 📄 CP_575_G.pdf

> │        ├── 📄 DSS_Business_Impuestos_y_mas Proposal for Copywriters - 1 - Plan.pdf

> │        ├── 📄 DSS_Business_Impuestos_y_mas Proposal for Copywriters - 2 - Factura.pdf

> │        ├── 📄 DSS_Business_Impuestos_y_mas Proposal for Copywriters - 3 - Acuerdo (1).pdf

> │        ├── 📄 DSS_Business_Impuestos_y_mas Proposal for Copywriters - 3 - Acuerdo.pdf

> │        ├── 📄 EX-Form-001-CP575G.pdf

> │        ├── 📄 EX-Invoice-002-Invoice.pdf

> │        ├── 📄 EX-Other-003-SOLIS.pdf

> │        ├── 📄 EX-Other-004-SOLISEIN.pdf

> │        ├── 📄 EX-Other-005-000021-001.pdf

> │        ├── 📄 HoneyBook_ Workflow And Community To Grow And Manage Your Business.pdf

> │        ├── 📄 HoneyBook_ Workflow And Community To Grow And Manage Your Business2.pdf

> │        ├── 📄 HoneyBook_ Workflow And Community To Grow And Manage Your Business3.pdf

> │        ├── 📄 Invoice.pdf

> │        ├── 📄 SOLIS.pdf

> │        ├── 📄 SOLISEIN.pdf

> │        ├── 📄 qi-ally_gmail-acceso_ES.html

> │      └── 📂 kb/

> │        ├── 📄 README.md

> │        ├── 📄 _2_KB.md

> │        └── 📂 engagements/

> │          └── 📂 Contracts_and_Agreements/

> │            ├── 📄 Drafts_and_Templates.md

> │            ├── 📄 Signed_Contracts.md

> │            ├── 📄 _Contracts_and_Agreements.md

> │          ├── 📄 Project_Notes.md

> │          └── 📂 Proposals_and_Offers/

> │            ├── 📄 Active_Proposals.md

> │            ├── 📄 Archived_Proposals.md

> │            ├── 📄 _Proposals_and_Offers.md

> │          └── 📂 Work_Summaries/

> │            ├── 📄 Deliverables_and_Results.md

> │            ├── 📄 Monthly_Summary.md

> │            ├── 📄 _Work_Summaries.md

> │          ├── 📄 _02_Engagements.md

> │        └── 📂 eos/

> │          ├── 📄 00.10.10_Welcome.md

> │          ├── 📄 10_Welcome.md

> │          ├── 📄 20_About_QiAlly.md

> │          ├── 📄 30_Value_and_Scope.md

> │          ├── 📄 40_Policies_and_Procedures.md

> │          ├── 📄 50_Onboarding.md

> │          ├── 📄 60_How_To.md

> │          ├── 📄 70_FAQ_and_Glossary.md

> │          ├── 📄 About_QiAlly.md

> │          ├── 📄 FAQ_and_Glossary.md

> │          ├── 📄 Onboarding_Guide.md

> │          ├── 📄 Policies_and_Procedures.md

> │          ├── 📄 Using_This_System.md

> │          ├── 📄 Value_and_Scope.md

> │          ├── 📄 _01_EOS.md

> │      └── 📂 site/

> │        ├── 📄 README.md

> │        ├── 📄 Video_Comercial_de_Llantero_a_Casa.mp4

> │        ├── 📄 index.html

> │        └── 📂 portal/

> │          ├── 📄 astro.config.mjs

> │          ├── 📄 package-lock.json

> │          ├── 📄 package.json

> │          ├── 📄 tsconfig.json

> │    └── 📂 c.hee/

> │      ├── 📄 $5,000_Cap__How_Pros_Use_Schedule_C_Corrections_and_Success-Bas.m4a

> │      ├── 📄 2024_Audit_Review - Intake Form.pdf

> │      └── 📂 2024_Audit_Review-files/

> │      ├── 📄 2024_Audit_Review-files.zip

> │        ├── 📄 WAHEED2655_IN_2022_ArchiveTaxReturn.pdf

> │        ├── 📄 WAHEED2655_IN_2023_ArchiveTaxReturn.pdf

> │        ├── 📄 WAHEED2655_US_2022_ArchiveTaxReturn.pdf

> │        ├── 📄 WAHEED2655_US_2023_ArchiveTaxReturn.pdf

> │      ├── 📄 Client_OnePage_Pitch (1).html

> │      ├── 📄 Client_OnePage_Pitch.html

> │      ├── 📄 Email_Bottom_Block (1).txt

> │      ├── 📄 Email_Bottom_Block.txt

> │      ├── 📄 IntakeInterview and Quality Review Sheet-f13614c.pdf

> │      ├── 📄 Kickoff_Agenda_Notes (1).html

> │      ├── 📄 Kickoff_Agenda_Notes.html

> │      ├── 📄 NotebookLM Mind Map (1).png

> │      ├── 📄 NotebookLM Mind Map.png

> │      ├── 📄 Solving_Back_Taxes__Case_Study.mp4

> │      ├── 📄 Stage_Task_Setup_Prompts (1).txt

> │      ├── 📄 Stage_Task_Setup_Prompts.txt

> │      ├── 📄 Tax Resolution & Engagement Packet – Haseeb Waheed.pdf

> │      ├── 📄 Tax Resolution Pitch_ Haseeb Waheed (1).pdf

> │      ├── 📄 Tax Resolution Pitch_ Haseeb Waheed.pdf

> │      ├── 📄 combinepdf.pdf

> │      ├── 📄 engagement_fee_agreement.pdf

> │      ├── 📄 engagement_packet_standard.html

> │      ├── 📄 intake.txt

> │      ├── 📄 tax-engagement-monorepo-folderpicker.zip

> │      ├── 📄 tax_resolution_packet_full 280f84a044028081b475f4593cd8a86c_all.csv

> │    └── 📂 c.inh/

> │      ├── 📄 10_Welcome.md

> │      ├── 📄 20_About_QiAlly.md

> │      ├── 📄 30_Value_and_Scope.md

> │      └── 📂 3_sites/

> │        └── 📂 3.1_innovahire-marketing-site.g/

> │          ├── 📄 LICENSE

> │          ├── 📄 README.md

> │          ├── 📄 package.json

> │          └── 📂 public/

> │            ├── 📄 index.html

> │            ├── 📄 logoround.png

> │            ├── 📄 logosquare.png

> │            ├── 📄 logowide.png

> │            ├── 📄 privacy.html

> │            ├── 📄 styles.css

> │            ├── 📄 terms.html

> │          └── 📂 scripts/

> │            ├── 📄 build.js

> │          └── 📂 src/

> │          ├── 📄 wrangler.toml

> │        └── 📂 3.2_innovahire-kb-site.g/

> │          ├── 📄 LICENSE

> │          ├── 📄 QIOS_REPO_INFO.txt

> │          ├── 📄 README.md

> │          └── 📂 docs/

> │            └── 📂 brands/

> │            └── 📂 docs/

> │              ├── 📄 QT_Client Work Summary_ Employer Account Compliance Letter & BMV Submission (2).pdf

> │            ├── 📄 index.md

> │            └── 📂 kb/

> │              └── 📂 1_welcome/

> │                ├── 📄 1_welcome.md

> │                ├── 📄 2_overview.md

> │                ├── 📄 3_about_qially.md

> │                ├── 📄 4_about_client.md

> │                ├── 📄 5_structure_map.md

> │                ├── 📄 6_onboarding.md

> │                ├── 📄 7_how_to.md

> │                ├── 📄 8_faq_and_glossary.md

> │                ├── 📄 9_msa.md

> │                ├── 📄 index.md

> │              └── 📂 2_ops/

> │                └── 📂 1_company/

> │                  ├── 📄 index.md

> │                └── 📂 2_sops/

> │                  ├── 📄 1_Onboarding.md

> │                  ├── 📄 2_Service_Delivery.md

> │                  ├── 📄 3_Compliance.md

> │                  ├── 📄 4_Communications.md

> │                  ├── 📄 5_Review-Renewal.md

> │                  ├── 📄 index.md

> │                └── 📂 3_systems/

> │                  ├── 📄 1_Overview.md

> │                  ├── 📄 2_Access_Map.md

> │                  ├── 📄 3_Integrations.md

> │                  ├── 📄 4_Credentials.md

> │                  ├── 📄 5_Backup-Recovery.md

> │                  ├── 📄 6_Logs.md

> │                  ├── 📄 index.md

> │                └── 📂 4_contracts/

> │                  ├── 📄 InnovaHireMSA.md

> │                  ├── 📄 index.md

> │                └── 📂 5_brand/

> │                  ├── 📄 1_brand_overview.md

> │                  ├── 📄 2_logo_assets_index.md

> │                  ├── 📄 3_website_notes.md

> │                  ├── 📄 4_campaigns.md

> │                  ├── 📄 5_Linked-In.md

> │                  ├── 📄 index.md

> │                ├── 📄 index.md

> │              └── 📂 3_finance/

> │                └── 📂 1_Accounting/

> │                  └── 📂 1_Assets/

> │                    ├── 📄 index.md

> │                  └── 📂 2_Banking/

> │                    ├── 📄 index.md

> │                  └── 📂 3_Income/

> │                    └── 📂 1_Salary/

> │                      ├── 📄 index.md

> │                    └── 📂 2_Business/

> │                      ├── 📄 index.md

> │                    ├── 📄 index.md

> │                  └── 📂 4_Expenses/

> │                    ├── 📄 index.md

> │                  └── 📂 6_Liabilities/

> │                    └── 📂 1_Loans/

> │                      ├── 📄 index.md

> │                    └── 📂 2_Credit-Cards/

> │                      ├── 📄 index.md

> │                    ├── 📄 index.md

> │                  └── 📂 7_Process/

> │                    ├── 📄 1_Bookkeeping_Procedures.md

> │                    ├── 📄 index.md

> │                  └── 📂 8_QuickBooks/

> │                    ├── 📄 index.md

> │                  └── 📂 9_Receipts_and_Invoices/

> │                    ├── 📄 index.md

> │                  ├── 📄 index.md

> │                └── 📂 2_Insurance/

> │                  ├── 📄 index.md

> │                └── 📂 4_Taxes/

> │                  └── 📂 1_Tax-Planning/

> │                    ├── 📄 1040_Federal_Return.md

> │                    ├── 📄 Current_Year.md

> │                    ├── 📄 Prior_Years.md

> │                    ├── 📄 Schedule_C.md

> │                    ├── 📄 index.md

> │                    ├── 📄 tax_mapping.md

> │                  └── 📂 2_Returns-and-Filings/

> │                    └── 📂 20xx/

> │                      └── 📂 1_Prepare_for_Taxes/

> │                        ├── 📄 index.md

> │                      └── 📂 2_Document_Review/

> │                        ├── 📄 index.md

> │                      └── 📂 3_Tax_Mapping/

> │                        ├── 📄 index.md

> │                      └── 📂 4_Filing_and_Supporting_Documents/

> │                        ├── 📄 index.md

> │                      ├── 📄 index.md

> │                    ├── 📄 index.md

> │                  └── 📂 3_Tax-Binders/

> │                    └── 📂 2022_Filings/

> │                      └── 📂 20_Deductions/

> │                        ├── 📄 index.md

> │                      └── 📂 30_Adjusting/

> │                        ├── 📄 index.md

> │                      └── 📂 40_Credits/

> │                        ├── 📄 index.md

> │                      └── 📂 50_Contractors/

> │                        ├── 📄 index.md

> │                        └── 📂 payroll-contractors/

> │                          └── 📂 _versions/

> │                            ├── 📄 index.md

> │                          ├── 📄 index.md

> │                      └── 📂 60_Banking/

> │                        └── 📂 banking/

> │                          └── 📂 _versions/

> │                            ├── 📄 index.md

> │                          ├── 📄 index.md

> │                        ├── 📄 index.md

> │                      └── 📂 70_Payments/

> │                        ├── 📄 index.md

> │                      └── 📂 90_Receipts/

> │                        ├── 📄 index.md

> │                      └── 📂 99_Prep/

> │                        ├── 📄 index.md

> │                      ├── 📄 index.md

> │                    └── 📂 2023_Filings/

> │                      └── 📂 00_Returns/

> │                        ├── 📄 index.md

> │                      └── 📂 10_Income/

> │                        ├── 📄 index.md

> │                        └── 📂 invoices/

> │                          ├── 📄 index.md

> │                      └── 📂 20_Deductions/

> │                        ├── 📄 index.md

> │                      └── 📂 30_Adjusting/

> │                        ├── 📄 index.md

> │                      └── 📂 40_Credits/

> │                        ├── 📄 index.md

> │                      └── 📂 50_Contractors/

> │                        ├── 📄 index.md

> │                        └── 📂 payroll-contractors/

> │                          └── 📂 _versions/

> │                            ├── 📄 index.md

> │                          ├── 📄 index.md

> │                      └── 📂 60_Banking/

> │                        └── 📂 banking/

> │                          └── 📂 _versions/

> │                            ├── 📄 index.md

> │                          ├── 📄 index.md

> │                        ├── 📄 index.md

> │                      └── 📂 70_Payments/

> │                        ├── 📄 index.md

> │                      └── 📂 90_Receipts/

> │                        ├── 📄 index.md

> │                      └── 📂 99_Prep/

> │                        ├── 📄 index.md

> │                      └── 📂 Extract Rays-Construction-LLC/

> │                        ├── 📄 Extract[1].pdf

> │                        ├── 📄 Extract[2].pdf

> │                        ├── 📄 Extract[3].pdf

> │                        ├── 📄 Extract[4].pdf

> │                        ├── 📄 Extract[5].pdf

> │                        ├── 📄 Extract[6].pdf

> │                        ├── 📄 Extract[7].pdf

> │                        ├── 📄 Extract[8].pdf

> │                        ├── 📄 Extract[9].pdf

> │                        ├── 📄 index.md

> │                      ├── 📄 index.md

> │                    └── 📂 2024_Filings/

> │                      └── 📂 10_Income/

> │                        ├── 📄 index.md

> │                        └── 📂 invoices/

> │                          ├── 📄 index.md

> │                      └── 📂 20_Deductions/

> │                        ├── 📄 index.md

> │                      └── 📂 30_Adjusting/

> │                        ├── 📄 index.md

> │                      └── 📂 40_Credits/

> │                        ├── 📄 index.md

> │                      └── 📂 50_Contractors/

> │                        ├── 📄 index.md

> │                        └── 📂 payroll-contractors/

> │                          └── 📂 _versions/

> │                            ├── 📄 index.md

> │                          ├── 📄 index.md

> │                      └── 📂 60_Banking/

> │                        └── 📂 banking/

> │                          └── 📂 _versions/

> │                            ├── 📄 index.md

> │                          ├── 📄 index.md

> │                        ├── 📄 index.md

> │                      └── 📂 70_Payments/

> │                        ├── 📄 index.md

> │                      └── 📂 90_Receipts/

> │                        ├── 📄 index.md

> │                      ├── 📄 index.md

> │                    └── 📂 2025_Filings/

> │                      └── 📂 10_Income/

> │                        ├── 📄 index.md

> │                        └── 📂 invoices/

> │                          ├── 📄 index.md

> │                      └── 📂 20_Deductions/

> │                        ├── 📄 index.md

> │                      └── 📂 50_Contractors/

> │                        ├── 📄 index.md

> │                        └── 📂 payroll-contractors/

> │                          └── 📂 _versions/

> │                            ├── 📄 index.md

> │                          ├── 📄 index.md

> │                      └── 📂 60_Banking/

> │                        └── 📂 banking/

> │                          └── 📂 _versions/

> │                            ├── 📄 index.md

> │                          ├── 📄 index.md

> │                        ├── 📄 index.md

> │                      └── 📂 90_Receipts/

> │                        ├── 📄 index.md

> │                      ├── 📄 index.md

> │                    └── 📂 20xx_Filings/

> │                      ├── 📄 index.md

> │                    ├── 📄 index.md

> │                  └── 📂 4_Estimated-Payments/

> │                    ├── 📄 index.md

> │                  └── 📂 5_Binders/

> │                    └── 📂 2021_Filings/

> │                      ├── 📄 index.md

> │                    └── 📂 2022_Filings/

> │                      └── 📂 00_Returns/

> │                        ├── 📄 index.md

> │                      └── 📂 20_Deductions/

> │                        ├── 📄 index.md

> │                      └── 📂 30_Adjusting/

> │                        ├── 📄 index.md

> │                      └── 📂 40_Credits/

> │                        ├── 📄 index.md

> │                      └── 📂 50_Contractors/

> │                        └── 📂 1099-checklist/

> │                          ├── 📄 index.md

> │                        ├── 📄 index.md

> │                      └── 📂 60_Banking/

> │                        ├── 📄 index.md

> │                      └── 📂 70_Payments/

> │                        ├── 📄 index.md

> │                      └── 📂 90_Receipts/

> │                        ├── 📄 index.md

> │                      ├── 📄 index.md

> │                    └── 📂 2023_Filings/

> │                      └── 📂 00_Returns/

> │                        ├── 📄 index.md

> │                      └── 📂 10_Income/

> │                        ├── 📄 index.md

> │                      └── 📂 20_Deductions/

> │                        ├── 📄 index.md

> │                      └── 📂 30_Adjusting/

> │                        ├── 📄 index.md

> │                      └── 📂 40_Credits/

> │                        ├── 📄 index.md

> │                      └── 📂 70_Payments/

> │                        ├── 📄 index.md

> │                      └── 📂 90_Receipts/

> │                        ├── 📄 index.md

> │                      ├── 📄 index.md

> │                    ├── 📄 index.md

> │                  ├── 📄 index.md

> │                └── 📂 5_Agreements/

> │                  ├── 📄 index.md

> │                └── 📂 6_Reports/

> │                  ├── 📄 index.md

> │                ├── 📄 index.md

> │              └── 📂 4_legal/

> │                ├── 📄 index.md

> │              └── 📂 5_projects/

> │                └── 📂 2025-09-01_innovahire-on-qially/

> │                  ├── 📄 LICENSE

> │                  ├── 📄 README.md

> │                  ├── 📄 index.md

> │                └── 📂 2025-10-01_Microsoft-Setup/

> │                  ├── 📄 07.10.10.10_Microsoft-Business-365.md

> │                  ├── 📄 INH-04.20A_Microsoft-Business-365.md

> │                  ├── 📄 index.md

> │                └── 📂 2025-10-02_Time-Keeper/

> │                  ├── 📄 index.mdx

> │                └── 📂 2025-11-01_InnovaHire_Integrated_Services/

> │                  ├── 📄 2025-11-08_Plan-of-Action.md

> │                  ├── 📄 BookkeepingPlan.md

> │                  ├── 📄 index.md

> │                └── 📂 2025-11-01_MIBOR_Member_Directory/

> │                  └── 📂 Iteration-One/

> │                    ├── 📄 SOW_Real_Estate_Agent_Search.md

> │                    └── 📂 alternative_sources/

> │                      ├── 📄 index.md

> │                    ├── 📄 billing_breakdown.md

> │                    └── 📂 client_package/

> │                      ├── 📄 README.md

> │                      ├── 📄 index.md

> │                    ├── 📄 final_summary.md

> │                    └── 📂 homes_all_pages/

> │                      ├── 📄 all_pages_combined.txt

> │                      ├── 📄 index.md

> │                      ├── 📄 page_1.txt

> │                    └── 📂 homes_html/

> │                      ├── 📄 index.md

> │                    └── 📂 homes_text_dump/

> │                      ├── 📄 index.md

> │                      ├── 📄 raw_text_all.txt

> │                      ├── 📄 raw_text_page_1.txt

> │                    ├── 📄 hybrid_puppeteer_scraper.js

> │                    ├── 📄 index.md

> │                    └── 📂 indianapolis_agents_client_package/

> │                      ├── 📄 README.md

> │                      ├── 📄 SOW_Real_Estate_Agent_Search.md

> │                      ├── 📄 final_summary.md

> │                      ├── 📄 index.md

> │                    └── 📂 indianapolis_agents_viewer/

> │                      ├── 📄 index.md

> │                    ├── 📄 package-lock.json

> │                    ├── 📄 package.json

> │                    ├── 📄 yellowpages.md

> │                  └── 📂 Iteration-Two/

> │                    ├── 📄 index.md

> │                  ├── 📄 Realtor_Directory.md

> │                  ├── 📄 index.md

> │                └── 📂 2025-11-13_Realtor_Lookup/

> │                  ├── 📄 index.md

> │                └── 📂 Brain_Sessions/

> │                  └── 📂 Lumara/

> │                    └── 📂 asset/

> │                      └── 📂 advids/

> │                        └── 📂 30s-Lumara-Mini-Commercial/

> │                          ├── 📄 index.md

> │                        ├── 📄 index.md

> │                      └── 📂 demoapp/

> │                        ├── 📄 index.html

> │                      └── 📂 logos/

> │                        ├── 📄 icon.jpeg

> │                        ├── 📄 logo.jpeg

> │                        ├── 📄 square.jpeg

> │                        ├── 📄 square2.jpeg

> │                      ├── 📄 mockup.png

> │                    └── 📂 data/

> │                      ├── 📄 Lumara_Business_Plan_Draft.csv

> │                    └── 📂 docs/

> │                    ├── 📄 how-it-works.html

> │                    ├── 📄 index.html

> │                    ├── 📄 index.md

> │                    ├── 📄 partners.html

> │                    ├── 📄 styles.css

> │                  ├── 📄 index.md

> │                ├── 📄 index.md

> │              └── 📂 6_personal/

> │                ├── 📄 10_contacts_and_ids.md

> │                ├── 📄 20_immigration_notes.md

> │                ├── 📄 30_health_or_misc.md

> │                ├── 📄 index.md

> │              └── 📂 7_misc/

> │                ├── 📄 index.md

> │              ├── 📄 index.md

> │            └── 📂 media/

> │              ├── 📄 site.html.bak

> │            └── 📂 refs/

> │              └── 📂 design/

> │              └── 📂 finance/

> │                ├── 📄 2025-11-01_Bookkeeping-Agreement.html

> │              └── 📂 html_package/

> │                ├── 📄 README.md

> │                └── 📂 agent_viewer/

> │                  ├── 📄 indianapolis_agents.csv

> │                  ├── 📄 indianapolis_agents_viewer.html

> │              └── 📂 legal/

> │              └── 📂 tech/

> │              └── 📂 training/

> │          ├── 📄 mkdocs.yml

> │          ├── 📄 package-lock.json

> │          ├── 📄 package.json

> │          └── 📂 public/

> │            ├── 📄 extra.css

> │            ├── 📄 extra.js

> │            ├── 📄 favicon.svg

> │            ├── 📄 logo.svg

> │          ├── 📄 requirements.txt

> │          └── 📂 scripts/

> │            ├── 📄 README.md

> │            ├── 📄 fix-links.js

> │            ├── 📄 sync_from_client_root.sh

> │          └── 📂 site/

> │          ├── 📄 sync_from_client_root.ps1

> │        ├── 📄 README.md

> │      ├── 📄 40_Policies_and_Procedures.md

> │      └── 📂 4_apps/

> │        └── 📂 innovahire-kb-site-realtor-lookup.g/

> │          ├── 📄 LICENSE

> │          ├── 📄 QIOS_REPO_INFO.txt

> │          ├── 📄 QIOS_SAFE_TO_DELETE.txt

> │          ├── 📄 README.md

> │          ├── 📄 convert-csv-to-json.js

> │          ├── 📄 index.html

> │          ├── 📄 package-lock.json

> │          ├── 📄 package.json

> │          └── 📂 public/

> │            └── 📂 data/

> │              ├── 📄 Contacts_2025_11_12.csv

> │              ├── 📄 realtors.json

> │          └── 📂 src/

> │            ├── 📄 App.jsx

> │            └── 📂 components/

> │              ├── 📄 Filters.jsx

> │              ├── 📄 Table.jsx

> │            ├── 📄 index.css

> │            ├── 📄 main.jsx

> │          ├── 📄 vite.config.js

> │      ├── 📄 50_Onboarding.md

> │      └── 📂 5_tools/

> │        └── 📂 automations/

> │          ├── 📄 contacts_to_realtors.py

> │          ├── 📄 copy-commands

> │          ├── 📄 csv_to_json.py

> │          ├── 📄 qicode_indexer.py

> │        └── 📂 exports/

> │        └── 📂 lib/

> │        └── 📂 reporting/

> │      ├── 📄 60_How_To.md

> │      └── 📂 6_sys/

> │        └── 📂 config/

> │        └── 📂 infra/

> │        └── 📂 security/

> │      ├── 📄 70_FAQ_and_Glossary.md

> │      └── 📂 Accounting/

> │        ├── 📄 index.md

> │        └── 📂 supporting_files/

> │          └── 📂 PunchPro/

> │          ├── 📄 index.md

> │      └── 📂 Brain_Sessions/

> │        ├── 📄 index.md

> │      └── 📂 Brand/

> │        └── 📂 10_Brand-Guide/

> │          ├── 📄 03.50.10.10_Branding_Guide.md

> │          ├── 📄 _10_Brand-Guide.md

> │        └── 📂 20_Logos/

> │          ├── 📄 _20_Logos.md

> │          ├── 📄 logoround.png

> │          ├── 📄 logosquare.png

> │          ├── 📄 logowide.png

> │        └── 📂 30_Marketing/

> │          └── 📂 10_Strategy/

> │            ├── 📄 _10_Strategy.md

> │            ├── 📄 index.md

> │          └── 📂 20_Campaigns/

> │            ├── 📄 _20_Campaigns.md

> │            ├── 📄 index.md

> │          └── 📂 30_Assets/

> │            ├── 📄 _30_Assets.md

> │            ├── 📄 index.md

> │          └── 📂 40_Socials/

> │            ├── 📄 _40_Socials.md

> │            ├── 📄 index.md

> │          ├── 📄 _30_Marketing.md

> │          ├── 📄 index.md

> │        └── 📂 40_Website/

> │          ├── 📄 03.50.40.10_Website_Assets.md

> │          ├── 📄 _40_Website.md

> │        ├── 📄 _50_Brand.md

> │      └── 📂 Business_Ops/

> │        └── 📂 1_Company_Info/

> │          ├── 📄 _1_Company_Info.md

> │        └── 📂 2_Procedures_and_SOPs/

> │          ├── 📄 10_incident-001.md

> │          ├── 📄 20_release.md

> │          ├── 📄 _2_Procedures_and_SOPs.md

> │          ├── 📄 _Procedures_and_SOPs.md

> │        └── 📂 3_Compliance_and_Regulations/

> │          ├── 📄 _Compliance_and_Regulations.md

> │        ├── 📄 Business_Notes.md

> │        ├── 📄 _Business_and_Operations.md

> │      └── 📂 Checklists_and_Guides/

> │        ├── 📄 _Checklists_and_Guides.md

> │      └── 📂 Contracts_and_Agreements/

> │        ├── 📄 Drafts_and_Templates.md

> │        ├── 📄 Signed_Contracts.md

> │        ├── 📄 _Contracts_and_Agreements.md

> │      └── 📂 Education_and_Certificates/

> │        ├── 📄 _Education_and_Certificates.md

> │      └── 📂 Finance_and_Legal/

> │        └── 📂 Accounting/

> │          └── 📂 Assets/

> │            └── 📂 04.10.40.10_Real-Estate/

> │              ├── 📄 10_deed.pdf

> │              ├── 📄 20_property-tax.pdf

> │              ├── 📄 _04.10.40.10_Real-Estate.md

> │            └── 📂 04.10.40.20_Investments/

> │              ├── 📄 10_2024_Investment-Statements.pdf

> │              ├── 📄 _04.10.40.20_Investments.md

> │            ├── 📄 _Assets.md

> │            ├── 📄 _index.md

> │          └── 📂 Banking/

> │            ├── 📄 _Banking.md

> │            ├── 📄 _index.md

> │            └── 📂 check-images/

> │              ├── 📄 _check-images.md

> │              ├── 📄 _index.md

> │          └── 📂 Expenses/

> │            ├── 📄 _Expenses.md

> │            ├── 📄 _index.md

> │          └── 📂 Income/

> │            └── 📂 04.10.30.10_Salary/

> │              ├── 📄 10_pay-stubs.pdf

> │              ├── 📄 20_w2-forms.pdf

> │              ├── 📄 _04.10.30.10_Salary.md

> │            └── 📂 04.10.30.20_Business/

> │              ├── 📄 10_invoices.pdf

> │              ├── 📄 20_expenses.pdf

> │              ├── 📄 _04.10.30.20_Business.md

> │            ├── 📄 _Income.md

> │            ├── 📄 _index.md

> │          └── 📂 Liabilities/

> │            └── 📂 04.10.50.10_Loans/

> │              ├── 📄 10_loan-agreement.pdf

> │              ├── 📄 _04.10.50.10_Loans.md

> │            └── 📂 04.10.50.20_Credit-Cards/

> │              ├── 📄 10_credit-statement.pdf

> │              ├── 📄 _04.10.50.20_Credit-Cards.md

> │            ├── 📄 _Liabilities.md

> │            ├── 📄 _index.md

> │          └── 📂 Process/

> │            ├── 📄 04.20.20.10_Bookkeeping_Procedures.md

> │            ├── 📄 06.00_Bookkeeping_Procedures.md

> │            ├── 📄 _Process.md

> │          └── 📂 QuickBooks/

> │            ├── 📄 BankRules.csv

> │            ├── 📄 BankRules.xls

> │            ├── 📄 BankRules_QuickBooks.csv

> │            ├── 📄 InnovaHire LLC_Account List.csv

> │            ├── 📄 InnovaHire LLC_Account List.xlsx

> │            ├── 📄 InnovaHire_LLC_Bank_Feed_Rules_FINAL.csv

> │            ├── 📄 InnovaHire_LLC_Bank_Feed_Rules_FINAL.xls

> │            ├── 📄 _QuickBooks.md

> │          └── 📂 Receipts/

> │            ├── 📄 _Receipts_and_Invoices.md

> │          ├── 📄 _Accounting.md

> │        └── 📂 Billing/

> │          └── 📂 04.30.40_Expenses/

> │            ├── 📄 10_monthly-expenses.pdf

> │            ├── 📄 20_receipts-summary.pdf

> │            ├── 📄 _04.30.40_Expenses.md

> │          ├── 📄 _04.30_Billing-and-Payments.md

> │        └── 📂 Contracts_and_Policies/

> │          ├── 📄 _Contracts_and_Policies.md

> │        ├── 📄 Finance_Notes.md

> │        └── 📂 Insurance/

> │          ├── 📄 Insurance_Audits.md

> │          ├── 📄 _Insurance.md

> │        ├── 📄 README.md

> │        └── 📂 Reports_and_Statements/

> │          └── 📂 04.40.40_Budgets-Forcasts/

> │            ├── 📄 10_2025-q4-budget.pdf

> │            ├── 📄 _04.40.40_Budgets-Forcasts.md

> │          ├── 📄 04.80.10_Financial_Reports.md

> │          └── 📂 04.80.50_Budgets-Forcasts/

> │            ├── 📄 2025-Q4-budget.md

> │            ├── 📄 _04.80.50_Budgets-Forcasts.md

> │          ├── 📄 H.030_Financial_Reports.md

> │          ├── 📄 _04.40_Reports.md

> │          ├── 📄 _04.80_Reports.md

> │          ├── 📄 _80_Reports.md

> │          ├── 📄 _Reports_and_Statements.md

> │        └── 📂 Tax_Returns/

> │          └── 📂 04.20.10_Tax-Planning/

> │            ├── 📄 1040_Federal_Return.md

> │            ├── 📄 H.02.00.10_Current_Year.md

> │            ├── 📄 H.020.020_Prior_Years.md

> │            ├── 📄 Schedule_C.md

> │            ├── 📄 _04.20.10_Tax-Planning.md

> │          └── 📂 04.20.20_Returns-and-Filings/

> │            └── 📂 2023/

> │              └── 📂 01_Prepare_for_Taxes/

> │                ├── 📄 01_engagement-letter.pdf

> │                ├── 📄 02_trial-balance.pdf

> │                ├── 📄 03_adjusting-entries.pdf

> │                ├── 📄 04_tax-return-prep.pdf

> │                ├── 📄 05_tax-provision.pdf

> │                ├── 📄 06_financial-statements.pdf

> │                ├── 📄 07_client-approval-docs.pdf

> │                ├── 📄 _01_Prepare_for_Taxes.md

> │              └── 📂 02_Document_Review/

> │                ├── 📄 01_approved-documents.pdf

> │                ├── 📄 02_document-reviews.pdf

> │                ├── 📄 _02_Document_Review.md

> │              └── 📂 03_Tax_Mapping/

> │                ├── 📄 01_tax-mapping.pdf

> │                ├── 📄 02_adjustments-summary.pdf

> │                ├── 📄 _03_Tax_Mapping.md

> │              └── 📂 04_Filing_and_Supporting_Documents/

> │                ├── 📄 01_filed-1040.pdf

> │                ├── 📄 02_filed-schedule-c.pdf

> │                ├── 📄 03_supporting-documents.pdf

> │                ├── 📄 _04_Filing_and_Supporting_Documents.md

> │              ├── 📄 10_1040_fed-return.pdf

> │              ├── 📄 20_schedule-c.pdf

> │              ├── 📄 30_tax-workpapers.pdf

> │              ├── 📄 _2023.md

> │            └── 📂 2024/

> │              ├── 📄 10_1040_fed-return.pdf

> │              ├── 📄 20_schedule-c.pdf

> │              ├── 📄 30_tax-workpapers.pdf

> │              ├── 📄 _2024.md

> │            ├── 📄 _04.20.20_Returns-and-Filings.md

> │          └── 📂 04.20.30_Tax-Binders/

> │            └── 📂 2021_Filings/

> │              ├── 📄 INH_Tax-return-2021_ITIN Application.pdf

> │              ├── 📄 _2021_Filings.md

> │            └── 📂 2022_Filings/

> │              └── 📂 20_Deductions/

> │                ├── 📄 _20_Deductions.md

> │                ├── 📄 _index.md

> │                ├── 📄 index.html

> │              └── 📂 30_Adjusting/

> │                ├── 📄 _30_Adjusting.md

> │                ├── 📄 _index.md

> │              └── 📂 40_Credits/

> │                ├── 📄 _40_Credits.md

> │                ├── 📄 _index.md

> │              └── 📂 50_Contractors/

> │                ├── 📄 Print 1099 Information Sheet.pdf

> │                ├── 📄 Rays Construction LLC_1099_07277.pdf

> │                ├── 📄 Rays Construction LLC_1099_09b61.pdf

> │                ├── 📄 Rays Construction LLC_1099_10742.pdf

> │                ├── 📄 Rays Construction LLC_1099_29c79.pdf

> │                ├── 📄 Rays Construction LLC_1099_328e1.pdf

> │                ├── 📄 Rays Construction LLC_1099_32db2.pdf

> │                ├── 📄 Rays Construction LLC_1099_429ab.pdf

> │                ├── 📄 Rays Construction LLC_1099_4e93c.pdf

> │                ├── 📄 Rays Construction LLC_1099_55f6e.pdf

> │                ├── 📄 Rays Construction LLC_1099_94455.pdf

> │                ├── 📄 Rays Construction LLC_1099_a424d.pdf

> │                ├── 📄 Rays Construction LLC_1099_a6179.pdf

> │                ├── 📄 Rays Construction LLC_1099_ae4ed.pdf

> │                ├── 📄 Rays Construction LLC_1099_bc8a7.pdf

> │                ├── 📄 Rays Construction LLC_1099_d8795.pdf

> │                ├── 📄 Rays Construction LLC_1099_da8fb.pdf

> │                ├── 📄 Rays Construction LLC_1099_e65f6.pdf

> │                ├── 📄 Rays Construction LLC_1099_ef83f.pdf

> │                ├── 📄 Rays Construction LLC_1099_fa137.pdf

> │                ├── 📄 _50_Contractors.md

> │                ├── 📄 _index.md

> │                ├── 📄 index.html

> │                └── 📂 payroll-contractors/

> │                  ├── 📄 _payroll-contractors.md

> │                  └── 📂 _versions/

> │                    ├── 📄 __versions.md

> │                    ├── 📄 index.html

> │                    ├── 📄 index.md-2.html

> │                    ├── 📄 index.md.html

> │                  ├── 📄 index.html

> │                  ├── 📄 index.md

> │                  ├── 📄 index.md.bak

> │                  ├── 📄 index.md.bak2

> │              └── 📂 60_Banking/

> │                ├── 📄 1.pdf

> │                ├── 📄 10.pdf

> │                ├── 📄 11.pdf

> │                ├── 📄 12.pdf

> │                ├── 📄 2.pdf

> │                ├── 📄 251.pdf

> │                ├── 📄 252.pdf

> │                ├── 📄 253.pdf

> │                ├── 📄 254.pdf

> │                ├── 📄 255.pdf

> │                ├── 📄 256.pdf

> │                ├── 📄 257.pdf

> │                ├── 📄 258.pdf

> │                ├── 📄 3.pdf

> │                ├── 📄 4.pdf

> │                ├── 📄 5.pdf

> │                ├── 📄 6.pdf

> │                ├── 📄 7.pdf

> │                ├── 📄 8.pdf

> │                ├── 📄 9.pdf

> │                ├── 📄 _60_Banking.md

> │                ├── 📄 _index.md

> │                └── 📂 banking/

> │                  ├── 📄 _banking.md

> │                  └── 📂 _versions/

> │                    ├── 📄 __versions.md

> │                    ├── 📄 index.html

> │                    ├── 📄 index.md-2.html

> │                    ├── 📄 index.md.html

> │                  ├── 📄 index.html

> │                  ├── 📄 index.md

> │                  ├── 📄 index.md.bak

> │                  ├── 📄 index.md.bak2

> │                ├── 📄 index.html

> │              └── 📂 70_Payments/

> │                ├── 📄 _70_Payments.md

> │                ├── 📄 _index.md

> │              └── 📂 90_Receipts/

> │                ├── 📄 _90_Receipts.md

> │                ├── 📄 _index.md

> │              └── 📂 99_Prep/

> │                ├── 📄 2022-Tax Binder.pdf

> │                ├── 📄 60.2022_builtbyrays.pdf

> │                ├── 📄 _99_Prep.md

> │                ├── 📄 _index.md

> │              ├── 📄 INH_Tax-return-2022.pdf

> │              ├── 📄 _2022_Filings.md

> │            └── 📂 2023_Filings/

> │              └── 📂 00_Returns/

> │                ├── 📄 1040x_signature_page.pdf

> │                ├── 📄 _00_Returns.md

> │                ├── 📄 _index.md

> │                ├── 📄 bbr_TaxReturn.20250930T915949Z (1).pdf

> │              └── 📂 10_Income/

> │                ├── 📄 _10_Income.md

> │                ├── 📄 _index.md

> │                └── 📂 invoices/

> │                  ├── 📄 _invoices.md

> │                  ├── 📄 sample-invoice.json

> │              └── 📂 20_Deductions/

> │                ├── 📄 _20_Deductions.md

> │                ├── 📄 _index.md

> │                ├── 📄 index.html

> │              └── 📂 30_Adjusting/

> │                ├── 📄 _30_Adjusting.md

> │                ├── 📄 _index.md

> │              └── 📂 40_Credits/

> │                ├── 📄 _40_Credits.md

> │                ├── 📄 _index.md

> │              └── 📂 50_Contractors/

> │                ├── 📄 Print 1099 Information Sheet.pdf

> │                ├── 📄 Rays Construction LLC_1099_07277.pdf

> │                ├── 📄 Rays Construction LLC_1099_09b61.pdf

> │                ├── 📄 Rays Construction LLC_1099_10742.pdf

> │                ├── 📄 Rays Construction LLC_1099_29c79.pdf

> │                ├── 📄 Rays Construction LLC_1099_328e1.pdf

> │                ├── 📄 Rays Construction LLC_1099_32db2.pdf

> │                ├── 📄 Rays Construction LLC_1099_429ab.pdf

> │                ├── 📄 Rays Construction LLC_1099_4e93c.pdf

> │                ├── 📄 Rays Construction LLC_1099_55f6e.pdf

> │                ├── 📄 Rays Construction LLC_1099_94455.pdf

> │                ├── 📄 Rays Construction LLC_1099_a424d.pdf

> │                ├── 📄 Rays Construction LLC_1099_a6179.pdf

> │                ├── 📄 Rays Construction LLC_1099_ae4ed.pdf

> │                ├── 📄 Rays Construction LLC_1099_bc8a7.pdf

> │                ├── 📄 Rays Construction LLC_1099_d8795.pdf

> │                ├── 📄 Rays Construction LLC_1099_da8fb.pdf

> │                ├── 📄 Rays Construction LLC_1099_e65f6.pdf

> │                ├── 📄 Rays Construction LLC_1099_ef83f.pdf

> │                ├── 📄 Rays Construction LLC_1099_fa137.pdf

> │                ├── 📄 _50_Contractors.md

> │                ├── 📄 _index.md

> │                ├── 📄 index.html

> │                └── 📂 payroll-contractors/

> │                  ├── 📄 _payroll-contractors.md

> │                  └── 📂 _versions/

> │                    ├── 📄 __versions.md

> │                    ├── 📄 index.html

> │                    ├── 📄 index.md-2.html

> │                    ├── 📄 index.md.html

> │                  ├── 📄 index.html

> │                  ├── 📄 index.md

> │                  ├── 📄 index.md.bak

> │                  ├── 📄 index.md.bak2

> │              └── 📂 60_Banking/

> │                ├── 📄 1.pdf

> │                ├── 📄 10.pdf

> │                ├── 📄 11.pdf

> │                ├── 📄 12.pdf

> │                ├── 📄 2.pdf

> │                ├── 📄 251.pdf

> │                ├── 📄 252.pdf

> │                ├── 📄 253.pdf

> │                ├── 📄 254.pdf

> │                ├── 📄 255.pdf

> │                ├── 📄 256.pdf

> │                ├── 📄 257.pdf

> │                ├── 📄 258.pdf

> │                ├── 📄 3.pdf

> │                ├── 📄 4.pdf

> │                ├── 📄 5.pdf

> │                ├── 📄 6.pdf

> │                ├── 📄 7.pdf

> │                ├── 📄 8.pdf

> │                ├── 📄 9.pdf

> │                ├── 📄 _60_Banking.md

> │                ├── 📄 _index.md

> │                └── 📂 banking/

> │                  ├── 📄 _banking.md

> │                  └── 📂 _versions/

> │                    ├── 📄 __versions.md

> │                    ├── 📄 index.html

> │                    ├── 📄 index.md-2.html

> │                    ├── 📄 index.md.html

> │                  ├── 📄 index.html

> │                  ├── 📄 index.md

> │                  ├── 📄 index.md.bak

> │                  ├── 📄 index.md.bak2

> │                ├── 📄 index.html

> │              └── 📂 70_Payments/

> │                ├── 📄 _70_Payments.md

> │                ├── 📄 _index.md

> │              └── 📂 90_Receipts/

> │                ├── 📄 _90_Receipts.md

> │                ├── 📄 _index.md

> │              └── 📂 99_Prep/

> │                ├── 📄 09302025_RAYS CONSTRUCTION LLC Profit &Loss January through Dece.pdf

> │                ├── 📄 2023-Tax Binder.pdf

> │                ├── 📄 BasicCompanyFinancials Copy.pdf

> │                ├── 📄 ExpandedCompanyFinancials.pdf

> │                ├── 📄 _99_Prep.md

> │                ├── 📄 _index.md

> │                ├── 📄 bbr-tax-scedule-2023.pdf

> │                ├── 📄 e2187d81-51f2-47ae-bc8a-7872f3635794.pdf

> │              └── 📂 Extract Rays-Construction-LLC/

> │                ├── 📄 Extract[1].pdf

> │                ├── 📄 Extract[2].pdf

> │                ├── 📄 Extract[3].pdf

> │                ├── 📄 Extract[4].pdf

> │                ├── 📄 Extract[5].pdf

> │                ├── 📄 Extract[6].pdf

> │                ├── 📄 Extract[7].pdf

> │                ├── 📄 Extract[8].pdf

> │                ├── 📄 Extract[9].pdf

> │                ├── 📄 _Extract Rays-Construction-LLC.md

> │              ├── 📄 _2023_Filings.md

> │              ├── 📄 _index.md

> │            └── 📂 2024_Filings/

> │              └── 📂 10_Income/

> │                ├── 📄 _10_Income.md

> │                ├── 📄 _index.md

> │                └── 📂 invoices/

> │                  ├── 📄 _invoices.md

> │                  ├── 📄 sample-invoice.json

> │              ├── 📄 2024-Tax Binder.pdf

> │              └── 📂 20_Deductions/

> │                ├── 📄 _20_Deductions.md

> │                ├── 📄 _index.md

> │                ├── 📄 index.html

> │              └── 📂 30_Adjusting/

> │                ├── 📄 _30_Adjusting.md

> │                ├── 📄 _index.md

> │              └── 📂 40_Credits/

> │                ├── 📄 _40_Credits.md

> │                ├── 📄 _index.md

> │              └── 📂 50_Contractors/

> │                ├── 📄 Print 1099 Information Sheet.pdf

> │                ├── 📄 Rays Construction LLC_1099_07277.pdf

> │                ├── 📄 Rays Construction LLC_1099_09b61.pdf

> │                ├── 📄 Rays Construction LLC_1099_10742.pdf

> │                ├── 📄 Rays Construction LLC_1099_29c79.pdf

> │                ├── 📄 Rays Construction LLC_1099_328e1.pdf

> │                ├── 📄 Rays Construction LLC_1099_32db2.pdf

> │                ├── 📄 Rays Construction LLC_1099_429ab.pdf

> │                ├── 📄 Rays Construction LLC_1099_4e93c.pdf

> │                ├── 📄 Rays Construction LLC_1099_55f6e.pdf

> │                ├── 📄 Rays Construction LLC_1099_94455.pdf

> │                ├── 📄 Rays Construction LLC_1099_a424d.pdf

> │                ├── 📄 Rays Construction LLC_1099_a6179.pdf

> │                ├── 📄 Rays Construction LLC_1099_ae4ed.pdf

> │                ├── 📄 Rays Construction LLC_1099_bc8a7.pdf

> │                ├── 📄 Rays Construction LLC_1099_d8795.pdf

> │                ├── 📄 Rays Construction LLC_1099_da8fb.pdf

> │                ├── 📄 Rays Construction LLC_1099_e65f6.pdf

> │                ├── 📄 Rays Construction LLC_1099_ef83f.pdf

> │                ├── 📄 Rays Construction LLC_1099_fa137.pdf

> │                ├── 📄 _50_Contractors.md

> │                ├── 📄 _index.md

> │                ├── 📄 index.html

> │                └── 📂 payroll-contractors/

> │                  ├── 📄 _payroll-contractors.md

> │                  └── 📂 _versions/

> │                    ├── 📄 __versions.md

> │                    ├── 📄 index.html

> │                    ├── 📄 index.md-2.html

> │                    ├── 📄 index.md.html

> │                  ├── 📄 index.html

> │                  ├── 📄 index.md

> │                  ├── 📄 index.md.bak

> │                  ├── 📄 index.md.bak2

> │              └── 📂 60_Banking/

> │                ├── 📄 1.pdf

> │                ├── 📄 10.pdf

> │                ├── 📄 11.pdf

> │                ├── 📄 12.pdf

> │                ├── 📄 2.pdf

> │                ├── 📄 251.pdf

> │                ├── 📄 252.pdf

> │                ├── 📄 253.pdf

> │                ├── 📄 254.pdf

> │                ├── 📄 255.pdf

> │                ├── 📄 256.pdf

> │                ├── 📄 257.pdf

> │                ├── 📄 258.pdf

> │                ├── 📄 3.pdf

> │                ├── 📄 4.pdf

> │                ├── 📄 5.pdf

> │                ├── 📄 6.pdf

> │                ├── 📄 7.pdf

> │                ├── 📄 8.pdf

> │                ├── 📄 9.pdf

> │                ├── 📄 _60_Banking.md

> │                ├── 📄 _index.md

> │                └── 📂 banking/

> │                  ├── 📄 _banking.md

> │                  └── 📂 _versions/

> │                    ├── 📄 __versions.md

> │                    ├── 📄 index.html

> │                    ├── 📄 index.md-2.html

> │                    ├── 📄 index.md.html

> │                  ├── 📄 index.html

> │                  ├── 📄 index.md

> │                  ├── 📄 index.md.bak

> │                  ├── 📄 index.md.bak2

> │                ├── 📄 index.html

> │              └── 📂 70_Payments/

> │                ├── 📄 _70_Payments.md

> │                ├── 📄 _index.md

> │              └── 📂 90_Receipts/

> │                ├── 📄 _90_Receipts.md

> │                ├── 📄 _index.md

> │              ├── 📄 _2024_Filings.md

> │              ├── 📄 _index.md

> │            └── 📂 2025_Filings/

> │              └── 📂 10_Income/

> │                ├── 📄 _10_Income.md

> │                └── 📂 invoices/

> │                  ├── 📄 _invoices.md

> │                  ├── 📄 sample-invoice.json

> │              └── 📂 20_Deductions/

> │                ├── 📄 _20_Deductions.md

> │                ├── 📄 index.html

> │              └── 📂 50_Contractors/

> │                ├── 📄 Print 1099 Information Sheet.pdf

> │                ├── 📄 Rays Construction LLC_1099_07277.pdf

> │                ├── 📄 Rays Construction LLC_1099_09b61.pdf

> │                ├── 📄 Rays Construction LLC_1099_10742.pdf

> │                ├── 📄 Rays Construction LLC_1099_29c79.pdf

> │                ├── 📄 Rays Construction LLC_1099_328e1.pdf

> │                ├── 📄 Rays Construction LLC_1099_32db2.pdf

> │                ├── 📄 Rays Construction LLC_1099_429ab.pdf

> │                ├── 📄 Rays Construction LLC_1099_4e93c.pdf

> │                ├── 📄 Rays Construction LLC_1099_55f6e.pdf

> │                ├── 📄 Rays Construction LLC_1099_94455.pdf

> │                ├── 📄 Rays Construction LLC_1099_a424d.pdf

> │                ├── 📄 Rays Construction LLC_1099_a6179.pdf

> │                ├── 📄 Rays Construction LLC_1099_ae4ed.pdf

> │                ├── 📄 Rays Construction LLC_1099_bc8a7.pdf

> │                ├── 📄 Rays Construction LLC_1099_d8795.pdf

> │                ├── 📄 Rays Construction LLC_1099_da8fb.pdf

> │                ├── 📄 Rays Construction LLC_1099_e65f6.pdf

> │                ├── 📄 Rays Construction LLC_1099_ef83f.pdf

> │                ├── 📄 Rays Construction LLC_1099_fa137.pdf

> │                ├── 📄 _50_Contractors.md

> │                ├── 📄 _index.md

> │                ├── 📄 index.html

> │                └── 📂 payroll-contractors/

> │                  ├── 📄 _payroll-contractors.md

> │                  └── 📂 _versions/

> │                    ├── 📄 __versions.md

> │                    ├── 📄 index.html

> │                    ├── 📄 index.md-2.html

> │                    ├── 📄 index.md.html

> │                  ├── 📄 index.html

> │                  ├── 📄 index.md

> │                  ├── 📄 index.md.bak

> │                  ├── 📄 index.md.bak2

> │              └── 📂 60_Banking/

> │                ├── 📄 1.pdf

> │                ├── 📄 10.pdf

> │                ├── 📄 11.pdf

> │                ├── 📄 12.pdf

> │                ├── 📄 2.pdf

> │                ├── 📄 251.pdf

> │                ├── 📄 252.pdf

> │                ├── 📄 253.pdf

> │                ├── 📄 254.pdf

> │                ├── 📄 255.pdf

> │                ├── 📄 256.pdf

> │                ├── 📄 257.pdf

> │                ├── 📄 258.pdf

> │                ├── 📄 3.pdf

> │                ├── 📄 4.pdf

> │                ├── 📄 5.pdf

> │                ├── 📄 6.pdf

> │                ├── 📄 7.pdf

> │                ├── 📄 8.pdf

> │                ├── 📄 9.pdf

> │                ├── 📄 _60_Banking.md

> │                └── 📂 banking/

> │                  ├── 📄 _banking.md

> │                  └── 📂 _versions/

> │                    ├── 📄 __versions.md

> │                    ├── 📄 index.html

> │                    ├── 📄 index.md-2.html

> │                    ├── 📄 index.md.html

> │                  ├── 📄 index.html

> │                  ├── 📄 index.md

> │                  ├── 📄 index.md.bak

> │                  ├── 📄 index.md.bak2

> │                ├── 📄 index.html

> │              └── 📂 90_Receipts/

> │                ├── 📄 _90_Receipts.md

> │              ├── 📄 _2025_Filings.md

> │              ├── 📄 _index.md

> │            ├── 📄 _04.20.30_Tax-Binders.md

> │          └── 📂 10_Tax-Planning/

> │            ├── 📄 1040_Federal_Return.md

> │            ├── 📄 Schedule_C.md

> │            ├── 📄 _10_Tax-Planning.md

> │          └── 📂 20_Estimated-Payments/

> │            ├── 📄 _20_Estimated-Payments.md

> │            ├── 📄 index.md

> │          └── 📂 30_Tax-Binders/

> │            └── 📂 2021_Filings/

> │              ├── 📄 INH_Tax-return-2021_ITIN Application.pdf

> │              ├── 📄 _2021_Filings.md

> │            └── 📂 2022_Filings/

> │              └── 📂 00_Returns/

> │                ├── 📄 INH_Tax-return-2022.pdf

> │                ├── 📄 _00_Returns.md

> │                ├── 📄 index.md

> │              └── 📂 20_Deductions/

> │                ├── 📄 _20_Deductions.md

> │                ├── 📄 _index.md

> │              └── 📂 30_Adjusting/

> │                ├── 📄 _30_Adjusting.md

> │                ├── 📄 _index.md

> │              └── 📂 40_Credits/

> │                ├── 📄 _40_Credits.md

> │                ├── 📄 _index.md

> │              └── 📂 50_Contractors/

> │                └── 📂 1099-checklist/

> │                  ├── 📄 _1099-checklist.md

> │                  ├── 📄 index.md

> │                ├── 📄 _50_Contractors.md

> │                ├── 📄 index.md

> │              └── 📂 60_Banking/

> │                ├── 📄 _60_Banking.md

> │                ├── 📄 _index.md

> │                ├── 📄 index.html

> │              └── 📂 70_Payments/

> │                ├── 📄 _70_Payments.md

> │                ├── 📄 _index.md

> │              └── 📂 90_Receipts/

> │                ├── 📄 _90_Receipts.md

> │                ├── 📄 _index.md

> │              ├── 📄 _2022_Filings.md

> │            └── 📂 2023_Filings/

> │              └── 📂 00_Returns/

> │                ├── 📄 _00_Returns.md

> │                ├── 📄 index.md

> │              └── 📂 10_Income/

> │                ├── 📄 _10_Income.md

> │                ├── 📄 index.md

> │              └── 📂 20_Deductions/

> │                ├── 📄 _20_Deductions.md

> │                ├── 📄 index.md

> │              └── 📂 30_Adjusting/

> │                ├── 📄 _30_Adjusting.md

> │                ├── 📄 index.md

> │              └── 📂 40_Credits/

> │                ├── 📄 _40_Credits.md

> │                ├── 📄 index.md

> │              └── 📂 70_Payments/

> │                ├── 📄 _70_Payments.md

> │                ├── 📄 index.md

> │              └── 📂 90_Receipts/

> │                ├── 📄 _90_Receipts.md

> │                ├── 📄 index.md

> │              ├── 📄 _2023_Filings.md

> │              ├── 📄 index.md

> │            ├── 📄 _30_Tax-Binders.md

> │            ├── 📄 index.md

> │          ├── 📄 Munoz_Corp_DOR_Letter.docx

> │          ├── 📄 _04.10_TAX.md

> │          ├── 📄 _04.20_Tax.md

> │          ├── 📄 _10_TAX.md

> │          ├── 📄 _Tax_Returns.md

> │          ├── 📄 _tax.md

> │        ├── 📄 _Finance_and_Legal.md

> │      └── 📂 Health_and_Wellness/

> │        ├── 📄 _Health_and_Wellness.md

> │      └── 📂 IDs_and_Documents/

> │        ├── 📄 _IDs_and_Documents.md

> │      └── 📂 Immigration_and_Travel/

> │        └── 📂 00_Drafts_and_Strategy/

> │          ├── 📄 2025-09-01_QiAlly_Leg_Strat_v01_final.pdf

> │          ├── 📄 2025-09-05_QiAlly_Leg_Timeline_v01_final.pdf

> │          ├── 📄 2025-09-10_QiAlly_Leg_Draft_v01_Aff_draft.pdf

> │          ├── 📄 2025-09-15_QiAlly_Leg_Timeline_v01_review_final.pdf

> │          ├── 📄 _00_Drafts_and_Strategy.md

> │        └── 📂 10_Bio_and_IDs/

> │          ├── 📄 2025-09-28_QiAlly_Leg_Bio_BC.pdf

> │          ├── 📄 2025-09-28_QiAlly_Leg_Bio_ID.pdf

> │          ├── 📄 2025-09-28_QiAlly_Leg_Bio_MC.pdf

> │          ├── 📄 2025-09-28_QiAlly_Leg_Bio_PC.pdf

> │          ├── 📄 _10_Bio_and_IDs.md

> │        └── 📂 20_Employment/

> │          ├── 📄 2025-09-28_QiAlly_Leg_Emp_OL.pdf

> │          ├── 📄 2025-09-28_QiAlly_Leg_Emp_PS.pdf

> │          ├── 📄 2025-09-28_QiAlly_Leg_Emp_W2.pdf

> │          ├── 📄 _20_Employment.md

> │        └── 📂 30_Financial/

> │          ├── 📄 2025-09-28_QiAlly_Leg_Fin_BS.pdf

> │          ├── 📄 2025-09-28_QiAlly_Leg_Fin_EIS.pdf

> │          ├── 📄 2025-09-28_QiAlly_Leg_Fin_Tax.pdf

> │          ├── 📄 _30_Financial.md

> │        └── 📂 40_Other_Evidence/

> │          ├── 📄 2025-09-28_QiAlly_Leg_Other_LOS.pdf

> │          ├── 📄 2025-09-28_QiAlly_Leg_Other_PR.pdf

> │          ├── 📄 2025-09-28_QiAlly_Leg_Other_UB.pdf

> │          ├── 📄 _40_Other_Evidence.md

> │        └── 📂 50_Form_Filings/

> │          └── 📂 10_I-589 (Asylum)/

> │            ├── 📄 2025-09-28_QiAlly_Leg_i589_Aff_v01_draft.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_i589_CL_v01_final.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_i589_EOS.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_i589_SD.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_i589_form.pdf

> │            ├── 📄 _10_I-589 (Asylum).md

> │          └── 📂 20_I-360 (Special Immigrant)/

> │            ├── 📄 2025-09-28_QiAlly_Leg_i360_CL_v01_final.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_i360_EOSvc.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_i360_PS_v01_final.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_i360_form.pdf

> │            ├── 📄 _20_I-360 (Special Immigrant).md

> │          └── 📂 30_I-130 (Family Sponsorship)/

> │            ├── 📄 2025-09-28_QiAlly_Leg_i130_CL_v01_final.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_i130_EOR_v01_final.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_i130_SP.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_i130_form.pdf

> │            ├── 📄 _30_I-130 (Family Sponsorship).md

> │          └── 📂 40_I-765 (Employment Authorization)/

> │            ├── 📄 2025-09-28_QiAlly_Leg_i765_CL_v01_final.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_i765_ED.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_i765_EOS.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_i765_form.pdf

> │            ├── 📄 _40_I-765 (Employment Authorization).md

> │          └── 📂 50_I-485 (Adjustment of Status)/

> │            ├── 📄 2025-09-28_QiAlly_Leg_i485_Bio.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_i485_CL_v01_final.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_i485_EOS.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_i485_ME.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_i485_form.pdf

> │            ├── 📄 _50_I-485 (Adjustment of Status).md

> │          └── 📂 60_Change_of_Address/

> │            ├── 📄 2025-09-28_QiAlly_Leg_COA_form.pdf

> │            ├── 📄 _60_Change_of_Address.md

> │          └── 📂 70_Indiana_BMV_License/

> │            ├── 📄 2025-09-28_QiAlly_Leg_BMV_Apps.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_BMV_Docs.pdf

> │            ├── 📄 _70_Indiana_BMV_License.md

> │          └── 📂 80_Social_Security_Applications/

> │            ├── 📄 2025-09-28_QiAlly_Leg_Soc-Sec_Apps.pdf

> │            ├── 📄 2025-09-28_QiAlly_Leg_Soc-Sec_Docs.pdf

> │            ├── 📄 _80_Social_Security_Applications.md

> │          ├── 📄 _50_Form_Filings.md

> │        ├── 📄 _Immigration.md

> │        ├── 📄 _Immigration_and_Travel.md

> │      └── 📂 InnovaHire_Accounting/

> │        ├── 📄 index.md

> │        └── 📂 supporting_files/

> │          └── 📂 PunchPro/

> │          ├── 📄 index.md

> │      ├── 📄 LICENSE

> │      └── 📂 Lumara/

> │        ├── 📄 index.md

> │      └── 📂 Media_and_Visuals/

> │        ├── 📄 _Media_and_Visuals.md

> │      └── 📂 Misc_References/

> │        ├── 📄 _Misc_References.md

> │      └── 📂 Personal/

> │      ├── 📄 Personal_Notes.md

> │      └── 📂 Proposals_and_Offers/

> │        └── 📂 2025-11-01_InnovaHire_Integrated_Services/

> │          ├── 📄 111.md

> │          ├── 📄 2025-11-08_Plan-of-Action.md

> │          ├── 📄 2025-11-08_Plan-of-action.html

> │          └── 📂 Bookkeeping/

> │            ├── 📄 _Bookkeeping.md

> │          ├── 📄 _InnovaHire_Integrated_Services.md

> │        ├── 📄 Active_Proposals.md

> │        ├── 📄 Archived_Proposals.md

> │        ├── 📄 _Proposals_and_Offers.md

> │      └── 📂 PunchPro/

> │        └── 📂 Lead_Contacts/

> │          ├── 📄 Businesses_2025_11_09.csv

> │          ├── 📄 Contacts_2025_11_09.csv

> │        ├── 📄 index.md

> │      └── 📂 Qi-Mind/

> │        ├── 📄 README.md

> │        ├── 📄 directory-map.html

> │        ├── 📄 navigator-3d.html

> │        ├── 📄 navigator.html

> │        ├── 📄 run-navigator.bat

> │        ├── 📄 run-navigator.ps1

> │      ├── 📄 QuickLinks.mdx

> │      ├── 📄 README.md

> │      └── 📂 Templates_and_Forms/

> │        ├── 📄 05.00.10_innova_hire_direct_hire_agreement.md

> │        ├── 📄 05.30.70_innova_hire_direct_hire_agreement.md

> │        ├── 📄 05.40.10_msa.md

> │        ├── 📄 10_info-release-template.md

> │        ├── 📄 10_msa.md

> │        └── 📂 Authorizations/

> │          ├── 📄 05.60.10_Info-Release-Template.md

> │          ├── 📄 Info-Release-Template.md

> │          ├── 📄 _05.60_Authorizations.md

> │          ├── 📄 _index.md

> │        ├── 📄 Innova Hire Direct Hire Agreement.docx

> │        ├── 📄 Proposal - Proposal For Direct Hire Staffing Services.pptx

> │        ├── 📄 _Templates_and_Forms.md

> │        ├── 📄 innova_hire_direct_hire_agreement.md

> │      └── 📂 Work_Summaries/

> │        └── 📂 2025-09-01_innovahire-on-qially/

> │          ├── 📄 LICENSE

> │          ├── 📄 README.md

> │          ├── 📄 _innovahire-on-qially.md

> │          ├── 📄 index.html

> │        └── 📂 2025-10-01_Microsoft-Setup/

> │          ├── 📄 07.10.10.10_Microsoft-Business-365.md

> │          ├── 📄 INH-04.20A_Microsoft-Business-365.md

> │          ├── 📄 _INH-04.20_Microsoft-Setup.md

> │        └── 📂 2025-10-02_Time-Keeper/

> │          ├── 📄 answer.pptx

> │          ├── 📄 index.mdx

> │        └── 📂 2025-11-01_MIBOR_Member_Directory/

> │          └── 📂 Iteration-One/

> │            ├── 📄 SOW_Real_Estate_Agent_Search.md

> │            ├── 📄 _Iteration-One.md

> │            ├── 📄 _inh_grab-home-text.md

> │            ├── 📄 add-agents.mjs

> │            ├── 📄 add-emails-and-dedup.mjs

> │            └── 📂 alternative_sources/

> │              ├── 📄 _alternative_sources.md

> │              ├── 📄 source_7_www_kw_com.html

> │            ├── 📄 billing_breakdown.md

> │            ├── 📄 bypass-homes-scraper.mjs

> │            └── 📂 client_package/

> │              ├── 📄 README.md

> │              ├── 📄 _client_package.md

> │              ├── 📄 indianapolis_agents.csv

> │              ├── 📄 indianapolis_agents_viewer.html

> │            ├── 📄 create-viewer.mjs

> │            ├── 📄 debug-full-page.mjs

> │            ├── 📄 debug-pagination.mjs

> │            ├── 📄 dedup-summary.mjs

> │            ├── 📄 dedup-with-emails.mjs

> │            ├── 📄 final-summary.mjs

> │            ├── 📄 final_summary.md

> │            ├── 📄 fix-viewer.mjs

> │            ├── 📄 grab-homes-text.mjs

> │            └── 📂 homes_all_pages/

> │              ├── 📄 _homes_all_pages.md

> │              ├── 📄 all_pages_combined.txt

> │              ├── 📄 page_1.txt

> │            └── 📂 homes_html/

> │              ├── 📄 _homes_html.md

> │              ├── 📄 homes_main_content.html

> │              ├── 📄 homes_page.html

> │            └── 📂 homes_text_dump/

> │              ├── 📄 _homes_text_dump.md

> │              ├── 📄 raw_text_all.txt

> │              ├── 📄 raw_text_page_1.txt

> │            ├── 📄 hybrid_puppeteer_scraper.js

> │            └── 📂 indianapolis_agents_client_package/

> │              ├── 📄 README.md

> │              ├── 📄 SOW_Real_Estate_Agent_Search.md

> │              ├── 📄 _indianapolis_agents_client_package.md

> │              ├── 📄 final_summary.md

> │              ├── 📄 indianapolis_agents_v1.csv

> │              ├── 📄 indianapolis_agents_viewer.html

> │            ├── 📄 indianapolis_agents_v1.csv

> │            └── 📂 indianapolis_agents_viewer/

> │            ├── 📄 indianapolis_agents_viewer.html

> │              ├── 📄 _indianapolis_agents_viewer.md

> │              ├── 📄 indianapolis_agents_viewer.html

> │            ├── 📄 kw_agents.csv

> │            ├── 📄 package-lock.json

> │            ├── 📄 package.json

> │            ├── 📄 parse-kw-agents.mjs

> │            ├── 📄 parse-yellowpages.mjs

> │            ├── 📄 sample-yellowpages.csv

> │            ├── 📄 save-homes-html.mjs

> │            ├── 📄 scrape-allpages-real-estate.mjs

> │            ├── 📄 scrape-homes-all-pages.mjs

> │            ├── 📄 test-different-urls.mjs

> │            ├── 📄 test-page-2.mjs

> │            ├── 📄 try-alternative-sources.mjs

> │            ├── 📄 yellowpages-summary.mjs

> │            ├── 📄 yellowpages-to-csv.mjs

> │            ├── 📄 yellowpages.md

> │            ├── 📄 yellowpages_real_estate.csv

> │            ├── 📄 yellowpages_real_estate_deduplicated.csv

> │            ├── 📄 yellowpages_real_estate_updated.csv

> │          └── 📂 Iteration-Two/

> │            ├── 📄 _Iteration-Two.md

> │          ├── 📄 MIBOR_Scraper_Summary.md

> │          ├── 📄 QiAlly Document Services — MIBOR Member Directory Capture & Automation.md

> │          ├── 📄 _MIBOR_Member_Directory.md

> │          ├── 📄 _QiScripts.md

> │        ├── 📄 Deliverables_and_Results.md

> │        ├── 📄 Monthly_Summary.md

> │        ├── 📄 _Work_Summaries.md

> │      ├── 📄 _02_Engagements.md

> │      ├── 📄 _03_Client.md

> │      ├── 📄 _Personal.md

> │      ├── 📄 _Resources.md

> │      └── 📂 assets/

> │        ├── 📄 houston.webp

> │        ├── 📄 houston.webp.bak

> │      └── 📂 automations/

> │        ├── 📄 contacts_to_realtors.py

> │        ├── 📄 copy-commands

> │        ├── 📄 csv_to_json.py

> │        ├── 📄 qicode_indexer.py

> │      └── 📂 c.inh-OS-site-kb/

> │        ├── 📄 CLOUDFLARE_BUILD.md

> │        ├── 📄 CODE_OF_CONDUCT.md

> │        ├── 📄 Dockerfile

> │        ├── 📄 LICENSE.txt

> │        ├── 📄 QUARTZ_CUSTOMIZATION.md

> │        ├── 📄 README.md

> │        └── 📂 content/

> │          └── 📂 docs/

> │            ├── 📄 QT_Client Work Summary_ Employer Account Compliance Letter & BMV Submission (2).pdf

> │            ├── 📄 index.md

> │          ├── 📄 index.md

> │          └── 📂 kb/

> │            └── 📂 1_welcome/

> │              ├── 📄 1_welcome.md

> │              ├── 📄 2_overview.md

> │              ├── 📄 3_about_qially.md

> │              ├── 📄 4_about_client.md

> │              ├── 📄 5_structure_map.md

> │              ├── 📄 6_onboarding.md

> │              ├── 📄 7_how_to.md

> │              ├── 📄 8_faq_and_glossary.md

> │              ├── 📄 9_msa.md

> │              ├── 📄 index.md

> │            └── 📂 2_ops/

> │              └── 📂 1_company/

> │                ├── 📄 index.md

> │              └── 📂 2_sops/

> │                ├── 📄 1_Onboarding.md

> │                ├── 📄 2_Service_Delivery.md

> │                ├── 📄 3_Compliance.md

> │                ├── 📄 4_Communications.md

> │                ├── 📄 5_Review-Renewal.md

> │                ├── 📄 index.md

> │              └── 📂 3_systems/

> │                ├── 📄 1_Overview.md

> │                ├── 📄 2_Access_Map.md

> │                ├── 📄 3_Integrations.md

> │                ├── 📄 4_Credentials.md

> │                ├── 📄 5_Backup-Recovery.md

> │                ├── 📄 6_Logs.md

> │                ├── 📄 index.md

> │              └── 📂 4_contracts/

> │                ├── 📄 InnovaHireMSA.md

> │                ├── 📄 index.md

> │              └── 📂 5_brand/

> │                ├── 📄 1_brand_overview.md

> │                ├── 📄 2_logo_assets_index.md

> │                ├── 📄 3_website_notes.md

> │                ├── 📄 4_campaigns.md

> │                ├── 📄 5_Linked-In.md

> │                ├── 📄 index.md

> │              ├── 📄 index.md

> │            └── 📂 3_finance/

> │              └── 📂 1_Accounting/

> │                └── 📂 1_Assets/

> │                  ├── 📄 index.md

> │                └── 📂 2_Banking/

> │                  ├── 📄 index.md

> │                └── 📂 3_Income/

> │                  └── 📂 1_Salary/

> │                    ├── 📄 index.md

> │                  └── 📂 2_Business/

> │                    ├── 📄 index.md

> │                  ├── 📄 index.md

> │                └── 📂 4_Expenses/

> │                  ├── 📄 index.md

> │                └── 📂 6_Liabilities/

> │                  └── 📂 1_Loans/

> │                    ├── 📄 index.md

> │                  └── 📂 2_Credit-Cards/

> │                    ├── 📄 index.md

> │                  ├── 📄 index.md

> │                └── 📂 7_Process/

> │                  ├── 📄 1_Bookkeeping_Procedures.md

> │                  ├── 📄 index.md

> │                └── 📂 8_QuickBooks/

> │                  ├── 📄 index.md

> │                └── 📂 9_Receipts_and_Invoices/

> │                  ├── 📄 index.md

> │                ├── 📄 index.md

> │              └── 📂 2_Insurance/

> │                ├── 📄 index.md

> │              └── 📂 4_Taxes/

> │                └── 📂 1_Tax-Planning/

> │                  ├── 📄 1040_Federal_Return.md

> │                  ├── 📄 Current_Year.md

> │                  ├── 📄 Prior_Years.md

> │                  ├── 📄 Schedule_C.md

> │                  ├── 📄 index.md

> │                  ├── 📄 tax_mapping.md

> │                └── 📂 2_Returns-and-Filings/

> │                  └── 📂 20xx/

> │                    └── 📂 1_Prepare_for_Taxes/

> │                      ├── 📄 index.md

> │                    └── 📂 2_Document_Review/

> │                      ├── 📄 index.md

> │                    └── 📂 3_Tax_Mapping/

> │                      ├── 📄 index.md

> │                    └── 📂 4_Filing_and_Supporting_Documents/

> │                      ├── 📄 index.md

> │                    ├── 📄 index.md

> │                  ├── 📄 index.md

> │                └── 📂 3_Tax-Binders/

> │                  └── 📂 2022_Filings/

> │                    └── 📂 20_Deductions/

> │                      ├── 📄 index.md

> │                    └── 📂 30_Adjusting/

> │                      ├── 📄 index.md

> │                    └── 📂 40_Credits/

> │                      ├── 📄 index.md

> │                    └── 📂 50_Contractors/

> │                      ├── 📄 index.md

> │                      └── 📂 payroll-contractors/

> │                        └── 📂 _versions/

> │                          ├── 📄 index.md

> │                        ├── 📄 index.md

> │                    └── 📂 60_Banking/

> │                      └── 📂 banking/

> │                        └── 📂 _versions/

> │                          ├── 📄 index.md

> │                        ├── 📄 index.md

> │                      ├── 📄 index.md

> │                    └── 📂 70_Payments/

> │                      ├── 📄 index.md

> │                    └── 📂 90_Receipts/

> │                      ├── 📄 index.md

> │                    └── 📂 99_Prep/

> │                      ├── 📄 index.md

> │                    ├── 📄 index.md

> │                  └── 📂 2023_Filings/

> │                    └── 📂 00_Returns/

> │                      ├── 📄 index.md

> │                    └── 📂 10_Income/

> │                      ├── 📄 index.md

> │                      └── 📂 invoices/

> │                        ├── 📄 index.md

> │                    └── 📂 20_Deductions/

> │                      ├── 📄 index.md

> │                    └── 📂 30_Adjusting/

> │                      ├── 📄 index.md

> │                    └── 📂 40_Credits/

> │                      ├── 📄 index.md

> │                    └── 📂 50_Contractors/

> │                      ├── 📄 index.md

> │                      └── 📂 payroll-contractors/

> │                        └── 📂 _versions/

> │                          ├── 📄 index.md

> │                        ├── 📄 index.md

> │                    └── 📂 60_Banking/

> │                      └── 📂 banking/

> │                        └── 📂 _versions/

> │                          ├── 📄 index.md

> │                        ├── 📄 index.md

> │                      ├── 📄 index.md

> │                    └── 📂 70_Payments/

> │                      ├── 📄 index.md

> │                    └── 📂 90_Receipts/

> │                      ├── 📄 index.md

> │                    └── 📂 99_Prep/

> │                      ├── 📄 index.md

> │                    └── 📂 Extract Rays-Construction-LLC/

> │                      ├── 📄 Extract[1].pdf

> │                      ├── 📄 Extract[2].pdf

> │                      ├── 📄 Extract[3].pdf

> │                      ├── 📄 Extract[4].pdf

> │                      ├── 📄 Extract[5].pdf

> │                      ├── 📄 Extract[6].pdf

> │                      ├── 📄 Extract[7].pdf

> │                      ├── 📄 Extract[8].pdf

> │                      ├── 📄 Extract[9].pdf

> │                      ├── 📄 index.md

> │                    ├── 📄 index.md

> │                  └── 📂 2024_Filings/

> │                    └── 📂 10_Income/

> │                      ├── 📄 index.md

> │                      └── 📂 invoices/

> │                        ├── 📄 index.md

> │                    └── 📂 20_Deductions/

> │                      ├── 📄 index.md

> │                    └── 📂 30_Adjusting/

> │                      ├── 📄 index.md

> │                    └── 📂 40_Credits/

> │                      ├── 📄 index.md

> │                    └── 📂 50_Contractors/

> │                      ├── 📄 index.md

> │                      └── 📂 payroll-contractors/

> │                        └── 📂 _versions/

> │                          ├── 📄 index.md

> │                        ├── 📄 index.md

> │                    └── 📂 60_Banking/

> │                      └── 📂 banking/

> │                        └── 📂 _versions/

> │                          ├── 📄 index.md

> │                        ├── 📄 index.md

> │                      ├── 📄 index.md

> │                    └── 📂 70_Payments/

> │                      ├── 📄 index.md

> │                    └── 📂 90_Receipts/

> │                      ├── 📄 index.md

> │                    ├── 📄 index.md

> │                  └── 📂 2025_Filings/

> │                    └── 📂 10_Income/

> │                      ├── 📄 index.md

> │                      └── 📂 invoices/

> │                        ├── 📄 index.md

> │                    └── 📂 20_Deductions/

> │                      ├── 📄 index.md

> │                    └── 📂 50_Contractors/

> │                      ├── 📄 index.md

> │                      └── 📂 payroll-contractors/

> │                        └── 📂 _versions/

> │                          ├── 📄 index.md

> │                        ├── 📄 index.md

> │                    └── 📂 60_Banking/

> │                      └── 📂 banking/

> │                        └── 📂 _versions/

> │                          ├── 📄 index.md

> │                        ├── 📄 index.md

> │                      ├── 📄 index.md

> │                    └── 📂 90_Receipts/

> │                      ├── 📄 index.md

> │                    ├── 📄 index.md

> │                  └── 📂 20xx_Filings/

> │                    ├── 📄 index.md

> │                  ├── 📄 index.md

> │                └── 📂 4_Estimated-Payments/

> │                  ├── 📄 index.md

> │                └── 📂 5_Binders/

> │                  └── 📂 2021_Filings/

> │                    ├── 📄 index.md

> │                  └── 📂 2022_Filings/

> │                    └── 📂 00_Returns/

> │                      ├── 📄 index.md

> │                    └── 📂 20_Deductions/

> │                      ├── 📄 index.md

> │                    └── 📂 30_Adjusting/

> │                      ├── 📄 index.md

> │                    └── 📂 40_Credits/

> │                      ├── 📄 index.md

> │                    └── 📂 50_Contractors/

> │                      └── 📂 1099-checklist/

> │                        ├── 📄 index.md

> │                      ├── 📄 index.md

> │                    └── 📂 60_Banking/

> │                      ├── 📄 index.md

> │                    └── 📂 70_Payments/

> │                      ├── 📄 index.md

> │                    └── 📂 90_Receipts/

> │                      ├── 📄 index.md

> │                    ├── 📄 index.md

> │                  └── 📂 2023_Filings/

> │                    └── 📂 00_Returns/

> │                      ├── 📄 index.md

> │                    └── 📂 10_Income/

> │                      ├── 📄 index.md

> │                    └── 📂 20_Deductions/

> │                      ├── 📄 index.md

> │                    └── 📂 30_Adjusting/

> │                      ├── 📄 index.md

> │                    └── 📂 40_Credits/

> │                      ├── 📄 index.md

> │                    └── 📂 70_Payments/

> │                      ├── 📄 index.md

> │                    └── 📂 90_Receipts/

> │                      ├── 📄 index.md

> │                    ├── 📄 index.md

> │                  ├── 📄 index.md

> │                ├── 📄 index.md

> │              └── 📂 5_Agreements/

> │                ├── 📄 index.md

> │              └── 📂 6_Reports/

> │                ├── 📄 index.md

> │              ├── 📄 index.md

> │            └── 📂 4_legal/

> │              ├── 📄 index.md

> │            └── 📂 5_projects/

> │              └── 📂 2025-09-01_innovahire-on-qially/

> │                ├── 📄 LICENSE

> │                ├── 📄 README.md

> │                ├── 📄 index.md

> │              └── 📂 2025-10-01_Microsoft-Setup/

> │                ├── 📄 07.10.10.10_Microsoft-Business-365.md

> │                ├── 📄 INH-04.20A_Microsoft-Business-365.md

> │                ├── 📄 index.md

> │              └── 📂 2025-10-02_Time-Keeper/

> │                ├── 📄 index.md

> │                ├── 📄 index.mdx

> │              └── 📂 2025-11-01_InnovaHire_Integrated_Services/

> │                ├── 📄 2025-11-08_Plan-of-Action.md

> │                ├── 📄 BookkeepingPlan.md

> │                ├── 📄 index.md

> │              └── 📂 2025-11-01_MIBOR_Member_Directory/

> │                └── 📂 Iteration-One/

> │                  ├── 📄 SOW_Real_Estate_Agent_Search.md

> │                  └── 📂 alternative_sources/

> │                    ├── 📄 index.md

> │                  ├── 📄 billing_breakdown.md

> │                  └── 📂 client_package/

> │                    ├── 📄 README.md

> │                    ├── 📄 index.md

> │                  ├── 📄 final_summary.md

> │                  └── 📂 homes_all_pages/

> │                    ├── 📄 all_pages_combined.txt

> │                    ├── 📄 index.md

> │                    ├── 📄 page_1.txt

> │                  └── 📂 homes_html/

> │                    ├── 📄 index.md

> │                  └── 📂 homes_text_dump/

> │                    ├── 📄 index.md

> │                    ├── 📄 raw_text_all.txt

> │                    ├── 📄 raw_text_page_1.txt

> │                  ├── 📄 hybrid_puppeteer_scraper.js

> │                  ├── 📄 index.md

> │                  └── 📂 indianapolis_agents_client_package/

> │                    ├── 📄 README.md

> │                    ├── 📄 SOW_Real_Estate_Agent_Search.md

> │                    ├── 📄 final_summary.md

> │                    ├── 📄 index.md

> │                  └── 📂 indianapolis_agents_viewer/

> │                    ├── 📄 index.md

> │                  ├── 📄 package-lock.json

> │                  ├── 📄 package.json

> │                  ├── 📄 yellowpages.md

> │                └── 📂 Iteration-Two/

> │                  ├── 📄 index.md

> │                ├── 📄 Realtor_Directory.md

> │                ├── 📄 index.md

> │              └── 📂 2025-11-13_Realtor_Lookup/

> │                ├── 📄 index.md

> │              └── 📂 Brain_Sessions/

> │                └── 📂 Lumara/

> │                  └── 📂 asset/

> │                    └── 📂 advids/

> │                      └── 📂 30s-Lumara-Mini-Commercial/

> │                        ├── 📄 index.md

> │                      ├── 📄 index.md

> │                    └── 📂 demoapp/

> │                      ├── 📄 index.html

> │                    └── 📂 logos/

> │                      ├── 📄 icon.jpeg

> │                      ├── 📄 logo.jpeg

> │                      ├── 📄 square.jpeg

> │                      ├── 📄 square2.jpeg

> │                    ├── 📄 mockup.png

> │                  └── 📂 data/

> │                    ├── 📄 Lumara_Business_Plan_Draft.csv

> │                  ├── 📄 how-it-works.html

> │                  ├── 📄 index.html

> │                  ├── 📄 index.md

> │                  ├── 📄 partners.html

> │                  ├── 📄 styles.css

> │                └── 📂 PunchPro/

> │                  ├── 📄 index.md

> │                ├── 📄 index.md

> │              ├── 📄 index.md

> │            └── 📂 6_personal/

> │              ├── 📄 10_contacts_and_ids.md

> │              ├── 📄 20_immigration_notes.md

> │              ├── 📄 30_health_or_misc.md

> │              ├── 📄 index.md

> │            └── 📂 7_misc/

> │              ├── 📄 index.md

> │            ├── 📄 index.md

> │          └── 📂 media/

> │            ├── 📄 index.md

> │            ├── 📄 site.html.bak

> │          └── 📂 refs/

> │            └── 📂 design/

> │            └── 📂 finance/

> │              ├── 📄 2025-11-01_Bookkeeping-Agreement.html

> │            └── 📂 html_package/

> │              ├── 📄 README.md

> │              └── 📂 agent_viewer/

> │                ├── 📄 indianapolis_agents.csv

> │                ├── 📄 indianapolis_agents_viewer.html

> │            ├── 📄 index.md

> │            └── 📂 legal/

> │            └── 📂 tech/

> │            └── 📂 training/

> │        └── 📂 docs/

> │          └── 📂 advanced/

> │            ├── 📄 architecture.md

> │            ├── 📄 creating components.md

> │            ├── 📄 index.md

> │            ├── 📄 making plugins.md

> │            ├── 📄 paths.md

> │          ├── 📄 authoring content.md

> │          ├── 📄 build.md

> │          ├── 📄 configuration.md

> │          └── 📂 features/

> │            ├── 📄 Citations.md

> │            ├── 📄 Docker Support.md

> │            ├── 📄 Latex.md

> │            ├── 📄 Mermaid diagrams.md

> │            ├── 📄 Obsidian compatibility.md

> │            ├── 📄 OxHugo compatibility.md

> │            ├── 📄 RSS Feed.md

> │            ├── 📄 Roam Research compatibility.md

> │            ├── 📄 SPA Routing.md

> │            ├── 📄 backlinks.md

> │            ├── 📄 breadcrumbs.md

> │            ├── 📄 callouts.md

> │            ├── 📄 comments.md

> │            ├── 📄 darkmode.md

> │            ├── 📄 explorer.md

> │            ├── 📄 folder and tag listings.md

> │            ├── 📄 full-text search.md

> │            ├── 📄 graph view.md

> │            ├── 📄 i18n.md

> │            ├── 📄 index.md

> │            ├── 📄 popover previews.md

> │            ├── 📄 private pages.md

> │            ├── 📄 reader mode.md

> │            ├── 📄 recent notes.md

> │            ├── 📄 social images.md

> │            ├── 📄 syntax highlighting.md

> │            ├── 📄 table of contents.md

> │            ├── 📄 upcoming features.md

> │            ├── 📄 wikilinks.md

> │          ├── 📄 hosting.md

> │          └── 📂 images/

> │            ├── 📄 custom-social-image-preview-dark.png

> │            ├── 📄 custom-social-image-preview-light.png

> │            ├── 📄 dns records.png

> │            ├── 📄 giscus-discussion.png

> │            ├── 📄 giscus-example.png

> │            ├── 📄 giscus-repo.png

> │            ├── 📄 giscus-results.png

> │            ├── 📄 github-init-repo-options.png

> │            ├── 📄 github-quick-setup.png

> │            ├── 📄 quartz transform pipeline.png

> │            ├── 📄 quartz-layout-desktop.png

> │            ├── 📄 quartz-layout-mobile.png

> │            ├── 📄 quartz-layout-tablet.png

> │            ├── 📄 social-image-preview-dark.png

> │            ├── 📄 social-image-preview-light.png

> │          ├── 📄 index.md

> │          ├── 📄 layout-components.md

> │          ├── 📄 layout.md

> │          ├── 📄 migrating from Quartz 3.md

> │          ├── 📄 philosophy.md

> │          └── 📂 plugins/

> │            ├── 📄 AliasRedirects.md

> │            ├── 📄 Assets.md

> │            ├── 📄 CNAME.md

> │            ├── 📄 Citations.md

> │            ├── 📄 ComponentResources.md

> │            ├── 📄 ContentIndex.md

> │            ├── 📄 ContentPage.md

> │            ├── 📄 CrawlLinks.md

> │            ├── 📄 CreatedModifiedDate.md

> │            ├── 📄 CustomOgImages.md

> │            ├── 📄 Description.md

> │            ├── 📄 ExplicitPublish.md

> │            ├── 📄 Favicon.md

> │            ├── 📄 FolderPage.md

> │            ├── 📄 Frontmatter.md

> │            ├── 📄 GitHubFlavoredMarkdown.md

> │            ├── 📄 HardLineBreaks.md

> │            ├── 📄 Latex.md

> │            ├── 📄 NotFoundPage.md

> │            ├── 📄 ObsidianFlavoredMarkdown.md

> │            ├── 📄 OxHugoFlavoredMarkdown.md

> │            ├── 📄 RemoveDrafts.md

> │            ├── 📄 RoamFlavoredMarkdown.md

> │            ├── 📄 Static.md

> │            ├── 📄 SyntaxHighlighting.md

> │            ├── 📄 TableOfContents.md

> │            ├── 📄 TagPage.md

> │            ├── 📄 index.md

> │          ├── 📄 setting up your GitHub repository.md

> │          ├── 📄 showcase.md

> │          └── 📂 tags/

> │            ├── 📄 component.md

> │            ├── 📄 plugin.md

> │          ├── 📄 upgrading.md

> │        ├── 📄 globals.d.ts

> │        ├── 📄 index.d.ts

> │        ├── 📄 package-lock.json

> │        ├── 📄 package.json

> │        └── 📂 quartz/

> │        ├── 📄 quartz.config.ts

> │        ├── 📄 quartz.layout.ts

> │          ├── 📄 bootstrap-cli.mjs

> │          ├── 📄 bootstrap-worker.mjs

> │          ├── 📄 build.ts

> │          ├── 📄 cfg.ts

> │          └── 📂 cli/

> │            ├── 📄 args.js

> │            ├── 📄 constants.js

> │            ├── 📄 handlers.js

> │            ├── 📄 helpers.js

> │          └── 📂 components/

> │            ├── 📄 ArticleTitle.tsx

> │            ├── 📄 Backlinks.tsx

> │            ├── 📄 Body.tsx

> │            ├── 📄 Breadcrumbs.tsx

> │            ├── 📄 Comments.tsx

> │            ├── 📄 ConditionalRender.tsx

> │            ├── 📄 ContentMeta.tsx

> │            ├── 📄 Darkmode.tsx

> │            ├── 📄 Date.tsx

> │            ├── 📄 DesktopOnly.tsx

> │            ├── 📄 Explorer.tsx

> │            ├── 📄 Flex.tsx

> │            ├── 📄 Footer.tsx

> │            ├── 📄 Graph.tsx

> │            ├── 📄 Head.tsx

> │            ├── 📄 Header.tsx

> │            ├── 📄 MobileOnly.tsx

> │            ├── 📄 OverflowList.tsx

> │            ├── 📄 PageList.tsx

> │            ├── 📄 PageTitle.tsx

> │            ├── 📄 ReaderMode.tsx

> │            ├── 📄 RecentNotes.tsx

> │            ├── 📄 Search.tsx

> │            ├── 📄 Spacer.tsx

> │            ├── 📄 SplashScreen.tsx

> │            ├── 📄 TableOfContents.tsx

> │            ├── 📄 TagList.tsx

> │            ├── 📄 index.ts

> │            └── 📂 pages/

> │              ├── 📄 404.tsx

> │              ├── 📄 Content.tsx

> │              ├── 📄 FolderContent.tsx

> │              ├── 📄 TagContent.tsx

> │            ├── 📄 renderPage.tsx

> │            └── 📂 scripts/

> │              ├── 📄 callout.inline.ts

> │              ├── 📄 checkbox.inline.ts

> │              ├── 📄 clipboard.inline.ts

> │              ├── 📄 comments.inline.ts

> │              ├── 📄 darkmode.inline.ts

> │              ├── 📄 explorer.inline.ts

> │              ├── 📄 graph.inline.ts

> │              ├── 📄 mermaid.inline.ts

> │              ├── 📄 popover.inline.ts

> │              ├── 📄 readermode.inline.ts

> │              ├── 📄 search.inline.ts

> │              ├── 📄 spa.inline.ts

> │              ├── 📄 toc.inline.ts

> │              ├── 📄 util.ts

> │            └── 📂 styles/

> │              ├── 📄 backlinks.scss

> │              ├── 📄 breadcrumbs.scss

> │              ├── 📄 clipboard.scss

> │              ├── 📄 contentMeta.scss

> │              ├── 📄 darkmode.scss

> │              ├── 📄 explorer.scss

> │              ├── 📄 footer.scss

> │              ├── 📄 graph.scss

> │              ├── 📄 legacyToc.scss

> │              ├── 📄 listPage.scss

> │              ├── 📄 mermaid.inline.scss

> │              ├── 📄 popover.scss

> │              ├── 📄 readermode.scss

> │              ├── 📄 recentNotes.scss

> │              ├── 📄 search.scss

> │              ├── 📄 toc.scss

> │            ├── 📄 types.ts

> │          └── 📂 i18n/

> │            ├── 📄 index.ts

> │            └── 📂 locales/

> │              ├── 📄 ar-SA.ts

> │              ├── 📄 ca-ES.ts

> │              ├── 📄 cs-CZ.ts

> │              ├── 📄 de-DE.ts

> │              ├── 📄 definition.ts

> │              ├── 📄 en-GB.ts

> │              ├── 📄 en-US.ts

> │              ├── 📄 es-ES.ts

> │              ├── 📄 fa-IR.ts

> │              ├── 📄 fi-FI.ts

> │              ├── 📄 fr-FR.ts

> │              ├── 📄 he-IL.ts

> │              ├── 📄 hu-HU.ts

> │              ├── 📄 id-ID.ts

> │              ├── 📄 it-IT.ts

> │              ├── 📄 ja-JP.ts

> │              ├── 📄 kk-KZ.ts

> │              ├── 📄 ko-KR.ts

> │              ├── 📄 lt-LT.ts

> │              ├── 📄 nb-NO.ts

> │              ├── 📄 nl-NL.ts

> │              ├── 📄 pl-PL.ts

> │              ├── 📄 pt-BR.ts

> │              ├── 📄 ro-RO.ts

> │              ├── 📄 ru-RU.ts

> │              ├── 📄 th-TH.ts

> │              ├── 📄 tr-TR.ts

> │              ├── 📄 uk-UA.ts

> │              ├── 📄 vi-VN.ts

> │              ├── 📄 zh-CN.ts

> │              ├── 📄 zh-TW.ts

> │          └── 📂 plugins/

> │            └── 📂 emitters/

> │              ├── 📄 404.tsx

> │              ├── 📄 aliases.ts

> │              ├── 📄 assets.ts

> │              ├── 📄 cname.ts

> │              ├── 📄 componentResources.ts

> │              ├── 📄 contentIndex.tsx

> │              ├── 📄 contentPage.tsx

> │              ├── 📄 favicon.ts

> │              ├── 📄 folderPage.tsx

> │              ├── 📄 helpers.ts

> │              ├── 📄 index.ts

> │              ├── 📄 ogImage.tsx

> │              ├── 📄 static.ts

> │              ├── 📄 tagPage.tsx

> │            └── 📂 filters/

> │              ├── 📄 draft.ts

> │              ├── 📄 explicit.ts

> │              ├── 📄 index.ts

> │            ├── 📄 index.ts

> │            └── 📂 transformers/

> │              ├── 📄 citations.ts

> │              ├── 📄 description.ts

> │              ├── 📄 frontmatter.ts

> │              ├── 📄 gfm.ts

> │              ├── 📄 index.ts

> │              ├── 📄 lastmod.ts

> │              ├── 📄 latex.ts

> │              ├── 📄 linebreaks.ts

> │              ├── 📄 links.ts

> │              ├── 📄 ofm.ts

> │              ├── 📄 oxhugofm.ts

> │              ├── 📄 roam.ts

> │              ├── 📄 syntax.ts

> │              ├── 📄 toc.ts

> │            ├── 📄 types.ts

> │            ├── 📄 vfile.ts

> │          └── 📂 processors/

> │            ├── 📄 emit.ts

> │            ├── 📄 filter.ts

> │            ├── 📄 parse.ts

> │          └── 📂 static/

> │            └── 📂 giscus/

> │              ├── 📄 dark.css

> │              ├── 📄 light.css

> │            ├── 📄 icon.png

> │            ├── 📄 og-image.png

> │          └── 📂 styles/

> │            ├── 📄 base.scss

> │            ├── 📄 callouts.scss

> │            ├── 📄 custom.scss

> │            ├── 📄 syntax.scss

> │            ├── 📄 variables.scss

> │          └── 📂 util/

> │            ├── 📄 clone.ts

> │            ├── 📄 ctx.ts

> │            ├── 📄 emoji.ts

> │            ├── 📄 emojimap.json

> │            ├── 📄 escape.ts

> │            ├── 📄 fileTrie.test.ts

> │            ├── 📄 fileTrie.ts

> │            ├── 📄 glob.ts

> │            ├── 📄 jsx.tsx

> │            ├── 📄 lang.ts

> │            ├── 📄 log.ts

> │            ├── 📄 og.tsx

> │            ├── 📄 path.test.ts

> │            ├── 📄 path.ts

> │            ├── 📄 perf.ts

> │            ├── 📄 random.ts

> │            ├── 📄 resources.tsx

> │            ├── 📄 sourcemap.ts

> │            ├── 📄 theme.ts

> │            ├── 📄 trace.ts

> │          ├── 📄 worker.ts

> │        ├── 📄 tsconfig.json

> │      └── 📂 c.inh-OS-site-lumara/

> │        ├── 📄 ASSET_MAPPING.md

> │        ├── 📄 CLOUDFLARE_DEPLOYMENT.md

> │        ├── 📄 LICENSE

> │        ├── 📄 README.md

> │        ├── 📄 VIDEO_COMPRESSION_README.md

> │        └── 📂 asset/

> │          ├── 📄 Icon.png

> │          └── 📂 demoapp/

> │            ├── 📄 app.html

> │          ├── 📄 fulllogo.png

> │          └── 📂 imgs/

> │            ├── 📄 mockup.png

> │          └── 📂 logos/

> │            ├── 📄 icon.jpeg

> │            ├── 📄 logo.jpeg

> │            ├── 📄 lumara (1).png

> │            ├── 📄 square.jpeg

> │            ├── 📄 square2.jpeg

> │            ├── 📄 torch.png

> │          ├── 📄 mindmap.png

> │          └── 📂 shorts/

> │            ├── 📄 247support.mp4

> │            ├── 📄 Father.mp4

> │            ├── 📄 Mother.mp4

> │            ├── 📄 appnow.mp4

> │            ├── 📄 baby.mp4

> │            ├── 📄 callcenter.mp4

> │            ├── 📄 docs.mp4

> │            ├── 📄 documents.mp4

> │            ├── 📄 familyevicted.mp4

> │            ├── 📄 horizon.mp4

> │            ├── 📄 humanonline.mp4

> │            ├── 📄 index.md

> │            ├── 📄 lost.mp4

> │            ├── 📄 neighbor.mp4

> │            ├── 📄 operationsnetwork.mp4

> │            ├── 📄 welcometotheapp.mp4

> │          └── 📂 videos/

> │            ├── 📄 Blueprint.mp4

> │            ├── 📄 Lumara__Profit_&_Impact.mp4

> │            ├── 📄 The_Lumara_Safety_Net.mp4

> │            ├── 📄 communityshield.mp4

> │            ├── 📄 humansafetynet.mp4

> │            ├── 📄 safety.mp4

> │            ├── 📄 safetynet.mp4

> │            ├── 📄 safetynet2.mp4

> │        ├── 📄 compress-videos-advanced.ps1

> │        ├── 📄 compress-videos.bat

> │        ├── 📄 compress-videos.ps1

> │        └── 📂 data/

> │          ├── 📄 Lumara_Business_Plan_Draft.csv

> │        └── 📂 docs/

> │          ├── 📄 A Shared Commitment to Empowering Immigrant Communities.md

> │          ├── 📄 A Strategic Business Plan for a National Immigrant Safety Network.md

> │          ├── 📄 Confidential Investment Memorandum.md

> │          ├── 📄 From a Virtual Lifeline to National Community Hubs.md

> │          ├── 📄 Inside the Blueprint for a Radical New Safety Net.md

> │          ├── 📄 LUMARA_PITCH_DECK_OUTLINE.md

> │          ├── 📄 VIDEO_LABELING_GUIDE.md

> │          ├── 📄 Your Safety Net in a New Land.md

> │        ├── 📄 how-it-works.html

> │        ├── 📄 index.html

> │        ├── 📄 index.md

> │        ├── 📄 partners.html

> │        ├── 📄 styles.css

> │      └── 📂 c.inh-OS-site-realtor/

> │        ├── 📄 LICENSE

> │        ├── 📄 QIOS_REPO_INFO.txt

> │        ├── 📄 README.md

> │        ├── 📄 convert-csv-to-json.js

> │        ├── 📄 index.html

> │        ├── 📄 package-lock.json

> │        ├── 📄 package.json

> │        └── 📂 public/

> │          └── 📂 data/

> │            ├── 📄 Contacts_2025_11_12.csv

> │            ├── 📄 realtors.json

> │        └── 📂 src/

> │          ├── 📄 App.jsx

> │          └── 📂 components/

> │            ├── 📄 Filters.jsx

> │            ├── 📄 Table.jsx

> │          ├── 📄 index.css

> │          ├── 📄 main.jsx

> │        ├── 📄 vite.config.js

> │      └── 📂 components/

> │        ├── 📄 ChatPanel.tsx

> │        ├── 📄 ClientHeader.astro

> │        ├── 📄 DriveEmbed.astro

> │        ├── 📄 Sidebar.astro

> │        ├── 📄 _components.md

> │      └── 📂 config/

> │      ├── 📄 content.config.ts

> │      └── 📂 data/

> │        ├── 📄 InnovaHire LLC_Account List.xlsx

> │        ├── 📄 InnovaHire_LLC_Bank_Feed_Rules.xls

> │      └── 📂 docs/

> │        ├── 📄 Innova Hire Direct Hire Agreement.docx

> │        ├── 📄 Proposal - Proposal For Direct Hire Staffing Services.pptx

> │        ├── 📄 Proposal_for_Direct_Hire_Staffing_Services.pptx

> │        ├── 📄 answer.pptx

> │        ├── 📄 innovahire.net.txt

> │        ├── 📄 lfs-files.txt

> │        ├── 📄 vdlsd1c12661c903e455ab312206937cc746f_QT_Client Work Summary_ Employer Account Compliance Letter & BMV Submission.pdf

> │        ├── 📄 vdlsdd89b8c2db830484ea1fbc8a36bf6b35d_QT_Client Work Summary_ Employer Account Compliance Letter & BMV Submission.pdf

> │      └── 📂 exports/

> │      ├── 📄 index.md

> │      ├── 📄 index.mdx

> │      └── 📂 infra/

> │      └── 📂 inh-imgs/

> │        ├── 📄 75668367024__71324B3A-3D75-4738-883B-74B979037EF7.heic

> │        ├── 📄 Blue_White_Modern_Innovative_Solutions_Proposal_(1).png

> │        ├── 📄 INNOVAHIRE_ONEPAGE_BROCHURE_DIRECT_PLACEMENTS.png

> │        ├── 📄 INNOVA_FLOW_ORDER_PROCESS_LIFE_CYCLE.png

> │        ├── 📄 InnovaHire_Direct_Placement_Staffing_Agreement.png

> │        ├── 📄 Screen_Shot_2019-06-05_at_7.17.43_PM.png

> │        ├── 📄 Untitled (2).png

> │        ├── 📄 Untitled 1.png

> │        ├── 📄 Untitled 2.png

> │        ├── 📄 Untitled 3.png

> │        ├── 📄 Untitled 4.png

> │        ├── 📄 iStock-1332570157_z3nxx8.jpeg

> │        ├── 📄 image (2).png

> │        ├── 📄 image 1 (2).png

> │        ├── 📄 image 2 (2).png

> │        ├── 📄 image 3.png

> │        ├── 📄 image 4.png

> │        ├── 📄 image 5.png

> │        ├── 📄 image 6.png

> │        ├── 📄 image 7.png

> │        ├── 📄 image 8.png

> │        ├── 📄 inh-imgs.md

> │      └── 📂 inh_realtor_navigator/

> │        ├── 📄 Businesses_2025_11_09.csv

> │        ├── 📄 Contacts_2025_11_09.csv

> │        ├── 📄 LICENSE

> │        ├── 📄 QIOS_REPO_INFO.txt

> │        ├── 📄 README.md

> │        ├── 📄 convert-csv-to-json.js

> │        ├── 📄 index.html

> │        ├── 📄 package-lock.json

> │        ├── 📄 package.json

> │        └── 📂 public/

> │          └── 📂 data/

> │            ├── 📄 Contacts_2025_11_12.csv

> │            ├── 📄 realtors.json

> │        └── 📂 raw_data/

> │          ├── 📄 Businesses_2025_11_09.csv

> │          └── 📂 Chrome-get/

> │            └── 📂 Chrome-get/

> │              ├── 📄 README.md

> │              ├── 📄 node scrape_mibor_debug.bat

> │              ├── 📄 node scrape_mibor_debug_search.bat

> │              ├── 📄 package-lock.json

> │              ├── 📄 package.json

> │              ├── 📄 run-scraper.bat

> │              ├── 📄 run.bat

> │              ├── 📄 save_storage_state.js

> │              ├── 📄 scrape.bat

> │              ├── 📄 scrape_mibor.js

> │              ├── 📄 scrape_mibor_controlled.js

> │              ├── 📄 scrape_mibor_debug.js

> │              ├── 📄 scrape_mibor_playwright.js

> │              ├── 📄 setup.bat

> │          ├── 📄 Matching_Report.md

> │          ├── 📄 add_contact_ids_and_rename_headers.py

> │          ├── 📄 contact_id_generation_log.txt

> │          ├── 📄 contacts.csv

> │          ├── 📄 contacts_updated.csv

> │          ├── 📄 contacts_zoho_ready.csv

> │          ├── 📄 match_businesses.py

> │          ├── 📄 matching_log.txt

> │          └── 📂 mibor-scraper-portable/

> │            ├── 📄 PACKAGE_INSTRUCTIONS.txt

> │            ├── 📄 README.md

> │            ├── 📄 checkpoint.json

> │            ├── 📄 launch-chrome-debug.bat

> │            ├── 📄 launch-edge-debug.bat

> │            ├── 📄 package-lock.json

> │            ├── 📄 package.json

> │            ├── 📄 run-scraper.bat

> │            ├── 📄 scrape_mibor_controlled.js

> │            ├── 📄 setup.bat

> │          ├── 📄 requirements.txt

> │          └── 📂 scrap/

> │            └── 📂 __pycache__/

> │              ├── 📄 aio_headless_slow.cpython-314.pyc

> │              ├── 📄 selenium_dual_browsers.cpython-314.pyc

> │            ├── 📄 aio_headless_slow.py

> │            ├── 📄 checkpoint.json

> │            ├── 📄 launch_scrapers.ps1

> │            ├── 📄 mibor_contacts_list.csv

> │            ├── 📄 mibor_contacts_list.csv.backup

> │            ├── 📄 mibor_human_list_cards.py

> │            ├── 📄 python mibor_human_list_cards.bat

> │            ├── 📄 requirements.txt

> │            ├── 📄 selenium_dual_browsers.py

> │          ├── 📄 verify_matches.py

> │          ├── 📄 verify_row_order.py

> │          ├── 📄 verify_zoho_ready.py

> │        ├── 📄 realtor-explorer.html

> │        └── 📂 src/

> │          ├── 📄 App.jsx

> │          └── 📂 components/

> │            ├── 📄 Filters.jsx

> │            ├── 📄 Table.jsx

> │          ├── 📄 index.css

> │          ├── 📄 main.jsx

> │        ├── 📄 vite.config.js

> │      └── 📂 kb/

> │        └── 📂 1_welcome/

> │        └── 📂 2_ops/

> │          └── 📂 1_company/

> │          └── 📂 2_sops/

> │          └── 📂 3_systems/

> │          └── 📂 4_contracts/

> │          └── 📂 5_brand/

> │        └── 📂 3_finance/

> │          └── 📂 1_Accounting/

> │            └── 📂 1_Assets/

> │            └── 📂 2_Banking/

> │            └── 📂 3_Income/

> │              └── 📂 1_Salary/

> │              └── 📂 2_Business/

> │            └── 📂 4_Expenses/

> │            └── 📂 6_Liabilities/

> │              └── 📂 1_Loans/

> │              └── 📂 2_Credit-Cards/

> │            └── 📂 7_Process/

> │            └── 📂 8_QuickBooks/

> │            └── 📂 9_Receipts_and_Invoices/

> │          └── 📂 2_Insurance/

> │          └── 📂 4_Taxes/

> │            └── 📂 1_Tax-Planning/

> │            └── 📂 2_Returns-and-Filings/

> │              └── 📂 20xx/

> │                └── 📂 1_Prepare_for_Taxes/

> │                └── 📂 2_Document_Review/

> │                └── 📂 3_Tax_Mapping/

> │                └── 📂 4_Filing_and_Supporting_Documents/

> │            └── 📂 3_Tax-Binders/

> │              └── 📂 2022_Filings/

> │                └── 📂 20_Deductions/

> │                └── 📂 30_Adjusting/

> │                └── 📂 40_Credits/

> │                └── 📂 50_Contractors/

> │                  └── 📂 payroll-contractors/

> │                    └── 📂 _versions/

> │                └── 📂 60_Banking/

> │                  └── 📂 banking/

> │                    └── 📂 _versions/

> │                └── 📂 70_Payments/

> │                └── 📂 90_Receipts/

> │                └── 📂 99_Prep/

> │              └── 📂 2023_Filings/

> │                └── 📂 00_Returns/

> │                └── 📂 10_Income/

> │                  └── 📂 invoices/

> │                └── 📂 20_Deductions/

> │                └── 📂 30_Adjusting/

> │                └── 📂 40_Credits/

> │                └── 📂 50_Contractors/

> │                  └── 📂 payroll-contractors/

> │                    └── 📂 _versions/

> │                └── 📂 60_Banking/

> │                  └── 📂 banking/

> │                    └── 📂 _versions/

> │                └── 📂 70_Payments/

> │                └── 📂 90_Receipts/

> │                └── 📂 99_Prep/

> │                └── 📂 Extract Rays-Construction-LLC/

> │              └── 📂 2024_Filings/

> │                └── 📂 10_Income/

> │                  └── 📂 invoices/

> │                └── 📂 20_Deductions/

> │                └── 📂 30_Adjusting/

> │                └── 📂 40_Credits/

> │                └── 📂 50_Contractors/

> │                  └── 📂 payroll-contractors/

> │                    └── 📂 _versions/

> │                └── 📂 60_Banking/

> │                  └── 📂 banking/

> │                    └── 📂 _versions/

> │                └── 📂 70_Payments/

> │                └── 📂 90_Receipts/

> │              └── 📂 2025_Filings/

> │                └── 📂 10_Income/

> │                  └── 📂 invoices/

> │                └── 📂 20_Deductions/

> │                └── 📂 50_Contractors/

> │                  └── 📂 payroll-contractors/

> │                    └── 📂 _versions/

> │                └── 📂 60_Banking/

> │                  └── 📂 banking/

> │                    └── 📂 _versions/

> │                └── 📂 90_Receipts/

> │              └── 📂 20xx_Filings/

> │            └── 📂 4_Estimated-Payments/

> │            └── 📂 5_Binders/

> │              └── 📂 2021_Filings/

> │              └── 📂 2022_Filings/

> │                └── 📂 00_Returns/

> │                └── 📂 20_Deductions/

> │                └── 📂 30_Adjusting/

> │                └── 📂 40_Credits/

> │                └── 📂 50_Contractors/

> │                  └── 📂 1099-checklist/

> │                └── 📂 60_Banking/

> │                └── 📂 70_Payments/

> │                └── 📂 90_Receipts/

> │              └── 📂 2023_Filings/

> │                └── 📂 00_Returns/

> │                └── 📂 10_Income/

> │                └── 📂 20_Deductions/

> │                └── 📂 30_Adjusting/

> │                └── 📂 40_Credits/

> │                └── 📂 70_Payments/

> │                └── 📂 90_Receipts/

> │          └── 📂 5_Agreements/

> │          └── 📂 6_Reports/

> │        └── 📂 4_legal/

> │        └── 📂 5_projects/

> │          └── 📂 2025-09-01_innovahire-on-qially/

> │          └── 📂 2025-10-01_Microsoft-Setup/

> │          └── 📂 2025-10-02_Time-Keeper/

> │          └── 📂 2025-11-01_InnovaHire_Integrated_Services/

> │          └── 📂 2025-11-01_MIBOR_Member_Directory/

> │            └── 📂 Iteration-One/

> │              └── 📂 alternative_sources/

> │              └── 📂 client_package/

> │              └── 📂 homes_all_pages/

> │              └── 📂 homes_html/

> │              └── 📂 homes_text_dump/

> │              └── 📂 indianapolis_agents_client_package/

> │              └── 📂 indianapolis_agents_viewer/

> │            └── 📂 Iteration-Two/

> │          └── 📂 2025-11-13_Realtor_Lookup/

> │          └── 📂 Brain_Sessions/

> │            └── 📂 Lumara/

> │              └── 📂 asset/

> │                └── 📂 advids/

> │                  └── 📂 30s-Lumara-Mini-Commercial/

> │                └── 📂 demoapp/

> │                └── 📂 logos/

> │              └── 📂 data/

> │              └── 📂 docs/

> │            └── 📂 PunchPro/

> │        └── 📂 6_personal/

> │        └── 📂 7_misc/

> │      └── 📂 lib/

> │      ├── 📄 navigator.html

> │      └── 📂 public/

> │        ├── 📄 favicon.ico

> │        ├── 📄 favicon.svg

> │      ├── 📄 requests.mdx

> │      ├── 📄 requirements.txt

> │      └── 📂 scripts/

> │        ├── 📄 README.md

> │        ├── 📄 _scripts.md

> │        ├── 📄 analyze-astro-structure.py

> │        ├── 📄 check-md-titles.py

> │        ├── 📄 clone-client-os.py

> │        ├── 📄 directory_walker.py

> │        ├── 📄 fix-missing-titles.ps1

> │        ├── 📄 generate_3d_data.py

> │        ├── 📄 run_3d_mindmap.bat

> │        ├── 📄 run_3d_real.bat

> │        ├── 📄 run_3d_simple.bat

> │        ├── 📄 undo-fix-titles.ps1

> │    └── 📂 c.mpp/

> │      ├── 📄 BUILD_SUMMARY.md

> │      ├── 📄 CLEANUP_RECOMMENDATIONS.md

> │      ├── 📄 CLIENT_OS_FEATURES_SUMMARY.md

> │      ├── 📄 CLOUDFLARE_PAGES_EXACT_SETTINGS.md

> │      ├── 📄 CLOUDFLARE_PAGES_SETTINGS.md

> │      ├── 📄 CODE_EXTRACTION.md

> │      ├── 📄 ENGAGEMENT_SUITE_SUMMARY.md

> │      ├── 📄 LICENSE

> │      ├── 📄 MULTI_TENANT_AI_SETUP.md

> │      ├── 📄 My Punch Pro Project Update and Action Items.html

> │      ├── 📄 MyPunchPro_ADHD_Proof_Task_Import.csv

> │      ├── 📄 MyPunchPro_Tasks_With_Dates.csv

> │      ├── 📄 QIOS_REPO_INFO.txt

> │      ├── 📄 QIOS_SAFE_TO_DELETE.txt

> │      ├── 📄 QUARTZ_BUILD_COMPARISON.md

> │      ├── 📄 Quartz4.md

> │      ├── 📄 README.md

> │      ├── 📄 README_EMAIL_GENERATOR.md

> │      ├── 📄 SEED_CONTENT_INVENTORY.md

> │      ├── 📄 mdSilo-all.json

> │      ├── 📄 mypunchpro_project_update (1).html

> │      ├── 📄 mypunchpro_project_update.html

> │      ├── 📄 package.json

> │    └── 📂 inh.c/

> │      └── 📂 docs/

> │        ├── 📄 INNOVAHIRE_ONEPAGE_BROCHURE_DIRECT_PLACEMENTS.pdf

> │        ├── 📄 InnovaHire_Direct_Placement_Staffing_Agreement.pdf

> │        ├── 📄 Proposal_for_Direct_Hire_Staffing_Services.pdf

> │    └── 📂 lae.c/

> │      └── 📂 kb/

> │        └── 📂 care_Plans/

> │          └── 📂 Lisa_English_Care_KB/

> │            └── 📂 00_Admin/

> │            └── 📂 06_Restricted-Private_Notes/

> │            └── 📂 10_Overview/

> │            └── 📂 20_Daily_Care/

> │            └── 📂 30_Escalation_Emergency_Playbooks/

> │            └── 📂 40_Tools_Eqiupment_Accessibility/

> │            └── 📂 50_Caregiver_SOPs/

> │            └── 📂 70_Change_Log/

> │            ├── 📄 Cononical_Fill_Guide.md

> │    └── 📂 zjk/

> │      ├── 📄 12272024_VEHICLE DESCRIPTION YEAR MAKE_MODEL 2018 CHEVROLET_ MAL OCR.pdf

> │      ├── 📄 12272024_VEHICLE DESCRIPTION YEAR MAKE_MODEL 2018 CHEVROLET_ MAL.pdf

> │  └── 📂 30_knowledge/

> │    └── 📂 10_timeline/

> │      └── 📂 10_Entries/

> │        └── 📂 1990-1992_Infancy/

> │          ├── 📄 00_OVERVIEW.md

> │          └── 📂 1990/

> │          └── 📂 1991/

> │          └── 📂 1992/

> │          ├── 📄 INDEX.md

> │        └── 📂 1993-1995_Preschool/

> │          ├── 📄 00_OVERVIEW.md

> │          └── 📂 1993/

> │          └── 📂 1994/

> │          └── 📂 1995/

> │          ├── 📄 INDEX.md

> │        └── 📂 1996-2001_Elementary/

> │          ├── 📄 00_OVERVIEW.md

> │          └── 📂 1996/

> │          └── 📂 1997/

> │          └── 📂 1998/

> │          └── 📂 1999/

> │          └── 📂 2000/

> │          └── 📂 2001/

> │          ├── 📄 INDEX.md

> │        └── 📂 2002-2004_Preadolescence/

> │          ├── 📄 00_OVERVIEW.md

> │          └── 📂 2002/

> │          └── 📂 2003/

> │          └── 📂 2004/

> │          ├── 📄 INDEX.md

> │        └── 📂 2002-2004_Rites/

> │          ├── 📄 00_OVERVIEW.md

> │          └── 📂 2002/

> │          └── 📂 2003/

> │          ├── 📄 INDEX.md

> │        └── 📂 2005-2008_Highschool/

> │          ├── 📄 00_OVERVIEW (2).md

> │          ├── 📄 00_OVERVIEW.md

> │          └── 📂 2005/

> │          └── 📂 2006/

> │          └── 📂 2007/

> │          └── 📂 2008/

> │          ├── 📄 INDEX (2).md

> │          ├── 📄 INDEX.md

> │        └── 📂 2009-2011_Early_Adult/

> │          ├── 📄 00_OVERVIEW.md

> │          └── 📂 2009/

> │          └── 📂 2010/

> │          └── 📂 2011/

> │          ├── 📄 INDEX.md

> │        └── 📂 2012-2015_Post_Grad/

> │          ├── 📄 00_OVERVIEW.md

> │          └── 📂 2012/

> │          └── 📂 2013/

> │          └── 📂 2014/

> │          └── 📂 2015/

> │          └── 📂 2015 1/

> │          ├── 📄 INDEX.md

> │        └── 📂 2016-2020_Late_20s/

> │          ├── 📄 00_OVERVIEW.md

> │          └── 📂 2016/

> │          └── 📂 2017/

> │          └── 📂 2017 1/

> │          └── 📂 2018/

> │          └── 📂 2018 1/

> │          └── 📂 2019/

> │          └── 📂 2019 1/

> │          └── 📂 2020/

> │          └── 📂 2020 1/

> │          ├── 📄 INDEX.md

> │        └── 📂 2021-2025_Early_30s/

> │          ├── 📄 00_OVERVIEW.md

> │          └── 📂 2021/

> │            └── 📂 11 - November/

> │              └── 📂 28 - Tuesday/

> │            └── 📂 12 - December/

> │              └── 📂 18 - Monday/

> │                └── 📂 Photos from the trip/

> │              └── 📂 19 - Tuesday/

> │              └── 📂 21 - Thursday/

> │              └── 📂 22 - Friday/

> │                └── 📂 The Mechanical/

> │              └── 📂 24 - Sunday - Christmas Eve!/

> │            └── 📂 Epics/

> │              └── 📂 Christmas/

> │                └── 📂 Shopping/

> │          └── 📂 2022/

> │          └── 📂 2023/

> │          └── 📂 2024/

> │            └── 📂 01-January/

> │            └── 📂 02-February/

> │            └── 📂 03-March/

> │            └── 📂 04-April/

> │            └── 📂 05-May/

> │            └── 📂 06-June/

> │            └── 📂 07-July/

> │            └── 📂 08-August/

> │            └── 📂 09-September/

> │            └── 📂 10-October/

> │            └── 📂 11-November/

> │            └── 📂 12-December/

> │          └── 📂 2025/

> │            └── 📂 01-January/

> │            └── 📂 02-February/

> │            └── 📂 03-March/

> │            └── 📂 04-April/

> │            └── 📂 05-May/

> │            └── 📂 06-June/

> │            └── 📂 07-July/

> │            └── 📂 08-August/

> │            └── 📂 09-September/

> │            └── 📂 10-October/

> │              └── 📂 Home Sale and Move/

> │            └── 📂 11 - November/

> │              └── 📂 11 - Tuesday/

> │            └── 📂 11-November/

> │              └── 📂 11 - Tuesday/

> │            └── 📂 12-December/

> │            └── 📂 20250913_A Window Between Us/

> │            └── 📂 Home Sale and Move/

> │          ├── 📄 INDEX.md

> │        └── 📂 2026-2030_Late_30s/

> │          ├── 📄 00_OVERVIEW.md

> │          └── 📂 2026/

> │            └── 📂 01/

> │              └── 📂 2026-01-06_Tuesday/

> │                ├── 📄 2026-01-06

> │          ├── 📄 INDEX.md

> │        └── 📂 2031-2040_Prime/

> │          ├── 📄 00_OVERVIEW.md

> │          ├── 📄 INDEX.md

> │        └── 📂 2041-2050_Steward/

> │          ├── 📄 00_OVERVIEW.md

> │          ├── 📄 INDEX.md

> │        └── 📂 2051-2060_Mentor/

> │          ├── 📄 00_OVERVIEW.md

> │          ├── 📄 INDEX.md

> │        └── 📂 2061-2090_Legacy/

> │          ├── 📄 00_OVERVIEW.md

> │          ├── 📄 INDEX.md

> │      └── 📂 20_clinical/

> │        └── 📂 10_conditions/

> │        └── 📂 20_mechanisms/

> │          └── 📂 neurodivergence_truth_misreadings/

> │            └── 📂 audio/

> │            └── 📂 docs/

> │            └── 📂 html/

> │            └── 📂 references/

> │            └── 📂 transcripts/

> │            └── 📂 video/

> │        └── 📂 40_assessments/

> │          └── 📂 case_analysis_cody_rice_velasquez/

> │            └── 📂 docs/

> │            └── 📂 references/

> │      └── 📂 30_creative/

> │        └── 📂 10_essays/

> │          └── 📂 life-balance/

> │          └── 📂 mirrors-between-us/

> │            └── 📂 raw/

> │            └── 📂 static/

> │              └── 📂 images/

> │        └── 📂 30_podcast/

> │        └── 📂 40_reflections/

> │        └── 📂 50_mythology/

> │        └── 📂 60_Guides/

> │          └── 📂 Cody_s Guide to Understanding and Connection/

> │            └── 📂 assets/

> │              └── 📂 images/

> │        └── 📂 70_visual_assets/

> │        └── 📂 713/

> │          └── 📂 00_meta/

> │            └── 📂 _meta/

> │              └── 📂 json/

> │              └── 📂 rag/

> │            └── 📂 meta/

> │              └── 📂 json/

> │              └── 📂 rag/

> │          └── 📂 01_architecture/

> │            └── 📂 07_series_notes/

> │            └── 📂 10_series_blueprints/

> │              └── 📂 2.30.20.10_713/

> │                └── 📂 2.30.20.21_Intro/

> │                  └── 📂 en/

> │                  └── 📂 es/

> │                  └── 📂 reader/

> │                  └── 📂 scripts/

> │                  └── 📂 static/

> │                  └── 📂 static_build/

> │                └── 📂 2.30.20.22_Seven/

> │                  └── 📂 2.30.20.11_Embrace-Now/

> │                    └── 📂 assets/

> │                    └── 📂 notes/

> │                  └── 📂 2.30.20.12_Mind-Body/

> │                    └── 📂 assets/

> │                    └── 📂 notes/

> │                  └── 📂 2.30.20.13_Power-Within/

> │                  └── 📂 2.30.20.14_One-With-Being/

> │                  └── 📂 2.30.20.15_Wisdom/

> │                  └── 📂 2.30.20.16_Elevate-Daily/

> │                  └── 📂 2.30.20.17_Remember/

> │                └── 📂 2.30.20.23_One/

> │                  └── 📂 2.30.20.18_The-Key/

> │                    └── 📂 01_Introduction/

> │                      └── 📂 1_Dedication/

> │                      └── 📂 2_Purpose/

> │                      └── 📂 3_Guide/

> │                    └── 📂 02_Backstory/

> │                      └── 📂 1_Origins/

> │                        └── 📂 1_Early_Life/

> │                        └── 📂 2_Family/

> │                        └── 📂 3_Culture-Environment/

> │                      └── 📂 2_Formative_Years/

> │                        └── 📂 First traumas and coping mechanisms/

> │                        └── 📂 Friendships/

> │                        └── 📂 School life/

> │                      └── 📂 3_Adulting_College/

> │                        └── 📂 Collegework/

> │                        └── 📂 Learning vs. survival/

> │                    └── 📂 03_Success_and_Setbacks/

> │                      └── 📂 04.01_Business_Highs/

> │                      └── 📂 04.02_Joel_s_Deportation/

> │                      └── 📂 04.03_Lafayette_Partners/

> │                      └── 📂 04.04_ISSITax_and_QHR_Collapse/

> │                    └── 📂 04_The_Free_Fall/

> │                      └── 📂 05.02_Narcissist and the test/

> │                      └── 📂 05.03_Homelessness and Fire/

> │                      └── 📂 09_Lafayette_Business_Betrayal/

> │                    └── 📂 05_Awakening/

> │                      └── 📂 03.01_Awakening_and_Revelations/

> │                      └── 📂 03.02_The Mirror & The Masks/

> │                    └── 📂 06_Faithful_Rebuild/

> │                    └── 📂 07_Final_Test/

> │                      └── 📂 07.01_Rock_Bottom/

> │                    └── 📂 08_This_Is_Me (CLIMAX)/

> │                      └── 📂 07.01_Personality_Type_INFJ ← Now it hits different/

> │                      └── 📂 07.02_Core_Values_and_Beliefs/

> │                      └── 📂 07.03_The Patterns I’ve Seen/

> │                      └── 📂 07.04_Mirrors I Became/

> │                      └── 📂 07.05_Masks I Dropped/

> │                      └── 📂 07.06_My True Self Emerging/

> │                      └── 📂 07.07_Why It All Makes Sense Now/

> │                    └── 📂 09_Hope_and_Legacy/

> │                      └── 📂 08.01_Hope/

> │                      └── 📂 08.02_Forgiveness/

> │                      └── 📂 08.03_My Legacy & EmpowerQNow/

> │                    └── 📂 10_My_Purpose_and_Mission/

> │                    └── 📂 11_Reconstruction/

> │                      └── 📂 06.01_Rebuilding_From_Zero/

> │                      └── 📂 06.02_New_Meaning/

> │                      └── 📂 06.03_Finding_Faith_in_Myself/

> │                    └── 📂 12_Epilogue/

> │                    └── 📂 16.10_You-thought-you-knew-me/

> │                └── 📂 2.30.20.24_Three/

> │                  └── 📂 2.30.20.19_Now/

> │                  └── 📂 2.30.20.20_Openness-Oneness/

> │                  └── 📂 2.30.20.21_Walking-the-Path/

> │                └── 📂 2.30.20.25_Integration/

> │            └── 📂 q_identity_model/

> │              └── 📂 01_Who_I_Am/

> │          └── 📂 02_books/

> │            └── 📂 book_00/

> │              └── 📂 meta/

> │              └── 📂 prelude/

> │            └── 📂 book_01/

> │              └── 📂 artifacts/

> │              └── 📂 chapters/

> │                └── 📂 00_meta/

> │                └── 📂 01_intro/

> │                  └── 📂 1_Dedication/

> │                  └── 📂 2_Purpose/

> │                  └── 📂 3_Guide/

> │                  └── 📂 en/

> │                  └── 📂 es/

> │                  └── 📂 reader/

> │                  └── 📂 scripts/

> │                  └── 📂 static/

> │                  └── 📂 static_build/

> │                └── 📂 02_backstory/

> │                  └── 📂 1_Origins/

> │                    └── 📂 1_Early_Life/

> │                    └── 📂 2_Family/

> │                    └── 📂 3_Culture-Environment/

> │                  └── 📂 2_Formative_Years/

> │                    └── 📂 First traumas and coping mechanisms/

> │                    └── 📂 Friendships/

> │                    └── 📂 School life/

> │                  └── 📂 3_Adulting_College/

> │                    └── 📂 Collegework/

> │                    └── 📂 Learning vs. survival/

> │                    └── 📂 responsibilities/

> │                └── 📂 05_the_mirrors/

> │          └── 📂 03_characters/

> │          └── 📂 03_creative/

> │            └── 📂 episodes/

> │          └── 📂 04_events_and_timelines/

> │            └── 📂 storyline/

> │          └── 📂 05_world_and_mythos/

> │          └── 📂 06_lore_and_analysis/

> │            └── 📂 articles_essays/

> │              └── 📂 mirrors-between-us/

> │            └── 📂 essays/

> │              └── 📂 Manual_to_Me/

> │              └── 📂 mirrors-between-us/

> │                └── 📂 raw/

> │                └── 📂 static/

> │                  └── 📂 images/

> │          └── 📂 07_sora/

> │          └── 📂 08_creative_assets/

> │            └── 📂 assets/

> │              └── 📂 2.30.20.30_audio_raw/

> │              └── 📂 2.30.20.31_audio_pub/

> │              └── 📂 2.30.20.32_video_raw/

> │              └── 📂 2.30.20.33_video_pub/

> │              └── 📂 2.30.20.34_images_raw/

> │              └── 📂 2.30.20.35_images_pub/

> │              └── 📂 2.30.20.52_highlights/

> │              └── 📂 2.30.20.90_epub/

> │              └── 📂 2.30.20.91_pdf/

> │              └── 📂 2.30.20.92_audio_mixdowns/

> │              └── 📂 2.30.20.93_site-sync/

> │                └── 📂 layouts/

> │                └── 📂 static/

> │                  └── 📂 css/

> │                  └── 📂 images/

> │                  └── 📂 js/

> │            └── 📂 content/

> │              └── 📂 en/

> │              └── 📂 es/

> │            └── 📂 exports/

> │              └── 📂 2.30.20.93_site-sync/

> │                └── 📂 layouts/

> │                └── 📂 static/

> │                  └── 📂 images/

> │            └── 📂 links/

> │            └── 📂 resources/

> │              └── 📂 goals/

> │              └── 📂 quotes/

> │              └── 📂 templates/

> │            └── 📂 static_build/

> │            └── 📂 tools/

> │              └── 📂 scripts/

> │          └── 📂 09_drafts/

> │            └── 📂 _scenes/

> │            └── 📂 journal/

> │              └── 📂 2021/

> │                └── 📂 11 - November/

> │                  └── 📂 28 - Tuesday/

> │                └── 📂 12 - December/

> │                  └── 📂 18 - Monday/

> │                  └── 📂 19 - Tuesday/

> │                  └── 📂 21 - Thursday/

> │                  └── 📂 22 - Friday/

> │                    └── 📂 The Mechanical/

> │                  └── 📂 24 - Sunday - Christmas Eve!/

> │                └── 📂 Epics/

> │                  └── 📂 Christmas/

> │                    └── 📂 Shopping/

> │              └── 📂 2025/

> │                └── 📂 11 - November/

> │                  └── 📂 11 - Tuesday/

> │            └── 📂 misc/

> │              └── 📂 integrations/

> │              └── 📂 one/

> │                └── 📂 2.30.20.18_The-Key/

> │                  └── 📂 00_Metadata/

> │                  └── 📂 01_Introduction/

> │                    └── 📂 1_Dedication/

> │                    └── 📂 2_Purpose/

> │                    └── 📂 3_Guide/

> │                  └── 📂 02_Backstory/

> │                    └── 📂 1_Origins/

> │                      └── 📂 1_Early_Life/

> │                      └── 📂 2_Family/

> │                      └── 📂 3_Culture-Environment/

> │                    └── 📂 2_Formative_Years/

> │                      └── 📂 First traumas and coping mechanisms/

> │                      └── 📂 Friendships/

> │                      └── 📂 School life/

> │                    └── 📂 3_Adulting_College/

> │                      └── 📂 Collegework/

> │                      └── 📂 Learning vs. survival/

> │                      └── 📂 responsibilities/

> │                  └── 📂 03_Success_and_Setbacks/

> │                    └── 📂 04.01_Business_Highs/

> │                    └── 📂 04.02_Joel_s_Deportation/

> │                    └── 📂 04.03_Lafayette_Partners/

> │                    └── 📂 04.04_ISSITax_and_QHR_Collapse/

> │                  └── 📂 04_The_Free_Fall/

> │                    └── 📂 05.02_Narcissist and the test/

> │                    └── 📂 05.03_Homelessness and Fire/

> │                    └── 📂 09_Lafayette_Business_Betrayal/

> │                  └── 📂 05_Awakening/

> │                    └── 📂 03.01_Awakening_and_Revelations/

> │                    └── 📂 03.02_The Mirror & The Masks/

> │                  └── 📂 06_Faithful_Rebuild/

> │                  └── 📂 07_Final_Test/

> │                    └── 📂 07.01_Rock_Bottom/

> │                  └── 📂 08_This_Is_Me (CLIMAX)/

> │                    └── 📂 07.01_Personality_Type_INFJ ← Now it hits different/

> │                    └── 📂 07.02_Core_Values_and_Beliefs/

> │                    └── 📂 07.03_The Patterns I’ve Seen/

> │                    └── 📂 07.04_Mirrors I Became/

> │                    └── 📂 07.05_Masks I Dropped/

> │                    └── 📂 07.06_My True Self Emerging/

> │                    └── 📂 07.07_Why It All Makes Sense Now/

> │                  └── 📂 09_Hope_and_Legacy/

> │                    └── 📂 08.01_Hope/

> │                    └── 📂 08.02_Forgiveness/

> │                    └── 📂 08.03_My Legacy & EmpowerQNow/

> │                    └── 📂 09_Legacy_and_Closure/

> │                  └── 📂 10_My_Purpose_and_Mission/

> │                  └── 📂 11_Reconstruction/

> │                    └── 📂 06.01_Rebuilding_From_Zero/

> │                    └── 📂 06.02_New_Meaning/

> │                    └── 📂 06.03_Finding_Faith_in_Myself/

> │                  └── 📂 12_Epilogue/

> │                  └── 📂 16.10_You-thought-you-knew-me/

> │              └── 📂 seven/

> │                └── 📂 2.30.20.11_Embrace-Now/

> │                  └── 📂 assets/

> │                  └── 📂 notes/

> │                └── 📂 2.30.20.12_Mind-Body/

> │                  └── 📂 assets/

> │                  └── 📂 notes/

> │                └── 📂 2.30.20.13_Power-Within/

> │                └── 📂 2.30.20.14_One-With-Being/

> │                └── 📂 2.30.20.15_Wisdom/

> │                └── 📂 2.30.20.16_Elevate-Daily/

> │                └── 📂 2.30.20.17_Remember/

> │              └── 📂 three/

> │                └── 📂 2.30.20.19_Now/

> │                └── 📂 2.30.20.20_Openness-Oneness/

> │                └── 📂 2.30.20.21_Walking-the-Path/

> │              └── 📂 you-thought-you-knew-me/

> │                └── 📂 00_Metadata_and_Indexing/

> │                └── 📂 01_Who_I_Am/

> │                └── 📂 02_Origins_and_Childhood/

> │                └── 📂 03_Adolescence_and_Awakening/

> │                └── 📂 04_Adulthood_and_Adaptation/

> │                └── 📂 05_The_Mirrors/

> │                └── 📂 06_Healing_and_Reconstruction/

> │                └── 📂 07_The_Love_I_Needed/

> │                └── 📂 08_My_Purpose_and_Mission/

> │                └── 📂 09_Legacy_and_Closure/

> │                └── 📂 10_Archive_and_Artifacts/

> │            └── 📂 notes/

> │              └── 📂 2.30.20.20_evergreen/

> │              └── 📂 StoryLine/

> │              └── 📂 resources/

> │                └── 📂 templates/

> │              └── 📂 scripts/

> │              └── 📂 src/

> │                └── 📂 components/

> │                └── 📂 data/

> │                └── 📂 types/

> │                └── 📂 utils/

> │            └── 📂 unknown/

> │          └── 📂 Mirrors/

> │            └── 📂 mirrors-between-us-main/

> │          └── 📂 scripts/

> │          └── 📂 static/

> │          └── 📂 workers/

> │        └── 📂 assets/

> │          └── 📂 audio/

> │          └── 📂 documents/

> │          └── 📂 images/

> │          └── 📂 videos/

> │      └── 📂 40_relationships/

> │        └── 📂 1.10.32_luis_a_palacios_de_la_rosa/

> │        └── 📂 1.10.33_zaitullah_jan_khebarkhil/

> │    └── 📂 20_sops/

> │      └── 📂 10_playbooks/

> │        └── 📂 10_production_bible/

> │          └── 📂 10_foundation/

> │            ├── 📄 1. Core Story Assets.md

> │        └── 📂 30_health/

> │          └── 📂 anthem/

> │            ├── 📄 Anthem_PPO_Summary.pdf

> │          └── 📂 guardian/

> │            ├── 📄 Guardian_Dental_Summary.pdf

> │        └── 📂 innovaflow/

> │          ├── 📄 INNOVA_FLOW_ORDER_PROCESS_LIFE_CYCLE.pdf

> │      └── 📂 20_procedures/

> │        └── 📂 Hair-Removal/

> │        ├── 📄 New_Client_Checklist.pdf

> │      └── 📂 30_runbooks/

> │      └── 📂 40_build_guides/

> │      └── 📂 50_operating_procedures/

> │    └── 📂 30_refernce/

> │      └── 📂 10_laws_and_regulations/

> │      └── 📂 20_financial_rules/

> │      └── 📂 30_medical_and_health/

> │        └── 📂 Sundowning/

> │          ├── 📄 readme.md

> │      └── 📂 40_technical_concepts/

> │      └── 📂 50_definitions_and_explanations/

> │      └── 📂 60_external_guides/

> │    └── 📂 40_professional/

> │      └── 📂 10_credentials_and_certs/

> │        └── 📂 CPR/

> │          ├── 📄 CPR certification.pdf

> │        └── 📂 Comfort_Keepers/

> │          └── 📂 Care_Academy/

> │            ├── 📄 care-academy-module_cert (1).png

> │            ├── 📄 care-academy-module_cert (2).png

> │            ├── 📄 care-academy-module_cert (3).png

> │            ├── 📄 care-academy-module_cert (4).png

> │            ├── 📄 care-academy-module_cert (5).png

> │            ├── 📄 care-academy-module_cert_summary.png

> │          └── 📂 Onboarding/

> │            ├── 📄 Orientation_and_Onboardin_signed_pages_Copy.pdf

> │      └── 📂 20_experience_and_roles/

> │      └── 📂 30_bios_and_summaries/

> │        └── 📂 Resume/

> │          ├── 📄 Profile.pdf

> │          ├── 📄 cody_rice_velasquez-fullstack.pdf

> │        ├── 📄 cody.vcf

> │        ├── 📄 qrcode-cody-contact-card.png

> │      └── 📂 40_capabilities_and_services/

> │      └── 📂 50_testimonials_and_outcomes/

> │    └── 📂 50_systems/

> │      └── 📂 10_github/

> │      └── 📂 20_qios/

> │      └── 📂 30_qinoteos/

> │      ├── 📄 30_qinoteos-merged.md

> │        ├── 📄 0.00.00-qios_genesis.md

> │        ├── 📄 2026-01-01_phase_1_dev_doc_greenlight.md

> │        ├── 📄 DEV_DOC.md

> │        ├── 📄 PHASE_1_CONTRACT.md

> │        ├── 📄 QiAlly Call Ecosystem & Gina Voice Architecture.md

> │        ├── 📄 QiNoteOS — Final Dev Doc & Roadmap (v1).md

> │        ├── 📄 QiNoteOS — Master Blueprint Draft v0.1.md

> │        ├── 📄 QiNoteOS — Module Contract.md

> │        ├── 📄 QiNoteOS — Phase 01 Module Contract v0.4.md

> │        ├── 📄 QiNoteOS — Phase 02.md

> │        ├── 📄 QiNoteOS — Phase 03.md

> │        ├── 📄 QiNoteOS — Phase 04.md

> │        ├── 📄 QiNoteOS — Phase 05.md

> │        ├── 📄 QiNoteOS — Phase 06 Kernel MVP v0.4 1.md

> │        ├── 📄 QiNoteOS_Dev_Doc_v1.2_ColdStart_Final.md

> │        ├── 📄 QiNoteOS_Dev_Doc_v1.2_ColdStart_Final.pdf

> │        ├── 📄 QiNoteOS_Master_Blueprint_v2.0.md

> │        ├── 📄 QiNoteOS_System_Manual_v3.0.md

> │        ├── 📄 README (2).md

> │        ├── 📄 README.md

> │        ├── 📄 UI_DATA_INTERFACE.md

> │        ├── 📄 gemini notes.md

> │        ├── 📄 gemini.md

> │        ├── 📄 gid_rules.md

> │        ├── 📄 grok notes.md

> │        ├── 📄 phase_1_module_identity.md.md

> │        ├── 📄 ui_contracts_v1.md

> │      └── 📂 40_tooling_and_software/

> │        └── 📂 backup_recovery/

> │          ├── 📄 README.md

> │          ├── 📄 Untitled.md

> │      └── 📂 50_infrastructure_and_hosting/

> │    └── 📂 90_archive/

> │      └── 📂 10_deprecated_sops/

> │      └── 📂 20_old_profiles/

> │      └── 📂 30_retired_systems/

> │      └── 📂 40_completed_reference/

> │  └── 📂 40_projects/

> │    └── 📂 713/

> │      └── 📂 21_Intro/

> │        └── 📂 en/

> │        └── 📂 es/

> │        └── 📂 reader/

> │        └── 📂 scripts/

> │        └── 📂 static/

> │        └── 📂 static_build/

> │      └── 📂 22_Seven/

> │      └── 📂 23_One/

> │      └── 📂 24_Three/

> │      └── 📂 25_Integration/

> │      └── 📂 26_Series-Notes/

> │    └── 📂 Ideas/

> │      └── 📂 PP_Partner_Problem/

> │        └── 📂 assets/

> │          ├── 📄 Video_Monologue_Generation_Complete.mp4

> │        ├── 📄 partner-or-problem.mp4

> │        ├── 📄 partner-or-problem.png

> │        ├── 📄 readme.md

> │    └── 📂 manual_to_me/

> │    └── 📂 mirrors_between_us/

> │      ├── 📄 mirrors_what_the_mirror_never_says.md

> │      └── 📂 raw/

> │      └── 📂 static/

> │        └── 📂 images/

> │    └── 📂 the_onion_effect/

> │      └── 📂 01_core_framework/

> │      └── 📂 02_episodes/

> │        ├── 📄 toe_why_the_small_things_hurt_so_much.md

> │      └── 📂 03_layers/

> │      └── 📂 04_patterns/

> │      └── 📂 05_integration/

> │      └── 📂 06_quotables_clips/

> │      ├── 📄 readme.md

> │  └── 📂 50_Resources/

> │    └── 📂 Checklists_and_Guides/

> │      ├── 📄 _Checklists_and_Guides.md

> │    └── 📂 Media_and_Visuals/

> │      ├── 📄 _Media_and_Visuals.md

> │    └── 📂 Misc_References/

> │      ├── 📄 _Misc_References.md

> │    └── 📂 Templates_and_Forms/

> │      ├── 📄 _Templates_and_Forms.md

> │    ├── 📄 _Resources.md

> │  └── 📂 60_personal/

> │    └── 📂 Education_and_Certificates/

> │      ├── 📄 _Education_and_Certificates.md

> │    └── 📂 Health_and_Wellness/

> │      └── 📂 TB_Test/

> │        ├── 📄 tb-site-image-1.jpeg

> │        ├── 📄 tb-site-image-2.jpeg

> │        ├── 📄 tb-site-image-3.jpeg

> │      ├── 📄 _Health_and_Wellness.md

> │    └── 📂 IDs_and_Documents/

> │      └── 📂 Car_Insurance/

> │        ├── 📄 06272025_INDIANA INSURANCE CARD.pdf

> │        ├── 📄 vehicle-insurance-id-card.pdf

> │      └── 📂 License/

> │        ├── 📄 drivers_license.jpeg

> │      ├── 📄 _IDs_and_Documents.md

> │    └── 📂 Immigration_and_Travel/

> │      ├── 📄 _Immigration_and_Travel.md

> │    ├── 📄 Personal_Notes.md

> │    ├── 📄 _Personal.md

> │  └── 📂 70_financial/

> │    └── 📂 10_banking/

> │      └── 📂 10_cashapp/

> │        └── 📂 10_statements/

> │          ├── 📄 monthly-statement (1).pdf

> │          ├── 📄 monthly-statement (10).pdf

> │          ├── 📄 monthly-statement (11).pdf

> │          ├── 📄 monthly-statement (12).pdf

> │          ├── 📄 monthly-statement (13).pdf

> │          ├── 📄 monthly-statement (14).pdf

> │          ├── 📄 monthly-statement (15).pdf

> │          ├── 📄 monthly-statement (16).pdf

> │          ├── 📄 monthly-statement (17).pdf

> │          ├── 📄 monthly-statement (18).pdf

> │          ├── 📄 monthly-statement (19).pdf

> │          ├── 📄 monthly-statement (2).pdf

> │          ├── 📄 monthly-statement (20).pdf

> │          ├── 📄 monthly-statement (21).pdf

> │          ├── 📄 monthly-statement (22).pdf

> │          ├── 📄 monthly-statement (23).pdf

> │          ├── 📄 monthly-statement (24).pdf

> │          ├── 📄 monthly-statement (25).pdf

> │          ├── 📄 monthly-statement (26).pdf

> │          ├── 📄 monthly-statement (27).pdf

> │          ├── 📄 monthly-statement (28).pdf

> │          ├── 📄 monthly-statement (29).pdf

> │          ├── 📄 monthly-statement (3).pdf

> │          ├── 📄 monthly-statement (30).pdf

> │          ├── 📄 monthly-statement (31).pdf

> │          ├── 📄 monthly-statement (32).pdf

> │          ├── 📄 monthly-statement (4).pdf

> │          ├── 📄 monthly-statement (5).pdf

> │          ├── 📄 monthly-statement (6).pdf

> │          ├── 📄 monthly-statement (7).pdf

> │          ├── 📄 monthly-statement (8).pdf

> │          ├── 📄 monthly-statement (9).pdf

> │          ├── 📄 monthly-statement.pdf

> │        ├── 📄 direct-deposit-form-CASHAPP.pdf

> │  └── 📂 qid0000001_0_module_alpha/

> │    ├── 📄 config.json

> │    └── 📂 docs/

> │    ├── 📄 index.html

> │    └── 📂 qid0000001-1_assets/

> │    └── 📂 vectors/

> │      ├── 📄 index.faiss

> │      ├── 📄 metadata.pkl

> ├── 📄 README.md

> └── 📂 output/

> │  ├── 📄 0.00.00-qios_genesis.txt

> │  ├── 📄 2026-01-01_phase_1_dev_doc_greenlight.txt

> │  ├── 📄 DEV_DOC.txt

> │  ├── 📄 PHASE_1_CONTRACT.txt

> │  ├── 📄 QiAlly Call Ecosystem & Gina Voice Architecture.txt

> │  ├── 📄 QiNoteOS — Final Dev Doc & Roadmap (v1).txt

> │  ├── 📄 QiNoteOS — Master Blueprint Draft v0.1.txt

> │  ├── 📄 QiNoteOS — Module Contract.txt

> │  ├── 📄 QiNoteOS — Phase 01 Module Contract v0.4.txt

> │  ├── 📄 QiNoteOS — Phase 02.txt

> │  ├── 📄 QiNoteOS — Phase 03.txt

> │  ├── 📄 QiNoteOS — Phase 04.txt

> │  ├── 📄 QiNoteOS — Phase 05.txt

> │  ├── 📄 QiNoteOS — Phase 06 Kernel MVP v0.4 1.txt

> │  ├── 📄 QiNoteOS_Dev_Doc_v1.2_ColdStart_Final.pdf

> │  ├── 📄 QiNoteOS_Dev_Doc_v1.2_ColdStart_Final.txt

> │  ├── 📄 QiNoteOS_Master_Blueprint_v2.0.txt

> │  ├── 📄 QiNoteOS_System_Manual_v3.0.txt

> │  ├── 📄 README (2).txt

> │  ├── 📄 README.txt

> │  ├── 📄 UI_DATA_INTERFACE.txt

> │  ├── 📄 gemini notes.txt

> │  ├── 📄 gemini.txt

> │  ├── 📄 gid_rules.txt

> │  ├── 📄 grok notes.txt

> │  ├── 📄 phase_1_module_identity.txt.md

> │  └── 📄 ui_contracts_v1.txt

> ```

### Assistant
> Below is a **copy/paste Gemini prompt** that will force it to generate the whole thing end-to-end (Cloudflare Pages site + Worker API + Stripe checkout + Supabase insert + ZeptoMail email), mapped cleanly into your **module layout** (datasets/modules split stays intact).
> 
> Use this prompt exactly as-is, then answer Gemini’s follow-ups with your real keys.
> 
> ```text
> You are a senior full-stack engineer. Build a minimal production-ready “Tax99 Intake + Payment” system using Cloudflare-first architecture.
> 
> CONTEXT
> - Domain: tax99.qially.com
> - Thank-you page: tax99.qially.com/next-steps-intake
> - Goal: Present offer → take payment → collect lead details → email me the intake details → store lead record → show next steps + secure upload link
> - Do NOT use Notion/Make/Zapier for core flow. Use Supabase as the lead database.
> - Hosting: Cloudflare Pages for the frontend. Cloudflare Worker for backend endpoints.
> - Keep it simple (KISS). No fancy UI frameworks required; plain HTML/CSS or very light JS is fine.
> 
> REPO OUTPUT REQUIRED
> Generate a complete repo with this structure:
> 
> /tax99/
>   /apps/
>     /tax99-site/                 (Cloudflare Pages static frontend)
>       /public/
>         index.html               (landing page)
>         next-steps-intake.html   (thank-you page shown after successful payment)
>         styles.css
>         app.js
>       README.md
>       wrangler.toml (only if needed for local dev; otherwise omit)
>   /workers/
>     /tax99-api/                  (Cloudflare Worker backend)
>       src/index.ts
>       package.json
>       wrangler.toml
>       README.md
>   /docs/
>     ARCHITECTURE.md
>     SETUP.md
>     SECURITY.md
>     SUPABASE_SCHEMA.sql
>   .gitignore
>   README.md
> 
> FRONTEND REQUIREMENTS (Cloudflare Pages)
> 1) Landing page (index.html) includes:
>    - Offer summary, disclaimers, what’s included / not included
>    - “Start & Pay $99” button that triggers Stripe Checkout
>    - A short form BEFORE checkout for: name, email, phone (optional), tax year, notes (optional)
>    - Basic validation
> 2) After Stripe success:
>    - Redirect user to /next-steps-intake.html?session_id=... (or a clean success token)
>    - Thank-you page must display:
>      - “We got your payment” confirmation (verified server-side)
>      - Next steps checklist
>      - A “Secure Upload Link” placeholder (simple URL placeholder in config)
>      - A note that they will receive an email with next steps
> 
> BACKEND REQUIREMENTS (Cloudflare Worker)
> Provide endpoints:
> - POST /api/create-checkout-session
>   Input: name, email, phone, tax_year, notes
>   Action: create Stripe checkout session; store a pending lead record in Supabase with status="pending"
>   Output: { url: "stripe_checkout_url" }
> 
> - GET /api/verify-session?session_id=...
>   Action: verify Stripe checkout session via Stripe API; if paid, mark Supabase lead record status="paid"
>   Output: { paid: true/false, lead: { ... } }
> 
> - POST /api/send-confirmation
>   Action: send confirmation email via ZeptoMail (or SMTP-like API) to:
>     - the customer (optional)
>     - ME (required) with all intake fields + Stripe amount + timestamps
>   Must run only after payment verification.
> 
> DATA STORE (Supabase)
> Create table: leads
> Fields:
> - id (uuid pk)
> - created_at (timestamp)
> - status (text: pending/paid/failed)
> - name (text)
> - email (text)
> - phone (text nullable)
> - tax_year (text)
> - notes (text nullable)
> - stripe_session_id (text unique nullable)
> - stripe_payment_intent (text nullable)
> - amount (integer)  -- cents
> - source (text default 'tax99')
> 
> Provide SQL in /docs/SUPABASE_SCHEMA.sql.
> 
> CONFIG / SECRETS
> Use Cloudflare Worker environment variables:
> - STRIPE_SECRET_KEY
> - STRIPE_WEBHOOK_SECRET (optional, only if you implement webhooks)
> - SUPABASE_URL
> - SUPABASE_SERVICE_ROLE_KEY
> - ZEPTOMAIL_API_KEY (or SMTP creds, but prefer ZeptoMail API)
> - NOTIFY_EMAIL_TO (my email)
> - SECURE_UPLOAD_URL (link shown on thank-you page)
> - APP_BASE_URL = https://tax99.qially.com
> 
> SECURITY
> - No secrets in frontend.
> - Validate inputs server-side.
> - CORS locked to tax99.qially.com
> - Rate limit basic (simple in-worker token bucket or per-IP guard)
> - Log minimal PII (avoid dumping full data into console logs)
> 
> DELIVERY
> 1) Output all code files completely (not snippets), separated by clear file headers like:
>    --- FILE: tax99/apps/tax99-site/public/index.html ---
> 2) Provide exact deployment steps:
>    - Create Supabase table (paste SQL)
>    - Deploy Worker (wrangler)
>    - Deploy Pages site (Cloudflare Pages)
>    - Set environment variables in Cloudflare dashboard
>    - Test flow checklist
> 
> CONSTRAINTS
> - Keep dependencies minimal.
> - Use TypeScript for Worker.
> - Prefer Stripe Checkout (hosted) over custom card form.
> - Avoid framework bloat.
> - Must work with Cloudflare Pages + Worker without needing a separate server.
> 
> If anything is ambiguous, make a reasonable assumption and document it in /docs/ARCHITECTURE.md.
> ```
> 
> ### Two small “make it actually succeed” notes (so Gemini doesn’t derail)
> 1) If Gemini tries to do webhooks (it often will), **let it**, but insist it remains optional. Your flow works fine with **verify-session on the thank-you page** without webhooks.
> 2) Tell it your preferred email provider is **ZeptoMail API** (not SMTP) so it doesn’t waste time.
> 
> ### Optional “strict mode” add-on (paste after the prompt if Gemini gets sloppy)
> ```text
> STRICT MODE:
> - Do not invent URLs or IDs.
> - All env vars must be referenced but not populated.
> - Ensure /next-steps-intake.html calls /api/verify-session and only then calls /api/send-confirmation.
> - Ensure Supabase insert happens on session creation (pending) and update happens on verification (paid).
> ```
> 
> If you want, I can also give you a **second Gemini prompt** that generates a **single-file Cloudflare Pages Functions** version (no separate Worker repo) — but the above is cleaner with your current “apps/ + workers/” organization.

### User
> wait wait we arent going to break anything we already build with qinote are we?

### Assistant
> No. Not if you follow two rules:
> 
> 1) **QiNote stays immutable.**  
>    - Don’t rename, move, or “normalize” anything inside your existing QiNote/QiDecimal/QID structures unless you are doing a controlled migration with a redirect/mapping layer.
>    - Treat QiNote as the source of truth for IDs and the knowledge graph.
> 
> 2) **Everything “new” happens as an additive layer outside QiNote.**  
>    - If you want Gemini to help clean/organize: it should generate **(a)** a proposed plan, **(b)** a mapping file, and **(c)** copy/clone targets—never destructive edits in place.
> 
> ### What this means for your current setup
> - Your `04_PRIMARY/10_datasets` and `04_PRIMARY/20_modules` structure can evolve **without touching QiNote**, as long as:
>   - You do **not** change existing QID-bearing files/paths inside your QiNote vault(s).
>   - You do **not** change any “already-ingested” canonical paths that your embeddings/indexer expect, unless you also update the indexer config and preserve an alias map.
> 
> ### The safe operating model (use this every time)
> **Plan → Map → Copy → Verify → Only then optionally migrate**
> 
> - **Plan:** Gemini outputs proposed folder moves/renames.
> - **Map:** Gemini outputs a CSV/JSON “move map” (`old_path,new_path,reason,risk,needs_redirect`).
> - **Copy:** You copy files into the new structure (leaving originals intact).
> - **Verify:** Run your indexer against the new structure and compare counts/hashes.
> - **Migrate (optional):** Only after verification, and even then, keep a rollback.
> 
> ### Red flags that *would* break QiNote
> If any of these are true, you can break stuff:
> - Renaming QID/QiDecimal filenames or front matter keys your pipeline relies on.
> - Moving the root folder that your indexer watches without updating config.
> - “Cleaning up duplicates” by deleting files that are referenced elsewhere.
> - Rewriting front matter schemas across the vault without backward compatibility.
> 
> ### Bottom line
> You’re safe **as long as this Gemini job is “propose + map + copy” and not “move/delete in place.”**
> 
> If you want, I’ll give you a Gemini prompt that explicitly:
> - forbids destructive operations,
> - outputs a move-map,
> - and defines “protected zones” (QiNote vault paths + any QID-bearing assets) so it won’t even suggest touching them.
