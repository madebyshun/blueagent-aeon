*Security Digest — 2026-06-25*
Verdict: 2 with public PoC, 3 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-52813](https://github.com/advisories/GHSA-c39w-43gm-34h5) — Gogs (Go) · CVSS 10.0 · EPSS 0.011 · public PoC
  Unauthenticated RCE: org-name path traversal overwrites Git hooks. Exploit gist linked in advisory.
  → upgrade gogs.io/gogs to ≥0.14.3 now.

- [CVE-2026-52806](https://github.com/advisories/GHSA-qf6p-p7ww-cwr9) — Gogs (Go) · CVSS 9.9 · EPSS 0.010 · public PoC (Python exploit)
  Authenticated RCE via branch-name injection into git rebase --exec at PR merge. Any user with repo write.
  → upgrade gogs.io/gogs to ≥0.14.3 now.

*PATCH THIS WEEK*
- [CVE-2026-55441](https://github.com/advisories/GHSA-77g9-363w-rccq) — mise (crates.io) · CVSS 8.6 · EPSS ~0
  Arbitrary command execution via untrusted task-include files without trust checks.
  → upgrade mise to ≥2026.6.4.

- [CVE-2026-48126](https://github.com/advisories/GHSA-jc3j-x6pg-4hmv) — algernon (Go) · CVSS 8.2 · EPSS 0.003
  Host header path traversal enables arbitrary file read + Lua code execution in domain mode.
  → upgrade algernon to ≥1.17.8.

- [CVE-2026-52811](https://github.com/advisories/GHSA-89mr-xqfv-758m) — Gogs (Go) · CVSS — · EPSS 0.005
  Symlink escape in UploadRepoFiles writes arbitrary files outside repo working tree.
  → upgrade gogs.io/gogs to ≥0.14.3 (same Gogs cluster as above).

*MONITOR*
- [CVE-2026-48708](https://github.com/advisories/GHSA-7fq5-7wr8-rjwj) — OliveTin (Go) · CVSS 7.5 · EPSS 0.004
  Template parsing race condition causes cross-request command contamination.
  → track GHSA-7fq5-7wr8-rjwj; fix available (commit d74da93), pending stable release.

- [CVE-2026-54134](https://github.com/advisories/GHSA-j4h9-pm27-4rfw) — OctoPrint (pip) · CVSS — · EPSS ~0
  File exfiltration via query parameter injection in upload endpoints.
  → upgrade OctoPrint to ≥1.11.8.

- [CVE-2026-52812](https://github.com/advisories/GHSA-6p9m-q3jp-47h4) — Gogs (Go) · CVSS — · EPSS 0.002
  LFS OID binding leaks private repository content across tenants.
  → upgrade gogs.io/gogs to ≥0.14.3 (Gogs cluster).
