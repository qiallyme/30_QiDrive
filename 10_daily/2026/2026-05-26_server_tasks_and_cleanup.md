---
layout: page
title: "Server Tasks and Cleanup"
slug: "server_tasks_and_cleanup"
created_at: "2026-05-26 16:54:55"
updated_at: "2026-07-18T11:03:15-04:00"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-008.json"
template_key: master-template
date: 2026-05-26
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a161696-c134-83ea-96fa-0fc917b4c29e"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Server Tasks and Cleanup

## Overview
- **Date**: 2026-05-26 16:54:55
- **Conversation ID**: `6a161696-c134-83ea-96fa-0fc917b4c29e`
- **Source**: `Chat-Export-28513-2026/conversations-008.json`

## Chat History

### User
> ok, what else did we need to get onto the server in this project. also how can we go about cleaning up the chat history in this project.

### Assistant
> Yes. For **QiAccess Start**, the remaining server work is not “more random apps.” It’s making the server match the doctrine: front door, launcher, library, map, control panel. The active blueprint says the goal is one coherent entry point where you can see what exists, launch tools, access protected services, find docs, and reuse the pattern later for Mom’s Care. fileciteturn0file0
> 
> ## What still needs to get onto the server
> 
> ### 1. QiAccess Start itself — fully deployed and wired
> 
> This is priority one.
> 
> Needs to be on `qiserver` and reachable through the current public/protected entry point:
> 
> - `access.qially.com`
> - redirect/entry button to the Tailscale server URL
> - clean homepage/dashboard
> - real bookmarks, not placeholders
> - dark mode
> - simple animated/dopamine-friendly UI
> - service cards with useful labels
> - clear private/public badges
> 
> This is the actual “front door.”
> 
> ### 2. Wiki.js content structure
> 
> Wiki.js is already chosen as the readable knowledge base/manual library.
> 
> Still needed:
> 
> - QiAccess Start section
> - QiServer section
> - Family OS section
> - Mom’s Care section
> - QiNexus section
> - Legal section
> - Finance section
> - Tech runbooks section
> - Personal workflows section
> - Reference section
> 
> Repo docs = engineering truth.  
> Wiki.js = “how do I use this damn thing” truth.
> 
> ### 3. Repo docs pushed and mirrored into server workflow
> 
> The repo should contain:
> 
> - `docs/00_blueprint/QiAccess_Start_Blueprint.md`
> - deployment notes
> - qiserver runbook
> - service map
> - access/exposure rules
> - app folder doctrine
> - roadmap
> - README updates
> 
> The server should have the repo cloned cleanly under the correct path, probably something like:
> 
> `/srv/qios/apps/_QiAccess_Start`
> 
> or whatever final app path we standardize. No more “where the hell did Codex put it” scavenger hunts.
> 
> ### 4. Server service inventory page
> 
> QiAccess needs a page/data file that knows what services exist.
> 
> Minimum services to register:
> 
> - Portainer
> - Cockpit
> - Wiki.js
> - Paperless-ngx
> - Open WebUI
> - Ollama
> - NocoDB
> - Firefly III
> - Qdrant
> - Neo4j
> - Uptime Kuma
> - SolidTime
> - Cloudflared
> - Tailscale links
> - GitHub repo links
> 
> For each service:
> 
> - name
> - purpose
> - URL
> - access type: private, public restricted, public safe
> - status/manual notes
> - restart command or Portainer stack name
> 
> ### 5. Restart/control strategy
> 
> Not full chaos-button automation yet. Just practical control.
> 
> You need:
> 
> - documented restart commands per stack
> - Portainer links per service
> - Uptime Kuma status links
> - maybe a “Restart Runbook” page in Wiki.js
> - later: controlled mini-admin panel or scripts
> 
> Do **not** expose raw restart buttons publicly unless protected. Server-control surfaces stay private/protected.
> 
> ### 6. QiNexus / Google Drive links
> 
> QiAccess should show the storage model:
> 
> - `00_inbox`
> - `01_workbench`
> - `02_timeline`
> - `03_life`
> - `04_people`
> - `05_business`
> - `06_finance`
> - `07_legal`
> - `08_tech`
> - `09_assets`
> - `10_data`
> - `11_reference`
> - `12_archive`
> - `13_system`
> 
> The app does not need to manage files yet. It just needs to show the map and link to the right Drive folders.
> 
> ### 7. Mom’s Care app later, not first
> 
> The blueprint is right: don’t use Mom’s Care as the first refactor target. Get QiAccess Start stable first, then reuse its pattern.
> 
> Mom’s Care eventually needs:
> 
> - dashboard
> - notes/logs
> - supplies
> - appointments
> - reports
> - routines
> - documents
> - emergency/reference info
> 
> But right now, that’s phase two. Don’t let it hijack the server front door.
> 
> ---
> 
> ## Server priority order
> 
> Do this in order:
> 
> 1. **Stabilize QiAccess Start repo on server**
> 2. **Deploy it cleanly**
> 3. **Fix UI enough to not offend God**
> 4. **Replace placeholders with real service links**
> 5. **Add private/public/protected labels**
> 6. **Add Wiki.js section structure**
> 7. **Add qiserver service inventory**
> 8. **Add restart/runbook docs**
> 9. **Add QiNexus storage map**
> 10. **Then reuse pattern for Mom’s Care**
> 
> That’s the thread. Pull that one. Everything else is sparkle dust until this is done.
> 
> ---
> 
> ## How to clean up the project chat history
> 
> Reality check: you probably **do not need to manually clean every chat**. That is a trap. ADHD archaeology. Absolutely not.
> 
> What you need is a **Project Memory / Receipt system** so the useful signal survives and the messy chat history stops mattering.
> 
> ### Best approach
> 
> Create a canonical folder:
> 
> `docs/99_project_receipts/`
> 
> Inside it:
> 
> - `2026-05-26_QiAccess_Server_State.md`
> - `2026-05-26_QiAccess_Open_Loops.md`
> - `2026-05-26_QiAccess_Codex_Prompts.md`
> - `2026-05-26_QiAccess_Decisions.md`
> - `2026-05-26_QiAccess_Service_Inventory.md`
> 
> Then each messy chat gets reduced into:
> 
> - decisions made
> - current server state
> - commands that worked
> - URLs/ports
> - unresolved problems
> - next Codex prompt
> - what is deprecated/no longer true
> 
> ### What to archive mentally
> 
> These chats can be treated as **source material**, not active truth:
> 
> - old QiOS business/client architecture
> - Supabase-first plans for QiAccess
> - multi-tenant portal ideas
> - overbuilt auth ideas
> - old folder trees before the current blueprint
> - “maybe we should” brainstorming that never became deployed reality
> 
> ### What to preserve
> 
> Keep only:
> 
> - actual server URLs
> - working repo path
> - working Docker paths
> - service names and ports
> - current blueprint
> - current roadmap
> - Codex prompts that produced working results
> - deployment commands that worked
> - known problems
> 
> ---
> 
> ## The cleanup rule
> 
> For each chat, extract only this:
> 
> **Decision / Server State / Useful Command / Open Loop / Trash**
> 
> If something does not fit those five buckets, it probably does not deserve oxygen.
> 
> Your project doesn’t need a cleaner chat history. It needs a **canonical state file** that makes the chat history irrelevant.

### User
> one is done and working. 2, yes we need to finish updating the content, really its just the docs in qiaccess that are converted or pushed to the wiki.js, 3, ummm yes, 4, I think that is basically done but we need to double check and actually start working on the workflows and automations that use all these services. 5. yes, 6. umm yes, 7. we are just doing bare minimal right now.

### Assistant
> Perfect. Then the list collapses. We are **not** still in “get the homepage working” mode. That part is done. Good. Now the project moves from **server setup** to **operationalization**.
> 
> Here’s the cleaned current state:
> 
> ## QiAccess Server Status
> 
> ### Done / basically done
> 
> 1. **QiAccess Start is deployed and working**
>    - Front door is live.
>    - Redirect/public-vs-server concept is working.
>    - UI is acceptable enough for now.
>    - We do **not** keep redesigning this unless something blocks usage.
> 
> 2. **Service inventory is mostly done**
>    - We still need to verify links, labels, and access boundaries.
>    - But we are no longer “discovering what exists.”
>    - The next job is using those services together.
> 
> 3. **Mom’s Care is deferred**
>    - Bare minimum only right now.
>    - Do not let it hijack QiAccess.
>    - The blueprint already says Mom’s Care comes after the QiAccess pattern stabilizes. fileciteturn0file0
> 
> ---
> 
> ## What remains now
> 
> ### 1. Finish docs → Wiki.js
> 
> This is the cleanest next task.
> 
> The docs inside QiAccess need to become readable Wiki.js pages.
> 
> Not all repo docs belong in Wiki.js. Split them like this:
> 
> | Source | Destination | Purpose |
> |---|---|---|
> | Blueprint / doctrine | Wiki.js summary page + repo canonical copy | “What is this system?” |
> | Runbooks | Wiki.js | “How do I operate it?” |
> | Service map | Wiki.js + QiAccess data | “Where is everything?” |
> | Deployment notes | Repo docs first, Wiki.js simplified | “How was this built?” |
> | ADRs / decisions | Repo docs canonical, Wiki.js summary | “Why did we choose this?” |
> | User manuals / workflows | Wiki.js | “How do I use it?” |
> 
> Repo docs stay engineering truth. Wiki.js becomes the readable operating manual. That matches the blueprint’s source-of-truth split. fileciteturn0file0
> 
> ---
> 
> ### 2. Double-check repo/server alignment
> 
> This is a fast audit, not a rebuild.
> 
> Need to confirm:
> 
> - server path of the deployed repo
> - GitHub remote is correct
> - pull/deploy process is documented
> - `.env` or config files are not messy
> - QiAccess docs folder exists and is current
> - README tells Codex/human what this project is
> - deployment command is known
> - restart command is known
> 
> Deliverable should be one file:
> 
> `docs/05_operations/QiAccess_Server_Runbook.md`
> 
> ---
> 
> ### 3. Verify service inventory
> 
> This is not “make another dashboard.” It is a truth table.
> 
> Each service needs:
> 
> - name
> - purpose
> - internal URL
> - public/Tailscale URL if any
> - access class: Private Only / Public Restricted / Public Safe
> - Docker stack name
> - data path
> - status: active / testing / parked / broken
> - what workflow uses it
> 
> This matters because the next phase is workflows and automations. If a service is not tied to a workflow, it is just a shiny little server pet.
> 
> ---
> 
> ### 4. Start workflow/automation design
> 
> This is the actual next chapter.
> 
> The service stack exists. Now we decide what jobs the stack performs.
> 
> Initial workflow buckets:
> 
> | Workflow | Services involved |
> |---|---|
> | Document intake | Google Drive / QiNexus → Paperless → Wiki.js/QiAccess |
> | Knowledge lookup | Wiki.js → Open WebUI/Ollama → maybe Qdrant/Neo4j later |
> | Finance ops | Firefly III / NocoDB / Drive exports |
> | Server monitoring | Uptime Kuma → QiAccess service status |
> | Personal dashboard | QiAccess → Wiki.js → service links |
> | Legal/evidence archive | Drive/QiNexus → Paperless → timeline docs |
> | Care docs | Wiki.js + QiAccess links, bare minimum for now |
> | Automation hub | n8n or scripts later, but not until workflows are named |
> 
> Do not automate yet until each workflow has:
> 
> 1. trigger  
> 2. input  
> 3. processing step  
> 4. output  
> 5. where truth lives  
> 6. failure/review step  
> 
> That saves us from building a robot that confidently files things into hell.
> 
> ---
> 
> ## Updated priority order
> 
> This is the new order:
> 
> 1. **Finish pushing/converting QiAccess docs into Wiki.js**
> 2. **Create/update the QiAccess server runbook**
> 3. **Audit service inventory and access classes**
> 4. **Define 5–7 core workflows**
> 5. **Pick the first workflow to automate**
> 6. **Only then wire n8n/scripts/API glue**
> 7. **Keep Mom’s Care bare minimum until the core pattern is stable**
> 
> ## Best next Codex prompt
> 
> Use this:
> 
> Codex, QiAccess Start is now deployed and working. Do not redesign the app or restructure the project unless necessary. Your next job is documentation and operational alignment.
> 
> Please audit the QiAccess repo and server deployment state, then update or create the following docs:
> 
> 1. `docs/00_blueprint/QiAccess_Start_Blueprint.md`
> 2. `docs/05_operations/QiAccess_Server_Runbook.md`
> 3. `docs/02_architecture/Service_Map.md`
> 4. `docs/05_operations/Access_And_Exposure_Rules.md`
> 5. `docs/06_workflows/Core_Workflows.md`
> 6. `docs/06_workflows/Automation_Backlog.md`
> 
> Goals:
> - Confirm the deployed repo path on qiserver.
> - Confirm the GitHub remote.
> - Document how to pull, build, restart, and verify QiAccess.
> - List all known services linked from QiAccess.
> - For each service, document purpose, URL, access class, Docker stack/container name if discoverable, and workflow usage.
> - Prepare docs so the readable content can be copied or pushed into Wiki.js.
> - Keep repo docs as engineering truth and Wiki.js as readable operating manuals.
> - Do not add Supabase, auth, database features, or new app complexity.
> - Do not redesign the UI.
> - Focus on clarity, server operations, and workflow readiness.
> 
> After the audit, produce a short summary of:
> - what was confirmed,
> - what was missing,
> - what docs were updated,
> - what the next automation candidate should be.
> 
> ## Bottom line
> 
> We are past “make it exist.”
> 
> Now the work is:
> 
> **Document it → map it → workflow it → automate it.**
> 
> That is the correct sequence. Anything else is how we end up with twelve dashboards and no damn system.

### User
> also we need to make sure that codex is checking for the actual paths and setup do not assume anything thats how we step on our own toes and dont forget there is codex on my machien for the reposand then codex on the server so anything pushed codex on server would need to pull and deploy if applicable.

### Assistant
> Exactly. That is the missing control rule. We need to stop treating “repo,” “server,” and “deployment” like one magical blob. They are **three different realities**:
> 
> 1. **Your machine Codex** = edits local repos, commits, pushes to GitHub.
> 2. **Server Codex** = inspects actual qiserver paths, pulls from GitHub, deploys/restarts.
> 3. **GitHub** = handoff layer between the two.
> 
> QiAccess already says current reality matters more than theoretical architecture, and that working links/deployment paths should not be broken. fileciteturn0file0 So yes: **Codex must verify before acting. No assumptions.**
> 
> Use this updated prompt.
> 
> ---
> 
> Codex, update your operating mode for QiAccess Start.
> 
> Do not assume paths, repo locations, service names, stack names, ports, remotes, deployment commands, or file structure. Before making changes, inspect the actual environment and document what is real.
> 
> There are two Codex working contexts:
> 
> 1. **Local machine Codex**
>    - Works on Cody’s local Windows machine.
>    - Edits local repos.
>    - Commits changes.
>    - Pushes to GitHub.
>    - Does not assume the server has received those changes.
> 
> 2. **Server Codex**
>    - Works on qiserver.
>    - Inspects actual server paths.
>    - Confirms deployed repo location.
>    - Pulls from GitHub when needed.
>    - Builds/restarts/deploys services only after confirming the correct repo and stack.
>    - Does not assume local changes exist until they are pulled.
> 
> GitHub is the handoff point between local and server.
> 
> Required behavior:
> 
> - First inspect the current directory and repo state before editing.
> - Confirm whether you are on Cody’s local machine or qiserver.
> - Confirm the repo root with `pwd`, `git rev-parse --show-toplevel`, and directory listing.
> - Confirm Git remote with `git remote -v`.
> - Confirm branch with `git branch --show-current`.
> - Confirm working tree state with `git status --short`.
> - If on the server, locate the actual deployed QiAccess path before pulling or deploying.
> - If the expected path does not exist, search under likely roots such as `/srv/qios`, `/srv/qios/apps`, `/srv/qios/stacks`, and the user home directory.
> - Do not create duplicate project folders unless explicitly approved.
> - Do not clone a second copy if a working repo already exists.
> - Do not overwrite `.env`, config files, Docker compose files, or deployment files without backing up or showing the diff.
> - Before deployment, identify the actual deployment method: Docker Compose, static build, Nginx/Caddy/Cloudflare, Node process, or other.
> - If local Codex pushes changes, server Codex must pull and deploy them.
> - If server Codex changes files directly, report that clearly because those changes may need to be committed/pushed back to GitHub.
> 
> Current project objective:
> 
> QiAccess Start is already deployed and working. Do not redesign or rebuild it. The next work is documentation, Wiki.js content prep, server runbook accuracy, service inventory verification, and workflow/automation readiness.
> 
> Tasks:
> 
> 1. Audit actual repo/server setup.
> 2. Confirm actual paths and deployment method.
> 3. Update repo docs only after verifying the real structure.
> 4. Prepare docs for Wiki.js conversion/publishing.
> 5. Verify service inventory and access classes.
> 6. Define core workflows and automation backlog.
> 7. Keep Mom’s Care bare minimum for now.
> 
> Create or update these docs if appropriate:
> 
> - `docs/00_blueprint/QiAccess_Start_Blueprint.md`
> - `docs/02_architecture/Service_Map.md`
> - `docs/05_operations/QiAccess_Server_Runbook.md`
> - `docs/05_operations/Access_And_Exposure_Rules.md`
> - `docs/06_workflows/Core_Workflows.md`
> - `docs/06_workflows/Automation_Backlog.md`
> - `docs/99_project_receipts/Current_Project_State.md`
> 
> For every doc update, include:
> 
> - what was verified,
> - what is assumed,
> - what is unknown,
> - what needs Cody confirmation,
> - what should be pushed to Wiki.js,
> - what stays repo-only.
> 
> Before finishing, output a concise report:
> 
> - Environment detected: local or server
> - Repo path confirmed
> - Git remote confirmed
> - Branch confirmed
> - Deployment path confirmed
> - Services discovered
> - Docs updated
> - Changes committed or not committed
> - Whether server pull/deploy is still needed
> - Next safest action
> 
> Hard rule:
> 
> If you are not sure, inspect.  
> If inspection fails, say what failed.  
> Do not guess and do not create duplicate structure.
> 
> ---
> 
> That last part is the spine:
> 
> **local edits → push → server pull → deploy**
> 
> And if server edits directly, then it becomes:
> 
> **server edits → commit/push back → local pulls later**
> 
> No more “oops, we built the same house in three neighborhoods.”

