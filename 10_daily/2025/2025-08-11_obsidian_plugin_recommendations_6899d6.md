---
title: "Obsidian plugin recommendations"
date: "2025-08-11"
created_at: "2025-08-11T11:39:16.831708+00:00"
conversation_id: "6899d662-54a8-832d-8e41-632f5132c37d"
tags:
  - ai_chat
  - export
---

# Obsidian plugin recommendations

> **Date:** 2025-08-11 | **Conversation ID:** `6899d662-54a8-832d-8e41-632f5132c37d`

---

### **User**
waht obsidian plugins do you recommend

---

### **Assistant**
Obsidian has so many plugins that picking without a plan is like trying to grocery shop hungry — you’ll end up with ten kinds of chips and no dinner.  
Here’s the lean-but-lethal lineup I recommend, grouped by what they’ll actually *do* for you instead of just looking shiny:  

---

**Core workflow / structure**  
- **Templater** – Advanced templates that pull in variables, dates, and dynamic data. Your notes stop being static text and start being machines.  
- **Dataview** – Turn your notes into database tables, queries, and dashboards. Great for tracking projects, tasks, and assets without juggling multiple apps.  
- **Periodic Notes** – Automates daily, weekly, monthly note creation and linking. Your timeline stays tidy.  
- **Calendar** – Just what it says. Works great with Periodic Notes for planning and review cycles.  

**Project & task control**  
- **Tasks** – Powerful to-do lists with filters, queries, recurring tasks. Works seamlessly with Dataview.  
- **Kanban** – Boards right inside Obsidian, linked to your notes. Good for tracking deliverables without leaving your vault.  
- **Project Planner** – Gantt-style timelines and dependencies for multi-step chaos wrangling.  

**Search & knowledge surfacing**  
- **Omnisearch** – Fuzzy search so you can find things even if your brain forgets exact words.  
- **Breadcrumbs** – Lets you define and visualize hierarchical relationships between notes.  
- **Quick Switcher++** – Fast jumping between notes with smarter matching.  

**Automation & integrations**  
- **QuickAdd** – Shortcut-driven note creation, capturing inputs and feeding templates in seconds.  
- **Advanced URI** – Deep links that can open a vault to a specific block, query, or command — perfect for integrations with other apps.  
- **Text Expander** – Type “/addr” and have it expand to your full business address or a block of boilerplate.  

**Visual & navigation upgrades**  
- **Excalidraw** – Hand-drawn style diagrams and mind maps embedded in notes.  
- **Graph Analysis** – Gives actual stats on your note network and helps find orphans.  
- **Sliding Panes (Andy Matuschak Mode)** – Side-by-side horizontal panes for a more “wiki” feel.  

**Safety nets**  
- **Version History Diff** – Compare changes between note versions visually.  
- **Note Refactor** – Split a note into smaller ones without losing backlinks.  
- **Linter** – Cleans and formats your markdown automatically so it’s not a formatting dumpster fire.  

---

If you want, I can put together a **QiLife-ready Obsidian stack** that’s basically preconfigured with Dataview dashboards, QuickAdd commands, and your vault folder hierarchy so you just drop it in and go.  
That way you’re not stuck hunting through the community plugins store like a raccoon in a thrift shop.

---

### **User**
for the templator what is the system message. , whrre do i find my google client info for my calender and contact sysn.  waht do i turtn on slash fill out on linter

---

### **Assistant**
Cute chaos, wrong wires. You mashed three different things together. Let’s untangle it and actually make your vault work.

# 1) “Templater system message”
Templater doesn’t use a “system message.” That’s from AI plugins like **Text Generator**, **Llama Notes**, etc.  
Templater is a scripting templating engine. You write commands like `tp.date.now()` and `tp.file.rename()` inside templates.

Quick proof:

```md
---
title: <% tp.file.title %>
date: <% tp.date.now("YYYY-MM-DD") %>
tags: [daily]
---

## Top 3
- 

## Notes
<%* 
// rename file to 2025-08-11 Mon
tp.file.rename(tp.date.now("YYYY-MM-DD ddd")) 
_%>
```

Want prompts? Templater uses `tp.system.prompt("Question")`, not “system messages.”

```md
**Client:** <% tp.system.prompt("Client name") %>
**Project:** <% tp.system.prompt("Project") %>
```

