Done. Here's the full output of the token-movers run:

---

**Token Movers — 2026-07-04**

*Market pulse:* ~70% of filtered top-100 alts green, median ~+2%; BTC +1.1% at $62.6K; broad gains across L1s with ANSEM and LAB dominating on trending-driven spikes.

**Top Winners (24h)**
1. ANSEM (The Black Bull) — $0.3572  +106.4% / 7d new / 1h +5.1%  •  $102M / #203  [TRENDING+UP][PUMP-RISK]
2. LAB (LAB) — $13.09  +80.2% / 7d −28.1% / 1h +17.6%  •  $89M / #27  [TRENDING+UP][FADE]
3. VELVET (Velvet) — $0.5679  +36.8% / 7d −58.3% / 1h −4.7%  •  $37.5M / #147  [FADE]
4. MAGMA (Magma Finance) — $0.6788  +27.6% / 7d +49.4% / 1h +3.3%  •  $24.6M / #224  [BREAKOUT]
5. BAS (BNB Attestation) — $0.04263  +18.8% / 7d +7.1% / 1h +1.4%  •  $34.5M / #256
6. ETHFI (Ether.fi) — $0.4085  +17.8% / 7d +15.4% / 1h +3.4%  •  $66.2M / #121
7. TAC (TAC) — $0.03566  +14.5% / 7d +59.2% / 1h −13.0%  •  $14.2M / #196
8. ULTIMA (Ultima) — $2331  +13.7% / 7d +23.0% / 1h +0.1%  •  $9.3M / #170
9. BONK (Bonk) — $0.000004950  +11.1% / 7d +17.9% / 1h +0.8%  •  $68.7M / #113
10. LIT (Lighter) — $2.220  +10.1% / 7d +24.8% / 1h −0.3%  •  $48.4M / #98  [TRENDING+UP]

**Top Losers (24h)**
1. SLX (Solstice) — $0.3676  −19.2% / 7d −21.1% / 1h +0.4%  •  $42.7M / #286  [CAPITULATION]
2. SYN (Synapse) — $0.4018  −18.7% / 7d +14.4% / 1h +0.5%  •  $49.0M / #288  [CAPITULATION]
3. RIF (RIF) — $0.1089  −15.1% / 7d +75.7% / 1h −0.8%  •  $17.6M / #250
4. B (BUILDon) — $0.2104  −14.3% / 7d −10.6% / 1h −0.8%  •  $7.4M / #164
5. VVV (Venice Token) — $12.24  −11.7% / 7d −8.2% / 1h +0.3%  •  $47.0M / #96
6. BP (Backpack) — $0.5620  −7.9% / 7d +3.4% / 1h +0.2%  •  $2.3M / #212
7. FARTCOIN (Fartcoin) — $0.1638  −6.9% / 7d +26.9% / 1h −0.1%  •  $30.2M / #192
8. JTO (Jito) — $0.7170  −6.5% / 7d −11.2% / 1h −0.6%  •  $41.8M / #126
9. MANA (Decentraland) — $0.07033  −5.9% / 7d +7.7% / 1h +0.4%  •  $27.2M / #215
10. APEPE (Ape and Pepe) — $0.000000925  −5.4% / 7d −9.2% / 1h −1.0%  •  $20.4M / #173

**Trending:** ANSEM, LAB, LIT, GRAM (prev. Toncoin), AERO, PENGU, HMSTR

**Notable signals:** ANSEM [TRENDING+UP][PUMP-RISK] +106% on $102M vol; LAB [TRENDING+UP][FADE] reversing yesterday's −20%; MAGMA [BREAKOUT] sustained +27.6%/7d+49.4%; SLX/SYN [CAPITULATION] on vol/mcap >0.45; LIT flip from loser to [TRENDING+UP].

## Summary

- Fetched top 250 markets (3 pages via WebFetch) + trending endpoint from CoinGecko
- Filtered stablecoins, illiquid tokens (<$1M vol), and institutional fund tokens
- Produced 10 winners, 10 losers, 7 trending with signal tags
- Notable: ANSEM/LAB dominate on trending+pump dynamics; two CAPITULATION signals (SLX, SYN); one BREAKOUT (MAGMA)
- Notification queued to `.pending-notify/` for post-run delivery
- Log appended to `memory/logs/2026-07-04.md`
