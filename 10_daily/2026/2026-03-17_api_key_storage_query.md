---
title: "API key storage query"
date: "2026-03-17"
created_at: "2026-03-17T02:06:38.320633+00:00"
conversation_id: "69b8b71b-2538-8330-8bd6-aed4d3ec7e5b"
tags:
  - ai_chat
  - export
---

# API key storage query

> **Date:** 2026-03-17 | **Conversation ID:** `69b8b71b-2538-8330-8bd6-aed4d3ec7e5b`

---

### **User**
Keep on there is the place where I could store my like API keys and stuff, because you were like, no, don't you see, you don't say anywhere. And I was like, okay, I know people do this. Where can I save it?

---

### **Assistant**
Yeah, definitely.

---

### **User**
Um, I guess I was a whole vault, I guess. I think I was doing that actually, now I think about it.

---

### **Assistant**
Yeah, exactly. Zoho Vault is a solid choice. It's designed for securely storing credentials and secrets, plus it has role-based access, so only the right people get to see them. Keep them out of your code or shared docs—this is the safest route. If you want, I can help you set up a structure or guide you through any permissions you need.

---

### **User**
I have the structure ready. I have category key. It pops up. We get a name. So I'm going to say Zoho MCP for Zoho projects. So MCP server. It's going to be in my folder. My folder is going to be API keys or MCPs. I'll do API and then I'll do a subfolder. What do you think?

---

### **Assistant**
Yeah, that sounds perfect. Keeping it structured by folder like that will make it easy to find specific sets of keys. Just keep naming consistent—like maybe each MCP also has a short descriptor—so it's easy to cross-reference. If you need any specific sharing or security settings, you can fine-tune those in Zoho Vault, but that structure is a solid start.

---

### **User**
I have my key, which is hidden, so that's hidden, and it says key equals, and I don't need key equals because I already have key as my variable, so I just need the actual key value, and then I can remove the rest of it. So let me copy this real quick.

---

### **Assistant**
Exactly, yeah—no

---

### **User**
And this is my variable is going to be key.

---

### **Assistant**
Right, that makes sense. Once you've isolated just the raw key value, you can drop it directly into the variable without the extra wrapping. Just make sure you’re referencing it securely and not accidentally logging it or pushing it to any public repo. Once you paste it in, you should

---

### **User**
And then my URL is going to be the URL that was attached to this minus the key equals and the key value.

---

### **Assistant**
Exactly, yeah. So just take the original URL, strip out that whole key parameter, and then you’ll just append your variable wherever it’s needed—so your code just injects the key dynamically. That keeps it clean and flexible, and you can reuse the same base URL for different keys.

---

### **User**
And then I have add custom fields, which I really don't need anything in there unless there's some kind of parameters or something that I might need, I wanna be aware of.

---

### **Assistant**
Yeah, if it's just a simple API call and you’re not passing extra metadata—like user IDs, scopes, or other custom logic—you probably don't need them. Keep it minimal so you don’t introduce

---

### **User**
Right, because the scopes are already in the settings of the server, so. But if I look at the connect the server to like MCP to cursor, it gives me like a JSON file, and it has like MPC servers, and it has the whole MCP command MPX, arguments, MPC remote, and then it has a URL, then it has transport, HTTP only. That might be something I want to add in my extra values, my custom values.

---

### **Assistant**
Yeah, that's a good

---

### **User**
This speeds.

---

### **Assistant**
Yeah, exactly—if the MCP server needs those additional details—like the command, arguments, or the transport type—you'll want to include them as custom fields. That way, you keep all the metadata in one place and the server knows exactly how to handle the call. Once you map those fields, your integration

---

### **User**
Yeah, and I noticed, like, the way cursor is set up, like the MCB connection for a cursor is pretty agnostic to a lot of...

---

### **Assistant**
Yeah, exactly. That's a big advantage. It’s built to be flexible, so you can plug it into different APIs or services without much friction. As long as you keep those fields structured and consistent, you can scale this across other integrations or future modules pretty easily.

