---
layout: page
title: "Evitar apagados automáticos"
slug: "evitar_apagados_automaticos"
created_at: "2025-08-13 09:29:01"
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
date: 2025-08-13
summary: ""
author: "Cody J. Rice-Velasquez"
owner: "Cody"
keywords: []
aliases: []
context: ""
sensitivity: internal
classification: business_internal
realm_label: "empowerqnow"
uid: "689ca129-fc2c-8331-9458-441e14d787ca"
canonical_ref: ""
---

# Evitar apagados automáticos

## Overview
- **Date**: 2025-08-13 09:29:01
- **Conversation ID**: `689ca129-fc2c-8331-9458-441e14d787ca`
- **Source**: `Chat-Export-28513-2026/conversations-000.json`

## Chat History

### User
> Hey, chica. ¿Cómo está usted? Oye, en la otra máquina que yo tengo, mi HP, que uso como mi server, aunque no es un server, ¿cómo le hago para que no se vuelva a apagar solito ni reiniciar sin que yo lo ponga? Porque cada rato yo vengo y está apagada la tienda de cosas. Gracias.

### Assistant
> Tienes que quitarle las manías de ahorro de energía y reinicios automáticos que Windows trae de fábrica como si todos viviéramos con laptops de 1998.  
> 
> Aquí te dejo el plan:  
> 
> **1. Desactivar suspensión y apagado automático**  
> - Ve a **Panel de control → Hardware y sonido → Opciones de energía**.  
> - Edita el plan que esté activo.  
> - Pon *Nunca* en “Suspender el equipo” y “Apagar la pantalla” (al menos para “Con corriente”).  
> 
> **2. Desactivar reinicio por actualizaciones**  
> - Abre **Configuración → Actualización y seguridad → Windows Update → Opciones avanzadas**.  
> - Desactiva “Reiniciar automáticamente lo antes posible…” y ajusta las horas activas para que cubran todo el día.  
> 
> **3. Evitar apagado por inactividad**  
> - En **Configuración → Sistema → Inicio/apagado/suspensión avanzada**, revisa que *Nada* esté programado en “Acciones al presionar el botón de encendido” y “Al cerrar la tapa” (aunque sea una PC de escritorio, a veces los perfiles de energía traen eso mal configurado).  
> 
> **4. Comprobar que no haya un fallo que lo apague**  
> - Abre el **Visor de eventos** y mira en *Registros de Windows → Sistema* si hay errores críticos (por ejemplo, *Kernel-Power*). Si ves muchos, puede ser hardware, no configuración.  
> 
> **5. Si quieres algo definitivo para modo “server casero”**  
> - En **Configuración avanzada de energía**, en la sección *Disco duro*, pon “Apagar disco duro tras…” en *Nunca*.  
> - En la sección *Suspender*, desactiva *Suspensión híbrida* y *Hibernar*.  
> 
> Si quieres, te puedo pasar un comando rápido de PowerShell para que el HP se quede encendido 24/7 y se olvide de dormirse aunque quiera. ¿Quieres que te lo deje listo?

### User
> hey my other computer has the hyper v and virtual machines turned on is there where i can share the work load from my main computer or nah?

### Assistant
> Yes, but not like magic “plug them together and they become Voltron.”  
> Hyper-V lets that HP host its own virtual machines, and you *can* split certain jobs between your main PC and that one — but only if the software you’re running supports distributing work across multiple machines.  
> 
> Here’s the reality check:  
> 
> **When it works**  
> - If what you’re doing is **containerized** (Docker, Kubernetes) or set up for **cluster computing** (like some AI model training frameworks, render farms, distributed databases), then you can make your HP run part of the load and your main PC run the rest.  
> - You’d connect them over your LAN and make them part of the same cluster/swarm.  
> 
> **When it won’t help**  
> - Most everyday desktop apps (video editors, browsers, Office, even most games) can’t magically use another machine’s CPU/GPU unless they were built for distributed processing.  
> - Running the HP as a Hyper-V box doesn’t make it a drop-in “extra CPU” for your main PC.  
> 
> **What you *could* do instead**  
> 1. **Dedicated task server** — Put your HP in charge of long, heavy, or background jobs (file conversions, backups, downloads, automation scripts, AI model runs) so your main PC stays snappy.  
> 2. **Remote build/render node** — If you use tools like Blender, Unreal, or Adobe Media Encoder with network render support, let the HP chew through those tasks.  
> 3. **Clustered AI work** — If you’re doing Python or AI workloads, set up something like Ray, Dask, or PyTorch distributed mode, and make both PCs part of the cluster.  
> 4. **VM host for testing** — Run multiple test environments or servers on the HP without touching your main rig.  
> 
> If you want, I can map you a *"how to make your HP a helper node"* plan so it actually lightens your main PC’s load instead of just sitting there sipping electricity. Want me to draft that setup?

