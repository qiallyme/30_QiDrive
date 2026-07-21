---
layout: article
title: Article 5. Local AI
slug: qicode-title-13-article-05-local-ai
summary: ""
status: publish
updated_at: "2026-07-21"
tags:
  - qicode
qicode_title: 13
qicode_article: 5
parent_title: Title 13. QiServer
canonical_ref: QiCode T13.A05
source_type: manual
---

## Article 5. Local AI

Stable ID: `T13.A05`

### Sec. 13.05.010. AI Compute Governance

Stable ID: `T13.A05.S010`

- `Line 1` Local AI services (Ollama, Open WebUI, Qdrant, Neo4j) are hosted and governed under QiServer; the active chat model is `llama3.2` and the embedding model is `embeddinggemma`. (`Sec. 13.05.010.L001`; stable ID `T13.A05.S010.L001`)
- `Line 2` AI models and vector indexes must be versioned and documented in `20_QiServer/10_ai_compute`; graph and vector outputs are derived â€” they are not canonical sources of truth. (`Sec. 13.05.010.L002`; stable ID `T13.A05.S010.L002`)
- `Line 3` Local AI services must not process protected legal or evidence records without explicit governance review; QiTTS and QiTranscribe are local AI services subject to this rule. (`Sec. 13.05.010.L003`; stable ID `T13.A05.S010.L003`)


