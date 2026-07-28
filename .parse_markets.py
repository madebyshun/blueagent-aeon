import json, sys

data = json.load(sys.stdin)

STABLECOINS = {
    'tether','usd-coin','dai','ethena-usde','true-usd','usdd','paypal-usd',
    'first-digital-usd','pax-gold','ripple-usd','usds','usd1','frax','busd',
    'gusd','cusd','usd0','usdgo','gho','usual-usd','ylds','circle-usyc',
    'buidl','blockchain-capital','ondo-us-dollar-yield',
    'janus-henderson-anemory-treasury','janus-henderson-anemoy-aaa-clo',
    'spiko-eu-t-bills-money-market','spiko-amundi-overnight-swap',
    'invesco-short-duration-us-govt','united-stables','bfusd',
    'figure-heloc','a7a5','canton-network','canton','rlusd','usdf',
    'world-liberty-financial-usd1',
}
STABLE_SYMS = {
    'USDT','USDC','DAI','USDE','TUSD','USDD','PYUSD','FDUSD','RLUSD',
    'USDS','USD1','USDG','USX','USD0','USDGO','GHO','USDF','USDY','YLDS',
    'USYC','BFUSD','FRAX','BUSD','GUSD','U',
}
SKIP_NAME_PARTS = [
    'stablecoin','treasury','t-bill','institutional','gold pegged',
    'heloc','anemoy','anemory','invesco','blackrock usd','spiko',
    'janus','falcon usd','canton','bfusd',
]

filtered = []
for c in data:
    cid = c.get('id', '')
    sym = (c.get('symbol') or '').upper()
    name_lower = (c.get('name') or '').lower()
    vol = c.get('total_volume') or 0

    if cid in STABLECOINS:
        continue
    if sym in STABLE_SYMS:
        continue
    if any(k in name_lower for k in SKIP_NAME_PARTS):
        continue
    if sym.startswith('USD') or sym.startswith('EUR') or sym.startswith('GBP'):
        continue
    if vol < 1_000_000:
        continue

    p24 = c.get('price_change_percentage_24h_in_currency')
    if p24 is None:
        continue

    filtered.append({
        'rank': c.get('market_cap_rank'),
        'sym': sym,
        'name': c.get('name'),
        'price': c.get('current_price'),
        'p1h': c.get('price_change_percentage_1h_in_currency'),
        'p24': p24,
        'p7d': c.get('price_change_percentage_7d_in_currency'),
        'vol': vol,
        'mcap': c.get('market_cap') or 0,
    })

filtered.sort(key=lambda x: x['p24'], reverse=True)

def fmt_price(p):
    if p is None:
        return 'N/A'
    if p >= 1000:
        return f'${p:,.0f}'
    if p >= 1:
        return f'${p:.4f}'
    if p >= 0.01:
        return f'${p:.5f}'
    return f'${p:.8f}'

def fmt_vol(v):
    if v >= 1e9:
        return f'${v/1e9:.1f}B'
    if v >= 1e6:
        return f'${v/1e6:.1f}M'
    return f'${v/1e3:.0f}K'

def fmt_pct(p):
    if p is None:
        return 'N/A'
    sign = '+' if p >= 0 else ''
    return f'{sign}{p:.1f}%'

print('=== TOP 15 WINNERS (24h) ===')
for i, c in enumerate(filtered[:15], 1):
    print(f'{i}. {c["sym"]} ({c["name"]}) -- {fmt_price(c["price"])}  24h {fmt_pct(c["p24"])} / 7d {fmt_pct(c["p7d"])} / 1h {fmt_pct(c["p1h"])}  |  vol {fmt_vol(c["vol"])} / rank #{c["rank"]}  mcap {fmt_vol(c["mcap"])}')

print()
print('=== TOP 15 LOSERS (24h) ===')
losers = sorted(filtered, key=lambda x: x['p24'])
for i, c in enumerate(losers[:15], 1):
    print(f'{i}. {c["sym"]} ({c["name"]}) -- {fmt_price(c["price"])}  24h {fmt_pct(c["p24"])} / 7d {fmt_pct(c["p7d"])} / 1h {fmt_pct(c["p1h"])}  |  vol {fmt_vol(c["vol"])} / rank #{c["rank"]}  mcap {fmt_vol(c["mcap"])}')

top100 = filtered[:100]
green = sum(1 for c in top100 if c['p24'] > 0)
top50_vals = sorted([c['p24'] for c in top100[:50]])
top50_median = top50_vals[25] if len(top50_vals) > 25 else 0

print()
print('=== MARKET PULSE ===')
print(f'Filtered coins with data: {len(filtered)}')
print(f'Top 100 (filtered): {green}/100 positive 24h  |  Median top-50 24h: {fmt_pct(top50_median)}')

btc = next((c for c in data if c.get('id') == 'bitcoin'), None)
eth = next((c for c in data if c.get('id') == 'ethereum'), None)
if btc:
    print(f'BTC: {fmt_price(btc["current_price"])} ({fmt_pct(btc.get("price_change_percentage_24h_in_currency"))} 24h)')
if eth:
    print(f'ETH: {fmt_price(eth["current_price"])} ({fmt_pct(eth.get("price_change_percentage_24h_in_currency"))} 24h)')

print()
print('=== ALL FILTERED (for dedup check) ===')
for c in filtered:
    p24 = fmt_pct(c['p24'])
    print(f'{c["sym"]} {p24}')
