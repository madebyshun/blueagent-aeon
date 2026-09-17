import json, sys

with open(sys.argv[1]) as f:
    data = json.load(f)

btc = next((c for c in data if c['symbol'] == 'btc'), None)
eth = next((c for c in data if c['symbol'] == 'eth'), None)
print(f"BTC: 24h={btc['price_change_percentage_24h_in_currency']:.2f}% 7d={btc['price_change_percentage_7d_in_currency']:.2f}%")
print(f"ETH: 24h={eth['price_change_percentage_24h_in_currency']:.2f}% 7d={eth['price_change_percentage_7d_in_currency']:.2f}%")
print()

dedup = {'VVV', 'ETHFI', 'ARB', 'NEAR', 'ZEC', 'JUP', 'UNI'}
results = []
btc24 = btc['price_change_percentage_24h_in_currency']
btc7 = btc['price_change_percentage_7d_in_currency']
eth24 = eth['price_change_percentage_24h_in_currency']
eth7 = eth['price_change_percentage_7d_in_currency']

for c in data:
    sym = c['symbol'].upper()
    if sym in dedup:
        continue
    mc = c.get('market_cap') or 0
    if mc < 20_000_000:
        continue
    v = c.get('total_volume') or 0
    c24 = c.get('price_change_percentage_24h_in_currency') or 0
    c7 = c.get('price_change_percentage_7d_in_currency') or 0
    score = 0
    breakdown = []
    if c24 > 0:
        score += 1
        breakdown.append('+1 24h>0')
    if c7 > 0:
        score += 1
        breakdown.append('+1 7d>0')
    if c24 > 5 and c7 > 5:
        score += 2
        breakdown.append('+2 both>5%')
    vm_ratio = v / mc if mc > 0 else 0
    if vm_ratio >= 0.20:
        score += 3
        breakdown.append(f'+3 vol/mc={vm_ratio:.2f}')
    elif vm_ratio >= 0.10:
        score += 2
        breakdown.append(f'+2 vol/mc={vm_ratio:.2f}')
    if c7 > btc7 and c7 > eth7:
        score += 2
        breakdown.append('+2 RS vs BTC/ETH')
    results.append((score, sym, c['current_price'], c24, c7, mc, vm_ratio, ' | '.join(breakdown)))

results.sort(reverse=True)
for score, sym, price, c24, c7, mc, vmr, bd in results[:25]:
    print(f"{sym:10} score={score} ${price:.4f} 24h={c24:.1f}% 7d={c7:.1f}% mc=${mc/1e9:.2f}B vmr={vmr:.2f} [{bd}]")
