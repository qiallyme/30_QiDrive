---
layout: page
title: QiSuite Dev Bible
slug: qisuite-dev-bible
status: legacy-reference
updated_at: "2026-06-30"
owner: CRV
tags:
  - qispark
  - legacy-doctrine
  - source-material
source_type: manual
realm: 2_QsKb
privacy: private
qi_decimal: 2.99.00-01.SYS
summary: Legacy technical doctrine retained as source material for QiSpark updates.
---
# QiSuite Dev Bible

## 📌 Project Overview

**QiSuite** is a modular second brain framework with:
- A desktop app (Electron + React + Tailwind)
- A hosted chatbot (Cloudflare Worker API)
- Core assistant ("Qinnie") that runs both locally and in the cloud

Main goal: create a modular and extensible foundation for AI-first business tools like:
- QiFileFlow (duplicate file cleaner + OCR)
- QiNote (semantic note builder)
- QiLifeFeed (daily logs, time tracking, automations)
- QiMind (vector memory / contextual Qinnie)

---

## 🔧 Stack Overview

### Desktop (Electron + React + Tailwind)

- Runs on `Electron` using Vite as the dev server.
- Hot-reloads React UI with Tailwind CSS.
- Has local storage-based settings management (for API keys, etc.).
- Loads Qinnie dock on all screens.

### Web API (Cloudflare Worker)

- POST endpoint: `/chat`
- Accepts `{ message }` JSON and returns `{ reply }`
- Will eventually support:
  - OpenAI + Ollama fallback
  - Per-client memory (KV store)
  - Branded deployment URLs

---

## ⚙️ Features (Current)

### ✅ Electron Shell

- Main window loads Vite app.
- Preload.js supports secure IPC for key storage.

### ✅ UI (React + Tailwind)

- Homepage with `Hero`, `Pitch`, `Pricing`, `Footer`
- Persistent `QinnieDock` open by default
- Responsive layout

### ✅ QinnieDock

- Floating assistant dock in lower right
- Open by default (can collapse)
- Settings panel (gear icon):
  - OpenAI Key
  - Worker URL
- Messages persist per session (local only)
- Replies fetched from Worker (if configured), else fallback

### ✅ Branding

- Core brand: **QiSuite**
- Powered by: **BuiltByRays™**
- All client-specific assets abstracted to `shared/theme.js`

### ✅ Worker API

- Cloudflare Worker endpoint: `/chat`
- Basic echo-style reply stub
- Ready for KV + OpenAI integrations

---

## 🔐 Settings Management

Uses localStorage for now:
- `OPENAI_API_KEY`
- `WORKER_API_URL`

Settings panel available inside Qinnie dock.

---

## 🧱 Folder Structure

```
QiSuite_Full_Build/
├── electron/
│   ├── main/              ← Electron startup logic
│   ├── renderer/
│   │   ├── pages/App.jsx
│   │   ├── components/    ← Modular UI: Hero, Pitch, Pricing, Dock, etc.
│   └── package.json
│
├── shared/
│   └── theme.js           ← Branding config
│
├── workers/
│   ├── src/index.js       ← Cloudflare Worker logic
│   └── wrangler.toml
└── README.md              ← Full setup & deployment guide
```

---

## 🌐 Cloudflare Deployment

### Setup

```bash
npm install -g wrangler
wrangler login
cd workers
wrangler publish
```

### URL

```http
POST https://your-app-name.workers.dev/chat
Content-Type: application/json
Body: { "message": "Hello Qinnie" }
```

### KV / Secrets (coming)

```bash
wrangler kv:namespace create QINNIE_KV
wrangler secret put OPENAI_API_KEY
```

---

## 🔮 Next Sprints

### Sprint 1: QiFileFlow

- Duplicate file detection (hashing)
- OCR and semantic labeling
- File quarantine + tagging UI

### Sprint 2: QiMind

- Local vector database (Chroma, Weaviate, or Ollama embed)
- RAG + search for enhanced memory in Qinnie

### Sprint 3: Client Portal Mode

- Convert UI into mobile-friendly PWA
- Tailwind theme overrides per client repo

---

## 🧠 Notes

- All branding should come from `theme.js`
- Clients can fork or clone this repo and deploy their own version
- Shared modules will live in `modules/` soon

---

## ✍️ Maintainer

**Q / Cody Rice Velasquez**
`qially.me` · `qiSuite.app` · `BuiltByRays™`

---

> “Go big or go home.” – The mission is modular sovereignty. This is just the beginning.
