Done. Here's what was executed:

## Summary

**Data fetched:** CoinGecko top-200 coins by market cap (pages 1–2) + trending endpoint. Both returned live data via curl.

**Filters applied:** Stablecoins, gold/silver pegs, money market funds, wrapped tokens, and coins with <$1M 24h volume excluded.

**Key findings:**

- **Market pulse:** Broad risk-off — only ~10/70 filtered top-cap coins green, median top-50 −4.0%. BTC −4.0% marking day 3 of drawdown.

- **Top winner:** STABLE (+8.4%), SEI (+7.7%), AAVE (+6.1%) [TRENDING+UP]

- **Top loser:** M (MemeCore) −72.0% [TRENDING+DOWN] — top trending coin in freefall, $33M volume confirms real selling (not a ghost market)

- **Notable signals:**
  - **CHZ** [CAPITULATION]: vol/mcap ratio 0.26 crossed the 0.25 threshold
  - **SYN** [PUMP-RISK]: rank #253, +40.8%, day 2 in trending — low-cap pump escalating
  - **EIGEN**: −9.5% with Jul 1 unlock now 6 days away — supply overhang arriving early
  - **XPL** [FADE]: anomalous $1.03B volume on $237M market cap (4.3× ratio)

**Files written:**
- `.pending-notify/token-movers.md` — queued for post-run delivery
- `memory/logs/2026-06-25.md` — token-movers entry appended

**Deduped:** BEAT, ADI, JUP, VELVET, DEXE (winners); WLD, PEPE, HYPE, QNT, ZEC (losers) — same direction as prior 2 days, no new tags.