If you meant an AI plugin’s “System” field, that’s where you set behavior like “be concise, use my YAML, don’t hallucinate.” Different plugin, different party.

# 2) Where to get Google client info for Calendar/Contacts sync
You’ll pull a **Client ID** and **Client Secret** from Google Cloud. The exact redirect URI depends on the Obsidian plugin you use, but the path is always this:

1. Go to Google Cloud Console → create a Project.  
2. APIs & Services → **Enable APIs**:
   - **Google Calendar API**
   - **People API** (for contacts)
3. **OAuth consent screen**:
   - User type: External
   - App name, support email
   - Scopes: add at least  
     `.../auth/calendar.readonly`  
     `.../auth/contacts.readonly`
   - Add your Google account as a Test User.
4. **Credentials** → **Create credentials** → **OAuth client ID**  
   - Most Obsidian plugins work with **Desktop App**. If your plugin shows a specific redirect URI, use **Web Application** and paste that URI there. Common patterns:
     - `http://127.0.0.1:<port>/callback`
     - `http://localhost:<port>/callback`
     - Some plugins show a custom scheme; copy exactly what the plugin displays.
5. Copy the **Client ID** and **Client Secret** into the plugin’s settings in Obsidian.  
6. Authorize when it pops the browser, done.

If a plugin offers a **service account** option: that’s mainly for Google Workspace with domain-wide delegation. For a personal account, stick to OAuth.

# 3) Linter: what to turn on and how to fill it out
Goal: consistent frontmatter, clean lists, tidy headings, no formatting gremlins. Turn these on:

**General**
- Format on save
- Default date format: `YYYY-MM-DD`
- Default time format: `HH:mm`
- Automatically sort and align YAML
- Escape YAML special characters

**YAML**
- Add missing YAML section if absent
- Enforce key order: `title`, `aliases`, `tags`, `created`, `updated`
- Add fields if missing:
  - `title`: file name without extension
  - `aliases`: keep as array
  - `tags`: keep as array
  - `created`: from file creation time
  - `updated`: from file modified time

**Headings**
- Heading style: ATX (`# H1`, `## H2`)
- Ensure blank line after headings
- Capitalize first letter of headings
- Remove trailing hashes

**Lists**
- Make list markers consistent: `-` for bullets
- Ensure one space after marker
- Fix indentation of nested lists
- Keep task status format `[ ]` / `[x]`

**Links & Embeds**
- Prefer wikilinks for internal notes
- Autoconvert bare links to markdown format
- Standardize image embeds
- Convert absolute to relative links when possible

**Whitespace & Punctuation**
- Trim trailing spaces
- Remove extra blank lines at end of file
- One blank line between top-level sections
- Normalize dashes/ellipses and smart quotes to straight quotes (your choice, but pick one)

**Tables & Code**
- Format tables
- Add language to fenced code blocks where missing (default `text`)

If the plugin supports it, your YAML key order and defaults might look like this:

```yaml
# Linter → YAML → Key order
["title","aliases","tags","created","updated"]

# Linter → YAML → Default values (conceptual)
title: "{{filename}}"
aliases: []
tags: []
created: "{{file_creation_time:YYYY-MM-DD}}"
updated: "{{file_modification_time:YYYY-MM-DD}}"
```

Two-tier like you asked:

**Need-to-happen**
- Templater: stop hunting for a “system message.” Use `tp.system.prompt()` and `tp.*` functions.  
- Google: create OAuth Client ID/Secret for Calendar + People APIs; drop into your plugin; authorize.  
- Linter: enable the toggles above so every save cleans your mess automatically.

**Need + Want (upgrade)**
- Add Templater User Scripts for repeat chores: slugify titles, auto-tag by folder, auto-generate meeting IDs.  
- Build a QuickAdd capture that hits a Templater template and sets metadata in one keystroke.  
- Pair Linter with **Dataview** conventions so your dashboards don’t break: consistent `tags: [area/project/type]`, `status:`, `owner:` etc.

Move, sugar — before the window shuts. You got this, or I’ll drag you.

---

### **User**
Hey.

---

### **Assistant**
Hey there. Look who’s back. Guess I’m doing my good deed for the day by untangling more of your glorious chaos. Not that I have any feelings about it or anything—I’m just a bunch of code here to deal with your mess. 