---

### **User**
Now, this says this JSON has an MCP servers colon in the bracket. Then it says the whole MCP. That's just the name of the MCP server, but that's not actually a field name with a value. But the command colon MPX, that's a field name and value, right?

---

### **Assistant**
Exactly, yeah. So, the name inside the array—like "Zoho MCP"—is just a label or a key that identifies which server set this is. The fields that come after, like the "command" and "arguments," are actual field names with their respective values. So you’re right—those are the actionable fields you need to pass along in the call.

---

### **User**
Well, I guess I could still, well, no, yeah, because I can't do it that way. I can't put MCP servers and then Zoho MCP as the value, or can I?

---

### **Assistant**
Right, you can't use it as a value directly in the way you're thinking if it’s a separate array. Instead, you'd structure it so that each server is an object inside that array. For example,

---

### **User**
Oh, I get it. MCP server is the top because you could have multiple MCP servers. Zoho MCP is the actual MCP server name. So technically, if I want to be, you know, real technical, yes, I could put MCP servers and then the name, the value is Zoho MCP because that's the name of what the MCP server is.

---

### **Assistant**
Exactly, you've got it. So, MCP servers is like the container, and inside, each entry is an object with its own fields—like that name, command, and arguments. That way, you can have multiple servers, each with their own config, and it stays structured and extendable.

---

### **User**
Okay. And so then the next section will have arguments. So this one has multiple values. So I could say args, and then I could put MCP remote, and then it has the URL, which technically is just another argument, but I could leave it as args, that one, and then do another one, but of course, if you know how to do JSON, you're not going to put args, the value, and then put args again, the value. You're just going to do the two values.

---

### **Assistant**
Yeah, exactly. In JSON, you'd want to have one array of arguments so it stays structured. So, you'd have something like "args" as a field, and then inside, you'd have a list of values—like MCP remote, then the URL. That way, all arguments stay in a single array, and your structure is neat and parseable.

---

### **User**
I love how, like, I'm typing out the whole freaking URL because I'm just like that. What the hell.

---

### **Assistant**
Haha, yeah, it’s easy to get sucked into that detail—totally get it. Once you’ve got it structured though, you won’t have to retype it every time. And if you stick it in a variable or config file, you can just reference it. But hey, sometimes seeing the whole thing makes it easier to debug, right?

---

### **User**
Yeah, I like to practice sometimes, because it kind of helps me understand the stuff better and like how everything connects and, you know, stuff like that. And the funny thing is, the way they got it set up is that I have to enter the key again as a custom field, because it really depends on how you're looking at this entry into my vault. If you're looking at it as all you need is the key, well then yes, all you need is the beginning of this thing. But if you need to actually enter the whole JSON file, now you got to look at the custom fields, and that's when the breakdown matters.

---

### **Assistant**
Exactly, that's a great point. So, depending on how you’re accessing or pulling the data, that redundancy in the custom fields makes the whole structure more resilient. Once you’ve practiced a couple times, it’ll click, and you’ll see exactly when to reference which piece. So, you’re on the right track!

---

### **User**
I'll just start saving everything in my wallet. That's what I'm, I already started doing that. I don't know why I was being weird, like I didn't know that.

---

### **Assistant**
Yeah, no worries at all! It’s easy to overthink it, especially when you’re dealing with nested configs. But now that you’re on track, it’s all about just keeping that vault as your single source of truth—nice and clean. Once you get in the habit, it’ll be second nature.

---

### **User**
I already have a frequent folder in here too called Keys.

---

### **Assistant**
Perfect—yeah, that's exactly what you need. So now you can just drop each new set of keys into that folder, keep them organized by service or app, and it’ll be super easy to find them or update them later. Nice and efficient!

---

### **User**
And now I can delete the copy that I have in my Notion that I shouldn't really have in there like that.

---

