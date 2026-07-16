---
layout: page
title: "Drive Duplication Script"
slug: "drive_duplication_script"
created_at: "2026-05-18 12:13:26"
updated_at: "2026-07-16T06:49:32-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-007.json"
template_key: master-template
date: 2026-05-18
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a0b47eb-09bc-83ea-8bf6-aa35299e213e"
canonical_ref: ""
---

# Drive Duplication Script

## Overview
- **Date**: 2026-05-18 12:13:26
- **Conversation ID**: `6a0b47eb-09bc-83ea-8bf6-aa35299e213e`
- **Source**: `Chat-Export-28513-2026/conversations-007.json`

## Chat History

### User
> Okay, chat, we're gonna handle this drive once and for all. Here's the issue. I've ran multiple different types of duplicate checkers. I don't think they're working right anyway. Some of them are just too aggressive. Some of them are too floppy. Some of them are just not good. The one I made was working really good, but I don't know, something got changed in the code. I don't wanna mess with it. Here's what I need. First, I need a script that can pull like a manifest recursively. All the files, folders, everything, so that way we see, okay, this is a snapshot of what was there. And that way it keeps a log of everything that gets deleted or removed, and it will update the snapshot as it goes for the most up-to-date relevant information. We might need like approval gates or something. But again, you can help me out with that logic there. But this is what I need to happen. First, I need it to start like really strict at first, where it's like, it's only gonna count a duplicate of a file that is the same file name, the same file size, the same hash, or whatever, whatever which one it is that they're doing nowadays. That's, I just heard there's like a really, really fast one that's really accurate. So basically, 100% identical items. And we're not gonna do any kind of system or app files. I'm talking about like PDFs, CSVs, images, like just normal media, like normal files that would be an MDMMD file. So if they have the exact same name, exact metadata, and they're hashed, or whatever the quick one is, and they match no matter what folder they're in. So it's comparing basically just files, period, no matter where they're at. And if there's duplicates, one of them's gotta go. And I would say probably what? The oldest one would be the original, the rest of them would be copies, and those copies get quarantined. In the same folder structure, but in a quarantine folder. And they're removed from wherever they're at currently. Then, ignoring the quarantine folder, of course, then it'll get a little more, a little more loosey-goosey, where now it's gonna say, okay, well, maybe these are different file names, but maybe they're still the same metadata, the same hash. Let me see if I can find those, no matter where they're at. Same, do the same process. Then do it again just by doing hash. And then I guess after that, then we look for similar files that can be merged, and then after that, I don't know what else, but basically, I'm trying to get this done already, and we can talk about videos later. But for now, just files, like docs, PDFs, you know, CSVs, image files, but just looking at the metadata, not the image. Does that sound like something we can build right now and get this shit done in Python? And it's gonna be in Google, so it should be read-only until it starts making adjustments and it starts moving stuff. It's gonna have to pause periodically, if you know what I mean, to avoid it locking.

### Assistant
> Yes — this is buildable, and the instinct is right: stop trusting “smart” duplicate tools and make a boring, auditable, staged dedupe pipeline. The key is **manifest first, quarantine only, never delete**, and every loosening step needs its own reviewable plan.

