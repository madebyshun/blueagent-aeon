#!/usr/bin/env python3
import json, sys

STABLECOINS = {
    'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg',
    'frax','true-usd','liquity-usd','ethena-usde','usds','usual-usd',
    'blackrock-usd-institutional-digital-liquidity-fund',
}
STABLE_SYMS = {'usdt','usdc','dai','tusd','usdd','fdusd','pyusd','gusd','usdp','usde','usds','eurc','eurs','paxg','frax','lusd','susd','crvusd','mkusd','gho'}
WRAPPED = {'wbtc','weth','steth','cbbtc','reth','weeth','solvbtc','hbtc','lbtc'}

markets_file = sys.argv[1]
trending_file = sys.argv[2]

with open(markets_file) as f:
    content = f.read()
start = content.find('[')
data = json.loads(content[start:])

with open(trending_file) as f:
    content2 = f.read()
start2 = content2.find('{')
trend_data = json.loads(content2[start2:])

# --- Filter ---
filtered = []
for c in data:
    cid = c.get('id','')
    sym = (c.get('symbol') or '').lower()
    name = (c.get('name') or '').lower()
    vol = c.get('total_volume') or 0
    if cid in STABLECOINS: continue
    if sym in STABLE_SYMS: continue
    if sym in WRAPPED: continue
    if 'stablecoin' in name: continue
    if sym.startswith('usd') or sym.startswith('eur') or sym.startswith('gbp'): continue
    if 'tether' in name or 'usd coin' in name: continue
    if vol < 1_000_000: continue
    filtered.append(c)

# --- Trending symbols ---
trend_coins = trend_data.get('coins', [])[:7]
trend_syms = {entry['item']['symbol'].lower() for entry in trend_coins}
trend_ids = {entry['item']['id'].lower() for entry in trend_coins if 'id' in entry['item']}

# --- Winners / Losers ---
by24h = sorted(
    [c for c in filtered if c.get('price_change_percentage_24h_in_currency') is not None],
    key=lambda x: x['price_change_percentage_24h_in_currency']
)
winners = list(reversed(by24h[-10:]))
losers = by24h[:10]

def fmt_price(p):
    if p is None: return 'N/A'
    if p >= 1000: return f"${p:,.0f}"
    if p >= 100: return f"${p:.2f}"
    if p >= 1: return f"${p:.3f}"
    if p >= 0.01: return f"${p:.4f}"
    return f"${p:.6f}"

def fmt_vol(v):
    if v is None: return 'N/A'
    if v >= 1e9: return f"${v/1e9:.1f}B"
    if v >= 1e6: return f"${v/1e6:.0f}M"
    return f"${v/1e3:.0f}K"

def pct(v):
    if v is None: return "N/A"
    sign = "+" if v >= 0 else ""
    return f"{sign}{v:.1f}%"

def get_tags(c, is_winner, trending_syms):
    sym = c['symbol'].lower()
    cid = c.get('id','').lower()
    p24 = c.get('price_change_percentage_24h_in_currency') or 0
    p7d = c.get('price_change_percentage_7d_in_currency') or 0
    vol = c.get('total_volume') or 0
    mcap = c.get('market_cap') or 1
    rank = c.get('market_cap_rank') or 999
    vol_mcap = vol / mcap if mcap > 0 else 0
    tags = []
    in_trending = (sym in trending_syms or cid in trend_ids)
    if is_winner:
        if in_trending: tags.append('[TRENDING+UP]')
        if p24 > 15 and p7d > 25: tags.append('[BREAKOUT]')
        elif p24 > 20 and p7d < 0: tags.append('[FADE]')
        if rank > 150 and p24 > 30: tags.append('[PUMP-RISK]')
        if mcap < 50_000_000: tags.append('[MICROCAP]')
        if rank <= 20: tags.append('[MAJOR]')
    else:
        if in_trending: tags.append('[TRENDING+DOWN]')
        if p24 < -10 and vol_mcap > 0.25: tags.append('[CAPITULATION]')
        if rank <= 20: tags.append('[MAJOR]')
        if mcap < 50_000_000: tags.append('[MICROCAP]')
    return tags[:2]

