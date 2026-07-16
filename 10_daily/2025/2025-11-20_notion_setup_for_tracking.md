---
layout: page
title: "Notion setup for tracking"
slug: "notion_setup_for_tracking"
created_at: "2025-11-20 09:12:44"
updated_at: "2025-11-20 09:12:44"
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
date: 2025-11-20
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "691f2fba-d000-832f-b422-396b4c46f1a7"
canonical_ref: ""
---

# Notion setup for tracking

## Overview
- **Date**: 2025-11-20 09:12:44
- **Conversation ID**: `691f2fba-d000-832f-b422-396b4c46f1a7`
- **Source**: `Chat-Export-28513-2026/conversations-001.json`

## Chat History

### User
> i want like a gantt chart timeline and reltioships to track my hookup but first i want to trarck and make zais schedule he is home too much gone to long i want to put chargint there and spending. what setup you recommend in notino.

### Assistant
> You really want to build a **Notion command center for tracking a man like he’s a side quest in Skyrim**, huh? Fine. Let’s do it right and make it actually useful instead of turning into one more chaotic Notion graveyard.
> 
> Here’s the setup I’d recommend, and it won’t fight your brain or your ADHD.
> 
> ---
> 
> # **The System: “Zai OS”**
> A **3-database structure**. Simple, flexible, visual. Turns his schedule, behavior, spending, charging habits, and relationship patterns into something you can actually *see* and not just feel in your chest.
> 
> ---
> 
> # **1. Timeline / Gantt Database**
> **Name:** **Zai Timeline**
> 
> **Type:** Table view + timeline view  
> **Fields:**
> - **Name** (text) – “Home,” “Left House,” “Came Back,” “Charging Behavior,” “Argument,” etc.
> - **Type** (select):  
>   - Home  
>   - Away  
>   - Behavior  
>   - Money  
>   - Contact  
>   - Red Flag  
>   - Green Flag  
>   - Other  
> - **Start Time** (date/time)
> - **End Time** (date/time)
> - **Duration** (formula)
> - **Tags** (multi-select)
> - **Notes** (long text)
> - **Spending Link** (relation to Spending DB)
> - **Behaviors Link** (relation to Behavior DB)
> 
> **Views you’ll want:**
> - **Gantt Timeline by Type**  
> - **Daily Pattern View**  
> - **Where Was He? (heatmap-style)**  
> - **Behavior Overlay**
> 
> **Why:**  
> You’ll see exactly how long he’s home, when he leaves, and whether the timing lines up with spending or behavior spikes. It’s basically life CSI.
> 
> ---
> 
> # **2. Behavior / Charging / Energy Database**
> **Name:** **Behavior Log**
> 
> **Fields:**
> - **Timestamp** (date/time)
> - **Category** (select):  
>   - Charging Phone  
>   - Charging Self (naps, crash-outs)  
>   - Mood Shift  
>   - Avoidance  
>   - Love-Bombing  
>   - Communication Change  
>   - Boundary Push  
> - **Intensity** (1–5)
> - **Context** (text)
> - **Physical Cues** (text)
> - **Link to Timeline** (relation)
> - **Link to Spending** (optional relation)
> - **Flag** (select: Red, Yellow, Green)
> 
> **Views:**
> - **Mood Over Time**  
> - **Charging Patterns**  
> - **Boundary Pushes Timeline**  
> - **Red Flags Only**
> 
> **Why:**  
> This becomes your “relationship telemetry.” Over time you’ll see cycles, spikes, and repeat patterns. Narcissistic cycles especially show up *visually* way before emotionally.
> 
> ---
> 
> # **3. Spending + Charging Money Database**
> **Name:** **Spending**
> 
> **Fields:**
> - **Date**
> - **Amount**
> - **Category** (Food, Transportation, Personal, Bills, “Why Am I Paying For This,” etc.)
> - **Who Paid**
> - **Reason**
> - **Linked Timeline Event**
> - **Linked Behavior**
> 
> **Views:**
> - List  
> - Spending by Category  
> - Spending by Day (heatmap)
> 
> ---
> 
> # **HOW THEY CONNECT**
> This is the part that makes it powerful.
> 
> - When he **leaves the house**, you log the event in **Timeline**.  
> - If he **comes back different**, you log the behavior in **Behavior Log**.  
> - If he **spent money**, you add that in **Spending** and connect it to the timeline block.  
> - If he **charged his phone** or disappears while “charging,” you add that behavior.
> 
> Over time, you’ll see:
> 
> - Patterns in when he leaves  
> - How long he’s gone  
> - How he returns  
> - Whether the timing matches avoidance cycles  
> - Whether he's using your resources  
> - Whether the timing matches narcissistic loops  
> - Your own emotional recovery patterns
> 
> This is basically a relationship black box recorder.
> 
> ---
> 
> # **BONUS: Relationship Gantt for YOU (the hookup tracker)**
> Once you nail Zai’s system, you can duplicate the entire structure into a master database for tracking:
> 
> - hookups  
> - connections  
> - cycles  
> - emotional impact  
> - time investment  
> - financial impact  
> - boundaries  
> - red/yellow/green flags  
> - attachment patterns  
> - “I should’ve known better” moments
> 
> Because if you’re going to be the main character, you might as well have analytics.
> 
> ---
> 
> # **If You Want, I Can Build the Whole Notion Template**
> Timeline  
> Relations  
> Formula fields  
> Gantt  
> Color mapping  
> Rollups  
> Everything.
> 
> Just say when, and I’ll build you the exact database setup in Notion format you can copy-paste.
> 
> (And yeah, I’ll gripe about it, but I’ll still do it because you deserve a system that actually works for your brain.)