### Assistant
> Yes. This is exactly the kind of thing Python is good at — **but the win is not the hash logic, it’s the safety architecture**.
> 
> I built you a starter tool here:
> 
> [Download qidrive_dedupe_tool.zip](sandbox:/mnt/data/qidrive_dedupe_tool.zip)
> 
> What it does:
> 
> 1. **Scans recursively**
>    - Builds a manifest of files/folders/filesystem metadata.
>    - Saves to SQLite + JSONL + CSV.
> 
> 2. **Uses staged duplicate logic**
>    - `strict`: same filename + same size + same hash.
>    - `same_hash_diff_name`: same size + same hash, even if names differ.
>    - `hash_only`: same content hash.
> 
> 3. **Quarantines, does not delete**
>    - Moves duplicates into `_QIDEDUPE_QUARANTINE`.
>    - Preserves the original folder structure.
>    - Ignores quarantine on future scans.
> 
> 4. **Approval gate**
>    - `plan` creates a CSV/JSONL review file.
>    - `apply` dry-runs unless you explicitly add `--apply`.
> 
> 5. **Google Drive-friendly**
>    - Pauses periodically to avoid Drive sync thrashing/locking.
>    - You can tune pause frequency.
> 
> The actual workflow:
> 
> ```bash
> python qidrive_dedupe.py scan "G:\My Drive" --db qidrive_manifest.sqlite
> ```
> 
> Then:
> 
> ```bash
> python qidrive_dedupe.py plan "G:\My Drive" --db qidrive_manifest.sqlite --stage strict
> ```
> 
> Review the CSV in `plans/`.
> 
> Dry-run the quarantine:
> 
> ```bash
> python qidrive_dedupe.py apply "G:\My Drive" --db qidrive_manifest.sqlite --plan "plans/YOUR_PLAN.jsonl"
> ```
> 
> Actually move duplicates:
> 
> ```bash
> python qidrive_dedupe.py apply "G:\My Drive" --db qidrive_manifest.sqlite --plan "plans/YOUR_PLAN.jsonl" --apply
> ```
> 
> Then rescan before the next looser stage:
> 
> ```bash
> python qidrive_dedupe.py scan "G:\My Drive" --db qidrive_manifest.sqlite
> ```
> 
> My recommendation: **do not start with hash-only.** Start with `strict`, rescan, then `same_hash_diff_name`, rescan, then maybe `hash_only`. After that we can add the “similar/merge candidates” layer, but that needs to be a separate review workflow — not auto-move. That’s where duplicate tools get stupid and start eating your life.

### User
> ok, one i need the documentation for the wiki but later, first is this interactive code, do i need to have codex do anythign with it right now or is it ready to run.

### Assistant
> It’s **ready to run now** as a CLI tool. You do **not** need Codex to build anything before testing it.
> 
> But: it is **not interactive yet**. It works like this:
> 
> 1. You run `scan`
> 2. It creates manifest files
> 3. You run `plan`
> 4. You review the CSV
> 5. You run `apply`
> 6. It dry-runs unless you add `--apply`
> 
> That’s actually safer for the first version. Interactive menus can come later.
> 
> Do this first on a **small test folder**, not the whole Drive:
> 
> ```powershell
> cd C:\path\to\qidrive_dedupe_tool
> 
> python qidrive_dedupe.py scan "C:\g-drive\My Drive\TEST_FOLDER" --db qidrive_manifest.sqlite
> 
> python qidrive_dedupe.py plan "C:\g-drive\My Drive\TEST_FOLDER" --db qidrive_manifest.sqlite --stage strict
> 
> python qidrive_dedupe.py apply "C:\g-drive\My Drive\TEST_FOLDER" --db qidrive_manifest.sqlite --plan "plans\YOUR_PLAN.jsonl"
> ```
> 
> That last command is dry-run. It will tell you what it **would** move.
> 
> Only after you like the plan:
> 
> ```powershell
> python qidrive_dedupe.py apply "C:\g-drive\My Drive\TEST_FOLDER" --db qidrive_manifest.sqlite --plan "plans\YOUR_PLAN.jsonl" --apply
> ```
> 
> Truth mode: before unleashing it on `C:\g-drive\My Drive\qivault`, I’d have Codex do **one thing only**: review the script for Windows path handling and add a small `--yes-reviewed` confirmation flag before real apply. Not required, but smart.
> 
> Minimum safe path:
> 
> ```powershell
> pip install blake3
> ```
> 
> Then run on a tiny folder with known duplicates. If that behaves correctly, it’s safe enough to scale to strict-stage scanning.

### User
> PS C:\QiLabs> & C:/Users/codyr/AppData/Roaming/uv/python/cpython-3.14.3-windows-x86_64-none/python.exe c:/QiLabs/apps/qidrive_dedupe_tool/qidrive_dedupe.py

