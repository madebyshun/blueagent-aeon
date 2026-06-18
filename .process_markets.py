import json, sys, statistics

data = json.load(sys.stdin)

STABLES = {
    'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd',
    'fdusd','paxg','bridged-usd-coin','true-usd','usds','frax','crvusd',
    'dola-borrowing-right','usdc','usdt','busd','susd','gusd'
}
STABLE_SYMS = {
    'usdt','usdc','dai','tusd','busd','usde','pyusd','fdusd','susd','gusd',
    'frax','lusd','usdp','usdd','mkusd','crvusd','usdm','dola','cusd','musd',
    'usdc.e','eurc','eur','steur','usd1'
}
WRAPPED = {
    'wrapped-bitcoin','wrapped-ether','wrapped-steth','staked-ether',
    'wrapped-eeth','coinbase-wrapped-staked-eth','rocket-pool-eth',
    'mantle-staked-ether','binance-eth'
}

filtered = []
for c in data:
    sym = c['symbol'].lower()
    cid = c['id'].lower()
    name_lower = c['name'].lower()
    if cid in STABLES or sym in STABLE_SYMS:
        continue
    if sym.startswith('usd') or sym.startswith('eur') or sym.startswith('gbp'):
        continue
    if 'stablecoin' in name_lower:
        continue
    vol = c.get('total_volume') or 0
    if vol < 1_000_000:
        continue
    if cid in WRAPPED:
        continue
    filtered.append(c)

print(f"Filtered count: {len(filtered)}", file=sys.stderr)

top100 = [c for c in filtered if c.get('market_cap_rank') and c['market_cap_rank'] <= 100]
green = sum(1 for c in top100 if (c.get('price_change_percentage_24h') or 0) > 0)
changes50 = sorted([c.get('price_change_percentage_24h') or 0 for c in filtered if c.get('market_cap_rank') and c['market_cap_rank'] <= 50])
med50 = statistics.median(changes50) if changes50 else 0

sorted_by_24h = sorted(filtered, key=lambda c: c.get('price_change_percentage_24h') or 0, reverse=True)
winners = sorted_by_24h[:15]
losers = list(reversed(sorted_by_24h[-15:]))

result = {
    'pulse': {'top100_green': green, 'top100_total': len(top100), 'median_top50': round(med50, 2)},
    'winners': [],
    'losers': [],
    'all_ids': [c['id'] for c in filtered]
}

for c in winners:
    result['winners'].append({
        'symbol': c['symbol'].upper(),
        'name': c['name'],
        'id': c['id'],
        'rank': c.get('market_cap_rank'),
        'price': c.get('current_price', 0),
        'ch24': round(c.get('price_change_percentage_24h') or 0, 1),
        'ch7d': round(c.get('price_change_percentage_7d_in_currency') or 0, 1),
        'ch1h': round(c.get('price_change_percentage_1h_in_currency') or 0, 1),
        'vol': c.get('total_volume') or 0,
        'mcap': c.get('market_cap') or 0
    })

for c in losers:
    result['losers'].append({
        'symbol': c['symbol'].upper(),
        'name': c['name'],
        'id': c['id'],
        'rank': c.get('market_cap_rank'),
        'price': c.get('current_price', 0),
        'ch24': round(c.get('price_change_percentage_24h') or 0, 1),
        'ch7d': round(c.get('price_change_percentage_7d_in_currency') or 0, 1),
        'ch1h': round(c.get('price_change_percentage_1h_in_currency') or 0, 1),
        'vol': c.get('total_volume') or 0,
        'mcap': c.get('market_cap') or 0
    })

print(json.dumps(result))
