*Security Digest — 2026-08-22*
Verdict: 2 KEV-confirmed exploited · 1 critical PoC cluster · 5 to schedule · 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-73570](https://nvd.nist.gov/vuln/detail/CVE-2026-73570) — Zimbra ZCS · KEV 2026-08-21 · EPSS 0.005 · due 2026-08-24
  OS command injection via crafted SMTP. Unauth'd RCE as zimbra user. Exploited per CISA.
  → apply Zimbra patch or isolate SMTP port today.

- [CVE-2026-33824](https://nvd.nist.gov/vuln/detail/CVE-2026-33824) — Microsoft IKE Service Extensions · KEV 2026-08-18 · EPSS 0.779 · past due
  Double-free → remote code execution. 77.9% exploitation probability (99.5th percentile).
  → apply Windows security update immediately.

- [GHSA-66mm-25pp-rfff](https://github.com/advisories/GHSA-66mm-25pp-rfff) + 2 CVEs — jsonata (npm) · critical · public PoC
  ACE cluster: object mutation + lambda destruction chain via crafted expressions. 3 overlapping CVEs (CVE-2026-77415/14/13).
  → upgrade jsonata to ≥2.2.1 (v2.x) or ≥1.8.8 (v1.x) and redeploy.

*PATCH THIS WEEK*
- [CVE-2026-61539](https://github.com/advisories/GHSA-x2rj-828p-hx9m) — xinference (pip) · CVSS 10.0 · affects ≤2.5.0
  RCE via unsafe eval() in Llama3 tool-call response parsing. No patch yet on PyPI at time of advisory.
  → upgrade xinference when patch lands; restrict tool-call surface in the interim.

- [CVE-2026-59310](https://nvd.nist.gov/vuln/detail/CVE-2026-59310) — VMware vCenter · KEV 2026-08-18 · EPSS 0.024 · past due
  Path traversal → arbitrary code execution via network access to vCenter.
  → schedule vCenter patch; restrict management network access.

- [CVE-2026-55040](https://nvd.nist.gov/vuln/detail/CVE-2026-55040) — Microsoft SharePoint · KEV 2026-08-18 · EPSS 0.055 · past due
  Auth bypass over network. → schedule SharePoint security update.

- [CVE-2026-64679](https://github.com/advisories/GHSA-26w5-6g95-gj28) — atlantis (Go) · CVSS 8.1 · fix ≥0.45.0
  Path traversal in workspace handling → directory deletion/creation outside workspace root.
  → upgrade atlantis to ≥0.45.0.

- [CVE-2026-54245](https://github.com/advisories/GHSA-7q96-f8xw-jv5j) — fleet (Go) · high · fix ≥4.86.2
  SQL injection in Okta conditional access endpoint; host-controlled DB compromise.
  → upgrade fleet to ≥4.86.2.

*MONITOR*
- [CVE-2026-61824](https://github.com/advisories/GHSA-jg4p-g6xj-4qmf) — defuddle (npm) · CVSS 8.2 · no fix yet
  XSS via unescaped attribute interpolation in site extractors. → sanitize defuddle output; track for patch.

- [CVE-2026-68508](https://github.com/advisories/GHSA-2cp2-2r3c-7p7r) — hydra-core (pip) · CVSS 7.8 · no fix yet
  Code execution via hydra.utils.instantiate with untrusted config. → avoid untrusted config inputs.

- [CVE-2026-54155](https://github.com/advisories/GHSA-mq36-523m-x7vv) — node-opcua (npm) · CVSS 7.7 · no fix yet
  Missing nonce verification in UserNameIdentityToken auth. → monitor for patched release.
