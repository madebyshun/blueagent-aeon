*Security Digest — 2026-06-01*
Verdict: 2 actively exploited (KEV), 1 urgent by CVSS 9.8+PoC, 3 to schedule, 2 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2024-21182](https://nvd.nist.gov/vuln/detail/CVE-2024-21182) — Oracle WebLogic Server · KEV added 2026-06-01 · EPSS 0.88 · CVSS N/A (KEV-confirmed)
  Unauth RCE via T3/IIOP. Actively exploited per CISA; due 2026-06-04.
  → Apply Oracle CPU patch for WebLogic today.

- [CVE-2026-48172](https://nvd.nist.gov/vuln/detail/CVE-2026-48172) — LiteSpeed cPanel Plugin · KEV added 2026-05-26 · EPSS 0.08 · CVSS N/A
  Priv escalation: any cPanel user executes scripts as root. Was due 2026-05-29 — overdue.
  → Update LiteSpeed cPanel plugin immediately.

- [GHSA-5xrq-8626-4rwp](https://github.com/advisories/GHSA-5xrq-8626-4rwp) — vitest (npm) · CVSS 9.8 · EPSS 0 · public PoC
  Vitest UI server: arbitrary file read + code execution on Windows when network-exposed.
  → upgrade vitest to ≥ 4.1.0 and redeploy.

*PATCH THIS WEEK*
- [GHSA-2h32-95rg-cppp](https://github.com/advisories/GHSA-2h32-95rg-cppp) — @vitest/browser (npm) · CVSS 9.6 · EPSS 0 · public PoC
  Unsanitized otelCarrier param → reflected XSS → RCE via embedded API token.
  → upgrade @vitest/browser to ≥ 4.1.6.

- [GHSA-87xg-pxx2-7hvx](https://github.com/advisories/GHSA-87xg-pxx2-7hvx) — dompurify (npm) · CVSS 8.2 · EPSS 0 · public PoC
  selectedcontent re-clone bypasses sanitizer; affects 3.4.4 only.
  → upgrade dompurify to ≥ 3.4.5.

- [GHSA-63gr-g7jc-v8rg](https://github.com/advisories/GHSA-63gr-g7jc-v8rg) — @agenticmail/mcp (npm) · high · no CVSS · public PoC
  MCP HTTP transport unauthenticated — anyone can invoke admin tools.
  → upgrade @agenticmail/mcp to ≥ 0.9.27.

*MONITOR*
- [GHSA-8g2p-pqm3-fcfh](https://github.com/advisories/GHSA-8g2p-pqm3-fcfh) — praisonai-platform (pip) · CVSS 9.6 · no confirmed patch · EPSS 0
  5 new auth bypass CVEs today (privesc, workspace delete, 3x IDOR). All < 0.1.4.
  → avoid multi-tenant use; watch for 0.1.4 patch.

- [GHSA-4g6j-g789-rghm](https://github.com/advisories/GHSA-4g6j-g789-rghm) — nezha (go) · CVSS 7.1 · no fix · EPSS 0
  Authenticated agents can forge monitor results for other users services.
  → watch for 1.14.15+/2.0.12+; restrict agent endpoint trust.
