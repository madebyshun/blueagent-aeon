import json, sys

with open(sys.argv[1]) as f:
    data = json.load(f)
coins = data.get('coins', [])
for c in coins:
    item = c['item']
    d = item.get('data', {})
    pct = d.get('price_change_percentage_24h', {})
    pct24 = pct.get('usd', 0) if isinstance(pct, dict) else pct
    print(f"{item['symbol']:10} rank={item['market_cap_rank']} price=${d.get('price', 0):.4f} 24h={pct24:.2f}% score={item['score']}")
