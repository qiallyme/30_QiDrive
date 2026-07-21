---
layout: page
title: "Paperless Docker Setup"
slug: "paperless_docker_setup"
created_at: "2026-05-08 05:25:00"
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
source_file: "Chat-Export-28513-2026/conversations-006.json"
template_key: master-template
date: 2026-05-08
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69fdb9df-055c-83ea-8801-efa91ac5c89e"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Paperless Docker Setup

## Overview
- **Date**: 2026-05-08 05:25:00
- **Conversation ID**: `69fdb9df-055c-83ea-8801-efa91ac5c89e`
- **Source**: `Chat-Export-28513-2026/conversations-006.json`

## Chat History

### User
> ok, i am installing paperless on docker on my local pc, we need to get the server actually working correctly so we can start vectorizing and graphing all intake.

### Assistant
> Yes. The move is: get Paperless stable locally first, then treat it as the intake/extraction layer feeding QiArchive—not as the final source of truth. We’re not building a cathedral today; we’re getting the spine breathing.

### Assistant
> Yes — and here’s the clean strategy:
> 
> **Paperless = intake/OCR/document staging.**  
> **QiArchive = canonical registration spine.**  
> **pgvector/Neo4j = derived retrieval + graph.**
> 
> Do **not** let Paperless become the truth source. That would violate your own blueprint: canonical file identity belongs to QiArchive, while vector and graph layers are derived, non-authoritative outputs. Your blueprint already says filesystem + registry/database are truth, while vector and graph are downstream derived layers. fileciteturn0file0
> 
> Paperless official docs say Docker Compose is the normal setup path, with an installation script available, and config values can live in `docker-compose.env`. The important one is `PAPERLESS_SECRET_KEY`; `PAPERLESS_URL` matters if exposing it beyond localhost. citeturn550992search5turn550992search1turn550992search3
> 
> ## Do this first: make local Paperless stable
> 
> Use this local folder layout on Windows:
> 
> Actual folders:
> 
> C:\QiData\paperless\consume  
> C:\QiData\paperless\data  
> C:\QiData\paperless\media  
> C:\QiData\paperless\export  
> C:\QiData\paperless\trash  
> 
> Then your QiOS intake folders stay separate:
> 
> C:\QiData\inbox  
> C:\QiData\processing  
> C:\QiData\reviewed  
> C:\QiData\failed  
> C:\QiData\extracted_text  
> C:\QiData\embeddings_cache  
> C:\QiData\logs  
> 
> This is the line: **Paperless can touch `C:\QiData\paperless\*`; QiArchive owns `C:\QiData\inbox` and beyond.**
> 
> ## Minimal Docker Compose for local Paperless
> 
> Create:
> 
> `C:\QiData\paperless\docker-compose.yml`
> 
> ```yaml
> services:
>   broker:
>     image: docker.io/library/redis:7
>     restart: unless-stopped
>     volumes:
>       - redisdata:/data
> 
>   db:
>     image: docker.io/library/postgres:16
>     restart: unless-stopped
>     volumes:
>       - pgdata:/var/lib/postgresql/data
>     environment:
>       POSTGRES_DB: paperless
>       POSTGRES_USER: paperless
>       POSTGRES_PASSWORD: paperless_local_change_me
> 
>   webserver:
>     image: ghcr.io/paperless-ngx/paperless-ngx:latest
>     restart: unless-stopped
>     depends_on:
>       - db
>       - broker
>     ports:
>       - "8001:8000"
>     volumes:
>       - ./data:/usr/src/paperless/data
>       - ./media:/usr/src/paperless/media
>       - ./export:/usr/src/paperless/export
>       - ./consume:/usr/src/paperless/consume
>       - ./trash:/usr/src/paperless/trash
>     env_file: docker-compose.env
>     environment:
>       PAPERLESS_REDIS: redis://broker:6379
>       PAPERLESS_DBHOST: db
> 
> volumes:
>   pgdata:
>   redisdata:
> ```
> 
> Create:
> 
> `C:\QiData\paperless\docker-compose.env`
> 
> ```env
> PAPERLESS_SECRET_KEY=replace_this_with_a_real_random_secret
> PAPERLESS_TIME_ZONE=America/Chicago
> PAPERLESS_OCR_LANGUAGE=eng
> PAPERLESS_FILENAME_FORMAT={created_year}/{correspondent}/{title}
> PAPERLESS_CONSUMER_POLLING=30
> PAPERLESS_CONSUMER_RECURSIVE=true
> PAPERLESS_TRASH_DIR=/usr/src/paperless/trash
> ```
> 
> Generate the secret key with:
> 
> ```powershell
> python -c "import secrets; print(secrets.token_urlsafe(64))"
> ```
> 
> Then start it:
> 
> ```powershell
> cd C:\QiData\paperless
> docker compose up -d
> ```
> 
> Check containers:
> 
> ```powershell
> docker compose ps
> ```
> 
> Watch logs:
> 
> ```powershell
> docker compose logs -f webserver
> ```
> 
> Open:
> 
> ```text
> http://localhost:8001
> ```
> 
> Create superuser:
> 
> ```powershell
> docker compose exec webserver python manage.py createsuperuser
> ```
> 
> ## Then test intake
> 
> Drop one simple PDF here:
> 
> ```text
> C:\QiData\paperless\consume
> ```
> 
> Then check logs:
> 
> ```powershell
> docker compose logs -f webserver
> ```
> 
> If it imports, Paperless is working.
> 
> ## The correct QiOS integration path
> 
> Phase 1 — **Paperless standalone works**
> 
> Paperless consumes files, OCRs, stores searchable docs.
> 
> Phase 2 — **QiArchive watches exports/originals**
> 
> Do not directly mutate Paperless DB yet. Instead, QiArchive should read either:
> 
> `C:\QiData\paperless\export`
> 
> or, better for now:
> 
> `C:\QiData\paperless\media\documents\originals`
> 
> Then QiArchive registers the file into:
> 
> `qiarchive.archive_files`  
> `qiarchive.archive_chunks`  
> `qiarchive.ingest_jobs`  
> `qigraph.master_index`
> 
> Your blueprint already has this exact pipeline: detect → register → extract → chunk → embed → index → route/review. fileciteturn0file0
> 
> Phase 3 — **Vectorize**
> 
> After QiArchive has `archive_id`, chunks get embedded into pgvector. This matters because embeddings must reference stable `archive_id` / `chunk_id`. Otherwise you get AI soup. Pretty soup, but soup.
> 
> Phase 4 — **Graph**
> 
> Only after registration + extraction + entity detection do we project into Neo4j/qigraph. Graph does **not** invent truth. It references canonical archive records.
> 
> ## Immediate health checklist
> 
> Run these after setup:
> 
> ```powershell
> cd C:\QiData\paperless
> docker compose ps
> ```
> 
> You want all services up.
> 
> ```powershell
> docker compose logs --tail=100 webserver
> ```
> 
> You want no DB connection errors, no Redis errors, no permission errors.
> 
> ```powershell
> docker compose exec webserver python manage.py check
> ```
> 
> You want no critical Django errors.
> 
> ```powershell
> docker compose exec db psql -U paperless -d paperless -c "\dt"
> ```
> 
> You want tables returned.
> 
> ## The thing not to overbuild yet
> 
> Do **not** start with Neo4j.
> 
> Order is:
> 
> 1. Paperless imports correctly.
> 2. Files land predictably.
> 3. QiArchive registers file identity.
> 4. Text extraction/chunking works.
> 5. Embeddings store with `archive_id`.
> 6. Search returns evidence.
> 7. Then graph.
> 
> Graph before identity is just a conspiracy board with better branding. Useful later. Dangerous now.
> 
> ## Codex / IDE instruction to wire this cleanly
> 
> Use this as the task prompt:
> 
> Create a local Paperless-ngx Docker setup under `C:\QiData\paperless` using Docker Compose. It must include Postgres, Redis, and the Paperless webserver. Use port `8001:8000`. Store Paperless folders as local bind mounts: `consume`, `data`, `media`, `export`, and `trash`.
> 
> Then add a QiArchive integration note/script scaffold that treats Paperless as a non-canonical intake/OCR layer. QiArchive must not write directly to the Paperless database. QiArchive should scan Paperless exported/original documents, register each file into the QiArchive pipeline, assign canonical identity, calculate checksum, preserve source path, and prepare extracted text/chunks for embedding.
> 
> Do not create graph projection yet. Stop at: Paperless working, file discovery working, registration scaffold working, and clear README instructions.
> 
> ## Today’s win condition
> 
> By the end of this setup, all we need is:
> 
> **Drop file into Paperless consume → Paperless imports it → QiArchive can see the imported/original file path → ready for registration.**
> 
> That’s it. That is the spine starting to breathe.

### User
> ok apparentlyt his is qiserver i wonder if the information is true. https://qiserver-1.cerberus-sirius.ts.net/

