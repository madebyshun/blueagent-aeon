import json, statistics
from urllib.request import urlopen, Request
from urllib.error import URLError

MARKETS_URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false&price_change_percentage=1h,24h,7d"
TRENDING_URL = "https://api.coingecko.com/api/v3/search/trending"

def fetch(url):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
    with urlopen(req, timeout=30) as r:
        return json.loads(r.read())

markets = fetch(MARKETS_URL)
print(f"Markets count: {len(markets)}", flush=True)

try:
    trending_raw = fetch(TRENDING_URL)
    trending_ids = {c["item"]["id"] for c in trending_raw.get("coins", [])}
    trending_list = []
    for c in trending_raw.get("coins", []):
        item = c["item"]
        trending_list.append({
            "id": item["id"],
            "name": item["name"],
            "symbol": item["symbol"].upper(),
            "rank": item.get("market_cap_rank"),
            "price": item.get("data", {}).get("price"),
            "ch24": item.get("data", {}).get("price_change_percentage_24h", {}).get("usd")
        })
    print(f"Trending count: {len(trending_list)}", flush=True)
except Exception as e:
    print(f"Trending failed: {e}", flush=True)
    trending_ids = set()
    trending_list = []

STABLE_IDS = {
    'tether','usd-coin','dai','first-digital-usd','ethena-usde','true-usd','usdd','paypal-usd',
    'fdusd','pax-gold','tether-gold','usd1','global-dollar','usual-usd',
    'usds','circle-usyc','blackrock-usd-institutional-digital-liquidity-fund','ripple-usd',
    'bfusd','janus-henderson-anemoy-treasury-fund','janus-henderson-anemoy-aaa-clo-fund',
    'invesco-short-duration-us-government-securities-fund','spiko-eu-t-bills-money-market-fund',
    'spiko-amundi-overnight-swap-fund','ylds','united-stables','ondo-us-dollar-yield',
    'falcon-usd','usx-stablecoin','blockchain-capital','stable-usd','world-liberty-financial',
    'frax','crvusd','dola-borrowing-right','binance-peg-busd','susd','gusd','mkusd','lusd','musd',
    'figr-heloc','figure-heloc','canton-network'
}
STABLE_SYMS = {
    'usdt','usdc','dai','tusd','busd','usde','pyusd','fdusd','susd','gusd','frax','lusd','usdp',
    'usdd','mkusd','crvusd','usdm','dola','cusd','musd','usdc.e','eurc','steur','usd1',
    'usds','usdy','usyc','eutbl','usdgo','ustb','eursafo','jaaa','jtrsy','buidl','rlusd','gho',
    'ylds','usx','u','bfusd','usdf','usd0','usdg','eur'
}
WRAPPED = {'wrapped-bitcoin','wrapped-ether','wrapped-steth','staked-ether','wrapped-eeth',
           'coinbase-wrapped-staked-eth','rocket-pool-eth','mantle-staked-ether','binance-eth'}

filtered = []
for c in markets:
    sym = (c.get('symbol') or '').lower()
    cid = (c.get('id') or '').lower()
    name_lower = (c.get('name') or '').lower()
    if cid in STABLE_IDS or sym in STABLE_SYMS:
        continue
    if sym.startswith('usd') or sym.startswith('eur') or sym.startswith('gbp'):
        continue
    if 'stablecoin' in name_lower or 'heloc' in cid or 'heloc' in name_lower:
        continue
    if cid in WRAPPED or sym in ('wbtc','weth','steth','paxg','xaut'):
        continue
    vol = c.get('total_volume') or 0
    if vol < 1_000_000:
        continue
    # Skip MemeCore (M) - rebranded stablecoin-like low float
    if sym == 'm' and 'memecore' in name_lower:
        continue
    filtered.append(c)

print(f"Filtered count: {len(filtered)}", flush=True)

top100 = [c for c in filtered if c.get('market_cap_rank') and c['market_cap_rank'] <= 100]
green = sum(1 for c in top100 if (c.get('price_change_percentage_24h') or 0) > 0)
changes50 = sorted([c.get('price_change_percentage_24h') or 0 for c in filtered if c.get('market_cap_rank') and c['market_cap_rank'] <= 50])
med50 = statistics.median(changes50) if changes50 else 0

