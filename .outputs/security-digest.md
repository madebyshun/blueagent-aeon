*Security Digest — 2026-08-11*
Verdict: nothing urgent today. 1 to schedule, 0 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH THIS WEEK*
- [GHSA-cxjq-mrr5-89rv](https://github.com/advisories/GHSA-cxjq-mrr5-89rv) — Traefik (Go) · CVSS 9.1 · EPSS 0.41% · public PoC
  Auth bypass via ReplacePathRegex path traversal. Single crafted request reaches BasicAuth/ForwardAuth-protected routes on any backend that normalizes paths (Express, Flask, Django, Spring, ASP.NET). Same class as CVE-2026-48020 (StripPrefix); check applied to ReplacePathRegex. Full docker-compose PoC in advisory.
  → upgrade github.com/traefik/traefik/v2 to ≥2.11.52 or v3 to ≥3.6.23/3.7.7 and redeploy.