### User
> ok, i have docker on both machines and they are on the same network and vpn with tailspine, how can i start having my main machine push jobs to my other machine without me having to remote into the other other mahcine and manually start a job.

### Assistant
> Cute dream, but no, your PCs won’t fuse into a single cyber-dragon. You can absolutely push work from your main box to the HP without babysitting it, though. Since you already have Docker on both and they’re on the same LAN and Tailscale VPN, here are three clean ways to do it, from “gets it done now” to “proper cluster.”
> 
> # 1) Fastest win: Docker Swarm over Tailscale
> Turn both machines into a tiny swarm so you deploy from your main PC and the HP just picks up jobs. No remoting in, no hand-holding.
> 
> **On MAIN (manager):**
> ```bash
> # Use your MAIN's Tailscale IP here
> docker swarm init --advertise-addr 100.x.y.z
> ```
> 
> It will spit a `docker swarm join ...` command with a token. Run that on the HP:
> 
> **On HP (worker):**
> ```bash
> # Use HP's own Tailscale IP for advertise-addr
> docker swarm join --token SWMTKN-... --advertise-addr 100.a.b.c 100.x.y.z:2377
> ```
> 
> **Back on MAIN, label the HP so you can target it:**
> ```bash
> docker node ls
> # grab the NODE ID for HP
> docker node update --label-add role=hp-worker <HP_NODE_ID>
> ```
> 
> **Create an overlay network (so services can talk across machines):**
> ```bash
> docker network create -d overlay --attachable backbone
> ```
> 
> **Deploy stacks from MAIN only. Example `stack.yml`:**
> ```yaml
> version: "3.9"
> services:
>   queue:                    # shared job queue (redis)
>     image: redis:7
>     networks: [backbone]
>     deploy:
>       placement:
>         constraints: [node.role == manager]  # keep on MAIN
> 
>   worker:                   # runs on HP only
>     image: yourorg/worker:latest
>     environment:
>       - QUEUE_HOST=queue
>     networks: [backbone]
>     deploy:
>       replicas: 2
>       placement:
>         constraints: [node.labels.role == hp-worker]
>       restart_policy:
>         condition: on-failure
> 
>   api:                      # optional: push jobs via HTTP
>     image: yourorg/api:latest
>     environment:
>       - QUEUE_HOST=queue
>     ports:
>       - "8080:8080"
>     networks: [backbone]
>     deploy:
>       placement:
>         constraints: [node.role == manager]
> 
> networks:
>   backbone:
>     external: false
> ```
> 
> **Launch it (from MAIN only):**
> ```bash
> docker stack deploy -c stack.yml jobs
> ```
> 
> Now any image updates or replica changes you do from MAIN roll out to HP automatically. HP stays hands-off.
> 
> Pro tip: if a service must run on MAIN or HP, use placement constraints like:
> - `node.role == manager` to pin to MAIN
> - `node.labels.role == hp-worker` to pin to HP
> 
> # 2) “No cluster, just shoot jobs there”: Docker Contexts
> If you don’t want Swarm, you can still control HP from MAIN using Docker contexts over SSH or Tailscale. You’ll run commands locally that execute against the HP’s Docker daemon.
> 
> **Create a context on MAIN:**
> ```bash
> # If you have SSH to HP
> docker context create hp --docker "host=ssh://USERNAME@100.a.b.c"
> 
> # Switch when you need to target HP
> docker --context hp ps
> docker --context hp compose -f worker.yml up -d
> ```
> 
> Combine with a small script or Makefile on MAIN and you can “deploy” to HP with one command. No RDP, no manual logins.
> 
> # 3) Proper control panel: Portainer + Agent
> If you prefer clicking buttons instead of remembering flags, run Portainer on MAIN and an Agent on both machines. Then you deploy stacks to either node from one dashboard. It’s the least grumpy path for future you.
> 
> - MAIN: run Portainer CE
> - MAIN + HP: run Portainer Agent
> - Add both endpoints to Portainer. Deploy stacks from there. Done.
> 
> # Job pattern that actually scales
> Your apps need a producer/worker model so “pushing jobs” is more than vibes.
> 
> - **Queue:** Redis or RabbitMQ in the swarm (keep on MAIN).
> - **Producer:** API or scheduler on MAIN that enqueues jobs.
> - **Workers on HP:** containers that pull from the queue and process.
> 
> Minimal example for a Python worker:
> 
> `Dockerfile` for worker:
> ```dockerfile
> FROM python:3.12-slim
> WORKDIR /app
> RUN pip install rq redis
> COPY worker.py .
> CMD ["python", "worker.py"]
> ```
> 
> `worker.py`:
> ```python
> import os, time
> from rq import Connection, Worker
> from redis import Redis
> 
> redis_host = os.getenv("QUEUE_HOST", "redis")
> while True:
>     try:
>         with Connection(Redis(host=redis_host, port=6379)):
>             Worker(["default"]).work(with_scheduler=True)
>     except Exception as e:
>         print("Worker error:", e, flush=True)
>         time.sleep(2)
> ```
> 
> **Producer sample (MAIN, inside your API):**
> ```python
> from rq import Queue
> from redis import Redis
> 
> q = Queue("default", connection=Redis(host="redis", port=6379))
> 
> def enqueue_job(payload):
>     return q.enqueue("tasks.process", payload)  # your function path
> ```
> 
> Workers on HP will just keep pulling. You push jobs from MAIN; HP eats them.
> 
> # Image distribution without pain
> Use a private registry reachable via Tailscale so both machines pull the same images.
> 
> **Registry stack on MAIN:**
> ```yaml
> version: "3.9"
> services:
>   registry:
>     image: registry:2
>     ports:
>       - "5000:5000"
>     deploy:
>       placement:
>         constraints: [node.role == manager]
> ```
> 
> Tag and push from MAIN:
> ```bash
> docker build -t 100.x.y.z:5000/yourorg/worker:latest .
> docker push  100.x.y.z:5000/yourorg/worker:latest
> # In your stack.yml, reference 100.x.y.z:5000/yourorg/worker:latest
> ```
> 
> # Need-to-Happen (no-BS fix)
> 1. Pick Swarm or Contexts. If you want one-command deploys and auto-placement, use **Swarm**.  
> 2. Use **Redis queue** pattern so MAIN enqueues, HP processes.  
> 3. Put both on a shared **overlay network**.  
> 4. Pin workers to HP via **node labels**.
> 
> # Need+Want (upgrade/future-proof)
> - Add **Portainer** for one-screen control.  
> - Add **healthchecks** and **resource limits** in the stack for stability.  
> - Use a **private registry** on MAIN for fast, consistent image updates.  
> - Add **autoscaling** later with Swarm’s replica bumps or jump to **k3s** if you insist on wearing the Kubernetes hat.
> 
> Focus, boo. This keeps your main machine free and turns the HP into a quiet work mule that does what it’s told without you logging into anything. Done. Dusted. Next bag.

