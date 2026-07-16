---
layout: page
title: "Notion watcher app"
slug: "notion_watcher_app"
created_at: "2025-09-29 03:29:48"
updated_at: "2025-09-29 03:29:48"
status: active
tags:
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-001.json"
template_key: master-template
date: 2025-09-29
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "68da437b-20c0-8324-9819-3693b3ffe740"
canonical_ref: ""
---

# Notion watcher app

## Overview
- **Date**: 2025-09-29 03:29:48
- **Conversation ID**: `68da437b-20c0-8324-9819-3693b3ffe740`
- **Source**: `Chat-Export-28513-2026/conversations-001.json`

## Chat History

### User
> create a mini app that will automatically run on startup and watch a folder of my choice so it need persistent settings what is will do is when i scan a file into that folder it will read the title and come of the content to get context, then it will create a notion page

### Assistant
> Built. Open the canvas and copy `notion_watcher.py`.
> 
> Setup, fast:
> 
> 1) Notion prep  
> - Create an internal integration. Copy the token (`secret_…`).  
> - Create a database. Share it with the integration. Copy the database ID.
> 
> 2) Install deps
> ```
> pip install watchdog requests PyPDF2 python-docx pillow pytesseract pdf2image
> ```
> Tesseract is already on your PATH. For PDF OCR fallback, install Poppler if you want it.
> 
> 3) First-run config
> ```
> python notion_watcher.py --init
> ```
> Enter: watch folder path, Notion token, database ID.
> 
> 4) Run
> ```
> python notion_watcher.py
> ```
> Drop a scanned file into the folder. It will create a Notion page titled from the filename and include a snippet plus source path. Supported: txt, pdf, docx, png, jpg. Ledger prevents duplicates. Config and ledger live in `~/.qi_watcher/`.
> 
> Startup options:
> 
> Windows (Task Scheduler)
> ```
> schtasks /Create /TN NotionWatcher /TR "python C:\path\to\notion_watcher.py" /SC ONLOGON /RL HIGHEST
> ```
> 
> Linux (systemd, user service `~/.config/systemd/user/notion-watcher.service`)
> ```
> [Unit]
> Description=Notion Watcher
> [Service]
> ExecStart=/usr/bin/python3 /PATH/TO/notion_watcher.py
> Restart=always
> [Install]
> WantedBy=default.target
> ```
> Then:
> ```
> systemctl --user enable --now notion-watcher
> ```
> 
> macOS (LaunchAgent `~/Library/LaunchAgents/me.qially.notionwatcher.plist`)
> ```xml
> <?xml version="1.0" encoding="UTF-8"?>
> <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
> <plist version="1.0"><dict>
>   <key>Label</key><string>me.qially.notionwatcher</string>
>   <key>ProgramArguments</key><array>
>     <string>/usr/bin/python3</string>
>     <string>/PATH/TO/notion_watcher.py</string>
>   </array>
>   <key>RunAtLoad</key><true/>
>   <key>KeepAlive</key><true/>
>   <key>WorkingDirectory</key><string>/PATH/TO</string>
>   <key>StandardOutPath</key><string>/tmp/notion_watcher.out</string>
>   <key>StandardErrorPath</key><string>/tmp/notion_watcher.err</string>
> </dict></plist>
> ```
> Then:
> ```
> launchctl load ~/Library/LaunchAgents/me.qially.notionwatcher.plist
> ```
> 
> Notes:
> - Uses only the database’s default `Name` property. Content goes in page blocks to avoid schema issues.  
> - Test a file without watching: `python notion_watcher.py --once /path/to/file.pdf`.  
> - To change settings, edit `~/.qi_watcher/config.json` and restart.
> 
> Upgrade path (when ready):
> - Add a Notion “Files” property and attach cloud links to the original file.  
> - Add tag routing via filename patterns.  
> - Enable recursive watching and MIME-type rules.
