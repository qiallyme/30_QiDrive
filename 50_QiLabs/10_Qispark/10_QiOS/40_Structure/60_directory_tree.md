---
layout: page
title: Ideal Directory Tree
slug: ideal-directory-tree
status: publish
updated_at: "2026-06-29"
tags:
  - qispark
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

# Ideal Directory Tree

This document outlines the official filesystem structure for an enrolled QiOS node.

```markdown
C:/QiLabs/
├── QiData/
│   ├── assigned_watch/
│   │   ├── .gitkeep
│   │   └── README.md
│   ├── backups/
│   │   └── .gitkeep
│   ├── devices/
│   │   └── this-device/
│   │       ├── capabilities.json
│   │       ├── device.json
│   │       ├── last_heartbeat.json
│   │       └── watcher_assignments.json
│   ├── dropzones/
│   │   ├── default/
│   │   │   └── .gitkeep
│   │   ├── imports/
│   │   │   └── .gitkeep
│   │   ├── mobile/
│   │   │   └── .gitkeep
│   │   ├── scans/
│   │   │   └── .gitkeep
│   │   └── README.md
│   ├── embeddings_cache/
│   │   └── .gitkeep
│   ├── extracted_text/
│   │   └── .gitkeep
│   ├── failed/
│   │   └── .gitkeep
│   ├── inbox/
│   │   ├── .gitkeep
│   │   └── README.md
│   ├── logs/
│   │   ├── ingest/
│   │   │   └── .gitkeep
│   │   ├── local-agent/
│   │   │   └── .gitkeep
│   │   ├── runtime/
│   │   │   └── .gitkeep
│   │   └── sync/
│   │       └── .gitkeep
│   ├── manifests/
│   │   └── .gitkeep
│   ├── model_cache/
│   │   └── .gitkeep
│   ├── normalized/
│   │   └── .gitkeep
│   ├── previews/
│   │   └── .gitkeep
│   ├── processing/
│   │   └── .gitkeep
│   ├── quarantine/
│   │   └── .gitkeep
│   ├── reviewed/
│   │   └── .gitkeep
│   ├── state/
│   │   ├── local-agent/
│   │   │   ├── cursor.json
│   │   │   ├── locks.json
│   │   │   └── queue.json
│   │   ├── runtime/
│   │   │   ├── embeddings_state.json
│   │   │   ├── pipeline_state.json
│   │   │   └── repair_state.json
│   │   └── sync/
│   │       ├── conflict_log.json
│   │       └── sync_cursor.json
│   ├── tmp/
│   │   └── .gitkeep
│   └── README.md
├── _QiOne_MonoRepo/
│   ├── .github/
│   │   ├── ISSUE_TEMPLATE/
│   │   │   ├── architecture_change.md
│   │   │   ├── bug_report.md
│   │   │   └── feature_request.md
│   │   ├── workflows/
│   │   │   ├── ci.yml
│   │   │   ├── docs.yml
│   │   │   ├── lint.yml
│   │   │   ├── migrations.yml
│   │   │   ├── release.yml
│   │   │   └── test.yml
│   │   ├── CODEOWNERS
│   │   └── pull_request_template.md
│   ├── apps/
│   │   ├── docs-site/
│   │   │   ├── overrides/
│   │   │   ├── README.md
│   │   │   ├── mkdocs.yml
│   │   │   └── package.json
│   │   ├── qially-web/
│   │   │   ├── public/
│   │   │   ├── src/
│   │   │   ├── README.md
│   │   │   ├── index.html
│   │   │   ├── package.json
│   │   │   └── vite.config.ts
│   │   └── qione-portal/
│   │       ├── public/
│   │       ├── src/
│   │       ├── README.md
│   │       ├── index.html
│   │       ├── package.json
│   │       ├── tsconfig.json
│   │       └── vite.config.ts
│   ├── docs/
│   │   └── __QiOS_Master_Blueprint_v0.4/
│   │       ├── 01_governance/
│   │       ├── 02_architecture/
│   │       ├── 03_structure/
│   │       ├── 04_data/
│   │       ├── 05_compute/
│   │       ├── 06_applications/
│   │       ├── 07_operations/
│   │       ├── adr/
│   │       ├── appendices/
│   │       └── index.md
│   ├── examples/
│   │   ├── archive_manifest.example.json
│   │   ├── fleet_job_payload.example.json
│   │   ├── local-agent.env.example
│   │   └── watcher_paths.example.yaml
│   ├── infra/
│   │   ├── docker/
│   │   │   ├── ai-api.Dockerfile
│   │   │   ├── app-api.Dockerfile
│   │   │   ├── compose.dev.yml
│   │   │   ├── local-agent.Dockerfile
│   │   │   └── worker-orchestrator.Dockerfile
│   │   ├── neo4j/
│   │   │   └── README.md
│   │   ├── redis/
│   │   │   └── README.md
│   │   ├── supabase/
│   │   │   ├── functions/
│   │   │   ├── migrations/
│   │   │   ├── config.toml
│   │   │   └── seed.sql
│   │   ├── tailscale/
│   │   │   ├── README.md
│   │   │   ├── acl.example.json
│   │   │   └── node-enrollment.md
│   │   └── README.md
│   ├── packages/
│   │   ├── config/
│   │   │   ├── eslint/
│   │   │   ├── prettier/
│   │   │   ├── tsconfig/
│   │   │   └── package.json
│   │   ├── db/
│   │   │   ├── src/
│   │   │   └── package.json
│   │   ├── domain-types/
│   │   │   ├── src/
│   │   │   └── package.json
│   │   ├── spine/
│   │   │   ├── src/
│   │   │   └── package.json
│   │   ├── ui/
│   │   │   ├── src/
│   │   │   ├── package.json
│   │   │   └── tsconfig.json
│   │   └── utils/
│   │       ├── src/
│   │       └── package.json
│   ├── scripts/
│   │   ├── archive/
│   │   │   ├── rebuild-manifest.py
│   │   │   ├── reconcile-lineage.py
│   │   │   ├── register-file.py
│   │   │   └── retry-failed.py
│   │   ├── db/
│   │   │   ├── db-migrate.ps1
│   │   │   ├── db-reset.ps1
│   │   │   ├── db-seed.ps1
│   │   │   ├── db-start.ps1
│   │   │   └── db-stop.ps1
│   │   ├── dev/
│   │   │   ├── check-env.ps1
│   │   │   ├── check-env.sh
│   │   │   ├── dev.ps1
│   │   │   ├── dev.sh
│   │   │   ├── start-ai-api.ps1
│   │   │   ├── start-app-api.ps1
│   │   │   ├── start-local-agent.ps1
│   │   │   ├── start-local-agent.sh
│   │   │   └── start-workers.ps1
│   │   ├── docs/
│   │   │   ├── docs-build.ps1
│   │   │   ├── docs-serve.ps1
│   │   │   └── docs-validate.ps1
│   │   ├── fleet/
│   │   │   ├── assign-watch-path.ts
│   │   │   ├── check-heartbeats.ts
│   │   │   ├── dispatch-node-job.ts
│   │   │   ├── issue-enrollment-token.ts
│   │   │   └── revoke-device.ts
│   │   ├── repo/
│   │   │   ├── enforce-structure.py
│   │   │   ├── lint-tree.py
│   │   │   ├── print-tree.py
│   │   │   └── validate-paths.py
│   │   └── README.md
│   ├── services/
│   │   ├── ai-api/
│   │   │   ├── app/
│   │   │   ├── README.md
│   │   │   ├── pyproject.toml
│   │   │   └── requirements.txt
│   │   ├── app-api/
│   │   │   ├── src/
│   │   │   ├── README.md
│   │   │   ├── package.json
│   │   │   └── tsconfig.json
│   │   ├── local-agent/
│   │   │   ├── app/
│   │   │   ├── tests/
│   │   │   ├── .env.example
│   │   │   ├── README.md
│   │   │   ├── agent.py
│   │   │   ├── main.py
│   │   │   ├── pyproject.toml
│   │   │   └── requirements.txt
│   │   └── worker-orchestrator/
│   │       ├── app/
│   │       ├── README.md
│   │       ├── main.py
│   │       ├── pyproject.toml
│   │       └── requirements.txt
│   ├── tests/
│   │   ├── e2e/
│   │   │   ├── admin-device-registry.spec.ts
│   │   │   ├── archive-dropzone.spec.ts
│   │   │   └── portal-auth.spec.ts
│   │   ├── fixtures/
│   │   │   ├── sample.pdf
│   │   │   ├── sample_email.eml
│   │   │   └── sample_metadata.json
│   │   ├── integration/
│   │   │   ├── test_archive_registration.py
│   │   │   ├── test_device_enrollment.py
│   │   │   ├── test_fleet_job_dispatch.py
│   │   │   └── test_watch_assignment.py
│   │   └── README.md
│   ├── .editorconfig
│   ├── .gitattributes
│   ├── .gitignore
│   ├── .prettierignore
│   ├── .prettierrc
│   ├── LICENSE
│   ├── README.md
│   ├── eslint.config.js
│   ├── mkdocs.yml
│   ├── package.json
│   ├── pnpm-lock.yaml
│   ├── pnpm-workspace.yaml
│   ├── tsconfig.base.json
│   └── turbo.json
├── bootstrap/
│   ├── templates/
│   │   ├── local-agent.env.template
│   │   ├── qilabs.env.template
│   │   └── watcher_paths.template.yaml
│   ├── README.md
│   ├── enroll_device.ps1
│   ├── enroll_device.sh
│   ├── install_local_agent.ps1
│   ├── install_local_agent.sh
│   ├── install_qilabs.ps1
│   ├── install_qilabs.sh
│   ├── validate_machine.ps1
│   └── validate_machine.sh
├── config/
│   ├── global/
│   │   ├── device_policy.yaml
│   │   ├── metadata_rules.yaml
│   │   ├── naming_rules.yaml
│   │   ├── repo_rules.yaml
│   │   ├── runtime_rules.yaml
│   │   └── watcher_rules.yaml
│   ├── local/
│   │   ├── dropzones.yaml
│   │   ├── embeddings.yaml
│   │   ├── local_agent.yaml
│   │   ├── ocr.yaml
│   │   └── watcher_paths.yaml
│   ├── secrets/
│   │   └── .gitkeep
│   └── README.md
├── tools/
│   ├── docs/
│   │   ├── backup_restore.md
│   │   ├── device_enrollment.md
│   │   ├── panic_recovery.md
│   │   └── workstation_setup.md
│   ├── scripts/
│   │   ├── backup_qidata.ps1
│   │   ├── repair_repo.ps1
│   │   ├── repair_repo.sh
│   │   ├── restore_qidata.ps1
│   │   ├── tree_snapshot.ps1
│   │   ├── tree_snapshot.sh
│   │   ├── verify_env.ps1
│   │   └── verify_env.sh
│   └── README.md
├── .env.example
├── .gitignore
└── README.md
```
