## Summary

**Token Movers — 2026-10-29** completed successfully.

**What I did:**
- Fetched top-250 market data and trending coins from CoinGecko via WebFetch (curl sandbox limitations required multiple offset fetches)
- Filtered stablecoins, gold-pegged tokens, and illiquid coins (< $1M 24h volume)
- Computed signal tags: [TRENDING+UP], [BREAKOUT], [CAPITULATION], [TRENDING+DOWN], [MAJOR]
- Queued notification to `.pending-notify/1793296357.md` for post-run delivery (sandbox blocked direct `./notify` execution)
- Logged results to `memory/logs/2026-10-29.md`

**Key signals today:**
- **HYPE** [TRENDING+UP][MAJOR] — +18.2% on $2.36B volume, 7d momentum intact. Dominant move of the day.
- **KNTQ** [BREAKOUT][TRENDING+UP] — +21.6% with 7d +33.2%, multi-day sustained run, small cap (#198)
- **Q (Quack AI)** [CAPITULATION] — -47.7% crash on $102M volume (57% of mcap), collapse in progress
- **PEPE** [TRENDING+UP] — +9.8% on $1.23B volume, meme rotation confirmed
- **PONS** [TRENDING+DOWN] — trending but down -5.7%, capitulation signal in a trending name
