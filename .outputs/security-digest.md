*Security Digest — 2026-09-07*
Verdict: nothing urgent today. 4 to schedule, 0 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH THIS WEEK*
- [CVE-2026-69084](https://github.com/advisories/GHSA-vh22-h7hf-www7) — siyuan-note/siyuan (Go) · CVSS 10.0 · EPSS 1.1%
  Unauthenticated raw SQL on main read-write DB via /api/search/searchEmbedBlock — no admin gate; anonymous reader executes arbitrary cross-notebook statements.
  → upgrade siyuan kernel to ≥ commit 23a17d44b5f3.

- [CVE-2026-69083](https://github.com/advisories/GHSA-fph3-ghq9-vw66) — siyuan-note/siyuan (Go) · CVSS 10.0 · EPSS 0.35%
  Raw SQL execution + REGEXP injection via /api/search/fullTextSearchAssetContent — method 2 missing admin gate, method 3 unescaped quote; read-write handle.
  → upgrade siyuan kernel to ≥ commit cf42dd5680c8.

- [CVE-2026-72811](https://github.com/advisories/GHSA-q2vg-7qgx-x5fc) — siyuan-note/siyuan (Go) · CVSS 10.0 · EPSS 0.25%
  First-order (client keyword) and second-order (stored document title with apostrophe) SQL injection via backlink search — anonymous reader reachable on publish surface.
  → upgrade siyuan kernel to ≥ commit 1a5b3431d5ab.

- [CVE-2026-62681](https://github.com/advisories/GHSA-fg9p-mrxr-hvq7) — orval (npm) · CVSS 4.0 ~9.3 · EPSS N/A
  RCE via backtick in generated URL template literal — malicious OpenAPI path closes template string and executes injected JS. Affects axios/fetch/react-query/swr clients; survives Orval default validation.
  → upgrade orval to ≥ 8.21.0.