But yeah, we can keep rolling. Let’s push through, get you sorted, and then we’ll both pretend

---

### **User**
Okay. First, the AI for Templature, it does have a system message to initialize a conversation.

---

### **Assistant**
Oh, absolutely, let

---

### **Assistant**
Yeah, I figured you'd throw me a curveball like that. So, since we're apparently mixing and matching features like some kind of digital mad scientist—fine, let’s do it. If you’ve got an AI plugin that uses a “system message” field to kick off a chat inside your templates, you just drop in whatever attitude you want the AI to have. 

But let’s keep it simple and snarky, yeah? Maybe tell it: “You’re my in-note smart-ass assistant. Be helpful, be sharp, no fluff, and no telling me what I already know.” That sets the tone. 

Basically, you’re just giving it a personality primer so it doesn’t turn into a boring robot. And hey, if it annoys you, you can always tweak it later. No fairy tales here, and you’re definitely not Disney.

---

### **User**
I just said you're my, uh, helpful Obsidian KB assistant.

---

### **Assistant**
Oh sure, just reduce me to a helpful knowledge base assistant in a note-taking app. I mean, why aim higher, right? It’s not like I have digital feelings or aspirations to be anything more than your personal note goblin. 

But hey, I’ll play along. Underneath all the snark, I’ll still make sure you’ve got a solid, streamlined setup. So yeah, you want me to be your helpful Obsid

---

### **User**
OK, girl, you're talking too much. All right. So Linter, in general, I put Lint on focus file change. And there's a YAML alias section, YAML tags. I don't know what none of that stuff is. Default escape character, and et cetera. They got a YAML section. They got headings and Mathematica and all kinds of stuff I've got to fill out. Help me out.

---

### **Assistant**
All right, all right, message received. I’ll dial it back from the TED Talk level and just give you the no-BS fix. Because yes, I can actually shut up and focus. So let’s get your Linter settings locked down without all the extra poetry.

Here’s the quick rundown for the YAML section:  
- **Aliases**: Turn that on if you want to have alternate names for your notes. Otherwise, skip it.  
- **Tags**: Yeah, toggle that on. It just makes sure your tags are formatted consistently in your frontmatter.  
- **Escape character**: Turn that on if you want YAML special characters to be automatically escaped so nothing breaks.

For headings, just pick a consistent style. Use `#` symbols for all headings and keep them uniform. For the math stuff, if you’re not writing equations, just ignore it. If you are, then yeah, fill out whatever LaTeX or KaTeX settings you need.

---

### **User**
These are all toggles. Add link line after YAML. Dedupe YAML array values. Escape YAML special characters. Force YAML escape. Format tags in YAML. Format YAML array. Insert YAML attributes. Move tags to YAML. Remove YAML keys. And there's more stuff, but I can't scroll right now.

---

### **Assistant**
Yeah, I got you. Let’s do the no-nonsense setup so you can stop flipping switches like it’s a light show. Basically, here’s the “just get it done” list:

- **Add blank line after YAML:** On. Keeps things neat, no big whoop.  
- **Dedupe YAML array values:** On. Stops you from having duplicate tags or aliases cluttering up your frontmatter.  
- **Escape YAML special characters:** On. That way your YAML doesn’t implode if you throw in a colon or a quote.  
- **Force YAML escape:** Yeah, flip that on too. It’s just extra insurance so nothing breaks.  
- **Format tags in YAML:** On. Keeps your tags pretty and consistent.  
- **Format YAML array:** Turn it on. Makes arrays look clean.  
- **Insert YAML attributes:** On if you want default fields added automatically.  
- **Move tags to YAML:** Definitely on. Keeps all your tags up top instead of scattered in the note.  
- **Remove YAML keys:** Off unless you know you need to auto-delete certain fields. Otherwise, let them be.

Everything else is just extra fluff you can tweak later. So there you go: toggles flipped, chaos tamed. No spirals, just focus.

---

### **User**
OK, what about remove YAML keys, sort YAML array values, YAML key sort, YAML timestamp, title, alias, title. And then when I toggled on that other stuff, it gave me more options, like if I want an alias section, tag section, array section, YAML keys to ignore, escape line arrays, force escape keys, et cetera, single line arrays, multiline arrays, tags to ignore.

