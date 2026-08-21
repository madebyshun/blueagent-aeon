*Security Digest — 2026-08-21*
Verdict: 2 actively exploited (KEV), 3 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- CVE-2026-72529 — TrueConf Server (all) · KEV 2026-08-20 · due 2026-08-23 · EPSS 0.003 · CVSS n/a
  Missing auth on port 4307/TCP — unauthenticated remote script execution. CISA-confirmed exploitation.
  → apply TrueConf vendor patch; firewall 4307/TCP if patch unavailable. Due in 2 days.

- CVE-2026-72530 — TrueConf Server (all) · KEV 2026-08-20 · due 2026-09-03 · EPSS 0.003 · CVSS n/a
  Code injection via port 4307/TCP — unauthenticated RCE on host. CISA-confirmed exploitation.
  → apply TrueConf vendor patch today.

*PATCH THIS WEEK*
- GHSA-rrwh-6jrq-wp5v / CVE-2026-54061 — dgraph (go) · CVSS 9.1 · EPSS 0.004 · public PoC
  Unauthenticated gRPC snapshot import replaces/clears group stores. Complete PoC published.
  → upgrade github.com/dgraph-io/dgraph/v25 to >=25.3.5.

- GHSA-ghvf-qf6h-g8x5 — @nocobase/server (npm) · high · no PoC
  Arbitrary file write chained with LFI leads to RCE. Fix available.
  → upgrade @nocobase/server to >=2.1.5.

- GHSA-f5f4-3hh4-f54m / CVE-2026-54167 — pipelines-as-code (go) · CVSS 8.2 · no public PoC
  Malicious Enterprise-Host header redirects GitHub App token — credential exfiltration.
  → upgrade openshift-pipelines/pipelines-as-code to >=0.48.0 / >=0.42.1 / >=0.39.6.

*MONITOR*
- GHSA-v667-gc2r-2xm7 / CVE-2026-55445 — @whyour/qinglong (npm) · critical · EPSS 0.004 · no fix
  Incomplete patch for CVE-2026-3965 — /open/user/init rewrites past auth guard → unauth admin reset.
  → no patch yet; restrict panel network access.

- GHSA-533j-2v4q-mw5h / CVE-2026-55253 — langgraph-checkpoint-mongodb + langgraph-store-mongodb (pip) · CVSS 7.7
  NoSQL operator injection in MongoDBSaver.list() → cross-tenant data exposure.
  → upgrade checkpoint-mongodb >=0.3.0 and store-mongodb >=0.4.0.

- GHSA-23m2-mghx-vqmf / CVE-2026-54263 — wagtail (pip) · CVSS 7.3 · EPSS 0.002
  Reflected XSS in dynamic image URL generator. No server-side PoC.
  → upgrade wagtail to >=7.3.3 or >=7.4.2.
