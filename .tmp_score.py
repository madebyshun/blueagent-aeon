import json, sys
data = json.load(sys.stdin)
btc = next((x for x in data if x['symbol']=='btc'), None)
eth = next((x for x in data if x['symbol']=='eth'), None)
btc24 = btc.get('price_change_percentage_24h',0) if btc else 0
eth24 = eth.get('price_change_percentage_24h',0) if eth else 0
btc7 = btc.get('price_change_percentage_7d_in_currency',0) if btc else 0
eth7 = eth.get('price_change_percentage_7d_in_currency',0) if eth else 0
print(f'BTC: 24h={btc24:.2f}% 7d={btc7:.2f}% price=${btc["current_price"]:,.2f}')
print(f'ETH: 24h={eth24:.2f}% 7d={eth7:.2f}% price=${eth["current_price"]:,.2f}')
print()

DEDUP = {'hype','pepe','ada','lit','aero'}
results = []
for t in data:
    sym = t['symbol'].lower()
    if sym in DEDUP:
        continue
    mcap = t.get('market_cap',0) or 0
    if mcap < 20_000_000:
        continue
    p24 = t.get('price_change_percentage_24h',0) or 0
    p7 = t.get('price_change_percentage_7d_in_currency',0) or 0
    vol = t.get('total_volume',0) or 0
    vol_mcap = vol/mcap if mcap else 0

    score = 0
    breakdown = []
    if p24 > 0:
        score += 1; breakdown.append('24h>0+1')
    if p7 > 0:
        score += 1; breakdown.append('7d>0+1')
    if p24 > 5 and p7 > 5:
        score += 2; breakdown.append('both>5%+2')
    if vol_mcap >= 0.20:
        score += 3; breakdown.append('vol/mcap>=0.20+3')
    elif vol_mcap >= 0.10:
        score += 2; breakdown.append('vol/mcap>=0.10+2')
    if p7 > btc7 and p7 > eth7:
        score += 2; breakdown.append('RS_BTC+ETH+2')

    results.append((score, sym, t['name'], t.get('current_price',0), p24, p7, vol, mcap, vol_mcap, breakdown))

results.sort(reverse=True)
for score, sym, name, price, p24, p7, vol, mcap, vm, bd in results[:25]:
    print(f'{score}/10 {sym.upper():10} {name[:22]:22} ${price} 24h={p24:.1f}% 7d={p7:.1f}% vol/mcap={vm:.3f} mcap=${mcap/1e9:.2f}B')
    print(f'  Breakdown: {" ".join(bd)}')