### User
> 100.126.18.2 - my main computer tailspine ip and my "server" ip is 100.91.109.112

### Assistant
> Got it, network goblin. We’ll make your MAIN the Swarm manager and the HP “server” the worker. You’ll deploy from MAIN and the server will quietly eat jobs. No remoting, no drama.
> 
> ## IPs
> - MAIN (manager): `100.126.18.2`
> - SERVER (worker): `100.91.109.112`
> 
> ## 1) Spin up a tiny Docker Swarm
> 
> **On MAIN (manager):**
> ```bash
> docker swarm init --advertise-addr 100.126.18.2
> ```
> It prints a `docker swarm join ...` command with a token. Copy that.
> 
> **On SERVER (worker):**
> ```bash
> # Use the token from above; add advertise-addr for clarity
> docker swarm join --token SWMTKN-XXXX 100.126.18.2:2377 --advertise-addr 100.91.109.112
> ```
> 
> **Back on MAIN, label the SERVER so we can target it:**
> ```bash
> docker node ls
> # Find the SERVER's node name
> docker node update --label-add role=hp-worker <SERVER_NODE_NAME>
> ```
> 
> **Make a cross-machine network:**
> ```bash
> docker network create -d overlay --attachable backbone
> ```
> 
> ## 2) Deploy a stack from MAIN only
> Here’s a minimal queue + worker pattern so MAIN pushes jobs and SERVER processes them.
> 
> Create `stack.yml` on MAIN:
> ```yaml
> version: "3.9"
> 
> networks:
>   backbone:
>     driver: overlay
>     attachable: true
> 
> services:
>   redis:
>     image: redis:7
>     networks: [backbone]
>     deploy:
>       placement:
>         constraints: [node.role == manager]  # keep Redis on MAIN
> 
>   worker:
>     image: 100.126.18.2:5000/yourorg/worker:latest  # or any public image while testing
>     environment:
>       - QUEUE_HOST=redis
>     networks: [backbone]
>     deploy:
>       replicas: 2
>       placement:
>         constraints: [node.labels.role == hp-worker]  # pin workers to SERVER
>       restart_policy:
>         condition: on-failure
> 
>   api:
>     image: 100.126.18.2:5000/yourorg/api:latest  # optional: enqueue jobs via HTTP
>     environment:
>       - QUEUE_HOST=redis
>     ports:
>       - "8080:8080"
>     networks: [backbone]
>     deploy:
>       placement:
>         constraints: [node.role == manager]  # keep API on MAIN
>       restart_policy:
>         condition: on-failure
> ```
> 
> Deploy it:
> ```bash
> docker stack deploy -c stack.yml jobs
> docker stack services jobs
> docker service ps jobs_worker
> ```
> 
> You now:
> - Send jobs to the API on MAIN (or any producer code on MAIN).
> - Workers run only on SERVER and pull from Redis automatically.
> - Scale workers without touching SERVER:
> ```bash
> docker service scale jobs_worker=4
> ```
> 
> ## 3) Optional: quick private registry on MAIN
> So both boxes pull the same images fast over Tailscale.
> 
> **Registry (run from MAIN):**
> ```bash
> docker run -d --name registry --restart=always -p 5000:5000 registry:2
> ```
> 
> Build, tag, push your images from MAIN:
> ```bash
> docker build -t 100.126.18.2:5000/yourorg/worker:latest path/to/worker
> docker push 100.126.18.2:5000/yourorg/worker:latest
> ```
> Reference that tag in `stack.yml` (already shown).
> 
> ## 4) No-cluster alternative: Docker Contexts
> If you hate Swarm, you can still control SERVER from MAIN without logging in.
> 
> If Tailscale SSH is enabled to the SERVER:
> ```bash
> docker context create server --docker "host=ssh://USERNAME@100.91.109.112"
> docker --context server ps
> docker --context server compose -f worker.yml up -d
> ```
> Script it, done. But Swarm is cleaner for “push once, both act.”
> 
> ## 5) Sanity checks
> - Both machines must have time in sync and be able to talk on 2377/7946/4789 (Swarm control, gossip, VXLAN). Tailscale usually handles this without you touching firewalls.
> - If Docker Desktop on Windows: ensure WSL2 backend is on and Swarm works. If it whines, run the worker on the HP and the manager on whichever box behaves.
> 
> Focus, boo. You deploy from `100.126.18.2`, and `100.91.109.112` does the heavy lifting without you touching it. Wrapped prettier than a Sunday hat.