### Assistant
> That URL **looks like your Tailscale HTTPS name for qiserver**, yes:
> 
> `qiserver-1.cerberus-sirius.ts.net`
> 
> But I **cannot verify the page from here** — it returned a **502 Bad Gateway** when I tried to open it. That usually means one of these:
> 
> 1. **It’s private to your Tailnet**, so only devices logged into your Tailscale account can reach it.
> 2. **Tailscale Serve/Funnel is misconfigured or not running.**
> 3. **The service behind it is down**, wrong port, or bound only to `127.0.0.1` without Serve mapping.
> 4. **qiserver itself is offline/asleep/disconnected.**
> 
> On your local PC, run this:
> 
> ```powershell
> tailscale status
> ```
> 
> Look for something like:
> 
> `qiserver-1`
> 
> Then test the server directly:
> 
> ```powershell
> ping qiserver-1
> ```
> 
> Then try SSH:
> 
> ```powershell
> ssh qiadmin@qiserver-1
> ```
> 
> or:
> 
> ```powershell
> ssh qiadmin@qiserver-1.cerberus-sirius.ts.net
> ```
> 
> Once inside qiserver, check what’s actually running:
> 
> ```bash
> docker ps
> ```
> 
> Then check Tailscale Serve:
> 
> ```bash
> tailscale serve status
> ```
> 
> If that URL is supposed to show your homepage/dashboard, we need to know what port it maps to. Based on your earlier setup, Homepage was probably on:
> 
> ```text
> 127.0.0.1:3001
> ```
> 
> So the likely fix on qiserver would be something like:
> 
> ```bash
> sudo tailscale serve --bg https / http://127.0.0.1:3001
> ```
> 
> But don’t run that blindly yet. First check:
> 
> ```bash
> docker ps
> curl -I http://127.0.0.1:3001
> tailscale serve status
> ```
> 
> That tells us whether the app is alive and whether Tailscale is pointing at the right thing.

### User
> yes, it is private, you would think from the server page i would have a terminal no?

### Assistant
> You’d *think*, but no — a server page at a Tailscale URL usually only exposes **whatever web app Tailscale Serve is forwarding**. It does **not automatically give you a terminal**.
> 
> That page is probably one of these:
> 
> - **Homepage dashboard** — just links/widgets.
> - **Cockpit** — web admin panel, *can include terminal*.
> - **Portainer** — Docker admin, limited console into containers, not full host terminal.
> - **Open WebUI / app surface** — no host terminal.
> - **A blank/reverse-proxy landing page** — just forwarding weirdness.
> 
> The terminal only exists if you’re exposing a service that provides one.
> 
> ## Fastest path: SSH is still the real terminal
> 
> From your Windows PC:
> 
> ```powershell
> ssh qiadmin@qiserver-1
> ```
> 
> or:
> 
> ```powershell
> ssh qiadmin@qiserver-1.cerberus-sirius.ts.net
> ```
> 
> That is the cleanest way. Don’t overcomplicate this with browser-terminal nonsense unless SSH is annoying you.
> 
> ## If you want a browser terminal
> 
> You probably already have **Cockpit** or can install it.
> 
> Try this in your browser while on Tailnet:
> 
> ```text
> https://qiserver-1.cerberus-sirius.ts.net:9090
> ```
> 
> or:
> 
> ```text
> https://qiserver-1:9090
> ```
> 
> Cockpit often runs on port `9090`. If it loads, log in as `qiadmin`. Then look for **Terminal** in the left menu.
> 
> ## Check from SSH what web services exist
> 
> Once you SSH in, run:
> 
> ```bash
> sudo ss -tulpn | grep LISTEN
> ```
> 
> Then:
> 
> ```bash
> docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Ports}}"
> ```
> 
> And:
> 
> ```bash
> tailscale serve status
> ```
> 
> That tells us exactly what the Tailscale URL is pointing to.
> 
> ## Real answer
> 
> No, the server page does not automatically equal terminal.
> 
> For your setup, the sane admin stack is:
> 
> - **SSH** for real terminal.
> - **Cockpit** for browser-based server admin/terminal.
> - **Portainer** for Docker containers.
> - **Homepage** as the pretty front door.
> 
> So right now: use SSH first, then we can make the page link to Cockpit, Portainer, Paperless, Open WebUI, Neo4j, etc. That’s the grown-up version of “one dashboard to rule them all.”

### User
> ssh is annoying me how hard it is to have a terminal already in my server, also i have sepearte urls for the potrainer and chatbot but i forget.

### Assistant
> Not hard. SSH is annoying because it’s the raw pipe. What you want is **Cockpit** as your browser terminal + admin panel.
> 
> Your clean setup should be:
> 
> - `https://qiserver-1.cerberus-sirius.ts.net` → Homepage dashboard
> - `https://qiserver-1.cerberus-sirius.ts.net:9090` → Cockpit terminal/admin
> - Portainer URL → Docker admin
> - Chatbot URL → Open WebUI / local AI chat
> 
> ## First: try Cockpit
> 
> Open this from a device connected to Tailscale:
> 
> `https://qiserver-1.cerberus-sirius.ts.net:9090`
> 
> or:
> 
> `https://qiserver-1:9090`
> 
> If Cockpit is already installed, log in with:
> 
> User: `qiadmin`
> 
> Then look for **Terminal** in the left sidebar.
> 
> ## If Cockpit is not installed
> 
> You only need SSH one more time to install the better door. Annoying, yes. Worth it, yes.
> 
> SSH in:
> 
> ```powershell
> ssh qiadmin@qiserver-1.cerberus-sirius.ts.net
> ```
> 
> Then run:
> 
> ```bash
> sudo apt update
> sudo apt install cockpit -y
> sudo systemctl enable --now cockpit.socket
> sudo systemctl status cockpit.socket
> ```
> 
> Then open:
> 
> `https://qiserver-1.cerberus-sirius.ts.net:9090`
> 
> Boom. Browser terminal.
> 
> ## To rediscover your Portainer and chatbot URLs
> 
> SSH in once and run this:
> 
> ```bash
> docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Ports}}"
> ```
> 
> Based on your old setup, likely suspects:
> 
> - Homepage: `http://127.0.0.1:3001`
> - Open WebUI / chatbot: `http://127.0.0.1:3000`
> - Neo4j: `http://127.0.0.1:7474`
> - Portainer: maybe `https://127.0.0.1:9443` or `http://127.0.0.1:9000`
> 
> Then check what Tailscale is serving:
> 
> ```bash
> tailscale serve status
> ```
> 
> That should show mappings like:
> 
> ```text
> https://qiserver-1... /  proxy http://127.0.0.1:3001
> ```
> 
> ## If you want the dashboard to show all links
> 
> Once we know the ports, your Homepage services should include links like:
> 
> - Cockpit Terminal
> - Portainer
> - Open WebUI
> - Neo4j
> - Paperless
> - QiArchive Admin
> - QiOne Portal
> 
> That’s the right move. You shouldn’t have to remember random URLs like a goblin guarding bridge riddles.
> 
> ## The minimum next command
> 
> Run this from Windows:
> 
> ```powershell
> ssh qiadmin@qiserver-1.cerberus-sirius.ts.net
> ```
> 
> Then paste this whole block:
> 
> ```bash
> echo "=== Docker services ==="
> docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Ports}}"
> 
> echo ""
> echo "=== Listening ports ==="
> sudo ss -tulpn | grep LISTEN
> 
> echo ""
> echo "=== Tailscale serve ==="
> tailscale serve status
> 
> echo ""
> echo "=== Cockpit status ==="
> systemctl status cockpit.socket --no-pager
> ```
> 
> Send me the output, and I’ll tell you exactly which URL is which and what to add to the server homepage.

### Assistant
> Yep — that page is **absolutely your QiAccess / qiserver dashboard**. The pasted HTML says the page title is **QiAccess** and description is **“One door to Cody’s stack”** fileciteturn1file0
> 
> Here are the URLs already embedded in the dashboard:
> 
> ## Your current qiserver links
> 
> **Main dashboard / QiAccess**  
> `https://qiserver-1.cerberus-sirius.ts.net/`
> 
> **AI Chat / QiBrain**  
> `https://qiserver-1.cerberus-sirius.ts.net:9446`  
> Listed as **AI Chat — QiBrain — Digital Twin** fileciteturn1file0
> 
> **Host Admin / Cockpit terminal**  
> `https://100.121.111.106:9090`  
> Listed as **Host Admin — Cockpit (Cerberus Node)** fileciteturn1file0
> 
> **Docker Admin / Portainer**  
> `https://100.121.111.106:9443`  
> Listed as **Docker Admin — Portainer Container Mgmt** fileciteturn1file0
> 
> **Paperless / Mail Intake**  
> `https://100.121.111.106:8000`  
> Listed as **Mail Intake — Document Warehouse (Paperless)** fileciteturn1file0
> 
> **Qi Queue / Automation Control Plane**  
> `https://100.121.111.106:8001`  
> Listed as **Qi Queue — Automation Control Plane** fileciteturn1file0
> 
> ## The important part
> 
> You already have the browser terminal link. It is:
> 
> `https://100.121.111.106:9090`
> 
> That should be Cockpit. Open that while connected to Tailscale, log in as `qiadmin`, then use the **Terminal** option inside Cockpit.
> 
> Tiny warning: your dashboard is using the raw Tailscale IP for Cockpit, Portainer, Paperless, and Qi Queue, but the hostname for AI Chat. That works, but it’s messy. Later we should normalize these to cleaner names like:
> 
> `https://qiserver-1.cerberus-sirius.ts.net:9090`  
> `https://qiserver-1.cerberus-sirius.ts.net:9443`  
> `https://qiserver-1.cerberus-sirius.ts.net:8000`
> 
> But for right now? Click **Host Admin**. That is your terminal door.

