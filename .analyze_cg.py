#!/usr/bin/env python3
import json, statistics

with open('/tmp/cg_markets.json') as f:
    data = json.load(f)

print(f"TOTAL_ENTRIES:{len(data)}")
for coin in data:
    cid = coin.get('id','')
    sym = coin.get('symbol','')
    name = coin.get('name','')
    rank = coin.get('market_cap_rank')
    price = coin.get('current_price')
    chg24 = coin.get('price_change_percentage_24h_in_currency') or coin.get('price_change_percentage_24h')
    chg7d = coin.get('price_change_percentage_7d_in_currency')
    chg1h = coin.get('price_change_percentage_1h_in_currency')
    vol = coin.get('total_volume')
    mcap = coin.get('market_cap')
    print(f"COIN|{cid}|{sym}|{name}|{rank}|{price}|{chg24}|{chg7d}|{chg1h}|{vol}|{mcap}")
