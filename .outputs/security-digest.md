*Security Digest — 2026-07-21*
Verdict: 3 actively exploited (KEV added today), 5 to patch this week, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- CVE-2026-0770 — Langflow (pip) · KEV 2026-07-21 · EPSS 0.10 · CVSS n/a
  RCE on Langflow instances, exploited in the wild per CISA (due 2026-07-24).
  → isolate Langflow from public network; apply mitigations or discontinue use.

- CVE-2026-63030 + CVE-2026-60137 — WordPress Core · KEV 2026-07-21 · EPSS 0.09/0.04
  SQL injection + interpretation conflict chain = unauthenticated RCE on default installs. Due 2026-07-24.
  → update WordPress Core immediately; apply BOD 26-04 mitigations.

- CVE-2021-27137 — DD-WRT firmware · KEV 2026-07-21 · EPSS 0.05 · CVSS n/a
  UPnP stack overflow → unauthenticated code exec. 2021 CVE now actively exploited. Due 2026-07-24.
  → patch DD-WRT to latest build with UPnP fix; disable UPnP if patch unavailable.

*PATCH THIS WEEK*
- CVE-2026-59873 (GHSA-23hp-3jrh-7fpw) — tar (npm) · CVSS 9.2 · EPSS 0.004 · public PoC
  Gzip bomb: no decompression limits → disk exhaust + service crash. PoC documented.
  → upgrade tar to ≥7.5.19.

- CVE-2026-61736 + CVE-2026-61740 (GHSA-6x6h-qqr7-855w / GHSA-f4vv-55c2-5789) — lightrag-hku (pip) · CVSS 9.3 + auth bypass · EPSS 0.004/0.003
  CORS wildcard with credentials (9.3) + hardcoded DEFAULT_TOKEN_SECRET defeats API key protection.
  → upgrade lightrag-hku to ≥1.5.4.

- CVE-2026-61836 + CVE-2026-61835 (GHSA-c6w9-5g5j-jh2p / GHSA-j5h6-vqc3-phqh) — directus (npm) · CVSS 8.6 / 7.7 · EPSS 0.003
  Auth-gated responses leak via shared cache key + SSRF bypass via 0.0.0.0.
  → upgrade directus to ≥12.0.0.

- CVE-2026-59731 (GHSA-vj59-8hwv-xxmv) — astro (npm) · CVSS 8.2 · EPSS 0.003
  Auth bypass via decode iteration limit + rewrite path canonicalization mismatch.
  → upgrade astro to ≥6.4.8.

- 8 CVEs — Pillow (pip) · CVSS 7.5–8.2 · EPSS up to 0.004
  Heap OOB writes, decompression bomb bypasses via font loading, OOB read via McIdas AREA files.
  → upgrade Pillow to ≥12.3.0 when released; pin to latest 12.x now.

*MONITOR*
- GHSA-7rc3-g7h6-22m7 + GHSA-fmm7-x4gx-8jhr — filebrowser (Go) · CVSS 8.2/8.1 · no patch yet
  Username normalization collision → shared home dirs; Create-only user deletes arbitrary files via symlink.
  → track filebrowser releases; restrict to trusted users only.

- GHSA-c8j7-8cv4-2xmq + GHSA-4j32-57v6-6g45 + GHSA-ffq3-xpv3-j92q — mistune (pip) · CVSS 7.5 · no patch
  Quadratic-time parsing on emphasis, strikethrough, and reference-link inputs; DoS on untrusted markdown.
  → watch for mistune 3.3.0; cap untrusted input lengths as interim mitigation.

- GHSA-r635-g3xr-vw7x (CVE-2026-59725) — engine.io (npm) · CVSS 7.5 · fix ≥6.6.7
  Polling transport connection exhaustion → socket.io service denial.
  → upgrade engine.io to ≥6.6.7 if in socket.io stack.

