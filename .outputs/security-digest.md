Done. Here's the full digest output:

---

**Security Digest — 2026-08-09**
Verdict: 3 actively exploited, 4 in tracked stack to schedule, 3 to monitor. *Sources: KEV, GH Advisory, EPSS*

**PATCH TODAY**
- **CVE-2026-8037** — Progress LoadMaster · KEV 2026-08-07 · EPSS 0.99 · CISA due 2026-08-10
  Command injection via unsanitized admin endpoints — unauthenticated arbitrary OS command execution.
  → apply vendor patch; take internet-facing LoadMaster offline until patched.

- **CVE-2026-34486** — Apache Tomcat · KEV 2026-08-04 · EPSS 0.81
  Missing encryption bypasses EncryptInterceptor; chains with CVE-2025-24813 for full exploitation.
  → upgrade Tomcat per vendor advisory; verify EncryptInterceptor config today.

- **CVE-2026-9198** — Langflow (pip) · KEV 2026-08-04 · EPSS 0.17
  Code injection on default deployments — unauthenticated RCE with no prerequisites.
  → upgrade Langflow immediately; restrict admin API to loopback if upgrade delayed.

**PATCH THIS WEEK**
- **CVE-2026-18556 + CVE-2026-18577** — N-able N-central · KEV (both) · EPSS 0.04 — auth bypass pair, both confirmed exploited, CISA due dates passed → schedule upgrade this week.
- **CVE-2026-63077** — JetBrains TeamCity · KEV 2026-08-05 · EPSS 0.01 · CISA due 2026-08-08 (overdue) — deserialization RCE via agent polling → upgrade TeamCity; block agent polling port externally.
- **GHSA-rg76-677x-56q9** (CVE-2026-71851) — crypto-js (npm) < 4.0.0 · CVSS 9.0 · EPSS 0.003 — insufficient entropy in secret generation → upgrade crypto-js to ≥4.0.0.
- **GitPython (pip) ≤ 3.1.57** · CVSS 8.8 — 4 advisories (2026-08-07): git option injection, sshCommand RCE, .gitmodules injection, read-tree file overwrite → upgrade GitPython to ≥3.1.58.

**MONITOR**
- **GHSA-wcx4-wpfv-mc5c** — jsii-diff (npm) < 1.131.0 · CVSS 7.8 — command injection → upgrade to ≥1.131.0.
- **GHSA-hc8v-wwc9-vgxm** — go-git (Go) ≤ 5.19.1 · CVSS 7.1 — symlink following → upgrade to ≥5.19.2.
- **GHSA-gm37-52c6-37mw** — pymdown-extensions (pip) ≤ 11.0.0 · CVSS 7.5 — ReDoS → upgrade to ≥11.0.1.

---

## Summary

- **KEV**: 6 new entries this week; top 3 selected for PATCH TODAY by EPSS (LoadMaster 0.99, Tomcat 0.81, Langflow 0.17)
- **Tracked stack hits**: crypto-js (npm), GitPython cluster ×4 (pip), jsii-diff (npm), go-git (Go), pymdown-extensions (pip)
- **GitPython notable**: 4 separate RCE/file-overwrite advisories published same day (2026-08-07), all resolved by upgrading to 3.1.58
- **Sources**: kev=ok, gh=ok, epss=ok (all via WebFetch — sandbox blocked curl)
- **Notification**: staged to `.pending-notify/security-digest-2026-08-09.md`
- **Log**: appended to `memory/logs/2026-08-09.md`
