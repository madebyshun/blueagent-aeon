*Security Digest — 2026-10-28*
Verdict: 3 actively exploited, 5 to schedule this week, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-111497](https://nvd.nist.gov/vuln/detail/CVE-2026-111497) — Google Brotli · KEV 2026-10-27 · EPSS 0.88 · CVSS n/a
  Crafted compressed stream → memory corruption, possible RCE. Confirmed exploitation per CISA.
  → update brotli in OS packages and container base images; redeploy.

- [CVE-2026-48356](https://github.com/advisories/GHSA-p3ch-8535-fp8j) — Adobe Commerce & Magento · KEV 2026-10-27 · EPSS 0.59 · CVSS 9.6
  Unrestricted file upload → RCE as current user. Confirmed exploitation per CISA.
  → apply Adobe Security Bulletin patch today.

- [GHSA-26p8-2jq9-3vq9](https://github.com/advisories/GHSA-26p8-2jq9-3vq9) — mlflow (pip) · CVSS 9.8 · EPSS 0.007 · public PoC
  Unauth RCE: upload artifact → trigger scorer import → arbitrary Python exec. Default server runs as root.
  → upgrade mlflow to ≥3.17.0 and redeploy.

*PATCH THIS WEEK*
- [GHSA-897f-g5gm-fmxm](https://github.com/advisories/GHSA-897f-g5gm-fmxm) — wasmtime (crates.io) · CVSS 9.9 · EPSS 0.005
  Numeric truncation + type confusion in Wasm host-call boundary. → upgrade wasmtime to ≥36.0.19 or ≥43.0.0.

- [GHSA-5x8w-8jj5-q52h](https://github.com/advisories/GHSA-5x8w-8jj5-q52h) — pillow (pip) · CVSS 9.2 · EPSS 0.007
  Heap buffer overflow in image decoder. → upgrade pillow to ≥13.0.0.

- [GHSA-rjh2-4xgw-p2hj](https://github.com/advisories/GHSA-rjh2-4xgw-p2hj) — atlantis (Go) · CVSS 8.8 · EPSS 0.005
  OS command injection in Terraform automation. → upgrade atlantis to ≥0.47.1.

- [GHSA-x94g-w73q-hpcw](https://github.com/advisories/GHSA-x94g-w73q-hpcw) — dd-trace (npm) · CVSS 8.7 · EPSS 0.004
  ReDoS via inefficient regex. → upgrade dd-trace to ≥5.131.1 (5.x) or ≥6.20.1 (6.x).

- [GHSA-mgqf-5mf5-prfj](https://github.com/advisories/GHSA-mgqf-5mf5-prfj) — filebrowser/backend (Go) · CVSS 8.6 · EPSS 0.005
  Path traversal + symlink following → arbitrary file access. → upgrade filebrowser/backend (post 2026-08-14 commit).

*MONITOR*
- [GHSA-mf2p-h6hf-fcwm](https://github.com/advisories/GHSA-mf2p-h6hf-fcwm) — tinymce (npm) · CVSS 8.5 · EPSS 0.003
  Stored XSS. → track; upgrade before next sprint.

- [GHSA-rh54-vffm-5fvp](https://github.com/advisories/GHSA-rh54-vffm-5fvp) — ckeditor5 (npm) · CVSS 8.1 · EPSS 0.005
  XSS in editor engine. → track; upgrade ckeditor5 when convenient.

- [GHSA-m65p-9j7q-6w33](https://github.com/advisories/GHSA-m65p-9j7q-6w33) — mlflow (pip) · CVSS 7.5 · EPSS 0.006
  Arbitrary file read via path traversal + false-tag bypass. Fixed by ≥3.17.0 (same as PATCH TODAY item).
