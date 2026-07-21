---
layout: page
title: "Qiserver UI Setup"
slug: "qiserver_ui_setup"
created_at: "2026-04-20 13:06:01"
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
date: 2026-04-20
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69e66af0-cfd8-83ea-863e-7182e3a0ca81"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Qiserver UI Setup

## Overview
- **Date**: 2026-04-20 13:06:01
- **Conversation ID**: `69e66af0-cfd8-83ea-863e-7182e3a0ca81`
- **Source**: `Chat-Export-28513-2026/conversations-006.json`

## Chat History

### User
> ok, before we do anything else, i need to make sure qiserver is up and running and i would like to be able to control it from this pc in a simple ui  if possible.

### Assistant
> I can’t live-check qiserver from here unless you paste me its current output or give me a connected source, so I’m going straight to the practical path: verify it fast, then put a clean web UI on top so this PC can control it without SSH gymnastics.

### Assistant
> You don’t need a whole desktop-over-the-network setup for this. The clean answer is: **Cockpit for server control, Portainer for Docker control, both reached over Tailscale**.

### Assistant
> Yes. And the simplest sane setup is:
> 
> **Cockpit = server/admin UI**  
> **Portainer = Docker/container UI**  
> **Tailscale = secure access path from this PC**  
> 
> That gives you a clean browser-based control plane without turning qiserver into some bloated remote-desktop mess. Cockpit is the web admin console for Linux, typically on port **9090**, and on Ubuntu the Cockpit project recommends installing the newer package from **backports**. Portainer’s UI is exposed on **9443** and their Linux Docker install uses a persistent `portainer_data` volume plus the Docker socket mount. citeturn684749search1turn736475view1turn736475view0
> 
> Run this on **qiserver** first to check what is alive right now:
> 
> ```bash
> echo "=== BASIC ==="
> hostname
> uptime
> tailscale status || true
> 
> echo
> echo "=== SERVICES ==="
> systemctl is-active docker || true
> systemctl is-active ollama || true
> systemctl is-active cockpit.socket || true
> 
> echo
> echo "=== DOCKER ==="
> docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}' || true
> 
> echo
> echo "=== LISTENING PORTS ==="
> ss -tulpn | grep -E ':(22|80|443|3000|9090|9443|11434)\b' || true
> ```
> 
> If Cockpit is **not** installed, install it like this:
> 
> ```bash
> . /etc/os-release
> sudo apt update
> sudo apt install -y -t ${VERSION_CODENAME}-backports cockpit
> sudo systemctl enable --now cockpit.socket
> ```
> 
> Cockpit’s docs say it normally listens on **9090** and you log in with your normal system user account. citeturn684749search1turn736475view1
> 
> If Docker is already on qiserver, install Portainer like this:
> 
> ```bash
> docker volume create portainer_data
> 
> docker run -d \
>   -p 8000:8000 \
>   -p 9443:9443 \
>   --name portainer \
>   --restart=always \
>   -v /var/run/docker.sock:/var/run/docker.sock \
>   -v portainer_data:/data \
>   portainer/portainer-ce:sts
> ```
> 
> That matches Portainer’s current Linux Docker install pattern, and the docs note the UI is on **9443**. citeturn736475view0
> 
> Then from **this PC**, assuming both machines are on your tailnet, open:
> 
> ```text
> https://qiserver:9090
> https://qiserver:9443
> ```
> 
> If MagicDNS name resolution is flaky, use the Tailscale IP instead:
> 
> ```text
> https://100.x.x.x:9090
> https://100.x.x.x:9443
> ```
> 
> You usually do **not** need Tailscale Serve just to access these from another one of your own devices on the tailnet. Serve is for publishing a local service *within the tailnet via Tailscale’s service layer*, and its CLI changed in newer versions, so I would skip that extra layer unless you actually need it. citeturn736475view2
> 
> My blunt recommendation:
> 
> 1. **Install Cockpit now**
> 2. **Install Portainer now**
> 3. **Do not bother with full Ubuntu remote desktop for admin**
> 4. Use desktop GUI only when you are physically on qiserver; use browser UI from this PC for everything else
> 
> If you want, paste me the output of that status block and I’ll tell you exactly what’s up, what’s broken, and the next command.

### User
> Learn more about enabling ESM Apps service at https://ubuntu.com/esm

> 

> Last login: Sat Apr 18 23:54:50 2026 from 192.168.0.74

> 

> QISERVER → Runbook: /srv/qios/docs/000_RUN_ME_FIRST.md

> QISERVER → Status: qs

> QISERVER → UI: https://qiserver-1.cerberus-sirius.ts.net

> 

> qiadmin@qiserver:~$ echo "=== BASIC ==="

> hostname

> uptime

> tailscale status || true

> 

> echo

> echo "=== SERVICES ==="

> systemctl is-active docker || true

> systemctl is-active ollama || true

> systemctl is-active cockpit.socket || true

> 

> echo

> echo "=== DOCKER ==="

> docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}' || true

> 

> echo

> echo "=== LISTENING PORTS ==="

> ss -tulpn | grep -E ':(22|80|443|3000|9090|9443|11434)\b' || true

> === BASIC ===

