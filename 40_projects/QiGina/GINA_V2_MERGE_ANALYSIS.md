---
layout: page
title: G.I.N.A_v2 Merge Analysis & Integration Plan
slug: g-i-n-a-v2-merge-analysis-integration-plan
status: active
updated_at: "2026-06-29"
tags:
  - projects
source_type: manual
summary: ""
created_at: ""
author: ""
owner: ""
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: ""
uid: ""
canonical_ref: ""
template_key: master-template
---

# G.I.N.A_v2 Merge Analysis & Integration Plan

**Date:** 2025-01-XX
**Purpose:** Analyze `C:\QiOS_v1\projects\G.I.N.A_v2` and create merge plan for full GINA chatbot with memory system

---

## Executive Summary

The `G.I.N.A_v2` folder contains **4 major components**:
1. **QiGina** - Standalone React chat UI (good, keep)
2. **QiMind** - Memory/ingestion system with v1 local brain (excellent, merge)
3. **QiGPT** - Alternative chat UI (duplicate, archive)
4. **QiSecondBrain** - Separate second brain system (evaluate, likely duplicate)

**Key Finding:** The v1 local brain in `QiMind/v1/brain.py` has **complete short-term and long-term memory** that the current local_core lacks. This is the critical merge target.

---

## Component Analysis

### 1. QiGina (`projects/G.I.N.A_v2/QiGina/`)

**Status:** ✅ **KEEP & MERGE**

**What it is:**
- Modern React + TypeScript chat interface
- Connects to GINA Local Core API (`/gina/chat`)
- Auto-fallback between Local Core and Cloudflare Worker
- Clean UI with tool suggestions, endpoint status

**What's Good:**
- ✅ Production-ready UI code
- ✅ Smart endpoint fallback logic (`ginaClient.ts`)
- ✅ Tool invocation UI
- ✅ Endpoint health monitoring
- ✅ Well-structured TypeScript

**What's Missing:**
- ❌ No conversation history persistence (in-memory only)
- ❌ No memory visualization
- ❌ No timeline integration

**Merge Plan:**
- Move to `apps/QiGina/` (or keep in projects, integrate into main)
- Connect to local_core's conversation_history
- Add QiMind timeline integration
- Add memory visualization UI

**Files to Keep:**
- `src/App.tsx` - Main UI
- `src/api/ginaClient.ts` - API client with fallback
- `src/types.ts` - Type definitions
- `package.json` - Dependencies

---

### 2. QiMind (`projects/G.I.N.A_v2/QiMind/`)

**Status:** ✅ **CRITICAL MERGE TARGET**

**What it is:**
- Memory/ingestion pipeline for GINA
- Supabase integration for timeline sessions
- **v1 Local Brain** with full STM/LTM memory system
- Ingestion scripts for chats, emails, documents

**What's Good:**

#### v1 Local Brain (`QiMind/v1/brain.py`)

- ✅ **Short-Term Memory (STM)**: Conversation context with deque
- ✅ **Long-Term Memory (LTM)**: Vector embeddings with Milvus Lite
- ✅ **Combined Context**: `get_full_context()` merges STM + LTM
- ✅ **100% Local**: No API keys, runs offline
- ✅ **Voice I/O**: Whisper STT + Piper TTS
- ✅ **File Watching**: Auto-index on file changes
- ✅ **Screen Watching**: Automatic screen capture
- ✅ **Email Capture**: IMAP integration
- ✅ **Task Management**: Todoist, Reminders, Things3
- ✅ **Streaming Responses**: Real-time token streaming

#### Supabase Integration (`QiMind/supabase/`)

- ✅ Timeline sessions (`timeline_sessions`, `timeline_messages`)
- ✅ Vector embeddings (`qi_chunks`)
- ✅ Node links (`timeline_node_link`)
- ✅ `ginaMemory.ts` - Memory node creation/management
- ✅ RAG search integration

**What's Duplicate:**
- ⚠️ Some ingestion scripts may overlap with `workers/local/local_core/`
- ⚠️ RAG implementation may overlap with `workers/local/local_core/rag.py`

**Merge Plan:**

#### Phase 1: Integrate v1 Brain Memory System

