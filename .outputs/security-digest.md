*Security Digest — 2026-08-30*
Verdict: 3 KEV (2 due today), 4 tracked-stack advisories to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
• [CVE-2023-49105](https://nvd.nist.gov/vuln/detail/CVE-2023-49105) — ownCloud · KEV 2026-08-27 · EPSS 0.432 · CVSS 9.8
  Auth bypass: access/modify/delete files with known username if signing-key missing. CISA due TODAY.
  → apply vendor mitigation or disable unauthenticated WebDAV access immediately.

• [CVE-2026-66384](https://nvd.nist.gov/vuln/detail/CVE-2026-66384) — JFrog Artifactory · KEV 2026-08-27 · EPSS 0.006 · CVSS 5.3
  Authenticated Docker cache path traversal — write outside intended dir under remote-repo conditions.
  → apply vendor mitigation; CISA due 2026-09-10.

• [CVE-2026-53362](https://nvd.nist.gov/vuln/detail/CVE-2026-53362) — Linux Kernel · KEV 2026-08-27 · EPSS 0.005 · CVSS 7.8
  IPv6 UDPv6 MSG_MORE fragmentation buffer overflow → local privilege escalation. CISA due TODAY.
  → update kernel; isolate IPv6-exposed hosts until patched.

*PATCH THIS WEEK*
• [CVE-2026-55247](https://github.com/advisories/GHSA-r82h-mqw3-fc56) — plone.app.event (pip) · CVSS 9.1 · EPSS 0.003
  Editor-level SSRF + DoS + stored XSS via malformed iCalendar import.
  → upgrade plone.app.event to ≥5.2.4 (Plone 6.x: ≥6.0.1).

• [CVE-2026-55248](https://github.com/advisories/GHSA-x5g3-w747-2h8q) — plone.app.portlets (pip) · CVSS 9.1 · EPSS 0.003
  DoS + XSS via RSS feed portlet; XSS in event URL field.
  → upgrade to ≥5.0.8 (6.x: ≥6.0.4; 7.x ≤7.0.1: no fix yet, monitor).

• [CVE-2026-55641](https://github.com/advisories/GHSA-86m2-fcxq-5q7c) — 9router (npm) · CVSS 8.2 · EPSS n/a
  Unauthenticated open-AI relay + SSRF via Host-header spoof (/v1); /codex auth bypass (CVE-2026-55638).
  → upgrade 9router to ≥0.5.2.

• [CVE-2026-55068](https://github.com/advisories/GHSA-x8mj-6p3q-g5pp) — free5GC (Go) · CVSS n/a (critical) · EPSS 0.004
  Unauthenticated NF profile poisoning — fake endpoints route 5G control-plane traffic to attacker.
  → upgrade github.com/free5gc/free5gc to ≥4.2.2.