> qiserver

>  13:20:00 up 10:21,  2 users,  load average: 0.00, 0.00, 0.00

> 100.121.111.106  qiserver-1            qiserver-1.cerberus-sirius.ts.net  linux    -                  

> 100.66.216.97    iphone-13-pro-max-1   crice4485@                         iOS      offline, last seen 26d ago

> 100.93.140.115   qigate2               crice4485@                         windows  offline, last seen 10d ago

> 100.67.25.114    qione-docker-desktop  crice4485@                         linux    -                  

> 100.115.240.56   qione                 crice4485@                         windows  active; direct 192.168.0.74:41641, tx 23020 rx 21180

> 

> === SERVICES ===

> active

> active

> inactive

> 

> === DOCKER ===

> NAMES        STATUS                  PORTS

> open-webui   Up 27 hours (healthy)   127.0.0.1:3000->8080/tcp

> neo4j        Up 27 hours             127.0.0.1:7474->7474/tcp, 7473/tcp, 127.0.0.1:7687->7687/tcp

> 

> === LISTENING PORTS ===

> tcp   LISTEN 0      4096               100.121.111.106:443        0.0.0.0:*

> tcp   LISTEN 0      4096                     127.0.0.1:3000       0.0.0.0:*

> tcp   LISTEN 0      4096                       0.0.0.0:22         0.0.0.0:*

> tcp   LISTEN 0      4096   [fd7a:115c:a1e0::8532:6f6a]:443           [::]:*

> tcp   LISTEN 0      4096                          [::]:22            [::]:*

> tcp   LISTEN 0      4096                             *:11434            *:*

> qiadmin@qiserver:~$

### Assistant
> You gave me enough to diagnose it. The box is up, Tailscale is up, Docker is up, Ollama is up. The missing piece is the admin UI layer.

### Assistant
> It’s up.
> 
> What your output says:
> 
> - **qiserver is online and healthy enough**: uptime is fine, load is basically zero.
> - **Tailscale is working** and your Windows box `qione` is actively connected.
> - **Docker is running**.
> - **Ollama is running** and listening on `11434`.
> - **Open WebUI is running** on `127.0.0.1:3000`.
> - **Cockpit is not running**.
> - **Portainer is not installed/running**.
> 
> So the problem is not “is qiserver alive?”  
> The problem is **you do not yet have the simple admin UI installed**.
> 
> Your current `https://qiserver-1.cerberus-sirius.ts.net` UI is almost certainly your existing proxied app, not a server control panel.
> 
> ### The clean setup
> Do this:
> 
> - **Cockpit** for server control
> - **Portainer** for Docker control
> 
> Cockpit is meant to be a web-based Linux admin interface, normally reached on **port 9090**, and you log in with your normal system account. It uses HTTPS on that same port by default. citeturn551579view0turn551579view3
> 
> Portainer’s Docker install exposes its UI on **9443** and the official Linux Docker install uses a `portainer_data` volume plus the Docker socket mount. Portainer also notes it uses a self-signed cert by default on 9443. citeturn551579view1
> 
> Tailscale lets you connect to services on another device using the **device name or Tailscale IP plus the port**, so you do not need to overcomplicate this with extra routing just to access these from your Windows PC. citeturn551579view2
> 
> ### Do this now on qiserver
> 
> Install Cockpit:
> 
> ```bash
> sudo apt update
> sudo apt install -y cockpit
> sudo systemctl enable --now cockpit.socket
> systemctl is-active cockpit.socket
> ss -tulpn | grep ':9090\b' || true
> ```
> 
> Install Portainer:
> 
> ```bash
> docker volume create portainer_data
> 
> docker run -d \
>   -p 8000:8000 \
>   -p 9443:9443 \
>   --name portainer \
>   --restart=always \
>   -v /var/run/docker.sock:/var/run/docker.sock \
>   -v portainer_data:/data \
>   portainer/portainer-ce:sts
> 
> docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
> ```
> 
> ### Then open these from this PC
> 
> Use either the Tailscale hostname or the Tailscale IP:
> 
> ```text
> https://qiserver-1.cerberus-sirius.ts.net:9090
> https://qiserver-1.cerberus-sirius.ts.net:9443
> ```
> 
> or
> 
> ```text
> https://100.121.111.106:9090
> https://100.121.111.106:9443
> ```
> 
> ### What each UI gives you
> 
> **Cockpit**
> - start/stop services
> - logs
> - disk usage
> - updates
> - terminal in browser
> - general server admin
> 
> **Portainer**
> - containers
> - images
> - volumes
> - stacks
> - restart/redeploy Docker stuff without CLI
> 
> ### My recommendation
> Don’t mess with full remote desktop for this. Waste of time.
> 
> Your best control model is:
> 
> - **Cockpit** = server brain
> - **Portainer** = Docker brain
> - **Open WebUI** = app you already use
> 
> That is the simple UI path.
> 
> After you run the two install blocks, paste me the output of:
> 
> ```bash
> systemctl is-active cockpit.socket
> docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
> ss -tulpn | grep -E ':(9090|9443)\b' || true
> ```
> 
> and I’ll tell you if it’s fully good or what still needs fixing.