### User
> ok you want to give me the prompt for codex pc and codex server and we can also use the ide ai for other task concurrently on my pc to help in any way this can be sped along, and i also want to mention while we are on teh topic i dont understand why we dont already have some workflow that indexes the folders we want, imports into paperless, embeds, udpated metadata and file names from the conetent context and keeps a updated file inventory or something, hashes i dont know and updated a rules lists or routing lists taht we can review or there is some approval flow that i can make correcitons and the ai dynamically learns and adjust until eventually is perfect at handling all income files and properly handling them, then GINA can actually be made and utilized.

### Assistant
> Yes — this is the exact moment to split labor cleanly instead of making one Codex do interpretive dance across three machines. I’ll give you three lanes: PC Codex, Server Codex, and IDE AI helper.

### Assistant
> Yes. And you’re right to be annoyed: **we should have an ingestion/indexing/routing workflow.** The reason it doesn’t already exist is not because the idea is hard conceptually. It’s because the pieces exist but the **orchestration layer** has not been formalized yet.
> 
> Right now you have ingredients:
> 
> - Google Drive / QiNexus = storage backbone
> - Paperless = OCR/document intake
> - Wiki.js = human-readable docs
> - Qdrant = embeddings/vector search
> - Neo4j = graph/context relationships
> - Open WebUI/Ollama = local AI interface
> - QiAccess = front door/control panel
> - possible n8n/scripts = automation glue
> 
> What’s missing is the **QiIngest Pipeline**:
> 
> **watch folders → hash files → classify → rename/metadata proposal → Paperless import → embed → inventory update → approval queue → routing rules update → learning loop.**
> 
> That is how GINA becomes useful. Not magic chatbot first. **Clean intake and memory first.**
> 
> ---
> 
> # Lane 1: Codex PC Prompt
> 
> Use this for **Codex on your Windows machine** where the repo lives and where edits/pushes happen.
> 
> ```text
> Codex, you are working on Cody’s LOCAL PC environment.
> 
> Your job is to inspect and update the local QiAccess Start repo only. Do not assume paths. Do not deploy to the server from here.
> 
> Operating rules:
> - First determine where you are.
> - Run inspection commands before editing.
> - Confirm repo root, branch, remotes, and working tree.
> - Do not create duplicate repos or duplicate project folders.
> - Do not overwrite existing docs/configs without checking current contents.
> - This local Codex lane edits, commits, and pushes to GitHub.
> - Server Codex will later pull and deploy from GitHub if needed.
> 
> First inspect:
> - current directory
> - likely repo locations
> - Git repo root
> - Git remote
> - current branch
> - working tree status
> - existing docs folder structure
> - existing QiAccess docs/content that should be pushed or converted to Wiki.js
> 
> Project status:
> QiAccess Start is deployed and working. Do not redesign the UI unless explicitly asked. Current work is documentation, service inventory, workflows, and ingestion/automation planning.
> 
> Main tasks:
> 
> 1. Audit the local QiAccess Start repo structure.
> 2. Find existing docs that should become Wiki.js content.
> 3. Update or create these docs where appropriate:
> 
> - docs/00_blueprint/QiAccess_Start_Blueprint.md
> - docs/02_architecture/Service_Map.md
> - docs/05_operations/QiAccess_Server_Runbook.md
> - docs/05_operations/Access_And_Exposure_Rules.md
> - docs/06_workflows/Core_Workflows.md
> - docs/06_workflows/Automation_Backlog.md
> - docs/06_workflows/QiIngest_Pipeline.md
> - docs/99_project_receipts/Current_Project_State.md
> 
> 4. Add a new workflow plan called QiIngest Pipeline.
> 
> QiIngest Pipeline should define a future local-first workflow for:
> 
> - watching selected folders
> - hashing files
> - detecting duplicates
> - importing documents into Paperless
> - extracting text/OCR results
> - classifying documents by content/context
> - proposing cleaned filenames
> - proposing metadata/tags/correspondents/document types
> - updating a file inventory
> - embedding document text into a vector store such as Qdrant
> - optionally mapping entities/relationships into Neo4j
> - creating an approval queue for Cody to review corrections
> - updating routing rules based on Cody-approved corrections
> - eventually improving classification/routing accuracy over time
> 
> Important:
> Do not build the full pipeline yet unless the repo already has working scripts for it. This task is primarily documentation and architecture planning. If any existing scripts already do part of this, document them and connect them to the plan.
> 
> For every doc update, clearly separate:
> 
> - verified facts
> - assumptions
> - unknowns
> - needs Cody confirmation
> - repo-only content
> - Wiki.js-ready content
> - future automation candidates
> 
> Create a section explaining the two-Codex workflow:
> 
> Local PC Codex:
> - edits repo
> - commits
> - pushes to GitHub
> 
> Server Codex:
> - inspects qiserver
> - pulls from GitHub
> - deploys/restarts if needed
> 
> GitHub:
> - handoff layer between local and server
> 
> Do not pretend server changes have happened just because local changes were pushed.
> 
> After edits:
> - show files changed
> - show summary of changes
> - suggest commit message
> - commit only if working tree looks safe
> - push only if Cody approves or if this session already has permission to proceed
> 
> Final report should include:
> 
> - local repo path confirmed
> - branch confirmed
> - remote confirmed
> - docs found
> - docs updated
> - whether anything is ready for Wiki.js
> - whether server pull/deploy is needed
> - next safest action
> ```
> 
> ---
> 
> # Lane 2: Codex Server Prompt
> 
> Use this for **Codex on qiserver**. Its job is not to invent. Its job is to verify reality, pull updates, and deploy if applicable.
> 
> ```text
> Codex, you are working on qiserver.
> 
> Your job is to inspect the actual server setup for QiAccess Start, verify real paths/services/deployment method, and only pull/deploy changes after confirming the correct repo and stack.
> 
> Do not assume:
> - repo path
> - app path
> - Docker stack name
> - compose file location
> - branch
> - remote
> - port
> - deployment method
> - public URL
> - Tailscale URL
> - Cloudflare tunnel setup
> 
> First determine actual environment.
> 
> Run inspection before making changes:
> - pwd
> - hostname
> - whoami
> - ls of current directory
> - search likely roots:
>   - /srv/qios
>   - /srv/qios/apps
>   - /srv/qios/stacks
>   - /srv/qios/docs
>   - /home/qiadmin
> - find QiAccess Start repo if it exists
> - confirm repo root with git rev-parse --show-toplevel
> - confirm remote with git remote -v
> - confirm branch with git branch --show-current
> - confirm status with git status --short
> - inspect package/deployment files
> - inspect docker compose files if present
> - inspect currently running containers related to QiAccess
> - inspect exposed ports and reverse proxy/tunnel clues
> 
> Project status:
> QiAccess Start is deployed and working. Do not redesign it. Do not clone a second copy unless no working repo exists and Cody approves.
> 
> Main tasks:
> 
> 1. Confirm actual deployed QiAccess path.
> 2. Confirm actual GitHub remote.
> 3. Confirm branch.
> 4. Confirm deployment method.
> 5. Confirm how to pull, build, restart, and verify.
> 6. Confirm whether the server copy is behind GitHub.
> 7. Pull from GitHub only after confirming correct repo/path.
> 8. Deploy/restart only after confirming correct method.
> 9. Do not overwrite .env or deployment config without backing up and showing diff.
> 10. Do not create duplicate folders.
> 
> Also inspect and document known services linked or intended for QiAccess:
> 
> - Portainer
> - Cockpit
> - Wiki.js
> - Paperless-ngx
> - Open WebUI
> - Ollama
> - NocoDB
> - Firefly III
> - Qdrant
> - Neo4j
> - Uptime Kuma
> - SolidTime
> - Cloudflared
> - Tailscale
> - any other discovered qios service
> 
> For each service, collect if discoverable:
> 
> - service name
> - purpose
> - docker container/stack name
> - compose path
> - internal URL/port
> - public or Tailscale URL if known
> - access class:
>   - Private Only
>   - Public Restricted
>   - Public Safe
> - data path if obvious
> - current status:
>   - active
>   - testing
>   - parked
>   - broken
>   - unknown
> 
> Update server-side docs only if this is the correct repo and docs are meant to be tracked. If you update docs directly on server, clearly report that these changes need to be committed/pushed back to GitHub or they may diverge from local PC.
> 
> If local PC Codex has pushed doc updates to GitHub:
> - pull them here
> - verify build still works
> - deploy/restart only if needed
> - confirm live app still works
> 
> Add or update operational docs if appropriate:
> 
> - docs/05_operations/QiAccess_Server_Runbook.md
> - docs/02_architecture/Service_Map.md
> - docs/05_operations/Access_And_Exposure_Rules.md
> - docs/99_project_receipts/Current_Project_State.md
> 
> Add a section to the runbook explaining:
> 
> Local PC Codex:
> - edits
> - commits
> - pushes
> 
> Server Codex:
> - pulls
> - deploys
> - verifies actual runtime
> 
> GitHub:
> - handoff between local and server
> 
> Hard rules:
> - If unsure, inspect.
> - If inspection fails, report the failure.
> - Do not guess.
> - Do not duplicate.
> - Do not deploy from the wrong path.
> - Do not restart random stacks.
> 
> Final report must include:
> 
> - environment detected
> - repo path confirmed
> - Git remote confirmed
> - branch confirmed
> - working tree state
> - deployment method confirmed
> - pull performed or not
> - build performed or not
> - restart/deploy performed or not
> - live verification result
> - services discovered
> - docs updated
> - whether changes need to be pushed back to GitHub
> - next safest action
> ```
> 
> ---
> 
> # Lane 3: IDE AI Helper Prompt
> 
> This is for Cursor/VS Code AI/whatever IDE assistant on your PC. This one should **not** touch deployment. Give it research/refactor/documentation chores.
> 
> ```text
> You are assisting inside the local QiAccess Start codebase.
> 
> Do not deploy. Do not change server files. Do not assume server paths.
> 
> Your job is to help prepare documentation, workflow architecture, and codebase understanding for QiAccess Start.
> 
> First inspect the project structure and summarize:
> - app framework
> - source folders
> - docs folders
> - data/config files
> - service/link config files
> - deployment-related files
> - README status
> 
> Then help with these tasks:
> 
> 1. Identify all existing docs that could be converted into Wiki.js pages.
> 2. Identify all hardcoded service links in the app.
> 3. Identify service data/config files if they exist.
> 4. Identify where launcher cards, access cards, server cards, and storage cards are defined.
> 5. Suggest a clean structure for service inventory data if missing.
> 6. Draft Wiki.js-ready content from existing repo docs.
> 7. Draft a QiIngest Pipeline architecture doc.
> 
> QiIngest Pipeline should describe a future workflow:
> 
> - watched folders
> - file inventory
> - hashing
> - deduplication
> - Paperless import
> - OCR/text extraction
> - metadata proposal
> - filename proposal
> - routing proposal
> - human approval queue
> - correction memory
> - routing rules
> - embeddings
> - Qdrant vector index
> - Neo4j relationship graph
> - Wiki.js readable summaries
> - QiAccess status/control view
> - GINA retrieval layer
> 
> Important:
> Do not build heavy automation yet.
> Do not add a database yet.
> Do not add Supabase.
> Do not redesign the UI.
> Do not restructure the app unless there is a clear reason.
> 
> Deliverables to draft or update:
> 
> - docs/06_workflows/QiIngest_Pipeline.md
> - docs/06_workflows/Core_Workflows.md
> - docs/06_workflows/Automation_Backlog.md
> - docs/02_architecture/Service_Map.md
> - docs/99_project_receipts/Current_Project_State.md
> 
> For each proposed workflow, include:
> 
> - trigger
> - input
> - processor
> - output
> - source of truth
> - human review step
> - failure handling
> - automation readiness score from 1 to 5
> 
> Final output:
> - files inspected
> - files changed
> - recommended next edits
> - any broken links or missing config discovered
> - what should be handed to Server Codex
> ```
> 
> ---
> 
> # The workflow you’re describing: yes, that is GINA’s skeleton
> 
> You’re basically describing a **closed-loop knowledge ingestion system**.
> 
> Not this:
> 
> **dump files → hope AI finds them later**
> 
> But this:
> 
> **capture → fingerprint → understand → propose → approve → route → index → learn.**
> 
> That is the correct architecture.
> 
> ## Name it
> 
> I’d call the system:
> 
> **QiIngest**
> 
> The full pipeline:
> 
> **QiIngest → QiIndex → QiRoute → QiRecall → GINA**
> 
> Meaning:
> 
> | Layer | Job |
> |---|---|
> | QiIngest | intake files from watched folders |
> | QiIndex | inventory, hash, OCR, embeddings |
> | QiRoute | classify, rename, tag, move/propose destination |
> | QiReview | approval queue where Cody corrects mistakes |
> | QiRecall | searchable memory through Wiki/Qdrant/Neo4j |
> | GINA | conversational layer over the structured memory |
> 
> GINA should not be born as a chatbot. That would be cute but useless.
> 
> GINA should be born as the interface on top of a disciplined memory pipeline.
> 
> ---
> 
> # The actual ingestion pipeline
> 
> ## Phase 1: Inventory only
> 
> Start stupid simple.
> 
> Input folders:
> 
> - Google Drive / QiNexus folders
> - Paperless consume folder
> - local drop folders
> - maybe downloads folder later
> 
> For every file:
> 
> - path
> - filename
> - extension
> - size
> - created date
> - modified date
> - hash
> - source folder
> - current status
> - duplicate status
> - last indexed date
> 
> Output:
> 
> - `file_inventory.csv` or SQLite table
> - no moving files yet
> - no renaming yet
> - no “AI decided your life” nonsense
> 
> This phase answers:
> 
> **What exists?**
> 
> ---
> 
> ## Phase 2: Paperless import tracking
> 
> Next:
> 
> - detect new PDFs/images/docs
> - copy/import into Paperless consume folder
> - track Paperless document ID if available
> - record OCR status
> - record tags/correspondent/document type if available
> 
> This phase answers:
> 
> **What got processed?**
> 
> ---
> 
> ## Phase 3: AI proposal only
> 
> AI does not rename or move things yet.
> 
> It proposes:
> 
> - cleaned title
> - document type
> - likely bucket
> - tags
> - date detected from content
> - people/entities
> - summary
> - confidence score
> - suggested filename
> - suggested destination
> - reason for suggestion
> 
> This phase answers:
> 
> **What does this appear to be?**
> 
> ---
> 
> ## Phase 4: Human approval queue
> 
> This is the money step.
> 
> You need a table/view with:
> 
> - original filename
> - AI suggested filename
> - AI suggested bucket
> - AI tags
> - summary
> - confidence
> - approve / edit / reject
> - Cody correction notes
> 
> This could live in:
> 
> - NocoDB first
> - simple SQLite + web UI later
> - maybe even CSV/manual at first
> 
> This phase answers:
> 
> **Did Cody approve the routing?**
> 
> ---
> 
> ## Phase 5: Rule learning
> 
> Every approved correction updates routing rules.
> 
> Example:
> 
> If Cody changes:
> 
> `bank_statement_may.pdf → 06_finance/banking/statements/chase`
> 
> The system learns:
> 
> - Chase statements go to finance
> - detect Chase by logo/text/account pattern
> - use statement date
> - filename pattern should be consistent
> 
> This creates:
> 
> - `routing_rules.yml`
> - `naming_rules.yml`
> - `tagging_rules.yml`
> - `entity_aliases.yml`
> 
> This phase answers:
> 
> **What did the system learn from corrections?**
> 
> ---
> 
> ## Phase 6: Embeddings + recall
> 
> Once the text is clean:
> 
> - chunk document text
> - embed into Qdrant
> - store metadata with each chunk
> - connect people/accounts/entities in Neo4j if useful
> - expose search through GINA/Open WebUI later
> 
> This phase answers:
> 
> **Can GINA find this later?**
> 
> ---
> 
> # Minimal stack for first version
> 
> Don’t overbuild it.
> 
> Use:
> 
> - Python scripts
> - SQLite
> - Paperless API
> - local folders
> - Qdrant later
> - NocoDB as approval UI if convenient
> - YAML rules files
> - Git-tracked configs
> 
> Not required yet:
> 
> - Supabase
> - complex auth
> - multi-user anything
> - fancy UI
> - agent swarm
> - autonomous file moving
> - “perfect” classification
> 
> Nope. Baby robot gets training wheels.
> 
> ---
> 
> # First automation candidate
> 
> The first real build should be:
> 
> ## QiIngest Inventory Scanner
> 
> It should:
> 
> 1. scan configured folders
> 2. hash files
> 3. detect duplicates
> 4. write/update inventory
> 5. produce a review report
> 
> No AI yet.
> 
> Why? Because if you don’t know what files exist, everything else is vibes in a trench coat.
> 
> ---
> 
> # Add this to Codex PC prompt if you want it to start blueprinting QiIngest now
> 
> ```text
> Also add a new documentation section for QiIngest.
> 
> Create or update:
> 
> - docs/06_workflows/QiIngest_Pipeline.md
> - docs/06_workflows/QiIngest_Phase_1_File_Inventory.md
> - docs/06_workflows/QiIngest_Routing_Rules.md
> - docs/06_workflows/QiIngest_Approval_Flow.md
> 
> Document the phased approach:
> 
> Phase 1:
> File inventory scanner only.
> 
> Phase 2:
> Paperless import tracking.
> 
> Phase 3:
> AI metadata/filename/routing proposal.
> 
> Phase 4:
> Human approval queue.
> 
> Phase 5:
> Routing/naming/tagging rule updates from approved corrections.
> 
> Phase 6:
> Embeddings and GINA recall.
> 
> For Phase 1, propose a practical Python script design:
> 
> - config file listing watched folders
> - SQLite database or CSV output
> - SHA256 file hashing
> - duplicate detection
> - file metadata capture
> - scan timestamp
> - status field
> - no file moving
> - no file renaming
> - no deletion
> - dry-run first
> 
> Do not implement unless asked. Produce the architecture and implementation checklist first.
> ```
> 
> ---
> 
> # The clean division of labor
> 
> ## PC Codex does:
> 
> - docs
> - repo edits
> - Git commits
> - GitHub push
> - QiIngest architecture
> - Wiki.js-ready content prep
> 
> ## Server Codex does:
> 
> - actual path verification
> - service discovery
> - pull from GitHub
> - deploy/restart
> - runtime docs
> - service map verification
> 
> ## IDE AI does:
> 
> - codebase inspection
> - doc drafting
> - broken link finding
> - data/config refactor suggestions
> - QiIngest pipeline planning
> 
> ---
> 
> # The next move
> 
> Run them in this order:
> 
> 1. **IDE AI** inspects local repo and drafts QiIngest/workflow docs.
> 2. **PC Codex** reviews/updates docs, commits, pushes.
> 3. **Server Codex** verifies real server paths, pulls, deploys if needed.
> 4. **PC Codex or IDE AI** prepares Wiki.js-ready pages.
> 5. **Server Codex** verifies Wiki.js access/content path/process.
> 
> That gives us speed without letting three little goblins edit the same wall from different sides.