### User
> ok and this is my web one, https://access.qially.com/

### Assistant
> Yep — **`https://access.qially.com/` is your public/web-facing access door**, and it’s behind **Cloudflare Access**.
> 
> I tried to open it and it redirects to a Cloudflare Access login page, which means the protection layer is active. Good. That’s exactly what we want for a private admin/control surface: public domain, gated entry. citeturn534617view0
> 
> So your two access layers are:
> 
> **Private Tailnet door**  
> `https://qiserver-1.cerberus-sirius.ts.net/`  
> Best for you/devices already on Tailscale.
> 
> **Cloudflare Zero Trust door**  
> `https://access.qially.com/`  
> Best as the polished web URL, protected by Cloudflare Access.
> 
> The current architecture is actually clean:
> 
> | Door | Purpose | Access Model |
> |---|---|---|
> | `qiserver-1.cerberus-sirius.ts.net` | Tailnet/private machine access | Tailscale only |
> | `access.qially.com` | Branded web access | Cloudflare Access login |
> | `100.121.111.106:9090` | Cockpit / browser terminal | Tailnet IP |
> | `100.121.111.106:9443` | Portainer | Tailnet IP |
> | `qiserver-1...:9446` | AI Chat | Tailnet hostname |
> 
> What I’d fix later: make the dashboard links use names instead of raw IPs wherever possible. The raw Tailscale IP works, but it’s ugly and easier to forget. The better pattern is:
> 
> `https://qiserver-1.cerberus-sirius.ts.net:9090` → Cockpit  
> `https://qiserver-1.cerberus-sirius.ts.net:9443` → Portainer  
> `https://qiserver-1.cerberus-sirius.ts.net:8000` → Paperless  
> `https://qiserver-1.cerberus-sirius.ts.net:8001` → Qi Queue  
> 
> Real talk: **you already built the front door.** The next move is not more architecture. It’s tightening the labels, links, and service routing so you don’t have to remember goblin URLs at 3 a.m.

### User
> ok so the issue is when i first start the machine i have to login to the ui before the server comes up, thats the problem. it shoudl auto start without me login into the ui.

### Assistant
> That’s a real server hygiene issue, not you being picky. A server that needs a human to log into the desktop before services start is basically a laptop cosplaying as infrastructure.

### Assistant
> Yes. The fix is to make everything run as **system services**, not as “things started by your logged-in UI session.”
> 
> Most likely one of these is true:
> 
> 1. **Docker is not enabled at boot**
> 2. **Your containers don’t have restart policies**
> 3. **Tailscale is not enabled at boot**
> 4. **Homepage/QiAccess was started manually instead of via Docker/systemd**
> 5. **If this is Windows Docker Desktop**, then yeah, Docker often waits for user login unless configured differently
> 
> Since this is `qiserver`, I’m assuming Ubuntu/Linux first.
> 
> ## On qiserver, run this in Cockpit Terminal
> 
> Open Host Admin:
> 
> `https://100.121.111.106:9090`
> 
> Then Terminal.
> 
> Run:
> 
> ```bash
> echo "=== OS ==="
> cat /etc/os-release | head
> 
> echo ""
> echo "=== Docker enabled? ==="
> systemctl is-enabled docker
> systemctl is-active docker
> 
> echo ""
> echo "=== Tailscale enabled? ==="
> systemctl is-enabled tailscaled
> systemctl is-active tailscaled
> 
> echo ""
> echo "=== Cockpit enabled? ==="
> systemctl is-enabled cockpit.socket
> systemctl is-active cockpit.socket
> 
> echo ""
> echo "=== Containers + restart policies ==="
> docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
> ```
> 
> ## Fix the boot services
> 
> Run:
> 
> ```bash
> sudo systemctl enable --now docker
> sudo systemctl enable --now tailscaled
> sudo systemctl enable --now cockpit.socket
> ```
> 
> Then check:
> 
> ```bash
> systemctl is-enabled docker tailscaled cockpit.socket
> ```
> 
> You want:
> 
> ```text
> enabled
> enabled
> enabled
> ```
> 
> ## Fix Docker containers so they restart automatically
> 
> For each important container, check restart policy:
> 
> ```bash
> docker inspect --format='{{.Name}} restart={{.HostConfig.RestartPolicy.Name}}' $(docker ps -aq)
> ```
> 
> If you see empty, `no`, or weirdness, fix the important ones:
> 
> ```bash
> docker update --restart unless-stopped $(docker ps -aq)
> ```
> 
> That tells Docker: “when the server boots, bring these back unless I manually stopped them.”
> 
> ## If QiAccess/Homepage is a Compose stack
> 
> Find it:
> 
> ```bash
> find /srv -maxdepth 5 -iname "docker-compose.yml" -o -iname "compose.yml" 2>/dev/null
> ```
> 
> You previously had something like:
> 
> ```text
> /srv/qios/stacks/_qiaccess_start
> ```
> 
> So try:
> 
> ```bash
> cd /srv/qios/stacks/_qiaccess_start
> docker compose ps
> docker compose up -d
> ```
> 
> Then make sure the compose file has this under each service:
> 
> ```yaml
> restart: unless-stopped
> ```
> 
> Especially for Homepage/QiAccess.
> 
> ## The real “make it boot like a server” fix
> 
> Create a systemd unit for the QiAccess stack so it starts even if Docker Compose doesn’t get triggered manually.
> 
> Run:
> 
> ```bash
> sudo nano /etc/systemd/system/qiaccess.service
> ```
> 
> Paste:
> 
> ```ini
> [Unit]
> Description=QiAccess Homepage Stack
> Requires=docker.service
> After=docker.service network-online.target tailscaled.service
> Wants=network-online.target
> 
> [Service]
> Type=oneshot
> WorkingDirectory=/srv/qios/stacks/_qiaccess_start
> ExecStart=/usr/bin/docker compose up -d
> ExecStop=/usr/bin/docker compose down
> RemainAfterExit=yes
> TimeoutStartSec=0
> 
> [Install]
> WantedBy=multi-user.target
> ```
> 
> Save, then:
> 
> ```bash
> sudo systemctl daemon-reload
> sudo systemctl enable --now qiaccess.service
> sudo systemctl status qiaccess.service --no-pager
> ```
> 
> Now QiAccess should come up at boot without logging into the UI.
> 
> ## Then test without guessing
> 
> Reboot the server:
> 
> ```bash
> sudo reboot
> ```
> 
> Do **not** log into the server UI.
> 
> From your PC, wait a minute, then try:
> 
> `https://qiserver-1.cerberus-sirius.ts.net/`
> 
> Then:
> 
> `https://100.121.111.106:9090`
> 
> If those load before anyone logs in, problem solved.
> 
> ## Important distinction
> 
> If this is actually your **Windows local PC** running Docker Desktop, different answer: Docker Desktop usually depends on user login. For true unattended boot, either:
> 
> - move the service to qiserver/Linux, or
> - run Docker through WSL/system service setup, or
> - use Windows Task Scheduler to start Docker/Desktop/app at startup/login
> 
> But for `qiserver`, the proper fix is: **Docker + Tailscale + Cockpit enabled at boot, containers using restart policies, and QiAccess managed by systemd.**

### User
> QISERVER → Runbook: /srv/qios/docs/000_RUN_ME_FIRST.md

> QISERVER → Status: qs

> QISERVER → UI: https://qiserver-1.cerberus-sirius.ts.net

> 

> qiadmin@qiserver:~$ echo "=== OS ==="

> === OS ===

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ cat /etc/os-release | head

> PRETTY_NAME="Ubuntu 24.04.4 LTS"

> NAME="Ubuntu"

> VERSION_ID="24.04"

> VERSION="24.04.4 LTS (Noble Numbat)"

> VERSION_CODENAME=noble

> ID=ubuntu

> ID_LIKE=debian

> HOME_URL="https://www.ubuntu.com/"

> SUPPORT_URL="https://help.ubuntu.com/"

> BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ echo ""

> 

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ echo "=== Docker enabled? ==="

> === Docker enabled? ===

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ systemctl is-enabled docker

> enabled

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ systemctl is-active docker

> active

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ echo ""

> 

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ echo "=== Tailscale enabled? ==="

