*Morning Brief — 2026-10-20*

*Focus today*
1. CVE-2026-96620 (claude-agent-sdk) — why now: patch unresolved since Oct 19; arg injection on live infra
2. 429 rate-limit cluster — why now: token-movers + token-pick run at 12 UTC; quota hit yesterday at 17:55 UTC
3. background: deal-flow success_rate=0.71 — below threshold; last succeeded Oct 12

*Since yesterday*
- token-movers: consecutive_failures now 2 (was 1); first-party 429 at 17:55 UTC
- token-pick: failed (consecutive_failures: 1); same 429 cluster
- github-trending: ok — 4 picks (ai-job-search, ruflo, Kronos, headroom)
- CVE-2026-96620: no resolution logged; still open

*Running today*
- heartbeat @ 08:00, 14:00, 20:00 UTC
- github-monitor @ 09:00 UTC
- token-movers @ 12:00 UTC
- token-pick @ 12:00 UTC
- narrative-tracker @ 13:30 UTC
