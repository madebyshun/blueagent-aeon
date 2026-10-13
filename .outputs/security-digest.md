*Security Digest — 2026-10-13*
Verdict: 3 actively exploited (2 new KEV today), 5 high-severity to patch this week, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-104935](https://nvd.nist.gov/vuln/detail/CVE-2026-104935) — Ivanti Connect Secure · KEV 2026-10-13 · EPSS — · CVSS pending
  Auth bypass by spoofing → unauth RCE. BOD 26-04 due 2026-10-16.
  → apply Ivanti mitigations immediately; isolate from internet if patch unavailable.

- [CVE-2026-96951](https://nvd.nist.gov/vuln/detail/CVE-2026-96951) — Microsoft Windows Shell · KEV 2026-10-13 · EPSS — · CVSS pending
  Command injection via Windows Shell; security feature bypass over network.
  → apply October 2026 Windows patches via Windows Update / WSUS.

- [CVE-2021-3199](https://nvd.nist.gov/vuln/detail/CVE-2021-3199) — ONLYOFFICE Docs · KEV 2026-10-08 · EPSS 0.194 · CVSS —
  Path traversal via image upload → RCE; chainable with CVE-2023-22621.
  → upgrade ONLYOFFICE Docs to ≥5.6.3.

*PATCH THIS WEEK*
- [GHSA-2xv2-w8cq-5gxw](https://github.com/advisories/GHSA-2xv2-w8cq-5gxw) (CVE-2026-61447) — praisonaiagents (pip) · CVSS 10.0 · EPSS 0.025 · PoC included
  CodeAgent runs LLM-generated Python without sandbox; leaks all env vars incl. API keys.
  → upgrade praisonaiagents to ≥1.6.78.

- [GHSA-9mp3-24cc-77mg](https://github.com/advisories/GHSA-9mp3-24cc-77mg) (CVE-2026-61445) — praisonai (pip) · CVSS 9.9 · EPSS 0.009 · no public PoC
  AICoder write_to_file/execute_command tools: no path or command validation; Docker runs as root.
  → upgrade praisonai to ≥4.6.78.

- [GHSA-8qpj-27x8-pwpq](https://github.com/advisories/GHSA-8qpj-27x8-pwpq) (CVE-2026-10561) — langflow (pip) · CVSS 9.9 · EPSS 0.008 · PoC included
  PythonREPLComponent: unsandboxed execution; auth users get host RCE + DB superuser escalation.
  → upgrade langflow to ≥1.10.1 (≥1.12.3 for full hardening).

- [GHSA-8r5x-fm3f-whwj](https://github.com/advisories/GHSA-8r5x-fm3f-whwj) (CVE-2026-106446) — handlebars (npm) · CVSS 9.8 · EPSS 0.006 · PoC + curl exploit
  AST type confusion bypasses 4.7.9 patch; JS injection → RCE on template render.
  → upgrade handlebars to ≥4.7.10.

- [GHSA-g2v8-7jhw-pp8p](https://github.com/advisories/GHSA-g2v8-7jhw-pp8p) (CVE-2026-106501) — @backstage/plugin-scaffolder-backend (npm) · CVSS 9.6 · EPSS 0.005 · no PoC
  Auth users can read task execution data including external service credentials.
  → upgrade to ≥3.3.1 / ≥3.4.1 / ≥4.1.0 per branch.

*MONITOR*
- [GHSA-r488-j9vj-wx3q](https://github.com/advisories/GHSA-r488-j9vj-wx3q) (CVE-2026-105857) — @payloadcms/plugin-form-builder (npm) · CVSS 10.0 · EPSS 0.004
  Payload Form Builder RCE issue; patch status unclear. → watch upstream for fix.

- [GHSA-33rr-wq23-g6gg](https://github.com/advisories/GHSA-33rr-wq23-g6gg) (CVE-2026-107809) — Nginx-UI (Go) · CVSS 8.8 · EPSS 0.003
  AuthRequired cookie fallback enables CSRF on management APIs. → restrict to trusted networks.

- [GHSA-pwhx-cvv3-qj5c](https://github.com/advisories/GHSA-pwhx-cvv3-qj5c) (CVE-2026-108259) — @tinacms/cli (npm) · CVSS 8.2 · EPSS 0.004
  Code injection via unescaped Git branch name in generated client source. → watch GHSA-pwhx-cvv3-qj5c.
