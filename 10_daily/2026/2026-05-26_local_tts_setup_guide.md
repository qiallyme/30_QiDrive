---
layout: page
title: "Local TTS Setup Guide"
slug: "local_tts_setup_guide"
created_at: "2026-05-26 08:21:08"
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
uid: "6a159e2f-f234-83ea-842b-2e94de71fa10"
canonical_ref: ""
type: event
event_type: ""
people: []
significance: normal
canonical: false
timeline_include: false
timeline_status: unreviewed
---

# Local TTS Setup Guide

## Overview
- **Date**: 2026-05-26 08:21:08
- **Conversation ID**: `6a159e2f-f234-83ea-842b-2e94de71fa10`
- **Source**: `Chat-Export-28513-2026/conversations-008.json`

## Chat History

### User
> what do i tell codex in order to get something like elevenlabs up and running locally so i dont keep running out of credit. s

### Assistant
> Yes — don’t burn ElevenLabs credits for routine narration/testing. I’ll give you a Codex-ready prompt that sets up a local TTS service, with sane defaults and a clean fallback path instead of some “research project from hell.”

### Assistant
> Tell Codex this:
> 
> ```text
> I want to add a local text-to-speech service to this server/app so I can stop relying on ElevenLabs credits for normal narration/testing.
> 
> Goal:
> Build a local TTS stack that runs on my server, exposes a simple HTTP API, and can generate audio files from text. Prioritize easy setup, low cost, and reliability over perfect ElevenLabs-level voice quality.
> 
> Preferred stack:
> 1. Primary engine: Kokoro TTS
>    - Use this as the default local voice engine.
>    - It should run locally, preferably CPU-capable first.
>    - It should expose an API endpoint like POST /tts.
>    - Input: text, optional voice, optional speed, optional output format.
>    - Output: saved .wav or .mp3 file and JSON with file path / URL.
> 
> 2. Optional fallback/lightweight engine: Piper TTS
>    - Only add Piper if it is easy and does not complicate the setup.
>    - Use it as a “fast/basic/offline fallback” option.
> 
> Do NOT make this a huge experimental AI lab. I need a working MVP.
> 
> Requirements:
> - Create a new service folder, likely something like:
>   /srv/qios/stacks/local-tts
>   or inside the current app if that is cleaner.
> - Include:
>   - docker-compose.yml
>   - README.md
>   - .env.example
>   - FastAPI wrapper if needed
>   - simple test script
>   - sample curl command
> - Bind the service to localhost by default, not public internet.
> - Use a port that does not conflict with existing services.
> - Store generated audio in a persistent volume/folder:
>   ./data/output
> - Add a health endpoint:
>   GET /health
> - Add a TTS endpoint:
>   POST /tts
> - Add a voices endpoint if supported:
>   GET /voices
> 
> API behavior:
> POST /tts should accept JSON like:
> {
>   "text": "Hello, this is a local test voice.",
>   "voice": "default",
>   "speed": 1.0,
>   "format": "wav"
> }
> 
> It should return:
> {
>   "status": "ok",
>   "engine": "kokoro",
>   "voice": "default",
>   "file": "/output/example.wav"
> }
> 
> Also create:
> - scripts/test_tts.sh
> - scripts/generate_sample.py if useful
> - docs explaining how to connect this later to Open WebUI, n8n, or my apps.
> 
> Important constraints:
> - Keep it simple.
> - No paid APIs.
> - No cloud dependency.
> - No GPU requirement for MVP.
> - Do not expose this publicly.
> - If voice cloning is not stable/easy, skip it for now and document it as Phase 2.
> - Phase 2 can evaluate XTTS-v2 or another local voice-cloning model, but the MVP should just work.
> 
> After implementation:
> - Run a local test.
> - Generate one sample audio file.
> - Confirm the endpoint works with curl.
> - Update the README with exact start/stop/test commands.
> ```
> 
> Reality check: **Kokoro is the right first move**. It’s lightweight, local, and good enough for everyday narration/testing; recent open-source TTS comparisons describe it as small, fast, and strong quality for its size. citeturn783909search12turn783909search18
> 
> Don’t start with XTTS/Coqui unless you specifically need voice cloning. That path is more annoying, more GPU-hungry, and may have licensing/commercial-use wrinkles depending on what you do with it. citeturn783909search13turn783909search17
> 
> The sane stack is:
> 
> **Phase 1:** Kokoro local API  
> **Phase 2:** Piper fallback for ultra-light/basic TTS  
> **Phase 3:** XTTS/F5-TTS only if you need cloned/custom voices
> 
> Translation: get the cheap local robot talking first, then make her glamorous later.

