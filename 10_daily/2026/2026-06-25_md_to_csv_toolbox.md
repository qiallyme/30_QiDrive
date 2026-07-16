---
layout: page
title: "MD to CSV Toolbox"
slug: "md_to_csv_toolbox"
created_at: "2026-06-25 20:04:16"
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
uid: "6a3dcfbb-f44c-83ea-be46-974a35154463"
canonical_ref: ""
---

# MD to CSV Toolbox

## Overview
- **Date**: 2026-06-25 20:04:16
- **Conversation ID**: `6a3dcfbb-f44c-83ea-be46-974a35154463`
- **Source**: `Chat-Export-28513-2026/conversations-009.json`

## Chat History

### User
> I would like to add a tool to the toolbox that allows me to select a folder where it will find all the .md files in the selected folders and its sub folders and conver the .md files to one csv file with front matter as columns and the page content as contenet an dleave behind only the csv file and the .md file quaratntined the the folder the where found.

### Assistant
> I’ll build this as a real QiOne toolbox module, not just pseudo-code. I’m reading your existing structure as: bucketed tool folder, `BaseTool` subclass, dry-run scan first, live execution moves files only after CSV writes cleanly.

### Assistant
> One design choice I’m making: this belongs in the **docs** bucket, not organize. It’s transforming Markdown documents into a structured document export, then quarantining originals as a safety step.

### Assistant
> Done. I built the toolbox module as:
> 
> ```txt
> tools/docs/md_frontmatter_csv_compiler/
>   __init__.py
>   md_frontmatter_csv_compiler.py
>   manifest.yaml
>   README.md
> ```
> 
> Download it here: [md_frontmatter_csv_compiler_tool.zip](sandbox:/mnt/data/md_frontmatter_csv_compiler_tool.zip)
> 
> ## What it does
> 
> - Finds every `.md` file in the selected folder and subfolders.
> - Extracts front matter into CSV columns.
> - Adds the Markdown body as the `content` column.
> - Adds source metadata columns:
>   - `_source_path`
>   - `_source_folder`
>   - `_filename`
>   - `_stem`
>   - `_modified_at`
>   - `_size_bytes`
> - Writes one CSV at the selected root folder.
> - Moves each original `.md` file into a quarantine folder **beside where it was found**:
> 
> ```txt
> SomeFolder/page.md
> SomeFolder/_md_quarantine/page.md
> ```
> 
> ## Safety behavior
> 
> - **Scan** previews only. No writing, no moving.
> - **Execute** writes the CSV first, then quarantines the Markdown files.
> - It does **not delete** Markdown files.
> - It does **not overwrite** existing CSV files unless you check the overwrite option.
> - It skips files already inside `_md_quarantine` by default.
> 
> ## Install
> 
> Extract the zip into your toolbox root, so this exists:
> 
> ```txt
> c:\QiLabs\toolbox\tools\docs\md_frontmatter_csv_compiler\
> ```
> 
> Then run:
> 
> ```bash
> python build_QiOne_Tools.py --preset dev-fast
> ```
> 
> Your builder is already designed to scan `tools/<bucket>/<tool>/<tool>.py` and auto-register discovered `BaseTool` classes, so you should not need to manually edit `main_ui.py`. fileciteturn2file0L66-L69 fileciteturn2file2L151-L187
> 
> I put this in the **docs** bucket because your guide defines that bucket for document operations, and this is a Markdown/document export tool, not just cleanup. fileciteturn2file0L75-L88
> 
> I also kept it aligned with your `BaseTool` contract: `get_name`, `build_ui`, and `execute`. fileciteturn2file1L14-L23
> 
> Only caveat: I intentionally avoided adding `PyYAML`. The parser handles normal front matter cleanly, including simple lists, but deeply nested YAML objects will be flattened/preserved as readable text rather than expanded into perfect nested columns. That is the right tradeoff for now: fewer dependencies, less build drama.

### User
> mam does this tool addon meet the specs so its picked up by th ebase tool.

### Assistant
> I’m going to verify it against the actual builder rules, not vibes: folder path, matching Python filename, exported class, `BaseTool` inheritance, and whether the builder regex will see it.

### User
> also why can i just hot swap tools why do i have to rebuild the app every time i add a tool.