### User
> heres the docs folder structure just to give you a reminder on the current folder setup, qiarchive is on gdrive {

>   "name": "docs",

>   "path": "c:\\QiLabs\\_QiAccess_Start\\docs",

>   "type": "directory",

>   "children": [],

>   "metadata": {

>     "generated": "2026-05-26T22:24:33.821Z",

>     "generator": "FileTree Pro Extension",

>     "version": "0.2.0",

>     "showIcons": false,

>     "maxDepth": 10

>   }

> }

### Assistant
> Got it. That changes the prompt slightly.
> 
> Your current local docs folder is:
> 
> `c:\QiLabs\_QiAccess_Start\docs`
> 
> And according to that tree export, it currently has **no child folders/files listed**. So either:
> 
> 1. the docs folder is actually empty,
> 2. FileTree Pro didn’t expand/populate the children correctly,
> 3. docs exist somewhere else in the repo,
> 4. Codex/server has docs that your PC copy doesn’t,
> 5. or the working content is in app/source files and needs to be converted into docs.
> 
> That means **Codex must not assume the docs already exist.** It needs to inspect the repo and create the docs structure if missing.
> 
> Also: QiArchive being on Google Drive means we should treat it as the **storage/archive backbone**, not the app repo. The blueprint already says Google Drive/QiNexus is the storage backbone while repo docs and Wiki.js have different truth roles. fileciteturn0file0
> 
> ## Updated PC Codex Prompt
> 
> Use this version instead of the earlier one:
> 
> ```text
> Codex, you are working on Cody’s LOCAL PC environment.
> 
> Current known local path:
> c:\QiLabs\_QiAccess_Start
> 
> Known docs folder path:
> c:\QiLabs\_QiAccess_Start\docs
> 
> Important:
> A recent FileTree export showed the docs folder exists but has no listed children. Do not assume docs are already present. Inspect the actual repo before deciding whether docs are empty, missing, elsewhere, or not captured by the export.
> 
> QiArchive is on Google Drive and should be treated as the storage/archive backbone, not as the app repo.
> 
> Your job is to inspect and update the local QiAccess Start repo only. Do not deploy to the server from here.
> 
> Operating rules:
> - First determine where you are.
> - Do not assume paths beyond the known candidate path.
> - Inspect before editing.
> - Confirm repo root, branch, remotes, and working tree.
> - Do not create duplicate repos or duplicate project folders.
> - Do not overwrite existing docs/configs without checking current contents.
> - This local Codex lane edits, commits, and pushes to GitHub.
> - Server Codex will later pull and deploy from GitHub if needed.
> 
> First inspect:
> 
> cd c:\QiLabs\_QiAccess_Start
> 
> Then confirm:
> - current directory
> - Git repo root
> - Git remote
> - current branch
> - working tree status
> - existing docs folder structure
> - whether docs are empty
> - whether docs exist elsewhere in the repo
> - existing README content
> - existing app/source content that should become docs or Wiki.js pages
> - existing service/link config files
> - existing deployment files
> 
> Project status:
> QiAccess Start is deployed and working. Do not redesign the UI unless explicitly asked. Current work is documentation, service inventory, workflows, and ingestion/automation planning.
> 
> Main tasks:
> 
> 1. Audit the local QiAccess Start repo structure.
> 2. Determine whether the docs folder is empty or just not captured by the tree export.
> 3. If docs are missing, create the docs structure.
> 4. If docs already exist elsewhere, do not duplicate; reconcile and document.
> 5. Find existing content that should become Wiki.js pages.
> 6. Update or create these docs where appropriate:
> 
> - docs/00_blueprint/QiAccess_Start_Blueprint.md
> - docs/02_architecture/Service_Map.md
> - docs/05_operations/QiAccess_Server_Runbook.md
> - docs/05_operations/Access_And_Exposure_Rules.md
> - docs/06_workflows/Core_Workflows.md
> - docs/06_workflows/Automation_Backlog.md
> - docs/06_workflows/QiIngest_Pipeline.md
> - docs/06_workflows/QiIngest_Phase_1_File_Inventory.md
> - docs/06_workflows/QiIngest_Routing_Rules.md
> - docs/06_workflows/QiIngest_Approval_Flow.md
> - docs/99_project_receipts/Current_Project_State.md
> 
> Docs structure to create if missing:
> 
> docs/
>   00_blueprint/
>   02_architecture/
>   05_operations/
>   06_workflows/
>   99_project_receipts/
> 
> Do not overbuild the docs tree yet. Keep it lean.
> 
> QiIngest Pipeline should define a future local-first workflow for:
> 
> - watching selected folders
> - hashing files
> - detecting duplicates
> - maintaining a file inventory
> - importing documents into Paperless
> - extracting OCR/text
> - classifying documents by content/context
> - proposing cleaned filenames
> - proposing metadata/tags/correspondents/document types
> - proposing destination/routing
> - creating a human approval queue
> - recording Cody’s corrections
> - updating routing/naming/tagging rules based on approved corrections
> - embedding document text into Qdrant
> - optionally mapping entities/relationships into Neo4j
> - supporting future GINA recall/search
> 
> Important:
> Do not build the full QiIngest pipeline yet unless the repo already has working scripts for it. This task is primarily documentation and architecture planning.
> 
> For Phase 1, document a practical file inventory scanner design:
> 
> - config file listing watched folders
> - SQLite database or CSV output
> - SHA256 file hashing
> - duplicate detection
> - file metadata capture
> - scan timestamp
> - status field
> - no file moving
> - no file renaming
> - no deletion
> - dry-run first
> 
> For every doc update, clearly separate:
> 
> - verified facts
> - assumptions
> - unknowns
> - needs Cody confirmation
> - repo-only content
> - Wiki.js-ready content
> - future automation candidates
> 
> Also document the two-Codex workflow:
> 
> Local PC Codex:
> - edits repo
> - commits
> - pushes to GitHub
> 
> Server Codex:
> - inspects qiserver
> - pulls from GitHub
> - deploys/restarts if needed
> 
> GitHub:
> - handoff layer between local and server
> 
> Do not pretend server changes have happened just because local changes were pushed.
> 
> After edits:
> - show files changed
> - show summary of changes
> - suggest commit message
> - commit only if working tree looks safe
> - push only if Cody approves or if this session already has permission to proceed
> 
> Final report should include:
> 
> - local repo path confirmed
> - branch confirmed
> - remote confirmed
> - docs folder status
> - docs found
> - docs created/updated
> - whether anything is ready for Wiki.js
> - whether server pull/deploy is needed
> - next safest action
> ```
> 
> ## Tiny correction to our mental map
> 
> Right now, assume:
> 
> | Thing | Role |
> |---|---|
> | `c:\QiLabs\_QiAccess_Start` | local app repo |
> | `c:\QiLabs\_QiAccess_Start\docs` | local repo docs, maybe empty |
> | GitHub repo | handoff between PC and server |
> | qiserver repo copy | deployed/runtime version |
> | QiArchive on Google Drive | storage/archive backbone |
> | Wiki.js | readable operating manual |
> 
> The next move is not “update docs.” The next move is:
> 
> **verify whether docs exist at all, then create the minimum correct docs tree.**
> 
> Good catch, because otherwise Codex would happily write a beautiful runbook into the wrong damn universe.

### User
> no that was just hte extension tripping here is the full treee.

