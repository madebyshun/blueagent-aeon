*Morning Brief — 2026-11-17*

*Focus today*
1. Diagnose systemic skill failures — API/gateway error hitting 7 skills since Nov 12
2. token-movers outage (5 days) — runs again 12:00 UTC; needs fix before then
3. deal-flow degraded (60% rate) — last success Oct 12; failed again yesterday

*Since yesterday*
- [stuck]: 7 core skills failing with same api_error pattern — token-movers, token-pick, defi-monitor, narrative-tracker, security-digest, github-trending, deal-flow
- [commit]: chore(cron): deal-flow failed — acknowledged, not yet fixed

*Running today*
- heartbeat @ 08:00, 14:00, 20:00 UTC
- github-monitor @ 09:00 UTC
- token-movers @ 12:00 UTC ⚠ (5 consecutive failures)
- token-pick @ 12:00 UTC ⚠ (4 consecutive failures)
- narrative-tracker @ 13:30 UTC ⚠ (4 consecutive failures)
