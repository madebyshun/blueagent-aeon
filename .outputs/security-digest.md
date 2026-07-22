*Security Digest — 2026-07-22*
Verdict: 3 patch today (FortiSandbox EPSS 0.84 active exploitation, Gitea Docker 9.8 PoC), 5 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-39808](https://nvd.nist.gov/vuln/detail/CVE-2026-39808) — Fortinet FortiSandbox · KEV 2026-07-16 · EPSS 0.84 · CVSS n/a
  Unauthenticated OS command injection via crafted HTTP — highest-EPSS item this week. Active exploitation confirmed per CISA.
  → patch FortiSandbox firmware immediately; restrict unauthenticated HTTP access.

- [CVE-2026-25089](https://nvd.nist.gov/vuln/detail/CVE-2026-25089) — Fortinet FortiSandbox · KEV 2026-07-16 · EPSS 0.36 · CVSS n/a
  Companion OS cmdinj CVE on the same attack surface. EPSS 0.36 — elevated active exploitation risk.
  → same patch covers both; verify firmware version after update.

- [CVE-2026-20896](https://github.com/advisories/GHSA-f75j-4cw6-rmx4) — Gitea Docker (Go) · CVSS 9.8 · EPSS 0.008 · public PoC
  Default REVERSE_PROXY_TRUSTED_PROXIES=* trusts X-WEBAUTH-USER from any IP — any attacker impersonates any user.
  → upgrade Gitea to ≥ 1.26.3, set explicit trusted-proxy IPs, redeploy.

*PATCH THIS WEEK*
- [CVE-2026-58644](https://nvd.nist.gov/vuln/detail/CVE-2026-58644) — Microsoft SharePoint · KEV 2026-07-16 · EPSS 0.015 · CVSS n/a
  Deserialization RCE over network. Actively exploited per CISA.
  → schedule MS SharePoint security update.

- [CVE-2026-46817](https://nvd.nist.gov/vuln/detail/CVE-2026-46817) — Oracle E-Business Suite · KEV 2026-07-15 · EPSS 0.010 · CVSS n/a
  Unauthenticated HTTP privilege escalation → full Oracle Payments module takeover.
  → apply Oracle Critical Patch Update for E-Business Suite.

- [CVE-2023-4346](https://nvd.nist.gov/vuln/detail/CVE-2023-4346) — KNX Protocol · KEV 2026-07-15 · EPSS 0.009 · CVSS n/a
  Lockout attack wipes devices and sets BCU keys when only Option 1 auth is enabled.
  → enable KNX security Option 2/3; update firmware.

- [GHSA-p63j-vcc4-9vmv](https://github.com/advisories/GHSA-p63j-vcc4-9vmv) — @vitest/browser (npm) · CVSS 9.4 · EPSS ~0 · no public PoC
  Browser Mode commands bypass allowWrite=false — arbitrary file read/write/delete at any path the Vitest process can access.
  → upgrade @vitest/browser to ≥ 3.2.7 (v3) / ≥ 4.1.10 (v4).

- [GHSA-2f96-g7mh-g2hx](https://github.com/advisories/GHSA-2f96-g7mh-g2hx) — GitPython (pip) · CVSS 8.8 · EPSS ~0
  Kwarg abbreviation bypasses the CVE-2026-42215 blocklist fix — RCE with attacker-controlled keyword args.
  → upgrade GitPython to ≥ 3.1.51.

*MONITOR*
- [GHSA-956x-8gvw-wg5v](https://github.com/advisories/GHSA-956x-8gvw-wg5v) — GitPython (pip) · CVSS 8.4 · no confirmed patch
  Command injection in Repo.archive(), ls_remote(), file overwrite via iter_commits()/blame(). Companion to above.
  → avoid untrusted input to affected methods; watch for GitPython ≥ 3.1.52.

- [GHSA-pf56-329r-95rw](https://github.com/advisories/GHSA-pf56-329r-95rw) — @sigstore/oci (npm) · CVSS 9.6 · EPSS 0.003 · fix: ≥ 0.7.1
  Credential confusion leaks private registry credentials to attacker-controlled registry.
  → upgrade @sigstore/oci to ≥ 0.7.1 in next dep update.

- [GHSA-hrxh-6v49-42gf](https://github.com/advisories/GHSA-hrxh-6v49-42gf) — gRPC-Go (go) · no CVE · no CVSS · patch pending
  xDS RBAC and HTTP/2 vulnerability cluster in google.golang.org/grpc. Details pending.
  → watch gRPC-Go release; update to latest stable once patch lands.
