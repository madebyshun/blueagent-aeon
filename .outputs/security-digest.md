*Security Digest — 2026-08-29*
Verdict: 3 actively exploited (KEV), 5 to schedule. _Sources: KEV +8 new this week, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-60004](https://nvd.nist.gov/vuln/detail/CVE-2026-60004) — Gitea · KEV 2026-08-25 *(due 2026-08-28, OVERDUE)* · EPSS 0.85 (99.7th) · CVSS 9.8
  Repo write access → plant malicious Git hook → RCE as Gitea service account via diffpatch API.
  → upgrade Gitea to ≥1.27.1 and audit existing hooks.

- [CVE-2021-23758](https://nvd.nist.gov/vuln/detail/CVE-2021-23758) — Ajax.NET Professional · KEV 2026-08-26 · EPSS 0.84 (99.7th) · CVSS 9.8
  .NET deserialization of untrusted data → unauthenticated RCE via arbitrary class instantiation; product likely EOL.
  → migrate off Ajax.NET Pro or network-isolate the host today.

- [CVE-2019-1068](https://nvd.nist.gov/vuln/detail/CVE-2019-1068) — Microsoft SQL Server · KEV 2026-08-26 *(due TODAY)* · EPSS 0.53 (98.9th) · CVSS 8.8
  Authenticated attacker executes arbitrary code as SQL Server service account.
  → apply MS SQL July 2019 patch (KB4505225 / CU equivalent) today.

*PATCH THIS WEEK*
- [CVE-2026-21962](https://nvd.nist.gov/vuln/detail/CVE-2026-21962) — Oracle HTTP Server / WebLogic Proxy · KEV 2026-08-24 *(due 2026-08-27, OVERDUE)* · EPSS 0.42 (98.6th) · CVSS 10.0
  Improper access control → unauthorized create/delete/modify of critical server data.
  → apply Oracle Critical Patch Update; escalate — already past federal due date.

- [CVE-2022-0995](https://nvd.nist.gov/vuln/detail/CVE-2022-0995) — Linux Kernel · KEV 2026-08-26 · EPSS 0.10 (95.2nd) · CVSS 7.8
  OOB write in watch_queue subsystem → local privilege escalation.
  → schedule kernel update; apply distro vendor security patch.

- [CVE-2015-3246](https://nvd.nist.gov/vuln/detail/CVE-2015-3246) — Red Hat Libuser · KEV 2026-08-26 · EPSS 0.09 (94.9th)
  Race condition → /etc/passwd corruption → DoS or privilege escalation.
  → yum update libuser on RHEL/CentOS systems.

- [CVE-2015-5287](https://nvd.nist.gov/vuln/detail/CVE-2015-5287) — Red Hat ABRT · KEV 2026-08-26 · EPSS 0.05 (91.6th)
  Symlink attack by local user with write permissions → privilege escalation; product may be EOL.
  → yum update abrt or disable ABRT service if unused.

- [CVE-2026-8452](https://nvd.nist.gov/vuln/detail/CVE-2026-8452) — Citrix NetScaler ADC / Gateway · KEV 2026-08-26 *(due TODAY)* · EPSS 0.02 (73.7th) · CVSS 9.8
  Memory buffer vulnerability → denial of service on exposed appliance.
  → apply Citrix Aug 2026 security bulletin update today.