### Assistant
> Ahhh, there it is. The extension wasn’t just tripping — it lied with confidence. Classic.
> 
> Your docs folder is **not empty**. It is already a whole documentation universe: **129 folders and 445 files** under `c:\QiLabs\_QiAccess_Start\docs`. fileciteturn1file0
> 
> So we need to **stop creating a new docs structure** and instead tell Codex to **align, audit, and promote existing docs**.
> 
> ## Corrected mental map
> 
> You already have major doc zones:
> 
> | Folder | Role |
> |---|---|
> | `docs/10_qicore/` | core doctrine, governance, architecture, registries, services, operations |
> | `docs/20_qinexus/` | QiNexus storage model / personal workspace map |
> | `docs/30_qiarchive/` | ingestion, extraction, chunking, embeddings, graphs, retrieval, memory |
> | `docs/40_qisystem/` | logs, audits, backups, generated reports, maintenance |
> | `docs/50_qiserver/` | currently exists but appears empty from tree |
> | `docs/60_qiapps/` | currently exists but appears empty from tree |
> | `docs/70_qiconnect/` | qifleet / connection layer |
> | `docs/configs`, `widgets`, `installation`, etc. | likely Homepage/gethomepage inherited docs |
> | `docs/notes/` | active notes/ADRs, including homepage-powered QiAccess |
> | `docs/10_qicore/60_knowledge/90_superseded_sources/` | old/ancestor docs quarantine |
> 
> The big important correction: **QiIngest already has a natural home.**
> 
> It belongs primarily in:
> 
> `docs/30_qiarchive/`
> 
> Because that tree already has:
> 
> - `10_ingestion`
> - `20_extraction`
> - `30_chunking`
> - `40_embeddings`
> - `50_graphs`
> - `60_retrieval`
> - `70_memory`
> - `80_sync_backups`
> 
> That is literally the pipeline skeleton. We don’t need to invent it. We need to wire it.
> 
> ## Where the new docs should go
> 
> Instead of creating `docs/06_workflows/`, use the existing structure:
> 
> | Needed doc | Correct location |
> |---|---|
> | QiIngest pipeline overview | `docs/30_qiarchive/10_ingestion/qiingest_pipeline.md` |
> | Phase 1 file inventory | `docs/30_qiarchive/10_ingestion/file_inventory_scanner.md` |
> | Paperless import flow | `docs/30_qiarchive/10_ingestion/10_paperless/paperless_import_workflow.md` |
> | Routing rules | `docs/30_qiarchive/10_ingestion/routing_rules.md` or `docs/10_qicore/10_governance/30_standards/routing_rules.yaml` |
> | Metadata/naming rules | existing `docs/10_qicore/10_governance/30_standards/metadata_rules.yaml` and `naming_rules.yaml` |
> | Embedding workflow | `docs/30_qiarchive/40_embeddings/` |
> | Graph workflow | `docs/30_qiarchive/50_graphs/` |
> | GINA memory/recall | `docs/30_qiarchive/70_memory/10_gina_profiles/` and `docs/10_qicore/40_service_apps/130_GINA/` |
> | Server runbook | `docs/50_qiserver/` |
> | App-specific QiAccess docs | `docs/60_qiapps/qiaccess_start/` maybe |
> | Current state receipt | `docs/40_qisystem/50_generated_reports/` or `docs/10_qicore/50_operations/30_dev_history/` |
> 
> No new parallel tree unless there’s a reason. Otherwise we become the very chaos we are trying to imprison. Rude.
> 
> ---
> 
> # Corrected PC Codex Prompt
> 
> Use this now:
> 
> ```text
> Codex, you are working on Cody’s LOCAL PC environment.
> 
> Current known local repo path:
> c:\QiLabs\_QiAccess_Start
> 
> Current known docs path:
> c:\QiLabs\_QiAccess_Start\docs
> 
> Important correction:
> The docs folder is NOT empty. A full tree export shows approximately 129 folders and 445 files. Do not create a new parallel docs architecture. Inspect and align with the existing structure.
> 
> Existing major docs zones include:
> 
> - docs/10_qicore/
> - docs/20_qinexus/
> - docs/30_qiarchive/
> - docs/40_qisystem/
> - docs/50_qiserver/
> - docs/60_qiapps/
> - docs/70_qiconnect/
> - docs/notes/
> - docs/configs/
> - docs/widgets/
> - docs/installation/
> 
> QiArchive is also conceptually tied to Google Drive / QiNexus storage, but this repo contains QiArchive documentation under docs/30_qiarchive. Treat repo docs as documentation/source-of-truth, not as the actual Drive archive.
> 
> Your job:
> Audit and align the existing documentation. Do not invent a new folder tree.
> 
> Operating rules:
> - Inspect before editing.
> - Confirm repo root, branch, remotes, and working tree.
> - Do not duplicate existing docs.
> - Do not create `docs/06_workflows/` unless there is already a strong project reason.
> - Use the existing numbered docs structure.
> - Do not redesign the UI.
> - Do not deploy from the PC.
> - This local Codex lane edits, commits, and pushes to GitHub.
> - Server Codex later pulls and deploys if needed.
> 
> First inspect:
> 
> cd c:\QiLabs\_QiAccess_Start
> 
> Then confirm:
> - pwd
> - git rev-parse --show-toplevel
> - git remote -v
> - git branch --show-current
> - git status --short
> - docs folder structure
> - existing README files
> - existing _index.md files
> - existing QiAccess Start docs
> - existing QiArchive ingestion/extraction/chunking/embedding/retrieval/memory docs
> - existing service/app docs
> - existing Homepage/gethomepage inherited docs
> - existing notes/ADRs
> 
> Known tree highlights:
> - docs/10_qicore/10_governance/
> - docs/10_qicore/20_structure/
> - docs/10_qicore/30_data/
> - docs/10_qicore/40_service_apps/
> - docs/10_qicore/50_operations/
> - docs/10_qicore/60_knowledge/
> - docs/20_qinexus/
> - docs/30_qiarchive/
> - docs/40_qisystem/
> - docs/50_qiserver/
> - docs/60_qiapps/
> - docs/notes/
> 
> Main tasks:
> 
> 1. Audit the current docs structure.
> 2. Identify which docs are active doctrine.
> 3. Identify which docs are inherited Homepage/gethomepage docs.
> 4. Identify which docs are superseded/legacy/quarantined.
> 5. Identify gaps for QiAccess Start, QiServer, Wiki.js, and QiIngest.
> 6. Update existing docs where appropriate instead of creating duplicates.
> 7. Add missing docs only in the correct existing folders.
> 
> Preferred locations:
> 
> QiAccess Start app docs:
> - docs/60_qiapps/qiaccess_start/
> 
> QiServer runbooks:
> - docs/50_qiserver/
> 
> Service maps:
> - docs/10_qicore/40_service_apps/
> - docs/10_qicore/20_structure/30_component_map.md
> - docs/10_qicore/20_structure/40_service_boundaries.md
> 
> Access and exposure rules:
> - docs/10_qicore/20_structure/70_runtime_zones.md
> - docs/10_qicore/40_service_apps/10_infrastructure/
> - docs/50_qiserver/
> 
> QiIngest / ingestion pipeline:
> - docs/30_qiarchive/10_ingestion/
> 
> File inventory scanner:
> - docs/30_qiarchive/10_ingestion/file_inventory_scanner.md
> 
> Paperless workflow:
> - docs/30_qiarchive/10_ingestion/10_paperless/paperless_import_workflow.md
> 
> Extraction/OCR:
> - docs/30_qiarchive/20_extraction/
> 
> Chunking:
> - docs/30_qiarchive/30_chunking/
> 
> Embeddings/Qdrant:
> - docs/30_qiarchive/40_embeddings/
> 
> Graphs/Neo4j:
> - docs/30_qiarchive/50_graphs/
> 
> Retrieval/RAG:
> - docs/30_qiarchive/60_retrieval/
> 
> GINA memory:
> - docs/30_qiarchive/70_memory/
> - docs/10_qicore/40_service_apps/130_GINA/
> 
> Generated reports/current state:
> - docs/40_qisystem/50_generated_reports/
> 
> Development history/session receipts:
> - docs/10_qicore/50_operations/30_dev_history/
> 
> Create or update these docs if missing or stale:
> 
> - docs/60_qiapps/qiaccess_start/_index.md
> - docs/60_qiapps/qiaccess_start/overview.md
> - docs/60_qiapps/qiaccess_start/wiki_publish_plan.md
> - docs/50_qiserver/_index.md
> - docs/50_qiserver/qiserver_runbook.md
> - docs/50_qiserver/deployment_map.md
> - docs/50_qiserver/access_and_exposure_rules.md
> - docs/30_qiarchive/10_ingestion/qiingest_pipeline.md
> - docs/30_qiarchive/10_ingestion/file_inventory_scanner.md
> - docs/30_qiarchive/10_ingestion/routing_approval_flow.md
> - docs/30_qiarchive/10_ingestion/10_paperless/paperless_import_workflow.md
> - docs/40_qisystem/50_generated_reports/current_project_state.md
> 
> QiIngest Pipeline should define a local-first workflow for:
> - watching selected folders
> - hashing files
> - detecting duplicates
> - maintaining a file inventory
> - importing documents into Paperless
> - extracting OCR/text
> - classifying documents by content/context
> - proposing cleaned filenames
> - proposing metadata/tags/correspondents/document types
> - proposing destination/routing
> - creating a human approval queue
> - recording Cody’s corrections
> - updating routing/naming/tagging rules based on approved corrections
> - embedding document text into Qdrant
> - optionally mapping entities/relationships into Neo4j
> - supporting future GINA recall/search
> 
> Important:
> Do not build the full QiIngest pipeline yet unless existing scripts already support part of it. First document architecture, phases, safety rules, and implementation checklist.
> 
> For Phase 1, document a practical file inventory scanner:
> - config file listing watched folders
> - SQLite database preferred, CSV export optional
> - SHA256 hashing
> - duplicate detection
> - file metadata capture
> - scan timestamp
> - status field
> - source path
> - proposed destination path
> - review status
> - no file moving
> - no file renaming
> - no deletion
> - dry-run first
> 
> For every doc update, separate:
> - verified facts
> - assumptions
> - unknowns
> - needs Cody confirmation
> - repo-only content
> - Wiki.js-ready content
> - future automation candidates
> 
> Also document the two-Codex workflow:
> 
> Local PC Codex:
> - edits repo
> - commits
> - pushes to GitHub
> 
> Server Codex:
> - inspects qiserver
> - pulls from GitHub
> - deploys/restarts if needed
> 
> GitHub:
> - handoff layer between local and server
> 
> Do not pretend server changes have happened just because local changes were pushed.
> 
> After edits:
> - show files changed
> - show summary of changes
> - suggest commit message
> - commit only if working tree looks safe
> - push only if Cody approves or if this session already has permission to proceed
> 
> Final report must include:
> - local repo path confirmed
> - branch confirmed
> - remote confirmed
> - docs structure confirmed
> - active docs found
> - legacy/superseded docs found
> - docs created/updated
> - Wiki.js-ready docs
> - server pull/deploy needed or not
> - next safest action
> ```
> 
> ---
> 
> # Corrected Server Codex Prompt
> 
> Use this on qiserver:
> 
> ```text
> Codex, you are working on qiserver.
> 
> Your job is to inspect the actual server setup for QiAccess Start and align it with the existing repo docs structure. Do not assume paths, stack names, ports, deployment method, or repo location.
> 
> Important:
> The local repo docs folder is not empty. It contains a large structured documentation system under docs/, including:
> - docs/10_qicore/
> - docs/20_qinexus/
> - docs/30_qiarchive/
> - docs/40_qisystem/
> - docs/50_qiserver/
> - docs/60_qiapps/
> - docs/70_qiconnect/
> 
> Do not create a separate docs structure on the server. Pull and preserve the existing repo structure.
> 
> First determine actual environment:
> - pwd
> - hostname
> - whoami
> - search likely roots:
>   - /srv/qios
>   - /srv/qios/apps
>   - /srv/qios/stacks
>   - /srv/qios/docs
>   - /home/qiadmin
> 
> Find the actual deployed QiAccess Start repo.
> 
> Once found, confirm:
> - git rev-parse --show-toplevel
> - git remote -v
> - git branch --show-current
> - git status --short
> - deployment method
> - docker compose files if any
> - running containers related to QiAccess
> - exposed ports
> - reverse proxy/tunnel configuration clues
> - whether docs/ exists and matches the expected structure
> 
> Project status:
> QiAccess Start is deployed and working. Do not redesign it. Do not clone a second copy unless no working repo exists and Cody approves.
> 
> Main tasks:
> 
> 1. Confirm actual deployed QiAccess path.
> 2. Confirm actual GitHub remote.
> 3. Confirm branch.
> 4. Confirm deployment method.
> 5. Confirm docs structure on server.
> 6. Confirm whether server repo is behind GitHub.
> 7. Pull from GitHub only after confirming correct repo/path.
> 8. Deploy/restart only after confirming correct method.
> 9. Do not overwrite .env or deployment config without backing up and showing diff.
> 10. Do not create duplicate folders.
> 
> Inspect and document known services:
> - Portainer
> - Cockpit
> - Wiki.js
> - Paperless-ngx
> - Open WebUI
> - Ollama
> - NocoDB
> - Firefly III
> - Qdrant
> - Neo4j
> - Uptime Kuma
> - SolidTime
> - Cloudflared
> - Tailscale
> - any other discovered qios service
> 
> For each service, collect if discoverable:
> - service name
> - purpose
> - docker container/stack name
> - compose path
> - internal URL/port
> - public or Tailscale URL if known
> - access class:
>   - Private Only
>   - Public Restricted
>   - Public Safe
> - data path if obvious
> - current status:
>   - active
>   - testing
>   - parked
>   - broken
>   - unknown
> 
> Use/update these existing doc locations if appropriate:
> - docs/50_qiserver/
> - docs/10_qicore/40_service_apps/
> - docs/10_qicore/20_structure/
> - docs/40_qisystem/50_generated_reports/
> - docs/10_qicore/50_operations/30_dev_history/
> 
> Do not create docs/06_workflows unless the repo already uses that path.
> 
> If local PC Codex has pushed doc updates:
> - pull them here
> - verify build still works
> - deploy/restart only if needed
> - confirm live app still works
> 
> Final report must include:
> - environment detected
> - repo path confirmed
> - Git remote confirmed
> - branch confirmed
> - working tree state
> - docs structure confirmed
> - deployment method confirmed
> - pull performed or not
> - build performed or not
> - restart/deploy performed or not
> - live verification result
> - services discovered
> - docs updated
> - whether changes need to be pushed back to GitHub
> - next safest action
> 
> Hard rules:
> - If unsure, inspect.
> - If inspection fails, report the failure.
> - Do not guess.
> - Do not duplicate.
> - Do not deploy from the wrong path.
> - Do not restart random stacks.
> ```
> 
> ---
> 
> # Big correction: QiIngest is not a new thing
> 
> Your docs already prove the architecture was forming.
> 
> `docs/30_qiarchive/` already has the exact pipeline stages:
> 
> 1. ingestion  
> 2. extraction  
> 3. chunking  
> 4. embeddings  
> 5. graphs  
> 6. retrieval  
> 7. memory  
> 8. sync/backups  
> 
> That means the next phase is not “design from scratch.”
> 
> It is:
> 
> **turn the existing QiArchive doc skeleton into an executable pipeline roadmap.**
> 
> And that is exactly how GINA gets born without becoming another mystical assistant with no memory and vibes for credentials.

### User
> now remember inside of the docs we house all the kb articles about the tools etc, but the really folders are on gdrive right you understood that.

### Assistant
> Yes — exactly.
> 
> There are **two different “folder systems”** here, and they should not be mentally merged.
> 
> ## 1. Repo `docs/` = KB articles + doctrine + tool docs
> 
> Local path:
> 
> `c:\QiLabs\_QiAccess_Start\docs`
> 
> This is where you’re housing:
> 
> - KB articles about tools
> - service docs
> - runbooks
> - app notes
> - standards
> - architecture
> - registries
> - workflow docs
> - Wiki.js-ready markdown
> - Homepage/gethomepage reference docs
> - QiArchive/QiNexus/QiServer documentation
> 
> That tree is the **knowledge/documentation layer**, not the actual storage warehouse. The uploaded tree shows it contains docs like `10_qicore`, `20_qinexus`, `30_qiarchive`, `40_qisystem`, and service/tool article folders. fileciteturn1file0
> 
> ## 2. Google Drive / QiArchive / QiNexus = real file storage
> 
> The **real folders and actual working/archive files** live on Google Drive.
> 
> That is where the actual stuff lives:
> 
> - incoming files
> - PDFs
> - statements
> - exports
> - personal records
> - legal files
> - finance docs
> - media/assets
> - archive material
> - evidence
> - source documents
> 
> So when the repo has:
> 
> `docs/30_qiarchive/10_ingestion/`
> 
> That is **documentation about the QiArchive ingestion system**.
> 
> It is not necessarily the actual Google Drive folder where ingestion files live.
> 
> Clean rule:
> 
> | Thing | Meaning |
> |---|---|
> | `repo/docs/30_qiarchive/` | documentation about QiArchive |
> | Google Drive QiArchive | actual archive/storage folders |
> | `repo/docs/20_qinexus/` | documentation about QiNexus |
> | Google Drive QiNexus | actual working storage system |
> | Wiki.js | readable published KB/manual |
> | QiAccess | front door / launcher / control panel |
> 
> ## Codex needs this rule
> 
> Add this to both prompts:
> 
> ```text
> Important storage/documentation distinction:
> 
> The repo `docs/` folder contains knowledge base articles, tool documentation, runbooks, standards, architecture notes, and Wiki.js-ready markdown.
> 
> The actual operational folders for QiArchive/QiNexus live on Google Drive. Do not treat `docs/30_qiarchive/` or `docs/20_qinexus/` as the real storage/archive folders. They are documentation about those systems.
> 
> When documenting paths, clearly distinguish:
> - repo documentation paths
> - server runtime paths
> - Google Drive storage/archive paths
> - Wiki.js published page paths
> 
> Do not move, rename, or reorganize real Google Drive archive folders unless explicitly instructed.
> ```
> 
> That distinction is critical. Otherwise Codex will try to “fix” the documentation tree like it’s the actual archive, and then we’re back in folder soup with a helmet on.

### User
> but the docs are the target folder hiearchies or the goal organization

### Assistant
> Yes — **that’s the sharper version**.
> 
> The repo `docs/` tree is not the live storage itself, but it **does define the target hierarchy / goal organization** for the real Google Drive systems.
> 
> So the model is:
> 
> | Layer | What it is | What it does |
> |---|---|---|
> | `c:\QiLabs\_QiAccess_Start\docs` | KB + doctrine + target maps | Defines how QiNexus/QiArchive/QiServer/QiApps should be organized |
> | Google Drive QiNexus/QiArchive | real operational storage | Holds the actual files, records, evidence, PDFs, exports, assets |
> | Wiki.js | published readable manual | Lets you browse/use the docs without living in the repo |
> | QiAccess | front door | Launches tools, services, docs, folders, workflows |
> 
> So yes:
> 
> `docs/20_qinexus/` = the **target/ideal QiNexus folder model**  
> Google Drive QiNexus = the **actual working folder system**
> 
> `docs/30_qiarchive/` = the **target/ideal QiArchive pipeline model**  
> Google Drive QiArchive = the **actual archive and ingestion storage**
> 
> The uploaded tree confirms the repo docs already mirror the intended operating structure: `20_qinexus` contains the root bucket model, and `30_qiarchive` contains ingestion, extraction, chunking, embeddings, graphs, retrieval, memory, and backup stages. fileciteturn1file0
> 
> ## Better rule
> 
> Use this wording for Codex:
> 
> ```text
> Important distinction:
> 
> The repo docs tree is the documentation and target hierarchy model for the system. It describes the intended organization of QiNexus, QiArchive, QiServer, QiApps, and related workflows.
> 
> The real operational folders live on Google Drive, the server, or inside app/service runtime paths.
> 
> Do not treat repo docs folders as the actual storage folders. Treat them as:
> 1. documentation,
> 2. target hierarchy,
> 3. governance map,
> 4. Wiki.js source content,
> 5. implementation guide.
> 
> When comparing docs to reality, check whether the real Google Drive/server/app folders match the target hierarchy described in docs. Do not change real folders unless explicitly instructed.
> ```
> 
> That’s the core idea:
> 
> **Docs are the blueprint. Drive/server are the building. Wiki.js is the visitor center. QiAccess is the front door.**

### User
> codex is still busy so lets do what we can on our own in the ide or server terminal

### Assistant
> Good. While Codex is chewing, we can do the safe prep work: inspect, inventory, and draft docs without touching deployment. No need to wait on the goblins.