sorted_by_24h = sorted(filtered, key=lambda c: c.get('price_change_percentage_24h') or 0, reverse=True)
winners = sorted_by_24h[:10]
losers = list(reversed(sorted_by_24h[-10:]))

def fmt_num(n):
    if n is None: return "N/A"
    if n >= 1e9: return f"${n/1e9:.2f}B"
    if n >= 1e6: return f"${n/1e6:.1f}M"
    if n >= 1e3: return f"${n/1e3:.1f}K"
    return f"${n:.2f}"

def fmt_price(p):
    if p is None: return "N/A"
    if p >= 1000: return f"${p:,.0f}"
    if p >= 1: return f"${p:.4f}"
    if p >= 0.01: return f"${p:.4f}"
    if p >= 0.0001: return f"${p:.6f}"
    return f"${p:.8f}"

def tags(c, trending_ids):
    cid = c.get('id','')
    p24 = c.get('price_change_percentage_24h') or 0
    p7d = c.get('price_change_percentage_7d_in_currency') or 0
    vol = c.get('total_volume') or 0
    mcap = c.get('market_cap') or 0
    rank = c.get('market_cap_rank') or 999
    is_trending = cid in trending_ids
    t = []
    if is_trending and p24 > 0: t.append('TRENDING+UP')
    if is_trending and p24 < 0: t.append('TRENDING+DOWN')
    if p24 > 15 and p7d > 25: t.append('BREAKOUT')
    elif p24 > 20 and p7d < 0: t.append('FADE')
    if p24 < -10 and mcap > 0 and vol / mcap > 0.25: t.append('CAPITULATION')
    if rank > 150 and p24 > 30: t.append('PUMP-RISK')
    if mcap < 50_000_000 and mcap > 0: t.append('MICROCAP')
    if rank <= 20: t.append('MAJOR')
    return t[:2]

print()
print(f"PULSE: {green}/{len(top100)} top-100 non-stables green | median top-50 24h = {med50:+.2f}%")
print()
print("=== WINNERS ===")
for c in winners:
    t = tags(c, trending_ids)
    tag_str = ' '.join(f'[{x}]' for x in t)
    p24 = c.get('price_change_percentage_24h') or 0
    p7d = c.get('price_change_percentage_7d_in_currency') or 0
    p1h = c.get('price_change_percentage_1h_in_currency') or 0
    print(f"#{c.get('market_cap_rank')} {c['symbol'].upper()} ({c['name']}) {fmt_price(c.get('current_price'))}  24h={p24:+.1f}%  7d={p7d:+.1f}%  1h={p1h:+.1f}%  vol={fmt_num(c.get('total_volume'))}  mcap={fmt_num(c.get('market_cap'))}  {tag_str}")

print()
print("=== LOSERS ===")
for c in losers:
    t = tags(c, trending_ids)
    tag_str = ' '.join(f'[{x}]' for x in t)
    p24 = c.get('price_change_percentage_24h') or 0
    p7d = c.get('price_change_percentage_7d_in_currency') or 0
    p1h = c.get('price_change_percentage_1h_in_currency') or 0
    print(f"#{c.get('market_cap_rank')} {c['symbol'].upper()} ({c['name']}) {fmt_price(c.get('current_price'))}  24h={p24:+.1f}%  7d={p7d:+.1f}%  1h={p1h:+.1f}%  vol={fmt_num(c.get('total_volume'))}  mcap={fmt_num(c.get('market_cap'))}  {tag_str}")

print()
print("=== TRENDING ===")
for t in trending_list[:7]:
    ch = t.get('ch24')
    ch_str = f"{ch:+.1f}%" if ch is not None else "N/A"
    price = t.get('price')
    price_str = fmt_price(price) if price else "N/A"
    print(f"#{t.get('rank')} {t['name']} ({t['symbol']})  {price_str}  24h={ch_str}")
