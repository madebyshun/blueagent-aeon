import json, sys

with open(sys.argv[1]) as f:
    trending_data = json.load(f)

with open(sys.argv[2]) as f:
    markets_data = json.load(f)

# Trending symbols
trending_symbols = set()
coins = trending_data.get('coins', [])
print('Trending coins:')
for c in coins:
    item = c['item']
    sym = item['symbol'].lower()
    trending_symbols.add(sym)
    d = item.get('data', {})
    price = d.get('price', 'N/A')
    pct = d.get('price_change_percentage_24h', {})
    pct_usd = pct.get('usd', 'N/A') if isinstance(pct, dict) else pct
    if isinstance(pct_usd, float):
        print(f"  {item['symbol'].upper()} (rank {item.get('market_cap_rank','?')}): ${price:.4f} | 24h: {pct_usd:.2f}%")
    else:
        print(f"  {item['symbol'].upper()}: {price}")

print()

# BTC and ETH benchmarks
btc = next(x for x in markets_data if x['symbol']=='btc')
eth = next(x for x in markets_data if x['symbol']=='eth')
btc_24h = btc['price_change_percentage_24h_in_currency']
btc_7d = btc['price_change_percentage_7d_in_currency']
eth_24h = eth['price_change_percentage_24h_in_currency']
eth_7d = eth['price_change_percentage_7d_in_currency']
print(f"BTC: ${btc['current_price']:,.0f} | 24h: {btc_24h:.2f}% | 7d: {btc_7d:.2f}%")
print(f"ETH: ${eth['current_price']:,.0f} | 24h: {eth_24h:.2f}% | 7d: {eth_7d:.2f}%")
print()

# Score tokens
skip_symbols = {'btc','eth','usdt','usdc','dai','usds','fdusd','tusd','busd','usdp','usde','pyusd','eurc','wbtc','cbbtc','weeth','wsteth','ezeth','rseth','reth','steth','bbtc'}
dedup = {'strk','inj','q'}
results = []
for t in markets_data:
    sym = t['symbol'].lower()
    if sym in skip_symbols: continue
    if sym in dedup: continue
    mcap = t.get('market_cap') or 0
    if mcap < 20_000_000: continue
    price = t.get('current_price', 0) or 0
    vol = t.get('total_volume', 0) or 0
    pct24h = t.get('price_change_percentage_24h_in_currency', 0) or 0
    pct7d = t.get('price_change_percentage_7d_in_currency', 0) or 0
    volmcap = vol / mcap if mcap > 0 else 0

    score = 0
    breakdown = []
    if pct24h > 0:
        score += 1; breakdown.append('24h>0+1')
    if pct7d > 0:
        score += 1; breakdown.append('7d>0+1')
    if pct24h > 5 and pct7d > 5:
        score += 2; breakdown.append('both>5%+2')
    if volmcap >= 0.20:
        score += 3; breakdown.append(f'vol/mcap{volmcap:.2f}+3')
    elif volmcap >= 0.10:
        score += 2; breakdown.append(f'vol/mcap{volmcap:.2f}+2')
    if pct7d > btc_7d and pct7d > eth_7d:
        score += 2; breakdown.append('RS vs BTC+ETH+2')
    if sym in trending_symbols:
        score += 2; breakdown.append('CG trending+2')

    results.append((score, sym.upper(), t['name'], price, pct24h, pct7d, mcap, vol, volmcap, breakdown))

results.sort(reverse=True)
print('Top 25 scored tokens:')
for score, sym, name, price, p24, p7d, mcap, vol, vm, bd in results[:25]:
    print(f"  {sym} ({name}): {score}/10 | ${price:.4f} | 24h={p24:.1f}% | 7d={p7d:.1f}% | mcap=${mcap/1e6:.0f}M | vol=${vol/1e6:.1f}M | v/mc={vm:.3f}")
    print(f"    [{', '.join(bd)}]")
