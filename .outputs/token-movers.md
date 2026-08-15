Files will remain but won't affect the run. The skill is complete.

---

## Summary

**What was done:**
- Fetched top 250 coins from CoinGecko markets API and trending endpoint via curl
- Filtered stablecoins and illiquid tokens (vol < $1M), computed winners/losers with jq
- Applied signal enrichment tags per skill rules
- Checked last 2 days of logs to dedup repeated movers (skipped ETHFI, BTW, CASHCAT)

**Key findings — 2026-08-15:**
- **Pulse:** Mild alt rotation, 54% of top-100 alts green, BTC flat at +0.3%
- **Top winner:** CYS (Cysic) +41.2% [BREAKOUT] — strongest confirmed multi-timeframe move
- **Notable risk:** COW +72.8% trending but absent from top-250 markets data (unverifiable volume) [PUMP-RISK]; ANSEM +34.6% trending AND in winners [PUMP-RISK][TRENDING+UP]
- **Capitulation:** BEAT −27.6% / 7d −81.5% [CAPITULATION] — gets its new tag today after being deduped prior days
- **AKE pump fading:** +107.3% Aug 14 → +13.6% today — energy exhaustion, watch for reversal

**Files modified:**
- `memory/logs/2026-08-15.md` — appended token-movers log entry
- `.pending-notify/token-movers-2026-08-15.md` — notification staged for post-run delivery (sandbox limitation)
