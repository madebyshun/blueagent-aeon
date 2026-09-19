import json, sys

data = json.load(sys.stdin)

STABLECOINS = {'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg','usdt','usdc','busd','frax','gusd','lusd','eurs','usds'}
STABLECOIN_SYMS = {'USDT','USDC','BUSD','DAI','FRAX','TUSD','USDD','PYUSD','FDUSD','PAXG','GUSD','LUSD','EURS'}
WRAPPED = {'wbtc','weth','steth','cbeth','reth','wsteth','weeth'}

filtered = []
for c in data:
    if c['id'] in STABLECOINS or c['id'] in WRAPPED:
        continue
    sym = c['symbol'].upper()
    if sym in STABLECOIN_SYMS:
        continue
    if sym.startswith(('USD','EUR','GBP')):
        continue
    if 'stablecoin' in (c['name'] or '').lower():
        continue
    vol = c.get('total_volume') or 0
    if vol < 1_000_000:
        continue
    filtered.append(c)

winners = sorted([c for c in filtered if (c.get('price_change_percentage_24h_in_currency') or 0) > 0],
                 key=lambda x: x.get('price_change_percentage_24h_in_currency') or 0, reverse=True)[:10]
losers = sorted([c for c in filtered if (c.get('price_change_percentage_24h_in_currency') or 0) < 0],
                key=lambda x: x.get('price_change_percentage_24h_in_currency') or 0)[:10]

def fmt(c):
    p24 = c.get('price_change_percentage_24h_in_currency') or 0
    p7 = c.get('price_change_percentage_7d_in_currency') or 0
    p1 = c.get('price_change_percentage_1h_in_currency') or 0
    vol = c.get('total_volume') or 0
    mcap = c.get('market_cap') or 0
    rank = c.get('market_cap_rank') or 0
    price = c.get('current_price') or 0
    vol_ratio = vol/mcap if mcap > 0 else 0
    return f"{c['symbol'].upper()}|{c['name']}|{rank}|{price}|{p24:.2f}|{p7:.2f}|{p1:.2f}|{vol:.0f}|{mcap:.0f}|{vol_ratio:.3f}"

print('=== WINNERS ===')
for c in winners:
    print(fmt(c))
print('=== LOSERS ===')
for c in losers:
    print(fmt(c))

top100 = sorted(filtered, key=lambda x: x.get('market_cap_rank') or 999)[:100]
green = sum(1 for c in top100 if (c.get('price_change_percentage_24h_in_currency') or 0) > 0)
changes50 = sorted([c.get('price_change_percentage_24h_in_currency') or 0 for c in sorted(filtered, key=lambda x: x.get('market_cap_rank') or 999)[:50]])
median = changes50[len(changes50)//2] if changes50 else 0
print('=== PULSE ===')
print(f'green={green}/100 median_top50={median:.1f}')
