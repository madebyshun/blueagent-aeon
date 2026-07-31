*Security Digest — 2026-07-31*
Verdict: nothing urgent today. 3 clusters to schedule, 3 to monitor.
_Sources: CISA KEV, GitHub Advisory DB, FIRST EPSS_

*PATCH THIS WEEK*

- [CVE-2025-4318](https://github.com/advisories/GHSA-hf3j-86p7-mfw8) — @aws-amplify/codegen-ui-react (npm) · critical · CVSS 9.5 · EPSS 0.009
Eval injection via attacker-controlled component schema; arbitrary JS at build/import time via aws CLI import. No public PoC.
→ upgrade to ≥ 2.20.4 (2.20.3 is a partial fix only).

- [CVE-2026-54664](https://github.com/advisories/GHSA-5f94-x226-ccpm) + [CVE-2026-54661](https://github.com/advisories/GHSA-38c3-wv3c-v3xj) + [CVE-2026-54662](https://github.com/advisories/GHSA-hqj5-cw9f-rx67) — swagger-typescript-api (npm) · CVSS 8.3 · EPSS 0.003
3 new code-injection vectors: unescaped enum strings + servers[0].url in axios/fetch templates. PoC published — import of generated module fires payload. CI pipelines are attack surface if spec is vendor-controlled.
→ upgrade swagger-typescript-api to ≥ 13.12.2 (also fixes GHSA-h754-fxp7-88wx token exfil, CVSS 7.4).

- [CVE-2026-54727](https://github.com/advisories/GHSA-7h3g-4w2f-fj2f) + [CVE-2026-54574](https://github.com/advisories/GHSA-9xq3-3fqg-4vg7) — proot-distro (pip) · CVSS 8.2
Container isolation bypass via hardlink in restore archive + symlink escape on install. PoC included for both.
→ upgrade proot-distro to ≥ 5.1.6 (fixes both).

*MONITOR*

- [CVE-2026-67437](https://github.com/advisories/GHSA-xpxj-f2fm-rqch) — OliveTin (go) · CVSS 7.5 · EPSS 0.0035
Unauthenticated OAuth2 state map grows unbounded → OOM DoS. Patch available.
→ upgrade if running OliveTin with OAuth2 enabled.

- [CVE-2026-54693](https://github.com/advisories/GHSA-jq8w-8q2f-ffm9) — ZITADEL (go) · no CVSS · EPSS 0.0034
Users self-verify email/phone via direct API call, bypassing verification flow. Partial patch across v2/v3/v4 branches.
→ check branch + restrict direct API access if email/phone verification is a security control.

- [CVE-2026-54722](https://github.com/advisories/GHSA-cg4g-m8jx-vjv2) — dssrf (npm) · no CVSS · EPSS 0.0033
SSRF protection bypassed by inserting @ in URL, stripping prefix sanitization.
→ upgrade to ≥ 1.0.4 if using dssrf.
