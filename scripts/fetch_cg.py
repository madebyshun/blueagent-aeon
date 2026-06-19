import urllib.request, json, sys

STAB_IDS = {'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg','frax','lusd','usdy','usdb','eurc','stasis-eurs','true-usd','binance-usd','gemini-dollar','wrapped-bitcoin','wrapped-eeth','wrapped-steth','staked-ether','rocket-pool-eth'}
STAB_SYMS = {'usdt','usdc','dai','fdusd','usde','tusd','usdd','pyusd','paxg','gusd','frax','susd','busd','musd','lusd','ceur','eurs','usdb','usdy'}

def is_stablecoin(c):
    sym = c['symbol'].lower()
    cid = c['id'].lower()
    name = c['name'].lower()
    if sym in STAB_SYMS: return True
    if cid in STAB_IDS: return True
    if any(x in name for x in ['stablecoin','pegged','wrapped usd']): return True
    if sym.startswith(('usd','eur','gbp')): return True
    return False

def is_wrapped_dupe(c):
    sym = c['symbol'].lower()
    return sym in {'wbtc','weth','steth','reth','wsteth','cbeth','wbeth','frxeth'}

def fmt_vol(v):
    if v >= 1e9: return f"${v/1e9:.1f}B"
    if v >= 1e6: return f"${v/1e6:.0f}M"
    return f"${v/1e3:.0f}K"

def fmt_price(p):
    if p >= 1000: return f"${p:,.0f}"
    if p >= 1: return f"${p:.4g}"
    if p >= 0.01: return f"${p:.4f}"
    return f"${p:.6f}"

url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false&price_change_percentage=1h,24h,7d'
try:
    with urllib.request.urlopen(url, timeout=20) as r:
        data = json.loads(r.read())
except Exception as e:
    print(f"FETCH_ERROR: {e}", file=sys.stderr)
    sys.exit(1)

filtered = [c for c in data
            if not is_stablecoin(c)
            and not is_wrapped_dupe(c)
            and (c.get('total_volume') or 0) >= 1_000_000
            and c.get('price_change_percentage_24h_in_currency') is not None]

winners = sorted(filtered, key=lambda c: c['price_change_percentage_24h_in_currency'], reverse=True)[:12]
losers = sorted(filtered, key=lambda c: c['price_change_percentage_24h_in_currency'])[:12]

def coin_line(c):
    p1h = c.get('price_change_percentage_1h_in_currency') or 0
    p24 = c.get('price_change_percentage_24h_in_currency') or 0
    p7d = c.get('price_change_percentage_7d_in_currency') or 0
    vol = c.get('total_volume') or 0
    mcap = c.get('market_cap') or 0
    rank = c.get('market_cap_rank') or 0
    price = c.get('current_price') or 0
    return f"{rank}|{c['symbol'].upper()}|{c['name']}|{fmt_price(price)}|{p1h:.2f}|{p24:.2f}|{p7d:.2f}|{fmt_vol(vol)}|{fmt_vol(mcap)}"

print("WINNERS")
for c in winners:
    print(coin_line(c))

print("LOSERS")
for c in losers:
    print(coin_line(c))

top100 = [c for c in filtered if (c.get('market_cap_rank') or 999) <= 100]
pos = sum(1 for c in top100 if (c.get('price_change_percentage_24h_in_currency') or 0) > 0)
neg = len(top100) - pos
top50_changes = sorted([c.get('price_change_percentage_24h_in_currency',0) for c in filtered if (c.get('market_cap_rank') or 999) <= 50])
median50 = top50_changes[len(top50_changes)//2] if top50_changes else 0

print(f"PULSE|top100={pos}+/{neg}-|median50={median50:.2f}")

winner_ids = {c['id'] for c in winners}
loser_ids = {c['id'] for c in losers}
print(f"WINNER_IDS|{','.join(c['id']+'='+f\"{c.get('price_change_percentage_24h_in_currency',0):.1f}\" for c in winners)}")
print(f"LOSER_IDS|{','.join(c['id']+'='+f\"{c.get('price_change_percentage_24h_in_currency',0):.1f}\" for c in losers)}")
