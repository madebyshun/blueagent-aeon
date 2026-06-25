import urllib.request, json, sys

url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false&price_change_percentage=1h,24h,7d'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=30) as r:
    data = json.loads(r.read())

STABLE_IDS = {'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','pax-gold','frax','true-usd','nusd','usdb','usd-plus','usdx','mountain-protocol-usdm','crvusd','mkusd','defi-dollar'}
WRAPPED_SYMS = {'wbtc','weth','steth','reth','cbeth','weeth','ezeth','lseth','oseth'}

def is_stable(c):
    if c['id'] in STABLE_IDS:
        return True
    sym = c['symbol'].upper()
    if sym.startswith(('USD','EUR','GBP')):
        return True
    if 'stablecoin' in c['name'].lower():
        return True
    return False

def is_wrapped(c):
    return c['symbol'].lower() in WRAPPED_SYMS

filtered = [c for c in data if not is_stable(c) and not is_wrapped(c) and c.get('total_volume', 0) >= 1_000_000]

print(f"Total: {len(data)}, After filter: {len(filtered)}")

valid = [c for c in filtered if c.get('price_change_percentage_24h_in_currency') is not None]
winners = sorted(valid, key=lambda x: x['price_change_percentage_24h_in_currency'], reverse=True)[:12]
losers = sorted(valid, key=lambda x: x['price_change_percentage_24h_in_currency'])[:12]

top100 = filtered[:100]
green = sum(1 for c in top100 if c.get('price_change_percentage_24h_in_currency', 0) > 0)
top50_changes = sorted([c.get('price_change_percentage_24h_in_currency', 0) for c in filtered[:50] if c.get('price_change_percentage_24h_in_currency') is not None])
median_50 = top50_changes[len(top50_changes)//2] if top50_changes else 0
btc = next((c for c in data if c['symbol'] == 'btc'), None)
btc_change = btc['price_change_percentage_24h_in_currency'] if btc else None
btc_price = btc['current_price'] if btc else None

print(f"MARKET_PULSE: {green}/100 green, median_top50={median_50:.1f}%, BTC={btc_change:.1f}%, BTC_price={btc_price}")

def fmt_price(p):
    if p is None:
        return 'N/A'
    if p >= 1000:
        return f'${p:,.0f}'
    if p >= 1:
        return f'${p:.4g}'
    if p >= 0.01:
        return f'${p:.4f}'
    return f'${p:.6f}'

def fmt_vol(v):
    if v >= 1e9:
        return f'${v/1e9:.1f}B'
    if v >= 1e6:
        return f'${v/1e6:.0f}M'
    return f'${v/1e3:.0f}K'

print("\n=== WINNERS ===")
for i, c in enumerate(winners, 1):
    chg1h = c.get('price_change_percentage_1h_in_currency') or 0
    chg24 = c.get('price_change_percentage_24h_in_currency') or 0
    chg7d = c.get('price_change_percentage_7d_in_currency') or 0
    vol = c.get('total_volume', 0)
    mcap = c.get('market_cap', 0)
    rank = c.get('market_cap_rank')
    price = c.get('current_price', 0)
    print(f"{i}|{c['symbol'].upper()}|{c['name']}|rank{rank}|{fmt_price(price)}|{chg24:+.1f}%|7d{chg7d:+.1f}%|1h{chg1h:+.1f}%|vol{fmt_vol(vol)}|mcap{fmt_vol(mcap)}")

print("\n=== LOSERS ===")
for i, c in enumerate(losers, 1):
    chg1h = c.get('price_change_percentage_1h_in_currency') or 0
    chg24 = c.get('price_change_percentage_24h_in_currency') or 0
    chg7d = c.get('price_change_percentage_7d_in_currency') or 0
    vol = c.get('total_volume', 0)
    mcap = c.get('market_cap', 0)
    rank = c.get('market_cap_rank')
    price = c.get('current_price', 0)
    print(f"{i}|{c['symbol'].upper()}|{c['name']}|rank{rank}|{fmt_price(price)}|{chg24:+.1f}%|7d{chg7d:+.1f}%|1h{chg1h:+.1f}%|vol{fmt_vol(vol)}|mcap{fmt_vol(mcap)}")

print("\n=== FULL DATA FOR SIGNAL SCORING ===")
for c in filtered[:200]:
    chg24 = c.get('price_change_percentage_24h_in_currency') or 0
    chg7d = c.get('price_change_percentage_7d_in_currency') or 0
    vol = c.get('total_volume', 0)
    mcap = c.get('market_cap', 0)
    rank = c.get('market_cap_rank') or 999
    print(f"{c['symbol'].upper()}|{chg24:.1f}|{chg7d:.1f}|{vol:.0f}|{mcap:.0f}|{rank}")
