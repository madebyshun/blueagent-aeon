import json, sys, urllib.request

STABLECOINS = {
    'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg',
    'usds','usdb','frax','lusd','susd','husd','busd','usdp','neutrino','tribe-2','reserve-rights-token',
    'origin-dollar','dola-borrowing-right','celo-dollar'
}
WRAPPED = {
    'wrapped-bitcoin','wrapped-ether','staked-ether','rocket-pool-eth','cbeth','reth','frxeth',
    'sfrxeth','wbeth','ankr-reward-bearing-staked-eth','weeth','wrapped-steth','wsteth'
}

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

def get_24h(c):
    v = c.get('price_change_percentage_24h_in_currency') or c.get('price_change_percentage_24h')
    return v if v is not None else 0

def get_tags(c, is_loser=False, trending_ids=None):
    if trending_ids is None:
        trending_ids = set()
    ch24 = get_24h(c)
    ch7d = c.get('price_change_percentage_7d_in_currency') or 0
    rank = c.get('market_cap_rank') or 999
    vol = c.get('total_volume') or 0
    mcap = c.get('market_cap') or 0
    cid = c.get('id','')
    tags = []

    in_trending = cid in trending_ids
    if in_trending and ch24 > 0:
        tags.append('TRENDING+UP')
    elif in_trending and ch24 < 0:
        tags.append('TRENDING+DOWN')

    if not is_loser:
        if ch24 > 15 and ch7d > 25:
            tags.append('BREAKOUT')
        elif ch24 > 20 and ch7d < 0:
            tags.append('FADE')
        if rank > 150 and ch24 > 30:
            tags.append('PUMP-RISK')
    else:
        if ch24 < -10 and mcap > 0 and vol / mcap > 0.25:
            tags.append('CAPITULATION')

    if mcap > 0 and mcap < 50_000_000:
        tags.append('MICROCAP')
    if rank <= 20:
        tags.append('MAJOR')

    seen = []
    for t in tags:
        if t not in seen:
            seen.append(t)
    return seen[:2]

# Fetch markets
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false&price_change_percentage=1h,24h,7d"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=20) as resp:
    data = json.load(resp)

# Fetch trending
turl = "https://api.coingecko.com/api/v3/search/trending"
treq = urllib.request.Request(turl, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(treq, timeout=20) as tresp:
    tdata = json.load(tresp)

trending_coins = tdata.get('coins', [])[:7]
trending_ids = {c['item']['id'] for c in trending_coins}

# Filter
filtered = []
for c in data:
    cid = c.get('id', '')
    sym = c.get('symbol', '').upper()
    name = c.get('name', '')
    vol = c.get('total_volume') or 0

    if cid in STABLECOINS:
        continue
    if sym.startswith(('USD', 'EUR', 'GBP')):
        continue
    if 'stablecoin' in name.lower():
        continue
    if cid in WRAPPED:
        continue
    if vol < 1_000_000:
        continue

    filtered.append(c)

# Market pulse
top100 = [c for c in filtered if (c.get('market_cap_rank') or 999) <= 100]
green = sum(1 for c in top100 if get_24h(c) > 0)
top50 = sorted(top100, key=lambda c: c.get('market_cap') or 0, reverse=True)[:50]
changes50 = sorted([get_24h(c) for c in top50])
median50 = changes50[len(changes50)//2] if changes50 else 0.0

# Sort by 24h
sorted_coins = sorted(filtered, key=get_24h, reverse=True)
winners = sorted_coins[:10]
losers = sorted_coins[-10:][::-1]

btc = next((c for c in data if c['id'] == 'bitcoin'), None)
eth = next((c for c in data if c['id'] == 'ethereum'), None)

print(f"PULSE: {green}/{len(top100)} top-100 green, median top-50 {median50:+.1f}%")
if btc:
    print(f"BTC: {fmt_price(btc['current_price'])} {get_24h(btc):+.1f}%")
if eth:
    print(f"ETH: {fmt_price(eth['current_price'])} {get_24h(eth):+.1f}%")

print("\n=== WINNERS ===")
for i, c in enumerate(winners, 1):
    ch24 = get_24h(c)
    ch7d = c.get('price_change_percentage_7d_in_currency') or 0
    ch1h = c.get('price_change_percentage_1h_in_currency') or 0
    rank = c.get('market_cap_rank') or 999
    tags = get_tags(c, is_loser=False, trending_ids=trending_ids)
    tag_str = ' '.join(f'[{t}]' for t in tags) if tags else ''
    print(f"{i}. {c['symbol'].upper()} ({c['name']}) — {fmt_price(c['current_price'])}  {ch24:+.1f}% / 7d {ch7d:+.1f}% / 1h {ch1h:+.1f}%  •  {fmt_vol(c['total_volume'])} / #{rank}  {tag_str}")

print("\n=== LOSERS ===")
for i, c in enumerate(losers, 1):
    ch24 = get_24h(c)
    ch7d = c.get('price_change_percentage_7d_in_currency') or 0
    ch1h = c.get('price_change_percentage_1h_in_currency') or 0
    rank = c.get('market_cap_rank') or 999
    tags = get_tags(c, is_loser=True, trending_ids=trending_ids)
    tag_str = ' '.join(f'[{t}]' for t in tags) if tags else ''
    print(f"{i}. {c['symbol'].upper()} ({c['name']}) — {fmt_price(c['current_price'])}  {ch24:+.1f}% / 7d {ch7d:+.1f}% / 1h {ch1h:+.1f}%  •  {fmt_vol(c['total_volume'])} / #{rank}  {tag_str}")

print("\n=== TRENDING ===")
for i, coin_wrap in enumerate(trending_coins, 1):
    item = coin_wrap['item']
    cid = item['id']
    sym = item.get('symbol', '').upper()
    name = item.get('name', '')
    rank = item.get('market_cap_rank', 'N/A')
    data_match = next((c for c in data if c['id'] == cid), None)
    if data_match:
        price = fmt_price(data_match['current_price'])
        ch24 = get_24h(data_match)
        tags = get_tags(data_match, is_loser=(ch24 < 0), trending_ids=trending_ids)
        tag_str = ' '.join(f'[{t}]' for t in tags) if tags else ''
        print(f"{i}. {name} ({sym}) — #{rank}, {price}, 24h {ch24:+.1f}%  {tag_str}")
    else:
        print(f"{i}. {name} ({sym}) — #{rank}, price N/A")
