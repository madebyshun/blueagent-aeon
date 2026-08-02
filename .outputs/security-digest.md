*Security Digest — 2026-08-02*
Verdict: 3 KEV confirmed-exploitation (Fortinet/Arista/Cisco) + 5 npm/go/pip to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2025-68686](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Fortinet FortiOS · KEV 2026-07-27 · EPSS 1.26% · CVSS N/A (check vendor)
  Info disclosure via symbolic-link persistency patch bypass. Due: Aug 10.
  → apply Fortinet vendor mitigations per BOD 26-04; discontinue if unavailable.

- [CVE-2026-16812](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Arista VeloCloud Orchestrator · KEV 2026-07-27 · EPSS 0.88% · CVSS N/A
  OS command injection → full orchestrator RCE. Due: Jul 30 (PAST DUE).
  → apply Arista vendor mitigations immediately.

- [CVE-2026-20316](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Cisco Secure FMC · KEV 2026-07-29 · EPSS 0.79% · CVSS N/A
  Hard-coded password allows unauthenticated remote login. Due: Aug 1 (PAST DUE).
  → patch immediately or discontinue.

*PATCH THIS WEEK*
- [CVE-2026-52887](https://github.com/advisories/GHSA-p849-8hwh-84j9) — @nocobase/plugin-notification-in-app-message (npm) ≤2.0.60 · CVSS 10.0 · EPSS 0.59% · public PoC
  SQL injection → PG superuser shell RCE. Anonymous reach (allowSignUp:true default).
  → upgrade to ≥2.0.61.

- [CVE-2026-54725](https://github.com/advisories/GHSA-r2v3-8gwf-7ghm) — vault-secrets-webhook (Go) ≤1.22.2 · CVSS 9.6 · EPSS 0.32% · PoC in advisory
  SSRF via vault-addr annotation at K8s admission time → SA JWT theft cluster-wide.
  → upgrade bank-vaults/vault-secrets-webhook to ≥1.23.1.

- [CVE-2026-52855](https://github.com/advisories/GHSA-pfvc-3p5h-x7h6) — pterodactyl/wings (Go) <1.12.3 · CVSS 9.9 · EPSS 0.27%
  Egg templating leaks daemon token → forge JWTs for all servers on the node.
  → upgrade to ≥1.12.3; rotate daemon tokens after.

- [CVE-2026-53609](https://github.com/advisories/GHSA-6h5j-32cf-4253) — apostrophe (npm) ≤4.30.0 · CVSS 9.1 · EPSS 0.24% · PoC included
  Prototype pollution via $pullAll → process-wide auth bypass for unauthenticated requests.
  → upgrade apostrophe to ≥4.31.0.

- [CVE-2026-53608](https://github.com/advisories/GHSA-wf43-fpp3-cf65) — @apostrophecms/seo (npm) ≤1.4.2 · CVSS 8.7 · EPSS 0.21%
  Stored XSS via unsanitized GA/GTM ID injected into HTML script tag.
  → upgrade @apostrophecms/seo to ≥1.5.0.
