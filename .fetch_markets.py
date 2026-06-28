import urllib.request, json, sys

url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false&price_change_percentage=1h,24h,7d'
req = urllib.request.urlopen(url, timeout=30)
data = json.loads(req.read())

STABLECOIN_IDS = {'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg','frax','usds','usdb','usdp'}
STABLECOIN_SYMS = {'USDT','USDC','DAI','BUSD','TUSD','USDD','PYUSD','FDUSD','FRAX','USDS','USDP','GUSD','LUSD'}
WRAPPED = {'wbtc','weth','steth','wsteth','weeth','reth','cbbtc','cbeth'}

filtered = []
for c in data:
    cid = c.get('id','')
    sym = (c.get('symbol') or '').upper()
    vol = c.get('total_volume') or 0
    name = (c.get('name') or '').lower()
    if cid in STABLECOIN_IDS: continue
    if sym in STABLECOIN_SYMS: continue
    if sym.startswith('USD') or sym.startswith('EUR') or sym.startswith('GBP'): continue
    if 'stablecoin' in name: continue
    if cid in WRAPPED: continue
    if vol < 1_000_000: continue
    filtered.append(c)

top100_filtered = [c for c in filtered if (c.get('market_cap_rank') or 999) <= 100]
positive = sum(1 for c in top100_filtered if (c.get('price_change_percentage_24h') or 0) > 0)
top50 = sorted(top100_filtered, key=lambda c: c.get('market_cap_rank') or 999)[:50]
median_idx = len(top50) // 2
changes_50 = sorted([c.get('price_change_percentage_24h') or 0 for c in top50])
median_change = changes_50[median_idx] if changes_50 else 0

sorted_by_24h = sorted(filtered, key=lambda c: c.get('price_change_percentage_24h') or 0, reverse=True)
winners = sorted_by_24h[:10]
losers = sorted_by_24h[-10:]

print(f"FILTERED_COUNT={len(filtered)}")
print(f"TOP100_GREEN={positive}/{len(top100_filtered)}")
print(f"MEDIAN_50={median_change:.1f}")
print("WINNERS:")
for c in winners:
    r = c.get('market_cap_rank') or 999
    sym = (c.get('symbol') or '').upper()
    name = c.get('name','')
    price = c.get('current_price') or 0
    ch24 = c.get('price_change_percentage_24h') or 0
    ch7 = c.get('price_change_percentage_7d_in_currency') or 0
    ch1 = c.get('price_change_percentage_1h_in_currency') or 0
    vol = c.get('total_volume') or 0
    mcap = c.get('market_cap') or 0
    print(f"  {sym}|{name}|{r}|{price}|{ch24:.1f}|{ch7:.1f}|{ch1:.1f}|{vol:.0f}|{mcap:.0f}")
print("LOSERS:")
for c in losers:
    r = c.get('market_cap_rank') or 999
    sym = (c.get('symbol') or '').upper()
    name = c.get('name','')
    price = c.get('current_price') or 0
    ch24 = c.get('price_change_percentage_24h') or 0
    ch7 = c.get('price_change_percentage_7d_in_currency') or 0
    ch1 = c.get('price_change_percentage_1h_in_currency') or 0
    vol = c.get('total_volume') or 0
    mcap = c.get('market_cap') or 0
    print(f"  {sym}|{name}|{r}|{price}|{ch24:.1f}|{ch7:.1f}|{ch1:.1f}|{vol:.0f}|{mcap:.0f}")
