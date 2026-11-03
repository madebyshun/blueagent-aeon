*Security Digest — 2026-11-03*
Verdict: 3 actively exploited, 5 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-111497](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Google Brotli · KEV 2026-10-27 · EPSS 0.826 · CVSS N/A
  Crafted compressed stream → memory corruption, data leak, possible RCE. Highest EPSS this cycle.
  → upgrade brotli to latest patched version and redeploy.

- [CVE-2026-48356](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Adobe Commerce/Magento · KEV 2026-10-27 · EPSS 0.446 · CVSS N/A
  Unrestricted file upload → code execution in current user context.
  → apply Adobe Commerce security patch and redeploy.

- [CVE-2026-97229](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — GitLab CE/EE · KEV 2026-10-29 · EPSS 0.277 · CVSS N/A
  Integer overflow in CI/CD regex → unauthenticated RCE on GitLab server.
  → upgrade GitLab to latest patched release and redeploy.

*PATCH THIS WEEK*
- [CVE-2026-46300](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Linux Kernel · KEV 2026-10-28 · EPSS 0.161 · CVSS N/A
  Uninitialized variable in ESP processing chains to PHP webshell + root exec (CVE-2026-109618/109619).
  → schedule kernel update and redeploy.

- [CVE-2026-119977](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — WordPress Core · KEV 2026-11-03 · EPSS 0.006 · CVSS N/A
  TOCTOU race during full-package upgrade → unauthenticated RCE. Added to KEV today.
  → schedule WordPress core upgrade and redeploy.

- [CVE-2026-118527](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) + [CVE-2026-111357](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Ivanti Connect Secure · KEV 2026-10-30 · EPSS 0.005 · CVSS N/A
  Predictable identifiers + missing auth check → file plant to known disk path + local privesc. Full compromise chain.
  → apply Ivanti Connect Secure vendor patches.

- [GHSA-26p8-2jq9-3vq9](https://github.com/advisories/GHSA-26p8-2jq9-3vq9) — mlflow (pip) · CVSS 9.8 · EPSS 0.007 · no public PoC
  Third-party scorer deserialization → unauthenticated RCE on exposed MLflow servers.
  → upgrade mlflow to ≥3.17.0.

- [GHSA-4xm8-rg9h-jhq2](https://github.com/advisories/GHSA-4xm8-rg9h-jhq2) — signalk-server (npm) · CVSS 9.8 · EPSS N/A · no public PoC
  Path traversal in resources API discloses JWT signing secret → RCE.
  → upgrade signalk-server to ≥2.34.0 and @signalk/resources-provider to ≥1.5.3.

*MONITOR*
- [GHSA-33r5-xmm8-v6x5](https://github.com/advisories/GHSA-33r5-xmm8-v6x5) — @enspirit/elo (npm) · CVSS 9.8 · EPSS N/A · no fix
  Sandbox escape via .constructor chain → arbitrary Node.js/browser code exec. No patch yet.
  → track GHSA-33r5-xmm8-v6x5; avoid user-supplied Elo input.

- [GHSA-f9j6-8p6x-r9j6](https://github.com/advisories/GHSA-f9j6-8p6x-r9j6) — @sd-jwt/core (npm) · CVSS N/A (high) · EPSS N/A · no fix
  Tampered SD-JWT disclosures silently dropped — verification bypass for selective disclosure claims.
  → track GHSA-f9j6-8p6x-r9j6; no patch yet.

- [GHSA-hff9-5pqw-6w9f](https://github.com/advisories/GHSA-hff9-5pqw-6w9f) — imgproxy (Go) · CVSS 9.8 · EPSS N/A · fix at 4.0.16
  ICO loader integer overflow → DoS and possible RCE on imgproxy v4.0.x.
  → upgrade imgproxy to ≥4.0.16.
