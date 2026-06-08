*Security Digest — 2026-06-08*
Verdict: 1 actively exploited, 5 to patch this week, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-28318](https://nvd.nist.gov/vuln/detail/CVE-2026-28318) — SolarWinds Serv-U · KEV added 2026-06-05 · EPSS 0.067 · CVSS N/A
  Unauthenticated DoS via crafted deflate POST — crashes the service with no auth. Exploited per CISA. Due: 2026-06-19.
  → apply SolarWinds Serv-U vendor patch or take offline.

*PATCH THIS WEEK*
- [GHSA-8v3q-9vmx-36vc](https://github.com/advisories/GHSA-8v3q-9vmx-36vc) — dbgate-serve (npm) · CVSS 10.0 · EPSS unscored
  Unauthenticated RCE via JSON Script Runner. +2 related dbgate CVEs (CVSS 9.4/9.3) same fix.
  → upgrade dbgate / dbgate-serve to ≥7.1.9.

- [GHSA-jpvj-wpmj-h7rv](https://github.com/advisories/GHSA-jpvj-wpmj-h7rv) — @cap-js/openapi (npm) · CVSS 9.6 · EPSS unscored
  Supply chain compromise: malicious code in version 1.4.1.
  → reject 1.4.1; upgrade to ≥1.4.2 now.

- [GHSA-4p62-hqp5-g644](https://github.com/advisories/GHSA-4p62-hqp5-g644) — stata-mcp (pip) · CVSS 9.3 · EPSS unscored
  Command injection via log_file_name parameter.
  → upgrade stata-mcp to ≥1.17.3.

- [GHSA-p462-prxw-mjx4](https://github.com/advisories/GHSA-p462-prxw-mjx4) — ait-core (pip) · CVSS 9.1 · EPSS unscored
  Path traversal → arbitrary file append (NASA AMMOS toolkit).
  → upgrade ait-core to ≥2.6.1 or ≥3.1.1.

- TinyMCE XSS cluster [GHSA-vg35-5wq7-3x7w](https://github.com/advisories/GHSA-vg35-5wq7-3x7w) +3 (npm) · CVSS 8.7 · EPSS 0.00032
  4 XSS vectors: media plugin, mce:protected comments, data-mce-* attrs, nested SVG bypass.
  → upgrade tinymce to ≥7.9.3 (v7), ≥8.5.1 (v8), or ≥5.11.1 LTS.

*MONITOR*
- [GHSA-q4x5-8cj6-52wg](https://github.com/advisories/GHSA-q4x5-8cj6-52wg) — @sync-in/server (npm) · CVSS 7.7 · fix: ≥2.3.0
  SSRF bypass via IPv4-mapped IPv6 addresses. → upgrade if internet-facing.

- klever-go DoS cluster [GHSA-rm5c-5x2p-48wr](https://github.com/advisories/GHSA-rm5c-5x2p-48wr) +2 (Go) · CVSS 7.5 · fix: ≥1.7.18
  3 P2P/REST DoS: nil-ptr crash, connection exhaustion, unbounded goroutines.

- [GHSA-wx3m-whqv-xv47](https://github.com/advisories/GHSA-wx3m-whqv-xv47) — skillctl (Rust) · CVSS 7.1 · fix: ≥0.1.2
  Path traversal + symlink follow → file disclosure and deletion.