1. **Extract memory classes** from `brain.py`:
   - `LocalAIBrain` class
   - `add_to_stm()` method
   - `remember()` method (LTM retrieval)
   - `get_full_context()` method

2. **Integrate into local_core**:
   - Add to `workers/local/local_core/memory.py` (new file)
   - Replace current conversation_history-only approach
   - Add STM deque per user_id
   - Add LTM vector search integration

3. **Update GINA chat endpoint**:
   - Use `get_full_context()` instead of just conversation_history
   - Inject STM + LTM into system prompt
   - Maintain backward compatibility

#### Phase 2: Supabase Memory Integration

1. **Connect ginaMemory.ts**:
   - Use `createGinaMemory()` for persistent memories
   - Use `findExistingMemoryNode()` to avoid duplicates
   - Store important facts/events/insights as QiNodes

2. **Timeline Integration**:
   - Query `timeline_sessions` for conversation history
   - Use `qi_chunks` for RAG search
   - Link conversations to QiNodes

#### Phase 3: Advanced Features (Optional)

- Voice I/O (if needed)
- File watching (if needed)
- Screen watching (if needed)

**Files to Keep:**
- `v1/brain.py` - **CRITICAL**: Full memory system
- `v1/README.md` - Documentation
- `supabase/worker/ginaMemory.ts` - Memory node management
- `supabase/worker/rag.ts` - RAG search
- `supabase/migrations/001_timeline_tables.sql` - Schema

**Files to Evaluate:**
- `ingest/` - Check for overlap with local_core ingestion
- `db/` - Data exports, may be outdated

---

### 3. QiGPT (`projects/G.I.N.A_v2/QiGPT/`)

**Status:** ⚠️ **DUPLICATE - ARCHIVE**

**What it is:**
- Alternative chat UI (similar to QiGina)
- Older implementation
- Cloudflare-focused

**What's Good:**
- ✅ Some UI components might be useful
- ✅ Settings drawer component

**What's Duplicate:**
- ❌ Overlaps with QiGina
- ❌ Less modern than QiGina
- ❌ No memory integration