> === Tailscale enabled? ===

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ systemctl is-enabled tailscaled

> enabled

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ systemctl is-active tailscaled

> active

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ echo ""

> 

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ echo "=== Cockpit enabled? ==="

> === Cockpit enabled? ===

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ systemctl is-enabled cockpit.socket

> enabled

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ systemctl is-active cockpit.socket

> active

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ echo ""

> 

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ echo "=== Containers + restart policies ==="

> === Containers + restart policies ===

> qiadmin@qiserver:~$ 

> qiadmin@qiserver:~$ docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

> NAMES            STATUS                    PORTS

> homepage         Up 22 minutes (healthy)   0.0.0.0:3001->3000/tcp, [::]:3001->3000/tcp

> portainer        Up 22 minutes             8000/tcp, 9000/tcp, 0.0.0.0:9443->9443/tcp, [::]:9443->9443/tcp

> open-webui       Up 22 minutes (healthy)   127.0.0.1:3000->8080/tcp

> neo4j            Up 22 minutes             127.0.0.1:7474->7474/tcp, 7473/tcp, 127.0.0.1:7687->7687/tcp

> friendly_elion   Exited (0) 2 weeks ago    

> qiadmin@qiserver:~$ sudo systemctl enable --now docker

> [sudo] password for qiadmin: 

> Sorry, try again.

> [sudo] password for qiadmin: 

> Synchronizing state of docker.service with SysV service script with /usr/lib/systemd/systemd-sysv-install.

> Executing: /usr/lib/systemd/systemd-sysv-install enable docker

> qiadmin@qiserver:~$ systemctl is-enabled docker tailscaled cockpit.socket

> enabled

> enabled

> enabled

> qiadmin@qiserver:~$ docker inspect --format='{{.Name}} restart={{.HostConfig.RestartPolicy.Name}}' $(docker ps -aq)

> /homepage restart=unless-stopped

> /portainer restart=always

> /open-webui restart=unless-stopped

> /neo4j restart=unless-stopped

> /friendly_elion restart=no

> qiadmin@qiserver:~$ docker update --restart unless-stopped $(docker ps -aq)

> 5be0d0165f5e

> 84663ecd9ba4

> ee7fc7eecea1

> c11fc8375559

> 5c606e3b7e1c

> qiadmin@qiserver:~$

### Assistant
> Good. This tells us the core boot chain is **already mostly correct**:
> 
> - Ubuntu server ✅
> - Docker enabled + active ✅
> - Tailscale enabled + active ✅
> - Cockpit enabled + active ✅
> - Main containers are running ✅
> - Restart policies are now fixed ✅
> 
> The likely issue was **container restart policy drift**, especially if something had been started manually at some point. You just corrected that with:
> 
> `docker update --restart unless-stopped $(docker ps -aq)`
> 
> So now after reboot, these should auto-start:
> 
> - `homepage`
> - `portainer`
> - `open-webui`
> - `neo4j`
> - `friendly_elion` too, but that one is probably junk/old and should be inspected later
> 
> ## What to do next: test the actual problem
> 
> Run this:
> 
> ```bash
> sudo reboot
> ```
> 
> Then **do not log into the server UI**.
> 
> From your other machine/browser, test:
> 
> 1. `https://qiserver-1.cerberus-sirius.ts.net`
> 2. `https://100.121.111.106:9090`
> 3. `https://100.121.111.106:9443`
> 4. `https://qiserver-1.cerberus-sirius.ts.net:9446`
> 
> If QiAccess loads without local UI login, fixed.
> 
> ## One thing I see immediately
> 
> Your dashboard says Paperless is:
> 
> `https://100.121.111.106:8000`
> 
> But your current Docker list does **not** show a Paperless container. Portainer internally exposes `8000/tcp`, but externally only maps:
> 
> `9443 -> 9443`
> 
> So that **Mail Intake / Paperless link is probably stale or wrong** unless Paperless is somewhere else, not Docker, or not currently installed.
> 
> Right now your live containers are only:
> 
> - Homepage/QiAccess on `3001`
> - Portainer on `9443`
> - Open WebUI on localhost `3000`
> - Neo4j on localhost `7474` / `7687`
> - one old exited container
> 
> ## Clean up check after reboot
> 
> After reboot, go into Cockpit Terminal and run:
> 
> ```bash
> qs
> ```
> 
> Since your login banner says `QISERVER → Status: qs`, that command likely already summarizes your server state. Nice. Use the tool you built, girl.
> 
> Then run:
> 
> ```bash
> docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
> ```
> 
> If `homepage`, `portainer`, `open-webui`, and `neo4j` are up before desktop login, we are done with boot.
> 
> ## Next fix after that
> 
> We need to update QiAccess links:
> 
> - Keep `Host Admin` → Cockpit
> - Keep `Docker Admin` → Portainer
> - Keep `AI Chat` → Open WebUI
> - Remove or disable `Mail Intake` until Paperless actually exists
> - Add Paperless back once the local Docker Paperless stack is installed and mapped correctly
> 
> Also, `friendly_elion` is probably trash. Later, inspect it with:
> 
> ```bash
> docker inspect friendly_elion --format '{{.Config.Image}}'
> ```
> 
> If it’s nothing important, remove it:
> 
> ```bash
> docker rm friendly_elion
> ```
> 
> But don’t clean that until after the reboot test. First prove the server starts like a server.

### User
> oh it because i need to install paperless still i think on the server, how do i do that.

### Assistant
> Yep. The dashboard link was aspirational/staged, not proof Paperless is installed. We’ll install it as a proper Docker Compose stack on qiserver and make it auto-start like the rest.