### Assistant
> Yes, ma’am — **the addon meets the pickup specs.** I checked the zip structure and the Python file.
> 
> ## Pickup check
> 
> | Requirement | Status |
> |---|---:|
> | Lives under `tools/<bucket>/<tool>/<tool>.py` | ✅ |
> | Folder name matches Python file name | ✅ |
> | Uses existing fixed bucket | ✅ `docs` |
> | Imports `BaseTool` | ✅ |
> | Class inherits `BaseTool` | ✅ |
> | Class name ends in `Tool` | ✅ |
> | Has `get_name()` | ✅ |
> | Has `build_ui()` | ✅ |
> | Has `execute()` | ✅ |
> | Has `__init__.py` re-export | ✅ |
> | Has `manifest.yaml` and `README.md` | ✅ |
> 
> The builder specifically scans this shape:
> 
> ```txt
> tools/<bucket>/<tool>/<tool>.py
> ```
> 
> and then looks for a class declaration matching `class SomethingTool(BaseTool):` or anything with `BaseTool` in the parent class list. Your addon does that. The builder then injects the import and registration into `main_ui.py`. fileciteturn4file0L156-L220 fileciteturn4file0L252-L294
> 
> Tiny nitpick: the zip includes `__pycache__`. That won’t break anything because your builder skips `__pycache__`, but it is trash packaging. Not dangerous, just messy. fileciteturn4file0L175-L184
> 
> ## Why you can’t hot-swap tools right now
> 
> Because your current architecture is **static-registration**, not runtime plugin loading.
> 
> Right now:
> 
> 1. The builder scans the `tools` folder.
> 2. It writes import lines into `main_ui.py`.
> 3. It writes `self.tools = [...]` into `main_ui.py`.
> 4. PyInstaller freezes that version into the app.
> 
> That means the running app only knows about tools that were imported and registered when `main_ui.py` was built. You can see that `main_ui.py` currently has hardcoded imports and a hardcoded `self.tools = [...]` list between the auto markers. fileciteturn3file4L9-L33 fileciteturn3file4L82-L84
> 
> ## The honest answer
> 
> You **can** hot-swap tools, but not with the current design.
> 
> To hot-swap, the app needs a **runtime plugin loader** that scans the `tools` folder when the app opens, imports modules dynamically with `importlib`, finds `BaseTool` subclasses, and registers them without rewriting `main_ui.py`.
> 
> That would let you:
> 
> ```txt
> drop tool folder in tools/docs/
> restart app
> tool appears
> ```
> 
> For true no-restart hot swap, you’d add a **Reload Tools** button. But start with restart-based runtime discovery. That is sane. Live-reloading Python modules inside a Tkinter app gets spicy fast, and not in a cute way.
> 
> ## Best path
> 
> I’d change the architecture like this:
> 
> ```txt
> Current:
> build script scans tools → edits main_ui.py → rebuild exe
> 
> Better:
> main_ui.py scans tools at startup → imports tools dynamically → no rebuild for new tools during dev
> 
> Best later:
> main_ui.py scans external plugins folder beside exe → packaged app can accept dropped-in tools
> ```
> 
> For development, you should absolutely move toward runtime discovery. Rebuilding every time you add a tiny tool is friction garbage.
> 
> For release builds, rebuilding still makes sense unless you intentionally support an external plugin folder. Packaged EXEs are frozen by design, so external hot-swap needs to be designed on purpose, not wished into existence.

### User
> i want to make the python tool builder interactive, there needs to be a option to input what i need to add, it use chatgpt api or local ollama to build the tool using the forrect template folder structure, readme, manifest ect, then add the tool automatically

### Assistant
> Yes. This is the right next upgrade. Rebuilding is tolerable; manually creating folders, manifests, imports, README, and class scaffolds every time is exactly the kind of dumb friction your toolbox should eat.

### Assistant
> The thing I’m building into the patch: **Generate Tool** becomes its own builder menu path. It will gather your request, choose OpenAI/Ollama/template mode, create the correct folder package, validate the class, then inject it into `main_ui.py`.

### User
> ok so like you were saying do we make the base app and each tool a plugin to use plugin folders or something to hotswap tools as we want.

