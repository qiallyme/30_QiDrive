---
layout: page
title: "Move window with keyboard"
slug: "move_window_with_keyboard"
created_at: "2026-04-21 04:38:27"
updated_at: "2026-04-21 04:38:27"
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
date: 2026-04-21
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "69e74588-7b04-83ea-b4ab-551b4d569572"
canonical_ref: ""
---

# Move window with keyboard

## Overview
- **Date**: 2026-04-21 04:38:27
- **Conversation ID**: `69e74588-7b04-83ea-b4ab-551b4d569572`
- **Source**: `Chat-Export-28513-2026/conversations-006.json`

## Chat History

### User
> how do i use the keyboard to move over a window that is on a display i cant see.

### Assistant
> On Windows, use this sequence:
> 
> 1. Click the app in the taskbar so that window is active.
> 2. Press `Alt + Space`
> 3. Press `M`
> 4. Press any arrow key once
> 5. Move your mouse, or keep using the arrow keys, until the window comes back onto the visible screen
> 6. Press `Enter`
> 
> Faster option if Windows still thinks the other monitor exists:
> 
> - `Win + Shift + Left Arrow`
> - or `Win + Shift + Right Arrow`
> 
> That throws the active window to another display.
> 
> If it still won’t show:
> 
> - Select the app on the taskbar
> - Press `Alt + Tab` until it’s active
> - Then press `Win + Up Arrow` to maximize it
> 
> Best order to try:
> `Win + Shift + Arrow` first, then `Alt + Space`, `M`, arrow key, move mouse.
> 
> If you want, I can give you the exact Mac version too.

### Assistant
> I see the YAML files came through.
> 
> You uploaded:
> - `bookmarks.yaml`
> - `docker.yaml`
> - `kubernetes.yaml`
> - `proxmox.yaml`
> - `services.yaml`
> - `settings.yaml`
> - `widgets.yaml`
> 
> These look like homepage / dashboard config files. I can review them, clean them up, merge them, explain what each one does, or help you wire them into your setup.

### User
> yes, give me copy and paste ready code for replacing these files with what you believe they should be.

### Assistant
> I’m opening the YAMLs and looking for structural problems, missing references, and anything that will break Homepage. Then I’ll give you replacement files you can paste straight in.

### Assistant
> The good news: these files are basically stock placeholders, so there’s no hidden complexity. I’m turning them into a clean baseline that should boot safely without forcing broken Docker/Proxmox/Kubernetes integrations.

