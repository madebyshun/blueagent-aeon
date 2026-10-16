*Security Digest — 2026-10-16*
Verdict: nothing urgent today. 5 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH THIS WEEK*
- [CVE-2026-94603](https://github.com/advisories/GHSA-2cvf-wqm6-wr9g) — Podman (go) · CVSS 10.0 · EPSS 0.92% · no PoC
  Image annotation disables almost all container sandboxing. → upgrade podman to ≥5.8.8 (v5) or ≥6.1.3 (v6).

- [CVE-2026-104252](https://github.com/advisories/GHSA-v75v-6fpf-gvw8) — Vitess vttablet (go) · CVSS 9.8 · EPSS 0.89% · no PoC
  Reflected XSS in /twopcz endpoint. → upgrade vitess.io/vitess to ≥0.23.5 or ≥0.24.2.

- [CVE-2026-77459](https://github.com/advisories/GHSA-fmxq-cgp8-87wp) — Argo CD (go) · CVSS 9.9 · EPSS 0.72% · no PoC
  AppProject namespace/resource restrictions bypassed via PostDelete hooks. → upgrade argo-cd v3 to ≥3.3.15 / ≥3.4.10 / ≥3.5.4; v2 unpatched.

- [CVE-2026-77524](https://github.com/advisories/GHSA-637c-6jxx-4rwm) — KEDA (go) · CVSS 9.9 · EPSS 0.64% · no PoC
  Namespace admin escalates to cluster admin via TriggerAuthentication. → upgrade keda/v2 to ≥2.21.0.

- [CVE-2026-102989](https://github.com/advisories/GHSA-qx66-fv34-fjm8) — TanStack Start (npm) · CVSS 9.3 · EPSS 0.52% · no PoC
  Unauthenticated reflected XSS in server-function responses. → upgrade @tanstack/react-start ≥1.168.60 (solid ≥1.168.57, vue ≥1.168.56).

*MONITOR*
- [CVE-2026-102748](https://github.com/advisories/GHSA-qj98-gp63-54xj) — Dgraph v25 (go) · CVSS n/a · EPSS 0.49% · no fix yet
  Unauth HTTP admin removeNode → DoS. → track GHSA-qj98-gp63-54xj; block admin port at network layer.

- [CVE-2026-86063](https://github.com/advisories/GHSA-pq7j-f95f-qfcv) — @anthropic-ai/claude-code (npm) · CVSS n/a · EPSS 0.17% · fix: ≥2.1.179
  Plugin hash pin bypass — plugins load without hash verification. → upgrade claude-code if used as dependency.

- [CVE-2026-103929](https://github.com/advisories/GHSA-g74g-rg72-j2p3) — mise (rust) · CVSS 7.8 · EPSS 0.20% · patch unclear
  Untrusted local config overrides shell args. → avoid untrusted .mise.toml; watch for confirmed patch.