### Assistant
> Yes. Do the **non-destructive prep work** now. We should avoid anything that conflicts with Codex while it’s still busy.
> 
> ## Safe work we can do right now
> 
> ### Lane A — IDE work on PC
> 
> Use the IDE AI to inspect and draft, not commit/deploy.
> 
> Give it this:
> 
> ```text
> You are helping inside c:\QiLabs\_QiAccess_Start.
> 
> Do not deploy.
> Do not push.
> Do not rename folders.
> Do not delete anything.
> Do not create a new docs architecture.
> 
> The repo docs tree already exists and is the target hierarchy / goal organization for the system. The real operational folders live on Google Drive, qiserver, or app runtime paths. Treat repo docs as documentation, target maps, governance, and Wiki.js source content.
> 
> Your task is inspection and drafting only.
> 
> Inspect the current docs tree and identify:
> 
> 1. Active doctrine docs
> 2. Tool/service KB docs
> 3. QiAccess Start-specific docs
> 4. QiServer docs
> 5. QiArchive pipeline docs
> 6. QiNexus target hierarchy docs
> 7. Homepage/gethomepage inherited docs
> 8. Superseded/legacy docs
> 9. Empty placeholder folders
> 10. Missing obvious docs
> 
> Pay special attention to these existing zones:
> 
> - docs/10_qicore/
> - docs/20_qinexus/
> - docs/30_qiarchive/
> - docs/40_qisystem/
> - docs/50_qiserver/
> - docs/60_qiapps/
> - docs/70_qiconnect/
> - docs/notes/
> 
> Do not create docs/06_workflows. Use the existing target hierarchy.
> 
> Draft, but do not necessarily save unless safe:
> 
> - docs/30_qiarchive/10_ingestion/qiingest_pipeline.md
> - docs/30_qiarchive/10_ingestion/file_inventory_scanner.md
> - docs/30_qiarchive/10_ingestion/routing_approval_flow.md
> - docs/50_qiserver/qiserver_runbook.md
> - docs/60_qiapps/qiaccess_start/overview.md
> - docs/60_qiapps/qiaccess_start/wiki_publish_plan.md
> - docs/40_qisystem/50_generated_reports/current_project_state.md
> 
> For each draft, include:
> 
> - verified facts
> - target hierarchy
> - actual runtime/storage location if known
> - unknowns
> - needs Cody confirmation
> - Wiki.js-ready summary
> - implementation notes
> 
> Final output:
> - files inspected
> - docs that already exist
> - docs that are missing
> - suggested files to create
> - suggested files to update
> - anything that may conflict with Codex
> ```
> 
> This gives us value without stepping on Codex’s toes.
> 
> ---
> 
> ## Lane B — Server terminal inspection only
> 
> On the server, do **read-only inspection**. No pull. No restart. No deploy while Codex is running.
> 
> Run this in terminal:
> 
> ```bash
> hostname
> whoami
> pwd
> 
> echo "=== QIOS ROOTS ==="
> ls -lah /srv || true
> ls -lah /srv/qios || true
> ls -lah /srv/qios/apps || true
> ls -lah /srv/qios/stacks || true
> ls -lah /srv/qios/docs || true
> 
> echo "=== FIND QIACCESS DIRS ==="
> find /srv/qios /home/qiadmin -maxdepth 5 -type d \( -iname "*qiaccess*" -o -iname "*_QiAccess_Start*" -o -iname "*access*" \) 2>/dev/null
> 
> echo "=== GIT REPOS UNDER /srv/qios ==="
> find /srv/qios -maxdepth 5 -type d -name ".git" 2>/dev/null | sed 's|/.git||'
> 
> echo "=== DOCKER CONTAINERS ==="
> docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"
> 
> echo "=== STACK DIRECTORIES ==="
> find /srv/qios/stacks -maxdepth 3 -type f \( -name "docker-compose.yml" -o -name "compose.yml" -o -name ".env" \) 2>/dev/null | sort
> 
> echo "=== LISTENING PORTS ==="
> ss -tulpn | grep LISTEN || true
> 
> echo "=== TAILSCALE STATUS ==="
> tailscale status 2>/dev/null || true
> 
> echo "=== TAILSCALE SERVE STATUS ==="
> tailscale serve status 2>/dev/null || true
> ```
> 
> That will give us the real server map.
> 
> ---
> 
> ## Lane C — If you find the repo path on server
> 
> Only after the inspection shows the correct repo path, run this **inside that repo**:
> 
> ```bash
> pwd
> git rev-parse --show-toplevel
> git remote -v
> git branch --show-current
> git status --short
> ls -lah
> ls -lah docs | head -50
> ```
> 
> Do **not** run `git pull` yet if Codex is still busy.
> 
> We only want facts.
> 
> ---
> 
> ## Lane D — Build the current-state report manually
> 
> Create or draft this file in IDE:
> 
> `docs/40_qisystem/50_generated_reports/current_project_state.md`
> 
> Use this structure:
> 
> ```markdown
> # Current Project State
> 
> ## Status
> 
> QiAccess Start is deployed and working.
> 
> ## Known Local Repo
> 
> - Path: `c:\QiLabs\_QiAccess_Start`
> - Docs path: `c:\QiLabs\_QiAccess_Start\docs`
> 
> ## Docs Role
> 
> The repo docs tree is the KB, doctrine, and target hierarchy model.
> 
> It describes the intended organization for QiCore, QiNexus, QiArchive, QiSystem, QiServer, QiApps, and QiConnect.
> 
> The real operational folders live on Google Drive, qiserver, and app/service runtime paths.
> 
> ## Major Docs Zones
> 
> - `docs/10_qicore/` — governance, structure, data, services, operations, knowledge, assets
> - `docs/20_qinexus/` — target QiNexus workspace/storage model
> - `docs/30_qiarchive/` — target ingestion, extraction, chunking, embeddings, graphs, retrieval, memory, sync/backup model
> - `docs/40_qisystem/` — logs, audits, backups, health checks, generated reports, generated indexes, maintenance
> - `docs/50_qiserver/` — qiserver runtime/runbook docs
> - `docs/60_qiapps/` — app-specific docs
> - `docs/70_qiconnect/` — connection/fleet docs
> 
> ## Immediate Work
> 
> 1. Finish Wiki.js publishing plan.
> 2. Verify qiserver repo path and deployment method.
> 3. Confirm service inventory.
> 4. Draft QiIngest pipeline docs.
> 5. Prepare file inventory scanner plan.
> 6. Keep Mom’s Care bare minimum.
> 
> ## QiIngest Direction
> 
> QiIngest should become the intake/index/routing pipeline:
> 
> 1. watch folders
> 2. hash files
> 3. detect duplicates
> 4. maintain inventory
> 5. import to Paperless
> 6. extract OCR/text
> 7. propose metadata/filename/routing
> 8. create approval queue
> 9. update routing rules from Cody corrections
> 10. embed into Qdrant
> 11. optionally map relationships in Neo4j
> 12. support future GINA recall
> 
> ## Unknowns
> 
> - Actual deployed qiserver repo path
> - Actual deployment method
> - Which docs are already published to Wiki.js
> - Which services are active vs parked
> - Actual Google Drive QiArchive/QiNexus folder match against target docs
> ```
> 
> That’s a safe, useful artifact.
> 
> ---
> 
> ## Lane E — QiIngest Phase 1 doc
> 
> Create/draft:
> 
> `docs/30_qiarchive/10_ingestion/file_inventory_scanner.md`
> 
> Skeleton:
> 
> ```markdown
> # File Inventory Scanner
> 
> ## Purpose
> 
> The File Inventory Scanner is Phase 1 of QiIngest.
> 
> Its job is to answer: what files exist, where are they, and have they changed?
> 
> ## Scope
> 
> Phase 1 is inventory only.
> 
> It does not move, rename, delete, or modify source files.
> 
> ## Watched Sources
> 
> Potential sources:
> 
> - Google Drive QiNexus
> - Google Drive QiArchive
> - local intake folders
> - Paperless consume folder
> - manual upload folders
> 
> ## Captured Metadata
> 
> - file path
> - filename
> - extension
> - size
> - created timestamp
> - modified timestamp
> - SHA256 hash
> - source root
> - detected duplicate group
> - inventory scan timestamp
> - status
> - review status
> 
> ## Output
> 
> Preferred:
> 
> - SQLite database
> 
> Optional:
> 
> - CSV export
> - JSON manifest
> 
> ## Safety Rules
> 
> - read-only scan first
> - no file movement
> - no renaming
> - no deletion
> - dry-run by default
> - log every scan
> - preserve original paths
> - never trust AI classification without approval
> 
> ## Future Phases
> 
> - Paperless import tracking
> - OCR/text extraction tracking
> - metadata proposal
> - filename proposal
> - routing proposal
> - human approval
> - routing rules update
> - embeddings
> - GINA recall
> ```
> 
> ---
> 
> ## Lane F — QiIngest pipeline doc
> 
> Create/draft:
> 
> `docs/30_qiarchive/10_ingestion/qiingest_pipeline.md`
> 
> Skeleton:
> 
> ```markdown
> # QiIngest Pipeline
> 
> ## Purpose
> 
> QiIngest is the intake, indexing, routing, and review pipeline for Cody’s files.
> 
> It connects real storage folders, Paperless, metadata rules, embeddings, retrieval, and future GINA recall.
> 
> ## Operating Principle
> 
> AI may propose.
> 
> Cody approves.
> 
> The system learns only from approved corrections.
> 
> ## Pipeline Stages
> 
> ### 1. Inventory
> 
> Scan watched folders, hash files, detect duplicates, and update inventory.
> 
> ### 2. Intake
> 
> Identify files eligible for Paperless or other processing.
> 
> ### 3. Extraction
> 
> Collect OCR/text from Paperless or other extractors.
> 
> ### 4. Classification Proposal
> 
> Propose document type, entities, dates, tags, and target folder.
> 
> ### 5. Filename Proposal
> 
> Suggest normalized filenames using naming rules.
> 
> ### 6. Routing Proposal
> 
> Suggest destination based on QiNexus/QiArchive target hierarchy.
> 
> ### 7. Review Queue
> 
> Cody approves, edits, or rejects proposals.
> 
> ### 8. Rule Update
> 
> Approved corrections update routing, naming, tagging, and entity rules.
> 
> ### 9. Indexing
> 
> Approved/extracted content is embedded into Qdrant and optionally mapped into Neo4j.
> 
> ### 10. Recall
> 
> GINA retrieves from approved inventory, metadata, embeddings, and relationship maps.
> 
> ## Hard Boundaries
> 
> - no autonomous deletion
> - no autonomous overwriting
> - no silent folder restructuring
> - no AI-only routing for sensitive files
> - no treating docs folders as live storage folders
> ```
> 
> ---
> 
> ## What not to do while Codex is busy
> 
> Do **not**:
> 
> - run `git pull`
> - run `git push`
> - restart containers
> - edit the same files Codex may be editing
> - rename folders
> - move Google Drive folders
> - publish to Wiki.js yet
> - create another docs structure
> - start building the whole ingestion app tonight like a raccoon with a soldering iron
> 
> The safest win is: **inspect, draft, inventory, report.**
> 
> Your docs tree already has the target architecture: `10_qicore`, `20_qinexus`, `30_qiarchive`, `40_qisystem`, `50_qiserver`, and `60_qiapps` are present in the current structure. fileciteturn1file0 So we are not starting over. We are making the existing blueprint executable.

