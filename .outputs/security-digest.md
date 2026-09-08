*Security Digest — 2026-09-08*
Verdict: nothing urgent today. 5 to schedule (nltk cluster), 0 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH THIS WEEK*
nltk (pip) — 5 CVEs fixed in v3.10.3, all affect ≤ 3.10.2. One upgrade covers all.

- [CVE-2026-79657](https://github.com/advisories/GHSA-x99w-6fgc-pmfw) · CVSS 9.3 · EPSS 1.2% · no PoC
  Pickle loader RCE via unsafe module-namespace trust — most severe.
  → upgrade nltk to ≥3.10.3.

- [CVE-2026-79676](https://github.com/advisories/GHSA-p4rw-rvv2-7xwr) · CVSS 8.2 · EPSS 0.31% · no PoC
  Corpus readers follow symlinks outside trusted roots — path traversal.
  → upgrade nltk to ≥3.10.3.

- [CVE-2026-78681](https://github.com/advisories/GHSA-97qj-x29f-37w7) · CVSS 8.7 · EPSS 0.29% · no PoC
  Entity-expansion DoS (billion laughs) via raw ElementTree parses.
  → upgrade nltk to ≥3.10.3.

- [CVE-2026-78682](https://github.com/advisories/GHSA-6ww7-3frv-cqxh) · CVSS 8.7 · EPSS 0.25% · no PoC
  pathsec SSRF bypass when a proxy is configured.
  → upgrade nltk to ≥3.10.3.

- [CVE-2026-79674](https://github.com/advisories/GHSA-3gq4-3j92-5w49) · CVSS 8.8 · EPSS 0.23% · no PoC
  Corpus Reader sandbox bypass — arbitrary corpus paths reachable.
  → upgrade nltk to ≥3.10.3.