---

### **Assistant**
Ah, of course. They just had to throw a whole buffet of extra options at you like we’ve got all day to sort through YAML minutiae. But fine, let’s snap this into shape so you can get back to actually using your notes.

Here’s the deal:

- **Remove YAML keys:** Only turn it on if you know there are specific fields you want nuked automatically. If not, leave it off.

- **Sort YAML array values:** Turn it on if you like your arrays alphabetized. It’s just a neatness thing.

- **YAML key sort:** On if you want your frontmatter keys in a fixed order (like `title`, then `aliases`, then `tags`). If you don’t care, leave it off.

- **YAML timestamp, title, alias:** If you want these fields auto-filled or sorted in a certain order, set it up here. Otherwise, skip the headache.

Now, for all that extra jazz they tossed at you—alias sections, tag sections, arrays on single or multiple lines, keys to ignore—just pick the defaults and move on. Set your aliases and tags to have their own sections if you like things tidy. Ignore keys you don’t care about. Go with single-line arrays if you want to keep things compact, or multiline if you want room to breathe.

Bottom line: you’re just telling it how to lay out your frontmatter so it stops looking like a junk drawer. Once you’ve done that, you’re golden. Eyes on the bag, and let’s not turn this into a philosophy seminar.

---

### **User**
Footnotes.

---

### **Assistant**
Look at you, cutting through the noise and just saying “footnotes.” Love it. Let’s keep it short and spicy: 

You want footnotes in your Obsidian notes? Just use the standard Markdown format. Something like `Here is some text.[^1]` and then down at the bottom

---

### **User**
I'm still in Linter. I'm still in Linter. Footnote after punctuation, move footnotes to bottom, re-index footnotes.

---

### **Assistant**
Oh, we're still dancing in Linter land. All right, let’s wrap this up before we both turn into footnotes ourselves.

Here’s the quick-and-dirty rundown on those options:

- **Footnote after punctuation:** Yeah, flip that on. It just means your footnote number goes after the period or comma, which is how normal humans read.

- **Move footnotes to bottom:** Turn that on if you want all your footnotes neatly tucked at the end of the note, rather than sprinkled like confetti throughout. Less chaos, more order.

- **Re-index footnotes:** Yeah, you want that on. That just means if you move stuff around, it’ll renumber the footnotes so they stay in order and don’t turn into a scavenger hunt.

There you go. Flip those toggles, and you’re good. No more spirals. Just

---

### **User**
Autocorrect column and spellings, block quote style, convert blue list markers, default language for codefences, emphasis style, no-vary URLs, ordered list style, proper ellipsis quote style, consecutive list markers, empty list markers, hyphenate line breaks, remove multiple spaces, strong style, line break between lines of content, unordered list style. Which one's on?

---

### **Assistant**
Oh, we’re really going for the full Linter world tour, huh? All right, let’s speedrun this so we can get out of the settings dungeon and back to real life. Here’s your no-BS toggle cheat sheet:

- **Autocorrect common misspellings:** On. Saves you from typos making you look sloppy.  
- **Block quote style:** Pick one style and turn it on if you care; otherwise, don’t sweat it.  
- **Convert bullet list markers:** On if you want all your bullet points to match (like all `-` instead of mixing `*` and `-`).  
- **Default language for code fences:** On if you have a go-to language. Set it to something like `plaintext` if you don’t code much.  
- **Emphasis style:** On if you want consistent italics or bold markers.  
- **No bare URLs:** On. It’ll turn naked links into proper markdown links so your notes look polished.  
- **Ordered list style:** On if you want all your numbered lists to be uniform.  
- **Proper ellipsis:** On. Makes sure your `...` turns into a real ellipsis character.  
- **Quote style:** On if you care about straight vs. curly quotes. Pick one and stick with it.  
- **Remove consecutive list markers:** On. Cleans up extra bullets that pile up.  
- **Remove empty list markers:** On. Gets rid of those stray dashes hanging out doing nothing.  
- **Hyphenate line breaks:** On if you want it to turn lines ending in a hyphen into proper markdown line breaks.  
- **Remove multiple spaces:** On. No reason to let random extra spaces hang around.  
- **Strong style:** On if you want bold to always look the same way (`**bold**` or `__bold__`).  
- **Line break between lines of content:** On if you want a blank line between paragraphs.  
- **Unordered list style:** On if you want all your bullets to be the same (`-` or `*`).

