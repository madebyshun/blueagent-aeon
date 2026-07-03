import json, sys, urllib.request

try:
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false&price_change_percentage=1h,24h,7d"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read())
except Exception as e:
    print(f"FETCH_ERROR: {e}", file=sys.stderr)
    sys.exit(1)

STABLE_IDS = {'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','pax-gold'}
WRAPPED = {'wbtc','weth','steth','weeth','wsteth','cbbtc'}

def is_stable(c):
    if c['id'] in STABLE_IDS: return True
    sym = c['symbol'].upper()
    if sym.startswith(('USD','EUR','GBP')): return True
    if 'stablecoin' in c['name'].lower(): return True
    return False

filtered = []
for c in data:
    if is_stable(c): continue
    if c['symbol'].lower() in WRAPPED: continue
    vol = c.get('total_volume') or 0
    if vol < 1_000_000: continue
    filtered.append(c)

by_24h = sorted(filtered, key=lambda c: c.get('price_change_percentage_24h_in_currency') or -999, reverse=True)
top10 = by_24h[:10]
bot10 = list(reversed(by_24h[-10:]))

def fmt_vol(v):
    if v >= 1e9: return f"${v/1e9:.1f}B"
    if v >= 1e6: return f"${v/1e6:.0f}M"
    return f"${v:,.0f}"

print(f"TOTAL:{len(data)} FILTERED:{len(filtered)}")
print("WINNERS:")
for c in top10:
    print(json.dumps({
        "sym": c["symbol"].upper(),
        "name": c["name"],
        "rank": c.get("market_cap_rank") or 999,
        "price": c.get("current_price") or 0,
        "ch24": round(c.get("price_change_percentage_24h_in_currency") or 0, 2),
        "ch7": round(c.get("price_change_percentage_7d_in_currency") or 0, 2),
        "ch1": round(c.get("price_change_percentage_1h_in_currency") or 0, 2),
        "vol": c.get("total_volume") or 0,
        "mc": c.get("market_cap") or 0,
    }))

print("LOSERS:")
for c in bot10:
    print(json.dumps({
        "sym": c["symbol"].upper(),
        "name": c["name"],
        "rank": c.get("market_cap_rank") or 999,
        "price": c.get("current_price") or 0,
        "ch24": round(c.get("price_change_percentage_24h_in_currency") or 0, 2),
        "ch7": round(c.get("price_change_percentage_7d_in_currency") or 0, 2),
        "ch1": round(c.get("price_change_percentage_1h_in_currency") or 0, 2),
        "vol": c.get("total_volume") or 0,
        "mc": c.get("market_cap") or 0,
    }))

top100 = sorted(filtered, key=lambda c: c.get("market_cap") or 0, reverse=True)[:100]
green = sum(1 for c in top100 if (c.get("price_change_percentage_24h_in_currency") or 0) > 0)
top50 = top100[:50]
ch50 = sorted([c.get("price_change_percentage_24h_in_currency") or 0 for c in top50])
median50 = ch50[25]

btc = data[0]
print(f"PULSE:{green}/100 median50={median50:.1f}% BTC=${btc['current_price']} BTC24h={btc.get('price_change_percentage_24h_in_currency',0):.2f}%")
