*Security Digest — 2026-09-19*
Verdict: 3 urgent (2 KEV infra + 1 pip exploit chain), 5 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- CVE-2025-39682 + CVE-2025-39964 + CVE-2026-53266 — Linux Kernel · KEV added 2026-09-18 · EPSS 0.012/0.008/0.003 · CVSS n/a
  TLS zero-length bypass, AF_ALG race, ebtables OOB write — 3 kernel exploits added to KEV yesterday.
  → apply kernel security patches and reboot affected hosts today.

- CVE-2025-66455 (GHSA-2vh9-42vm-xmv2) — lmdeploy (pip) · CVSS 9.8 · EPSS 0.007 · public PoC in advisory
  Unauthenticated RCE via pickle deserialization on DistServe /p2p_connect endpoint. Full exploit chain documented.
  → upgrade lmdeploy to >=0.16.0 and redeploy exposed DistServe endpoints today.

- CVE-2026-76461 — Cisco Secure Email Gateway · KEV added 2026-09-14 · EPSS 0.020 · CVSS n/a
  AsyncOS SQL injection = unauthenticated RCE with root. Highest EPSS of this week's KEV batch.
  → apply Cisco AsyncOS patch; verify mgmt interface is not internet-exposed.

*PATCH THIS WEEK*
- GHSA-c8w2-fgvx-vhv4 (CVE-2026-61682) — kcp (Go) · CVSS 9.9 · EPSS 0.003
  Front-proxy fails to strip X-Remote-* headers; any authenticated tenant can forge system:masters across all workspaces.
  → schedule upgrade: github.com/kcp-dev/kcp → >=v0.31.4 (or >=v0.32.2).

- GHSA-82r6-8w77-94w6 (CVE-2026-63374) — anyio (pip) · CVSS 9.3 · EPSS 0
  IDNA 2003 encoding enables TLS certificate spoofing for internationalized domain names.
  → schedule upgrade: anyio → >=4.14.2.

- GHSA-xcw4-53cc-hv32 (CVE-2026-59163) — mnemosyne-memory (pip) · CVSS 9.1 · EPSS 0.003
  JWT signature never verified on sync server; any well-formed token authenticates as any user.
  → schedule upgrade: mnemosyne-memory → >=3.10.1.

- GHSA-xwmw-prc4-v3cr — Obot (Go) · CVSS 8.8 · EPSS 0
  Unauthenticated OAuth client registration + no consent screen leaks full-access API tokens via one crafted link.
  → schedule upgrade: github.com/obot-platform/obot → >=v0.23.0.

- CVE-2026-76460 — Cisco Identity Services Engine · KEV added 2026-09-16 · EPSS 0.008
  Unauth'd privilege escalation via privileged API misuse on web management interface.
  → schedule Cisco ISE patch per vendor advisory.

*MONITOR*
- GHSA-jgh3-fggc-mcpm — Obot (Go) · CVSS 7.6 · EPSS 0 · fix: v0.23.0
  SSRF via unvalidated remote MCP server URL; can pivot to cloud metadata endpoint (169.254.169.254).
  → fix bundled with GHSA-xwmw-prc4-v3cr above; patch together.

- GHSA-vr5f-w35q-98jp (CVE-2026-63445) — perses (Go) · CVSS 7.1 · EPSS 0.006 · fix: v0.54.0-rc.0 only
  Path traversal on list endpoints reads arbitrary files from filesystem database.
  → avoid perses filesystem DB in prod; watch for stable release.

- CVE-2026-87886 — Acronis Backup · KEV added 2026-09-16 · EPSS 0.003
  Incorrect default permissions in cPanel/Plesk plugins enable local privilege escalation.
  → apply vendor patch if running Acronis Backup with cPanel or Plesk.
