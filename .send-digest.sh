#!/usr/bin/env bash
./notify "*Security Digest — 2026-06-24*
Verdict: 3 urgent (2 KEV-confirmed infra + 1 CVSS 9.8 PoC chain), 5 to patch this week, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-34910](https://www.cve.org/CVERecord?id=CVE-2026-34910) — Ubiquiti UniFi OS · KEV added 2026-06-23 · EPSS 0.82 · CVSS n/a
  Command injection via network-authenticated actor. Also KEV: CVE-2026-34909 (path traversal) + CVE-2026-34908 (access control bypass) same product. Due 2026-06-26.
  → apply Ubiquiti UniFi OS firmware update immediately; all 3 CVEs patch together.

- [CVE-2025-67038](https://www.cve.org/CVERecord?id=CVE-2025-67038) — Lantronix EDS5000 · KEV added 2026-06-23 · EPSS 0.01 · CVSS n/a
  OS command injection via username field, runs as root. Embedded serial device server.
  → apply vendor firmware patch or discontinue use; due 2026-06-26.

- [GHSA-qxvg-h7q2-hcxh](https://github.com/advisories/GHSA-qxvg-h7q2-hcxh) — motioneye (pip) · CVSS 9.8 · EPSS n/a · public PoC
  LFI chain: pass-the-hash admin + unsafe restore = unauthenticated RCE. No confirmed patch.
  → isolate from internet; disable anon normal-user access; track for >= 0.44.0.

*PATCH THIS WEEK*
- [GHSA-8qv3-p479-cj62](https://github.com/advisories/GHSA-8qv3-p479-cj62) / CVE-2026-54350 — @budibase/server (npm) · CVSS 10.0 · EPSS n/a
  Anonymous NoSQL operator injection via published-app query templates — unauthenticated data access.
  → upgrade @budibase/server to >= 3.39.12.

- [GHSA-phv5-334h-mxcw](https://github.com/advisories/GHSA-phv5-334h-mxcw) — motioneye (pip) · CVSS critical · EPSS n/a · public PoC
  Unauth path traversal reads config; SHA-1 admin hash accepted as auth token — full admin from zero creds.
  → set non-empty normal-user password; await >= 0.44.0.

- [GHSA-gfq7-5x4g-3xhf](https://github.com/advisories/GHSA-gfq7-5x4g-3xhf) / CVE-2026-54353 — @budibase/backend-core (npm) · CVSS 8.5 · EPSS n/a · public PoC
  SSRF via DNS rebinding bypass in outbound fetch validation — reaches internal/metadata endpoints.
  → upgrade @budibase/backend-core to >= 3.39.9.

- [GHSA-4q6h-8p4v-67vq](https://github.com/advisories/GHSA-4q6h-8p4v-67vq) / CVE-2026-48153 — @budibase/server (npm) · CVSS 8.5 · EPSS 0.002 · public PoC
  SSRF via OAuth2 token endpoint reaches internal hosts and cloud metadata.
  → upgrade @budibase/server to >= 3.39.12 (latest; covers all Budibase CVEs this digest).

- [GHSA-rgvg-3wpc-h44p](https://github.com/advisories/GHSA-rgvg-3wpc-h44p) / CVE-2026-54351 — @budibase/server (npm) · CVSS 8.2 · EPSS n/a · public PoC
  Webhook mass assignment: cross-workspace automation execution via appId override.
  → upgrade @budibase/server to >= 3.39.9.

*MONITOR*
- [GHSA-rw9q-97r9-8gvh](https://github.com/advisories/GHSA-rw9q-97r9-8gvh) / CVE-2026-55488 — motioneye (pip) · CVSS high · EPSS n/a · no fix yet
  Absolute path traversal in media handlers -> arbitrary server file read. -> track upstream; isolate media endpoints.

- [GHSA-3vwc-qwhc-3mj7](https://github.com/advisories/GHSA-3vwc-qwhc-3mj7) / CVE-2026-53925 — glances (pip) · CVSS 7.8 · EPSS n/a · no fix yet
  Arbitrary file write + RCE via secure_popen in AMP command config. -> track for >= 4.5.5; restrict AMP config.

- [GHSA-87qc-fj39-wccr](https://github.com/advisories/GHSA-87qc-fj39-wccr) / CVE-2026-46608 — glances (pip) · CVSS 7.4 · EPSS n/a · no fix yet
  XML-RPC CORS wildcard fallback — incomplete fix for CVE-2026-33533. -> track for >= 4.5.5; disable XML-RPC if unused."
