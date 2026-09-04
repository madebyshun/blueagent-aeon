*Security Digest — 2026-09-04*
Verdict: 1 actively exploited, 5 high-CVSS to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-85046](https://nvd.nist.gov/vuln/detail/CVE-2026-85046) — Google Chromium V8 · KEV added 2026-09-04 · EPSS 0.0046 · CVSS browser-scope
  Type confusion → RCE inside renderer sandbox via crafted HTML. Actively exploited in the wild; Chrome, Edge, Opera all affected. CISA due 2026-09-18.
  → update Chrome/Edge/Opera to latest build today.

*PATCH THIS WEEK*
- [CVE-2026-69084 +2](https://github.com/advisories/GHSA-vh22-h7hf-www7) — siyuan-note/siyuan (Go) · CVSS 10.0 · EPSS 0.011 · 13 advisories in 48h · no fix
  Unauthenticated SQL injection in publish mode: raw SQL exec via fullTextSearch/backlink/embed endpoints, any reader can reach them. No patch yet.
  → disable publish mode until patched; block external access to SiYuan ports.

- [CVE-2026-73843 +1](https://github.com/advisories/GHSA-qh9r-j7rp-4x2m) — openchoreo/openchoreo (Go) · CVSS 9.6 / 8.8 · EPSS 0.0029 · no fix
  Unauthenticated cluster-gateway API exposes all data-plane ops (9.6); authenticated workflow templates allow OS cmd injection in privileged pods (8.8).
  → firewall management-API port; restrict workflow template authorship.

- [CVE-2026-71428](https://github.com/advisories/GHSA-4mvj-m6j5-pmf7) — unstructured (pip) · CVSS 9.3 · EPSS 0.0025 · no fix
  SSRF in URL-based document partitioning — attacker-supplied URLs reach internal metadata services. AI/ETL pipelines exposed.
  → sanitize user-controlled URL inputs before passing to unstructured.

- [CVE-2026-62674 +2](https://github.com/advisories/GHSA-jrrm-9hc7-2v3h) — omnigent (pip) · CVSS 9.0 / 8.8 · EPSS 0.0034 · no fix
  3-CVE AI-agent RCE cluster: shared bundle overwrite → runner RCE; uploaded Python callable tools → RCE; unvalidated cwd → host filesystem traversal.
  → isolate runners; reject untrusted agent bundles until patched.

- [CVE-2026-73222](https://github.com/advisories/GHSA-79wm-x847-7cvg) — claude-code-templates (npm) · CVSS 8.8 · no fix
  Unauthenticated OS command injection in `--studio` server. Any local-network attacker gets RCE.
  → do not expose `--studio` on shared/public networks; bind localhost only.

*MONITOR*
- [GHSA-fg9p +8 variants](https://github.com/advisories/GHSA-fg9p-mrxr-hvq7) — orval (npm) · critical severity · EPSS ~0.005 · no CVSS assigned · no fix
  9 new import-time RCE variants Sep 3 via OpenAPI-spec template-literal injection (Sep 2 had 2 logged). Attack surface grows.
  → track series; avoid processing untrusted OpenAPI specs with orval.

- [CVE-2026-75931 +3](https://github.com/advisories/GHSA-5jgf-p345-68v8) — fast-uri (npm) · CVSS 7.5 · no fix
  4-CVE SSRF/host-confusion cluster: IPv6 normalization bypass, repeated percent-decode SSRF, scheme-relative confusion, scheme normalization. Widely transitive dependency.
  → watch GHSA-5jgf/f65p/fph4/jqff; sanitize URIs upstream of fast-uri consumers.

- [CVE-2026-72921](https://github.com/advisories/GHSA-gv5w-hfx8-8cwq) — seaweedfs/seaweedfs (Go) · CVSS 8.1 · no fix
  JWT allowed_prefixes literal match → cross-tenant access to sibling paths. Distinct from Sep 2's critical unauth admin (GHSA-2v6v).
  → track GHSA-gv5w; audit allowed_prefixes configuration.
