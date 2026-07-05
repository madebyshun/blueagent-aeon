*Security Digest — 2026-07-05*
Verdict: nothing urgent today. 0 to schedule, 1 to monitor. _Sources: KEV, GH Advisory, EPSS_

*MONITOR*
- [CVE-2026-46599](https://github.com/advisories/GHSA-q675-qj96-32m9) — golang.org/x/image (Go) · CVSS 7.5 · EPSS 0.35% · fix: 0.41.0
  Excessive resource consumption via PackBits decompression in tiff package — DoS if parsing untrusted TIFF files.
  → upgrade golang.org/x/image to ≥0.41.0; go get golang.org/x/image@v0.41.0.
