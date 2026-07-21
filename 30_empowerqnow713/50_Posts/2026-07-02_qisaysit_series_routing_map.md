---
layout: page
title: "QiSaysIt Series Routing Map"
slug: "qisaysit-series-routing-map"
summary: "A practical routing guide for deciding which QiSaysIt series a post belongs to."
status: active
visibility: internal
created_at: "2026-07-02T01:47:00-05:00"
updated_at: "2026-07-18T11:03:18-04:00"
author: "Cody J. Rice-Velasquez"
owner: ""
  - "Cody"
tags:
  - qisaysit
  - content-system
  - series-map
  - publishing
keywords:
  - QiSaysIt
  - EmpowerQNow
  - Field Notes
  - Mirrors
  - Power Studies
  - The Onion Effect
  - content routing
aliases:
  - "QiSaysIt Routing Map"
context: "Use this guide when deciding where a post belongs before publishing or filing it."
sensitivity: internal
classification: business_internal
realm_label: "QiSaysIt"
uid: "qisaysit-series-routing-map"
canonical_ref: "qisaysit/series-routing-map"
source_type: manual
template_key: master-template
type: note
---

# QiSaysIt Series Routing Map

## Purpose

This map decides where a QiSaysIt post belongs.

The rule is simple:

> Every post gets one primary series. Tags and cross-series links handle overlap.

Do **not** file the same post into five folders because it “kind of fits.” That turns the system into a glitter-covered junk drawer.

The routing question is:

> What job is this post doing for the reader?

---

## Fast Cheat Sheet

| Post Is Mainly About | Primary Series |
|---|---|
| Doctrine, declaration, sovereignty, public principle | EmpowerQNow |
| A lived moment, event, or daily observation | Field Notes |
| Self-recognition, identity, emotional clarity, relational reflection | Mirrors |
| Control, leverage, manipulation, institutions, money, status, family power | Power Studies |
| Layered healing, deeper truths under the first truth | The Onion Effect |
| Caregiving, unpaid labor, invisible emotional or logistical work | The Invisible Care Bill |
| Tarot, signs, intuition, spiritual messages, symbolic readings | Tarot Signals |
| God/source/unity/spiritual integration | Reflections of One |
| Tools, workflows, Obsidian, QiLabs, publishing systems | Systems |
| Reference material, sacred mappings, source notes, background research | Source Work |

---

## Recommended Front Matter Pattern

```yaml
series: "Mirrors"
series_role: "primary"
cross_series:
  - "The Onion Effect"
  - "Power Studies"
content_type: "essay"
post_status: "draft"
```

Use `series` for the canonical home. Use `cross_series` for overlap.

---

# Series Definitions

## EmpowerQNow

Use **EmpowerQNow** when the post is a flagship doctrine, public principle, declaration, or sovereignty statement.

### Use When

- The post says, “Here is the rule.”
- The post lands as a public truth.
- The post has manifesto energy.
- The post defines your philosophy.
- The post can stand as a core EmpowerQNow teaching.

### Examples

- “Access Is a Privilege”
- “I Am Done Carrying False Blame”
- “Endurance Is Not Obligation”

### Do Not Use When

The post is mostly a private journal entry, raw event recap, or supporting source note.

---

## Field Notes

Use **Field Notes** when the post is anchored in something that happened.

### Use When

- The post begins from a day, moment, conversation, drive, errand, conflict, or body signal.
- The lesson comes from lived experience.
- The reader should feel like they are watching you notice something in real time.

### Examples

- “The Day My Body Said No”
- “I Got in the Car and Realized I Was Done”
- “What the Parking Lot Taught Me”

### Do Not Use When

The post has been polished into a universal principle. At that point, it may belong in EmpowerQNow.

---

## Mirrors

Use **Mirrors** when the post is about recognition.

### Use When

- You are seeing yourself clearly.
- You are seeing someone else clearly.
- You are naming a relational or emotional pattern.
- The post is reflective more than strategic.
- The central movement is, “Oh, that is what this was.”

### Examples

- “I Wasn’t Crazy, I Was Pattern-Matching”
- “The Part of Me That Kept Explaining”
- “When Their Story Became My Mirror”

### Do Not Use When

The post is mainly about power, coercion, or institutional control. That belongs in Power Studies.

---

## Power Studies

Use **Power Studies** when the post analyzes control, leverage, manipulation, coercion, or status.

### Use When

- The post explains a power dynamic.
- The post names manipulation.
- The post examines family systems, institutions, money, reputation, access, or social control.
- The post helps the reader understand how power moves.

### Examples

- “Why People Call Boundaries Disrespect”
- “The Cost of Being the Convenient Scapegoat”
- “When Help Becomes Control”

### Do Not Use When

The post is mostly a personal emotional realization. That belongs in Mirrors or The Onion Effect.

---

## The Onion Effect

Use **The Onion Effect** when the post unfolds through layers.

### Use When

