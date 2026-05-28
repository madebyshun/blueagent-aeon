*Security Digest — 2026-05-28*
Verdict: 3 actively exploited (KEV), 5 patch this week, 2 to monitor. _Sources: CISA KEV · GH Advisory · EPSS_

*PATCH TODAY*
- [CVE-2025-34291](https://nvd.nist.gov/vuln/detail/CVE-2025-34291) — Langflow (pip) · KEV 2026-05-21 · EPSS 0.35 · CVSS n/a
  CORS misconfig + refresh token bypass → full system compromise. Actively exploited.
  → patch or remove Langflow · due 2026-06-04.

- [CVE-2026-9082](https://nvd.nist.gov/vuln/detail/CVE-2026-9082) — Drupal Core · KEV 2026-05-22 · EPSS 0.34 · CVSS n/a
  DB API SQL injection → privilege escalation + RCE. CISA due date 2026-05-27 — OVERDUE.
  → apply Drupal security update immediately.

- [CVE-2026-8398](https://nvd.nist.gov/vuln/detail/CVE-2026-8398) — Daemon Tools Lite · KEV 2026-05-27 · EPSS 0.33 · CVSS n/a
  Embedded malicious code; CIA triad fully compromised.
  → remove or patch Daemon Tools Lite · due 2026-05-30.

*PATCH THIS WEEK*
- [CVE-2026-48027](https://nvd.nist.gov/vuln/detail/CVE-2026-48027) — Nx Console (npm/VSCode) · KEV 2026-05-27 · EPSS 0.27 · CVSS n/a
  Malicious extension version harvested credentials from disk + memory.
  → uninstall or pin to clean version; rotate exposed credentials.

- [CVE-2026-45321](https://nvd.nist.gov/vuln/detail/CVE-2026-45321) — TanStack (npm) · KEV 2026-05-27 · EPSS 0.15 · CVSS n/a
  Malicious npm versions published credential-stealing malware. In-the-wild exploitation confirmed.
  → audit TanStack installs; upgrade to clean release; rotate exposed creds.

- [CVE-2026-48172](https://nvd.nist.gov/vuln/detail/CVE-2026-48172) — LiteSpeed cPanel Plugin · KEV 2026-05-26 · EPSS 0.08 · CVSS n/a
  cPanel users exec arbitrary scripts as root. DUE TOMORROW 2026-05-29.
  → apply LiteSpeed cPanel plugin update now.

- [GHSA-gf2q-c269-pqgc](https://github.com/advisories/GHSA-gf2q-c269-pqgc) — liquidjs (npm) · CVSS 10.0 · EPSS 0.00 · no public PoC
  RCE via crafted templates exploiting filter evaluation. Max severity.
  → upgrade liquidjs to ≥10.26.0.

- [GHSA-mxfr-6hcw-j9rq](https://github.com/advisories/GHSA-mxfr-6hcw-j9rq) — langroid (pip) · CVSS 9.8 · EPSS 0.00
  Prompt-to-SQL injection → RCE via DB dialect primitives. AI agent framework risk.
  → upgrade langroid to ≥0.63.0.

*MONITOR*
- [GHSA-hh27-hf48-9f5q](https://github.com/advisories/GHSA-hh27-hf48-9f5q) — liquidjs (npm) · CVSS 7.5 · no fix yet · EPSS 0.00
  Memory/render limit bypass via unbounded date filter width specifiers.
  → restrict template input sources; watch for patched release.

- [GHSA-chqv-56wv-7564](https://github.com/advisories/GHSA-chqv-56wv-7564) — deno (crates.io) · CVSS 7.4 · patch: ≥2.7.8 · EPSS 0.00
  TLS retry reuses stale upgrade hook → plaintext data when autoSelectFamily enabled.
  → upgrade deno to ≥2.7.8.
