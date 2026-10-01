*Security Digest — 2026-10-01*
Verdict: 1 confirmed PoC to patch today, 5 to schedule this week, 3 to monitor. _Sources: CISA KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-92937](https://github.com/advisories/GHSA-647f-g98j-qq25) — vm2 (npm) · CVSS 10.0 · EPSS 0.010 · PoC confirmed
  Bypass of prior fix (GHSA-m283-3h24-438v): call/apply indirection on Promise rejection handlers leaks host `process` → full RCE. Batch of 10 CVEs all fixed at 3.11.7.
  → upgrade vm2 to ≥3.11.7 and redeploy today.

*PATCH THIS WEEK*
- [GHSA-vcvr-r3jv-pc5j](https://github.com/advisories/GHSA-vcvr-r3jv-pc5j) — next (npm) · CVSS 9.5 · no PoC
  RCE via SVG injection in `next/og` ImageResponse (Node.js renderer path; Edge runtime unaffected).
  → upgrade next to ≥16.3.6.

- [GHSA-ffc3-869f-jxw9](https://github.com/advisories/GHSA-ffc3-869f-jxw9) — PyJWT (pip) · CVSS 9.1 · EPSS 0.002 · no PoC
  5-CVE batch: PEM whitespace bypass, BOM bypass, public-key-as-HMAC, empty HMAC acceptance, JWKS open redirect — auth bypass across all vectors.
  → upgrade PyJWT to ≥2.14.0.

- [GHSA-239g-whfq-7xj9](https://github.com/advisories/GHSA-239g-whfq-7xj9) — gitpython (pip) · CVSS 8.8 · EPSS 0.004 · no PoC
  Repo content can impersonate the `.git` directory → arbitrary command execution during repo operations.
  → upgrade gitpython to ≥3.1.60.

- [GHSA-hq2x-r82h-9wj4](https://github.com/advisories/GHSA-hq2x-r82h-9wj4) — electron (npm) · CVSS 8.2 · EPSS 0.001 · no PoC
  Popups opened from sandboxed documents lose inherited sandbox restrictions; second advisory GHSA-gr2m-v5gq-v685 covers same issue for windows from sandboxed context.
  → upgrade electron to ≥41.10.4 (or ≥42.5.2 / ≥43.0.0 on those branches).

- [GHSA-667r-xxjv-c9mm](https://github.com/advisories/GHSA-667r-xxjv-c9mm) — fastify (npm) · CVSS 8.1 · EPSS 0.004 · no PoC
  4-CVE batch: auth bypass via malformed URLs reaching protected routes, body replacement via async validators, header/boolean schema bypass.
  → upgrade fastify to ≥5.12.2.

*MONITOR*
- [GHSA-33jq-p8c2-q3q4](https://github.com/advisories/GHSA-33jq-p8c2-q3q4) — siyuan/kernel (Go) · CVSS 10.0 · EPSS 0.015
  Unauthenticated SQL injection in searchDocs (publish mode) → cross-notebook read/write via statement stacking. Fix only as a commit pseudo-version; no tagged release.
  → track GHSA-33jq-p8c2-q3q4; watch siyuan-note/siyuan for release.

- [GHSA-hrh2-vp3x-79xf](https://github.com/advisories/GHSA-hrh2-vp3x-79xf) — decompress (npm) · CVSS 9.1 · EPSS 0.008
  Path traversal via symlink chains allows extraction outside target dir. No patch for original `decompress` ≤4.2.1; only fork @xhmikosr/decompress ≥11.1.4 is fixed.
  → migrate to @xhmikosr/decompress ≥11.1.4; no patch for original package.

- [GHSA-ff3f-86qr-9cv3](https://github.com/advisories/GHSA-ff3f-86qr-9cv3) — @angular/router (npm) · CVSS ? · no PoC
  SSR Node adapter crashes on numeric URLs. No fix for ≤19.2.25; patched in ≥20.3.32, ≥21.2.24, ≥22.2.0.
  → block numeric-port URLs at edge if on Angular 19.x; upgrade if on 20/21/22 branch.
