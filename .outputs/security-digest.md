Cleanup blocked — not critical. The notification is queued in `.pending-notify/` for post-run delivery and the log is written.

---

## Summary

**security-digest run complete** — 2026-11-24.

**Sources:** CISA KEV (14 entries this week), GitHub Advisories (critical + high, 48h), EPSS (api.first.org) — all OK.

**PATCH TODAY (3)**
- **CVE-2026-40217** — BerriAI LiteLLM (pip) · KEV · EPSS 0.83 — RCE via /guardrails/test_custom_code, no auth required. **In-stack.** → `pip install --upgrade litellm`
- **CVE-2026-133968** — Project MONAI Label · KEV · EPSS 0.50 — path traversal → RCE, unauthenticated
- **CVE-2026-129448** — Apache Roller · KEV · EPSS 0.40 — XML-RPC deserialization before auth, unauthenticated RCE

**PATCH THIS WEEK (5)**
- **CVE-2026-59726 / GHSA-c4hm-4h84-2cf3** — ruflo (npm) · CVSS 10.0 · EPSS 0.06 — MCP bridge unauthenticated RCE in Docker defaults. **In-stack.** → `≥3.16.3`
- **CVE-2026-64855 / GHSA-859w-52fx-hcm6** — soapbar (pip) · CVSS 8.2 — signature forgery via embedded cert trust. **In-stack.** → `≥0.13.0`
- CVE-2026-90817 — REDCap · KEV · EPSS 0.34 — code injection
- CVE-2026-115731 — Puppet Enterprise · KEV · EPSS 0.13 — deserialization RCE
- CVE-2026-123890 — VMware vCenter · KEV · EPSS 0.04 — auth bypass

**MONITOR:** empty — all in-stack findings have patches.

Notification queued to `.pending-notify/1764835200.md` for post-run delivery. Log written to `memory/logs/2026-11-24.md`.
