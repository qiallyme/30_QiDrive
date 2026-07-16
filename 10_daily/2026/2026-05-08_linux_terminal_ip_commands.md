---
layout: page
title: "Linux terminal IP commands"
slug: "linux_terminal_ip_commands"
created_at: "2026-05-08 05:28:01"
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
uid: "69fdba9c-cf30-83ea-8de4-a11c76cf72a2"
canonical_ref: ""
---

# Linux terminal IP commands

## Overview
- **Date**: 2026-05-08 05:28:01
- **Conversation ID**: `69fdba9c-cf30-83ea-8de4-a11c76cf72a2`
- **Source**: `Chat-Export-28513-2026/conversations-006.json`

## Chat History

### User
> Quickly I need comman on Linux to pull up terminal and get up addresses

### Assistant
> Open a terminal:
> 
> Ubuntu/Linux desktop: **Ctrl + Alt + T**
> 
> Then run:
> 
> `ip addr`
> 
> Cleaner version showing just IP addresses:
> 
> `hostname -I`
> 
> For network devices + IPs:
> 
> `ip -br addr`
> 
> For public internet IP:
> 
> `curl ifconfig.me`
> 
> Tiny correction: it’s **IP addresses**, not “up addresses” — voice dictation did you dirty.

### User
> Nvm I just need the ssh for my widwrver

### Assistant
> Use:
> 
> `ssh username@server-ip`
> 
> Example:
> 
> `ssh cody@192.168.1.25`
> 
> If it’s your **qiserver** by Tailscale name, try:
> 
> `ssh cody@qiserver`
> 
> or:
> 
> `ssh cody@qiserver-1`
> 
> If it’s Windows → Linux server from PowerShell:
> 
> `ssh cody@192.168.x.x`
> 
> To find the IP on the server:
> 
> `hostname -I`
> 
> To find Tailscale IP/name:
> 
> `tailscale status`
> 
> Most likely command for you:
> 
> `ssh cody@qiserver-1.cerberus-sirius.ts.net`
