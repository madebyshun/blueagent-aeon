*Security Digest — 2026-10-27*
Verdict: 3 actively exploited, 5 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- CVE-2026-109618 — PHP 8.x · KEV added 2026-10-26 · EPSS 0.9999
  Memory corruption RCE, no auth required. Actively exploited per CISA.
  → upgrade PHP to ≥8.3.36 / ≥8.4.27 / ≥8.5.12 and restart servers today.

- CVE-2026-109619 — PHP 8.x · KEV added 2026-10-26 · EPSS 0.9999
  Stale request-state RCE, no auth required. Actively exploited per CISA.
  → same fix: upgrade PHP to ≥8.3.36 / ≥8.4.27 / ≥8.5.12.

- CVE-2026-110447 — Collabora Online Built-in CODE Server · KEV added 2026-10-23 · EPSS 0.116
  OS command injection when CODE server is stopped; allows RCE. Actively exploited per CISA.
  → apply Collabora Online update or disable built-in CODE server now.

*PATCH THIS WEEK*
- CVE-2026-114625 — Arista VeloCloud Orchestrator · KEV added 2026-10-23 · EPSS 0.010
  On-prem SQL injection reaches privileged internal functions. Confirmed in-the-wild.
  → schedule upgrade: apply Arista VeloCloud vendor patch.

- GHSA-m4w4-3r8h-jw98 — agno (pip) · CVSS 9.8 · EPSS 0.008
  Arbitrary code execution via eval() on user-controlled field_type in FunctionCall.
  → schedule upgrade: agno → ≥2.3.24.

- GHSA-6hp3-vr39-rqw8 — MONAI (pip) · CVSS 9.3
  Crafted DICOM input crashes server and silently corrupts inference output.
  → schedule upgrade: monai → ≥1.6.1.

- GHSA-6v38-4h7w-rj9h — authlib (pip) · CVSS 9.1 · EPSS 0.004
  Empty signature passes JWS JSON deserialization — auth bypass. Related: empty HMAC key forgery (CVE-2026-114616).
  → schedule upgrade: authlib → ≥1.9.1.

- GHSA-965c-763c-88jm — better-auth (npm) · CVSS 9.1 · EPSS 0.004
  OAuth state accepted as Magic Link token — unauthenticated sign-in as any user.
  → schedule upgrade: better-auth → ≥1.7.7.

*MONITOR*
- GHSA-h3rc-6mm3-gc2m — vLLM (pip) · CVSS 8.1
  User-controlled mm_processor_kwargs.code_revision allows RCE. Fix in 0.31.0.
  → track vllm; upgrade → ≥0.31.0.

- GHSA-f897-62hf-6gxq — @modelcontextprotocol/sdk (npm) · CVSS 7.5
  HTTP transports lack request body and JSON-RPC batch size limits — DoS. Fix in 1.30.1.
  → track; upgrade @modelcontextprotocol/sdk → ≥1.30.1.

- GHSA-mgcc-cww5-fp2q — go-jose (Go) · CVSS 7.5
  Panic parsing malformed RSA JWKs — DoS. No patched version confirmed.
  → watch go-jose/v3 and go-jose/v4 for patch; avoid exposing JWKS parsing to untrusted input.
