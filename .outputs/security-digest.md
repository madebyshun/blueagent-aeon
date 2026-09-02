*Security Digest — 2026-09-02*
Verdict: 3 actively exploited (KEV), 2 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-59822](https://github.com/advisories/GHSA-7488-6r32-c95q) — litellm (pip) · KEV 2026-09-02 · EPSS 0.005 · CVSS 8.8
  MCP endpoint auth bypass — fallback accepts any Bearer token, granting unauth MCP tool access. Exploited per CISA.
  → upgrade litellm to ≥1.84.0 and redeploy.

- [CVE-2026-48710](https://github.com/advisories/GHSA-86qp-5c8j-p5mr) — starlette (pip) · KEV 2026-09-02 · EPSS 0.021 · CVSS 6.5
  Missing Host header validation corrupts request.url.path, bypassing path-prefix auth middleware. Exploited per CISA.
  → upgrade starlette to ≥1.0.1 and redeploy.

- [CVE-2026-49869](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Kestra OSS · KEV 2026-09-02 · EPSS 0.010 · CVSS N/A · due 2026-09-05
  OS command injection — unauth attacker creates/executes arbitrary workflows. Exploited per CISA.
  → apply Kestra vendor patch or disable unauth workflow creation immediately; due Sep 5.

*PATCH THIS WEEK*
- [GHSA-p4cg-3328-rvfg](https://github.com/advisories/GHSA-p4cg-3328-rvfg) — orval (npm) · critical · EPSS 0.005 · CVSS unassigned · public PoC attached
  Import-time RCE via OpenAPI defaults injected into zod template literals on module import. Two variants (CVE-2026-72716 + CVE-2026-71866). PoC in advisory.
  → schedule upgrade: orval → ≥8.21.0

- [GHSA-2v6v-25fm-p4fg](https://github.com/advisories/GHSA-2v6v-25fm-p4fg) — SeaweedFS (go) · CVSS 9.8 · EPSS 0.004
  Unauth filer gRPC grants full S3 admin control without credentials.
  → schedule upgrade: build from commit ≥20260512; firewall gRPC filer port.

*MONITOR*
- [GHSA-m4rf-3fr8-xwx3](https://github.com/advisories/GHSA-m4rf-3fr8-xwx3) — nltk (pip) · CVSS 9.8 · EPSS 0.004 · no fix yet
  JVM arg injection via Stanford wrapper per-call options (incomplete prior fix, ≤3.10.2). → disable Stanford NLP plugin; watch for patch.

- [GHSA-vx52-2968-3vc6](https://github.com/advisories/GHSA-vx52-2968-3vc6) — pnpm (npm) · CVSS 7.4 · no fix
  Env secrets leaked via placeholder expansion in proxy settings from untrusted pnpm-workspace.yaml. → audit workspace.yaml proxy settings.

- [GHSA-vp52-pcj8-j9qc](https://github.com/advisories/GHSA-vp52-pcj8-j9qc) — grpc-go (go) · CVSS high · EPSS 0.004 · no fix
  HTTP/2 DATA fragmentation causes OOM heap exhaustion. → rate-limit HTTP/2 frame size at ingress; track upstream fix.
