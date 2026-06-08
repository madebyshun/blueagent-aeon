import json, sys

with open('.cg_markets.json') as f:
    data = json.load(f)

with open('.cg_trending_raw.json') as f:
    trending_raw = json.load(f)

trending_symbols = set()
for item in trending_raw.get('coins', []):
    sym = item.get('item', {}).get('symbol', '').upper()
    if sym:
        trending_symbols.add(sym)

print("CoinGecko trending symbols:", trending_symbols)

# Load dex trending
try:
    with open('.dex_trending.json') as f:
        dex_data = json.load(f)
    dex_symbols = set()
    for pair in dex_data.get('pairs', [])[:30]:
        sym = pair.get('baseToken', {}).get('symbol', '').upper()
        if sym:
            dex_symbols.add(sym)
    print("DexScreener symbols (sample):", list(dex_symbols)[:20])
except Exception as e:
    dex_symbols = set()
    print("DexScreener parse error:", e)

# BTC/ETH benchmark
btc_7d = None
eth_7d = None
for c in data:
    if c['symbol'].upper() == 'BTC':
        btc_7d = c.get('price_change_percentage_7d_in_currency', 0) or 0
        btc_24h = c.get('price_change_percentage_24h', 0) or 0
    if c['symbol'].upper() == 'ETH':
        eth_7d = c.get('price_change_percentage_7d_in_currency', 0) or 0
        eth_24h = c.get('price_change_percentage_24h', 0) or 0

print(f"BTC 24h={btc_24h:+.1f}% 7d={btc_7d:+.1f}%")
print(f"ETH 24h={eth_24h:+.1f}% 7d={eth_7d:+.1f}%")

DEDUP_BLOCKED = {'LAB', 'NEAR', 'WLD', 'ALLO', 'ENA'}

candidates = []
for c in data:
    sym = c['symbol'].upper()
    if sym in DEDUP_BLOCKED:
        continue
    mcap = c.get('market_cap', 0) or 0
    if mcap < 20_000_000:
        continue
    vol = c.get('total_volume', 0) or 0
    p24 = c.get('price_change_percentage_24h', 0) or 0
    p7d = c.get('price_change_percentage_7d_in_currency', 0) or 0
    ratio = vol / mcap if mcap > 0 else 0
    rank = c.get('market_cap_rank', 999)
    price = c.get('current_price', 0)

    score = 0
    breakdown = []

    if p24 > 0:
        score += 1
        breakdown.append('24h+1')
    if p7d > 0:
        score += 1
        breakdown.append('7d+1')
    if p24 > 5 and p7d > 5:
        score += 2
        breakdown.append('both>5%+2')
    if sym in trending_symbols:
        score += 2
        breakdown.append('trending+2')
    if ratio >= 0.20:
        score += 3
        breakdown.append('vol/mcap>=0.20+3')
    elif ratio >= 0.10:
        score += 2
        breakdown.append('vol/mcap>=0.10+2')
    if btc_7d is not None and eth_7d is not None:
        if p7d > btc_7d and p7d > eth_7d:
            score += 2
            breakdown.append('RS>BTC+ETH+2')
    if sym in dex_symbols:
        score += 1
        breakdown.append('dex+1')

    candidates.append({
        'sym': sym,
        'rank': rank,
        'price': price,
        'p24': p24,
        'p7d': p7d,
        'mcap': mcap,
        'vol': vol,
        'ratio': ratio,
        'score': score,
        'breakdown': ', '.join(breakdown),
    })

candidates.sort(key=lambda x: -x['score'])

print("\nTop 20 candidates:")
for c in candidates[:20]:
    print(f"  {c['sym']:12} score={c['score']:2}/10 rank={c['rank']:4} p24={c['p24']:+6.1f}% p7d={c['p7d']:+6.1f}% ratio={c['ratio']:.3f} mcap=${c['mcap']/1e6:.0f}M | {c['breakdown']}")