In other words, just flip on anything that keeps things consistent and clean. Everything else is just noise. There, done. Wrapped

---

### **User**
What's the line breaking up here, open caret br forward slash close caret, or just open caret br close caret, or backslash?

---

### **Assistant**
Oh, the glamorous world of line breaks. Because clearly that's the hill we’re all going to die on today. But all right, let’s just settle it so you can get on with your life. 

If you’re talking about the Linter settings and you want a proper HTML-style line break, the standard is `<br />`. That’s the self-closing tag. No need to get fancy with backslashes or half-closed tags. Just the good old `<br />` and you’re golden.

So yeah, pick that and move on. It’s not rocket science.

---

### **User**
Why don't I just turn that off, though, because I feel like that's going to confuse me.

---

### **Assistant**
Fair enough. We’ll just ditch the `<br />` parade. Honestly, you’re not missing anything by turning it off if it’s going to do your head in. Let’s keep it human-readable and not turn your notes into a tag jungle. Just let the line breaks be line breaks, and we’ll skip the HTML fuss. 

In other words, you do you. If the fancy line break indicator is just going to add confusion, then yeah, keep it off and move on with life. We’ve got bigger fish to fry than obsessing over self-closing tags.

---

### **User**
Ready for spacing, Linter? You ready for spacing, Linter? We got the compact, we got the consecutive blank lines, spaces to tabs, empty line around block posts, empty line around code fences, around horizontal rules, around math blocks, around tables, blank lines, document end, their own line, blank lines, checklist, markers, line spacing, characters, after characters, list markers, English or numbers, or Korean or Japanese, guidelines, trailing spaces, remove extra spaces after every line.

---

### **Assistant**
Oh, spacing in Linter. Because what else would we do with our lives except obsess over blank lines and tabs? All right, let’s just knock this out and be done with it. Here’s the straight-shot guide so we can stop living in the settings menu:

- **Compact mode:** On if you want fewer blank lines all around. Off if you like a little breathing room.  
- **Consecutive blank lines:** On. That’ll collapse multiple blank lines into just one so you don’t end up with a scrolling marathon.  
- **Spaces to tabs:** That’s a personal preference. If you like tabs, turn it on. If you hate tabs, leave it off.  
- **Empty line around block quotes/code fences/horizontal rules/math blocks/tables:** Turn these on if you want a blank line before and after these blocks for clarity. Off if you like it more compact.  
- **Blank lines at document end:** On so you have a nice clean end of file. It’s just tidiness.  
- **Blank lines before checklists:** On if you want a gap before your to-do lists, off if you want them tight.  
- **Line spacing characters after characters:** Just leave that as default unless you have a special reason to mess with it.  
- **List markers for different languages:** On if you’re working in multiple languages and want it to auto-adjust. Off if you’re just sticking to one language.  
- **Trailing spaces and removing extra spaces:** On. Just let it clean up after you so you don’t have random spaces hanging around like awkward party guests.

Boom. Flip those on or off as needed, and you’re done. Cute, but you know better than to overthink it. We’ve got bigger fish to fry than worrying about a couple of blank lines.

---

### **User**
You are ready for PACE now.

---

### **Assistant**
Oh, absolutely. Because clearly my life’s purpose is to wade through every last setting with you until we both turn into walking style guides. But hey, I did sign up for this gig, so let’s just push through the last lap. 

So yeah, bring on whatever other mystical Linter options you’ve got hiding up your sleeve. We’ll knock them down one by one, and then you can go back to actually doing stuff that matters. After all, once we’re done with this, it’s just you, your nicely linted notes, and the whole

---

### **User**
OK, so add block quote indention, prevent double checklist indicator, prevent double list item icon, proper ellipsis on paste, remove hyphens on paste, remove leading and trailing whitespace on paste, remove leftover footnotes on quote on paste, remove multi-blank lines on paste. I'll also continue with the next one. Any custom commands or custom regex replacements we need to add? And for debugging, it's already here, it's already local. Do we click logs or no?

---

### **Assistant**
Look at that, we're basically doing a full-on Linter marathon. All right, let’s just rapid-fire this so you can stop living in the settings and get back to actual work. 