### User
> i belibve we already was working on one so he should check and see what all is htere.

### Assistant
> Yep — then don’t tell Codex to build from scratch. Tell it to **audit first, reuse what exists, and only fill gaps**.
> 
> Use this:
> 
> ```text
> I believe we already started working on a local TTS / ElevenLabs replacement somewhere in this repo or server. Before building anything new, audit what already exists.
> 
> Your job:
> 1. Search the current repo and relevant server folders for any existing TTS, audio, speech, narration, voice, ElevenLabs, Kokoro, Piper, Coqui, XTTS, F5-TTS, OpenVoice, or audio-generation work.
> 2. Do not duplicate services, folders, ports, APIs, or Docker stacks.
> 3. Identify what already exists, what works, what is incomplete, and what is safe to reuse.
> 4. Then create the smallest working path to get local TTS running.
> 
> Search terms to check:
> - tts
> - text-to-speech
> - speech
> - voice
> - narration
> - elevenlabs
> - eleven
> - kokoro
> - piper
> - coqui
> - xtts
> - f5
> - openvoice
> - audio
> - wav
> - mp3
> 
> Check these likely locations:
> - current repo
> - /srv/qios/apps
> - /srv/qios/stacks
> - /srv/qios/tools
> - /srv/qios/data
> - any docker-compose.yml files
> - any README files
> - any .env.example files
> - any scripts folders
> - any API routes or FastAPI services
> 
> After the audit, report back with:
> 1. Existing files/folders found
> 2. Existing services or Docker stacks found
> 3. Existing ports used
> 4. Existing audio/TTS dependencies found
> 5. What appears abandoned or incomplete
> 6. Recommended path forward
> 
> Then implement only what is missing.
> 
> Target outcome:
> A working local TTS service that can generate audio from text without paid APIs.
> 
> Preferred MVP:
> - Use existing work if present.
> - If no usable work exists, create or complete a local Kokoro TTS API.
> - Optional lightweight fallback: Piper TTS.
> - Do not start with voice cloning unless existing work already supports it cleanly.
> 
> Service requirements:
> - Local-only by default.
> - No paid APIs.
> - No cloud dependency.
> - No GPU requirement for MVP.
> - Do not expose publicly.
> - Persistent output folder for generated audio.
> - Health endpoint.
> - TTS endpoint.
> - README with start/stop/test commands.
> - Sample generated audio file.
> - Curl test command.
> 
> API target:
> GET /health
> 
> POST /tts
> JSON body:
> {
>   "text": "Hello, this is a local test voice.",
>   "voice": "default",
>   "speed": 1.0,
>   "format": "wav"
> }
> 
> Expected response:
> {
>   "status": "ok",
>   "engine": "kokoro",
>   "voice": "default",
>   "file": "/output/sample.wav"
> }
> 
> Important:
> Before making changes, give me the audit summary and the exact implementation plan. Then proceed with the smallest clean change set.
> ```
> 
> And because Codex sometimes gets cute and starts architecting the Vatican, add this at the bottom:
> 
> ```text
> Hard rule:
> Do not build a second parallel TTS system if one already exists. Reuse, repair, or extend the existing one unless it is clearly broken beyond repair.
> ```
> 
> That’s the move. Make Codex act like a mechanic, not a toddler with a glue gun.
