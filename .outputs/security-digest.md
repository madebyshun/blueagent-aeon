*Security Digest — 2026-06-11*
Verdict: nothing urgent today. 3 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH THIS WEEK*
- CVE-2026-48039 (GHSA-9gw6-46qc-99vr) — meta-ads-mcp (pip) · CVSS 9.1 · EPSS 0 · public PoC
  Unauth POST to /mcp leaks operator Meta Access Token; full Meta Ads API takeover possible.
  -> upgrade meta-ads-mcp to >=1.0.109.

- CVE-2026-48054 (GHSA-4x76-22x2-rx8v) — @openzeppelin/wizard (npm) · CVSS 8.8 · EPSS 0 · no public PoC
  Code injection in generated Hardhat/Foundry tests via unsanitized opts.name/opts.uri; arbitrary code on npm test.
  -> upgrade @openzeppelin/wizard to >=0.10.9.

- CVE-2026-48060 (GHSA-542p-wvx7-72m4) — litestar (pip) · CVSS 8.1 · EPSS 0 · public PoC
  HTML injection via poisoned CSRF cookie escalates to XSS; credential theft and phishing possible.
  -> upgrade litestar to >=2.22.0.

*MONITOR*
- CVE-2026-48020 (GHSA-xf64-8mw2-4gr2) — traefik v2+v3 (Go) · high · no CVSS · EPSS 0
  StripPrefix auth bypass via path normalization skips middleware on protected routes; no patch yet.
  -> track GHSA-xf64-8mw2-4gr2; avoid StripPrefix on auth-critical routes until patched.

- CVE-2026-48068/48069 (GHSA-5375-pq7m-f5r2 + GHSA-99f4-grh7-6pcq) — @grpc/grpc-js (npm) · CVSS 7.5 · EPSS 0
  Two crash-on-receipt bugs: malformed request kills servers; compressed message kills clients. No patch yet.
  -> track both GHSAs.

- CVE-2026-47781 (GHSA-qq6c-99pv-prvf) — pdm (pip) · high · no CVSS · EPSS 0
  Project-controlled .pdm-plugins executes before CLI arg parsing; malicious repo clones run code on install.
  -> track GHSA-qq6c-99pv-prvf; audit untrusted pdm projects; no patch yet.