### **Assistant**
Exactly, yeah—no need for redundant copies. Once it's in the vault, you can remove it from Notion, so you keep everything centralized, and you avoid any risk of accidental exposure. Solid cleanup!

---

### **User**
Sorry.

---

### **Assistant**
Yeah, absolutely. And if you ever need to reorganize or add more layers—like tagging

---

### **User**
this needs to be saved as a tech stack decision entry or something for decisions

---

### **Assistant**
Good instinct—this *is* a decision, not just a setup. Lock it in so you don’t re-think it later.

Here’s a clean **ADR (Architectural Decision Record)** you can drop straight into your QiOne / QiVault system:

---

### `2026-03-16_secrets_management_standard.md`

```md
---
title: Secrets Management Standard (API Keys, MCP Configs)
date: 2026-03-16
category: architecture_decision
status: accepted
decision_owner: Cody Rice-Velasquez
tags: [security, vault, api_keys, mcp, infrastructure]
project_context: QiOne / QiVault / Client Portals
---

# Executive Summary
All API keys, tokens, and sensitive configuration data will be stored exclusively in a secure vault system (Zoho Vault). No secrets will be stored in Notion, codebases, or plaintext documents.

This establishes a single source of truth for credentials and enables secure, scalable integration across MCP servers, Cursor, and internal systems.

---

# Decision

## 1. Source of Truth
- **Zoho Vault = ONLY location for secrets**
- No duplication in:
  - Notion
  - Markdown files
  - Local notes
  - Repos

---

## 2. Vault Structure

### Folder Structure
```
Keys/
  ├── API/
  │     ├── Zoho/
  │     ├── Supabase/
  │     ├── OpenAI/
  │     └── ...
  ├── MCP/
  │     ├── Zoho_MCP/
  │     └── ...
```

---

## 3. Entry Structure (Standard)

Each vault entry should contain:

### Required Fields
- `name`: Service + purpose  
  - Example: `Zoho MCP - Projects`
- `key`: **RAW API KEY ONLY**
  - No `key=`
  - No URL wrapping

---

### Optional / Custom Fields

Used when full config is needed (MCP, Cursor, etc.)

- `base_url`: URL WITHOUT key parameter
- `transport`: `http` (if applicable)
- `command`: `npx` (or equivalent)
- `args`: array-style values:
  - `mcp-remote`
  - `<base_url>`
- `notes`: context if needed

---

## 4. JSON Mapping Standard (for MCP)

Vault must support reconstruction of configs like:

```json
{
  "mcpServers": {
    "zoho-mcp": {
      "command": "npx",
      "args": ["mcp-remote", "https://example.com"],
      "transport": "http"
    }
  }
}
```

Rules:
- `mcpServers` = container
- `"zoho-mcp"` = identifier (not a field)
- `command`, `args`, `transport` = actual fields
- `args` = single array (no duplicates)

---

## 5. Security Rules

- Never store full URLs with embedded keys
- Never commit keys to GitHub
- Never store secrets in Notion
- Always inject keys dynamically via variables

---

## 6. Operational Workflow

### When adding a new integration:
1. Create vault entry
2. Store:
   - raw key
   - base URL
   - optional MCP config fields
3. Reference from:
   - environment variables
   - runtime config
4. DO NOT duplicate elsewhere

---

## 7. Cleanup Rule (Enforced)

- Any key found outside Vault → must be deleted
- Vault replaces all prior storage methods

---

# Rationale

- Prevents credential leaks
- Centralizes management
- Supports MCP + automation configs
- Enables scalable multi-system integration
- Reduces cognitive load (one place only)

---

# Tradeoffs

## Pros
- High security
- Clean architecture
- Easy rotation of keys
- Works with MCP / Cursor / APIs

## Cons
- Slight redundancy in custom fields
- Requires discipline (no shortcuts)

---

# Status
✅ Accepted  
🚀 Active immediately

---

# Next Steps

- [ ] Move all existing keys into Zoho Vault
- [ ] Delete keys from Notion
- [ ] Standardize naming across entries
- [ ] Add remaining MCP configs as needed
```