### Assistant
> Yep — install Paperless **on qiserver**, not your local PC, if you want the dashboard link to work and the intake pipeline to be always-on.
> 
> Paperless-ngx is specifically meant for this: it turns documents into a searchable archive, stores files locally on your server, OCRs documents, supports PDFs/images/Office docs, and saves documents on disk with configurable filename formats. citeturn868356search1 Perfect fit as your **intake/OCR layer**, not your canonical QiArchive truth layer.
> 
> ## Install Paperless on qiserver
> 
> In Cockpit Terminal or SSH on qiserver:
> 
> ```bash
> sudo mkdir -p /srv/qios/stacks/paperless
> sudo mkdir -p /srv/qios/data/paperless/{consume,data,media,export,trash}
> sudo chown -R qiadmin:qiadmin /srv/qios/stacks/paperless /srv/qios/data/paperless
> cd /srv/qios/stacks/paperless
> ```
> 
> Create the env file:
> 
> ```bash
> nano docker-compose.env
> ```
> 
> Paste this:
> 
> ```env
> PAPERLESS_SECRET_KEY=CHANGE_ME_TO_A_RANDOM_SECRET
> PAPERLESS_TIME_ZONE=America/Chicago
> PAPERLESS_OCR_LANGUAGE=eng
> PAPERLESS_CONSUMER_RECURSIVE=true
> PAPERLESS_CONSUMER_POLLING=30
> PAPERLESS_TRASH_DIR=/usr/src/paperless/trash
> PAPERLESS_URL=https://100.121.111.106:8000
> PAPERLESS_ADMIN_USER=cody
> PAPERLESS_ADMIN_PASSWORD=CHANGE_ME_NOW
> PAPERLESS_ADMIN_MAIL=crice4485@gmail.com
> ```
> 
> Generate a real secret key:
> 
> ```bash
> python3 - <<'PY'
> import secrets
> print(secrets.token_urlsafe(64))
> PY
> ```
> 
> Replace `CHANGE_ME_TO_A_RANDOM_SECRET` with that output.
> 
> Now create the compose file:
> 
> ```bash
> nano docker-compose.yml
> ```
> 
> Paste:
> 
> ```yaml
> services:
>   paperless-broker:
>     image: docker.io/library/redis:7
>     restart: unless-stopped
>     volumes:
>       - paperless_redisdata:/data
> 
>   paperless-db:
>     image: docker.io/library/postgres:16
>     restart: unless-stopped
>     volumes:
>       - paperless_pgdata:/var/lib/postgresql/data
>     environment:
>       POSTGRES_DB: paperless
>       POSTGRES_USER: paperless
>       POSTGRES_PASSWORD: paperless_local_change_me
> 
>   paperless-webserver:
>     image: ghcr.io/paperless-ngx/paperless-ngx:latest
>     restart: unless-stopped
>     depends_on:
>       - paperless-db
>       - paperless-broker
>     ports:
>       - "8000:8000"
>     volumes:
>       - /srv/qios/data/paperless/data:/usr/src/paperless/data
>       - /srv/qios/data/paperless/media:/usr/src/paperless/media
>       - /srv/qios/data/paperless/export:/usr/src/paperless/export
>       - /srv/qios/data/paperless/consume:/usr/src/paperless/consume
>       - /srv/qios/data/paperless/trash:/usr/src/paperless/trash
>     env_file: docker-compose.env
>     environment:
>       PAPERLESS_REDIS: redis://paperless-broker:6379
>       PAPERLESS_DBHOST: paperless-db
> 
> volumes:
>   paperless_pgdata:
>   paperless_redisdata:
> ```
> 
> Bring it up:
> 
> ```bash
> docker compose up -d
> docker compose ps
> docker compose logs -f paperless-webserver
> ```
> 
> Open:
> 
> `https://100.121.111.106:8000`
> 
> Tiny warning: it may complain about HTTPS because Paperless itself is plain HTTP behind Docker. If the HTTPS link fails, try:
> 
> `http://100.121.111.106:8000`
> 
> If HTTP works but HTTPS doesn’t, we’ll fix the dashboard link. No drama.
> 
> ## Test intake
> 
> Drop a file into:
> 
> ```bash
> /srv/qios/data/paperless/consume
> ```
> 
> Or from Windows, once we make an easy network/drop path later.
> 
> For server-side test:
> 
> ```bash
> echo "QiOS Paperless test $(date)" > /srv/qios/data/paperless/consume/test.txt
> docker compose logs -f paperless-webserver
> ```
> 
> Then open Paperless and confirm it imported.
> 
> ## Add it to boot properly
> 
> Because the compose file has `restart: unless-stopped`, Docker should bring it back on reboot. But because we like grown-up infrastructure, add a systemd unit too:
> 
> ```bash
> sudo nano /etc/systemd/system/qios-paperless.service
> ```
> 
> Paste:
> 
> ```ini
> [Unit]
> Description=QiOS Paperless Stack
> Requires=docker.service
> After=docker.service network-online.target tailscaled.service
> Wants=network-online.target
> 
> [Service]
> Type=oneshot
> WorkingDirectory=/srv/qios/stacks/paperless
> ExecStart=/usr/bin/docker compose up -d
> ExecStop=/usr/bin/docker compose down
> RemainAfterExit=yes
> TimeoutStartSec=0
> 
> [Install]
> WantedBy=multi-user.target
> ```
> 
> Enable it:
> 
> ```bash
> sudo systemctl daemon-reload
> sudo systemctl enable --now qios-paperless.service
> sudo systemctl status qios-paperless.service --no-pager
> ```
> 
> ## Then update QiAccess if needed
> 
> Your current dashboard already points **Mail Intake** to:
> 
> `https://100.121.111.106:8000`
> 
> If Paperless only works over `http://100.121.111.106:8000`, update the Homepage config from `https` to `http`.
> 
> Find the config:
> 
> ```bash
> find /srv/qios/stacks/_qiaccess_start -maxdepth 3 -type f | sort
> ```
> 
> Likely file:
> 
> ```bash
> nano /srv/qios/stacks/_qiaccess_start/config/services.yaml
> ```
> 
> Change Mail Intake href to whichever works:
> 
> ```yaml
> href: http://100.121.111.106:8000
> ```
> 
> Then restart QiAccess:
> 
> ```bash
> cd /srv/qios/stacks/_qiaccess_start
> docker compose restart
> ```
> 
> ## The correct QiOS role
> 
> Paperless is now:
> 
> **Mail Intake / Document Warehouse**
> 
> Not final truth.
> 
> QiArchive still owns:
> 
> - canonical ID
> - short code
> - checksum
> - normalized filename
> - registration state
> - chunks
> - embeddings
> - graph projection eligibility
> 
> So the first real integration target after install is:
> 
> `/srv/qios/data/paperless/media/documents/originals`
> 
> or exported docs from:
> 
> `/srv/qios/data/paperless/export`
> 
> That folder becomes an input source for QiArchive scanning. Paperless gets documents readable. QiArchive makes them canonical.

### User
> qiadmin@qiserver:~$ docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

> NAMES            STATUS                          PORTS

> homepage         Up 45 seconds (healthy)         0.0.0.0:3001->3000/tcp, [::]:3001->3000/tcp

> portainer        Up 45 seconds                   8000/tcp, 9000/tcp, 0.0.0.0:9443->9443/tcp, [::]:9443->9443/tcp

> open-webui       Up 45 seconds (healthy)         127.0.0.1:3000->8080/tcp

> neo4j            Up 45 seconds                   127.0.0.1:7474->7474/tcp, 7473/tcp, 127.0.0.1:7687->7687/tcp

> friendly_elion   Restarting (0) 19 seconds ago   

> qiadmin@qiserver:~$

### Assistant
> Good news: **the reboot test basically passed.** Your real services came up after 45 seconds:
> 
> - `homepage` ✅
> - `portainer` ✅
> - `open-webui` ✅
> - `neo4j` ✅
> 
> So the “server needs UI login before services start” problem is likely fixed.
> 
> The only ugly thing is:
> 
> `friendly_elion   Restarting`
> 
> That’s junk until proven otherwise. It’s repeatedly restarting because we changed all containers to `unless-stopped`, including that old exited container. Classic “we fixed the house and accidentally resurrected a raccoon in the attic.”
> 
> ## Fix the restarting junk container
> 
> Run:
> 
> ```bash
> docker inspect friendly_elion --format 'name={{.Name}} image={{.Config.Image}} command={{.Config.Cmd}} restart={{.HostConfig.RestartPolicy.Name}}'
> ```
> 
> If it’s not something you recognize or need, stop and remove it:
> 
> ```bash
> docker stop friendly_elion
> docker rm friendly_elion
> ```
> 
> If you want to be cautious, disable restart first:
> 
> ```bash
> docker update --restart no friendly_elion
> docker stop friendly_elion
> ```
> 
> Then inspect later.
> 
> ## Now install Paperless
> 
> Since your core services boot correctly, do Paperless next. Use a different folder and avoid colliding with Portainer’s internal `8000/tcp` thing.
> 
> Run this:
> 
> ```bash
> sudo mkdir -p /srv/qios/stacks/paperless
> sudo mkdir -p /srv/qios/data/paperless/{consume,data,media,export,trash}
> sudo chown -R qiadmin:qiadmin /srv/qios/stacks/paperless /srv/qios/data/paperless
> cd /srv/qios/stacks/paperless
> ```
> 
> Create the secret:
> 
> ```bash
> python3 - <<'PY'
> import secrets
> print(secrets.token_urlsafe(64))
> PY
> ```
> 
> Create env file:
> 
> ```bash
> nano docker-compose.env
> ```
> 
> Paste this, replacing the two `CHANGE_ME` values:
> 
> ```env
> PAPERLESS_SECRET_KEY=CHANGE_ME_TO_RANDOM_SECRET_FROM_COMMAND
> PAPERLESS_TIME_ZONE=America/Chicago
> PAPERLESS_OCR_LANGUAGE=eng
> PAPERLESS_CONSUMER_RECURSIVE=true
> PAPERLESS_CONSUMER_POLLING=30
> PAPERLESS_TRASH_DIR=/usr/src/paperless/trash
> PAPERLESS_URL=http://100.121.111.106:8010
> PAPERLESS_ADMIN_USER=cody
> PAPERLESS_ADMIN_PASSWORD=CHANGE_ME_NOW
> PAPERLESS_ADMIN_MAIL=crice4485@gmail.com
> ```
> 
> I’m deliberately using **8010**, not 8000. Cleaner. Less “which 8000 is this?” nonsense.
> 
> Create compose file:
> 
> ```bash
> nano docker-compose.yml
> ```
> 
> Paste:
> 
> ```yaml
> services:
>   paperless-broker:
>     image: docker.io/library/redis:7
>     restart: unless-stopped
>     volumes:
>       - paperless_redisdata:/data
> 
>   paperless-db:
>     image: docker.io/library/postgres:16
>     restart: unless-stopped
>     volumes:
>       - paperless_pgdata:/var/lib/postgresql/data
>     environment:
>       POSTGRES_DB: paperless
>       POSTGRES_USER: paperless
>       POSTGRES_PASSWORD: paperless_local_change_me
> 
>   paperless-webserver:
>     image: ghcr.io/paperless-ngx/paperless-ngx:latest
>     restart: unless-stopped
>     depends_on:
>       - paperless-db
>       - paperless-broker
>     ports:
>       - "8010:8000"
>     volumes:
>       - /srv/qios/data/paperless/data:/usr/src/paperless/data
>       - /srv/qios/data/paperless/media:/usr/src/paperless/media
>       - /srv/qios/data/paperless/export:/usr/src/paperless/export
>       - /srv/qios/data/paperless/consume:/usr/src/paperless/consume
>       - /srv/qios/data/paperless/trash:/usr/src/paperless/trash
>     env_file: docker-compose.env
>     environment:
>       PAPERLESS_REDIS: redis://paperless-broker:6379
>       PAPERLESS_DBHOST: paperless-db
> 
> volumes:
>   paperless_pgdata:
>   paperless_redisdata:
> ```
> 
> Start it:
> 
> ```bash
> docker compose up -d
> docker compose ps
> docker compose logs -f paperless-webserver
> ```
> 
> Open:
> 
> `http://100.121.111.106:8010`
> 
> ## Then update QiAccess Mail Intake link
> 
> Your dashboard currently points Paperless to `https://100.121.111.106:8000`, which is stale/wrong.
> 
> Find the config:
> 
> ```bash
> find /srv/qios/stacks/_qiaccess_start -maxdepth 3 -type f | sort
> ```
> 
> Edit services:
> 
> ```bash
> nano /srv/qios/stacks/_qiaccess_start/config/services.yaml
> ```
> 
> Change Mail Intake to:
> 
> ```yaml
> href: http://100.121.111.106:8010
> ```
> 
> Restart QiAccess:
> 
> ```bash
> cd /srv/qios/stacks/_qiaccess_start
> docker compose restart
> ```
> 
> That gets you:
> 
> **QiAccess → Mail Intake → Paperless working**
> 
> Then we wire Paperless output into QiArchive. One beast at a time.

