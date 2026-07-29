# QiCode Conformance

QiCode doctrine is stable. Application conformance is recorded separately so
implementation status can change without rewriting doctrine.

Each system declares one row per provision. `aligned` requires evidence.
Repository evidence uses paths relative to the repository being verified.
Partial, missing, deferred, and unverified rows explain the gap in `notes`.

Run QiLife validation from its repository:

```powershell
node scripts/validate-qicode-conformance.mjs
```

The validator rejects unknown or superseded provisions, invalid statuses,
duplicate rows, evidence-free alignment, missing repository paths, and
contradictory active provisions.