# --- Market pulse ---
top100 = [c for c in filtered if (c.get('market_cap_rank') or 999) <= 100]
green = sum(1 for c in top100 if (c.get('price_change_percentage_24h_in_currency') or 0) > 0)
top50 = [c for c in filtered if (c.get('market_cap_rank') or 999) <= 50]
p50s = sorted([c.get('price_change_percentage_24h_in_currency') or 0 for c in top50])
median50 = p50s[len(p50s)//2] if p50s else 0

print(f"PULSE|{green}|{len(top100)}|{median50:.1f}")

# --- Output winners ---
print("WINNERS")
for i, c in enumerate(winners, 1):
    sym = c['symbol'].upper()
    name = c['name']
    p24 = c.get('price_change_percentage_24h_in_currency') or 0
    p7d = c.get('price_change_percentage_7d_in_currency')
    p1h = c.get('price_change_percentage_1h_in_currency')
    vol = c.get('total_volume') or 0
    mcap = c.get('market_cap') or 0
    rank = c.get('market_cap_rank') or 999
    price = c.get('current_price')
    tags = get_tags(c, True, trend_syms)
    p7d_str = pct(p7d) if p7d is not None else "N/A"
    p1h_str = pct(p1h) if p1h is not None else "N/A"
    tag_str = ' '.join(tags)
    print(f"{i}|{sym}|{name}|{fmt_price(price)}|{pct(p24)}|{p7d_str}|{p1h_str}|{fmt_vol(vol)}|{rank}|{tag_str}|{vol/max(mcap,1):.2f}")

# --- Output losers ---
print("LOSERS")
for i, c in enumerate(losers, 1):
    sym = c['symbol'].upper()
    name = c['name']
    p24 = c.get('price_change_percentage_24h_in_currency') or 0
    p7d = c.get('price_change_percentage_7d_in_currency')
    p1h = c.get('price_change_percentage_1h_in_currency')
    vol = c.get('total_volume') or 0
    mcap = c.get('market_cap') or 0
    rank = c.get('market_cap_rank') or 999
    price = c.get('current_price')
    tags = get_tags(c, False, trend_syms)
    p7d_str = pct(p7d) if p7d is not None else "N/A"
    p1h_str = pct(p1h) if p1h is not None else "N/A"
    tag_str = ' '.join(tags)
    print(f"{i}|{sym}|{name}|{fmt_price(price)}|{pct(p24)}|{p7d_str}|{p1h_str}|{fmt_vol(vol)}|{rank}|{tag_str}|{vol/max(mcap,1):.2f}")

# --- Trending ---
print("TRENDING")
for i, entry in enumerate(trend_coins, 1):
    item = entry.get('item', {})
    name = item.get('name','')
    sym = (item.get('symbol') or '').upper()
    rank = item.get('market_cap_rank','N/A')
    d = item.get('data', {})
    price = d.get('price')
    p24 = d.get('price_change_percentage_24h', {}).get('usd')
    # check if also a winner or loser
    sym_l = sym.lower()
    winner_syms = {c['symbol'].lower() for c in winners}
    loser_syms = {c['symbol'].lower() for c in losers}
    tags = []
    if sym_l in winner_syms: tags.append('[TRENDING+UP]')
    if sym_l in loser_syms: tags.append('[TRENDING+DOWN]')
    price_str = f"${price:.4f}" if price and price < 1 else (f"${price:.2f}" if price else "N/A")
    p24_str = pct(p24) if p24 is not None else "N/A"
    tag_str = ' '.join(tags)
    print(f"{i}|{name}|{sym}|{rank}|{price_str}|{p24_str}|{tag_str}")