### Assistant
> Yep. I rebuilt these into a cleaner, sane baseline.
> 
> What I changed:
> - turned the stock placeholder files into an actual starter dashboard structure
> - kept Docker enabled in a normal way
> - left Proxmox and Kubernetes inert on purpose so you do not fake integrations with bogus endpoints/tokens
> - added a real `settings.yaml`, grouped `services.yaml`, useful `bookmarks.yaml`, and practical header widgets
> 
> Homepage splits config across YAML files like `services.yaml`, `widgets.yaml`, `docker.yaml`, and `proxmox.yaml`, and Docker can auto-discover labeled containers once Docker is configured. Proxmox connections live in `proxmox.yaml`, and any configured Proxmox node name has to match the `proxmoxNode` used later in service entries. citeturn509610search0turn509610search3turn509610search4turn509610search5turn625691search5
> 
> I also generated the files for you here:
> [homepage_replacements.zip](sandbox:/mnt/data/homepage_replacements.zip)
> [homepage_replacements folder](sandbox:/mnt/data/homepage_replacements)
> 
> Paste this from inside your mounted Homepage config directory:
> 
> ```bash
> TS=$(date +%Y%m%d-%H%M%S)
> mkdir -p "_backup_$TS"
> cp -v ./*.yaml "_backup_$TS"/
> 
> cat > settings.yaml <<'YAML'
> ---
> title: QiAccess
> description: One door to Cody's stack
> language: en
> theme: dark
> color: slate
> target: _self
> headerStyle: boxedWidgets
> bookmarksStyle: icons
> useEqualHeights: true
> groupsInitiallyCollapsed: false
> searchDescriptions: true
> hideInternetSearch: false
> showSearchSuggestions: true
> 
> layout:
>   Core Services:
>     style: row
>     columns: 3
>   AI & Automation:
>     style: row
>     columns: 3
>   External Control:
>     style: row
>     columns: 3
>   Admin Bookmarks:
>     style: row
>     columns: 6
>   Docs & References:
>     style: row
>     columns: 6
> YAML
> 
> cat > bookmarks.yaml <<'YAML'
> ---
> - Admin Bookmarks:
>     - GitHub:
>         - abbr: GH
>           href: https://github.com/
>     - Cloudflare:
>         - abbr: CF
>           href: https://dash.cloudflare.com/
>     - Supabase:
>         - abbr: SB
>           href: https://supabase.com/dashboard
>     - Railway:
>         - abbr: RW
>           href: https://railway.com/
>     - Tailscale Admin:
>         - abbr: TS
>           href: https://login.tailscale.com/admin/machines
>     - Google Drive:
>         - abbr: GD
>           href: https://drive.google.com/
> 
> - Docs & References:
>     - Homepage Docs:
>         - abbr: HP
>           href: https://gethomepage.dev/
>     - Docker Docs:
>         - abbr: DK
>           href: https://docs.docker.com/
>     - Tailscale Docs:
>         - abbr: TL
>           href: https://tailscale.com/kb
>     - Ollama Docs:
>         - abbr: OL
>           href: https://ollama.com/library
>     - Portainer Docs:
>         - abbr: PT
>           href: https://docs.portainer.io/
> YAML
> 
> cat > services.yaml <<'YAML'
> ---
> - Core Services:
>     - Homepage:
>         href: https://qiserver-1.cerberus-sirius.ts.net
>         description: Main dashboard entry point
>     - Cockpit:
>         href: https://qiserver-1.cerberus-sirius.ts.net:9090
>         description: Server administration
>     - Portainer:
>         href: https://qiserver-1.cerberus-sirius.ts.net:9443
>         description: Docker management
> 
> - AI & Automation:
>     - Ollama API:
>         href: http://qiserver-1.cerberus-sirius.ts.net:11434
>         description: Local LLM endpoint
> 
> - External Control:
>     - Cloudflare:
>         href: https://dash.cloudflare.com/
>         description: DNS, tunnels, and edge control
>     - GitHub:
>         href: https://github.com/
>         description: Repos and code
>     - Supabase:
>         href: https://supabase.com/dashboard
>         description: Database and auth control plane
> YAML
> 
> cat > widgets.yaml <<'YAML'
> ---
> - resources:
>     cpu: true
>     memory: true
>     disk: /
>     uptime: true
>     refresh: 5000
> 
> - search:
>     provider: duckduckgo
>     target: _blank
> 
> - openmeteo:
>     label: Evansville
>     latitude: 37.9748
>     longitude: -87.5558
>     units: imperial
>     cache: 5
> 
> - datetime:
>     text_size: xl
>     format:
>       dateStyle: short
>       timeStyle: short
>       hour12: true
> YAML
> 
> cat > docker.yaml <<'YAML'
> ---
> # Requires /var/run/docker.sock to be mounted into the Homepage container.
> local:
>   socket: /var/run/docker.sock
> YAML
> 
> cat > proxmox.yaml <<'YAML'
> ---
> # Fill this in only when you are ready to connect Homepage to Proxmox.
> {}
> YAML
> 
> cat > kubernetes.yaml <<'YAML'
> ---
> # Fill this in only when you are ready to connect Homepage to Kubernetes.
> {}
> YAML
> 
> echo "Done."
> ```
> 
> Then refresh Homepage. The official docs note that `settings.yaml` changes require regenerating the static HTML via the refresh icon in the bottom-right; info widgets like `resources`, `search`, `openmeteo`, and `datetime` are defined in `widgets.yaml`. citeturn625691search6turn625691search3turn625691search0turn625691search1turn625691search2
> 
> One important caveat: I used the qiserver Tailnet URL you showed earlier and assumed Cockpit is on `9090`, Portainer on `9443`, and Ollama on `11434`. If any of those are wrong, change only the `href` values in `services.yaml`.
> 
> Next move after this: send me your `docker-compose.yml` for Homepage and I’ll tighten this so Docker auto-discovery and icons work cleanly instead of just giving you a decent baseline.