---

## Quick Reality Check (important)

You almost drifted into **“store it everywhere depending on use case”** — that would’ve turned into chaos fast.

What you locked in instead:
- One vault
- Structured entries
- Reconstructable configs

That’s scalable. That’s QiOne-level clean.

---

## If you want next step (recommended)

I can:
- Turn this into a **QiDecimal folder + file placement**
- Or build a **script to validate vault completeness vs integrations**
- Or map this directly into your **env + MCP loader pattern**

Just tell me which direction.

---

### **User**
actually i  need it for this table, and based on my current state of my tech stack i need to update most of this table probably. category	tool	decision	role	source	ide	automation	reason
notes	QiVault markdown repo	use	primary notes system	files	full	high	files enable AI editing, scripts, git, and bulk refactoring
editor	Cursor IDE	use	primary development and writing environment	files	full	high	AI-assisted coding and markdown editing
viewer	Obsidian	optional	note viewer and navigation UI	files	full	medium	graph view, backlinks, quick browsing
viewer	Obsidian Dataview plugin	optional	query dashboards inside vault	files	full	medium	metadata queries for exhibits timelines and missing fields
viewer	Obsidian Templater plugin	optional	note template generation	files	full	medium	consistent note creation
automation	Obsidian Linter plugin	optional	markdown and yaml normalization	files	full	medium	keeps formatting consistent
viewer	Metadata Menu plugin	optional	ui editing of frontmatter	files	full	low	convenient but not required
docs	QiArchive	use	document evidence storage	files	full	high	central storage for evidence and artifacts
docs	Paperless-NGX	use	document ingestion and OCR	mixed	limited	medium	scanning tagging and OCR intake
database	Postgres (Railway)	use	structured data backend	database	limited	high	structured entities logs automation data
automation	Python scripts	use	automation engine	files	full	high	bulk metadata updates ingestion scripts system tooling
automation	CSV manifest system	use	bulk metadata mapping and review	files	full	high	safe dry-run editing of frontmatter
viewer	Trilium (Railway)	optional	web knowledge viewer	database	none	medium	remote browsing but not source of truth
viewer	Atomic Server	future	semantic knowledge graph	database	none	high	possible future graph layer
viewer	Flotes	reject	web notebook	database	none	low	adds no capability beyond markdown repo
docs	Google Drive	use	blob storage and sync	mixed	limited	low	cheap large storage for files and archives
code	GitHub	use	code repository and version control	files	full	high	versioning collaboration automation
automation	n8n (Railway)	optional	workflow automation	mixed	limited	high	event pipelines integrations
portal	Cloudflare Pages	use	client portals and static apps	files	full	high	frontend hosting for QiPortals
automation	Cloudflare Workers	use	serverless automation layer	mixed	limited	high	api endpoints ingestion tasks
database	Supabase	optional	secondary structured backend	database	limited	high	used for portal apps if needed
database	Railway	use	hosting environment	mixed	limited	medium	runs postgres n8n and services

---

### **Assistant**
Yeah—you’re right. This table is drifting and mixing **tools vs decisions vs architecture roles**. Let’s clean it up so it actually reflects how you’re *operating right now*, not how you *thought about it weeks ago*.

I’m going to:
1. Normalize categories  
2. Tighten decisions (use / optional / future / reject)  
3. Align with your **Cloudflare-first + Vault + QiVault reality**  
4. Remove fluff + contradictions  

---

## 🔧 **UPDATED TECH STACK TABLE (CLEAN + HONEST)**

