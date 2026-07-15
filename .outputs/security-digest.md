*Security Digest — 2026-07-15*
Verdict: 3 actively exploited (KEV Jul 14), 5 to patch this week, 3 to monitor. _Sources: CISA KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-56164](https://nvd.nist.gov/vuln/detail/CVE-2026-56164) — SharePoint Server (Microsoft) · KEV 2026-07-14 · CVSS n/a
  Missing auth for critical function → unauthenticated network priv esc. Exploited per CISA.
  → apply MS SharePoint security update immediately.

- [CVE-2026-15409](https://nvd.nist.gov/vuln/detail/CVE-2026-15409) — SonicWall SMA1000 · KEV 2026-07-14 · CVSS n/a
  SSRF: unauthenticated attacker forces appliance to reach internal services.
  → upgrade SMA1000 firmware per SonicWall PSIRT.

- [CVE-2026-15410](https://nvd.nist.gov/vuln/detail/CVE-2026-15410) — SonicWall SMA1000 · KEV 2026-07-14 · CVSS n/a
  Code injection via admin panel; exploited in the wild.
  → same firmware update as CVE-2026-15409.

_Also KEV Jul 14: CVE-2026-56155 (MS ADFS local priv esc, authorized attacker) → apply Windows Update._

*PATCH THIS WEEK*
- [GHSA-j6r7-6fhx-77wx](https://github.com/advisories/GHSA-j6r7-6fhx-77wx) — n8n-mcp (npm) · CVE-2026-54052 · CVSS 9.9 · EPSS ~0
  Cross-tenant read of workflow version backups in multi-tenant HTTP deployments.
  → upgrade n8n-mcp to ≥2.56.1.

- [GHSA-xrcf-6jh3-ggvx](https://github.com/advisories/GHSA-xrcf-6jh3-ggvx) — anyquery (Go) · CVE-2026-50006 · CVSS 9.1 · EPSS ~0
  ATTACH DATABASE in server mode → arbitrary file write → RCE. Same pkg also: SSRF (CVE-2026-54628, CVSS 8.6) + LFR (CVE-2026-54629, CVSS 7.5).
  → upgrade anyquery to ≥0.4.5 (fixes all three); or disable server mode.

- [GHSA-q3fv-x8vg-qqm4](https://github.com/advisories/GHSA-q3fv-x8vg-qqm4) — trivy (Go) · CVE-2026-54448 · CVSS 8.7 · EPSS 0.25%
  Malformed Helm chart tar bomb → unbounded io.ReadAll → OOM crash. CI/CD scanners exposed.
  → upgrade trivy to ≥0.71.0.

- [GHSA-2p2f-px33-4vv5](https://github.com/advisories/GHSA-2p2f-px33-4vv5) — nebula-mesh (Go) · CVE-2026-53604 · CVSS 8.7 · EPSS ~0
  CA private key not zeroized on error paths. +3 companions: cert revocation bypass (CVE-2026-61699, CVSS 8.1), SSRF protection disable (CVSS 7.7), plaintext session tokens (CVE-2026-53603, CVSS 7.1).
  → upgrade nebula-mesh to ≥0.7.2 (fixes all four).

- [GHSA-qf34-295c-26v8](https://github.com/advisories/GHSA-qf34-295c-26v8) — woodpecker-ci (Go) · CVE-2026-61549 · CVSS 8.2 · EPSS ~0
  Unrestricted serviceAccountName in K8s backend → cluster privilege escalation.
  → upgrade woodpecker-ci to ≥3.16.0.

*MONITOR*
- [GHSA-9hc2-hjx8-q6pv](https://github.com/advisories/GHSA-9hc2-hjx8-q6pv) — tidgi (npm) · CVSS 9.6 · no patch
  TiddlyWiki auto-exec startup modules → unauthenticated RCE on untrusted repo import.
  → disable untrusted repo import; track release.

- [GHSA-mqxv-9rm6-w8qc](https://github.com/advisories/GHSA-mqxv-9rm6-w8qc) — ech0 (Go) · CVSS 8.7 · no patch
  Accept-Language _ separator → ~70× CPU amplification per request.
  → rate-limit in front; track release.

- [GHSA-pqg7-v6wh-3pfp](https://github.com/advisories/GHSA-pqg7-v6wh-3pfp) — tsdproxy (Go) · CVSS 8.5 · no patch
  Client X-Forwarded-For injection → IP spoofing in proxied backend requests.
  → strip/override XFF at ingress; track release.
