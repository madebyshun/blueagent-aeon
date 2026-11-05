*Security Digest — 2026-11-05*
Verdict: nothing urgent today. 2 to schedule, 0 to monitor. _Sources: KEV (curl), GH Advisory, EPSS_

*PATCH THIS WEEK*
- [CVE-2026-105769](https://github.com/advisories/GHSA-5q7h-w9jf-cx97) — kaniko (Go) · CVSS 9.3 · EPSS 0.20% · no public PoC
  Azure credential exfil via unanchored ACR regex in kaniko's built-in cred helper. Lookalike host in FROM line leaks Entra ID token to attacker's registry — no RUN needed.
  → upgrade github.com/chainguard-dev/kaniko to ≥v1.25.20.

- [CVE-2026-61536](https://github.com/advisories/GHSA-64vx-6h2c-rjh7) — banks (pip) · CVSS 7.5 · EPSS 0.38% · no public PoC
  Unsafe importlib.import_module of LLM-controlled Tool.import_path in CompletionExtension. Any Elo tool_calls JSON the LLM emits can resolve to os.system or subprocess — RCE in the banks process.
  → upgrade banks to ≥2.4.3.

_KEV note: 6 recent KEV entries (Apple, WordPress, Cisco, GitLab, Ivanti ×2) all covered in prior digests._