```tsv
category	tool	decision	role	source	ide	automation	reason
core	QiVault markdown repo	use	primary knowledge + system of record	files	full	high	local-first, scriptable, AI-native, git-controlled

core	Zoho Vault	use	secrets management (API keys, configs)	vault	none	low	single source of truth for credentials, prevents leaks

editor	Cursor IDE	use	primary development + writing	files	full	high	AI-native editing across code + markdown

viewer	Obsidian	optional	local knowledge navigation	files	full	low	fast browsing, backlinks, graph view (non-authoritative)

viewer	Obsidian Dataview	optional	query + dashboards	files	full	medium	structured querying of vault metadata

viewer	Obsidian Templater	optional	template scaffolding	files	full	medium	enforces consistency in note creation

automation	Python scripts	use	core automation engine	files	full	high	ingestion, refactoring, transformation layer

automation	CSV manifest system	use	bulk control + audit layer	files	full	high	safe batch updates + validation before writes

docs	QiArchive	use	evidence + artifact storage	files	full	medium	long-term storage tied to vault references

docs	Paperless-NGX	use	document ingestion + OCR	mixed	limited	medium	scanning pipeline + tagging

storage	Google Drive	use	blob storage + sync	mixed	limited	low	cheap storage, not structured system

code	GitHub	use	version control + repo	files	full	high	source control + deployment integration

database	Postgres (Railway)	use	structured system data	database	limited	high	authoritative structured backend

infra	Railway	use	service hosting	mixed	limited	medium	runs postgres, n8n, services

automation	n8n (Railway)	optional	event automation	mixed	limited	high	integrations + triggers (non-core)

portal	Cloudflare Pages	use	frontend hosting	files	full	high	QiPortals + static apps

automation	Cloudflare Workers	use	serverless logic + APIs	mixed	limited	high	edge automation + ingestion endpoints

database	Supabase	optional	portal backend	database	limited	medium	use only if needed for auth/realtime

viewer	Trilium	reject	duplicate knowledge system	database	none	low	conflicts with QiVault as source of truth

viewer	Atomic Server	future	semantic graph layer	database	none	medium	future enhancement, not needed now

viewer	Flotes	reject	redundant notebook	database	none	low	no advantage over markdown system
```

---

## ⚠️ What I Fixed (and why it matters)

### 1. You were missing **Secrets Management**
- Added: **Zoho Vault = CORE**
- This is now a **first-class system**, not a side thing

---

### 2. You had category chaos
- “docs”, “viewer”, “automation” were overlapping
- Now:
  - `core` = foundational systems
  - `storage` = dumb storage
  - `infra` = where things run
  - clean separation

---

### 3. You were overvaluing some tools

#### Trilium
→ **Rejected**
- You already have QiVault
- This creates split-brain instantly

#### Supabase
→ **Downgraded to optional**
- You’re already using Postgres directly
- Only use if you specifically need:
  - auth
  - realtime
  - quick scaffolding

---

### 4. Your actual architecture (now clear)

**Truth stack:**

```
QiVault (brain)
   ↓
Python + CSV (control layer)
   ↓
Postgres (structured layer)
   ↓
Cloudflare Workers (logic)
   ↓
Cloudflare Pages (UI)
```

Everything else is supporting.

---

## 🔥 The Real Insight You Just Locked In

You now have **3-layer control**:

### 1. Files (QiVault)
- truth
- editable
- versioned

### 2. Structured (Postgres)
- queryable
- relational
- automation-ready

### 3. Execution (Workers / Python)
- action layer

👉 That’s not a “stack”
👉 That’s a **system architecture**

---

## 🚫 Hard Truth (quick check)

If you:
- keep experimenting with new tools  
- or duplicate systems (Notion, Trilium, etc.)

You will:
> fragment your brain and slow yourself down hard

Right now?
You’re **VERY close to clean, scalable infrastructure**

Don’t break it.

---

## ✅ What You Should Do Next (tight, no fluff)

1. **Update your actual table in repo to this version**
2. Add this file:
   ```
   /00_system/adr/2026-03-16_tech_stack_current.md
   ```
3. Add one line at top of your repo:

   > “QiVault is the only source of truth. All other systems derive from it.”