### Assistant
> Yes. **Make the base app stable, and make every tool a plugin folder.** That is the cleaner architecture.
> 
> Right now your builder already treats tools *almost* like plugins: it expects each tool to live in `tools/<bucket>/<tool>/<tool>.py`, and it scans that shape for `BaseTool` subclasses. fileciteturn7file0L156-L190 But then it hard-injects imports/registrations into `main_ui.py`, which forces rebuilds. fileciteturn7file0L252-L270
> 
> ## The better architecture
> 
> ```txt
> QiOne_Tools.exe
> ├── core/
> │   └── base_tool.py
> ├── plugin_loader.py
> ├── main_ui.py
> └── plugins/
>     ├── docs/
>     │   └── md_frontmatter_csv_compiler/
>     │       ├── md_frontmatter_csv_compiler.py
>     │       ├── __init__.py
>     │       ├── manifest.yaml
>     │       └── README.md
>     ├── organize/
>     ├── dev/
>     ├── finance/
>     ├── media/
>     └── system/
> ```
> 
> ## What changes
> 
> ### Current model
> 
> ```txt
> Add tool
> → run builder
> → builder edits main_ui.py
> → rebuild app
> → tool appears
> ```
> 
> ### Plugin model
> 
> ```txt
> Add plugin folder
> → app scans plugins at startup
> → imports tools dynamically
> → tool appears
> ```
> 
> Then later:
> 
> ```txt
> Add plugin folder
> → click Reload Tools
> → tool appears without restart
> ```
> 
> That is the move.
> 
> ## Keep `BaseTool` as the contract
> 
> Do **not** overcomplicate this. A tool is valid if it inherits `BaseTool` and implements:
> 
> ```python
> get_name()
> build_ui(parent_frame)
> execute(target_path, is_dry_run, log_callback, progress_callback)
> ```
> 
> That is already your clean interface. fileciteturn7file2L18-L28
> 
> So the rule becomes:
> 
> > A plugin is just a folder containing a Python file with a valid `BaseTool` subclass plus metadata files.
> 
> ## Recommended folder strategy
> 
> I would keep two tool roots:
> 
> ```txt
> tools/      = built-in/core tools shipped with the app
> plugins/    = drop-in/hot-swappable user tools
> ```
> 
> Why? Because mixing them all into one folder gets messy fast.
> 
> ### Built-in tools
> 
> Stable, trusted, tested:
> 
> ```txt
> tools/docs/pdf_splitter/
> tools/organize/bloat_destroyer/
> tools/system/qilabs_structure_checker/
> ```
> 
> ### Plugins
> 
> Generated, experimental, hot-swappable:
> 
> ```txt
> plugins/docs/md_frontmatter_csv_compiler/
> plugins/organize/gdrive_cleaner/
> plugins/dev/random_new_tool/
> ```
> 
> That gives you a clean safety boundary:
> 
> | Folder | Purpose | Rebuild needed? |
> |---|---|---:|
> | `tools/` | shipped core tools | Usually yes |
> | `plugins/` | generated/drop-in tools | No |
> | `core/` | app contracts/helpers | Yes |
> | `main_ui.py` | shell/UI | Yes |
> 
> ## What the builder should become
> 
> The builder should stop being only a PyInstaller build script. It should become a **Tool Factory + App Builder**.
> 
> Menu should look like:
> 
> ```txt
> QILABS TOOLBOX BUILDER
> 
> 1) Build app - dev fast
> 2) Build app - dev clean
> 3) Build app - debug
> 4) Build app - release
> 5) Build app - release clean
> 
> 6) Generate new tool/plugin
> 7) Validate tools/plugins
> 8) Rebuild tool registry cache
> 9) Package selected plugin as zip
> 
> Q) Quit
> ```
> 
> ## For your AI generator idea
> 
> Yes — but don’t let the AI spray files directly into your app like a raccoon with admin rights.
> 
> Use this pipeline:
> 
> ```txt
> User describes tool
> → Builder collects:
>    - tool name
>    - bucket
>    - purpose
>    - inputs/options
>    - dry-run behavior
>    - live behavior
>    - safety rules
> → AI generates tool package
> → builder writes to plugins/<bucket>/<tool_name>/
> → validator checks structure
> → validator imports class safely
> → optional syntax check
> → optional smoke test
> → plugin becomes available
> ```
> 
> ## OpenAI / Ollama / template fallback
> 
> Use three generation modes:
> 
> | Mode | Use when | Notes |
> |---|---|---|
> | `template` | simple tools | safest, no API |
> | `ollama` | local/offline generation | good for privacy |
> | `openai` | best quality generation | needs API key |
> 
> The builder should ask:
> 
> ```txt
> Generation backend:
> 1) Template only
> 2) Ollama local
> 3) OpenAI API
> ```
> 
> For OpenAI, read from env:
> 
> ```txt
> OPENAI_API_KEY
> ```
> 
> For Ollama, default endpoint:
> 
> ```txt
> http://localhost:11434/api/generate
> ```
> 
> ## Important safety rule
> 
> Generated plugin tools should default to:
> 
> ```yaml
> status: draft
> review_before_live: true
> supports_dry_run: true
> ```
> 
> And the app should visually mark them as draft/experimental until you bless them. Don’t let a half-generated file mover go live and start rearranging your digital house like it pays rent.
> 
> ## My recommended end state
> 
> ```txt
> QiOne Core App
> ├── Stable shell
> ├── Stable BaseTool contract
> ├── Runtime plugin loader
> ├── Plugin validation
> ├── Reload Tools button
> └── Builder that can generate plugins with OpenAI/Ollama/template mode
> ```
> 
> That is the right system.
> 
> The sharp version: **stop making the builder inject every tool into `main_ui.py`.** Keep the app fixed, let it discover tools dynamically, and use the builder to create/validate/package plugins. That gives you speed without turning the codebase into spaghetti confetti.

