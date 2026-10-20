import sys, json

with open(sys.argv[1]) as f:
    data = json.load(f)

with open(sys.argv[2]) as f:
    trending_data = json.load(f)

stablecoins = {'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg','usdt','usdc','busd','frax','lusd','crvusd','gho','usdp'}
wrapped = {'wbtc','weth','steth','reth','cbeth','wsteth','weeth','ezeth','rseth','oseth'}

filtered = []
for c in data:
    sym = c['symbol'].lower()
    cid = c['id'].lower()
    name = c['name'].lower()
    if cid in stablecoins or sym in {'usdt','usdc','dai','busd','tusd','usdd','pyusd','fdusd','paxg'}:
        continue
    if sym.startswith('usd') or sym.startswith('eur') or sym.startswith('gbp'):
        continue
    if 'stablecoin' in name:
        continue
    vol = c.get('total_volume') or 0
    if vol < 1000000:
        continue
    if cid in wrapped:
        continue
    filtered.append(c)

# Build trending IDs set
trending_coins = trending_data.get('coins', [])
trending_ids = set()
trending_list = []
for tc in trending_coins[:7]:
    item = tc['item']
    trending_ids.add(item['id'])
    pd = item.get('data', {})
    p24_usd = pd.get('price_change_percentage_24h', {})
    if isinstance(p24_usd, dict):
        p24 = p24_usd.get('usd', 0)
    else:
        p24 = p24_usd or 0
    price = pd.get('price', 0)
    rank = item.get('market_cap_rank', '?')
    trending_list.append({
        'symbol': item['symbol'],
        'name': item['name'],
        'rank': rank,
        'price': price,
        'p24': p24,
        'id': item['id']
    })

winners = sorted(filtered, key=lambda x: x.get('price_change_percentage_24h_in_currency') or 0, reverse=True)[:10]
losers = sorted(filtered, key=lambda x: x.get('price_change_percentage_24h_in_currency') or 0)[:10]

def fmt_price(p):
    if p is None: return 'N/A'
    if p >= 1000: return f'${p:,.0f}'
    if p >= 1: return f'${p:.4g}'
    if p >= 0.01: return f'${p:.4f}'
    return f'${p:.6f}'

def fmt_vol(v):
    if v is None: return 'N/A'
    if v >= 1e9: return f'${v/1e9:.1f}B'
    if v >= 1e6: return f'${v/1e6:.0f}M'
    return f'${v/1e3:.0f}K'

def get_tags(c, trending_ids):
    t = []
    p24 = c.get('price_change_percentage_24h_in_currency') or 0
    p7 = c.get('price_change_percentage_7d_in_currency') or 0
    vol = c.get('total_volume') or 0
    mcap = c.get('market_cap') or 1
    rank = c.get('market_cap_rank') or 999
    cid = c['id']
    in_trending = cid in trending_ids
    if in_trending and p24 > 0: t.append('[TRENDING+UP]')
    if in_trending and p24 < 0: t.append('[TRENDING+DOWN]')
    if p24 > 15 and p7 > 25: t.append('[BREAKOUT]')
    if p24 > 20 and p7 < 0: t.append('[FADE]')
    if p24 < -10 and (vol/mcap) > 0.25: t.append('[CAPITULATION]')
    if rank > 150 and p24 > 30: t.append('[PUMP-RISK]')
    if mcap < 50e6: t.append('[MICROCAP]')
    if rank <= 20: t.append('[MAJOR]')
    return ' '.join(t[:2])

# Market pulse
top100 = [c for c in filtered if (c.get('market_cap_rank') or 999) <= 100]
top50 = sorted(top100, key=lambda x: x.get('market_cap_rank') or 999)[:50]
greens = sum(1 for c in top100 if (c.get('price_change_percentage_24h_in_currency') or 0) > 0)
changes = sorted([c.get('price_change_percentage_24h_in_currency') or 0 for c in top50])
median = changes[24] if len(changes) >= 25 else (changes[len(changes)//2] if changes else 0)

print(f'PULSE_GREENS={greens}')
print(f'PULSE_MEDIAN={median:.1f}')
print('---WINNERS---')
for c in winners:
    p24 = c.get('price_change_percentage_24h_in_currency') or 0
    p7 = c.get('price_change_percentage_7d_in_currency') or 0
    p1 = c.get('price_change_percentage_1h_in_currency') or 0
    tgs = get_tags(c, trending_ids)
    print(f'{c["symbol"].upper()}|{c["name"]}|{c.get("market_cap_rank","?")}|{fmt_price(c["current_price"])}|{p24:+.1f}%|{p7:+.1f}%|{p1:+.1f}%|{fmt_vol(c["total_volume"])}|{fmt_vol(c["market_cap"])}|{tgs}')
print('---LOSERS---')
for c in losers:
    p24 = c.get('price_change_percentage_24h_in_currency') or 0
    p7 = c.get('price_change_percentage_7d_in_currency') or 0
    p1 = c.get('price_change_percentage_1h_in_currency') or 0
    tgs = get_tags(c, trending_ids)
    print(f'{c["symbol"].upper()}|{c["name"]}|{c.get("market_cap_rank","?")}|{fmt_price(c["current_price"])}|{p24:+.1f}%|{p7:+.1f}%|{p1:+.1f}%|{fmt_vol(c["total_volume"])}|{fmt_vol(c["market_cap"])}|{tgs}')
print('---TRENDING---')
for t in trending_list:
    print(f'{t["symbol"]}|{t["name"]}|{t["rank"]}|{fmt_price(t["price"])}|{t["p24"]:+.1f}%')
