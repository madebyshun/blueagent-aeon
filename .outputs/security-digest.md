*Security Digest — 2026-06-20*
Verdict: 0 new KEV today, 3 PoC-confirmed, 5 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-55255](https://github.com/advisories/GHSA-qrpv-q767-xqq2) — langflow (pip) · CVSS 9.9 · EPSS —
  IDOR in /api/v1/responses — authenticated users read any workspace's AI flow outputs.
  → upgrade langflow to ≥1.9.1.

- [CVE-2026-47103](https://github.com/advisories/GHSA-v4jc-pm6r-3vj8) — python-statemachine (pip) · CVSS 9.8 · EPSS 0.008
  SCXML data-expr eval injection — arbitrary code executes on state machine load.
  → upgrade python-statemachine to ≥3.2.0.

- [CVE-2026-55447](https://github.com/advisories/GHSA-ccv6-r384-xp75) — langflow (pip) · CVSS 9.6 · EPSS —
  BaseFileComponent arbitrary file read to in-container RCE; PoC confirmed in advisory.
  → upgrade langflow to ≥1.9.2 (covers both Langflow issues above).

*PATCH THIS WEEK*
- [GHSA-2jq4-q6vv-4cp3](https://github.com/advisories/GHSA-2jq4-q6vv-4cp3) — crawl4ai (pip) · CVSS 9.6 · EPSS —
  Path traversal in downloads dir to arbitrary file write to RCE.
  → upgrade crawl4ai to ≥0.9.0.

- [CVE-2026-48814](https://github.com/advisories/GHSA-r78r-rwrf-rjwp) — network-ai (npm) · CVSS 9.1 · EPSS 0.003
  Incomplete CVE-2026-46701 fix — empty default secret still authorizes all requests.
  → upgrade network-ai to ≥5.7.2.

- [GHSA-wcpr-6g7x-p44r](https://github.com/advisories/GHSA-wcpr-6g7x-p44r) — googleapis/mcp-toolbox (Go) · CVSS — · EPSS 0.002
  Auth bypass in opaque token validation path (two CVEs, same fix).
  → upgrade mcp-toolbox to ≥1.4.0.

- [GHSA-x845-2f78-7v36](https://github.com/advisories/GHSA-x845-2f78-7v36) — blocky (Go) · CVSS 8.6 · EPSS —
  DNSSEC validation bypass + cache scope pollution — DNS spoofing risk.
  → upgrade blocky to ≥0.32.0.

- [GHSA-hxpf-9xvq-wph8](https://github.com/advisories/GHSA-hxpf-9xvq-wph8) — netlicensing-mcp (pip) · CVSS 9.6 · EPSS —
  REST path traversal bypasses token redaction — internal tokens exposed.
  → upgrade netlicensing-mcp to ≥0.1.8.

*MONITOR*
- [GHSA-wfqx-gjrf-g28r](https://github.com/advisories/GHSA-wfqx-gjrf-g28r) — crossplane (Go) · CVSS 9.0 · EPSS —
  Signature verification TOCTOU via mutable tags; v1 branch has no patch yet.
  → v2 users upgrade to ≥2.3.3; v1 users pin immutable digest refs.

- [CVE-2026-44727](https://github.com/advisories/GHSA-fcw5-x6j4-ccmp) — jupyter-server (pip) · CVSS unscored · EPSS —
  Stored XSS in NbconvertFileHandler/PostHandler.
  → upgrade jupyter-server to ≥2.20.0.

- [GHSA-rpj2-4hq8-938g](https://github.com/advisories/GHSA-rpj2-4hq8-938g) — vcrpy (pip) · CVSS 7.8 · EPSS —
  Unsafe YAML deserialization of cassette files to RCE in test environments.
  → upgrade vcrpy to ≥8.2.1.