### User
> PS C:\WINDOWS\system32> docker swarm init --advertise-addr 100.126.18.2                                                 error during connect: Post "http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine/v1.51/swarm/init": open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.                                                              PS C:\WINDOWS\system32>

### Assistant
> Tu daemon de Docker está… muerto. Ese error del named pipe `dockerDesktopLinuxEngine` significa que **el motor de Docker no está corriendo** en Windows. No es Swarm, no es Tailscale, es que no hay servidor al cual hablar. Respira. Arreglamos eso y luego sí `swarm init`.
> 
> ## Paso 0: verifica si hay motor
> En PowerShell:
> ```powershell
> docker version   # si "Server" no aparece, el daemon está apagado
> ```
> 
> ---
> 
> ## Ruta A: Windows 10/11 con Docker Desktop (la más común)
> 
> 1) **Levanta Docker Desktop**
> ```powershell
> Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"
> ```
> Espera a que el ícono de la bandeja deje de “pensar”. Luego:
> ```powershell
> docker version
> ```
> 
> 2) **Si sigue sin levantar, revisa el servicio**
> ```powershell
> Get-Service com.docker.service
> Start-Service com.docker.service
> ```
> 
> 3) **WSL2 encendido e integrado**  
> Docker Desktop usa WSL2 por defecto. Actívalo si no lo tienes:
> ```powershell
> wsl --version         # debe mostrar versión; si no, toca instalar
> dism /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
> dism /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
> wsl --install         # instala kernel y distro base si falta
> ```
> Reinicia la PC si te lo pide. Luego, en Docker Desktop:
> - Settings → **General**: “Use the WSL 2 based engine” activado.
> - Settings → **Resources → WSL Integration**: habilita tu distro (por ejemplo “Ubuntu”).
> 
> 4) **Si prefieres Hyper-V en lugar de WSL2**  
> En Docker Desktop, cambia a **Use the legacy Hyper-V backend** y aplica. Asegúrate de tener Hyper-V activo:
> ```powershell
> dism /online /enable-feature /featurename:Microsoft-Hyper-V-All /all /norestart
> ```
> 
> 5) **Ahora sí, crea el Swarm en tu MAIN**  
> Cuando `docker version` ya muestre Client y Server:
> ```powershell
> docker swarm init --advertise-addr 100.126.18.2
> ```
> Luego unes el “server” con el token que te da.
> 
> ---
> 
> ## Ruta B: Windows Server o “sin Desktop”
> Si esto es Windows Server o desinstalaste Docker Desktop, necesitas **Docker Engine para Windows** como servicio.
> 
> 1) **Servicio del Engine**
> ```powershell
> Get-Service docker   # nombre suele ser 'docker'
> Start-Service docker
> ```
> Si el servicio no existe, instala el Engine (o repara la instalación). Al final, `docker version` debe mostrar Server.
> 
> 2) **Swarm**
> ```powershell
> docker swarm init --advertise-addr 100.126.18.2
> ```
> 
> ---
> 
> ## Checks rápidos que evitan dolores
> - **WSL2 o Hyper-V** activos, no a medias. Uno u otro, pero bien.  
> - **Docker muestra “Server”** en `docker version`. Sin server, no hay Swarm.  
> - **Firewall**: Tailscale normalmente cuida los puertos, pero Swarm usa 2377 (control), 7946 (gossip TCP/UDP) y 4789 (VXLAN).
> 
> ---
> 
> ## Después de levantar el daemon
> Cuando `docker version` ya esté bien:
> 
> En MAIN:
> ```powershell
> docker swarm init --advertise-addr 100.126.18.2
> ```
> 
> En el “server”:
> ```powershell
> docker swarm join --token <TU_TOKEN> 100.126.18.2:2377 --advertise-addr 100.91.109.112
> ```
> 
> Etiqueta el nodo del server para apuntarle los workers:
> ```powershell
> docker node ls
> docker node update --label-add role=hp-worker <NOMBRE_DEL_SERVER>
> ```
> 
> Red overlay y stack, como ya te dejé antes.  
> Nope. Reset. Nada de “se apaga solo.” Primero enciende el motor, luego domamos el Swarm. And just like that, handled.

