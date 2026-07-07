*Security Digest — 2026-07-07*
Verdict: 0 new KEV, 3 patch now (CVSS 10.0/9.9, 2 public PoC), 4 to schedule, 3 to monitor. _Sources: KEV (0 new since Jul-01), GH Advisory, EPSS_

*PATCH TODAY*
- [GHSA-vjc7-jrh9-9j86](https://github.com/advisories/GHSA-vjc7-jrh9-9j86) — 9router (npm) · CVSS 10.0 · EPSS n/a · PoC confirmed (curl)
  Unauthenticated CRUD on /api/providers + full API key + conversation leak. No patch.
  → remove 9router or block /api/providers & /api/usage/stats at network level immediately.

- [CVE-2026-54769](https://github.com/advisories/GHSA-q9p7-wqxg-mrhc) — langroid (pip) · CVSS 10.0 · EPSS n/a · PoC confirmed
  TableChatAgent eval() sandbox escape → RCE via crafted prompt. Patched at 0.65.2.
  → upgrade langroid to ≥0.65.2 and redeploy.

- [CVE-2026-55500](https://github.com/advisories/GHSA-qvfm-67h2-2qfx) — 9router (npm) · CVSS 9.9 · EPSS n/a
  Credential theft + unprotected DB export across all users. No patch.
  → isolate or remove 9router deployments today.

*PATCH THIS WEEK*
- [CVE-2026-49445](https://github.com/advisories/GHSA-3fcv-jvfp-m4q9) — cilium (go) · CVSS 9.2 · EPSS n/a · no workaround
  Envoy local admin socket world-readable → TLS secret leak + cluster disruption.
  → schedule upgrade: cilium → ≥1.19.2 / ≥1.18.8 / ≥1.17.14

- [CVE-2026-53486](https://github.com/advisories/GHSA-mp2f-45pm-3cg9) — @xhmikosr/decompress (npm) · CVSS 9.1 · EPSS n/a · no PoC
  Archive path traversal → write files outside target dir; setuid escalation possible. Upstream decompress unmaintained.
  → schedule upgrade: @xhmikosr/decompress → ≥10.2.1 / ≥11.1.3; migrate off decompress.

- [CVE-2026-55786](https://github.com/advisories/GHSA-h9f9-h6gm-wc85) — flyto-core (pip) · CVSS 8.4 · EPSS n/a
  Unauthenticated command execution via HTTP MCP execute_module endpoint.
  → schedule upgrade: flyto-core → ≥2.26.4

- coder/v2 (go) — 8 CVEs · CVSS up to 8.7 · cross-workspace rebinding, SSH config injection, OIDC account takeover, route hijacking, TLS skip
  → schedule upgrade: github.com/coder/coder/v2 → ≥2.34.2 / ≥2.33.10 / ≥2.32.9 / ≥2.29.19

*MONITOR*
- [CVE-2026-54496](https://github.com/advisories/GHSA-ww9q-8r59-xv46) — halo2_gadgets/orchard (rust) · CVSS 9.3 · no fix yet
  Missing ZK copy constraint breaks Orchard Action circuit soundness. Affects zebrad ≤4.5.1.
  → track GHSA-ww9q-8r59-xv46; avoid production Orchard deployments until patched.

- [CVE-2026-54771](https://github.com/advisories/GHSA-gjgq-w2m6-wr5q) — langroid (pip) · CVSS 8.1 · no fix yet
  handle_message() executes unverified user-supplied tool JSON — any LLM reply can trigger tools.
  → track GHSA-gjgq-w2m6-wr5q; restrict untrusted agent message paths.

- [CVE-2026-55615](https://github.com/advisories/GHSA-2pq5-3q89-j7cc) — langroid (pip) · no CVSS · no fix yet
  Neo4jChatAgent executes LLM-generated Cypher without validation → prompt-to-Cypher injection RCE.
  → track GHSA-2pq5-3q89-j7cc; disable Neo4jChatAgent in production.
