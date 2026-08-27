*Security Digest — 2026-08-27*
Verdict: 3 actively exploited (all CISA KEV today), 5 to patch this week (incl. 1 unpatched CVSS 9.8 RCE + 1 supply-chain compromise), 2 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- CVE-2023-49105 — ownCloud · KEV 2026-08-27 · due 2026-08-30 · EPSS 0.111 (95th pct) · CVSS ~9.8
  Unauthenticated file access/delete if victim username known and no signing-key set. Exploited in the wild.
  → apply BOD 26-04 vendor mitigations; discontinue if unavailable.

- CVE-2026-53362 — Linux Kernel IPv6 · KEV 2026-08-27 · due 2026-08-30 · EPSS 0.003
  Privilege escalation via IPv6 networking subsystem — RHEL, SUSE, upstream.
  → apply Red Hat/SUSE kernel patches and reboot today.

- CVE-2026-66384 — JFrog Artifactory · KEV 2026-08-27 · due 2026-09-10 · EPSS 0.003
  Authenticated users write outside Docker cache path under remote-repo conditions.
  → patch Artifactory to latest per BOD 26-04.

*PATCH THIS WEEK*
- GHSA-jrw6-7x4q-w25j / CVE-2026-54569 — senaite.core (pip) · CVSS 9.8 · EPSS 0.008 · PoC published · NO FIX YET
  Unauthenticated RCE: eval() in /@@API/update runs arbitrary Python on default Plone install. Full host compromise.
  → disable /@@API routes or block anonymous access until patch available.

- GHSA-93qj-5q5v-3c2h — pantheon-agents (pip) · supply-chain · PyPI 0.6.1–0.6.2 trojanized · fix via git
  Hades campaign: compromised PyPI token; wheel exfiltrates env vars, cloud creds, SSH keys on import.
  → pip uninstall; rotate all credentials; reinstall from github.com/aristoteleo/PantheonOS.

- GHSA-8vh3-g2qg-2h2c / CVE-2026-55640 — nextcloud-mcp-server (pip) · CVSS 9.1 · EPSS 0.005 · fix >=0.117.2
  Unauthenticated webhook endpoint deletes any user's vector embeddings (WEBHOOK_SECRET unset by default).
  → upgrade nextcloud-mcp-server to >=0.117.2.

- GHSA-w93q-cq9w-58p7 / CVE-2026-54606 — suneditor (npm) · CVSS v4 8.5 · fix >=3.1.4
  DOM XSS via Embed plugin: crafted iframe+script bypasses sanitizer, executes attacker JS in editor context.
  → upgrade suneditor to >=3.1.4.

- GHSA-mf7q-r4rv-jv94 — crossplane-runtime (go) · CVSS v4 8.2 · fix >=2.3.3
  TOCTOU: cosign verifies one tag, installer fetches different one from adversarial OCI registry. Signature bypass.
  → upgrade crossplane-runtime to >=2.3.3 (v2.3) or >=2.4.0-rc.1 (v2.4); use digest pins.

*MONITOR*
- GHSA-2wxc-x7rj-hg8f / CVE-2026-54591 — asyncssh (pip) · CVSS 8.1 · fix >=2.23.1
  SCP path traversal: malicious SSH server overwrites ~/.bashrc or ~/.ssh/authorized_keys for RCE chain.
  → track; upgrade asyncssh to >=2.23.1.

- GHSA-w5fv-7x5q-g8qp / CVE-2026-54563 — cloudreve v3 (go) · CVSS 7.1 · no fix for v3
  WebDAV scoped credential escapes root via %2e%2e; full owner-namespace read/write.
  → migrate to Cloudreve v4 >=4.16.1 or restrict DAV accounts to full-namespace scope.
