*Security Digest — 2026-07-25*
Verdict: 1 with confirmed PoC, 5 to schedule this week, 3 to monitor. _Sources: KEV no new entries, GH Advisory, EPSS_

*PATCH TODAY*
- [GHSA-7gfh-x38p-prh3](https://github.com/advisories/GHSA-7gfh-x38p-prh3) — velocityjs (npm) · CVSS 9.8 · public PoC confirmed
  RCE via property-chain → Function constructor; bypasses prior patch (GHSA-j658-c2gf-x6pq). No auth required.
  → upgrade velocityjs to ≥2.1.7 and redeploy.

*PATCH THIS WEEK*
- [GHSA-w28w-gp39-m4p6](https://github.com/advisories/GHSA-w28w-gp39-m4p6) — @prompty/core (npm) · CVSS 10.0 · EPSS n/a
  Nunjucks SSTI → full RCE on host Node.js process via constructor chain traversal; untrusted .prompty template files.
  → upgrade @prompty/core to ≥0.1.5 or ≥2.0.0-beta.5.

- [GHSA-rjg6-39jm-rgg4](https://github.com/advisories/GHSA-rjg6-39jm-rgg4) — @better-auth/scim (npm) · CVSS 9.9 · EPSS n/a
  SCIM provider-id collision links new identity to existing user → account takeover and stale access.
  → upgrade @better-auth/scim to ≥1.6.22 / ≥1.7.0-beta.10.

- [GHSA-mv8w-475r-vwqw](https://github.com/advisories/GHSA-mv8w-475r-vwqw) — seroval (npm) · CVSS 9.8 · EPSS 0.002 (CVE-2026-59940)
  fromJSON() Promise resolver type confusion invokes attacker-controlled methods during deserialization.
  → upgrade seroval to ≥1.5.3.

- [GHSA-r277-6w6q-xmqw](https://github.com/advisories/GHSA-r277-6w6q-xmqw) — kin-openapi (Go) · CVSS 9.1 · EPSS n/a
  ValidationHandler.Load() defaults to NoopAuthenticationFunc → all security schemes fail open silently.
  → upgrade github.com/getkin/kin-openapi to ≥v0.144.0.

- GitPython 5-advisory batch (pip) · CVSS 8.8 highest · EPSS n/a
  [GHSA-r9mr-m37c-5fr3](https://github.com/advisories/GHSA-r9mr-m37c-5fr3) kwarg smuggling→cmd exec · [GHSA-3rp5-jjmw-4wv2](https://github.com/advisories/GHSA-3rp5-jjmw-4wv2) config-section inject→RCE · [GHSA-6p8h-3wgx-97gf](https://github.com/advisories/GHSA-6p8h-3wgx-97gf) --template hook RCE · [GHSA-fjr4-x663-mwxc](https://github.com/advisories/GHSA-fjr4-x663-mwxc) diff output file overwrite · [GHSA-94p4-4cq8-9g67](https://github.com/advisories/GHSA-94p4-4cq8-9g67) env-var exfil via create_remote
  → upgrade GitPython to ≥3.1.55.

*MONITOR*
- @budibase/server (npm) · CVSS 9.6 · no patch yet
  8-advisory batch today: SQL inject, OIDC SSO account takeover, privilege escalation, SSRF, MongoDB NoSQL inject. No fix available.
  → restrict external Budibase API; watch for patch release.

- [GHSA-7835-87q9-rgvv](https://github.com/advisories/GHSA-7835-87q9-rgvv) — @anthropic-ai/claude-code (npm) · CVSS 7.7 · EPSS 0.006 (CVE-2026-55607)
  Sandbox escape via git worktree path confusion → unsandboxed code execution.
  → upgrade @anthropic-ai/claude-code to ≥2.1.163.

- [GHSA-hhrp-gw25-jr43](https://github.com/advisories/GHSA-hhrp-gw25-jr43) — ray (pip) · CVSS 8.8 · EPSS 0.006 (CVE-2026-57516)
  read_webdataset() calls pickle.loads() and torch.load(weights_only=False) on untrusted data → RCE.
  → upgrade ray to ≥2.56.0 (cap overflow from PATCH THIS WEEK).