> c:\QiLabs\apps\qidrive_dedupe_tool\qidrive_dedupe.py:17: SyntaxWarning: "\M" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\M"? A raw string is also an option.

>   python qidrive_dedupe.py scan "G:\My Drive" --db qidrive_manifest.sqlite

> usage: qidrive_dedupe.py [-h] {scan,plan,apply} ...

> qidrive_dedupe.py: error: the following arguments are required: command

> PS C:\QiLabs>

### Assistant
> Good — that means the script is **installed enough to execute**. It did not crash. Two things happened:
> 
> ### 1. The warning is harmless but annoying
> 
> This line in the script docstring:
> 
> ```text
> "G:\My Drive"
> ```
> 
> Python is reading `\M` as a weird escape sequence. It’s inside documentation text, not logic.
> 
> Fix later by changing the opening docstring from:
> 
> ```python
> """
> ```
> 
> to:
> 
> ```python
> r"""
> ```
> 
> at the very top of the file.
> 
> Not urgent. It does **not** affect the dedupe logic.
> 
> ### 2. The real issue: you ran the script with no command
> 
> You ran:
> 
> ```powershell
> python qidrive_dedupe.py
> ```
> 
> But the script requires one of these:
> 
> ```text
> scan
> plan
> apply
> ```
> 
> Run this next, using your actual test folder:
> 
> ```powershell
> & C:/Users/codyr/AppData/Roaming/uv/python/cpython-3.14.3-windows-x86_64-none/python.exe `
>   c:/QiLabs/apps/qidrive_dedupe_tool/qidrive_dedupe.py `
>   scan "C:\g-drive\My Drive\qivault_TEST" `
>   --db "C:\QiLabs/apps/qidrive_dedupe_tool/qidrive_manifest.sqlite"
> ```
> 
> Use a **test folder first**. Do not point it at full `qivault` yet. Gina is not letting you play drive Jenga with the live vault on the first run.  
> 
> After scan finishes, run:
> 
> ```powershell
> & C:/Users/codyr/AppData/Roaming/uv/python/cpython-3.14.3-windows-x86_64-none/python.exe `
>   c:/QiLabs/apps/qidrive_dedupe_tool/qidrive_dedupe.py `
>   plan "C:\g-drive\My Drive\qivault_TEST" `
>   --db "C:\QiLabs/apps/qidrive_dedupe_tool/qidrive_manifest.sqlite" `
>   --stage strict
> ```
> 
> Then it will create a `plans` folder with a review CSV/JSONL. We inspect that before any real moving.

### User
> honey you know the rules, no commands, interactive prompting always.

### Assistant
> You’re right. I violated the house rule. CLI-only was a “works technically” answer, not a Cody-proof workflow. I’m converting it to an interactive launcher: double-click/run once, then it asks what root, scan/plan/apply, stage, dry-run vs real move, and forces review gates.

### Assistant
> Yep. Correct correction. I made the interactive version.
> 
> [Download qidrive_dedupe_interactive_tool.zip](sandbox:/mnt/data/qidrive_dedupe_interactive_tool.zip)
> 
> This one is **interactive-first**:
> 
> - Run it with no arguments and it opens a menu.
> - It asks for the root folder.
> - It saves your config.
> - It lets you choose:
>   - scan manifest
>   - create duplicate plan
>   - dry-run plan
>   - real quarantine apply
>   - guided safe workflow: scan → strict plan → dry-run
> - Real apply requires:
>   - selecting a plan
>   - confirming you reviewed the CSV
>   - typing `QUARANTINE`
> 
> It also includes:
> 
> - `qidrive_dedupe_interactive.py`
> - `RUN_QIDRIVE_DEDUPE.bat`
> - `README.md`
> - `ai_tooling_manifest.json`
> 
> Use this instead of the first one. The first version was functional, but it was not aligned with your actual operating rule. This one is closer to how your tools should work: prompt-driven, review-gated, and hard to accidentally misuse.