### User
> ok there was some kind of error with paperles on the server we need to check what actualy happened

### Assistant
> Yep, pause the install brain and go diagnostic mode. We need the actual container state, logs, and compose config—guessing here would be how we create Docker soup.

### Assistant
> Run these from qiserver inside the Paperless stack folder:
> 
> ```bash
> cd /srv/qios/stacks/paperless
> ```
> 
> ## 1. Show what Paperless containers exist
> 
> ```bash
> docker compose ps
> ```
> 
> Then also:
> 
> ```bash
> docker ps -a --filter "name=paperless" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
> ```
> 
> ## 2. Pull the actual logs
> 
> Start with the webserver:
> 
> ```bash
> docker compose logs --tail=200 paperless-webserver
> ```
> 
> Then DB and Redis:
> 
> ```bash
> docker compose logs --tail=100 paperless-db
> docker compose logs --tail=100 paperless-broker
> ```
> 
> ## 3. Check the compose file for typos
> 
> ```bash
> cat docker-compose.yml
> ```
> 
> And env file, but hide secrets:
> 
> ```bash
> grep -v "PASSWORD\|SECRET" docker-compose.env
> ```
> 
> ## 4. Check port conflicts
> 
> Since we were deliberately using `8010`, confirm nothing else grabbed it:
> 
> ```bash
> sudo ss -tulpn | grep -E ':8010|:8000|:9443|:3001|:3000'
> ```
> 
> ## 5. Check folder permissions
> 
> ```bash
> ls -lah /srv/qios/data/paperless
> ls -lah /srv/qios/stacks/paperless
> ```
> 
> ## 6. Check if Paperless image pulled correctly
> 
> ```bash
> docker images | grep paperless
> ```
> 
> ## 7. If it is restarting, inspect why
> 
> ```bash
> docker inspect paperless-paperless-webserver-1 --format '{{.State.Status}} {{.State.ExitCode}} {{.State.Error}}'
> ```
> 
> If the container name is different, get exact names with:
> 
> ```bash
> docker ps -a --format "table {{.Names}}\t{{.Status}}"
> ```
> 
> ## Send me this output
> 
> The most useful pieces are:
> 
> ```bash
> docker compose ps
> docker compose logs --tail=200 paperless-webserver
> docker compose logs --tail=100 paperless-db
> sudo ss -tulpn | grep -E ':8010|:8000'
> ```
> 
> Common likely causes:
> 
> - `PAPERLESS_SECRET_KEY` still says `CHANGE_ME...`
> - password/env typo
> - Postgres not ready yet
> - volume permission issue
> - port conflict
> - compose file indentation issue
> - browser using `https://` when Paperless is only on `http://`
> 
> Don’t reinstall yet. First we read the body at the scene of the crime.

### User
> the folder has not configuration file it says.

### Assistant
> That means you’re in the folder, but **`docker-compose.yml` was never created there** or it was created under a different name/path.
> 
> Run this first:
> 
> ```bash
> pwd
> ls -lah
> ```
> 
> You should be in:
> 
> `/srv/qios/stacks/paperless`
> 
> If `docker-compose.yml` is missing, create it now:
> 
> ```bash
> cd /srv/qios/stacks/paperless
> nano docker-compose.yml
> ```
> 
> Paste this:
> 
> ```yaml
> services:
>   paperless-broker:
>     image: docker.io/library/redis:7
>     restart: unless-stopped
>     volumes:
>       - paperless_redisdata:/data
> 
>   paperless-db:
>     image: docker.io/library/postgres:16
>     restart: unless-stopped
>     volumes:
>       - paperless_pgdata:/var/lib/postgresql/data
>     environment:
>       POSTGRES_DB: paperless
>       POSTGRES_USER: paperless
>       POSTGRES_PASSWORD: paperless_local_change_me
> 
>   paperless-webserver:
>     image: ghcr.io/paperless-ngx/paperless-ngx:latest
>     restart: unless-stopped
>     depends_on:
>       - paperless-db
>       - paperless-broker
>     ports:
>       - "8010:8000"
>     volumes:
>       - /srv/qios/data/paperless/data:/usr/src/paperless/data
>       - /srv/qios/data/paperless/media:/usr/src/paperless/media
>       - /srv/qios/data/paperless/export:/usr/src/paperless/export
>       - /srv/qios/data/paperless/consume:/usr/src/paperless/consume
>       - /srv/qios/data/paperless/trash:/usr/src/paperless/trash
>     env_file: docker-compose.env
>     environment:
>       PAPERLESS_REDIS: redis://paperless-broker:6379
>       PAPERLESS_DBHOST: paperless-db
> 
> volumes:
>   paperless_pgdata:
>   paperless_redisdata:
> ```
> 
> Then confirm the env file exists:
> 
> ```bash
> ls -lah docker-compose.env
> ```
> 
> If that says missing too, create it:
> 
> ```bash
> nano docker-compose.env
> ```
> 
> Paste this, but replace the password and secret:
> 
> ```env
> PAPERLESS_SECRET_KEY=CHANGE_ME_RANDOM_SECRET
> PAPERLESS_TIME_ZONE=America/Chicago
> PAPERLESS_OCR_LANGUAGE=eng
> PAPERLESS_CONSUMER_RECURSIVE=true
> PAPERLESS_CONSUMER_POLLING=30
> PAPERLESS_TRASH_DIR=/usr/src/paperless/trash
> PAPERLESS_URL=http://100.121.111.106:8010
> PAPERLESS_ADMIN_USER=cody
> PAPERLESS_ADMIN_PASSWORD=CHANGE_ME_NOW
> PAPERLESS_ADMIN_MAIL=crice4485@gmail.com
> ```
> 
> Generate the secret with:
> 
> ```bash
> python3 - <<'PY'
> import secrets
> print(secrets.token_urlsafe(64))
> PY
> ```
> 
> Now run:
> 
> ```bash
> docker compose config
> ```
> 
> If that prints the combined config with no errors, start it:
> 
> ```bash
> docker compose up -d
> docker compose ps
> ```
> 
> Open:
> 
> `http://100.121.111.106:8010`
> 
> If `docker compose config` still says no configuration file, you are not in the right folder. Run:
> 
> ```bash
> find /srv/qios -maxdepth 5 \( -name "docker-compose.yml" -o -name "compose.yml" \) -print
> ```
> 
> Tiny but important: the file must be named **exactly** one of these:
> 
> `docker-compose.yml`  
> `compose.yml`
> 
> Not `docker-compose.yaml.txt`, not `docker-compose.yml.save`, not inside some accidental nested folder.

### User
> says permission denied to writing

### Assistant
> Permission issue. Easy fix — the folder is probably owned by `root` because we created it with `sudo`.
> 
> Run this:
> 
> ```bash
> sudo chown -R qiadmin:qiadmin /srv/qios/stacks/paperless /srv/qios/data/paperless
> sudo chmod -R u+rwX /srv/qios/stacks/paperless /srv/qios/data/paperless
> ```
> 
> Then go back in:
> 
> ```bash
> cd /srv/qios/stacks/paperless
> pwd
> ls -lah
> ```
> 
> Now try creating the file again:
> 
> ```bash
> nano docker-compose.yml
> ```
> 
> If `nano` still says permission denied, use sudo just for the edit:
> 
> ```bash
> sudo nano docker-compose.yml
> ```
> 
> Then after saving, fix ownership again:
> 
> ```bash
> sudo chown qiadmin:qiadmin docker-compose.yml
> ```
> 
> Also create/check the env file:
> 
> ```bash
> nano docker-compose.env
> ```
> 
> or if needed:
> 
> ```bash
> sudo nano docker-compose.env
> sudo chown qiadmin:qiadmin docker-compose.env
> ```
> 
> Then validate:
> 
> ```bash
> docker compose config
> ```
> 
> If that works, start it:
> 
> ```bash
> docker compose up -d
> docker compose ps
> ```
> 
> One more thing: if Docker itself gives permission denied later, add your user to the Docker group:
> 
> ```bash
> sudo usermod -aG docker qiadmin
> ```
> 
> Then log out/back in, or run:
> 
> ```bash
> newgrp docker
> ```
> 
> But right now your error sounds like plain folder/file ownership, not Docker.

