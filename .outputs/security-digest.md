*Security Digest — 2026-08-31*
Verdict: 2 actively exploited (KEV), 5 to schedule this week, 1 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-81578](https://nvd.nist.gov/vuln/detail/CVE-2026-81578) — PaperCut NG/MF · KEV 2026-08-31 · CVSS n/a · EPSS 0.004
  Missing auth for critical functions → unauth remote config modification. Chain entry point for CVE-2026-82078. CISA-confirmed exploitation. Due 2026-09-14.
  → apply PaperCut NG/MF vendor patch today.

- [CVE-2026-82078](https://nvd.nist.gov/vuln/detail/CVE-2026-82078) — PaperCut NG/MF · KEV 2026-08-31 · CVSS n/a · EPSS 0.005
  Unsafe reflection → arbitrary Java bytecode execution under server security context. Chains with CVE-2026-81578. CISA-confirmed exploitation. Due 2026-09-14.
  → apply PaperCut NG/MF vendor patch today.

*PATCH THIS WEEK*
- [CVE-2026-54755](https://github.com/advisories/GHSA-cgc5-v3f2-8m2v) — klever-go (Go) · CVSS 9.6 · EPSS 0.004 · no PoC
  Integer overflow in split-royalty validation enables unbounded token minting.
  → upgrade github.com/klever-io/klever-go to ≥1.7.19.

- [CVE-2026-54754](https://github.com/advisories/GHSA-p7gw-2pcp-5pf8) — klever-go (Go) · CVSS 9.6 · EPSS 0.003 · no PoC
  Marketplace settlement mints KLV when referral + royalty % exceed cap.
  → upgrade github.com/klever-io/klever-go to ≥1.7.19.

- [CVE-2026-55485](https://github.com/advisories/GHSA-2gh4-jmwq-rr8w) — piccolo-admin (pip) · CVSS 8.8 · EPSS 0.004 · no PoC
  Admin → superuser privilege escalation via session manipulation.
  → upgrade piccolo-admin to ≥1.14.0.

- [CVE-2026-55638](https://github.com/advisories/GHSA-8gmq-j984-vp4r) — 9router (npm) · CVSS 8.6 · EPSS 0.006 · no PoC
  Unauthenticated LLM proxy access via /codex rewrite auth bypass. (Separate from Aug 30 GHSA-86m2-fcxq-5q7c Host-header issue.)
  → upgrade 9router to ≥0.5.2.

- [CVE-2026-55108](https://github.com/advisories/GHSA-fmgp-q6jx-gg3x) — kubevela (Go) · CVSS 8.5 · EPSS 0.006 · no PoC
  Terraform remote loader DoS via unbounded file read.
  → upgrade github.com/oam-dev/kubevela to ≥1.9.14.

*MONITOR*
- [CVE-2026-55784](https://github.com/advisories/GHSA-334q-h5g3-fpxv) — free5GC AUSF (Go) · CVSS 7.5 · no fix yet · EPSS 0.003
  Auth contexts overwritten by concurrent requests — session fixation pattern.
  → track GHSA-334q-h5g3-fpxv; avoid exposing AUSF to untrusted networks.
