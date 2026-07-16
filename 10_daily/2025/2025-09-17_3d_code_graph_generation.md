---
layout: page
title: "3D code graph generation"
slug: "3d_code_graph_generation"
created_at: "2025-09-17 01:14:19"
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
date: 2025-09-17
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "68ca51a9-2928-8322-8811-2b46b08a3c5e"
canonical_ref: ""
---

# 3D code graph generation

## Overview
- **Date**: 2025-09-17 01:14:19
- **Conversation ID**: `68ca51a9-2928-8322-8811-2b46b08a3c5e`
- **Source**: `Chat-Export-28513-2026/conversations-000.json`

## Chat History

### User
> how can i turn my code into an interactive graph 3d that i can see how the code flos and connects ect.

### Assistant
> Snap & steer time, Q. You want a living, 3D map of your code—modules as planets, imports as orbits—so you can *see* how it flows. Here are two clean paths: a 10-minute “bare fix” and a sturdier upgrade you can wire into your portal later.
> 
> # Tier 1 — Bare Fix (fastest): 3D module graph in your browser
> Works for JS/TS right away; Python too with a tiny tweak.
> 
> **A) Generate a dependency JSON**
> - **JS/TS projects**
>   ```bash
>   npm i -g madge
>   # from your repo root:
>   madge --json ./src > graph.json
>   ```
> - **Python projects**
>   ```bash
>   pip install pydeps
>   # Creates a .dot; we’ll convert it:
>   pydeps your_pkg_or_entry.py --max-bacon=3 --noshow --pylib --show-deps --output=pydeps.dot
>   pip install pydot
>   python - <<'PY'
> import pydot, json
> graphs = pydot.graph_from_dot_file('pydeps.dot')
> g = graphs[0]
> edges = []
> nodes = set()
> for e in g.get_edges():
>     s = e.get_source().strip('"')
>     t = e.get_destination().strip('"')
>     nodes.update([s,t]); edges.append({"source": s, "target": t})
> data = {"nodes": [{"id": n} for n in nodes], "links": edges}
> open("graph.json","w").write(json.dumps(data))
> PY
>   ```
> 
> **B) Drop this minimal viewer next to `graph.json` and open it**
> Save as `index.html` (no build step; just open the file or serve it):
> 
> ```html
> <!doctype html>
> <html>
> <head>
>   <meta charset="utf-8" />
>   <title>Code Graph 3D</title>
>   <style>html,body,#graph{margin:0;height:100%;background:#0b1220;color:#eee;font-family:system-ui}</style>
> </head>
> <body>
>   <div id="graph"></div>
>   <script src="https://unpkg.com/three/build/three.min.js"></script>
>   <script src="https://unpkg.com/3d-force-graph"></script>
>   <script>
>     // If your madge output is a { module: [deps] } dict, normalize to nodes/links:
>     async function normalizeMadge(raw){
>       if (raw.nodes && raw.links) return raw; // already normalized (Python branch)
>       const modules = Object.keys(raw);
>       const links = [];
>       modules.forEach(src => (raw[src]||[]).forEach(t => links.push({source: src, target: t})));
>       return { nodes: modules.map(id => ({ id })), links };
>     }
> 
>     fetch('graph.json').then(r => r.json()).then(normalizeMadge).then(data => {
>       const Graph = ForceGraph3D()(document.getElementById('graph'))
>         .graphData(data)
>         .nodeId('id')
>         .nodeLabel(n => n.id)
>         .nodeAutoColorBy(n => n.id.split('/')[0])
>         .linkDirectionalParticles(2)
>         .linkDirectionalParticleSpeed(0.005)
>         .onNodeClick(node => {
>           const dist = 120;
>           const camera = Graph.camera();
>           const {x,y,z} = node;
>           const az = Math.atan2(z, x);
>           const el = Math.atan2(y, Math.sqrt(x*x+z*z));
>           const newPos = { x: Math.cos(az)*Math.cos(el)*dist, y: Math.sin(el)*dist, z: Math.sin(az)*Math.cos(el)*dist };
>           Graph.cameraPosition(newPos, node, 1000);
>           console.log('Focus:', node.id);
>         });
>     });
>   </script>
> </body>
> </html>
> ```
> 
> **Run it**
> - Double-click `index.html`, or:
>   ```bash
>   npx serve .
>   # open http://localhost:3000 (or whatever it prints)
>   ```
> 
> You now have a 3D, zoomable code-constellation. Click a node to fly the camera to it; particle flow shows import direction.
> 
> # Tier 2 — Upgrade / Future-Proof
> When you’re ready to level up:
> 
> 1) **Per-language call graphs (not just imports)**
> - **Python**: `pyan3` can analyze function-level call graphs.
>   ```bash
>   pip install pyan3
>   pyan3 **/*.py --uses --no-defines --dot > callgraph.dot
>   # convert with the same pydot → JSON trick; visualize with the viewer above
>   ```
> - **JS/TS**: Use `esbuild` or `ts-morph` to walk the AST and emit function-to-function edges (I can hand you a script when you’re ready).
> 
> 2) **Make it part of your CI**
> - Add a script that regenerates `graph.json` on every push and deploy the viewer to **portal.qially.com** under `/dev/graphs/<repo>/`.
> - Gate PRs: fail the build if the graph density explodes (keeps tangles in check).
> 
> 3) **Add filters + search (React/Cloudflare-ready)**
> - Swap the raw HTML for a React component (Vite + Cloudflare Pages) using `3d-force-graph` + a sidebar for:
>   - search (regex on node ids),
>   - level-of-detail toggles (only show imports across packages, or within a package),
>   - “highlight path from A→B” to trace flows,
>   - “show cycles” to surface knotty dependencies.
> 
> 4) **Polyglot repos**
> - Generate one `graph.json` per package (Python, TS, Go, etc.), then merge them into a supergraph using node prefixes (`py:package.module`, `ts:src/file.ts`) so the 3D view shows cross-language seams.
> 
> # Quick reads (when you’re moving fast)
> - **Imports only** answers “who depends on whom?” → use **madge / pydeps**.
> - **Function calls** answers “what runs what?” → use **pyan3** (Py) or a TS AST walker.
> - **3D viz** → **3d-force-graph** (browser, WebGL), zero friction, big graphs stay fluid.
> 
> # Snap notes for your stack
> - Fits your Cloudflare Pages flow (just static assets).
> - No vendor lock-in, no telemetry, works offline.
> - Easy to embed under `/admin` with a passcode for your Cockpit.
> 
> Call the play: if you drop me your repo language mix (JS/TS vs Python heavy), I’ll just hand you the exact script + npm/pip steps wired to your file paths and PR workflow so it’s push-to-see-the-graph.

