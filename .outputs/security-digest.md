*Security Digest — 2026-07-28*
Verdict: 3 actively exploited, 5 to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-63030](https://nvd.nist.gov/vuln/detail/CVE-2026-63030) — WordPress Core · KEV added 2026-07-21 · EPSS 0.98
  Interpretation conflict enables unauthenticated RCE chained with CVE-2026-60137. Default installs exposed. CISA due 2026-07-24 (overdue).
  → patch WordPress Core to latest today.

- [CVE-2026-60137](https://nvd.nist.gov/vuln/detail/CVE-2026-60137) — WordPress Core · KEV added 2026-07-21 · EPSS 0.78
  SQL injection feeding the RCE chain above. Exploited in the wild.
  → same patch as above.

- [CVE-2026-50522](https://nvd.nist.gov/vuln/detail/CVE-2026-50522) — Microsoft SharePoint · KEV added 2026-07-22 · EPSS 0.57
  Deserialization of untrusted data → unauthenticated network RCE. CISA due 2026-07-25 (overdue).
  → apply Microsoft July 2026 cumulative update today.

*PATCH THIS WEEK*
- [CVE-2026-0770](https://nvd.nist.gov/vuln/detail/CVE-2026-0770) — Langflow (pip) · KEV added 2026-07-21 · EPSS 0.56
  Arbitrary code execution via untrusted functionality. AI workflow builder widely used in agentic stacks. Actively exploited.
  → upgrade langflow now or restrict to trusted networks only.

- [GHSA-w6p7-2fxx-4f44](https://github.com/advisories/GHSA-w6p7-2fxx-4f44) — pocket-id (Go) · CVSS 8.5 · EPSS 0.002
  OIDC refresh tokens bypass account disabling, group restrictions, and revocation. Disabled employees persist indefinitely.
  → upgrade pocket-id to ≥v2.6.0.

- [GHSA-4pj9-g833-qx53](https://github.com/advisories/GHSA-4pj9-g833-qx53) — lettre (crates.io) · CVSS 9.1 · EPSS 0.002
  Inverted boolean silently disables TLS hostname verification by default on boring-tls backend. Any chain-valid cert passes. MITM trivial for SMTP credential theft.
  → upgrade lettre to ≥0.11.22.

- [GHSA-8r6w-3qq5-4p4r](https://github.com/advisories/GHSA-8r6w-3qq5-4p4r) — pterodactyl/wings (Go) · CVSS 8.1
  JWT scope flaw lets subusers reuse websocket or download tokens to write arbitrary files without file.create permission.
  → upgrade wings to ≥1.12.2.

- [GHSA-w4q6-qw23-4rg7](https://github.com/advisories/GHSA-w4q6-qw23-4rg7) — github-mcp-server (Go) · CVSS 7.5
  Nil pointer dereference on malformed completion/complete request → unauthenticated crash before auth check (11.7% crash rate in fuzzing).
  → upgrade github-mcp-server to ≥v1.1.0.