### User
> Client:

>  Version:           28.3.0

>  API version:       1.51

>  Go version:        go1.24.4

>  Git commit:        38b7060

>  Built:             Tue Jun 24 15:44:57 2025

>  OS/Arch:           windows/amd64

>  Context:           desktop-linux

> error during connect: Get "http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine/v1.51/version": open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.

> PS C:\WINDOWS\system32>

### Assistant
> Tu cliente habla, pero el daemon está en coma. Ese pipe `dockerDesktopLinuxEngine` no existe porque Docker Desktop no está levantado o su backend (WSL2/Hyper-V) está frito. Arreglamos eso y luego armamos el Swarm.
> 
> ## Arreglar Docker en Windows (rápido y sin llorar)
> 
> ### 1) Ver si Docker Desktop está vivo
> En PowerShell (admin):
> ```powershell
> # Abre Docker Desktop
> Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"
> 
> # Espera 20–60s y verifica
> docker version
> ```
> Si “Server” sigue sin aparecer, pasa al 2.
> 
> ### 2) Levanta el servicio y WSL
> ```powershell
> # Servicio de Docker Desktop
> Get-Service com.docker.service
> Start-Service com.docker.service
> 
> # WSL debe existir y funcionar
> wsl -l -v
> # Si no ves nada o salen errores, instala/activa WSL2:
> dism /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
> dism /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
> wsl --install
> ```
> Reinicia si te lo pide. Luego abre Docker Desktop otra vez.
> 
> ### 3) Resetea el backend WSL (muy común)
> ```powershell
> # Apaga todas las distros WSL
> wsl --shutdown
> # Vuelve a abrir Docker Desktop
> Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"
> ```
> En 10–60s deberían aparecer las distros “docker-desktop” y “docker-desktop-data” cuando corras `wsl -l -v`.
> 
> ### 4) Si usas Hyper-V en lugar de WSL2
> Actívalo:
> ```powershell
> dism /online /enable-feature /featurename:Microsoft-Hyper-V-All /all /norestart
> ```
> Luego en Docker Desktop: Settings → General → activa “Use legacy Hyper-V backend”, aplica y reinicia Docker Desktop.
> 
> ### 5) Contexto correcto
> A veces el “context” apunta a algo fantasma.
> ```powershell
> docker context ls
> # Usa el que diga "desktop-linux" o "default" con TYPE=moby
> docker context use desktop-linux
> ```
> Si el daemon igual no está, da lo mismo el context: vuelve a los pasos 1–3.
> 
> ### 6) Señales rojas típicas
> - BIOS sin virtualización activa. Entra al BIOS y activa SVM/VT-x si estuviera apagado.
> - Antivirus bloqueando WSL o Docker. Haz la prueba desactivando “protección de virtualización/aislamiento” temporalmente.
> - Logs: mira `%AppData%\Docker\log\` si sigue sin levantar.
> 
> Cuando `docker version` muestre **Client** y **Server**, ya sirve. Entonces sí:
> 
> ## Crear tu mini-cluster Swarm
> 
> IPs:
> - MAIN (manager): `100.126.18.2`
> - SERVER (worker): `100.91.109.112`
> 
> **En MAIN:**
> ```powershell
> docker swarm init --advertise-addr 100.126.18.2
> ```
> 
> **En SERVER (con el token que salió arriba):**
> ```powershell
> docker swarm join --token SWMTKN-... 100.126.18.2:2377 --advertise-addr 100.91.109.112
> ```
> 
> **De vuelta en MAIN, etiqueta el SERVER:**
> ```powershell
> docker node ls
> docker node update --label-add role=hp-worker <NOMBRE_DEL_SERVER>
> ```
> 
> **Red overlay y despliegue base:**
> ```powershell
> docker network create -d overlay --attachable backbone
> ```
> 
> `stack.yml` mínimo para cola y workers:
> ```yaml
> version: "3.9"
> networks:
>   backbone:
>     driver: overlay
>     attachable: true
> 
> services:
>   redis:
>     image: redis:7
>     networks: [backbone]
>     deploy:
>       placement:
>         constraints: [node.role == manager]
> 
>   worker:
>     image: 100.126.18.2:5000/yourorg/worker:latest  # o una pública para probar
>     environment: [ "QUEUE_HOST=redis" ]
>     networks: [backbone]
>     deploy:
>       replicas: 2
>       placement:
>         constraints: [node.labels.role == hp-worker]
>       restart_policy:
>         condition: on-failure
> ```
> 
> **Desde MAIN:**
> ```powershell
> docker stack deploy -c stack.yml jobs
> docker stack services jobs
> ```
> 
> Listo: empujas trabajos desde MAIN, los containers worker jalan del queue y el SERVER mastica sin que tengas que meterte a su escritorio. Focus, boo. Eso era configuración, no brujería. Done. Dusted. Next bag.

### User
> PS C:\WINDOWS\system32> docker version

> Client:

>  Version:           28.3.0

>  API version:       1.51

>  Go version:        go1.24.4

>  Git commit:        38b7060

>  Built:             Tue Jun 24 15:44:57 2025

>  OS/Arch:           windows/amd64

>  Context:           desktop-linux

> request returned 500 Internal Server Error for API route and version http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine/v1.51/version, check if the server supports the requested API version

> PS C:\WINDOWS\system32>  -- in english please.

### Assistant
> Your Docker **client** is fine. The **daemon** behind Docker Desktop is face-planting. That 500 on `.../dockerDesktopLinuxEngine/v1.51/version` means the backend didn’t start cleanly or WSL/Hyper-V is borked. Do this in order, fast and clean:
> 
> # Fix the daemon, then swarm
> 
> ## 1) Start or restart Docker Desktop properly
> PowerShell (Admin):
> ```powershell
> # Make sure Docker Desktop is up
> Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"
> 
> # If it's already open, restart its Windows service
> Get-Service com.docker.service
> Restart-Service com.docker.service
> ```
> 
> ## 2) Hard-reset the WSL backend (most common fix)
> ```powershell
> # Stop all WSL distros
> wsl --shutdown
> 
> # Relaunch Docker Desktop
> Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"
> ```
> Wait 20–60 seconds. Then check:
> ```powershell
> wsl -l -v
> ```
> You want to see `docker-desktop` and `docker-desktop-data` listed. If they aren’t there or are “Stopped,” keep going.
> 
> ## 3) Make sure virtualization is actually on
> - In BIOS/UEFI: enable **Intel VT-x/AMD-V** (sometimes called SVM).  
> - In Windows (Admin PowerShell):
> ```powershell
> dism /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
> dism /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
> wsl --install
> ```
> Reboot if prompted, then open Docker Desktop again.
> 
> ## 4) Fix a stuck or corrupted Docker WSL distro
> If Docker Desktop still throws 500s:
> 
> A) Try a clean restart of just the Docker distros:
> ```powershell
> wsl --terminate docker-desktop
> wsl --terminate docker-desktop-data
> Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"
> ```
> 
> B) Low disk space inside the WSL VHDX can also trigger 500s. Free some Windows disk space, then compact:
> ```powershell
> wsl --shutdown
> # Optional: compact the VHDX files from Disk Cleanup or Storage Sense
> ```
> 
> C) Nuclear but effective (DESTROYS all Docker images/containers/volumes; keep only if you’re okay losing them):
> ```powershell
> wsl --shutdown
> wsl --unregister docker-desktop
> wsl --unregister docker-desktop-data
> Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"
> ```
> 
> ## 5) If you’re using Hyper-V instead of WSL2
> Enable Hyper-V fully, then switch Docker Desktop to legacy Hyper-V backend in Settings → General.
> ```powershell
> dism /online /enable-feature /featurename:Microsoft-Hyper-V-All /all /norestart
> ```
> Reboot, then open Docker Desktop.
> 
> ## 6) Sanity check your Docker context
> A wrong context won’t create a 500 by itself, but let’s align it:
> ```powershell
> docker context ls
> docker context use desktop-linux
> ```
> 
> ## 7) Verify it’s alive
> ```powershell
> docker version   # This time you should see BOTH Client and Server sections
> docker info
> ```
> 
> When the **Server** shows up, then and only then:
> 
> ## 8) Bring up your mini-swarm
> MAIN (manager) at `100.126.18.2`:
> ```powershell
> docker swarm init --advertise-addr 100.126.18.2
> ```
> SERVER (worker) at `100.91.109.112`:
> ```powershell
> docker swarm join --token <PASTE_TOKEN_HERE> 100.126.18.2:2377 --advertise-addr 100.91.109.112
> ```
> Back on MAIN:
> ```powershell
> docker node ls
> docker node update --label-add role=hp-worker <SERVER_NODE_NAME>
> docker network create -d overlay --attachable backbone
> ```
> Then deploy your stack like we outlined earlier.
> 
> Focus, boo. This isn’t “Docker is broken,” it’s “the daemon didn’t get out of bed.” Kick WSL/Hyper-V awake, relaunch Docker Desktop, and it’ll behave. Wrapped prettier than a Sunday hat.