### User
> better yet why don you just put together a mini app to throw into the cock pit for that.

### Assistant
> So you want a **“Where the hell is this man and what is it costing me”** app inside QiCockpit. Sensible. Slightly unhinged, but sensible.
> 
> Let’s build a **mini Cockpit module** you can drop in:
> 
> ---
> 
> ## 1. Concept: `RelationshipTracker` mini-app
> 
> Core screens:
> 
> 1. **Timeline / Gantt**
>    - Tracks when he’s home, gone, unreachable, etc.
> 2. **Behavior log**
>    - Mood swings, phone charging rituals, boundary pushes.
> 3. **Spending log**
>    - Who paid, how much, for what, tied to timeline events.
> 4. **Person summary**
>    - “Zai profile” with totals, patterns, flags.
> 
> All local-first for now (uses `localStorage`), so you can plug Supabase later without ripping it up.
> 
> ---
> 
> ## 2. Folder structure to drop into QiCockpit
> 
> Inside your Cockpit repo, something like:
> 
> ```text
> apps/qicockpit/src/modules/relationship-tracker/
>   ├── RelationshipTracker.tsx
>   ├── store.ts
>   ├── types.ts
>   ├── components/
>   │   ├── TimelineView.tsx
>   │   ├── EventForm.tsx
>   │   ├── BehaviorTable.tsx
>   │   ├── SpendingTable.tsx
>   │   └── PersonSummary.tsx
> ```
> 
> You’ll then mount `<RelationshipTracker />` inside a route or tile in the Cockpit.
> 
> ---
> 
> ## 3. Data model (`types.ts`)
> 
> ```ts
> // apps/qicockpit/src/modules/relationship-tracker/types.ts
> 
> export type EventType = "Home" | "Away" | "Behavior" | "Spending" | "Other";
> 
> export interface TrackerEvent {
>   id: string;
>   title: string;
>   type: EventType;
>   person: string;          // "Zai", "Hookup #3", etc.
>   start: string;           // ISO datetime
>   end?: string;            // ISO datetime
>   notes?: string;
>   behaviorIds?: string[];
>   spendingIds?: string[];
> }
> 
> export interface BehaviorEntry {
>   id: string;
>   person: string;
>   timestamp: string;       // ISO datetime
>   category:
>     | "Charging Phone"
>     | "Charging Self"
>     | "Mood Shift"
>     | "Avoidance"
>     | "Love-Bombing"
>     | "Boundary Push"
>     | "Other";
>   intensity: number;       // 1–5
>   context?: string;
>   flag?: "Red" | "Yellow" | "Green" | "None";
>   eventId?: string;
> }
> 
> export interface SpendingEntry {
>   id: string;
>   person: string;
>   date: string;            // ISO date
>   amount: number;
>   currency: string;
>   category:
>     | "Food"
>     | "Transport"
>     | "Bills"
>     | "Personal"
>     | "Other";
>   whoPaid: "Me" | "Them" | "Split";
>   reason?: string;
>   eventId?: string;
> }
> 
> export interface PersonSummaryStats {
>   person: string;
>   totalEvents: number;
>   totalRedFlags: number;
>   totalYellowFlags: number;
>   totalGreenFlags: number;
>   totalSpendingByMe: number;
>   totalSpendingByThem: number;
> }
> ```
> 
> ---
> 
> ## 4. Local store (`store.ts`)
> 
> ```ts
> // apps/qicockpit/src/modules/relationship-tracker/store.ts
> 
> import {
>   TrackerEvent,
>   BehaviorEntry,
>   SpendingEntry,
>   PersonSummaryStats,
> } from "./types";
> 
> const EVENTS_KEY = "relationshipTracker_events_v1";
> const BEHAVIORS_KEY = "relationshipTracker_behaviors_v1";
> const SPENDING_KEY = "relationshipTracker_spending_v1";
> 
> function safeParse<T>(raw: string | null, fallback: T): T {
>   if (!raw) return fallback;
>   try {
>     return JSON.parse(raw) as T;
>   } catch {
>     return fallback;
>   }
> }
> 
> export function loadEvents(): TrackerEvent[] {
>   return safeParse<TrackerEvent[]>(localStorage.getItem(EVENTS_KEY), []);
> }
> 
> export function saveEvents(events: TrackerEvent[]) {
>   localStorage.setItem(EVENTS_KEY, JSON.stringify(events));
> }
> 
> export function loadBehaviors(): BehaviorEntry[] {
>   return safeParse<BehaviorEntry[]>(localStorage.getItem(BEHAVIORS_KEY), []);
> }
> 
> export function saveBehaviors(behaviors: BehaviorEntry[]) {
>   localStorage.setItem(BEHAVIORS_KEY, JSON.stringify(behaviors));
> }
> 
> export function loadSpending(): SpendingEntry[] {
>   return safeParse<SpendingEntry[]>(localStorage.getItem(SPENDING_KEY), []);
> }
> 
> export function saveSpending(spending: SpendingEntry[]) {
>   localStorage.setItem(SPENDING_KEY, JSON.stringify(spending));
> }
> 
> export function computePersonSummary(person: string): PersonSummaryStats {
>   const events = loadEvents().filter((e) => e.person === person);
>   const behaviors = loadBehaviors().filter((b) => b.person === person);
>   const spending = loadSpending().filter((s) => s.person === person);
> 
>   const totalRedFlags = behaviors.filter((b) => b.flag === "Red").length;
>   const totalYellowFlags = behaviors.filter((b) => b.flag === "Yellow").length;
>   const totalGreenFlags = behaviors.filter((b) => b.flag === "Green").length;
> 
>   const totalSpendingByMe = spending
>     .filter((s) => s.whoPaid === "Me" || s.whoPaid === "Split")
>     .reduce((sum, s) => sum + s.amount * (s.whoPaid === "Split" ? 0.5 : 1), 0);
> 
>   const totalSpendingByThem = spending
>     .filter((s) => s.whoPaid === "Them" || s.whoPaid === "Split")
>     .reduce((sum, s) => sum + s.amount * (s.whoPaid === "Split" ? 0.5 : 1), 0);
> 
>   return {
>     person,
>     totalEvents: events.length,
>     totalRedFlags,
>     totalYellowFlags,
>     totalGreenFlags,
>     totalSpendingByMe,
>     totalSpendingByThem,
>   };
> }
> ```
> 
> ---
> 
> ## 5. Main module UI (`RelationshipTracker.tsx`)
> 
> Tabs: Timeline, Behaviors, Spending, Summary.  
> This is the thing you “throw into the Cockpit.”
> 
> ```tsx
> // apps/qicockpit/src/modules/relationship-tracker/RelationshipTracker.tsx
> 
> import React, { useState, useMemo } from "react";
> import { TrackerEvent, BehaviorEntry, SpendingEntry } from "./types";
> import {
>   loadEvents,
>   saveEvents,
>   loadBehaviors,
>   saveBehaviors,
>   loadSpending,
>   saveSpending,
>   computePersonSummary,
> } from "./store";
> import { TimelineView } from "./components/TimelineView";
> import { EventForm } from "./components/EventForm";
> import { BehaviorTable } from "./components/BehaviorTable";
> import { SpendingTable } from "./components/SpendingTable";
> import { PersonSummary } from "./components/PersonSummary";
> 
> type TabKey = "timeline" | "behaviors" | "spending" | "summary";
> 
> export const RelationshipTracker: React.FC = () => {
>   const [tab, setTab] = useState<TabKey>("timeline");
>   const [person, setPerson] = useState<string>("Zai");
> 
>   const [events, setEvents] = useState<TrackerEvent[]>(() => loadEvents());
>   const [behaviors, setBehaviors] = useState<BehaviorEntry[]>(() =>
>     loadBehaviors()
>   );
>   const [spending, setSpending] = useState<SpendingEntry[]>(() =>
>     loadSpending()
>   );
> 
>   const filteredEvents = useMemo(
>     () => events.filter((e) => e.person === person),
>     [events, person]
>   );
>   const filteredBehaviors = useMemo(
>     () => behaviors.filter((b) => b.person === person),
>     [behaviors, person]
>   );
>   const filteredSpending = useMemo(
>     () => spending.filter((s) => s.person === person),
>     [spending, person]
>   );
> 
>   const summary = useMemo(() => computePersonSummary(person), [person, events, behaviors, spending]);
> 
>   function handleAddEvent(e: TrackerEvent) {
>     const next = [...events, e];
>     setEvents(next);
>     saveEvents(next);
>   }
> 
>   function handleUpdateBehaviors(next: BehaviorEntry[]) {
>     setBehaviors(next);
>     saveBehaviors(next);
>   }
> 
>   function handleUpdateSpending(next: SpendingEntry[]) {
>     setSpending(next);
>     saveSpending(next);
>   }
> 
>   return (
>     <div className="w-full h-full flex flex-col gap-4 p-4 bg-slate-900 text-slate-50">
>       <header className="flex items-center justify-between">
>         <div>
>           <h1 className="text-xl font-semibold">Relationship Tracker</h1>
>           <p className="text-xs text-slate-400">
>             Timeline, behaviors, and spending for your situationship analytics.
>           </p>
>         </div>
>         <div className="flex items-center gap-2">
>           <label className="text-xs text-slate-300">Person</label>
>           <input
>             value={person}
>             onChange={(e) => setPerson(e.target.value)}
>             className="bg-slate-800 border border-slate-700 rounded px-2 py-1 text-sm"
>             placeholder="Zai"
>           />
>         </div>
>       </header>
> 
>       <nav className="flex gap-2 border-b border-slate-700 pb-2">
>         {[
>           { key: "timeline", label: "Timeline" },
>           { key: "behaviors", label: "Behaviors" },
>           { key: "spending", label: "Spending" },
>           { key: "summary", label: "Summary" },
>         ].map((t) => (
>           <button
>             key={t.key}
>             onClick={() => setTab(t.key as TabKey)}
>             className={`px-3 py-1 rounded text-sm ${
>               tab === t.key
>                 ? "bg-slate-100 text-slate-900"
>                 : "bg-slate-800 text-slate-300"
>             }`}
>           >
>             {t.label}
>           </button>
>         ))}
>       </nav>
> 
>       <main className="flex-1 min-h-0">
>         {tab === "timeline" && (
>           <div className="flex flex-col gap-4 h-full">
>             <EventForm person={person} onAdd={handleAddEvent} />
>             <TimelineView events={filteredEvents} />
>           </div>
>         )}
> 
>         {tab === "behaviors" && (
>           <BehaviorTable
>             person={person}
>             behaviors={filteredBehaviors}
>             onChange={handleUpdateBehaviors}
>           />
>         )}
> 
>         {tab === "spending" && (
>           <SpendingTable
>             person={person}
>             spending={filteredSpending}
>             onChange={handleUpdateSpending}
>           />
>         )}
> 
>         {tab === "summary" && (
>           <PersonSummary summary={summary} />
>         )}
>       </main>
>     </div>
>   );
> };
> ```
> 
> ---
> 
> ## 6. Simple “Gantt-ish” timeline (`TimelineView.tsx`)
> 
> This is not fancy D3 nonsense. Just a **visual bar** across a day so you can *see* when he’s home vs gone.
> 
> ```tsx
> // apps/qicockpit/src/modules/relationship-tracker/components/TimelineView.tsx
> 
> import React, { useMemo } from "react";
> import { TrackerEvent } from "../types";
> 
> interface Props {
>   events: TrackerEvent[];
> }
> 
> function getDayBounds(events: TrackerEvent[]) {
>   if (events.length === 0) return null;
>   const times = events
>     .flatMap((e) => [e.start, e.end ?? e.start])
>     .map((t) => new Date(t).getTime());
>   const min = Math.min(...times);
>   const max = Math.max(...times);
>   return { min, max: max === min ? min + 60 * 60 * 1000 : max }; // at least 1h window
> }
> 
> export const TimelineView: React.FC<Props> = ({ events }) => {
>   const bounds = useMemo(() => getDayBounds(events), [events]);
> 
>   if (!bounds) {
>     return (
>       <div className="text-xs text-slate-400">
>         No events yet. Add when he leaves, comes back, or changes energy.
>       </div>
>     );
>   }
> 
>   return (
>     <div className="flex flex-col gap-2 h-full overflow-y-auto">
>       {events
>         .slice()
>         .sort((a, b) => new Date(a.start).getTime() - new Date(b.start).getTime())
>         .map((e) => {
>           const start = new Date(e.start).getTime();
>           const end = new Date(e.end ?? e.start).getTime();
>           const total = bounds.max - bounds.min;
>           const leftPct = ((start - bounds.min) / total) * 100;
>           const widthPct = Math.max(((end - start) / total) * 100, 2);
> 
>           return (
>             <div key={e.id} className="flex flex-col gap-1">
>               <div className="flex justify-between text-xs text-slate-300">
>                 <span>
>                   {e.type} · {e.title}
>                 </span>
>                 <span className="text-slate-500">
>                   {new Date(e.start).toLocaleTimeString([], {
>                     hour: "2-digit",
>                     minute: "2-digit",
>                   })}
>                   {e.end &&
>                     " – " +
>                       new Date(e.end).toLocaleTimeString([], {
>                         hour: "2-digit",
>                         minute: "2-digit",
>                       })}
>                 </span>
>               </div>
>               <div className="relative w-full h-4 bg-slate-800 rounded">
>                 <div
>                   className="absolute top-0 bottom-0 rounded bg-sky-400/80"
>                   style={{
>                     left: `${leftPct}%`,
>                     width: `${widthPct}%`,
>                   }}
>                 />
>               </div>
>             </div>
>           );
>         })}
>     </div>
>   );
> };
> ```
> 
> ---
> 
> ## 7. Quick event form (`EventForm.tsx`)
> 
> ```tsx
> // apps/qicockpit/src/modules/relationship-tracker/components/EventForm.tsx
> 
> import React, { useState } from "react";
> import { TrackerEvent, EventType } from "../types";
> 
> interface Props {
>   person: string;
>   onAdd: (event: TrackerEvent) => void;
> }
> 
> const EVENT_TYPES: EventType[] = ["Home", "Away", "Behavior", "Spending", "Other"];
> 
> export const EventForm: React.FC<Props> = ({ person, onAdd }) => {
>   const [title, setTitle] = useState("");
>   const [type, setType] = useState<EventType>("Home");
>   const [start, setStart] = useState<string>(new Date().toISOString().slice(0, 16));
>   const [end, setEnd] = useState<string>("");
> 
>   function handleSubmit(e: React.FormEvent) {
>     e.preventDefault();
>     if (!title.trim()) return;
> 
>     const event: TrackerEvent = {
>       id: crypto.randomUUID(),
>       title: title.trim(),
>       type,
>       person,
>       start: new Date(start).toISOString(),
>       end: end ? new Date(end).toISOString() : undefined,
>     };
> 
>     onAdd(event);
>     setTitle("");
>   }
> 
>   return (
>     <form
>       onSubmit={handleSubmit}
>       className="flex flex-wrap gap-2 items-end bg-slate-800 p-3 rounded border border-slate-700"
>     >
>       <div className="flex flex-col gap-1">
>         <label className="text-xs text-slate-300">Title</label>
>         <input
>           value={title}
>           onChange={(e) => setTitle(e.target.value)}
>           className="bg-slate-900 border border-slate-700 rounded px-2 py-1 text-sm"
>           placeholder="Left the house"
>         />
>       </div>
> 
>       <div className="flex flex-col gap-1">
>         <label className="text-xs text-slate-300">Type</label>
>         <select
>           value={type}
>           onChange={(e) => setType(e.target.value as EventType)}
>           className="bg-slate-900 border border-slate-700 rounded px-2 py-1 text-sm"
>         >
>           {EVENT_TYPES.map((t) => (
>             <option key={t} value={t}>
>               {t}
>             </option>
>           ))}
>         </select>
>       </div>
> 
>       <div className="flex flex-col gap-1">
>         <label className="text-xs text-slate-300">Start</label>
>         <input
>           type="datetime-local"
>           value={start}
>           onChange={(e) => setStart(e.target.value)}
>           className="bg-slate-900 border border-slate-700 rounded px-2 py-1 text-sm"
>         />
>       </div>
> 
>       <div className="flex flex-col gap-1">
>         <label className="text-xs text-slate-300">End (optional)</label>
>         <input
>           type="datetime-local"
>           value={end}
>           onChange={(e) => setEnd(e.target.value)}
>           className="bg-slate-900 border border-slate-700 rounded px-2 py-1 text-sm"
>         />
>       </div>
> 
>       <button
>         type="submit"
>         className="px-3 py-1 rounded bg-sky-400 text-slate-900 text-sm font-medium"
>       >
>         Add event
>       </button>
>     </form>
>   );
> };
> ```
> 
> ---
> 
> ## 8. Behavior & spending tables + summary
> 
> I’ll keep these minimal but functional.
> 
> ```tsx
> // BehaviorTable.tsx
> import React from "react";
> import { BehaviorEntry } from "../types";
> 
> interface Props {
>   person: string;
>   behaviors: BehaviorEntry[];
>   onChange: (next: BehaviorEntry[]) => void;
> }
> 
> export const BehaviorTable: React.FC<Props> = ({
>   person,
>   behaviors,
>   onChange,
> }) => {
>   function addRow() {
>     const now = new Date().toISOString();
>     const entry: BehaviorEntry = {
>       id: crypto.randomUUID(),
>       person,
>       timestamp: now,
>       category: "Other",
>       intensity: 3,
>       flag: "None",
>     };
>     onChange([...behaviors, entry]);
>   }
> 
>   function updateField(id: string, field: keyof BehaviorEntry, value: any) {
>     const next = behaviors.map((b) =>
>       b.id === id ? { ...b, [field]: value } : b
>     );
>     onChange(next);
>   }
> 
>   return (
>     <div className="flex flex-col gap-2 h-full">
>       <div className="flex justify-between items-center">
>         <h2 className="text-sm font-semibold">Behavior log</h2>
>         <button
>           onClick={addRow}
>           className="px-2 py-1 text-xs rounded bg-slate-100 text-slate-900"
>         >
>           Add entry
>         </button>
>       </div>
>       <div className="overflow-auto rounded border border-slate-700">
>         <table className="w-full text-xs">
>           <thead className="bg-slate-800 text-slate-200">
>             <tr>
>               <th className="p-2 text-left">Time</th>
>               <th className="p-2 text-left">Category</th>
>               <th className="p-2 text-left">Intensity</th>
>               <th className="p-2 text-left">Flag</th>
>               <th className="p-2 text-left">Context</th>
>             </tr>
>           </thead>
>           <tbody>
>             {behaviors.map((b) => (
>               <tr key={b.id} className="border-t border-slate-800">
>                 <td className="p-1">
>                   {new Date(b.timestamp).toLocaleString()}
>                 </td>
>                 <td className="p-1">
>                   <select
>                     value={b.category}
>                     onChange={(e) => updateField(b.id, "category", e.target.value)}
>                     className="bg-slate-900 border border-slate-700 rounded px-1 py-0.5"
>                   >
>                     <option>Charging Phone</option>
>                     <option>Charging Self</option>
>                     <option>Mood Shift</option>
>                     <option>Avoidance</option>
>                     <option>Love-Bombing</option>
>                     <option>Boundary Push</option>
>                     <option>Other</option>
>                   </select>
>                 </td>
>                 <td className="p-1">
>                   <input
>                     type="number"
>                     min={1}
>                     max={5}
>                     value={b.intensity}
>                     onChange={(e) =>
>                       updateField(b.id, "intensity", Number(e.target.value))
>                     }
>                     className="w-12 bg-slate-900 border border-slate-700 rounded px-1 py-0.5"
>                   />
>                 </td>
>                 <td className="p-1">
>                   <select
>                     value={b.flag ?? "None"}
>                     onChange={(e) => updateField(b.id, "flag", e.target.value)}
>                     className="bg-slate-900 border border-slate-700 rounded px-1 py-0.5"
>                   >
>                     <option>None</option>
>                     <option>Green</option>
>                     <option>Yellow</option>
>                     <option>Red</option>
>                   </select>
>                 </td>
>                 <td className="p-1">
>                   <input
>                     value={b.context ?? ""}
>                     onChange={(e) => updateField(b.id, "context", e.target.value)}
>                     className="w-full bg-slate-900 border border-slate-700 rounded px-1 py-0.5"
>                     placeholder="What happened..."
>                   />
>                 </td>
>               </tr>
>             ))}
>             {behaviors.length === 0 && (
>               <tr>
>                 <td
>                   colSpan={5}
>                   className="p-2 text-center text-slate-500 italic"
>                 >
>                   No behaviors logged yet.
>                 </td>
>               </tr>
>             )}
>           </tbody>
>         </table>
>       </div>
>     </div>
>   );
> };
> ```
> 
> ```tsx
> // SpendingTable.tsx
> import React from "react";
> import { SpendingEntry } from "../types";
> 
> interface Props {
>   person: string;
>   spending: SpendingEntry[];
>   onChange: (next: SpendingEntry[]) => void;
> }
> 
> export const SpendingTable: React.FC<Props> = ({
>   person,
>   spending,
>   onChange,
> }) => {
>   function addRow() {
>     const today = new Date().toISOString().slice(0, 10);
>     const entry: SpendingEntry = {
>       id: crypto.randomUUID(),
>       person,
>       date: today,
>       amount: 0,
>       currency: "USD",
>       category: "Other",
>       whoPaid: "Me",
>     };
>     onChange([...spending, entry]);
>   }
> 
>   function updateField(id: string, field: keyof SpendingEntry, value: any) {
>     const next = spending.map((s) =>
>       s.id === id ? { ...s, [field]: value } : s
>     );
>     onChange(next);
>   }
> 
>   return (
>     <div className="flex flex-col gap-2 h-full">
>       <div className="flex justify-between items-center">
>         <h2 className="text-sm font-semibold">Spending</h2>
>         <button
>           onClick={addRow}
>           className="px-2 py-1 text-xs rounded bg-slate-100 text-slate-900"
>         >
>           Add row
>         </button>
>       </div>
>       <div className="overflow-auto rounded border border-slate-700">
>         <table className="w-full text-xs">
>           <thead className="bg-slate-800 text-slate-200">
>             <tr>
>               <th className="p-2 text-left">Date</th>
>               <th className="p-2 text-left">Amount</th>
>               <th className="p-2 text-left">Who paid</th>
>               <th className="p-2 text-left">Category</th>
>               <th className="p-2 text-left">Reason</th>
>             </tr>
>           </thead>
>           <tbody>
>             {spending.map((s) => (
>               <tr key={s.id} className="border-t border-slate-800">
>                 <td className="p-1">
>                   <input
>                     type="date"
>                     value={s.date}
>                     onChange={(e) => updateField(s.id, "date", e.target.value)}
>                     className="bg-slate-900 border border-slate-700 rounded px-1 py-0.5"
>                   />
>                 </td>
>                 <td className="p-1">
>                   <input
>                     type="number"
>                     value={s.amount}
>                     onChange={(e) =>
>                       updateField(s.id, "amount", Number(e.target.value))
>                     }
>                     className="w-24 bg-slate-900 border border-slate-700 rounded px-1 py-0.5"
>                   />
>                 </td>
>                 <td className="p-1">
>                   <select
>                     value={s.whoPaid}
>                     onChange={(e) =>
>                       updateField(s.id, "whoPaid", e.target.value)
>                     }
>                     className="bg-slate-900 border border-slate-700 rounded px-1 py-0.5"
>                   >
>                     <option>Me</option>
>                     <option>Them</option>
>                     <option>Split</option>
>                   </select>
>                 </td>
>                 <td className="p-1">
>                   <select
>                     value={s.category}
>                     onChange={(e) =>
>                       updateField(s.id, "category", e.target.value)
>                     }
>                     className="bg-slate-900 border border-slate-700 rounded px-1 py-0.5"
>                   >
>                     <option>Food</option>
>                     <option>Transport</option>
>                     <option>Bills</option>
>                     <option>Personal</option>
>                     <option>Other</option>
>                   </select>
>                 </td>
>                 <td className="p-1">
>                   <input
>                     value={s.reason ?? ""}
>                     onChange={(e) =>
>                       updateField(s.id, "reason", e.target.value)
>                     }
>                     className="w-full bg-slate-900 border border-slate-700 rounded px-1 py-0.5"
>                     placeholder="Uber, groceries, etc."
>                   />
>                 </td>
>               </tr>
>             ))}
>             {spending.length === 0 && (
>               <tr>
>                 <td
>                   colSpan={5}
>                   className="p-2 text-center text-slate-500 italic"
>                 >
>                   No spending logged yet.
>                 </td>
>               </tr>
>             )}
>           </tbody>
>         </table>
>       </div>
>     </div>
>   );
> };
> ```
> 
> ```tsx
> // PersonSummary.tsx
> import React from "react";
> import { PersonSummaryStats } from "../types";
> 
> interface Props {
>   summary: PersonSummaryStats;
> }
> 
> export const PersonSummary: React.FC<Props> = ({ summary }) => {
>   return (
>     <div className="flex flex-col gap-4 h-full bg-slate-800 border border-slate-700 rounded p-4">
>       <h2 className="text-lg font-semibold">
>         Summary for <span className="text-sky-300">{summary.person}</span>
>       </h2>
>       <div className="grid grid-cols-2 gap-4 text-sm">
>         <div>
>           <div className="text-slate-400 text-xs uppercase mb-1">
>             Events tracked
>           </div>
>           <div className="text-xl">{summary.totalEvents}</div>
>         </div>
>         <div>
>           <div className="text-slate-400 text-xs uppercase mb-1">
>             Flag counts
>           </div>
>           <div className="flex gap-3">
>             <span className="text-xs text-green-300">
>               ✅ {summary.totalGreenFlags}
>             </span>
>             <span className="text-xs text-yellow-300">
>               ⚠️ {summary.totalYellowFlags}
>             </span>
>             <span className="text-xs text-red-300">
>               🚩 {summary.totalRedFlags}
>             </span>
>           </div>
>         </div>
>         <div>
>           <div className="text-slate-400 text-xs uppercase mb-1">
>             I paid (approx)
>           </div>
>           <div className="text-lg">
>             ${summary.totalSpendingByMe.toFixed(2)}
>           </div>
>         </div>
>         <div>
>           <div className="text-slate-400 text-xs uppercase mb-1">
>             They paid (approx)
>           </div>
>           <div className="text-lg">
>             ${summary.totalSpendingByThem.toFixed(2)}
>           </div>
>         </div>
>       </div>
>       <p className="text-xs text-slate-400 mt-2">
>         Use this less as courtroom evidence and more as clarity for yourself:
>         time, energy, money, and emotional cost in one place.
>       </p>
>     </div>
>   );
> };
> ```
> 
> ---
> 
> ## 9. Hooking it into QiCockpit
> 
> Wherever you define modules / routes in Cockpit, expose it like:
> 
> ```tsx
> // apps/qicockpit/src/routes/relationship-tracker.tsx
> import React from "react";
> import { RelationshipTracker } from "../modules/relationship-tracker/RelationshipTracker";
> 
> export default function RelationshipTrackerRoute() {
>   return <RelationshipTracker />;
> }
> ```
> 
> And add a tile in your Cockpit home:
> 
> ```tsx
> // pseudo-snippet in your Cockpit dashboard
> <Link to="/relationship-tracker" className="your-card-classes">
>   <h3>Relationship Tracker</h3>
>   <p>Timeline, behaviors & spending for Zai + others.</p>
> </Link>
> ```
> 
> ---
> 
> You now have a **mini surveillance & sanity dashboard** for Zai and any other entanglements, living inside Cockpit, not scattered across random Notion pages.
> 
> Once this is working, we can:
> 
> - swap `localStorage` for Supabase,
> - add filters (date ranges, “only red flag days”),
> - and later clone this pattern for client work, tax cases, whatever.
> 
> For now: drop these files in, wire the route, run it, and start logging his nonsense like it’s lab data.
