*Security Digest — 2026-06-02*
Verdict: 3 actively exploited/KEV, 5 to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-48027](https://github.com/advisories/GHSA-rp36-8xq3-r6c4) — Nx Console (npm/VS Code ext) · KEV 2026-05-27 · EPSS 0.32 · CVSS N/A
  Supply chain: malicious version harvested credentials from disk and memory.
  → Uninstall compromised Nx Console; upgrade VS Code extension to latest verified release.

- [CVE-2026-45321](https://github.com/advisories/GHSA-rp36-8xq3-r6c4) — TanStack (npm) · KEV 2026-05-27 · EPSS 0.17 · CVSS N/A
  Supply chain: credential-stealing malware published to npm under trusted package identity.
  → Run npm audit; upgrade all @tanstack/* packages; audit CI deps.

- [GHSA-rp36-8xq3-r6c4](https://github.com/advisories/GHSA-rp36-8xq3-r6c4) + 4 related — vm2 (npm) · CVSS 10.0 · public PoC
  Sandbox escape cluster: builtin denylist bypass + JSPI Promise species bypass → host RCE confirmed.
  → upgrade vm2 to >=3.11.4 today, or migrate to isolated-vm.

_Also new in KEV: CVE-2022-0492 Linux Kernel priv-esc (EPSS 0.05) — patch OS/containers._

*PATCH THIS WEEK*
- [GHSA-3qg8-5g3r-79v5](https://github.com/advisories/GHSA-3qg8-5g3r-79v5) — praisonai-platform (pip) · CVSS 9.8
  JWT key defaults to hardcoded dev-secret-change-me. Any user token forgeable.
  → upgrade to >=0.1.4; rotate JWT_SECRET.

- [GHSA-4mr5-g6f9-cfrh](https://github.com/advisories/GHSA-4mr5-g6f9-cfrh) — praisonaiagents (pip) · CVSS 9.9
  Sandbox escape via print.__self__ builtins leak → arbitrary Python exec.
  → upgrade praisonaiagents >=1.6.40, PraisonAI >=4.6.40.

- [GHSA-29h4-r29x-hchv](https://github.com/advisories/GHSA-29h4-r29x-hchv) — redshift-connector (pip) · CVSS 9.8 · EPSS 0.00076
  eval() injection RCE via server response in amazon-redshift-python-driver.
  → upgrade redshift-connector to >=2.1.14.

- [GHSA-vg22-4gmj-prxw](https://github.com/advisories/GHSA-vg22-4gmj-prxw) — PraisonAI (pip) · CVSS 9.8
  Unauthenticated A2A endpoint reaches real LLM eval() execution.
  → upgrade PraisonAI >=4.6.40; add auth to A2A endpoints.

- [GHSA-c2m8-4gcg-v22g](https://github.com/advisories/GHSA-c2m8-4gcg-v22g) — praisonai-platform (pip) · CVSS 9.6
  Any workspace member can PATCH self to owner role.
  → upgrade praisonai-platform >=0.1.4.
