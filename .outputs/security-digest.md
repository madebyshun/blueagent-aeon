*Security Digest — 2026-10-06*
Verdict: 1 actively exploited (KEV, BOD due tomorrow), 2 PoC-confirmed CVSS 10.0, 5 to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-88779](https://nvd.nist.gov/vuln/detail/CVE-2026-88779) — Citrix NetScaler ADC/Gateway · KEV added 2026-10-04 · EPSS 0.006 · CVSS n/a
  Unauthenticated remote DoS via OOB memory buffer. BOD 26-04 compliance due 2026-10-07.
  → apply patch CTX697174 today (deadline: tomorrow).

- [CVE-2026-92946](https://github.com/advisories/GHSA-j3hm-6rg5-mchv) — vm2 (npm) · CVSS 10.0 · EPSS 0.009 · PoC public
  NodeVM require.external without require.root grants full host FS + RCE. Exploitable via vm2's own documented examples.
  → upgrade vm2 to ≥3.11.7.

- [CVE-2026-92956](https://github.com/advisories/GHSA-wjwh-qqvp-g4p4) — vm2 (npm) · CVSS 10.0 · EPSS 0.006 · PoC public
  Sandbox escape via WebAssembly Promise species bypass on Node.js 26; PoC writes to host OS.
  → upgrade vm2 to ≥3.11.7 (≥3.12.2 fixes full batch).

*PATCH THIS WEEK*
- [CVE-2026-8505](https://github.com/advisories/GHSA-cf6m-vc3m-7cgm) — langflow (pip) · CVSS 9.8 · EPSS 0.010
  Webhook auth bypass → unauth flow execution.
  → upgrade langflow to ≥1.9.1.

- [CVE-2026-10561](https://github.com/advisories/GHSA-8qpj-27x8-pwpq) — langflow (pip) · CVSS 9.9 · EPSS 0.010
  PythonREPLComponent executes unsandboxed code → auth'd RCE + privesc.
  → upgrade langflow to ≥1.10.1 (covers both Langflow CVEs).

- [CVE-2026-92934](https://github.com/advisories/GHSA-x965-fc75-jpqh) — vm2 (npm) · CVSS 9.5 · EPSS 0.008
  Sandbox escape via AggregateError Error sanitization bypass.
  → upgrade vm2 to ≥3.11.8.

- [CVE-2026-92955](https://github.com/advisories/GHSA-88hf-g992-jg85) — vm2 (npm) · CVSS 10.0 · EPSS 0.007
  NodeVM sandbox escape (batch fix #2).
  → upgrade vm2 to ≥3.11.8.

- [CVE-2026-92953](https://github.com/advisories/GHSA-3vgf-8m4q-q4qr) — vm2 (npm) · CVSS 10.0 · EPSS 0.005
  Default VM mutates host TypedArray/ArrayBuffer intrinsics, bypassing prior prototype-pollution fix.
  → upgrade vm2 to ≥3.11.8.

*MONITOR*
- [CVE-2026-87776](https://github.com/advisories/GHSA-vc2v-76pw-4v95) — compression (npm) · CVSS 7.5 · EPSS 0.006
  Memory leak DoS on premature response close. → upgrade compression to ≥1.8.2.

- [CVE-2026-92942](https://github.com/advisories/GHSA-r4fx-v8hh-22mv) — vm2 (npm) · CVSS 7.5 · EPSS 0.005
  Timeout bypass via FinalizationRegistry cleanup callback. → upgrade vm2 to ≥3.11.7.

- [CVE-2026-92959](https://github.com/advisories/GHSA-f8gf-w286-fmq2) — vm2 (npm) · CVSS 7.1 · EPSS 0.004
  allowAsync:false bypass via Promise thenable assimilation. → upgrade vm2 to ≥3.11.8.

_Also notable: Payload CMS batch (6 advisories 10-06 — SQL injection CVSS 9.8, access control bypass, MCP plugin key exposure; upgrade payload to ≥3.88.0). MCP TypeScript SDK OAuth credential redirect CVSS 7.5 → upgrade @modelcontextprotocol/sdk to ≥1.31.0._
