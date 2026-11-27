*Security Digest — 2026-11-27*
Verdict: 3 actively exploited, 5 to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-133968](https://nvd.nist.gov/vuln/detail/CVE-2026-133968) — MONAI Label (pip) · KEV 2026-11-23 · EPSS 0.272 · CVSS est. 9.x
  Unauthenticated path traversal → arbitrary file write outside datastore dir → RCE.
  → upgrade monailabel to latest patched release; block public internet access to server.

- [CVE-2026-129448](https://nvd.nist.gov/vuln/detail/CVE-2026-129448) — Apache Roller (Java) · KEV 2026-11-20 · EPSS 0.242 · CVSS est. 9.x
  XML-RPC endpoint deserializes vendor extension types before auth → unauthenticated RCE.
  → upgrade Apache Roller; disable XML-RPC endpoint if unused.

- [CVE-2026-123890](https://nvd.nist.gov/vuln/detail/CVE-2026-123890) — VMware vCenter (Broadcom) · KEV 2026-11-20 · EPSS 0.050 · CVSS est. 9.x
  VMware Directory Service auth bypass → unauthorized vCenter access.
  → apply Broadcom patch; restrict vCenter mgmt interface to management VLAN.

*PATCH THIS WEEK*
- [CVE-2026-120705](https://nvd.nist.gov/vuln/detail/CVE-2026-120705) — OSGeo GeoServer · KEV 2026-11-27 · EPSS N/A (new) · CVSS est. 9.x
  Unauth XML injection via WFS GetFeatureById → SSRF + local file read; chainable to RCE.
  → upgrade GeoServer; restrict WFS endpoint access.

- [CVE-2026-129243](https://nvd.nist.gov/vuln/detail/CVE-2026-129243) — OSGeo GeoServer · KEV 2026-11-27 · EPSS N/A (new) · CVSS est. 9.x
  Unauth service-role bypass via prefixed parameter → chainable to RCE.
  → upgrade GeoServer (same patch as CVE-2026-120705).

- [CVE-2026-136716](https://nvd.nist.gov/vuln/detail/CVE-2026-136716) — Drupal Core · KEV 2026-11-27 · EPSS 0.012 · CVSS est. 9.x
  Incomplete install state → installer accessible → unauthenticated site takeover.
  → block install.php; apply Drupal security update.

- [CVE-2023-25914](https://nvd.nist.gov/vuln/detail/CVE-2023-25914) — Danfoss AK-SM 800A · KEV 2026-11-25 · EPSS 0.018 · CVSS est. 8.x
  Path traversal via XML interface → arbitrary server file read.
  → apply Danfoss firmware update; isolate device from public network.

- [CVE-2026-133303](https://nvd.nist.gov/vuln/detail/CVE-2026-133303) — Mitel MiCollab AWV · KEV 2026-11-25 · EPSS 0.013 · CVSS est. 9.x
  Unauth OS command injection via pre-staged content in AWV component.
  → upgrade MiCollab; block AWV component from public internet.