### Assistant
> Good. Paperless **did install and start**. The error was simply that the folder originally had no compose file, then ownership was root-owned. You fixed both.
> 
> Current status from your pasted output:
> 
> - `/srv/qios/stacks/paperless` exists
> - `docker-compose.yml` now exists and validates
> - `docker-compose.env` now exists
> - Docker created the Paperless network and volumes
> - Redis started
> - Postgres started
> - Paperless webserver started
> - Paperless is mapped to `0.0.0.0:8010->8000/tcp`
> - Health is still `starting`, which is normal right after first launch fileciteturn2file0
> 
> Open this now:
> 
> `http://100.121.111.106:8010`
> 
> Not HTTPS. Use **HTTP** for this one unless we later put it behind a reverse proxy/Tailscale Serve/Cloudflare.
> 
> ## One important security cleanup
> 
> You pasted the Paperless admin password and secret key into chat/log text. Treat those as exposed now. Not panic-level because this is private Tailnet-ish, but still: rotate them. Don’t reuse that password.
> 
> Edit:
> 
> ```bash
> cd /srv/qios/stacks/paperless
> nano docker-compose.env
> ```
> 
> Change:
> 
> `PAPERLESS_ADMIN_PASSWORD=...`
> 
> Also change:
> 
> `PAPERLESS_SECRET_KEY=...`
> 
> Generate a new secret:
> 
> ```bash
> python3 - <<'PY'
> import secrets
> print(secrets.token_urlsafe(64))
> PY
> ```
> 
> Then restart:
> 
> ```bash
> docker compose down
> docker compose up -d
> ```
> 
> Since this is first install, restarting clean is fine. If you already logged in or imported docs, tell me before changing the secret key.
> 
> ## Check if it fully came up
> 
> Run:
> 
> ```bash
> cd /srv/qios/stacks/paperless
> docker compose ps
> docker compose logs --tail=100 paperless-webserver
> ```
> 
> You want the webserver to move from:
> 
> `health: starting`
> 
> to something like:
> 
> `healthy`
> 
> ## Update QiAccess link
> 
> Your dashboard currently points Mail Intake to the old/wrong URL. Set it to:
> 
> `http://100.121.111.106:8010`
> 
> Find/edit:
> 
> ```bash
> nano /srv/qios/stacks/_qiaccess_start/config/services.yaml
> ```
> 
> Then restart dashboard:
> 
> ```bash
> cd /srv/qios/stacks/_qiaccess_start
> docker compose restart
> ```
> 
> ## Then test intake
> 
> Once the UI opens, drop a tiny test file:
> 
> ```bash
> echo "QiOS Paperless test $(date)" > /srv/qios/data/paperless/consume/test.txt
> ```
> 
> Then watch:
> 
> ```bash
> cd /srv/qios/stacks/paperless
> docker compose logs -f paperless-webserver
> ```
> 
> If it imports, Paperless is alive. Then we wire QiArchive to watch Paperless originals/exports.

### Assistant
> Found it. Paperless itself is fine. The webserver is failing because **Postgres rejected the password for user `paperless`**:
> 
> `FATAL: password authentication failed for user "paperless"` fileciteturn3file0
> 
> This usually happens when the Postgres volume was created with one password, then the compose/env password changed afterward. Postgres keeps the original password inside the DB volume. Docker env changes do **not** reset an existing Postgres database. Annoying, but normal.
> 
> Since this is a fresh Paperless install with no documents yet, easiest clean fix: **delete the Paperless Postgres volume and recreate it.**
> 
> ## Do this exactly
> 
> From:
> 
> ```bash
> cd /srv/qios/stacks/paperless
> ```
> 
> Run:
> 
> ```bash
> docker compose down
> ```
> 
> Now remove only the Paperless DB + Redis volumes:
> 
> ```bash
> docker volume rm paperless_paperless_pgdata paperless_paperless_redisdata
> ```
> 
> Then bring it back:
> 
> ```bash
> docker compose up -d
> docker compose ps
> ```
> 
> Watch logs:
> 
> ```bash
> docker compose logs -f paperless-webserver
> ```
> 
> You want it to get past:
> 
> `Apply database migrations...`
> 
> and not throw the password failure.
> 
> ## If Docker says volume is in use
> 
> Run:
> 
> ```bash
> docker compose down --volumes
> ```
> 
> Then:
> 
> ```bash
> docker compose up -d
> ```
> 
> That wipes the Paperless DB volume only for this stack. Fine because this is first setup.
> 
> ## After it starts
> 
> Open:
> 
> `http://100.121.111.106:8010`
> 
> Then immediately change the admin password inside Paperless UI if needed.
> 
> Also: you pasted the DB/admin password and secret earlier, so after Paperless is healthy, rotate them. But **don’t rotate mid-fix** or we’ll chase our tail like a cursed Roomba. First get it healthy.

### User
> erless-webserver-1  | [init-folders] Running with root privileges, adjusting directories and permissions
> paperless-webserver-1  | paperless-db:5432 - accepting connections
> paperless-webserver-1  | [init-db-wait] Connected to PostgreSQL
> paperless-webserver-1  | [init-db-wait] Database is ready
> paperless-webserver-1  | [init-migrations] Apply database migrations...
> paperless-webserver-1  | Waiting for Redis...
> paperless-webserver-1  | Connected to Redis broker.
> paperless-webserver-1  | [init-redis-wait] Redis ready
> paperless-webserver-1  | Traceback (most recent call last):
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 279, in ensure_connection
> paperless-webserver-1  |     self.connect()
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
> paperless-webserver-1  |     return func(*args, **kwargs)
> paperless-webserver-1  |            ^^^^^^^^^^^^^^^^^^^^^
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 256, in connect
> paperless-webserver-1  |     self.connection = self.get_new_connection(conn_params)
> paperless-webserver-1  |                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
> paperless-webserver-1  |     return func(*args, **kwargs)
> paperless-webserver-1  |            ^^^^^^^^^^^^^^^^^^^^^
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/db/backends/postgresql/base.py", line 332, in get_new_connection
> paperless-webserver-1  |     connection = self.Database.connect(**conn_params)
> paperless-webserver-1  |                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/psycopg/connection.py", line 120, in connect
> paperless-webserver-1  |     raise last_ex.with_traceback(None)
> paperless-webserver-1  | psycopg.OperationalError: connection failed: connection to server at "172.23.0.2", port 5432 failed: FATAL:  password authentication failed for user "paperless"
> paperless-webserver-1  | 
> paperless-webserver-1  | The above exception was the direct cause of the following exception:
> paperless-webserver-1  | 
> paperless-webserver-1  | Traceback (most recent call last):
> paperless-webserver-1  |   File "/usr/src/paperless/src/manage.py", line 10, in <module>
> paperless-webserver-1  |     execute_from_command_line(sys.argv)
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/core/management/__init__.py", line 442, in execute_from_command_line
> paperless-webserver-1  |     utility.execute()
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/core/management/__init__.py", line 436, in execute
> paperless-webserver-1  |     self.fetch_command(subcommand).run_from_argv(self.argv)
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/core/management/base.py", line 416, in run_from_argv
> paperless-webserver-1  |     self.execute(*args, **cmd_options)
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/core/management/base.py", line 460, in execute
> paperless-webserver-1  |     output = self.handle(*args, **options)
> paperless-webserver-1  |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/core/management/base.py", line 107, in wrapper
> paperless-webserver-1  |     res = handle_func(*args, **kwargs)
> paperless-webserver-1  |           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/core/management/commands/migrate.py", line 114, in handle
> paperless-webserver-1  |     executor = MigrationExecutor(connection, self.migration_progress_callback)
> paperless-webserver-1  |                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/db/migrations/executor.py", line 18, in __init__
> paperless-webserver-1  |     self.loader = MigrationLoader(self.connection)
> paperless-webserver-1  |                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/db/migrations/loader.py", line 58, in __init__
> paperless-webserver-1  |     self.build_graph()
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/db/migrations/loader.py", line 235, in build_graph
> paperless-webserver-1  |     self.applied_migrations = recorder.applied_migrations()
> paperless-webserver-1  |                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/db/migrations/recorder.py", line 89, in applied_migrations
> paperless-webserver-1  |     if self.has_table():
> paperless-webserver-1  |        ^^^^^^^^^^^^^^^^
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/db/migrations/recorder.py", line 63, in has_table
> paperless-webserver-1  |     with self.connection.cursor() as cursor:
> paperless-webserver-1  |          ^^^^^^^^^^^^^^^^^^^^^^^^
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
> paperless-webserver-1  |     return func(*args, **kwargs)
> paperless-webserver-1  |            ^^^^^^^^^^^^^^^^^^^^^
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 320, in cursor
> paperless-webserver-1  |     return self._cursor()
> paperless-webserver-1  |            ^^^^^^^^^^^^^^
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 296, in _cursor
> paperless-webserver-1  |     self.ensure_connection()
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/utils/asyncio.py", line 26, in inner
> paperless-webserver-1  |     return func(*args, **kwargs)
> paperless-webserver-1  |            ^^^^^^^^^^^^^^^^^^^^^
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/db/backends/base/base.py", line 278, in ensure_connection
> paperless-webserver-1  |     with self.wrap_database_errors:
> paperless-webserver-1  |          ^^^^^^^^^^^^^^^^^^^^^^^^^
> paperless-webserver-1  |   File "/usr/local/lib/python3.12/site-packages/django/db/utils.py", line 91, in __exit__