### User
> ok im aligned, do you want the ide to build it or you build it?

### Assistant
> I should build the first pass. Let the IDE do the boring apply/run/debug loop after that. You don’t need another “idea”; you need a concrete architecture patch with plugin discovery, validation, and a builder menu path.

### Assistant
> I found we already had a partial AI-generator builder file sitting in the uploaded workspace, but it still keeps the old static registration model. I’m not going to double down on that. I’m separating this into two layers: runtime plugin loader for the app, and builder tool-factory for creating plugin folders.

### Assistant
> I built the first-pass patch. **IDE should apply and test it.** That is the right split: I do the architecture work; IDE does the Windows run/debug loop.
> 
> Download it here: [qione_plugin_runtime_patch.zip](sandbox:/mnt/data/qione_plugin_runtime_patch.zip)
> 
> ## What I built
> 
> This patch moves QiOne toward the plugin model:
> 
> ```txt
> core/
>   plugin_loader.py
> 
> tools/
>   built-in shipped tools
> 
> plugins/
>   hot-swappable generated/downloaded tools
> 
> main_ui.py
>   runtime discovery instead of static imports
> 
> build_QiOne_Tools.py
>   generate plugins + build app
> ```
> 
> Your current system was doing static discovery and then injecting imports/registrations into `main_ui.py`, which is exactly why every new tool forced a rebuild. fileciteturn9file0 The existing `BaseTool` contract is still the correct interface, so I kept that intact. fileciteturn9file1
> 
> ## New behavior
> 
> ### App side
> 
> - App scans runtime folders at startup.
> - App has **Reload Tools** button in the sidebar.
> - App has **Loader Issues** button to show broken plugins.
> - Tools can live in:
> 
> ```txt
> tools/<bucket>/<tool>/<tool>.py
> plugins/<bucket>/<tool>/<tool>.py
> ```
> 
> ### Builder side
> 
> The builder now has:
> 
> ```txt
> 6) Generate Plugin
> ```
> 
> It can generate a plugin using:
> 
> ```txt
> 1) Template only
> 2) OpenAI API
> 3) Local Ollama
> ```
> 
> Generated plugins go here by default:
> 
> ```txt
> plugins/<bucket>/<tool_slug>/
> ```
> 
> with:
> 
> ```txt
> <tool_slug>.py
> __init__.py
> manifest.yaml
> README.md
> ```
> 
> ## Included sample plugin
> 
> I moved the Markdown CSV tool into the plugin structure:
> 
> ```txt
> plugins/docs/md_frontmatter_csv_compiler/
> ```
> 
> So you can immediately test whether runtime plugin loading works.
> 
> ## Install
> 
> Extract the zip, then copy these into your toolbox root:
> 
> ```txt
> core/plugin_loader.py
> main_ui.py
> build_QiOne_Tools.py
> plugins/
> ```
> 
> Do **not** manually edit `main_ui.py` for new tools anymore. That era is over. Good riddance.
> 
> ## Test order
> 
> Run this from the toolbox root:
> 
> ```bash
> python build_QiOne_Tools.py --generate-tool
> ```
> 
> Or validate runtime loading indirectly by opening the app and checking whether the Markdown CSV plugin appears.
> 
> Then build:
> 
> ```bash
> python build_QiOne_Tools.py --preset dev-fast
> ```
> 
> ## Caveat
> 
> I validated the Python syntax and confirmed the runtime loader discovers the included plugin cleanly in this environment. I could **not** run the actual Windows Tkinter GUI or PyInstaller EXE build here, so the IDE still needs to do the final integration pass. That’s normal. This is architecture surgery, not a magic wand.
