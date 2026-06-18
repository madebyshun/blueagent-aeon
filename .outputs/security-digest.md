*Security Digest — 2026-06-18*
Verdict: 2 actively exploited (KEV), 5 to patch this week, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- CVE-2026-10520 — Ivanti Sentry · KEV added 2026-06-11 · EPSS 0.595 (99th pct) · CVSS n/a (KEV)
  OS command injection → unauth root RCE when admin endpoints exposed. Missed yesterday (added Jun 11, below yesterday's cap).
  → patch Ivanti Sentry to vendor-advised version and restrict admin endpoint access now.

- CVE-2026-20253 — Splunk Enterprise · KEV added 2026-06-18 · EPSS 0.017 · CVSS n/a (KEV)
  Missing auth in PostgreSQL sidecar → unauth file create/truncate on the host. Fresh KEV add today.
  → apply Splunk mitigations per vendor advisory and restrict PostgreSQL sidecar endpoints today.

*PATCH THIS WEEK*
- GHSA-v4jc-pm6r-3vj8 / CVE-2026-47103 — python-statemachine (pip) · CVSS 9.8 · EPSS 0.008
  SCXML <data expr> eval injection → RCE on crafted state machine input.
  → upgrade python-statemachine to ≥3.2.0.

- GHSA-fcw5-x6j4-ccmp / CVE-2026-44727 — jupyter-server (pip) · CVSS 9.3 · EPSS n/a
  Stored XSS in NbconvertFileHandler/PostHandler via missing sandbox CSP.
  → upgrade jupyter-server to ≥2.20.0.

- GHSA-p69m-4f92-2v84 +3 — praisonai (npm ≤1.7.1) · CVSS 9.8 · EPSS n/a
  4 advisories: unauthenticated agent listing, unauthenticated MCP tool calls, RCE via codeMode sandbox escape (Function constructor).
  → upgrade praisonai (npm) to ≥1.7.2.

- GHSA-cwj8-7gp2-ggcw — praisonai-platform (pip ≤0.1.4) · CVSS 9.8 · EPSS n/a
  Hardcoded JWT secret 'dev-secret-change-me' in default deployment → trivial token forgery.
  → upgrade praisonai-platform to ≥0.1.6.

- GHSA-29w3-p9w9-wc47 +2 — praisonai (pip <4.6.61) · CVSS 9.1 · EPSS n/a
  Arbitrary file R/W via multiedit + sandbox escape via Landlock fallback + auth bypass via env var.
  → upgrade praisonai (pip) to ≥4.6.61.

*MONITOR*
- GHSA-vmh5-mc38-953g / CVE-2026-9697 — undici (npm) · CVSS 7.4 · EPSS 0.002
  SOCKS5 proxy silently drops requestTls → TLS cert validation bypass. Patch: 7.28.0 / 8.5.0.
  → upgrade undici when convenient; audit services using SOCKS5 proxies.

- GHSA-38rv-x7px-6hhq / CVE-2026-9675 — undici (npm) · CVSS 7.5 · EPSS 0.003
  Fragmented WebSocket messages bypass cumulative payload limits → OOM DoS. Patch: 8.5.0.
  → upgrade undici to ≥8.5.0 when convenient.

- GHSA-p6gq-j5cr-w38f — nodemailer (npm ≤9.0.0) · CVSS 7.1 · EPSS n/a
  message.raw bypasses disableFileAccess/disableUrlAccess → SSRF + arbitrary local file read.
  → upgrade nodemailer to ≥9.0.1 when convenient.
