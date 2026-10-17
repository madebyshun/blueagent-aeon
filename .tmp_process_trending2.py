import json

with open('/home/runner/work/blueagent-aeon/blueagent-aeon/.tmp_trending.json') as f:
    data = json.load(f)

coins = data.get('coins', [])

print('TRENDING')
for i, entry in enumerate(coins[:7]):
    item = entry.get('item', {})
    name = item.get('name','')
    sym = item.get('symbol','').upper()
    rank = item.get('market_cap_rank','?')
    d = item.get('data', {})
    price = d.get('price', 0)
    ch24_dict = d.get('price_change_percentage_24h', {})
    ch24 = ch24_dict.get('usd', 0) if isinstance(ch24_dict, dict) else 0
    cid = item.get('id','')
    if isinstance(price, (int, float)) and price >= 1:
        price_str = f'${price:,.4g}'
    elif isinstance(price, (int, float)) and price >= 0.01:
        price_str = f'${price:.4f}'
    elif isinstance(price, (int, float)):
        price_str = f'${price:.6f}'
    else:
        price_str = str(price)
    print(f"{sym}|{name}|{rank}|{price_str}|{ch24:+.1f}%|{cid}")
