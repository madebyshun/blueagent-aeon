import json, sys

data = json.load(sys.stdin)
coins = data.get('coins', [])
print('=== TRENDING ===')
for item in coins[:7]:
    c = item.get('item', {})
    name = c.get('name','')
    sym = c.get('symbol','')
    rank = c.get('market_cap_rank','?')
    d2 = c.get('data', {})
    price = d2.get('price', '')
    p24 = d2.get('price_change_percentage_24h', {})
    p24_usd = p24.get('usd', '') if isinstance(p24, dict) else ''
    print(f"{name}|{sym}|{rank}|{price}|{p24_usd}")
