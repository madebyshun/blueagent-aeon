import sys, json, statistics

data = json.load(sys.stdin)

STABLE_IDS = {
    'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg',
    'tether-gold','ethena-usde','usds','global-dollar','hashnote-usyc','bfusd','ripple-usd',
    'falcon-finance','blackrock-usd-institutional-digital-liquidity-fund',
    'superstate-short-duration-us-government-securities-fund-ustb','blockchain-capital',
    'janus-henderson-anemoy-treasury-fund','eutbl','spiko-amundi-overnight-swap-fund-eur',
    'usual-usd','gho','united-stables','usdgo','ylds','usx','true-usd','ondo-us-dollar-yield',
    'janus-henderson-anemoy-aaa-clo-fund','usd1-wlfi','figure-heloc','bianrensheng',
    'rain','stable-2'
}
STABLE_SYMS = {
    'usdt','usdc','dai','tusd','usdd','pyusd','fdusd','usde','usds','usdg','usyc','rlusd',
    'bfusd','usdf','buidl','ustb','jtrsy','eutbl','eursafo','usd0','gho','u','usdgo',
    'ylds','usx','usdy','usd1','figr_heloc','jaaa','bcap','xaut','paxg','rain','stable'
}

filtered = []
for c in data:
    sym = c.get('symbol','').lower()
    cid = c.get('id','')
    vol = c.get('total_volume') or 0
    if cid in STABLE_IDS or sym in STABLE_SYMS:
        continue
    if vol < 1000000:
        continue
    pct24 = c.get('price_change_percentage_24h_in_currency')
    if pct24 is None:
        continue
    filtered.append({
        'rank': c.get('market_cap_rank'),
        'sym': c.get('symbol','').upper(),
        'name': c.get('name'),
        'price': c.get('current_price'),
        'pct24': round(pct24, 2),
        'pct7d': round(c.get('price_change_percentage_7d_in_currency') or 0, 2),
        'pct1h': round(c.get('price_change_percentage_1h_in_currency') or 0, 2),
        'vol': c.get('total_volume'),
        'mcap': c.get('market_cap'),
    })

filtered.sort(key=lambda x: x['pct24'], reverse=True)

def fmt(c):
    p = c['price']
    if p < 0.0001:
        ps = f"${p:.8f}"
    elif p < 0.01:
        ps = f"${p:.6f}"
    elif p < 1:
        ps = f"${p:.4f}"
    elif p < 100:
        ps = f"${p:.3f}"
    else:
        ps = f"${p:,.2f}"
    vol = c['vol']
    vs = f"${vol/1e9:.2f}B" if vol >= 1e9 else f"${vol/1e6:.1f}M"
    mc = c['mcap']
    ms = f"${mc/1e9:.2f}B" if mc >= 1e9 else f"${mc/1e6:.0f}M"
    return f"#{c['rank']} {c['sym']} ({c['name']}) {c['pct24']:+.1f}% 7d:{c['pct7d']:+.1f}% 1h:{c['pct1h']:+.1f}%  vol:{vs} mcap:{ms} {ps}"

print('=== TOP 15 WINNERS ===')
for c in filtered[:15]:
    print(fmt(c))

print()
print('=== TOP 15 LOSERS ===')
for c in filtered[-15:][::-1]:
    print(fmt(c))

print()
print(f'Total filtered coins: {len(filtered)}')

top100 = [c for c in filtered if (c.get('rank') or 999) <= 100]
green = sum(1 for c in top100 if c['pct24'] > 0)
top50 = sorted(top100, key=lambda x: x.get('rank') or 999)[:50]
median50 = statistics.median([c['pct24'] for c in top50]) if top50 else 0
print(f'Top-100 green: {green}/{len(top100)}, median top-50 pct24: {median50:.2f}%')