### Assistant
> Good. This server inspection gave us a **real map**, not vibes. Here’s the signal.
> 
> ## Confirmed server reality
> 
> ### Server identity
> 
> - Hostname: `qiserver`
> - User: `qiadmin`
> - Home: `/home/qiadmin`
> - Runbook exists at `/srv/qios/docs/000_RUN_ME_FIRST.md`
> - Tailscale UI base: `https://qiserver-1.cerberus-sirius.ts.net` fileciteturn2file0
> 
> ### Important paths
> 
> You have **three QiAccess-related locations**:
> 
> | Path | Meaning |
> |---|---|
> | `/srv/qios/apps/_QiAccess_Start` | likely deployed app repo |
> | `/srv/qios/repos/_QiAccess_Start` | likely repo/source copy |
> | `/srv/qios/stacks/_qiaccess_start` | Docker Compose/runtime stack |
> 
> That is the thing to be careful with. We need to know which one is canonical for deployment. Do **not** let Codex blindly edit all three like a caffeinated raccoon.
> 
> ### Active Docker service for QiAccess
> 
> Container:
> 
> `homepage`
> 
> Image:
> 
> `ghcr.io/gethomepage/homepage:latest`
> 
> Port:
> 
> `127.0.0.1:3001 -> 3000`
> 
> Tailscale serves it at:
> 
> `https://qiserver-1.cerberus-sirius.ts.net`
> 
> That confirms QiAccess Start is currently powered by Homepage/gethomepage, not a custom React/Vite app runtime at the server level. fileciteturn2file0
> 
> ## Current active services
> 
> Confirmed running:
> 
> | Service | Local Port | Tailscale |
> |---|---:|---|
> | QiAccess/Homepage | `127.0.0.1:3001` | base URL |
> | Wiki.js | `127.0.0.1:3002` | `:9448` |
> | Paperless | `127.0.0.1:8010` | `:9447` |
> | n8n | `127.0.0.1:5678` | `:9450` |
> | Qdrant | `127.0.0.1:6333` | `:9452` |
> | Open WebUI | `127.0.0.1:3000` | `:9446` |
> | Uptime Kuma | `127.0.0.1:3005` | `:9451` |
> | SolidTime | `127.0.0.1:8095` | `:9453` |
> | DailyWave frontend | `127.0.0.1:3020` | `:9454` |
> | DailyWave backend | `127.0.0.1:8020` | `:9455` |
> | NocoDB | `127.0.0.1:8088` | `:8443` |
> | Portainer | `127.0.0.1:9443` | `:9449` |
> | BookStack | `127.0.0.1:6875` | `:6875` |
> | Firefly III | `127.0.0.1:6877` | `:6877` |
> | Firefly importer | `127.0.0.1:6878` | `:6878` |
> | Neo4j | `127.0.0.1:7474` | `:7474` |
> | Ollama | `127.0.0.1:11434` | `:11434` |
> | QiTTS API | `127.0.0.1:8890` | not shown in Tailscale serve |
> | QiTranscribe | restarting/broken | not stable |
> 
> QiTranscribe is the one ugly little blinking light: `qitranscribe-whisper-webui` is restarting. That gets logged as **broken/needs inspection**, not a blocker for QiAccess.
> 
> ## What this means
> 
> ### 1. QiAccess is not just “an app”
> 
> On server, QiAccess is currently:
> 
> - gethomepage container
> - stack at `/srv/qios/stacks/_qiaccess_start`
> - likely config/docs/source in `/srv/qios/apps/_QiAccess_Start`
> - possible source mirror in `/srv/qios/repos/_QiAccess_Start`
> 
> So deployment probably depends on the stack config, not just “npm build and restart.” Important.
> 
> ### 2. The docs need to record three path types
> 
> For every workflow, Codex needs to distinguish:
> 
> | Type | Example |
> |---|---|
> | repo/source path | `/srv/qios/repos/_QiAccess_Start` |
> | deployed app path | `/srv/qios/apps/_QiAccess_Start` |
> | stack/runtime path | `/srv/qios/stacks/_qiaccess_start` |
> 
> No more “the repo” as a vague noun. That’s where toes get stepped on.
> 
> ---
> 
> # Next safe server commands
> 
> Run these next. Still read-only except `cd`.
> 
> ## Inspect both QiAccess repos
> 
> ```bash
> echo "=== APPS COPY ==="
> cd /srv/qios/apps/_QiAccess_Start && \
> pwd && \
> git rev-parse --show-toplevel && \
> git remote -v && \
> git branch --show-current && \
> git status --short && \
> echo "--- top level ---" && \
> ls -lah && \
> echo "--- docs sample ---" && \
> find docs -maxdepth 2 -type d | sort | head -80
> 
> echo "=== REPOS COPY ==="
> cd /srv/qios/repos/_QiAccess_Start && \
> pwd && \
> git rev-parse --show-toplevel && \
> git remote -v && \
> git branch --show-current && \
> git status --short && \
> echo "--- top level ---" && \
> ls -lah && \
> echo "--- docs sample ---" && \
> find docs -maxdepth 2 -type d | sort | head -80
> ```
> 
> ## Compare the two copies
> 
> ```bash
> echo "=== COMPARE GIT HEADS ==="
> cd /srv/qios/apps/_QiAccess_Start && echo "apps HEAD:  $(git rev-parse --short HEAD) $(git log -1 --pretty=%s)"
> cd /srv/qios/repos/_QiAccess_Start && echo "repos HEAD: $(git rev-parse --short HEAD) $(git log -1 --pretty=%s)"
> 
> echo "=== COMPARE REMOTES ==="
> cd /srv/qios/apps/_QiAccess_Start && echo "apps remote:" && git remote -v
> cd /srv/qios/repos/_QiAccess_Start && echo "repos remote:" && git remote -v
> ```
> 
> ## Inspect QiAccess stack
> 
> ```bash
> echo "=== QIACCESS STACK ==="
> cd /srv/qios/stacks/_qiaccess_start && \
> pwd && \
> ls -lah && \
> echo "--- compose ---" && \
> sed -n '1,220p' docker-compose.yml
> ```
> 
> ## Inspect Homepage config mounts
> 
> ```bash
> echo "=== HOMEPAGE CONTAINER INSPECT MOUNTS ==="
> docker inspect homepage --format '{{range .Mounts}}{{println .Source "->" .Destination}}{{end}}'
> 
> echo "=== HOMEPAGE CONTAINER LABELS ==="
> docker inspect homepage --format '{{json .Config.Labels}}' | python3 -m json.tool 2>/dev/null || true
> ```
> 
> This will tell us where the live Homepage config is actually coming from.
> 
> ---
> 
> # What to tell Codex now
> 
> Give server Codex this shorter updated instruction:
> 
> ```text
> Codex, server inspection confirmed these QiAccess-related paths:
> 
> - /srv/qios/apps/_QiAccess_Start
> - /srv/qios/repos/_QiAccess_Start
> - /srv/qios/stacks/_qiaccess_start
> 
> Do not assume which is canonical.
> 
> QiAccess Start currently appears to run as the `homepage` container from image `ghcr.io/gethomepage/homepage:latest`, listening on `127.0.0.1:3001->3000`, served by Tailscale at `https://qiserver-1.cerberus-sirius.ts.net`.
> 
> Your next task is read-only verification unless explicitly told otherwise:
> 
> 1. Inspect Git state of both:
>    - /srv/qios/apps/_QiAccess_Start
>    - /srv/qios/repos/_QiAccess_Start
> 
> 2. Compare:
>    - remotes
>    - branches
>    - HEAD commits
>    - working tree status
>    - docs structure
> 
> 3. Inspect:
>    - /srv/qios/stacks/_qiaccess_start/docker-compose.yml
>    - homepage container mounts
>    - live config paths
> 
> 4. Determine which path is:
>    - source repo
>    - deployed app/config path
>    - runtime stack path
> 
> 5. Do not git pull.
> 6. Do not restart.
> 7. Do not deploy.
> 8. Do not clone.
> 9. Do not edit files.
> 
> Final report should identify:
> - canonical source path if knowable
> - deployed/live config path
> - runtime stack path
> - whether apps and repos copies are duplicates or intentionally separate
> - whether either working tree is dirty
> - what should be updated by PC Codex versus Server Codex
> - safest next action
> ```
> 
> ## My call
> 
> The likely clean model should become:
> 
> - `/srv/qios/repos/_QiAccess_Start` = source mirror / maybe retire if duplicate
> - `/srv/qios/apps/_QiAccess_Start` = live app/config repo
> - `/srv/qios/stacks/_qiaccess_start` = Docker stack
> 
> But don’t act on that yet. Verify. Because right now there are two repo copies, and duplicate repo copies are exactly how systems start wearing clown shoes.

### Assistant
> Perfect. This clarified the server setup a lot.
> 
> ## What we now know for real
> 
> ### 1. Live QiAccess is the stack, not the app repo
> 
> The live Homepage/QiAccess runtime is here:
> 
> `/srv/qios/stacks/_qiaccess_start`
> 
> And the actual live config is mounted from:
> 
> - `/srv/qios/stacks/_qiaccess_start/config -> /app/config`
> - `/srv/qios/stacks/_qiaccess_start/public -> /app/public`
> - `/srv/qios/stacks/_qiaccess_start/config/images -> /app/public/images`
> 
> The running container is `homepage`, using Docker Compose project `qiaccess_start`, with config file:
> 
> `/srv/qios/stacks/_qiaccess_start/docker-compose.yml` fileciteturn3file0
> 
> So: **editing `/srv/qios/apps/_QiAccess_Start` does not automatically change the live page** unless there is a sync/build/deploy step that copies stuff into the stack config. That’s the landmine.
> 
> ## 2. There are two repo copies
> 
> You have:
> 
> | Path | Remote | Status |
> |---|---|---|
> | `/srv/qios/apps/_QiAccess_Start` | `git@github.com-qidocs:qiallyme/_QiAccess_Start.git` | clean from shown output |
> | `/srv/qios/repos/_QiAccess_Start` | `git@github.com:qiallyme/_QiAccess_Start.git` | dirty: `.gitignore` modified |
> 
> The remotes are **different SSH aliases**:
> 
> - `github.com-qidocs`
> - `github.com`
> 
> That matters. The `apps` copy is likely the one using the deploy key/config that finally worked. The `repos` copy has a modified `.gitignore` and may be older/local working clutter. fileciteturn3file0
> 
> ## 3. Docs exist in both copies
> 
> Both server repo copies have the expected docs structure:
> 
> - `docs/10_qicore`
> - `docs/20_qinexus`
> - `docs/30_qiarchive`
> - `docs/40_qisystem`
> - `docs/assets`
> - `docs/configs`
> - `docs/widgets`
> - etc. fileciteturn3file0
> 
> So the local docs tree is mirrored on server, but again: that does **not** mean Wiki.js is already updated.
> 
> ---
> 
> # Correct operating model now
> 
> Use this until proven otherwise:
> 
> | Layer | Path | Role |
> |---|---|---|
> | Local PC repo | `c:\QiLabs\_QiAccess_Start` | edit/docs/source |
> | GitHub | `_QiAccess_Start` | handoff |
> | Server app repo | `/srv/qios/apps/_QiAccess_Start` | likely canonical server repo copy |
> | Server old/source copy | `/srv/qios/repos/_QiAccess_Start` | duplicate/needs reconciliation |
> | Live runtime stack | `/srv/qios/stacks/_qiaccess_start` | actual Homepage deployment |
> | Live Homepage config | `/srv/qios/stacks/_qiaccess_start/config` | what the dashboard actually reads |
> | Live Homepage public assets | `/srv/qios/stacks/_qiaccess_start/public` | mounted public assets |
> 
> The spicy truth: **the app repo and the live dashboard config are separate right now.** That’s fine, but it must be documented or we will absolutely step on rakes.
> 
> ---
> 
> # Next safe commands
> 
> Run this next to inspect the live Homepage config. This is the important one.
> 
> ```bash
> cd /srv/qios/stacks/_qiaccess_start
> 
> echo "=== LIVE HOMEPAGE CONFIG FILES ==="
> find config -maxdepth 3 -type f | sort
> 
> echo "=== LIVE HOMEPAGE PUBLIC FILES ==="
> find public -maxdepth 3 -type f | sort | head -100
> 
> echo "=== CONFIG TOP LEVEL ==="
> ls -lah config
> 
> echo "=== SERVICES CONFIG ==="
> sed -n '1,240p' config/services.yaml 2>/dev/null || sed -n '1,240p' config/services.yml 2>/dev/null || true
> 
> echo "=== BOOKMARKS CONFIG ==="
> sed -n '1,240p' config/bookmarks.yaml 2>/dev/null || sed -n '1,240p' config/bookmarks.yml 2>/dev/null || true
> 
> echo "=== SETTINGS CONFIG ==="
> sed -n '1,220p' config/settings.yaml 2>/dev/null || sed -n '1,220p' config/settings.yml 2>/dev/null || true
> 
> echo "=== WIDGETS CONFIG ==="
> sed -n '1,220p' config/widgets.yaml 2>/dev/null || sed -n '1,220p' config/widgets.yml 2>/dev/null || true
> ```
> 
> This tells us what QiAccess is actually showing.
> 
> ---
> 
> # Then check whether repo has matching config
> 
> Run:
> 
> ```bash
> echo "=== APP REPO HOMEPAGE CONFIG CANDIDATES ==="
> cd /srv/qios/apps/_QiAccess_Start
> find . -maxdepth 5 -type f \( -name "services.yaml" -o -name "services.yml" -o -name "bookmarks.yaml" -o -name "bookmarks.yml" -o -name "settings.yaml" -o -name "settings.yml" -o -name "widgets.yaml" -o -name "widgets.yml" \) | sort
> 
> echo "=== STACK CONFIG VS REPO CONFIG POSSIBLE MATCHES ==="
> find . -maxdepth 5 -type d \( -name "config" -o -name "configs" \) | sort
> ```
> 
> We need to know if the live config is tracked in the repo or only lives in the stack folder.
> 
> ---
> 
> # What to tell Server Codex now
> 
> Use this:
> 
> ```text
> Codex, updated server inspection confirms:
> 
> Live QiAccess/Homepage runtime:
> - Stack path: /srv/qios/stacks/_qiaccess_start
> - Compose file: /srv/qios/stacks/_qiaccess_start/docker-compose.yml
> - Container: homepage
> - Image: ghcr.io/gethomepage/homepage:latest
> - Local port: 127.0.0.1:3001 -> 3000
> - Tailscale base URL: https://qiserver-1.cerberus-sirius.ts.net
> 
> Live mounted config:
> - /srv/qios/stacks/_qiaccess_start/config -> /app/config
> - /srv/qios/stacks/_qiaccess_start/public -> /app/public
> - /srv/qios/stacks/_qiaccess_start/config/images -> /app/public/images
> 
> Repo copies:
> - /srv/qios/apps/_QiAccess_Start
>   - remote: git@github.com-qidocs:qiallyme/_QiAccess_Start.git
>   - branch: main
>   - appears clean in latest output
> - /srv/qios/repos/_QiAccess_Start
>   - remote: git@github.com:qiallyme/_QiAccess_Start.git
>   - branch: main
>   - dirty: .gitignore modified
> 
> Do not assume editing either repo changes the live dashboard. The live dashboard reads from the stack config folder unless a deploy/sync script says otherwise.
> 
> Next task is read-only inspection:
> 
> 1. Inspect /srv/qios/stacks/_qiaccess_start/config and public.
> 2. List live Homepage config files.
> 3. Determine whether live config is tracked in /srv/qios/apps/_QiAccess_Start.
> 4. Find any sync/deploy scripts that copy repo files into the stack config.
> 5. Determine the safest canonical flow:
>    - PC repo edit
>    - GitHub push
>    - server apps repo pull
>    - sync/build/copy into /srv/qios/stacks/_qiaccess_start/config if needed
>    - docker compose restart only if needed
> 
> Do not git pull.
> Do not restart.
> Do not deploy.
> Do not edit.
> Do not touch /srv/qios/repos/_QiAccess_Start except to inspect, because it has a dirty .gitignore and may be duplicate/legacy.
> 
> Final report should say:
> - live config files found
> - whether they are tracked in the app repo
> - whether a sync script exists
> - whether /srv/qios/repos/_QiAccess_Start can be archived/ignored later
> - what the safe update path should be
> ```
> 
> ---
> 
> # My current recommendation
> 
> ## Canonical server source should probably be:
> 
> `/srv/qios/apps/_QiAccess_Start`
> 
> Because:
> 
> - it uses the `github.com-qidocs` SSH alias that you fixed
> - it appears clean
> - it is under `/apps`, which matches deployed app ownership
> - `/repos` has a dirty `.gitignore`
> 
> ## Runtime stays:
> 
> `/srv/qios/stacks/_qiaccess_start`
> 
> Because Docker Compose is there and live Homepage config is mounted from there.
> 
> ## Later cleanup
> 
> Do **not** delete this now, but eventually:
> 
> `/srv/qios/repos/_QiAccess_Start`
> 
> should probably become one of:
> 
> - archived
> - removed
> - documented as legacy
> - converted into a read-only mirror
> 
> Right now it is duplicate confusion bait. Cute? No. Dangerous? Mildly. Annoying? Deeply.
> 
> ---
> 
> # The key doctrine to write down
> 
> Put this in the server runbook:
> 
> ```md
> ## QiAccess Deployment Reality
> 
> QiAccess Start is currently served by the Homepage container.
> 
> The live runtime is controlled by:
> 
> - `/srv/qios/stacks/_qiaccess_start/docker-compose.yml`
> - `/srv/qios/stacks/_qiaccess_start/config/`
> - `/srv/qios/stacks/_qiaccess_start/public/`
> 
> The repo copy at `/srv/qios/apps/_QiAccess_Start` contains source/docs and may be the canonical server repo, but changes there do not affect the live dashboard unless copied/synced into the stack config or otherwise deployed.
> 
> Do not edit `/srv/qios/repos/_QiAccess_Start` for active deployment unless its role is re-confirmed. It appears to be a duplicate or older source copy and currently has a modified `.gitignore`.
> 
> Safe update sequence:
> 
> 1. Edit locally on PC.
> 2. Commit and push to GitHub.
> 3. Pull on server into `/srv/qios/apps/_QiAccess_Start`.
> 4. Sync relevant Homepage config/assets into `/srv/qios/stacks/_qiaccess_start/config` or `/public` if needed.
> 5. Restart Homepage only if required.
> 6. Verify `https://qiserver-1.cerberus-sirius.ts.net`.
> ```
> 
> This is the kind of boring rule that prevents future Cody from yelling at present Cody. Which, frankly, is a civic service.

### Assistant
> Excellent. This is the missing deployment truth.
> 
> ## Confirmed: live config is duplicated but trackable
> 
> The **live Homepage config** lives at:
> 
> `/srv/qios/stacks/_qiaccess_start/config`
> 
> It contains the real active files:
> 
> - `bookmarks.yaml`
> - `services.yaml`
> - `settings.yaml`
> - `widgets.yaml`
> - `custom.css`
> - `custom.js`
> - images/assets
> - backup copies of prior configs fileciteturn4file0
> 
> The **repo copy** contains matching config candidates at:
> 
> `/srv/qios/apps/_QiAccess_Start/qiaccess/config/`
> 
> with:
> 
> - `bookmarks.yaml`
> - `services.yaml`
> - `settings.yaml`
> - `widgets.yaml`
> 
> It also has skeleton versions at:
> 
> `/srv/qios/apps/_QiAccess_Start/src/skeleton/` fileciteturn4file0
> 
> So the model is now clear:
> 
> | Layer | Path | Role |
> |---|---|---|
> | Live config | `/srv/qios/stacks/_qiaccess_start/config` | What Homepage actually uses |
> | Repo canonical config candidate | `/srv/qios/apps/_QiAccess_Start/qiaccess/config` | What should probably be tracked in Git |
> | Skeleton defaults | `/srv/qios/apps/_QiAccess_Start/src/skeleton` | Template/defaults, not live |
> | Stack runtime | `/srv/qios/stacks/_qiaccess_start` | Docker Compose runtime |
> 
> ## The landmine
> 
> The live config and repo config may not be identical.
> 
> Before anyone edits anything, compare them:
> 
> ```bash
> cd /srv/qios
> 
> echo "=== COMPARE LIVE VS REPO HOMEPAGE CONFIG ==="
> diff -u stacks/_qiaccess_start/config/services.yaml apps/_QiAccess_Start/qiaccess/config/services.yaml || true
> diff -u stacks/_qiaccess_start/config/bookmarks.yaml apps/_QiAccess_Start/qiaccess/config/bookmarks.yaml || true
> diff -u stacks/_qiaccess_start/config/settings.yaml apps/_QiAccess_Start/qiaccess/config/settings.yaml || true
> diff -u stacks/_qiaccess_start/config/widgets.yaml apps/_QiAccess_Start/qiaccess/config/widgets.yaml || true
> ```
> 
> If the live config has newer changes, copy it **back into the repo config** before Codex/PC changes overwrite it.
> 
> ## Safe sync direction
> 
> For now:
> 
> ### When the dashboard is edited live on server
> 
> Sync:
> 
> `/srv/qios/stacks/_qiaccess_start/config/*.yaml`
> 
> back to:
> 
> `/srv/qios/apps/_QiAccess_Start/qiaccess/config/*.yaml`
> 
> Then commit/push from the app repo if clean.
> 
> ### When the dashboard is edited on PC
> 
> Flow is:
> 
> 1. Edit local PC repo.
> 2. Push to GitHub.
> 3. Pull on server into `/srv/qios/apps/_QiAccess_Start`.
> 4. Copy/sync from:
> 
>    `/srv/qios/apps/_QiAccess_Start/qiaccess/config/`
> 
>    to:
> 
>    `/srv/qios/stacks/_qiaccess_start/config/`
> 
> 5. Restart Homepage only if needed.
> 
> ## Create a tiny deploy/sync script later
> 
> Not now while things are moving, but the final version should have a script like:
> 
> `scripts/sync_homepage_config_to_stack.sh`
> 
> Purpose:
> 
> - back up live stack config
> - copy repo `qiaccess/config/*.yaml` to stack config
> - copy repo assets if needed
> - validate YAML if possible
> - restart homepage container or `docker compose up -d`
> - show status
> 
> This prevents manual copy chaos.
> 
> ## What to tell Codex now
> 
> Give Codex this:
> 
> ```text
> Codex, latest inspection confirmed the live Homepage config and repo config relationship.
> 
> Live runtime:
> - /srv/qios/stacks/_qiaccess_start/docker-compose.yml
> - /srv/qios/stacks/_qiaccess_start/config/
> - /srv/qios/stacks/_qiaccess_start/public/
> 
> Live config files:
> - config/services.yaml
> - config/bookmarks.yaml
> - config/settings.yaml
> - config/widgets.yaml
> - config/custom.css
> - config/custom.js
> 
> Repo config candidates:
> - /srv/qios/apps/_QiAccess_Start/qiaccess/config/services.yaml
> - /srv/qios/apps/_QiAccess_Start/qiaccess/config/bookmarks.yaml
> - /srv/qios/apps/_QiAccess_Start/qiaccess/config/settings.yaml
> - /srv/qios/apps/_QiAccess_Start/qiaccess/config/widgets.yaml
> 
> Skeleton defaults also exist:
> - /srv/qios/apps/_QiAccess_Start/src/skeleton/
> 
> Do not treat skeleton files as live config.
> 
> Next task:
> Compare live config against repo config using diff. Do not overwrite either side until differences are reviewed.
> 
> Determine whether live config has newer manual edits. If so, propose syncing live config back into repo config first.
> 
> Then document the canonical deployment flow:
> 
> PC repo edit -> GitHub push -> server apps repo pull -> sync qiaccess/config into /srv/qios/stacks/_qiaccess_start/config -> restart Homepage if needed -> verify Tailscale URL.
> 
> Do not touch /srv/qios/repos/_QiAccess_Start except for read-only inspection. It appears duplicate/legacy and has a dirty .gitignore.
> 
> Add this deployment reality to:
> - docs/50_qiserver/qiserver_runbook.md
> - docs/60_qiapps/qiaccess_start/overview.md
> - docs/40_qisystem/50_generated_reports/current_project_state.md
> 
> If those docs do not exist, create them in the existing docs hierarchy.
> ```
> 
> ## What the live dashboard currently contains
> 
> The service layout is actually not bad. It already has:
> 
> - Core Services
> - Workflows
> - Knowledge
> - Admin
> - Attention
> 
> And it includes the important stack pieces: Open WebUI, Paperless, Firefly, DailyWave, NocoDB, n8n, SolidTime, Wiki.js, Neo4j, Qdrant, Uptime Kuma, Portainer, Cockpit, Cloudflare, Firefly Importer, QI Transcribe, and FamilyWall. fileciteturn4file0
> 
> So we are not rebuilding the dashboard. We are doing the boring-but-critical thing:
> 
> **make the repo config, live config, docs, and deployment process line up.**
> 
> That is the next win.

### Assistant
> Yep. This diff confirms the exact problem:
> 
> ## The repo config is **newer/design-forward**, but the live config is **real-working**
> 
> The live stack config has the actual usable Tailscale URLs and current working service layout. The repo config has prettier/future-state organization, but it still contains placeholder URLs like:
> 
> - `paperless.placeholder.qially.internal`
> - `nocodb.placeholder.qially.internal`
> - `docs.placeholder.qially.internal`
> - `firefly.placeholder.qially.internal`
> 
> So **do not sync repo config → live config right now**. That would break the dashboard links. The live config is the one currently safe for function. fileciteturn5file0
> 
> ## What the diff tells us
> 
> ### Live config has real links
> 
> Live `services.yaml` includes real Tailscale service links for:
> 
> - Open WebUI
> - Paperless
> - Firefly III
> - DailyWave
> - NocoDB
> - n8n
> - SolidTime
> - BookStack
> - Wiki.js
> - Neo4j
> - Qdrant
> - Uptime Kuma
> - Portainer
> - Cockpit
> - Firefly Importer
> - FamilyWall
> 
> That’s the working production-ish config.
> 
> ### Repo config has better structure but fake links
> 
> Repo `qiaccess/config/services.yaml` has better sections:
> 
> - QiAccess
> - Core Services
> - Knowledge + Archive
> - Finance + Admin
> - Automation
> - Server Control
> - Recovery
> 
> But it uses placeholders. So it is not deployable yet.
> 
> ### Settings differ too
> 
> Live settings are simpler:
> 
> - `color: zinc`
> - `headerStyle: clean`
> - `bookmarksStyle: icons`
> - DuckDuckGo search
> 
> Repo settings are more styled:
> 
> - `color: slate`
> - `headerStyle: boxedWidgets`
> - `iconStyle: theme`
> - `statusStyle: dot`
> - `fullWidth: true`
> - Google quicklaunch
> - richer layout groups
> 
> That might be visually better, but again: don’t deploy it blindly.
> 
> ---
> 
> # Correct next action
> 
> We need to make the **repo config become deployable** by merging:
> 
> **live URLs + repo structure**
> 
> Not:
> 
> **repo placeholders over live working links**
> 
> ## Safe merge rule
> 
> Use repo config as the **layout/design target**.
> 
> Use live config as the **truth source for real URLs**.
> 
> So the final repo `qiaccess/config/services.yaml` should keep the nicer categories but replace all placeholders with the real Tailscale links from the live stack.
> 
> ## Tell Codex this
> 
> ```text
> Codex, the diff confirms live config and repo config are different.
> 
> Important:
> Do NOT sync repo config into the live stack yet.
> 
> The live stack config at:
> - /srv/qios/stacks/_qiaccess_start/config/services.yaml
> - /srv/qios/stacks/_qiaccess_start/config/bookmarks.yaml
> - /srv/qios/stacks/_qiaccess_start/config/settings.yaml
> - /srv/qios/stacks/_qiaccess_start/config/widgets.yaml
> 
> contains the real currently-working service URLs.
> 
> The repo config at:
> - /srv/qios/apps/_QiAccess_Start/qiaccess/config/services.yaml
> - /srv/qios/apps/_QiAccess_Start/qiaccess/config/bookmarks.yaml
> - /srv/qios/apps/_QiAccess_Start/qiaccess/config/settings.yaml
> - /srv/qios/apps/_QiAccess_Start/qiaccess/config/widgets.yaml
> 
> contains better future-state organization and styling, but many placeholder URLs.
> 
> Task:
> Create a safe merged repo config.
> 
> Use:
> - live config as the source of truth for real service URLs
> - repo config as the source of truth for improved grouping/layout/styling where useful
> 
> Do not touch live stack config yet.
> 
> Update only the repo config first:
> - /srv/qios/apps/_QiAccess_Start/qiaccess/config/services.yaml
> - /srv/qios/apps/_QiAccess_Start/qiaccess/config/bookmarks.yaml
> - /srv/qios/apps/_QiAccess_Start/qiaccess/config/settings.yaml
> - /srv/qios/apps/_QiAccess_Start/qiaccess/config/widgets.yaml
> 
> Rules:
> - Replace placeholder URLs with real Tailscale/service URLs from live config.
> - Preserve useful repo grouping if it does not reduce clarity.
> - Keep QI Transcribe in an Attention or Recovery section because it is currently restarting/broken.
> - Keep admin tools clearly separated from regular workflow tools.
> - Do not expose secrets.
> - Do not add API tokens.
> - Do not edit /srv/qios/stacks/_qiaccess_start/config yet.
> - After updating repo config, show a diff.
> - Do not deploy until Cody reviews.
> 
> Also document:
> - live config is currently authoritative for working URLs
> - repo config should become canonical after merge
> - deployment requires syncing repo qiaccess/config into stack config after review
> ```
> 
> ## My recommended final dashboard grouping
> 
> Use this grouping. It’s clean and operational:
> 
> ### QiAccess
> 
> - QiAccess Home
> - Wiki.js
> - current project state / docs link later
> 
> ### Core Services
> 
> - Open WebUI
> - Paperless
> - NocoDB
> - DailyWave
> 
> ### Knowledge + Archive
> 
> - Wiki.js
> - BookStack
> - Qdrant
> - Neo4j
> 
> ### Finance + Time
> 
> - Firefly III
> - Firefly Importer
> - SolidTime
> 
> ### Automation
> 
> - n8n
> - Uptime Kuma
> - QiTTS
> - maybe QiTranscribe when fixed
> 
> ### Server Control
> 
> - Portainer
> - Cockpit
> - Cloudflare
> - Tailscale Admin
> 
> ### Attention
> 
> - QiTranscribe — restarting
> - anything broken or unstable
> - anything using placeholders
> 
> ### External / Mobile
> 
> - Google Drive
> - Gmail
> - Google Calendar
> - FamilyWall
> - GitHub
> - ChatGPT
> - NotebookLM
> 
> That’s the right blend: not too many categories, not a junk drawer.
> 
> ## Bottom line
> 
> We found the answer:
> 
> **Live config works. Repo config is prettier but not safe yet.**
> 
> Next move:
> 
> **merge real URLs into repo config, review, then sync repo config to live stack.**
> 
> No deploy until the merged repo config has zero placeholder links unless intentionally marked.

### User
> is this prompt for codex server or pc

### Assistant
> That prompt is for **Codex Server**.
> 
> Because it references server paths:
> 
> - `/srv/qios/stacks/_qiaccess_start/config/...`
> - `/srv/qios/apps/_QiAccess_Start/qiaccess/config/...`
> - live stack config
> - Tailscale URLs
> - not touching live deployment yet
> 
> So give it to **Codex running on qiserver**.
> 
> The job is:
> 
> **Server Codex compares live config vs server repo config, then safely updates the server repo config only — not the live stack yet.**
> 
> Do **not** give that exact prompt to PC Codex unless you rewrite the paths to local Windows paths.
> 
> For PC Codex, the equivalent would be:
> 
> ```text
> Codex, you are working on Cody’s local PC repo at:
> 
> c:\QiLabs\_QiAccess_Start
> 
> Do not deploy.
> Do not touch qiserver.
> Do not assume the local config is currently live.
> 
> Server inspection showed that live QiAccess/Homepage config on qiserver is currently different from the repo config. The live server config has real working Tailscale URLs. The repo config has better future-state grouping/styling but contains placeholder URLs.
> 
> Your job on PC is to prepare the repo-side canonical config and docs, not deploy.
> 
> Work only in:
> 
> c:\QiLabs\_QiAccess_Start\qiaccess\config\
> 
> Review/update:
> 
> - services.yaml
> - bookmarks.yaml
> - settings.yaml
> - widgets.yaml
> 
> Goal:
> Make the repo config deployment-ready by replacing placeholders with the real service URLs discovered from qiserver notes, while preserving useful improved grouping/layout.
> 
> Rules:
> - Do not use placeholder URLs unless intentionally marked.
> - Do not add secrets or API tokens.
> - Do not touch live server paths.
> - Do not claim the dashboard is updated until Server Codex syncs it.
> - Document that deployment requires server pull + sync into /srv/qios/stacks/_qiaccess_start/config.
> 
> Also update docs if present:
> - docs/50_qiserver/qiserver_runbook.md
> - docs/60_qiapps/qiaccess_start/overview.md
> - docs/40_qisystem/50_generated_reports/current_project_state.md
> 
> Final report:
> - files changed
> - placeholders removed
> - remaining unknowns
> - whether server pull/sync is required
> ```
> 
> Clean split:
> 
> **Server Codex:** compare and merge using actual server files.  
> **PC Codex:** prepare local repo/docs so GitHub becomes canonical.  
> **Nobody touches live stack config until we review the merged config.**

### User
> • Updated locally only. No deploy, no qiserver changes, no claim that live Homepage is

>   updated.

> 

>   Files changed:

> 

>   - /C:/QiLabs/_QiAccess_Start/qiaccess/config/services.yaml

>   - /C:/QiLabs/_QiAccess_Start/qiaccess/config/bookmarks.yaml

>   - /C:/QiLabs/_QiAccess_Start/qiaccess/config/settings.yaml

>   - /C:/QiLabs/_QiAccess_Start/qiaccess/config/widgets.yaml

>   - /C:/QiLabs/_QiAccess_Start/docs/50_qiserver/qiserver_runbook.md

>   - /C:/QiLabs/_QiAccess_Start/docs/60_qiapps/qiaccess_start/overview.md

>   - /C:/QiLabs/_QiAccess_Start/docs/40_qisystem/50_generated_reports/

>     current_project_state.md

> 

>   What changed in config:

> 

>   - Replaced placeholder service URLs with repo-supported private routes for:

>       - Open WebUI 9446

>       - Paperless 9447

>       - Wiki.js 9448

>       - Portainer 9449

>       - n8n 9450

>       - Uptime Kuma 9451

>       - Qdrant 9452

>       - NocoDB 8443

>       - Cockpit 100.121.111.106:9090

>   - Added the private Homepage launcher root https://qiserver-1.cerberus-sirius.ts.net/.

>   - Replaced bookmark placeholders for Family Wall, Documentation / QiCore, and Recovery

>     notes.

>   - Removed placeholder href values for unconfirmed entries instead of faking them:

>       - Firefly III

>       - SolidTime

>       - Finance portals

>       - Care/admin links

>   - Added explicit comments in all four config files that repo edits are not live until

>     Server Codex pulls and syncs them into /srv/qios/stacks/_qiaccess_start/config/.

> 

>   Validation:

> 

>   - All four YAML files parsed successfully.

> 

>   Remaining unknowns:

> 

>   - Confirmed private URL for Firefly III

>   - Confirmed private URL for SolidTime

>   - Whether Neo4j should stay visible in Homepage while repo notes still mark 7474

>     offline

>   - Whether recovery/doc links should stay GitHub-backed or later move to stable Wiki.js

>     targets

> 

>   Server pull/sync required:

> 

>   - Yes.

>   - Required later step is server-side pull plus sync into:

>       - /srv/qios/stacks/_qiaccess_start/config/services.yaml

>       - /srv/qios/stacks/_qiaccess_start/config/bookmarks.yaml

>       - /srv/qios/stacks/_qiaccess_start/config/settings.yaml

>       - /srv/qios/stacks/_qiaccess_start/config/widgets.yaml

> 

>   Current local git note:

> 

>   - The four qiaccess/config/*.yaml files are tracked modifications.

>   - The three updated docs are in local untracked docs paths that already existed in

>     your worktree, so they are not committed or pushed by this pass.

> 

> ─ Worked for 4m 10s ────────────────────────────────────────────────────────────────────

> 

> 

> › Implement {feature}

### Assistant
> Good. PC Codex behaved correctly: **local only, no fake deployment claim, YAML validated.** That’s the discipline we want.
> 
> But there are a few corrections because PC Codex is missing facts we already verified from qiserver.
> 
> ## Corrections to feed back
> 
> These are **not unknown anymore**:
> 
> | Item | Confirmed server URL |
> |---|---|
> | Firefly III | `http://qiserver-1.cerberus-sirius.ts.net:6877` |
> | Firefly Importer | `http://qiserver-1.cerberus-sirius.ts.net:6878` |
> | SolidTime | `https://qiserver-1.cerberus-sirius.ts.net:9453` |
> | Neo4j | `http://qiserver-1.cerberus-sirius.ts.net:7474` |
> 
> Those were confirmed in the running Docker/Tailscale output and live Homepage config. fileciteturn3file0 fileciteturn4file0
> 
> So PC Codex should do one more local pass before anything is pushed/synced.
> 
> ## Give PC Codex this next
> 
> ```text
> Codex, correction pass.
> 
> You are still on the local PC repo:
> 
> c:\QiLabs\_QiAccess_Start
> 
> Do not deploy.
> Do not touch qiserver.
> Do not claim live Homepage changed.
> 
> Update the local repo config and docs using these confirmed qiserver URLs:
> 
> - Firefly III: http://qiserver-1.cerberus-sirius.ts.net:6877
> - Firefly Importer: http://qiserver-1.cerberus-sirius.ts.net:6878
> - SolidTime: https://qiserver-1.cerberus-sirius.ts.net:9453
> - Neo4j: http://qiserver-1.cerberus-sirius.ts.net:7474
> 
> These are no longer unknowns.
> 
> Tasks:
> 
> 1. Update qiaccess/config/services.yaml:
>    - restore/add Firefly III with confirmed URL
>    - restore/add Firefly Importer with confirmed URL
>    - restore/add SolidTime with confirmed URL
>    - keep Neo4j visible with confirmed URL unless there is a current local doc saying it must be hidden
>    - keep QiTranscribe in Attention because server inspection showed it restarting
> 
> 2. Update bookmarks.yaml only if needed:
>    - do not use fake placeholder URLs
>    - keep GitHub, Cloudflare, Tailscale, Google Drive, Gmail, Calendar, ChatGPT, NotebookLM, FamilyWall if real URLs are known
>    - leave finance/care portals out if not confirmed
> 
> 3. Update docs:
>    - docs/50_qiserver/qiserver_runbook.md
>    - docs/60_qiapps/qiaccess_start/overview.md
>    - docs/40_qisystem/50_generated_reports/current_project_state.md
> 
> 4. Since those three docs are untracked but intentional, stage them if they are in the correct existing docs hierarchy.
> 
> 5. Validate YAML again.
> 
> 6. Show:
>    - git status --short
>    - files changed
>    - any remaining placeholders
>    - any remaining unknown URLs
>    - suggested commit message
> 
> Do not push unless explicitly told.
> ```
> 
> ## After that
> 
> Once PC Codex finishes correction pass, the order is:
> 
> 1. Review `git status --short`.
> 2. Commit locally.
> 3. Push to GitHub.
> 4. Server Codex pulls into `/srv/qios/apps/_QiAccess_Start`.
> 5. Server Codex syncs only the approved config files into `/srv/qios/stacks/_qiaccess_start/config/`.
> 6. Restart Homepage if needed.
> 7. Verify `https://qiserver-1.cerberus-sirius.ts.net`.
> 
> Do **not** answer Codex’s `Implement {feature}` prompt. That’s generic bait. We are not adding a random feature. We are doing **correction pass → commit → server pull/sync**.

### User
> i gave the command to the ide cause we have exaugested codex for the day, do you want to give me a workflow or adr or documentation on this now.

### Assistant
> Yes. Do **both**: one ADR plus one workflow doc. ADR locks the decision. Workflow makes it executable.
> 
> Use these two files:
> 
> 1. `docs/10_qicore/10_governance/50_decisions/ADR-0012_qiaccess_homepage_config_deployment_flow.md`
> 2. `docs/50_qiserver/qiaccess_homepage_config_sync_workflow.md`
> 
> ---
> 
> # ADR-0012 — QiAccess Homepage Config Deployment Flow
> 
> Save as:
> 
> `docs/10_qicore/10_governance/50_decisions/ADR-0012_qiaccess_homepage_config_deployment_flow.md`
> 
> ```md
> # ADR-0012 — QiAccess Homepage Config Deployment Flow
> 
> ## Status
> 
> Accepted
> 
> ## Date
> 
> 2026-05-26
> 
> ## Context
> 
> QiAccess Start is currently served by the Homepage container on qiserver.
> 
> The live runtime is controlled by the Docker Compose stack at:
> 
> - `/srv/qios/stacks/_qiaccess_start/docker-compose.yml`
> 
> The live Homepage configuration is mounted from:
> 
> - `/srv/qios/stacks/_qiaccess_start/config/`
> - `/srv/qios/stacks/_qiaccess_start/public/`
> 
> The server also contains a repo copy at:
> 
> - `/srv/qios/apps/_QiAccess_Start`
> 
> The repo contains Homepage config candidates at:
> 
> - `/srv/qios/apps/_QiAccess_Start/qiaccess/config/services.yaml`
> - `/srv/qios/apps/_QiAccess_Start/qiaccess/config/bookmarks.yaml`
> - `/srv/qios/apps/_QiAccess_Start/qiaccess/config/settings.yaml`
> - `/srv/qios/apps/_QiAccess_Start/qiaccess/config/widgets.yaml`
> 
> The local PC repo lives at:
> 
> - `c:\QiLabs\_QiAccess_Start`
> 
> A second server repo copy also exists at:
> 
> - `/srv/qios/repos/_QiAccess_Start`
> 
> This second copy is not currently treated as the active deployment source because it has a different Git remote alias and showed a dirty `.gitignore`.
> 
> ## Decision
> 
> The canonical edit flow for QiAccess Homepage configuration is:
> 
> 1. Edit config/docs locally in `c:\QiLabs\_QiAccess_Start`.
> 2. Commit and push to GitHub.
> 3. Pull changes on qiserver into `/srv/qios/apps/_QiAccess_Start`.
> 4. Sync approved config files from:
> 
>    `/srv/qios/apps/_QiAccess_Start/qiaccess/config/`
> 
>    into:
> 
>    `/srv/qios/stacks/_qiaccess_start/config/`
> 
> 5. Restart or reload the Homepage stack only if needed.
> 6. Verify the live dashboard at:
> 
>    `https://qiserver-1.cerberus-sirius.ts.net`
> 
> The live stack config remains the runtime truth until repo config is reviewed and synced.
> 
> The repo config is the intended canonical source after review.
> 
> ## Rules
> 
> - Do not edit the live stack config casually.
> - Do not overwrite live config from repo config if repo config contains placeholder URLs.
> - Do not treat `src/skeleton/` config files as live config.
> - Do not deploy from `/srv/qios/repos/_QiAccess_Start` unless its role is re-confirmed.
> - Do not assume local repo changes are live until server pull and sync occur.
> - Do not assume server repo changes are reflected locally unless pushed back to GitHub.
> - Do not add secrets, tokens, passwords, or private API keys to tracked config.
> - Do not create duplicate QiAccess folders.
> - If paths are uncertain, inspect before acting.
> 
> ## Confirmed Runtime Facts
> 
> QiAccess Start is currently powered by Homepage/gethomepage.
> 
> The live container is:
> 
> - container: `homepage`
> - image: `ghcr.io/gethomepage/homepage:latest`
> - port: `127.0.0.1:3001 -> 3000`
> - Tailscale URL: `https://qiserver-1.cerberus-sirius.ts.net`
> 
> Confirmed live mounted config paths:
> 
> - `/srv/qios/stacks/_qiaccess_start/config -> /app/config`
> - `/srv/qios/stacks/_qiaccess_start/public -> /app/public`
> - `/srv/qios/stacks/_qiaccess_start/config/images -> /app/public/images`
> 
> ## Config Source Roles
> 
> | Path | Role |
> |---|---|
> | `c:\QiLabs\_QiAccess_Start\qiaccess\config` | Local editable repo config |
> | `/srv/qios/apps/_QiAccess_Start/qiaccess/config` | Server repo config after GitHub pull |
> | `/srv/qios/stacks/_qiaccess_start/config` | Live Homepage runtime config |
> | `/srv/qios/apps/_QiAccess_Start/src/skeleton` | Defaults/templates only |
> | `/srv/qios/repos/_QiAccess_Start` | Duplicate/legacy candidate, not active deployment source |
> 
> ## Consequences
> 
> This creates a safe separation between:
> 
> - local editing,
> - version control,
> - server source,
> - live runtime config,
> - deployment/sync.
> 
> It prevents accidental overwrites of working live config and avoids treating multiple server repo copies as interchangeable.
> 
> ## Future Improvement
> 
> Create a controlled sync script:
> 
> - `scripts/sync_homepage_config_to_stack.sh`
> 
> The script should:
> 
> 1. verify it is running on qiserver,
> 2. verify repo path,
> 3. verify stack path,
> 4. back up live config,
> 5. validate YAML,
> 6. copy approved config files,
> 7. restart Homepage only if needed,
> 8. verify container status,
> 9. print the live URL.
> ```
> 
> ---
> 
> # QiAccess Homepage Config Sync Workflow
> 
> Save as:
> 
> `docs/50_qiserver/qiaccess_homepage_config_sync_workflow.md`
> 
> ```md
> # QiAccess Homepage Config Sync Workflow
> 
> ## Purpose
> 
> This workflow defines how QiAccess Homepage config changes move from local repo edits to the live qiserver dashboard.
> 
> It prevents accidental overwrites, duplicate repo confusion, and broken Homepage links.
> 
> ## Current Deployment Reality
> 
> QiAccess Start is currently served by Homepage/gethomepage.
> 
> Live stack:
> 
> - `/srv/qios/stacks/_qiaccess_start`
> 
> Live Docker Compose file:
> 
> - `/srv/qios/stacks/_qiaccess_start/docker-compose.yml`
> 
> Live mounted config:
> 
> - `/srv/qios/stacks/_qiaccess_start/config/`
> 
> Live mounted public assets:
> 
> - `/srv/qios/stacks/_qiaccess_start/public/`
> 
> Server repo copy:
> 
> - `/srv/qios/apps/_QiAccess_Start`
> 
> Local PC repo:
> 
> - `c:\QiLabs\_QiAccess_Start`
> 
> ## Workflow Summary
> 
> ```text
> PC repo edit
> → commit
> → push to GitHub
> → server pulls into /srv/qios/apps/_QiAccess_Start
> → reviewed config syncs into /srv/qios/stacks/_qiaccess_start/config
> → Homepage restarts if needed
> → live URL is verified
> ```
> 
> ## Step 1 — Local PC Edit
> 
> Edit tracked config files locally:
> 
> - `qiaccess/config/services.yaml`
> - `qiaccess/config/bookmarks.yaml`
> - `qiaccess/config/settings.yaml`
> - `qiaccess/config/widgets.yaml`
> 
> Optional docs to update:
> 
> - `docs/50_qiserver/qiserver_runbook.md`
> - `docs/60_qiapps/qiaccess_start/overview.md`
> - `docs/40_qisystem/50_generated_reports/current_project_state.md`
> 
> ## Step 2 — Local Validation
> 
> Before commit:
> 
> ```bash
> git status --short
> ```
> 
> Validate YAML using available tooling.
> 
> Required checks:
> 
> - no fake placeholder URLs unless intentionally marked,
> - no secrets,
> - no API tokens,
> - no passwords,
> - no broken YAML,
> - no accidental edits to skeleton files,
> - no claim that live Homepage changed.
> 
> ## Step 3 — Commit and Push
> 
> Commit local changes after review.
> 
> Suggested commit format:
> 
> ```text
> docs/config: align QiAccess Homepage config deployment flow
> ```
> 
> Push to GitHub.
> 
> ## Step 4 — Server Pull
> 
> On qiserver, use the active app repo:
> 
> ```bash
> cd /srv/qios/apps/_QiAccess_Start
> git status --short
> git pull
> ```
> 
> Do not use `/srv/qios/repos/_QiAccess_Start` unless its role has been re-confirmed.
> 
> ## Step 5 — Compare Repo Config to Live Config
> 
> Before syncing, compare:
> 
> ```bash
> cd /srv/qios
> 
> diff -u stacks/_qiaccess_start/config/services.yaml apps/_QiAccess_Start/qiaccess/config/services.yaml || true
> diff -u stacks/_qiaccess_start/config/bookmarks.yaml apps/_QiAccess_Start/qiaccess/config/bookmarks.yaml || true
> diff -u stacks/_qiaccess_start/config/settings.yaml apps/_QiAccess_Start/qiaccess/config/settings.yaml || true
> diff -u stacks/_qiaccess_start/config/widgets.yaml apps/_QiAccess_Start/qiaccess/config/widgets.yaml || true
> ```
> 
> Review the diff before copying.
> 
> ## Step 6 — Back Up Live Config
> 
> Before overwriting live config:
> 
> ```bash
> cd /srv/qios/stacks/_qiaccess_start
> 
> STAMP="$(date +%Y%m%d_%H%M%S)"
> mkdir -p backups/config_$STAMP
> 
> cp config/services.yaml backups/config_$STAMP/services.yaml
> cp config/bookmarks.yaml backups/config_$STAMP/bookmarks.yaml
> cp config/settings.yaml backups/config_$STAMP/settings.yaml
> cp config/widgets.yaml backups/config_$STAMP/widgets.yaml
> ```
> 
> ## Step 7 — Sync Approved Config
> 
> Only after review:
> 
> ```bash
> cd /srv/qios
> 
> cp apps/_QiAccess_Start/qiaccess/config/services.yaml stacks/_qiaccess_start/config/services.yaml
> cp apps/_QiAccess_Start/qiaccess/config/bookmarks.yaml stacks/_qiaccess_start/config/bookmarks.yaml
> cp apps/_QiAccess_Start/qiaccess/config/settings.yaml stacks/_qiaccess_start/config/settings.yaml
> cp apps/_QiAccess_Start/qiaccess/config/widgets.yaml stacks/_qiaccess_start/config/widgets.yaml
> ```
> 
> ## Step 8 — Restart Homepage If Needed
> 
> Homepage often reads config dynamically, but restart if changes do not appear or if layout/settings changed.
> 
> ```bash
> cd /srv/qios/stacks/_qiaccess_start
> docker compose up -d
> ```
> 
> Then verify:
> 
> ```bash
> docker ps --filter "name=homepage"
> docker logs --tail=80 homepage
> ```
> 
> ## Step 9 — Verify Live Dashboard
> 
> Open:
> 
> ```text
> https://qiserver-1.cerberus-sirius.ts.net
> ```
> 
> Check:
> 
> - dashboard loads,
> - service cards appear,
> - links open correctly,
> - no placeholders are visible,
> - broken services remain in Attention/Recovery,
> - admin services are clearly separated.
> 
> ## Known Confirmed Service URLs
> 
> | Service | URL |
> |---|---|
> | QiAccess/Homepage | `https://qiserver-1.cerberus-sirius.ts.net` |
> | Open WebUI | `https://qiserver-1.cerberus-sirius.ts.net:9446` |
> | Paperless | `https://qiserver-1.cerberus-sirius.ts.net:9447` |
> | Wiki.js | `https://qiserver-1.cerberus-sirius.ts.net:9448` |
> | Portainer | `https://qiserver-1.cerberus-sirius.ts.net:9449` |
> | n8n | `https://qiserver-1.cerberus-sirius.ts.net:9450` |
> | Uptime Kuma | `https://qiserver-1.cerberus-sirius.ts.net:9451` |
> | Qdrant | `https://qiserver-1.cerberus-sirius.ts.net:9452/dashboard` |
> | SolidTime | `https://qiserver-1.cerberus-sirius.ts.net:9453` |
> | DailyWave frontend | `https://qiserver-1.cerberus-sirius.ts.net:9454` |
> | DailyWave backend | `https://qiserver-1.cerberus-sirius.ts.net:9455` |
> | NocoDB | `https://qiserver-1.cerberus-sirius.ts.net:8443` |
> | BookStack | `http://qiserver-1.cerberus-sirius.ts.net:6875` |
> | Firefly III | `http://qiserver-1.cerberus-sirius.ts.net:6877` |
> | Firefly Importer | `http://qiserver-1.cerberus-sirius.ts.net:6878` |
> | Neo4j Browser | `http://qiserver-1.cerberus-sirius.ts.net:7474` |
> | Ollama | `http://qiserver-1.cerberus-sirius.ts.net:11434` |
> | Cockpit | `https://qiserver-1.cerberus-sirius.ts.net:9090` |
> 
> ## Current Caution Items
> 
> ### QiTranscribe
> 
> QiTranscribe was observed restarting.
> 
> Keep it in Attention/Recovery until fixed.
> 
> ### Duplicate Server Repo
> 
> `/srv/qios/repos/_QiAccess_Start` exists but is not treated as active deployment source.
> 
> Do not use it for deployment unless re-confirmed.
> 
> ### Skeleton Config
> 
> `src/skeleton/*.yaml` files are defaults/templates.
> 
> Do not treat them as live config.
> 
> ## Rollback
> 
> If the dashboard breaks after sync:
> 
> ```bash
> cd /srv/qios/stacks/_qiaccess_start
> 
> ls backups
> 
> cp backups/config_YYYYMMDD_HHMMSS/services.yaml config/services.yaml
> cp backups/config_YYYYMMDD_HHMMSS/bookmarks.yaml config/bookmarks.yaml
> cp backups/config_YYYYMMDD_HHMMSS/settings.yaml config/settings.yaml
> cp backups/config_YYYYMMDD_HHMMSS/widgets.yaml config/widgets.yaml
> 
> docker compose up -d
> ```
> 
> Verify:
> 
> ```text
> https://qiserver-1.cerberus-sirius.ts.net
> ```
> 
> ## Hard Rule
> 
> The repo config can be canonical only after it is reviewed, pulled, synced, and verified live.
> 
> Until then, the live stack config is runtime truth.
> ```
> 
> ---
> 
> ## Add this tiny note to `current_project_state.md`
> 
> ```md
> ## QiAccess Config Deployment State
> 
> QiAccess Homepage config is currently split between repo config and live stack config.
> 
> The live stack config is runtime truth:
> 
> - `/srv/qios/stacks/_qiaccess_start/config/`
> 
> The repo config is the intended canonical source after review:
> 
> - `qiaccess/config/`
> 
> The safe deployment flow is:
> 
> 1. edit local repo,
> 2. push to GitHub,
> 3. pull on qiserver into `/srv/qios/apps/_QiAccess_Start`,
> 4. compare repo config against live config,
> 5. back up live config,
> 6. sync approved config into stack config,
> 7. restart Homepage only if needed,
> 8. verify Tailscale URL.
> 
> Do not sync placeholder repo config into the live stack.
> ```
> 
> This is the boring little seatbelt that keeps us from launching ourselves through the windshield.
