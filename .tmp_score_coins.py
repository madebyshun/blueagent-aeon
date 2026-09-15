import json, sys
data = json.load(sys.stdin)
stables = {'usdt','usdc','dai','busd','tusd','usdp','frax','lusd','gusd','usdd','fdusd','pyusd','figr_heloc'}
results = []
for c in data:
    if c['symbol'].lower() in stables: continue
    mcap = c.get('market_cap') or 0
    if mcap < 20_000_000: continue
    p24 = c.get('price_change_percentage_24h_in_currency') or 0
    p7 = c.get('price_change_percentage_7d_in_currency') or 0
    vol = c.get('total_volume') or 0
    ratio = vol / mcap if mcap else 0
    score = 0
    if p24 > 0: score += 1
    if p7 > 0: score += 1
    if p24 > 5 and p7 > 5: score += 2
    if ratio >= 0.20: score += 3
    elif ratio >= 0.10: score += 2
    # BTC 7d=-2.6%, ETH 7d=-2.2%; outperforming both means p7 > -2.2
    if p7 > -2.6 and p7 > -2.2: score += 2
    results.append({
        'symbol': c['symbol'].upper(),
        'name': c['name'],
        'price': c['current_price'],
        'p24': round(p24, 2),
        'p7': round(p7, 2),
        'mcap_b': round(mcap/1e9, 2),
        'vol_m': round(vol/1e6, 1),
        'ratio': round(ratio, 3),
        'score': score,
        'rank': c['market_cap_rank']
    })
results.sort(key=lambda x: -x['score'])
for r in results[:25]:
    print(f"{r['score']:2d} | {r['symbol']:10s} | ${r['price']:10.4f} | 24h:{r['p24']:+.1f}% 7d:{r['p7']:+.1f}% | mcap ${r['mcap_b']}B | vol ${r['vol_m']}M | v/m:{r['ratio']:.3f} | rank#{r['rank']}")
