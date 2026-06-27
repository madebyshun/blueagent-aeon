import json

STABLECOIN_IDS = {
    'tether', 'usd-coin', 'dai', 'first-digital-usd', 'usde', 'tusd', 'usdd', 'pyusd', 'fdusd',
    'paxg', 'usdt', 'usdc', 'busd', 'frax', 'mim', 'lusd', 'crvusd', 'usdb', 'usds', 'usdx',
    'usd-plus', 'eur-coin', 'steur', 'nusd', 'usdr', 'usde', 'sky', 'usual', 'resolv',
    'savings-dai', 'sdai', 'susd', 'gusd', 'husd', 'musd', 'ousd', 'usdm', 'usdy', 'cusd'
}
WRAPPED_IDS = {'wbtc', 'weth', 'steth', 'cbeth', 'weeth', 'reth', 'wsteth', 'lseth', 'wsol'}

with open('/home/runner/work/blueagent-aeon/blueagent-aeon/.cg_markets_tmp.json') as f:
    coins = json.load(f)

print(f"Total coins fetched: {len(coins)}")

def is_stablecoin(c):
    if c['id'] in STABLECOIN_IDS:
        return True
    sym = c['symbol'].upper()
    name = c['name'].lower()
    if sym.startswith('USD') or sym.startswith('EUR') or sym.startswith('GBP'):
        return True
    if 'stablecoin' in name:
        return True
    return False

def get24(c):
    v = c.get('price_change_percentage_24h_in_currency')
    if v is None:
        v = c.get('price_change_percentage_24h')
    return v or 0

def get7d(c):
    return c.get('price_change_percentage_7d_in_currency') or 0

def get1h(c):
    return c.get('price_change_percentage_1h_in_currency') or 0

# Filter
filtered = []
for c in coins:
    if is_stablecoin(c):
        continue
    if c['id'] in WRAPPED_IDS:
        continue
    vol = c.get('total_volume') or 0
    if vol < 1_000_000:
        continue
    ch24 = get24(c)
    filtered.append(c)

print(f"After filters: {len(filtered)} coins")

sorted_by_24h = sorted(filtered, key=get24, reverse=True)
winners = sorted_by_24h[:10]
losers = sorted_by_24h[-10:][::-1]

def fmt_price(p):
    if p is None:
        return "$?"
    if p >= 1000:
        return f"${p:,.0f}"
    elif p >= 1:
        return f"${p:.4g}"
    elif p >= 0.01:
        return f"${p:.4f}"
    else:
        return f"${p:.6f}"

def fmt_vol(v):
    if v >= 1e9:
        return f"${v/1e9:.1f}B"
    elif v >= 1e6:
        return f"${v/1e6:.0f}M"
    else:
        return f"${v/1e3:.0f}K"

def fmt_mcap(m):
    if not m:
        return "?"
    if m >= 1e9:
        return f"${m/1e9:.1f}B"
    else:
        return f"${m/1e6:.0f}M"

print("\n=== TOP 10 WINNERS (24h) ===")
for c in winners:
    mcap = c.get('market_cap') or 0
    vol = c.get('total_volume') or 0
    rank = c['market_cap_rank'] or 999
    print(f"  #{rank:<4}  {c['symbol'].upper():<8}  {fmt_price(c['current_price']):<14}  24h:{get24(c):+.1f}%  7d:{get7d(c):+.1f}%  1h:{get1h(c):+.1f}%  vol:{fmt_vol(vol)}  mcap:{fmt_mcap(mcap)}")

print("\n=== TOP 10 LOSERS (24h) ===")
for c in losers:
    mcap = c.get('market_cap') or 0
    vol = c.get('total_volume') or 0
    rank = c['market_cap_rank'] or 999
    print(f"  #{rank:<4}  {c['symbol'].upper():<8}  {fmt_price(c['current_price']):<14}  24h:{get24(c):+.1f}%  7d:{get7d(c):+.1f}%  1h:{get1h(c):+.1f}%  vol:{fmt_vol(vol)}  mcap:{fmt_mcap(mcap)}")

# Market pulse
top100 = [c for c in filtered if (c['market_cap_rank'] or 999) <= 100]
print(f"\n=== MARKET PULSE ===")
print(f"  Filtered top-100 count: {len(top100)}")
green = [c for c in top100 if get24(c) > 0]
red = [c for c in top100 if get24(c) < 0]
changes = sorted([get24(c) for c in top100])
median_change = changes[len(changes)//2] if changes else 0
print(f"  Green: {len(green)}/{len(top100)}, Red: {len(red)}")
print(f"  Median 24h (top-100): {median_change:+.2f}%")

top50 = [c for c in filtered if (c['market_cap_rank'] or 999) <= 50]
top50_changes = sorted([get24(c) for c in top50])
median_top50 = top50_changes[len(top50_changes)//2] if top50_changes else 0
print(f"  Median 24h (top-50): {median_top50:+.2f}%")

# Build lookup for trending cross-check
all_by_id = {c['id']: c for c in filtered}
all_by_sym = {c['symbol'].upper(): c for c in filtered}
print("\n=== SIGNAL TAGS (winners) ===")
winner_ids = {c['id'] for c in winners}
loser_ids = {c['id'] for c in losers}
winner_syms = {c['symbol'].upper() for c in winners}
loser_syms = {c['symbol'].upper() for c in losers}

for c in winners + losers:
    tags = []
    rank = c['market_cap_rank'] or 999
    ch24 = get24(c)
    ch7d = get7d(c)
    mcap = c.get('market_cap') or 0
    vol = c.get('total_volume') or 0

    if ch24 > 15 and ch7d > 25:
        tags.append("BREAKOUT")
    if ch24 > 20 and ch7d < 0:
        tags.append("FADE")
    if ch24 < -10 and mcap > 0 and vol / mcap > 0.25:
        tags.append("CAPITULATION")
    if rank > 150 and ch24 > 30:
        tags.append("PUMP-RISK")
    if mcap < 50_000_000:
        tags.append("MICROCAP")
    if rank <= 20:
        tags.append("MAJOR")

    print(f"  {c['symbol'].upper()}: {tags}")
