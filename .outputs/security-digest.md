*Security Digest — 2026-11-26*
Verdict: 3 actively exploited (KEV), 5 to schedule, 2 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-132165](https://nvd.nist.gov/vuln/detail/CVE-2026-132165) — Drupal Core · KEV 2026-11-24 · EPSS 0.11 · CVSS N/A
  Unauth RCE via install.php reinstall flaw. Highest EPSS of new KEV this week.
  → disable install.php; apply Drupal security update today.

- [CVE-2026-133323](https://nvd.nist.gov/vuln/detail/CVE-2026-133323) — Mitel MiCollab AWV · KEV 2026-11-25 · EPSS 0.056 · CVSS N/A
  Unauth OS cmd injection via AWV component. Part of 5-CVE Mitel cluster added today.
  → apply MiCollab vendor patch; isolate AWV from public internet.

- [CVE-2025-41450](https://nvd.nist.gov/vuln/detail/CVE-2025-41450) — Danfoss AK-SM 800A · KEV 2026-11-25 · EPSS 0.043 · CVSS N/A
  Improper auth exposes internal IPs, usernames, store names via web reports.
  → apply Danfoss firmware update; restrict management interface to trusted networks.

*PATCH THIS WEEK*
- [CVE-2023-25915](https://nvd.nist.gov/vuln/detail/CVE-2023-25915) — Danfoss AK-SM 800A · KEV 2026-11-25 · EPSS 0.025
  Remote cmd exec via XML interface input validation bypass.
  → schedule Danfoss AK-SM firmware update.

- [CVE-2026-134624](https://nvd.nist.gov/vuln/detail/CVE-2026-134624) — N-able MailAssure · KEV 2026-11-23 · EPSS 0.018
  Auth'd SSRF via LDAP sync; can reach internal hosts.
  → schedule MailAssure update; restrict LDAP sync API.

- [CVE-2026-103406](https://nvd.nist.gov/vuln/detail/CVE-2026-103406) — HPE Juniper Session Smart · KEV 2026-11-25 · EPSS 0.015
  OS cmd injection via crafted salt minion ID; runs as root.
  → schedule HPE Juniper Session Smart Router update.

- [CVE-2026-76466](https://nvd.nist.gov/vuln/detail/CVE-2026-76466) — Cisco Expressway · KEV 2026-11-20 · EPSS 0.011
  Hard-coded creds allow unauth root cmd execution on clustered nodes.
  → schedule Cisco Expressway security update.

- [CVE-2025-42884](https://nvd.nist.gov/vuln/detail/CVE-2025-42884) — SAP NetWeaver · KEV 2026-11-20 · EPSS 0.011
  JNDI injection via Enterprise Portal; unauth info disclosure/modification.
  → schedule SAP NetWeaver patch.

*MONITOR*
- [GHSA-vw2v-g4x7-xcqg](https://github.com/advisories/GHSA-vw2v-g4x7-xcqg) — fulgur (crates.io) · CVSS 7.5 · EPSS 0.007 · no patch
  Unbounded string-set accumulation → memory/CPU DoS.
  → track for patched release; audit string-set usage in prod.

- [GHSA-jp3c-6v3g-mpxv](https://github.com/advisories/GHSA-jp3c-6v3g-mpxv) — insomniacslk/dhcp (Go) · CVSS N/A · no patch
  Malformed IPv4 payload length → DoS.
  → track for patch; avoid exposing DHCP parsing to untrusted input.