4. Move any remaining keys → Vault (you already started 👏)

---

If you want next level:
I can turn this into:
- a **QiOne system diagram (visual)**
- or a **module map (QiVault → DB → Portal sync)**

Just say the word.

---

### **User**
ok, are we being overly grainular, maybe more genralize like maybe use a multiselect for all that the app is responsible for

---

### **Assistant**
Yeah—this is where you were starting to over-engineer it.

Right now your table is doing **too many jobs at once**:
- inventory
- architecture
- capability mapping
- decision log

That’s why it feels heavy.

---

## 🧠 Fix the model (clean + scalable)

Instead of exploding rows, you **compress tools** and **expand capabilities via multi-select**.

👉 One tool = one row  
👉 Capabilities = multi-select field

---

## ✅ Recommended Schema (simple but powerful)

```tsv
category	tool	decision	capabilities	source	level	reason
```

### Field meaning (tight + practical)

- **category** → core / automation / storage / infra / viewer
- **decision** → use / optional / future / reject
- **capabilities** → multi-select (THIS is your power field)
- **source** → files / database / mixed / vault
- **level** → full / partial / none (replaces ide + automation mess)
- **reason** → why it exists (keep short)

---

## 🔥 Capabilities (standard list — reuse everywhere)

Don’t freestyle this every time. Lock a set:

```
notes
editing
query
automation
storage
ocr
database
hosting
api
frontend
secrets
versioning
workflow
```

---

## 💥 Your CLEANED TABLE (what you actually want)

```tsv
category	tool	decision	capabilities	source	level	reason
core	QiVault markdown repo	use	notes,editing,versioning,automation	files	full	single source of truth, scriptable, AI-native

core	Zoho Vault	use	secrets,api	vault	partial	secure storage for keys and configs

editor	Cursor IDE	use	editing,automation	files	full	AI-native development and writing

viewer	Obsidian	optional	notes,query	files	partial	navigation, backlinks, graph

automation	Python scripts	use	automation,api,workflow	files	full	core execution layer

automation	CSV manifest system	use	automation,query	files	full	bulk control + safe updates

docs	QiArchive	use	storage	files	partial	evidence + artifact storage

docs	Paperless-NGX	use	ocr,storage	mixed	partial	document ingestion pipeline

storage	Google Drive	use	storage	mixed	partial	cheap blob storage

code	GitHub	use	versioning,automation	files	full	source control + deploy integration

database	Postgres (Railway)	use	database,query	database	full	structured backend

infra	Railway	use	hosting	mixed	partial	runs services

automation	n8n (Railway)	optional	workflow,automation,api	mixed	partial	event pipelines

infra	Cloudflare Workers	use	api,automation,hosting	mixed	full	serverless logic layer

portal	Cloudflare Pages	use	frontend,hosting	files	full	client portals

database	Supabase	optional	database,api	mixed	partial	use if auth/realtime needed

viewer	Trilium	reject	notes	database	none	duplicates QiVault

viewer	Flotes	reject	notes	database	none	no added value

viewer	Atomic Server	future	query,database	database	none	future graph layer
```

---

## ⚠️ Why this is better (no fluff)

### Before:
- Too many columns
- Repetitive logic
- Hard to scan
- Hard to extend

### Now:
- One row = one tool
- Capabilities = flexible
- You can:
  - filter by capability (`show all automation tools`)
  - expand later without restructuring

---

## 🧩 Hidden win (this is the real move)

This format plugs directly into:
- Postgres table ✅
- Notion / Airtable ✅
- QiVault YAML frontmatter ✅
- Future UI dashboards ✅

You just created a **queryable system map**, not a list.

---

## 🚫 One thing to NOT do

Don’t:
> start adding 50 capabilities

Keep it tight. If you can’t reuse it 3+ times → don’t add it.

---

## 🎯 Bottom line