### User
> i wnat it to read teh code base and make the graph

### Assistant
> Got it. You want “read the repo → spit out a 3D graph” with zero vibes, all results. Here’s a drop-in mini-tool that scans JS/TS with **madge** and scans Python with a quick import parser, merges both, and writes `graph.json` you can open in a WebGL viewer.
> 
> ## 1) Add files
> 
> **`package.json`**
> ```json
> {
>   "name": "code-graph",
>   "private": true,
>   "type": "module",
>   "scripts": {
>     "graph": "node scripts/gen-graph.mjs",
>     "view": "npx serve public -l 5174"
>   },
>   "dependencies": {
>     "fast-glob": "^3.3.2",
>     "madge": "^8.0.0"
>   }
> }
> ```
> 
> **`scripts/gen-graph.mjs`**
> ```js
> import fs from "fs";
> import path from "path";
> import fg from "fast-glob";
> import madge from "madge";
> 
> const ROOT = process.env.ROOT || process.cwd();
> const OUT = process.env.OUT || path.join(ROOT, "public", "graph.json");
> 
> // --- helpers
> const uniq = (arr) => [...new Set(arr)];
> const toId = (p) => p.replace(/\\/g, "/"); // windows-safe ids
> 
> // --- JS/TS via madge
> async function scanJsTs() {
>   const srcs = await fg(["**/*.{js,jsx,ts,tsx}","!**/node_modules/**","!**/dist/**","!**/build/**"], { cwd: ROOT });
>   if (srcs.length === 0) return { nodes: [], links: [] };
>   const res = await madge(srcs.map(p => path.join(ROOT, p)), {
>     baseDir: ROOT,
>     fileExtensions: ["js","jsx","ts","tsx"],
>     includeNpm: false
>   });
>   const obj = await res.obj();
>   const nodes = uniq(Object.keys(obj).concat(...Object.values(obj))).map(id => ({ id: `ts:${toId(id)}` }));
>   const links = [];
>   for (const [src, deps] of Object.entries(obj)) {
>     deps.forEach(t => links.push({ source: `ts:${toId(src)}`, target: `ts:${toId(t)}`, kind: "import" }));
>   }
>   return { nodes, links };
> }
> 
> // --- Python (simple import parser: import x / from x import y)
> function parsePyImports(text) {
>   const imports = [];
>   const re1 = /^\s*import\s+([a-zA-Z0-9_\.]+)/gm;
>   const re2 = /^\s*from\s+([a-zA-Z0-9_\.]+)\s+import\s+/gm;
>   let m;
>   while ((m = re1.exec(text))) imports.push(m[1]);
>   while ((m = re2.exec(text))) imports.push(m[1]);
>   return imports;
> }
> 
> async function scanPy() {
>   const pys = await fg(["**/*.py","!**/.venv/**","!**/venv/**","!**/__pycache__/**","!**/dist/**","!**/build/**"], { cwd: ROOT });
>   if (pys.length === 0) return { nodes: [], links: [] };
> 
>   const fileToModule = (file) => {
>     const rel = file.replace(/\\/g,"/").replace(/\.py$/,"");
>     const parts = rel.split("/");
>     // simple heuristic: treat folders as packages if they contain __init__.py
>     return `py:${rel}`;
>   };
> 
>   const nodes = [];
>   const links = [];
>   for (const rel of pys) {
>     const abs = path.join(ROOT, rel);
>     const id = fileToModule(rel);
>     nodes.push({ id });
>     const txt = fs.readFileSync(abs, "utf8");
>     const deps = parsePyImports(txt);
>     for (const d of deps) {
>       // approximate target id; we link to top-level module name; it still shows flow
>       const tgt = `py:${d.replace(/\./g, "/")}`;
>       links.push({ source: id, target: tgt, kind: "import" });
>     }
>   }
>   // add target nodes so edges don’t dangle invisibly
>   const targetOnly = uniq(links.map(l => l.target)).filter(t => !nodes.find(n => n.id === t));
>   nodes.push(...targetOnly.map(id => ({ id })));
>   return { nodes, links };
> }
> 
> // --- Merge + write
> function mergeGraphs(g1, g2) {
>   const nodes = uniq([...g1.nodes, ...g2.nodes].map(n => n.id)).map(id => ({ id }));
>   const key = (l) => `${l.source}→${l.target}:${l.kind||""}`;
>   const seen = new Set();
>   const links = [];
>   for (const l of [...g1.links, ...g2.links]) {
>     const k = key(l);
>     if (!seen.has(k)) { seen.add(k); links.push(l); }
>   }
>   return { nodes, links, meta: { generatedAt: new Date().toISOString() } };
> }
> 
> (async () => {
>   console.log("Scanning repo:", ROOT);
>   const [jsts, py] = await Promise.all([scanJsTs(), scanPy()]);
>   const data = mergeGraphs(jsts, py);
>   fs.mkdirSync(path.dirname(OUT), { recursive: true });
>   fs.writeFileSync(OUT, JSON.stringify(data, null, 2));
>   console.log(`Wrote ${OUT} with ${data.nodes.length} nodes, ${data.links.length} links.`);
> })();
> ```
> 
> **`public/index.html`**
> ```html
> <!doctype html>
> <html>
> <head>
>   <meta charset="utf-8" />
>   <title>Code Graph 3D</title>
>   <style>html,body,#graph{margin:0;height:100%;background:#0b1220;color:#eee;font-family:system-ui}</style>
> </head>
> <body>
>   <div id="graph"></div>
>   <script src="https://unpkg.com/three/build/three.min.js"></script>
>   <script src="https://unpkg.com/3d-force-graph"></script>
>   <script>
>     fetch('graph.json').then(r=>r.json()).then(data=>{
>       const Graph = ForceGraph3D()(document.getElementById('graph'))
>         .graphData(data)
>         .nodeId('id')
>         .nodeLabel(n=>n.id)
>         .nodeAutoColorBy(n=>n.id.split(':')[0]) // py vs ts
>         .linkDirectionalParticles(2)
>         .linkDirectionalParticleSpeed(0.006)
>         .onNodeClick(node=>{
>           const dist=140, {x,y,z}=node;
>           const az=Math.atan2(z,x), el=Math.atan2(y,Math.hypot(x,z));
>           const newPos={x:Math.cos(az)*Math.cos(el)*dist,y:Math.sin(el)*dist,z:Math.sin(az)*Math.cos(el)*dist};
>           Graph.cameraPosition(newPos, node, 1000);
>         });
>     });
>   </script>
> </body>
> </html>
> ```
> 
> ## 2) Install & run
> 
> ```bash
> # from your repo root
> npm i
> npm run graph           # generates public/graph.json
> npm run view            # serves public/ at http://localhost:5174
> ```
> 
> Open `http://localhost:5174` → fly around, click nodes, watch import flow.
> 
> ## 3) How it behaves (so you can trust it)
> - **JS/TS** uses `madge` (battle-tested) to resolve `import/require` accurately.
> - **Python** uses a lightweight parser for `import x` / `from x import y`. It’s fast and good enough to visualize architecture; you can upgrade later to function-level calls via `pyan3`.
> - Nodes are prefixed: `ts:` and `py:` so cross-language seams are obvious.
> - Output is a simple `{nodes:[{id}], links:[{source,target,kind}]}` JSON your portal can ship as a static asset.
> 
> ## 4) Upgrades (when you want more fidelity)
> - **Call graphs (Python)**: swap the Python scanner for `pyan3`:
>   ```bash
>   pip install pyan3
>   pyan3 **/*.py --uses --no-defines --dot > callgraph.dot
>   ```
>   Then parse DOT (small change in `gen-graph.mjs`) to add `kind:"calls"` edges.
> - **Filter knobs** (big repos): add env vars to the script:
>   - `INCLUDE="apps/**,src/**"` `EXCLUDE="**/tests/**,**/*.spec.ts"` and wire them into the `fast-glob` patterns.
> - **CI**: add `npm run graph` to your build → publish `/public` on Cloudflare Pages under `/dev/graphs/<repo>/`.
> 
> ## 5) Snap & steer
> You now have a push-button read-the-code → 3D graph. If you want this auto-embedded in **QiEOS** `/admin` behind a passcode, we can wrap that `public/index.html` in a React route and point it at the same `graph.json`. Next bag: add “cycle detection” and “highlight path A→B” to hunt tangles on sight.