**Merge Plan:**
- **Archive** (move to `projects/_archived/QiGPT/`)
- Extract useful components if needed:
  - `SettingsDrawer.tsx` (if better than QiGina's)
  - Any unique features

---

### 4. QiSecondBrain (`projects/G.I.N.A_v2/QiSecondBrain/`)

**Status:** ⚠️ **EVALUATE - LIKELY DUPLICATE**

**What it is:**
- Separate "Second Brain" system
- Python-based backend/frontend
- Image labeling, search engine

**What's Good:**
- ✅ Image processing capabilities
- ✅ Search engine with GPU/CPU support

**What's Duplicate:**
- ❌ Overlaps with QiMind's memory system
- ❌ Separate codebase, not integrated
- ❌ May conflict with QiOS architecture

**Merge Plan:**
- **Evaluate** if image search is needed
- If useful, extract image processing features
- Otherwise, **archive** or keep as separate tool

---

## Current Local Core State

### What Exists Now (`workers/local/local_core/`)

**Memory System:**
- ✅ `conversation_history` table (SQLite)
- ✅ `conversation_embeddings` table (for semantic search)
- ✅ Basic conversation logging
- ❌ **NO short-term memory** (no deque/context window)
- ❌ **NO long-term memory retrieval** (embeddings exist but not used in chat)
- ❌ **NO memory consolidation**

**GINA Chat:**
- ✅ `/gina/chat` endpoint exists
- ✅ RAG search via `rag.py`
- ✅ Tool calling support
- ✅ Conversation history (last 10 messages)
- ❌ **NO STM/LTM integration**
- ❌ **NO memory node creation**

---

## Merge Strategy

### Phase 1: Core Memory Integration (HIGH PRIORITY)

**Goal:** Add STM/LTM to local_core

**Steps:**

1. **Create `workers/local/local_core/memory.py`**:
   ```python
   from collections import deque
   from typing import List, Dict, Optional
   from .rag import search_semantic_profile

   class GinaMemory:
       def __init__(self, stm_max: int = 30):
           self.stm: Dict[str, deque] = {}  # user_id -> deque of messages
           self.stm_max = stm_max

       def add_to_stm(self, user_id: str, role: str, content: str):
           """Add message to short-term memory."""
           if user_id not in self.stm:
               self.stm[user_id] = deque(maxlen=self.stm_max)
           self.stm[user_id].append({"role": role, "content": content})

       def get_ltm(self, query: str, user_id: str, k: int = 5) -> List[Dict]:
           """Get long-term memories via RAG."""
           # Use existing rag.py search_semantic_profile
           results = search_semantic_profile(query, limit=k)
           return [{"text": r.content, "score": r.score} for r in results]

       def get_full_context(self, user_id: str, query: str) -> List[Dict[str, str]]:
           """Get combined STM + LTM context."""
           stm_messages = list(self.stm.get(user_id, []))
           ltm = self.get_ltm(query, user_id)

           ltm_context = "\n---\n".join([m["text"] for m in ltm])
           system_message = {
               "role": "system",
               "content": f"Long-term memories:\n{ltm_context}"
           }

           return stm_messages + [system_message]
   ```

2. **Update `qios_local_core.py`**:
   - Import `GinaMemory`
   - Initialize in FastAPI app
   - Replace conversation_history-only approach with `get_full_context()`
   - Add STM updates after each message

3. **Update GINA prompt**:
   - Add memory system explanation
   - Reference STM/LTM in system prompt

**Files to Modify:**
- `workers/local/local_core/qios_local_core.py` - Add memory integration
- `workers/local/local_core/memory.py` - **NEW FILE**
- `workers/local/local_core/gina_prompt.py` - Update prompt

---

### Phase 2: QiGina UI Integration

**Goal:** Integrate QiGina UI into main project

**Steps:**

1. **Move QiGina to proper location**:
   - Option A: `apps/QiGina/` (if apps structure exists)
   - Option B: Keep in `projects/G.I.N.A_v2/QiGina/` but integrate

2. **Add conversation history persistence**:
   - Load from `conversation_history` on mount
   - Save new messages to backend
   - Add session management

3. **Add memory visualization**:
   - Show STM context window
   - Show LTM matches
   - Timeline integration

4. **Connect to local_core**:
   - Already connected via `ginaClient.ts`
   - Verify endpoint compatibility
   - Test tool invocation

**Files to Modify:**
- `projects/G.I.N.A_v2/QiGina/src/App.tsx` - Add history loading
- `projects/G.I.N.A_v2/QiGina/src/api/ginaClient.ts` - Add history endpoints

---

### Phase 3: Supabase Memory Nodes

**Goal:** Integrate persistent memory nodes via Supabase

**Steps:**

1. **Port `ginaMemory.ts` to Python**:
   - Create `workers/local/local_core/memory_nodes.py`
   - Implement `create_gina_memory()`
   - Implement `find_existing_memory_node()`
   - Use Supabase client

2. **Add memory creation triggers**:
   - After important conversations
   - After tool executions
   - After insights

3. **Integrate with RAG**:
   - Query memory nodes in RAG search
   - Link conversations to memory nodes

**Files to Create:**
- `workers/local/local_core/memory_nodes.py` - **NEW FILE**
- `workers/local/local_core/integrations/supabase/` - Supabase client

---

### Phase 4: Advanced Features (Optional)

**Voice I/O:**
- Extract from `brain.py` if needed
- Integrate TTS/STT into local_core

**File Watching:**
- Extract from `brain.py` if needed
- Integrate with vault crawler

**Screen Watching:**
- Extract from `brain.py` if needed
- Add as optional feature

---

## Duplicate Detection

### Confirmed Duplicates

1. **QiGPT vs QiGina**: QiGPT is duplicate, archive it
2. **QiSecondBrain vs QiMind**: Likely duplicate, evaluate first

### Potential Overlaps

1. **Ingestion Scripts**:
   - `QiMind/ingest/` vs `workers/local/local_core/crawler/`
   - **Action**: Compare, merge best of both

2. **RAG Implementation**:
   - `QiMind/supabase/worker/rag.ts` vs `workers/local/local_core/rag.py`
   - **Action**: Keep Python version, port TypeScript features if needed

3. **Database Schema**:
   - `QiMind/supabase/migrations/` vs `workers/local/local_core/migrations/`
   - **Action**: Merge timeline tables into local_core migrations

---

## File Organization After Merge

```
workers/local/local_core/
├── memory.py                    # NEW: STM/LTM memory system
├── memory_nodes.py              # NEW: Supabase memory nodes
├── qios_local_core.py           # MODIFY: Add memory integration
├── gina_prompt.py               # MODIFY: Update with memory info
├── rag.py                       # KEEP: Already good
└── integrations/
    └── supabase/                # NEW: Supabase client for memory nodes

apps/QiGina/                     # MOVE from projects/G.I.N.A_v2/QiGina/
├── src/
│   ├── App.tsx                  # MODIFY: Add history persistence
│   ├── api/ginaClient.ts        # MODIFY: Add history endpoints
│   └── components/
│       └── MemoryView.tsx       # NEW: Memory visualization

projects/_archived/              # NEW: Archive duplicates
├── QiGPT/                       # MOVE: Duplicate UI
└── QiSecondBrain/              # MOVE: If not needed
```

---

## Implementation Priority

### 🔴 CRITICAL (Do First)

1. **Extract STM/LTM from brain.py** → `memory.py`
2. **Integrate memory into GINA chat** → Update `qios_local_core.py`
3. **Test memory system** → Verify STM/LTM works

### 🟡 HIGH (Do Next)

4. **Move QiGina to apps/** → Organize structure
5. **Add conversation history to QiGina** → Persistence
6. **Port ginaMemory.ts to Python** → Memory nodes

### 🟢 MEDIUM (Nice to Have)

7. **Memory visualization UI** → Show STM/LTM
8. **Timeline integration** → Supabase timeline
9. **Advanced features** → Voice, file watching

### ⚪ LOW (Future)

10. **Archive duplicates** → Clean up
11. **Documentation** → Update GINA.md
12. **Testing** → Comprehensive tests

---

## Testing Plan

### Memory System Tests

1. **STM Test**:
   - Send 5 messages
   - Verify STM contains all 5
   - Send 35 more (total 40)
   - Verify STM only has last 30

2. **LTM Test**:
   - Ingest document
   - Ask question about document
   - Verify LTM retrieval works
   - Verify context injected

3. **Combined Context Test**:
   - Use STM + LTM together
   - Verify system prompt has both
   - Verify response uses both

### Integration Tests

1. **QiGina + Local Core**:
   - Load conversation history
   - Send new message
   - Verify STM updated
   - Verify response uses memory

2. **Memory Nodes**:
   - Create memory node
   - Verify stored in Supabase
   - Query via RAG
   - Verify retrieved

---

## Risks & Mitigations

### Risk 1: Breaking Existing Functionality

**Mitigation**:
- Keep conversation_history as fallback
- Add feature flags for memory system
- Gradual rollout

### Risk 2: Performance Impact

**Mitigation**:
- STM is in-memory (fast)
- LTM uses existing RAG (already optimized)
- Add caching if needed

### Risk 3: Data Migration

**Mitigation**:
- No migration needed (additive)
- Existing conversations stay in conversation_history
- New system works alongside old

---

## Success Criteria

✅ **Phase 1 Complete When:**
- STM/LTM integrated into local_core
- GINA chat uses memory system
- Tests pass

✅ **Phase 2 Complete When:**
- QiGina integrated into main project
- Conversation history persists
- UI shows memory context

✅ **Phase 3 Complete When:**
- Memory nodes created automatically
- Supabase integration working
- RAG includes memory nodes

✅ **Full Merge Complete When:**
- All duplicates archived
- Documentation updated
- System tested end-to-end

---

## Next Steps

1. ✅ **Phase 1 COMPLETE** - Memory system integrated (see `GINA_MEMORY_MERGE_COMPLETE.md`)
2. **Start Phase 2** - QiGina UI integration
3. **Start Phase 3** - Supabase memory nodes
4. **Iterate** based on results

---

## Questions to Resolve

1. **Where should QiGina live-** (`apps/` vs `projects/`)
2. **Should we keep QiSecondBrain-** (evaluate image search need)
3. **Voice I/O priority-** (optional vs required)
4. **File watching priority-** (optional vs required)
5. **Timeline integration priority-** (high vs medium)

---

**End of Analysis**
