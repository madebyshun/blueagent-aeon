*Security Digest — 2026-08-26*
Verdict: 1 actively exploited (KEV), 2 PoC-confirmed RCE — patch today. 5 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-60004](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Gitea · KEV 2026-08-25 · CVSS — · EPSS n/a
  Code injection via Git hooks: repo write-access → shell as Gitea service account. Exploited in wild. Due 2026-08-28.
  → apply BOD 26-04 vendor mitigations or take offline today.

- [CVE-2026-45018](https://github.com/advisories/GHSA-w3fx-mc44-mf6j) — chainlit (pip) · CVSS 9.8 · EPSS n/a · PoC public
  Unauthenticated command injection via /mcp endpoint — npx args unvalidated → RCE as Chainlit process. Requires MCP enabled.
  → upgrade chainlit to ≥2.12.0 today.

- [CVE-2026-55546](https://github.com/advisories/GHSA-mw6r-2hvm-4rp2) — qwed-mcp (pip) · CVSS 9.8 · EPSS n/a · PoC public
  parse_expr() passes user input to Python eval with unrestricted builtins → unauthenticated RCE via __import__('os').
  → upgrade qwed-mcp to ≥0.2.1 today.

*PATCH THIS WEEK*
- [CVE-2026-54523](https://github.com/advisories/GHSA-79gf-7frw-68m9) — kyverno (Go) · CVSS 9.6 · EPSS n/a · no patch yet
  Unvalidated namespace arg in NamespacedGeneratingPolicy → background controller creates RoleBindings in kube-system. Affects 1.18.0–1.18.1.
  → restrict ClusterRole; pin <1.18.0; track upstream patch.

- [CVE-2026-55536](https://github.com/advisories/GHSA-6g6r-q6gw-w8fg) — PraisonAI (pip) · CVSS 9.1 · EPSS n/a · no patch yet
  Patch bypass of CVE-2026-40289: unanchored WebSocket origin regex → CSRF on MCP HTTP server. Affects <4.6.58.
  → firewall or disable PraisonAI MCP WebSocket until patch lands.

- [CVE-2026-55585](https://github.com/advisories/GHSA-q27q-98j4-9pfv) — qwed (pip) · CVSS 8.8 · EPSS n/a · no patch yet
  Same SymPy parse_expr root cause as CVE-2026-55546 — authenticated path, different package.
  → sandbox or remove qwed until patched.

- [CVE-2026-55596](https://github.com/advisories/GHSA-qj6x-xx2h-8hvv) — @platejs/media (npm) · CVSS 8.7 · EPSS 0.43% · no patch yet
  Embed provider metadata bypasses URL sanitization → iframe JS execution. Plate editor XSS.
  → disable media embeds or block untrusted provider metadata until fix lands.

- [CVE-2026-45019](https://github.com/advisories/GHSA-hvfh-5mj3-5f3j) — chainlit (pip) · CVSS 7.2 · EPSS n/a · fix: 2.12.0
  SSRF via MCP SSE/streamable-http → unauthenticated internal network access. Companion to CVE-2026-45018.
  → upgrade chainlit to ≥2.12.0 (same fix as TODAY action).

*MONITOR*
- [CVE-2026-55677](https://github.com/advisories/GHSA-vfp3-v2gw-7wfq) — echo/v5 (Go) · CVSS 7.5 · EPSS 0.43% · no fix yet
  %2F-encoded slash bypasses route middleware → exposes static paths behind auth. → watch for patch; avoid sensitive static routes under echo/v5.

- [CVE-2026-55092](https://github.com/advisories/GHSA-mcj4-mphf-j9ff) — trivy (Go) · CVSS 7.5 · EPSS 0.44% · no fix yet
  Path traversal via crafted vuln DB or artifacts → write outside install dir. → use only trusted DB mirrors; watch upstream.

- [GHSA-vwf3-4xxj-qg6h](https://github.com/advisories/GHSA-vwf3-4xxj-qg6h) — mcp-contextforge-gateway (pip) · no CVSS · EPSS n/a · no fix yet
  Unsandboxed Jinja2 in PromptService._render_template → SSTI/RCE via untrusted prompt input. → do not expose to untrusted input; watch for patched release.
