*Security Digest — 2026-09-27*
Verdict: nothing urgent today. 2 to schedule, 3 to monitor. _Sources: KEV (no new adds since 09-25), GH Advisory, EPSS_

*PATCH THIS WEEK*
- [CVE-2026-61732](https://github.com/advisories/GHSA-g5f9-3xfg-p9mf) — decepticon-core/decepticon/decepticon-sdk (pip) · CVSS 10.0 · EPSS 0.012 · no patch yet
  ChatML special-token injection via web crawl output → LLM context role-boundary forgery. AI agent pipelines on ≤1.1.16 are affected.
  → remove decepticon-* from agent pipelines until patch ships.

- [CVE-2026-59723](https://github.com/advisories/GHSA-3cj3-hqcr-g934) — cline (npm) · CVSS 8.8 · EPSS 0.002 · patched at 3.0.30
  Cross-origin WebSocket hijacking in Cline Hub Dashboard /browser endpoint. Attacker page can hijack dev agent session.
  → upgrade cline to ≥3.0.30.

*MONITOR*
- [GHSA-jmg2-rcxh-w8q3](https://github.com/advisories/GHSA-jmg2-rcxh-w8q3) — @rsdoctor/rspack-plugin (npm) · CVSS 7.5 · EPSS 0.004 · no fix yet
  Unauthenticated HTTP API exposes full project source + build metadata.
  → disable rsdoctor plugin in shared/CI envs; watch for patch.

- [CVE-2026-57231](https://github.com/advisories/GHSA-4hq8-gpf5-8p68) — podman v3–v5 (Go) · CVSS 7.5 · EPSS 0.004 · patched at 5.8.4
  Malformed container image leaks host env vars into container runtime.
  → schedule podman upgrade to ≥5.8.4.

- [GHSA-29h2-jr22-frmh](https://github.com/advisories/GHSA-29h2-jr22-frmh) — @openzeppelin/confidential-contracts (npm) · CVSS 7.1 · EPSS n/a · patched at 0.3.2 / 0.4.2 / 0.5.2
  Malicious ERC-7984 token extracts private data from VestingWalletConfidential.
  → upgrade @openzeppelin/confidential-contracts per your branch.