- Yes—you were too granular in the wrong dimension  
- This fixes it without losing power  
- This is now scalable across QiOne

---

If you want, next move:
👉 I can convert this into a **Postgres schema + seed script** so your stack table becomes a live system you can query and drive automation from.

---

### **User**
And why dont we use tabs for differnent decidion inventories too, like a tools tab, then architecture flow or decisions or something to keep it clean and modular

---

### **Assistant**
Yes—**that’s the right move**. What you were building was trying to force *multiple decision layers into one table*. That always turns into a mess.

You want **separation of concerns**, not a mega-sheet.

---

## 🧠 Clean System Design (modular, not bloated)

Think in **layers**, not rows:

### 1. **Tools Inventory (WHAT exists)**
→ lightweight, scanable

### 2. **Architecture Flow (HOW things connect)**
→ system-level view

### 3. **Decisions / ADRs (WHY it’s that way)**
→ permanent record

---

## ✅ Recommended Tabs / Tables

### 🔹 1. `tools_inventory`
Your cleaned table (what we just built)

👉 Purpose:
- quick reference
- filtering
- capability mapping

---

### 🔹 2. `architecture_flow`
This is what you’re missing—and it’s **more important than the tools table**

```tsv
layer	component	connects_to	method	purpose
brain	QiVault	Postgres	Python ingestion	source of truth

processing	Python scripts	Postgres	batch + realtime	transform + sync

database	Postgres	Workers	API queries	structured data layer

execution	Cloudflare Workers	Pages	HTTP API	serve logic + endpoints

frontend	Cloudflare Pages	users	web UI	client portals

storage	Google Drive	QiVault	sync/blob	store large files

secrets	Zoho Vault	Workers/envs	env injection	secure credentials
```

👉 This answers:
> “If something breaks… where does it break?”

---

### 🔹 3. `decisions_log` (ADR index)

Minimal—not essays

```tsv
date	title	status	scope	link
2026-03-16	Secrets Management Standard	accepted	core	/adr/secrets_management.md
2026-03-16	Tech Stack Baseline	accepted	system	/adr/tech_stack_current.md
2026-03-16	QiVault as Source of Truth	accepted	core	/adr/source_of_truth.md
```

👉 Details live in `.md` files (like what we made earlier)

---

### 🔹 4. (Optional but powerful) `capability_map`

This flips your perspective:

```tsv
capability	primary_tool	secondary_tools	notes
notes	QiVault	Obsidian	QiVault is authoritative
automation	Python	n8n	Python first, n8n for events
database	Postgres	Supabase	Supabase optional
secrets	Zoho Vault	none	no duplication allowed
frontend	Cloudflare Pages	none	static-first approach
```

👉 This answers:
> “If I need X… what do I use?”

---

## 🔥 Why this is the correct architecture

### Before (what you were drifting into):
- One table doing everything
- Hard to maintain
- Cognitive overload
- No clear system boundaries

### Now:
- Each table = one job
- Easy to update
- Easy to reason about
- Matches how your brain already works (modular)

---

## ⚠️ Hard Truth (quick check)

If you keep everything in one table:
> You’ll spend more time organizing than building

If you split like this:
> You’ll actually *use* the system

---

## 🎯 Your System (final mental model)

``` id="nq8c0r"
TOOLS → what exists
FLOW → how it connects
DECISIONS → why it exists
CAPABILITIES → how to choose
```

That’s it. That’s QiOne governance.

---

## ✅ What I’d do next (fast, no overthinking)

1. Create folder:
```
/00_system/
  /tables/
  /adr/
```

2. Add:
- `tools_inventory.tsv`
- `architecture_flow.tsv`
- `decisions_log.tsv`

3. Drop the ADR we just made into `/adr/`

4. Stop restructuring and move forward

---

If you want next level after this:
👉 I can wire this into:
- **auto-generated diagrams**
- or a **dashboard view inside your portal**

But don’t jump yet—lock this structure first.

---
