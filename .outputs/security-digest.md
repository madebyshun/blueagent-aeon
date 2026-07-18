The security-digest skill is complete. Here's a summary:

## Summary

**What was done:**

1. **CISA KEV** — Fetched via WebFetch. No new KEV additions since Jul 17's digest (last batch was Jul 16: FortiSandbox × 2 + SharePoint, all covered yesterday). 12 total additions this week.

2. **GitHub Advisories (last 48h)** — Pulled critical + high via `gh api`. Filtered to tracked stack (npm, pip, Go, crates.io). Deduped against Jul 16 + Jul 17 logs (excluded 6 IDs already reported).

3. **EPSS enrichment** — 5 of 10 CVEs had data; all 2026 CVEs too new, treated as 0. Gitea (CVE-2026-27771) highest at **EPSS 0.407** — near PATCH TODAY threshold.

4. **Digest tiered and sent** via `.pending-notify/` (sandbox post-run delivery):

   - **PATCH TODAY:** empty (no new KEV, no EPSS ≥ 0.5)
   - **PATCH THIS WEEK (5):** Gitea ≥1.26.2 · meta-ads-mcp ≥1.0.115 (public PoC) · skipper ≥0.27.26 (public PoC) · @prompty/core ≥2.0.0-beta.3 · prompty ≥2.0.0b2 (multi-ecosystem)
   - **MONITOR (3):** sh (no patch) · vllm ReDoS (no patch) · meta-ads-mcp auth bypass (no patch)

5. **Logged** to `memory/logs/2026-07-18.md` with tier counts, IDs, and source status.

**Notable:** Prompty carries two separate CVEs (code exec + file read) both patched in recent betas — directly relevant to the AI agent toolchain tracked in memory.
