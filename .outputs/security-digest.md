Done. Here's the full digest output:

---

**Security Digest — 2026-08-15**

**Verdict:** nothing urgent today. 5 to schedule, 3 to monitor.

---

**PATCH THIS WEEK**

- **[CVE-2026-70477](https://github.com/advisories/GHSA-5xvg-pmgg-3mxr)** — flowise (npm) · CVSS 9.5 · EPSS 0.004 · public PoC (ZDI)
  Prompt injection → unauthenticated RCE via CSV Agent. Pyodide unsandboxed; 8 regex-bypass techniques confirmed. Reachable via public prediction endpoint.
  → upgrade flowise to ≥ 3.1.3 (also closes CVE-2026-70478 OAuth2 token theft and CVE-2026-69264 data-URI RCE).

- **[CVE-2026-65600](https://github.com/advisories/GHSA-cxjq-mrr5-89rv)** — traefik (Go) · CVSS 9.1 · EPSS 0.004 · public PoC
  Auth bypass via path traversal in ReplacePathRegex — same class as CVE-2026-48020. Single request bypasses BasicAuth/ForwardAuth.
  → upgrade to v3.7.7 / v3.6.23 / v2.11.52. Traefik v1 (≤ 1.7.34): no fix (EOL).

- **[CVE-2026-73080](https://github.com/advisories/GHSA-87fv-vqqr-m4jr)** — seaweedfs (Go) · CVSS 9.3 · EPSS 0.004
  Unauth SSRF via VolumeServer gRPC — reads cloud metadata (169.254.169.254), leaks IAM creds. Default config is unauthenticated.
  → upgrade seaweedfs to ≥ 4.24; restrict gRPC to trusted hosts; enable mTLS via security.toml.

- **[CVE-2026-71319](https://github.com/advisories/GHSA-279x-mwfv-vcqv)** — @nuxt/devtools (npm) · CVSS 9.6 · EPSS 0.003 · public PoC
  Unauth RCE via HMR WebSocket — no token check before channel open. Reachable from LAN (`--host`) or any browser while dev server runs.
  → upgrade @nuxt/devtools to ≥ 3.3.1 (lockfile refresh / npm install).

- **[CVE-2026-71851](https://github.com/advisories/GHSA-rg76-677x-56q9)** — crypto-js (npm) · CVSS 9.0 · EPSS 0.003 · active exploitation (~$5M drained)
  CryptoJS.lib.WordArray.random() < 4.0.0 produces ~2^39 entropy. BIP39 seed recovery confirmed end-to-end (Coinspect Ill Bloom). Previously generated secrets remain exposed after upgrading.
  → upgrade crypto-js to ≥ 4.0.0; audit transitive deps for < 4.0.0 pins; rotate any secrets generated via the affected function.

---

**MONITOR**

- **[CVE-2026-55157](https://github.com/advisories/GHSA-49mq-fc6q-3h46)** — @ooples/token-optimizer-mcp (npm) · CVSS 8.4 · new 2026-08-14
  OS command injection in `smart_user` — username interpolated into shell; `$(...)` evaluated inside double quotes.
  → upgrade @ooples/token-optimizer-mcp to ≥ 5.1.0.

- **[CVE-2026-53657](https://github.com/advisories/GHSA-2j9v-p4xj-cjw2)** — lima-vm (Go) · CVSS 8.2 · EPSS 0.001 · new 2026-08-14
  Any QEMU VM user gains root in the VM via guest agent socket privilege escalation.
  → upgrade lima to ≥ 2.1.3.

- **[CVE-2026-35511](https://github.com/advisories/GHSA-29rf-f4vv-pvq6)** — authorizer (Go) · CVSS unscored · new 2026-08-14
  Zero-click account takeover via OAuth identity linking to unverified email accounts.
  → upgrade authorizer; enforce email verification in OAuth provider config.

---

**Summary:** No new CISA KEV entries since Aug 11 (all 4 this-week additions already covered). Sources: kev=ok, gh=ok, epss=ok. Notification staged at `.pending-notify/security-digest-2026-08-15.md`. Log appended to `memory/logs/2026-08-15.md`.
