---
layout: page
title: "Voice isolation and transcription"
slug: "voice_isolation_and_transcription"
created_at: "2025-07-26 17:46:00"
updated_at: "2026-07-16T06:49:28-04:00"
status: active
tags: []
  - chat-log
category: "chat-log"
location: ""
involved: []
severity: 1
critical: false
source_type: "chat-log"
source_file: "Chat-Export-28513-2026/conversations-000.json"
template_key: master-template
date: 2025-07-26
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "68855a91-b58c-8321-99c9-02d579c31c67"
canonical_ref: ""
---

# Voice isolation and transcription

## Overview
- **Date**: 2025-07-26 17:46:00
- **Conversation ID**: `68855a91-b58c-8321-99c9-02d579c31c67`
- **Source**: `Chat-Export-28513-2026/conversations-000.json`

## Chat History

### User
> I have these mp4 video clips of me and my spouse arguing i need to isolate the voices and transcribe the audio, how can i do this.

### Assistant
> Alright, Q—here’s the game plan. You’re basically trying to do **speaker separation + transcription** (pull y’all’s voices apart, then turn it into text). Here are three levels you can play with:  
> 
> ---
> 
> ### **1. Fast & Dirty (Quickest DIY)**
> - **Tool:** [AudioStrip](https://www.audiostrip.co.uk/) or [VocalRemover.org](https://vocalremover.org)  
> - **Steps:**
>   1. Upload the MP4 → It will separate vocals from background noise (you’ll still have both voices together, but cleaner).
>   2. Export the “vocals only” audio as WAV or MP3.
>   3. Upload that to [Otter.ai](https://otter.ai) or [Sonix.ai](https://sonix.ai) for auto-transcription.
> 
> > Pros: Free-ish, no install.  
> > Cons: Won’t split *your* voice from *their* voice—just removes background noise.  
> 
> ---
> 
> ### **2. Solid & Safe (Clear Speaker Separation)**
> - **Tool:** [Demucs](https://github.com/facebookresearch/demucs) + [Whisper.cpp or OpenAI Whisper](https://github.com/openai/whisper)  
> - **Steps:**
>   1. Convert your MP4 to WAV (`ffmpeg -i input.mp4 output.wav`).
>   2. Run Demucs to isolate vocal stems (gives cleaner voice track).
>   3. Use **Whisper** to transcribe and optionally label timestamps.
>   4. (Optional) Use [pyannote.audio](https://github.com/pyannote/pyannote-audio) for **speaker diarization** (splits “Speaker A” vs “Speaker B”).
> 
> > Pros: Offline, powerful, can separate speakers.  
> > Cons: Setup is more technical (Python, command line).
> 
> ---
> 
> ### **3. Big Energy (Perfect Courtroom-Ready)**
> - **Tool:** Paid forensic software like [Izotope RX](https://www.izotope.com/en/products/rx.html) (for voice isolation) + [Descript](https://www.descript.com/) (for multi-speaker transcription + editing).  
> - **Steps:**
>   1. Import MP4 into RX → clean and isolate each voice (spectral editing).
>   2. Drop the cleaned tracks into Descript → it transcribes *and* assigns each speaker.
>   3. Export transcript with timestamps.
> 
> > Pros: Professional-quality, speaker-labeled, clean enough for legal/mediation use.  
> > Cons: Costs money, learning curve.
> 
> ---
> 
> ### What I need to know so I can tailor:
> - Do you want **free/DIY** or **pro/clean enough for legal proof**?
> - Do you need **timestamps** (like “2:34 – He said X”)?
> - Do you need **speaker labels** (like “Q” vs “Spouse”)?
> - Are you cool with **cloud tools** (uploading to web) or do you want **offline/private**?
> 
> You want me to **write you the exact commands/scripts** (so you can just copy-paste), or do you want **web-app links and no coding**?

### User
> does 3 cost money or should we use python and use the steps in 2

### Assistant
> Big Energy #3 **definitely costs money** — Izotope RX = ~$400+ (sometimes cheaper with sales) and Descript = ~$15–$30/month. It’s overkill unless you’re prepping this for **court-level forensic clarity** or need pristine audio.  
> 
> **Python route (#2) is free** (just your time + installing a few things). It’ll give you:  
> - **Voice isolation** (Demucs)  
> - **Transcription** (Whisper)  
> - **Speaker separation** (Pyannote)  
> 
> …and all offline, no data leaving your machine.  
> 
> ---
> 
> ### If you want to roll with Python (#2), here’s the roadmap:
> 
> #### **Step 1: Install tools**
> ```bash
> # Install ffmpeg (for converting mp4 to wav)
> sudo apt install ffmpeg
> 
> # Create virtual environment (optional but cleaner)
> python3 -m venv qvoice && source qvoice/bin/activate
> 
> # Install Demucs for voice isolation
> pip install demucs
> 
> # Install Whisper for transcription
> pip install openai-whisper
> 
> # Install Pyannote for speaker diarization (splits voices)
> pip install pyannote.audio
> ```
> 
> ---
> 
> #### **Step 2: Convert MP4 to WAV**
> ```bash
> ffmpeg -i argument.mp4 argument.wav
> ```
> 
> ---
> 
> #### **Step 3: Isolate voice track (Demucs)**
> ```bash
> demucs argument.wav
> ```
> > Output: Creates a folder with isolated stems (`vocals.wav`, `other.wav`, etc.)
> 
> ---
> 
> #### **Step 4: Transcribe with Whisper**
> ```bash
> whisper separated_folder/vocals.wav --model medium --language en
> ```
> > Output: `.txt` and `.srt` with timestamps.
> 
> ---
> 
> #### **Step 5: Split speakers with Pyannote**
> This part detects who’s speaking when (no names, just “Speaker 1 / 2”). You run:
> ```python
> from pyannote.audio import Pipeline
> 
> pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")
> diarization = pipeline("vocals.wav")
> 
> with open("diarization.txt", "w") as f:
>     for turn, _, speaker in diarization.itertracks(yield_label=True):
>         f.write(f"{turn.start:.1f}-{turn.end:.1f} {speaker}\n")
> ```
> > Combine this with the Whisper transcript → clean “Q vs Spouse” transcript.
> 
> ---
> 
> ### Want me to **write this as a full ready-to-run Python script** (copy/paste → run)?  
> Or you want me to **step-by-step guide you while you do it**?  
> 
> Also — **Windows, Mac, or Linux**? That’ll change how I package the commands for you.

### User
> ok so we are doing this in windows and I dont want it in qivoice that is for phone calls and such unless you think it makes since to use it later for transcribing calls.

### Assistant
> Gotchu, Q. **Windows setup, no mixing with Qivoice (yet).** We’ll make this its own clean project folder—later, if you decide Qivoice should handle *all* voice stuff (calls + arguments), we can merge it. For now: keep it separate so we don’t clutter your call pipeline.  
> 
> Here’s the **Windows-ready plan**:
> 
> ---
> 
> ## **Setup: Python Environment**
> 1. **Install Python** (if you don’t have it):
>    - Grab latest 3.10 or 3.11 from [python.org/downloads](https://www.python.org/downloads/windows/)
>    - During install: **check “Add Python to PATH”**
> 
> 2. **Install Git** (needed for some repos):
>    - [git-scm.com/download/win](https://git-scm.com/download/win)
> 
> 3. **Open Command Prompt / PowerShell**
>    ```powershell
>    mkdir voice_transcripts
>    cd voice_transcripts
>    python -m venv venv
>    .\venv\Scripts\activate
>    ```
> 
> ---
> 
> ## **Install Required Libraries**
> ```powershell
> pip install ffmpeg-python demucs openai-whisper pyannote.audio torch torchaudio
> ```
> 
> *(Torch will auto-pull the right GPU/CPU version — if no GPU, it’ll still work, just slower.)*
> 
> ---
> 
> ## **Convert MP4 → WAV**
> ```powershell
> ffmpeg -i "argument.mp4" "argument.wav"
> ```
> 
> ---
> 
> ## **Isolate Vocals (Demucs)**
> ```powershell
> demucs "argument.wav"
> ```
> - Output folder → `separated/htdemucs/argument/vocals.wav`
> 
> ---
> 
> ## **Transcribe Vocals (Whisper)**
> ```powershell
> whisper "separated/htdemucs/argument/vocals.wav" --model medium --language en
> ```
> - Outputs: `vocals.txt` + `vocals.srt` (timestamps included)
> 
> ---
> 
> ## **Speaker Separation (Pyannote)**
> > This splits *you* vs *spouse*, but doesn’t name them — we’ll label manually after.
> 
> Create `diarize.py`:
> ```python
> from pyannote.audio import Pipeline
> 
> pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")
> diarization = pipeline("separated/htdemucs/argument/vocals.wav")
> 
> with open("diarization.txt", "w") as f:
>     for turn, _, speaker in diarization.itertracks(yield_label=True):
>         f.write(f"{turn.start:.1f}-{turn.end:.1f} {speaker}\n")
> ```
> 
> Run it:
> ```powershell
> python diarize.py
> ```
> 
> ---
> 
> ## **Combine Transcript + Speaker**
> - We’ll merge the **timestamps from Whisper** with **speaker labels from Pyannote** into one readable transcript (I can script this for you if you want it auto-merged).
> 
> ---
> 
> ### **Next Decision**
> Do you want me to:  
> 1. **Write a single all-in-one Python script** (drag-drop MP4 → done, get clean transcript)?  
> 2. **Keep modular steps** (so you control each step and tweak)?  
> 3. **Integrate into Qivoice later** (so *calls + clips* all feed into same transcript vault)?  
> 
> Also: **Do you want me to prep this so it can handle *multiple* clips at once?** Or just one file at a time for now?

### User
> PUT TOGETHER THE DOCUMENTATION AND RELEVANT CODE FOR ME TO DOWNLOAD. OMITT ANYTHING THAT WILL NOT HELP US WITH THE QILIFE APP

### Assistant
> I packaged the **documentation + code** for the Windows voice transcription workflow. This is standalone (not tied to Qivoice) and ready to import into QiLife later if needed.
> 
> **Download here:**  
> [voice_transcription_windows.zip](sandbox:/mnt/data/voice_transcription_windows.zip)
> 
> ---
> 
> Do you want me to **also prep the merge script** (so Whisper + Pyannote outputs combine into a single labeled transcript automatically)? Or keep it modular?
