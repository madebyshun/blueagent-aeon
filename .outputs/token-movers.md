## Summary

Token-movers skill executed for 2026-09-17.

**What was done:**
- Fetched 250-coin market data from CoinGecko (curl → jq) + trending endpoint (WebFetch)
- Filtered stablecoins, wrapped dupes, and sub-$1M volume coins
- Computed top 10 winners / losers and market pulse

**Market picture:**
- Post-FOMC relief bounce — 87/100 top liquid coins green, median +1.9%
- Top winner: MCAT +174.9% (rank 92, no 7d history — new listing)
- Key signals: STONK [PUMP-RISK][TRENDING+UP] +40.9%, ZCAT [PUMP-RISK][BREAKOUT] +37.7%, DRV [TRENDING+UP][BREAKOUT] +23.9%
- ARGUS collapsed −39.5% after yesterday's +851% pump; ONE rank 769 +133.4% extreme PUMP-RISK
- Losers are shallow (worst: AKE −21.8%); confirms broad recovery

**Files modified:**
- `.pending-notify/token_movers_2026-09-17.md` — notification queued for post-run delivery by workflow
- `memory/logs/2026-09-17.md` — log entry appended