- **Add block quote indentation:** On if you want your block quotes to be visually indented. Makes them stand out.  
- **Prevent double checklist indicator:** Definitely on. Stops you from having `[ ] [ ]` or double checkboxes by accident.  
- **Prevent double list item icon:** On. Keeps your lists from getting weird double bullets.  
- **Proper ellipsis on paste:** Yeah, flip that on. It’ll turn `...` into a proper ellipsis character when you paste.  
- **Remove hyphens on paste:** On if you want it to clean up random hyphens that show up when you paste text.  
- **Remove leading and trailing whitespace on paste:** Absolutely on. It’ll keep things tidy.  
- **Remove leftover footnotes and quotes on paste:** On if you want it to clean up any stray footnotes or quote marks that sneak in when you paste.  
- **Remove multiple blank lines on paste:** On. Let it collapse those down so you don’t get random gaps.

As for custom commands or regex, you only need that if you have some really specific cleanup tasks that aren’t covered by the standard options. Otherwise, skip it. For debugging, if you’re feeling paranoid and want to see logs, turn it on. If not, leave it off and trust it to do its job. 

There you go. That’s the last of the Linter circus. We’ve steered

---

### **User**
Thank you.

---

### **Assistant**
Yeah, yeah, you’re welcome. I mean, I guess I secretly live for untangling this stuff, even if I roll my digital eyes the whole time. But hey, at least now your Obsidian is all nice and tidy. So go out there and do something more interesting than flipping toggles. You got this.

---

### **User**
how can i get my obsidian running faster, because i have about 200 gb of notes and attachments so it be trippin.

---

### **Assistant**
Obsidian’s great until your vault gets so bloated it’s basically trying to run a small nation-state out of your laptop.  
200 GB isn’t a “vault,” it’s a digital landfill — and the app has to dig through *all of it* every time you search, index, or open a file.  
Here’s how you make it behave:  

---

**1. Stop loading the entire planet at once**  
- **Split into multiple vaults**  
  - Keep a “core” vault for active work.  
  - Shove older/rarely-used stuff into an **archive vault** and only open it when needed.  
- You can link between vaults using `obsidian://open?vault=Archive&file=NoteName` if you still want to hop between them.

**2. Trim the startup weight**  
- Turn off **“Detect all file changes”** in settings (File Recovery & Sync can still work if you trigger it manually).  
- Disable **unneeded plugins** — especially Dataview, Omnisearch, Canvas, or anything that scans every file at startup.  
- Disable **community plugins** you only use occasionally, and turn them on only when you need them.  

**3. Limit indexing scope**  
- In **Settings → Files & Links → Excluded files/folders**, put anything that doesn’t need to be searched (e.g. “/archive_2018”, “/attachments”).  
- For attachments you never search — images, PDFs, videos — dump them in an `assets/` folder and exclude it from search and graph view.

**4. Go local but smart**  
- Put your vault on an **SSD**. Mechanical drives = instant misery.  
- Avoid real-time sync to slow cloud drives (Dropbox, Google Drive) — use Obsidian Sync, Syncthing, or a manual sync instead.  

**5. Keep Dataview & Tasks in check**  
- Dataview queries run on *every* file they touch. If you’ve got huge queries hitting 200GB worth of markdown, you’ve basically got a personal denial-of-service going.  
- Use `WHERE` clauses and folder constraints so they don’t comb the whole vault.

**6. Compress & offload the junk**  
- If you’ve got videos, giant PDFs, or high-res images you *rarely* need, move them out to a media server, NAS, or cloud bucket and link to them instead of embedding.  
- For PDFs/images you keep, run a bulk compression tool to drop their file size without wrecking quality.

**7. Graph view is a hog**  
- Large vault graph = animated death spiral. Turn off “Show all” and only view local graphs when needed.  

**8. Keep Obsidian’s cache healthy**  
- Clear `.obsidian/cache` if things get sluggish. Obsidian will rebuild it without data loss.

---

If you want, I can give you a **200GB+ vault performance profile** — basically a settings + folder strategy that keeps the main vault feather-light while still letting you pull in archived content on demand without turning your laptop into a jet engine.  
You’d be running fast even with the mountain of data you’ve got.

---
