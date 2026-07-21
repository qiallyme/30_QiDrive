# QiLife App Placement

Notes: Merged QiLife placement in QiOS, app home, docs home, and system boundary roles.
QiCode: § 03.05.006
Sort Key: 03.05.006
Status: active
Tags: Core, Hubs, Registry/Archive
Type: Standard
Version: Reconciled V1

**Merged from:** QiLife Data Model Spine  

**System:** QiOS  

**Parent App:** QiLife  

**Status:** Active Doctrine  

**Version:** Reconciled V1

## Position in QiOS

```
QiOS
├── QiSpark
│   └── homepage, docs, doctrine, maps, guides, bookmarks
│
├── QiApps
│   └── QiLife, MomCare, utilities, dashboards, experiments
│
├── QiDrive
│   └── files, evidence, documents, assets, exports, archives
│
├── QiServer
│   └── runtime, cockpit, docker, databases, services, local AI
│
├── QiConnect
│   └── Google, GitHub, Supabase, imports, exports, sync jobs
│
└── QiArchive
    └── old systems, deprecated builds, frozen exports
```

QiLife lives in **QiApps**.

QiSpark documents it.

QiDrive stores related files.

QiServer may run it.

QiConnect may sync into it.

QiArchive preserves inactive versions.

## App Placement

- **App Home:** `QiApps/QiLife`
- **Docs Home:** `QiSpark/docs`
- **File Backbone:** QiDrive

## Architecture Rule

QiLife is the app-layer operating system for living records. It should stay inside **QiApps**, while doctrine and published documentation live in **QiSpark**, files live in **QiDrive**, runtime services live in **QiServer**, sync pathways live in **QiConnect**, and inactive versions live in **QiArchive**.