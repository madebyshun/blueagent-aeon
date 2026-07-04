*Security Digest — 2026-07-04*
Verdict: nothing urgent today. 4 to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH THIS WEEK*
- [CVE-2026-52735](https://github.com/advisories/GHSA-gf9r-m956-97qx) — zebrad/zebra-script (crates.io) · CVSS 9.3 · EPSS 0.00 · no public PoC
  Consensus divergence via P2SH sigop undercount in Rust opcode parser — malicious tx can fork a zebrad node off consensus. Three companion Zebra issues (mempool misbehavior, block suppression, address-book abort) fixed in same 4.5.0/7.0.0 release.
  → upgrade zebra-script to ≥7.0.0 and zebrad to ≥4.5.0.

- [GHSA-w4v6-g3wm-w36c](https://github.com/advisories/GHSA-w4v6-g3wm-w36c) — openclaw (npm) · CVSS 9.3 · EPSS N/A · no public PoC
  QQBot admin commands bypass DM-only restriction and allowFrom allowlist — any server member can execute admin-level commands.
  → upgrade openclaw to ≥2026.4.29.

- [CVE-2026-52792](https://github.com/advisories/GHSA-mm6c-5j6x-hq8m) — algernon (go) · CVSS 8.7 · EPSS 0.00 · no public PoC
  NTFS filename tricks on Windows expose Lua/Tengo server-side script source without auth.
  → upgrade github.com/xyproto/algernon to ≥1.17.9.

- [GHSA-322x-v876-g883](https://github.com/advisories/GHSA-322x-v876-g883) — @asymmetric-effort/nogginlessdom (npm) · CVSS 8.7 · EPSS N/A · no public PoC
  Path traversal in matchFileSnapshot allows arbitrary file write outside test working dir.
  → upgrade @asymmetric-effort/nogginlessdom to ≥0.0.22.
