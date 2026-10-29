*Security Digest — 2026-10-29*
Verdict: 2 actively exploited (KEV), 5 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-46300](https://www.cve.org/CVERecord?id=CVE-2026-46300) — Linux Kernel · KEV added 2026-10-28 · EPSS 0.16 · CVSS n/a
  Missing var init in socket buffer coalescing; chained with 2 other CVEs to implant PHP webshells and run as root. Actively exploited.
  → apply kernel vendor patch immediately; triage hosts for signs of webshell implant.

- [CVE-2026-41709](https://www.cve.org/CVERecord?id=CVE-2026-41709) — Broadcom VMware ESX · KEV added 2026-10-28 · EPSS 0.008 · CVSS n/a
  Admin-level ops run without audit log entries — forensic blind spot under active exploitation.
  → apply VMware patch per CISA BOD 26-04; verify audit log integrity on affected hosts.

*PATCH THIS WEEK*
- [GHSA-mghf-wjfp-p5xm](https://github.com/advisories/GHSA-mghf-wjfp-p5xm) — wasmtime (crates.io) · CVSS 9.9 · EPSS 0.01 · no public PoC
  Cranelift aarch64 backend jumps to wrong target on large br_table — silent miscompilation, sandbox escape.
  → upgrade wasmtime to ≥36.0.19 / ≥48.0.7 / ≥49.0.4 per installed branch.

- [GHSA-84c9-qqpq-2pq5](https://github.com/advisories/GHSA-84c9-qqpq-2pq5) + [GHSA-pqh8-4pj7-32xx](https://github.com/advisories/GHSA-pqh8-4pj7-32xx) — obsidian-tc (npm) · CVSS 9.9/9.6 · EPSS 0.003/0.002
  Token auth bypass lets attacker read arbitrary vaults; DNS rebinding widens attack surface.
  → upgrade obsidian-tc to ≥1.3.1.

- [GHSA-v9pv-5gc8-w2m6](https://github.com/advisories/GHSA-v9pv-5gc8-w2m6) — Pillow (pip) · CVSS 9.8 · EPSS 0.007 · no public PoC
  Multi-frame loaders reuse stale native image storage after mode transitions — memory corruption, potential RCE.
  → upgrade Pillow to ≥13.0.0.

- [GHSA-h3rc-j82p-2c3h](https://github.com/advisories/GHSA-h3rc-j82p-2c3h) — vLLM (pip) · CVSS 8.1 · EPSS 0.007 · no public PoC
  Untrusted EPS input triggers Ghostscript RCE or DoS on inference servers.
  → upgrade vllm to ≥0.32.0 (also fixes GHSA-6757-hggm-hp2w SHM pickle forgery).

- [GHSA-3f7j-7jwc-fxfj](https://github.com/advisories/GHSA-3f7j-7jwc-fxfj) — systeminformation (npm) · CVSS 7.8 · EPSS 0.001
  Unicode quotation marks bypass Windows command-injection protections in services().
  → upgrade systeminformation to ≥5.33.16.

*MONITOR*
- [GHSA-f8c7-rwf9-fmgm](https://github.com/advisories/GHSA-f8c7-rwf9-fmgm) + [GHSA-rv4m-xm3f-3ccq](https://github.com/advisories/GHSA-rv4m-xm3f-3ccq) — mercury (pip) · CVSS 10.0/9.8 · no patch yet
  Unauthenticated RCE via /api/terminals and /api/kernels on notebook server. → watch for ≥3.2.4/3.2.6 release; block external access now.

- [GHSA-c8p4-j97h-3vg8](https://github.com/advisories/GHSA-c8p4-j97h-3vg8) — happy-dom (npm) · CVSS 8.6 · no patch yet · EPSS 0.004
  SSRF via iframe and link stylesheet when parsing untrusted HTML. → track issue; sanitize untrusted HTML before passing to happy-dom.

- [GHSA-6757-hggm-hp2w](https://github.com/advisories/GHSA-6757-hggm-hp2w) — vLLM (pip) · CVSS 7.5 · EPSS 0.005
  SHM handle forgery reaches pickle.loads() in worker. → resolved by vllm ≥0.32.0 (see PATCH THIS WEEK).
