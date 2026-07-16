---
layout: page
title: "GINA Desktop Dev Docs"
slug: "gina_desktop_dev_docs"
created_at: "2025-12-06 01:53:22"
updated_at: "2025-12-06 01:53:22"
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
date: 2025-12-06
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "6933e0f0-1728-8329-8f62-d6ff5f5cf20e"
canonical_ref: ""
---

# GINA Desktop Dev Docs

## Overview
- **Date**: 2025-12-06 01:53:22
- **Conversation ID**: `6933e0f0-1728-8329-8f62-d6ff5f5cf20e`
- **Source**: `Chat-Export-28513-2026/conversations-001.json`

## Chat History

### User
> real quick we need a desktop stay in front floating gina, that i can click have my question transcribed and she be ablelt o read the supabase table to retrive information coherently as a stand alone assistant for now if i can get that i will feel better, all i want is for her to be able to read and write and update entires in supabase for now in a coherent way.

### Assistant
> Short answer: yes, this is absolutely doable as a *small* thing — but we need to be ruthless about scope or you’ll drown yourself again.
> 
> You’re asking for:
> 
> > A tiny always-on-top desktop GINA where you click → talk → she:
> > - transcribes you
> > - reads from Supabase (semantic_profile & friends)
> > - can write/update rows
> > - answers coherently as a standalone assistant
> 
> I’ll give you a concrete v1 design + exact build steps.
> 
> ---
> 
> ## 0. Reality check (what you already have)
> 
> From the repo:
> 
> - Local-core FastAPI backend with `/gina/chat` and all the other endpoints is already scaffolded and wired to SQLite as the “single-machine brain”.fileciteturn0file3L1-L9  
> - There’s a full GINA chat contract + personality prompt defined for `/gina/chat` with proper request/response models.fileciteturn0file1L1-L8  
> - Orchestrator GINA already pulls live telemetry from Supabase (worker_status, ingestion_queue, semantic_profile *counts*).fileciteturn0file4L1-L8  
> - QiNote already has an API client pattern for ingest/query/memory that talks to workers/Supabase.fileciteturn0file2L42-L52  
> - The architecture review explicitly calls out “Desktop app wrapper (Electron/Tauri)” as a long-term plan.fileciteturn0file5L399-L417  
> 
> So we’re **not** starting from zero. We’re just carving out a thin slice: *one small client* that talks to Supabase + OpenAI (or to `/gina/chat`) and gives you a floating window.
> 
> ---
> 
> ## 1. Pick the MVP architecture (don’t overcomplicate)
> 
> I’d do **Option A now**, **Option B later**:
> 
> ### Option A – “Brutally simple” desktop GINA (recommended for *right now*)
> 
> - **Tech**: Tauri + React + TypeScript (same stack you already use).
> - **Where it lives**: `apps/gina_desktop/` (QiApp, clean with your ontology).
> - **What it talks to directly**:
>   - Supabase REST (via `@supabase/supabase-js`)
>   - OpenAI Chat (with the existing GINA prompt copied over)
> 
> No workers, no orchestrator, no local_core dependency for v1. Just your desktop shell talking straight to the brain.
> 
> ### Option B – “QiOS-pure” version (later)
> 
> - Same Tauri app, but instead of hitting Supabase/OpenAI directly, it:
>   - Calls `http://localhost:7130/gina/chat` on **local_core**, and
>   - local_core handles all Supabase + RAG/query logic.
> 
> You *already* have the `/gina/chat` contract and prompt extracted into Python for local_core.fileciteturn0file1L33-L40  
> But right now, that endpoint isn’t doing full semantic_profile RAG, it’s more of a placeholder.fileciteturn0file3L40-L48
> 
> So: **A is fastest** to get you emotional relief. B is “correct” QiOS architecture for later.
> 
> ---
> 
> ## 2. Non-negotiable prerequisite: Supabase reality
> 
> You want:
> 
> > “read and write and update entries in supabase”
> 
> That assumes:
> 
> - Supabase project exists (it does).
> - The **QiOS schema is actually deployed** (this was flagged as missing in the repo audit).fileciteturn0file5L189-L206  
> - `semantic_profile` and whatever tables you want to touch exist *in that project*.
> 
> So before you waste time on UI:
> 
> 1. **In Supabase SQL editor**, run (or confirm you already ran) the QiBrain schema:
>    - `data/schemas/qios_brain_db_v1.sql` and any migrations in `apps/QiNote/supabase/migrations/`.fileciteturn0file5L253-L269  
> 2. Verify:
> 
>    ```sql
>    select * from semantic_profile limit 5;
>    ```
> 
>    If that gives an error, you don’t have a table. Fix that first.
> 
> If schema is not deployed, your “desktop GINA” is just a pretty box with nowhere to read/write. Don’t skip this.
> 
> ---
> 
> ## 3. Data contract for GINA ↔ Supabase (MVP)
> 
> For v1, keep it **embarrassingly simple**:
> 
> ### What GINA can *read* (MVP):
> 
> Use `semantic_profile` like:
> 
> - `id` (uuid / text)
> - `title` / `file_name`
> - `chunk_index`
> - `content` (text chunk)
> - maybe `summary`
> 
> We’ll fetch “relevant” rows via simple text search (you can add pgvector later):
> 
> ```ts
> // pseudo-SQL using Supabase-js
> supabase
>   .from('semantic_profile')
>   .select('id, title, chunk_index, content')
>   .ilike('content', `%${query}%`)
>   .limit(10);
> ```
> 
> You pass these chunks into the system prompt as context.
> 
> ### What GINA can *write/update* (MVP):
> 
> Don’t let the LLM do arbitrary SQL. That’s how you end up with chaos.
> 
> Instead, give it **one constrained surface**:
> 
> - A single table for “assistant notes” or “user annotations” (pick one):
> 
>   - Option 1: Re-use `semantic_profile` for now with a special `source = 'gina_desktop'`
>   - Option 2: Create `gina_journal`:
> 
>     ```sql
>     create table if not exists gina_journal (
>       id uuid primary key default gen_random_uuid(),
>       created_at timestamptz default now(),
>       updated_at timestamptz default now(),
>       author text, -- 'gina', 'user', etc.
>       title text,
>       body text,
>       tags text[]
>     );
>     ```
> 
> And then in the app you expose **explicit actions**:
> 
> - “Save this answer as note”
> - “Update note”
> - “Delete note”
> 
> Those actions are buttons in the UI → mapped to **Supabase CRUD**. Don’t trust the LLM to decide schema changes.
> 
> ---
> 
> ## 4. High-level flow for the desktop app
> 
> Here’s the exact loop for v1 (Option A):
> 
> 1. You click the floating GINA.
> 2. She:
>    - Starts mic capture (Web Speech API or any STT lib) → transcribes to text.
> 3. `askGina(transcript)` runs:
>    - **Step 1 – Query Supabase** for relevant context rows.
>    - **Step 2 – Build prompt**: GINA personality + context + your question.
>    - **Step 3 – Call OpenAI Chat** and get `reply`.
>    - **Step 4 – Show reply** in the floating window.
> 4. (Optional) You click “Save as note” → this calls `supabase.from('gina_journal').insert(...)`.
> 
> That’s it. No workers. No orchestrator. Just one clean path.
> 
> ---
> 
> ## 5. Concrete file layout for `apps/gina_desktop/`
> 
> Minimal structure:
> 
> ```text
> apps/gina_desktop/
>   package.json
>   vite.config.ts
>   index.html
>   tauri.conf.json        # Tauri config (always-on-top)
>   src/
>     main.tsx
>     App.tsx
>     supabaseClient.ts
>     openaiClient.ts
>     ginaPrompt.ts
>     askGina.ts
>     components/
>       FloatingShell.tsx
>       MicButton.tsx
>       MessageList.tsx
>       SettingsPanel.tsx
> ```
> 
> ### `supabaseClient.ts` (MVP)
> 
> ```ts
> // apps/gina_desktop/src/supabaseClient.ts
> import { createClient } from '@supabase/supabase-js';
> 
> const supabaseUrl = import.meta.env.VITE_SUPABASE_URL!;
> const supabaseKey = import.meta.env.VITE_SUPABASE_SERVICE_KEY!; // desktop, trusted
> 
> export const supabase = createClient(supabaseUrl, supabaseKey, {
>   auth: { persistSession: false },
> });
> ```
> 
> Yes, I’m deliberately using the service key here because this is a **local desktop tool only you run**, not a public web app. If you ever distribute this, we lock this down.
> 
> ### `openaiClient.ts`
> 
> ```ts
> // apps/gina_desktop/src/openaiClient.ts
> import OpenAI from 'openai';
> 
> const apiKey = import.meta.env.VITE_OPENAI_API_KEY!;
> 
> export const openai = new OpenAI({ apiKey, dangerouslyAllowBrowser: true });
> ```
> 
> (If you don’t like `dangerouslyAllowBrowser`, put the OpenAI call in a tiny Tauri command / backend instead.)
> 
> ### `ginaPrompt.ts`
> 
> Copy the existing GINA personality prompt from `workers/local_core/gina_prompt.py` into a TS string so you keep behavior consistent.fileciteturn0file1L33-L40  
> 
> ```ts
> export const GINA_SYSTEM_PROMPT = `
> You are GINA, the Orchestrator for the QiOS system...
> [paste trimmed personality prompt here]
> `;
> ```
> 
> ---
> 
> ## 6. The brains: `askGina.ts`
> 
> ```ts
> // apps/gina_desktop/src/askGina.ts
> import { supabase } from './supabaseClient';
> import { openai } from './openaiClient';
> import { GINA_SYSTEM_PROMPT } from './ginaPrompt';
> 
> export async function askGina(question: string) {
>   // 1) Fetch context from Supabase
>   const { data: chunks, error } = await supabase
>     .from('semantic_profile')
>     .select('id, title, chunk_index, content')
>     .ilike('content', `%${question}%`)
>     .limit(10);
> 
>   if (error) {
>     console.error('Supabase error', error);
>   }
> 
>   const contextText =
>     (chunks ?? [])
>       .map(
>         (c) =>
>           `# ${c.title ?? 'Untitled'} [chunk ${c.chunk_index}]\n${c.content}`,
>       )
>       .join('\n\n') || 'No matching context found in semantic_profile.';
> 
>   const messages = [
>     {
>       role: 'system' as const,
>       content: `${GINA_SYSTEM_PROMPT}
> 
> You have access to the following snippets from the QiOS semantic_profile table:
> 
> ${contextText}
> 
> Use them to answer the user's question. If context is missing, still answer from your general knowledge but say that explicitly.`,
>     },
>     { role: 'user' as const, content: question },
>   ];
> 
>   // 2) Call OpenAI
>   const completion = await openai.chat.completions.create({
>     model: 'gpt-4.1-mini',
>     messages,
>   });
> 
>   const reply = completion.choices[0]?.message?.content ?? '';
> 
>   return { reply, contextUsed: chunks ?? [] };
> }
> ```
> 
> Saving notes:
> 
> ```ts
> export async function saveGinaNote(
>   title: string,
>   body: string,
>   tags: string[] = [],
> ) {
>   const { data, error } = await supabase
>     .from('gina_journal')
>     .insert({ author: 'gina_desktop', title, body, tags })
>     .select()
>     .single();
> 
>   if (error) throw error;
>   return data;
> }
> ```
> 
> ---
> 
> ## 7. Floating desktop UI (React)
> 
> Very small:
> 
> ```tsx
> // apps/gina_desktop/src/App.tsx
> import { useState } from 'react';
> import { askGina, saveGinaNote } from './askGina';
> import { FloatingShell } from './components/FloatingShell';
> 
> export default function App() {
>   const [messages, setMessages] = useState<
>     { role: 'user' | 'gina'; text: string }[]
>   >([]);
>   const [isThinking, setIsThinking] = useState(false);
> 
>   async function handleAsk(text: string) {
>     if (!text.trim()) return;
>     setMessages((m) => [...m, { role: 'user', text }]);
>     setIsThinking(true);
> 
>     try {
>       const { reply } = await askGina(text);
>       setMessages((m) => [...m, { role: 'user', text }, { role: 'gina', text: reply }]);
>     } catch (e) {
>       console.error(e);
>       setMessages((m) => [
>         ...m,
>         {
>           role: 'gina',
>           text: 'I hit an error talking to Supabase or OpenAI. Check your config.',
>         },
>       ]);
>     } finally {
>       setIsThinking(false);
>     }
>   }
> 
>   async function handleSaveLast() {
>     const last = [...messages].reverse().find((m) => m.role === 'gina');
>     if (!last) return;
>     await saveGinaNote('Desktop GINA note', last.text);
>   }
> 
>   return (
>     <FloatingShell
>       messages={messages}
>       onAsk={handleAsk}
>       onSaveLast={handleSaveLast}
>       isThinking={isThinking}
>     />
>   );
> }
> ```
> 
> `FloatingShell` is just a little glass card with a textarea (or mic button) and message list. Make it ADHD-friendly: big mic button, always visible, minimal options.
> 
> ---
> 
> ## 8. Always-on-top behavior (Tauri)
> 
> In `tauri.conf.json`:
> 
> ```json
> {
>   "tauri": {
>     "windows": [
>       {
>         "title": "GINA Desktop",
>         "alwaysOnTop": true,
>         "decorations": false,
>         "transparent": true,
>         "resizable": true,
>         "width": 420,
>         "height": 600
>       }
>     ]
>   }
> }
> ```
> 
> From JS you can also force it:
> 
> ```ts
> import { appWindow } from '@tauri-apps/api/window';
> 
> appWindow.setAlwaysOnTop(true);
> ```
> 
> Optional: add a global hotkey (e.g. `Ctrl+Space`) to toggle show/hide so it’s truly “stay in front but not annoying”.
> 
> ---
> 
> ## 9. Voice → text
> 
> Don’t overthink this v1. In the React component:
> 
> ```ts
> const SpeechRecognition =
>   (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
> 
> function useSpeechToText(onText: (t: string) => void) {
>   // hook that starts SR, collects result, calls onText
> }
> ```
> 
> Use it only on desktop where Chrome/Edge supports it. If it’s flaky, just fall back to typing; you can swap to a local STT later.
> 
> ---
> 
> ## 10. Do-this-now checklist
> 
> If you want to actually feel better today, follow this order:
> 
> 1. **Confirm Supabase schema**
>    - Run `select * from semantic_profile limit 1;`  
>    - If it errors → deploy `qios_brain_db_v1.sql` first.fileciteturn0file5L253-L269  
> 
> 2. **Create `apps/gina_desktop/` with Vite + Tauri**
>    - `npm create vite@latest gina_desktop -- --template react-ts`
>    - Add Tauri per docs.
>    - Add `@supabase/supabase-js` + `openai`.
> 
> 3. **Wire up `supabaseClient.ts`, `openaiClient.ts`, `askGina.ts`** using the snippets above.
> 
> 4. **Build the minimal FloatingShell**:
>    - Message list
>    - Input box or mic button
>    - “Save last answer” button
> 
> 5. **Add always-on-top in Tauri config** so she’s truly “stay in front”.
> 
> Once that’s in place, you’ve got:
> 
> - Click → talk → GINA answers using your Supabase semantic_profile.
> - Single-click to save interesting answers back into Supabase.
> - No dependency on the whole QiOS stack being perfect.
> 
> When you’re ready, we can refactor this to:
> 
> - Hit `/gina/chat` on local_core instead of OpenAI directly.
> - Switch from dumb text search → proper vector similarity.
> - Use the existing orchestrator-aware GINA state pipeline instead of this micro-brain.fileciteturn0file4L25-L40  
> 
> If you want, next step I can write the exact `FloatingShell.tsx` with mic handling and a barebones `tauri.conf.json` so you can drop it straight into the repo and run.

### User
> give me the dev docs for this

### Assistant
> # GINA Desktop — Developer Documentation (MVP v1)
> 
> ## Overview
> 
> GINA Desktop is a lightweight standalone desktop assistant for the QiOS ecosystem.
> 
> Primary goals:
> 
> - Always-on-top floating assistant
> - Voice or text input
> - Coherent retrieval from Supabase
> - Read/write/update structured records
> - ADHD-friendly low-friction UX
> - Fast local-feeling interaction
> - Minimal dependencies on full QiOS infrastructure
> 
> This is intentionally a **thin client MVP**, not the full orchestration stack.
> 
> ---
> 
> # 1. System Goals
> 
> ## MVP Requirements
> 
> GINA Desktop must:
> 
> - Float above other windows
> - Accept typed or spoken input
> - Retrieve relevant context from Supabase
> - Generate coherent responses using LLM context injection
> - Save/update notes and memory objects
> - Operate independently of the full QiOS backend
> 
> ---
> 
> # 2. Architecture
> 
> ## MVP Architecture
> 
> ```text
> ┌────────────────────┐
> │   GINA Desktop     │
> │  (Tauri + React)   │
> └─────────┬──────────┘
>           │
>           ├── Supabase-js
>           │      ├── semantic_profile
>           │      ├── gina_journal
>           │      └── future tables
>           │
>           └── OpenAI API
>                  └── Chat Completion
> ```
> 
> ---
> 
> # 3. Technology Stack
> 
> | Layer | Technology |
> |---|---|
> | Desktop Shell | Tauri |
> | Frontend | React + TypeScript |
> | Build Tool | Vite |
> | Database | Supabase |
> | AI | OpenAI |
> | STT | Web Speech API (initial) |
> | Styling | TailwindCSS |
> | State | React state initially |
> | Packaging | Tauri Build |
> 
> ---
> 
> # 4. Repository Structure
> 
> ## Recommended Location
> 
> ```text
> QiLabs/
> └── apps/
>     └── gina_desktop/
> ```
> 
> ---
> 
> ## Folder Structure
> 
> ```text
> gina_desktop/
> ├── package.json
> ├── vite.config.ts
> ├── tauri.conf.json
> ├── .env.local
> ├── src/
> │   ├── main.tsx
> │   ├── App.tsx
> │   ├── styles/
> │   ├── lib/
> │   │   ├── supabaseClient.ts
> │   │   ├── openaiClient.ts
> │   │   ├── askGina.ts
> │   │   ├── speech.ts
> │   │   └── ginaPrompt.ts
> │   ├── components/
> │   │   ├── FloatingShell.tsx
> │   │   ├── MicButton.tsx
> │   │   ├── MessageList.tsx
> │   │   ├── InputBar.tsx
> │   │   └── SettingsPanel.tsx
> │   └── types/
> │       └── index.ts
> └── src-tauri/
> ```
> 
> ---
> 
> # 5. Environment Variables
> 
> ## `.env.local`
> 
> ```env
> VITE_SUPABASE_URL=
> VITE_SUPABASE_SERVICE_KEY=
> VITE_OPENAI_API_KEY=
> ```
> 
> ---
> 
> # 6. Supabase Requirements
> 
> ## Required Tables
> 
> ### semantic_profile
> 
> Used for contextual retrieval.
> 
> Minimum recommended columns:
> 
> ```sql
> id uuid primary key
> title text
> chunk_index integer
> content text
> summary text
> tags text[]
> created_at timestamptz
> updated_at timestamptz
> ```
> 
> ---
> 
> ### gina_journal
> 
> Used for assistant-created notes.
> 
> ```sql
> create table if not exists gina_journal (
>     id uuid primary key default gen_random_uuid(),
>     created_at timestamptz default now(),
>     updated_at timestamptz default now(),
>     author text,
>     title text,
>     body text,
>     tags text[]
> );
> ```
> 
> ---
> 
> # 7. Core Retrieval Pipeline
> 
> ## Flow
> 
> ```text
> User Input
>     ↓
> Speech-to-Text
>     ↓
> Query Supabase
>     ↓
> Inject Context into Prompt
>     ↓
> OpenAI Completion
>     ↓
> Display Response
>     ↓
> Optional Save to Supabase
> ```
> 
> ---
> 
> # 8. Retrieval Logic
> 
> ## Initial Retrieval Strategy
> 
> MVP uses text similarity:
> 
> ```ts
> .ilike('content', `%${query}%`)
> ```
> 
> This is temporary.
> 
> ---
> 
> ## Future Upgrade
> 
> Replace with:
> 
> - pgvector
> - embeddings
> - semantic ranking
> - graph retrieval
> - hybrid search
> 
> ---
> 
> # 9. OpenAI Prompting Strategy
> 
> ## Structure
> 
> ```text
> SYSTEM:
> GINA personality + operational rules
> 
> CONTEXT:
> Relevant semantic_profile rows
> 
> USER:
> Actual user message
> ```
> 
> ---
> 
> ## Context Injection Rules
> 
> - Limit to ~10 chunks
> - Truncate oversized context
> - Preserve source attribution
> - Prefer recent records
> - Avoid duplicate chunks
> 
> ---
> 
> # 10. CRUD Permissions
> 
> ## Allowed Operations (MVP)
> 
> | Operation | Allowed |
> |---|---|
> | Read semantic_profile | YES |
> | Create journal notes | YES |
> | Update journal notes | YES |
> | Delete journal notes | YES |
> | Arbitrary SQL | NO |
> | Schema modification | NO |
> 
> ---
> 
> # 11. Security Rules
> 
> ## IMPORTANT
> 
> This is currently a trusted local desktop application.
> 
> The MVP may temporarily use:
> 
> ```env
> VITE_SUPABASE_SERVICE_KEY
> ```
> 
> This is acceptable ONLY if:
> 
> - app is local-only
> - not publicly distributed
> - not browser-hosted
> 
> ---
> 
> ## Future Security Upgrade
> 
> Later versions should:
> 
> - proxy through local_core
> - use signed auth
> - use RLS
> - use scoped service accounts
> - remove browser-visible keys
> 
> ---
> 
> # 12. UI/UX Principles
> 
> ## UX Priorities
> 
> ### MUST HAVE
> 
> - Extremely low friction
> - Minimal clicks
> - Floating utility feel
> - Fast perceived response
> - Keyboard-first
> - ADHD-friendly
> - Persistent availability
> 
> ---
> 
> ## Avoid
> 
> - Modal overload
> - Settings clutter
> - Complex navigation
> - Multi-window workflows
> - Excessive animations
> 
> ---
> 
> # 13. Window Behavior
> 
> ## Required
> 
> | Behavior | Status |
> |---|---|
> | Always-on-top | REQUIRED |
> | Frameless | REQUIRED |
> | Resizable | YES |
> | Transparent | OPTIONAL |
> | Global hotkey | FUTURE |
> | Tray icon | FUTURE |
> 
> ---
> 
> # 14. Speech-to-Text
> 
> ## MVP Choice
> 
> Use browser-native speech recognition:
> 
> ```ts
> window.SpeechRecognition
> window.webkitSpeechRecognition
> ```
> 
> Advantages:
> 
> - fast
> - free
> - easy
> 
> Limitations:
> 
> - browser dependent
> - inconsistent quality
> - internet-dependent
> 
> ---
> 
> ## Future Upgrade Path
> 
> Possible replacements:
> 
> | Engine | Notes |
> |---|---|
> | Whisper.cpp | Strong local option |
> | faster-whisper | Excellent |
> | Deepgram | Cloud |
> | OpenAI realtime | Future possibility |
> 
> ---
> 
> # 15. Future Architecture Evolution
> 
> ## Phase 1 — Current MVP
> 
> ```text
> Desktop → Supabase/OpenAI directly
> ```
> 
> ---
> 
> ## Phase 2 — Local Core Gateway
> 
> ```text
> Desktop → local_core → Supabase/OpenAI
> ```
> 
> Benefits:
> 
> - central auth
> - unified orchestration
> - tool routing
> - memory control
> - logging
> - caching
> 
> ---
> 
> ## Phase 3 — Full QiOS Agent
> 
> ```text
> Desktop
>     ↓
> Orchestrator
>     ↓
> Workers
>     ↓
> RAG + Graph + Memory
> ```
> 
> ---
> 
> # 16. Logging
> 
> ## MVP Logging
> 
> Create:
> 
> ```text
> logs/
> ```
> 
> Store:
> 
> - prompt logs
> - errors
> - retrieval failures
> - response latency
> - Supabase errors
> 
> ---
> 
> # 17. Recommended Initial Features
> 
> ## Build Order
> 
> ### Phase 1
> 
> - Floating window
> - Text input
> - Supabase retrieval
> - OpenAI responses
> 
> ### Phase 2
> 
> - Speech input
> - Save notes
> - Journal browsing
> 
> ### Phase 3
> 
> - Semantic retrieval
> - Embeddings
> - Graph memory
> 
> ### Phase 4
> 
> - Tool calling
> - Scheduling
> - Calendar
> - Automation
> 
> ---
> 
> # 18. Recommended Commands
> 
> ## Development
> 
> ```bash
> npm install
> npm run tauri dev
> ```
> 
> ---
> 
> ## Build
> 
> ```bash
> npm run tauri build
> ```
> 
> ---
> 
> # 19. Known MVP Constraints
> 
> ## Expected Limitations
> 
> | Limitation | Reason |
> |---|---|
> | Weak retrieval | No embeddings yet |
> | Context overflow | Simple chunk injection |
> | No memory hierarchy | MVP only |
> | No agent tools | Deferred |
> | No auth isolation | Trusted local app |
> | STT quality inconsistent | Browser API |
> 
> ---
> 
> # 20. Success Criteria
> 
> GINA Desktop MVP succeeds if:
> 
> - Cody can click and ask questions quickly
> - GINA can retrieve coherent Supabase context
> - GINA can save/update notes reliably
> - Interaction feels immediate and low-friction
> - Daily usage replaces scattered note-taking
> 
> Not success:
> 
> - Full AGI orchestration
> - Perfect memory graph
> - Multi-agent ecosystem
> - Enterprise security
> - Autonomous workflows
> 
> Those come later.
> 
> ---
> 
> # 21. Strategic Note
> 
> This app is not the final architecture.
> 
> This is a stabilization layer.
> 
> The real purpose is:
> 
> > give immediate operational relief and restore cognitive continuity.
> 
> That matters more right now than perfect architecture.