### Assistant
> Same error. The DB volume did **not** get reset, or the webserver and DB are still using mismatched passwords.
> 
> We’re going to stop being cute and verify the actual state.
> 
> ## 1. Stop the Paperless stack
> 
> ```bash
> cd /srv/qios/stacks/paperless
> docker compose down
> ```
> 
> ## 2. See the actual Paperless volumes
> 
> ```bash
> docker volume ls | grep paperless
> ```
> 
> You should see something like:
> 
> `paperless_paperless_pgdata`
> 
> ## 3. Remove the Paperless volumes
> 
> Since this is fresh and no docs are imported yet:
> 
> ```bash
> docker volume rm paperless_paperless_pgdata paperless_paperless_redisdata
> ```
> 
> If it says “volume is in use,” run:
> 
> ```bash
> docker compose down --volumes --remove-orphans
> ```
> 
> Then check again:
> 
> ```bash
> docker volume ls | grep paperless
> ```
> 
> If any Paperless volumes remain, remove them manually.
> 
> ## 4. Check the passwords match
> 
> Show the relevant config without secrets:
> 
> ```bash
> grep -n "POSTGRES_PASSWORD\|PAPERLESS_DBPASS\|PAPERLESS_DB" docker-compose.yml docker-compose.env
> ```
> 
> Here is the issue: your compose file sets:
> 
> `POSTGRES_PASSWORD=...`
> 
> But Paperless may not be explicitly told the DB password unless `PAPERLESS_DBPASS` is set.
> 
> So add this to `docker-compose.env`:
> 
> ```env
> PAPERLESS_DBPASS=paperless_local_change_me
> ```
> 
> And make sure your compose Postgres password is the same:
> 
> ```yaml
> POSTGRES_PASSWORD: paperless_local_change_me
> ```
> 
> For right now, do **not** use the admin password as the DB password. Keep DB boring:
> 
> `paperless_local_change_me`
> 
> Edit:
> 
> ```bash
> nano docker-compose.env
> ```
> 
> Make sure it includes:
> 
> ```env
> PAPERLESS_DBPASS=paperless_local_change_me
> ```
> 
> Edit:
> 
> ```bash
> nano docker-compose.yml
> ```
> 
> Make sure DB has:
> 
> ```yaml
> POSTGRES_PASSWORD: paperless_local_change_me
> ```
> 
> ## 5. Validate config
> 
> ```bash
> docker compose config | grep -E "POSTGRES_PASSWORD|PAPERLESS_DBPASS|PAPERLESS_DBHOST|PAPERLESS_ADMIN_USER"
> ```
> 
> You want to see:
> 
> `POSTGRES_PASSWORD: paperless_local_change_me`  
> `PAPERLESS_DBPASS: paperless_local_change_me`  
> `PAPERLESS_DBHOST: paperless-db`
> 
> ## 6. Start fresh
> 
> ```bash
> docker compose up -d
> docker compose logs -f paperless-webserver
> ```
> 
> If the password mismatch was the only problem, it should now get past migrations.
> 
> ## If it still fails
> 
> Run this and paste only the output:
> 
> ```bash
> cd /srv/qios/stacks/paperless
> 
> echo "=== compose ps ==="
> docker compose ps
> 
> echo "=== volumes ==="
> docker volume ls | grep paperless
> 
> echo "=== password-related config ==="
> docker compose config | grep -E "POSTGRES_PASSWORD|PAPERLESS_DBPASS|PAPERLESS_DBHOST|PAPERLESS_DBUSER|PAPERLESS_DBNAME"
> 
> echo "=== db logs ==="
> docker compose logs --tail=80 paperless-db
> 
> echo "=== web logs last 60 ==="
> docker compose logs --tail=60 paperless-webserver
> ```
> 
> The fix is not reinstalling. It’s one of two things:
> 
> 1. **Old Postgres volume still has old password**
> 2. **Paperless webserver has no/mismatched `PAPERLESS_DBPASS`**
> 
> Right now I’m betting on #2 plus old volume persistence. Nasty little Docker goblin, but very fixable.

### User
> how can i get codex to do this, cause i got other stuff i got to do.

### Assistant
> Absolutely. Give Codex one tight mission: **fix Paperless Docker on qiserver, don’t redesign the stack, don’t touch unrelated services.**
> 
> Paste this into Codex:
> 
> ---
> 
> ### Codex task: Fix Paperless Docker stack on qiserver
> 
> We are on Ubuntu server `qiserver`.
> 
> Paperless stack path:
> 
> `/srv/qios/stacks/paperless`
> 
> Paperless data path:
> 
> `/srv/qios/data/paperless`
> 
> Current issue:
> 
> Paperless starts, Redis and Postgres start, but `paperless-webserver` fails during migrations with:
> 
> `FATAL: password authentication failed for user "paperless"`
> 
> Likely cause:
> 
> The Postgres Docker volume was initialized with one password, then compose/env password changed. Also `PAPERLESS_DBPASS` may not be explicitly set to match `POSTGRES_PASSWORD`.
> 
> Goal:
> 
> Fix the Paperless stack so it starts cleanly at:
> 
> `http://100.121.111.106:8010`
> 
> Do not touch existing running services except Paperless.
> 
> Existing important services that must not be broken:
> 
> - `homepage`
> - `portainer`
> - `open-webui`
> - `neo4j`
> 
> Required actions:
> 
> 1. Go to:
> 
> `/srv/qios/stacks/paperless`
> 
> 2. Inspect:
> 
> `docker-compose.yml`  
> `docker-compose.env`  
> Paperless Docker volumes  
> Paperless container logs
> 
> 3. Ensure the compose stack uses:
> 
> - `paperless-broker` Redis
> - `paperless-db` Postgres 16
> - `paperless-webserver` Paperless-ngx latest
> - port mapping `8010:8000`
> - bind mounts:
>   - `/srv/qios/data/paperless/data:/usr/src/paperless/data`
>   - `/srv/qios/data/paperless/media:/usr/src/paperless/media`
>   - `/srv/qios/data/paperless/export:/usr/src/paperless/export`
>   - `/srv/qios/data/paperless/consume:/usr/src/paperless/consume`
>   - `/srv/qios/data/paperless/trash:/usr/src/paperless/trash`
> 
> 4. Make sure DB credentials match exactly:
> 
> In Postgres service:
> 
> `POSTGRES_DB=paperless`  
> `POSTGRES_USER=paperless`  
> `POSTGRES_PASSWORD=paperless_local_change_me`
> 
> In Paperless env:
> 
> `PAPERLESS_DBHOST=paperless-db`  
> `PAPERLESS_DBUSER=paperless`  
> `PAPERLESS_DBPASS=paperless_local_change_me`  
> `PAPERLESS_DBNAME=paperless`
> 
> 5. Because this is a fresh install with no documents imported, safely reset only the Paperless volumes if needed:
> 
> - stop Paperless stack
> - remove Paperless Postgres/Redis volumes only
> - do not remove unrelated Docker volumes
> - restart Paperless stack
> 
> 6. Validate with:
> 
> `docker compose config`  
> `docker compose up -d`  
> `docker compose ps`  
> `docker compose logs --tail=100 paperless-webserver`
> 
> 7. Success criteria:
> 
> - `paperless-webserver` becomes healthy or stays running without migration/password errors
> - `http://100.121.111.106:8010` loads Paperless
> - Redis and Postgres containers are running
> - no password authentication failure remains
> - no unrelated containers are stopped or modified
> 
> 8. After Paperless is healthy, update QiAccess dashboard if needed:
> 
> File likely at:
> 
> `/srv/qios/stacks/_qiaccess_start/config/services.yaml`
> 
> Set Mail Intake href to:
> 
> `http://100.121.111.106:8010`
> 
> Then restart only QiAccess/homepage stack:
> 
> `cd /srv/qios/stacks/_qiaccess_start && docker compose restart`
> 
> 9. Report back with:
> 
> - final `docker compose ps`
> - Paperless URL
> - whether QiAccess link was updated
> - any files changed
> - any volumes removed
> - any unresolved issue
> 
> Do not rotate secrets yet unless Paperless is confirmed healthy. Do not install extra tools. Do not touch Portainer, Open WebUI, Neo4j, or Homepage except restarting Homepage only if updating its config.
> 
> ---
> 
> That’s the clean handoff. Codex should be able to run this without dragging you into password goblin hell.
