*Security Digest — 2026-05-31*
Verdict: 3 actively exploited (KEV-confirmed), 3 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-0257](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Palo Alto PAN-OS · KEV 2026-05-29 · EPSS 0.415
  Auth bypass allows unauthenticated attackers to establish unauthorized VPN sessions. CISA due 2026-06-01.
  → apply PAN-OS vendor patches or disable affected VPN endpoints today.

- [CVE-2026-48027](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Nx Console (npm) · KEV 2026-05-27 · EPSS 0.268
  Malicious version harvested credentials from disk and memory. Supply chain compromise.
  → audit npm lockfile for compromised Nx Console versions; upgrade to clean release.

- [CVE-2026-45321](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — TanStack (npm) · KEV 2026-05-27 · EPSS 0.171
  Malicious npm versions deployed credential-stealing malware via registry.
  → audit lockfile for compromised TanStack versions; rotate any exposed secrets.

*PATCH THIS WEEK*
- [CVE-2026-8398](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Daemon Tools Lite · KEV 2026-05-27 · EPSS 0.155
  Embedded malicious code. CISA due date 2026-05-30 has passed — high-confidence exploitation.
  → update or uninstall Daemon Tools Lite immediately.

- [GHSA-35jp-ww65-95wh](https://github.com/advisories/GHSA-35jp-ww65-95wh) — axios (npm ≥1.0.0 <1.16.0) · CVSS 8.7 · PoC confirmed
  Prototype pollution in config.proxy routes all requests through attacker proxy; intercepts Authorization headers (full MITM).
  → schedule upgrade: axios → ≥1.16.0.

- [GHSA-c3m2-jqmq-pvp3](https://github.com/advisories/GHSA-c3m2-jqmq-pvp3) — goauthentik.io (Go <20260528) · CVSS 8.5 · no public PoC
  XML Signature Wrapping in SAML ACS allows auth bypass as any federated user.
  → schedule upgrade: goauthentik.io → post-2026-05-28 commit a370d76d23c7.

*MONITOR*
- [GHSA-v6mx-mf47-r5wg](https://github.com/advisories/GHSA-v6mx-mf47-r5wg) +4 — vm2 (npm ≤3.11.3) · CVSS 10.0 · no fix · abandoned
  5 sandbox escapes published this week (builtins leak, Promise species, Symbol.for). No patch will ship.
  → migrate off vm2; consider isolated-vm or quickjs-emscripten.

- [GHSA-4mr5-g6f9-cfrh](https://github.com/advisories/GHSA-4mr5-g6f9-cfrh) — praisonaiagents (pip ≤1.6.39) · CVSS 9.9 · no fix
  Sandbox escape via print.__self__ builtins module leak in execute_code subprocess mode.
  → track; no patch yet. Avoid exposing execute_code to untrusted input.

- [GHSA-3qg8-5g3r-79v5](https://github.com/advisories/GHSA-3qg8-5g3r-79v5) — praisonai-platform (pip ≤0.1.2) · CVSS 9.8 · no fix
  JWT signing key defaults to hardcoded dev-secret; any user can forge tokens for any account.
  → track; no patch yet. Override JWT secret via PLATFORM_ENV explicitly.
