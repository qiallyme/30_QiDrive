---
layout: page
title: "Local LLM Setup Guide"
slug: "local_llm_setup_guide"
created_at: "2026-05-29 14:33:44"
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
date: 2026-05-29
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6a19e9f8-f3bc-83ea-a734-cf3bf18a0425"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Local LLM Setup Guide

## Overview
- **Date**: 2026-05-29 14:33:44
- **Conversation ID**: `6a19e9f8-f3bc-83ea-a734-cf3bf18a0425`
- **Source**: `Chat-Export-28513-2026/conversations-008.json`

## Chat History

### User
> hey i keep getting stuck on codex credit limits, and i have like 40gb available on my main pc, can we use another local llm that is really good too thats fast too.

### Assistant
> Yes — we can absolutely route around Codex limits. I’m going to separate this into: best local models for coding, what fits in 40GB free disk, and the fastest “actually usable” setup for your PC.

### Assistant
> Yes. **Codex should become “premium burst mode,” not your daily driver.** For your setup, use a **local coding model through Ollama** for routine edits, scaffolding, refactors, and repo cleanup — then use Codex only when you need heavy reasoning or final polish.
> 
> Here’s the clean stack.
> 
> ## Best local coding models to try
> 
> ### 1. **Qwen3-Coder / Qwen3-Coder-Next**
> This is the first one I’d try for your workflow. It is coding-focused, agent-friendly, and available through Ollama. Ollama describes Qwen3-Coder as trained heavily on code and boosted with execution-driven reinforcement learning for real-world coding tasks. citeturn204442search0
> 
> Install:
> 
> ```powershell
> ollama pull qwen3-coder
> ollama run qwen3-coder
> ```
> 
> Or try:
> 
> ```powershell
> ollama pull qwen3-coder-next
> ollama run qwen3-coder-next
> ```
> 
> ### 2. **DeepSeek-Coder-V2 Lite**
> This is a strong fallback. The Lite model is available on Ollama, and DeepSeek describes Coder-V2 as an open-source MoE code model trained on a large multi-source code corpus. citeturn204442search1
> 
> Install:
> 
> ```powershell
> ollama pull deepseek-coder-v2:lite
> ollama run deepseek-coder-v2:lite
> ```
> 
> Ollama lists the DeepSeek-Coder-V2 latest model around **8.9GB** with a large context window, so it is reasonable for your 40GB storage situation. citeturn204442search15
> 
> ### 3. **DeepSeek-Coder 6.7B**
> This is lighter, older, but probably faster. Good for quick edits, small scripts, and “fix this Python file” work. Ollama lists DeepSeek Coder in 1.3B, 6.7B, and 33B sizes. citeturn204442search3
> 
> ```powershell
> ollama pull deepseek-coder:6.7b
> ollama run deepseek-coder:6.7b
> ```
> 
> ## Reality check: 40GB free disk is okay, but RAM/VRAM decides speed
> 
> Disk space only tells us whether you can **store** the model. Speed depends mostly on:
> 
> - RAM
> - GPU VRAM
> - CPU
> - whether Ollama can offload layers to GPU
> 
> With 40GB free, don’t download a buffet of models. That’s how we make another digital junk drawer. Pick **two**:
> 
> 1. `qwen3-coder` or `qwen3-coder-next`
> 2. `deepseek-coder-v2:lite`
> 
> Then test.
> 
> ## The setup I’d use for you
> 
> Use:
> 
> - **Ollama** as the local model runner
> - **Continue.dev** inside VS Code / Cursor-style IDE for chat/editing
> - Optional: **Open WebUI** for a browser chat UI
> - Keep **Codex** only for “finish this whole feature” or “audit this architecture” moments
> 
> You already have Ollama working through qiserver, but for the main PC we want a **local direct lane**:
> 
> ```powershell
> ollama list
> ollama pull qwen3-coder
> ollama pull deepseek-coder-v2:lite
> ```
> 
> Then test each with:
> 
> ```powershell
> ollama run qwen3-coder
> ```
> 
> Prompt:
> 
> ```text
> You are coding inside C:\QiLabs\60_QiApps\_qilife. Review the project structure I paste next and suggest the next 3 implementation steps only. Do not rewrite the app yet.
> ```
> 
> ## My recommendation
> 
> Start with this:
> 
> ```powershell
> ollama pull qwen3-coder
> ollama pull deepseek-coder-v2:lite
> ```
> 
> Then wire one of them into your IDE as the **cheap local worker**.
> 
> Use this division:
> 
> | Task | Model |
> |---|---|
> | Small code fixes | DeepSeek-Coder-V2 Lite |
> | App scaffolding | Qwen3-Coder |
> | Repo cleanup | Qwen3-Coder |
> | Explaining errors | DeepSeek-Coder-V2 Lite |
> | Big architecture decisions | Me / Codex |
> | Final implementation sprint | Codex when credits allow |
> 
> ## Important: don’t expect local to fully replace Codex
> 
> Local models are good. They are not magic. They will absolutely mess up files if you let them run wild.
> 
> The winning workflow is:
> 
> 1. **You give me the architecture / prompt.**
> 2. **Local model does small bounded edits.**
> 3. **Git diff after every change.**
> 4. **Codex gets used only for hard mode.**
> 
> That keeps your credits alive and avoids the “AI touched 47 files and now the app is haunted” problem.
> 
> For QiLife specifically, use local LLM for:
> 
> - schema drafts
> - SQL migration drafts
> - component stubs
> - README updates
> - file cleanup
> - route scaffolding
> - tests
> - boring glue code
> 
> Use Codex for:
> 
> - full feature implementation
> - database integrity
> - auth/security logic
> - refactoring across many files
> - final review before server deploy
> 
> Best next move: install/pull **Qwen3-Coder** and **DeepSeek-Coder-V2 Lite**, then we make your IDE button/command so you’re not living in PowerShell like it’s 2007.
