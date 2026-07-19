*Security Digest — 2026-07-19*
Verdict: nothing urgent today. 0 to schedule, 3 to monitor. _Sources: KEV (no new since Jul 16), GH Advisory, EPSS_

*MONITOR*
- [CVE-2026-54567 / GHSA-937x-gpqr-72gg](https://github.com/advisories/GHSA-937x-gpqr-72gg) — Flask-Reuploaded (pip) · CVSS 7.5 · EPSS N/A · no patch yet
  Extension denylist bypass via Unicode case-folding in filename-override path. Incomplete fix for CVE-2026-27641; all versions ≤ 1.5.0 still vulnerable.
  → watch for patched release; apply server-side type validation beyond extension checks.

- [CVE-2026-54234 / GHSA-8wr5-jm2h-8r4f](https://github.com/advisories/GHSA-8wr5-jm2h-8r4f) — vllm (pip) · CVSS 7.5 · EPSS 0.003 · fix: ≥ 0.24.0
  Remote DoS via invalid recovered token reinjection affecting ≥ 0.17.1 < 0.24.0. Second vllm CVE this week — same fix as Jul 18 notice.
  → upgrade vllm to ≥ 0.24.0 if not already done per Jul 18 advisory.

- [CVE-2026-55177 / GHSA-r95q-fp26-h3hc](https://github.com/advisories/GHSA-r95q-fp26-h3hc) — @tak-ps/cloudtak (npm) · CVSS N/A · EPSS N/A · fix: ≥ 13.10.0
  Authenticated SSRF on /api/esri* routes; user-supplied URL fetched without IP-classification guard. Requires auth to exploit.
  → upgrade @tak-ps/cloudtak to ≥ 13.10.0 if deployed.
