*Security Digest — 2026-10-03*
Verdict: 1 PoC-confirmed, 5 to schedule, 3 to monitor. No new KEV adds today. _Sources: KEV ok · GH Advisory ok · EPSS ok_

*PATCH TODAY*
- [CVE-2026-73802](https://github.com/advisories/GHSA-x4q3-gcj3-m6cf) — gitea-runner (Go) · CVSS 9.9 · EPSS N/A (new CVE)
  Workflow `container.options` passes `--pid=host --ipc=host --cap-add=ALL` to job containers even when privileged mode is disabled. PoC YAML in advisory — attacker workflow can nsenter to runner host as root.
  → disable container.options in runner config until gitea-runner ≥1.0.9-20260731 is tagged.

*PATCH THIS WEEK*
- [GHSA-jqmf-mx4f-hfr6](https://github.com/advisories/GHSA-jqmf-mx4f-hfr6) — vibe-trading-ai (pip) · CVSS 10.0 · no fix
  LLM-callable tools (run_command, execute_code) carry no sandbox — any reachable prompt can exec arbitrary commands on the server. → remove vibe-trading-ai; no patch yet.

- [GHSA-v2f8-6655-7grj](https://github.com/advisories/GHSA-v2f8-6655-7grj) — vibe-trading-ai (pip) · CVSS 10.0 · no fix
  FastAPI endpoints unauthenticated: file upload + arbitrary path read exposed publicly. → remove vibe-trading-ai; no patch yet.

- [CVE-2026-10032](https://github.com/advisories/GHSA-72qq-p3r5-f7wq) — @a2ui/web_core (npm) · CVSS 9.3 · EPSS 0.001 · no fix
  openUrl passes javascript: URIs through — XSS to RCE in Electron/webview contexts. → audit openUrl usage; reject javascript: scheme manually; no fix released.

- [GHSA-8mcx-5rqc-vhmf](https://github.com/advisories/GHSA-8mcx-5rqc-vhmf) — dulwich (pip) · CVSS 8.8 · no fix · +3 related GHSAs
  Arbitrary file write on Windows via unvalidated drive-letter path in checkout; 3 related symlink-traversal advisories in same batch. → assess dulwich usage; avoid Windows deploys; no fix yet.

- [CVE-2026-71416](https://github.com/advisories/GHSA-h46j-26q3-rggf) — headroom-ai (pip) · CVSS 8.8 · EPSS 0.002 · no fix
  Cross-Site WebSocket Hijacking — attacker origin issues authenticated WS commands. → remove headroom-ai; no patch available.

*MONITOR*
- [GHSA-x8gv-g2g3-65fj](https://github.com/advisories/GHSA-x8gv-g2g3-65fj) — siyuan/kernel (Go) · CVSS 8.2 · no fix yet
  SSRF via DNS-rebinding TOCTOU bypasses CheckHostSafe; 5 total siyuan advisories this batch. → watch for patch; avoid public exposure.

- [GHSA-gg6r-gp4c-89hp](https://github.com/advisories/GHSA-gg6r-gp4c-89hp) — trigger.dev (npm) · no CVSS · no fix yet · +4 related GHSAs
  Default V1 coordinator secret allows unauth Socket.IO; SQL injection + SSRF + run-replay injection in same batch. → watch patch release; don't expose coordinator publicly.

- [CVE-2026-92708](https://github.com/advisories/GHSA-j22f-vq7h-c4qm) — devalue (npm) · CVSS 7.5 · EPSS 0.007 · no fix yet
  stringify/uneval leaks cross-request shared memory in SSR contexts. → track devalue patch; audit SSR data paths.