- The first truth reveals a deeper truth.
- The post peels back emotional layers.
- The post moves from surface reaction to root wound.
- The point is the process of realization.

### Examples

- “I Thought I Was Angry. I Was Tired.”
- “Under the Boundary Was Grief”
- “The Truth Beneath the Truth”

### Do Not Use When

The post is one clear reflection with no layered unfolding. That belongs in Mirrors.

---

## The Invisible Care Bill

Use **The Invisible Care Bill** when the post accounts for unpaid, unseen, or undervalued care labor.

### Use When

- The post is about caregiving.
- The post names hidden emotional, physical, financial, or logistical labor.
- The post exposes the cost of being the person everyone assumes will handle it.
- The post is about survival labor that nobody counted.

### Examples

- “The Labor Nobody Counts”
- “They Counted the Hours, Not the Life I Paused”
- “The Care Bill Always Comes Due”

### Do Not Use When

The post is mainly about general power or manipulation without care labor at the center.

---

## Tarot Signals

Use **Tarot Signals** when the post is a reading, sign, symbolic message, or intuition note.

### Use When

- The post interprets tarot.
- The post names a spiritual sign.
- The post processes a message from God, Jesus, source, intuition, or the cards.
- The post is mystical, symbolic, or divinatory in structure.

### Examples

- “Be Still Was the Message”
- “The Cards Said Stop Fighting the Fog”
- “What the Signal Was Trying to Tell Me”

### Routing Rule

| If The Tarot Post Becomes... | Move Or Cross-Link To |
|---|---|
| A public doctrine | EmpowerQNow |
| A personal realization | Mirrors |
| A layered healing essay | The Onion Effect |
| A spiritual unity teaching | Reflections of One |

---

## Reflections of One

Use **Reflections of One** when the post is about unity, God/source, sacred identity, or collective spiritual integration.

### Use When

- The post has devotional or sacred integration energy.
- The post is less about the individual event and more about the universal pattern.
- The post speaks from “I am that we are” energy.

### Examples

- “I Am That We Are”
- “The Self, the Source, and the Signal”
- “What God Mirrors Back”

### Do Not Use When

The post is a practical spiritual reading. That belongs in Tarot Signals.

---

## Systems

Use **Systems** when the post is about operating methods, tools, workflow, structure, or build logic.

### Use When

- The post explains a workflow.
- The post documents QiLabs, QiDex, Obsidian, templates, automation, or publishing rules.
- The post teaches your operating method.
- The post is builder-brain content.

### Examples

- “Why My Notes Need Rules”
- “A Messy System Makes a Sharp Mind Look Chaotic”
- “The Publishing Pipeline Is Part of the Healing”

### Do Not Use When

The post is primarily philosophical. That may belong in EmpowerQNow.

---

## Source Work

Use **Source Work** for reference and support material.

### Use When

- The file maps ideas to sacred texts.
- The file stores research notes.
- The file supports a public post but is not itself the polished essay.
- The file is background architecture.

### Examples

- “EmpowerQNow Mapped to Sacred Teachings”
- “Sacred Teaching Crosswalk”
- “Doctrine Source Notes”

### Important

Source Work is not really a public essay series. It is a supporting shelf.

Recommended front matter:

```yaml
content_type: "reference"
public_status: "supporting"
```

---

# Overlap Tie-Breakers

| If It Fits Both | Choose This As Primary |
|---|---|
| EmpowerQNow + Mirrors | EmpowerQNow if it ends as a public principle; Mirrors if it stays personal |
| Field Notes + Mirrors | Field Notes if the event matters most; Mirrors if the realization matters most |
| Field Notes + Power Studies | Power Studies if the post analyzes the system; Field Notes if it narrates the moment |
| Tarot Signals + EmpowerQNow | Tarot Signals for the reading; EmpowerQNow for the doctrine extracted from it |
| Invisible Care Bill + Power Studies | Invisible Care Bill if care labor is central; Power Studies if leverage/control is central |
| Onion Effect + Mirrors | Onion Effect if it unfolds in layers; Mirrors if it is one clean reflection |
| Systems + EmpowerQNow | Systems if it teaches the method; EmpowerQNow if it teaches the philosophy |

---

# Folder Role Map

## Public Essay Series

```text
EmpowerQNow
Field Notes
Mirrors
Power Studies
The Onion Effect
The Invisible Care Bill
Tarot Signals
Reflections of One
Systems
```

## Support / Reference Area

```text
Source Work
```

## Long-Form Collections

```text
The Awakening of Angela
Breaking the Silence
You Thought You Knew Me
The QiDex Manual of Me
Paid in Full
```

Posts can link to books. Do not file regular posts inside books unless they are chapters, excerpts, or source drafts.

---

# Final Routing Principle

EmpowerQNow is the umbrella brand.

The series are channels inside the voice.

So do not ask:

> Is this EmpowerQNow or Mirrors?

Ask:

> Is this a flagship doctrine piece, or is it one of the sub-series doing a specific job?

That question keeps the system clean.
