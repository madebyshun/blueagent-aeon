import json

with open('.cg_markets.json') as f:
    coins = json.load(f)

STABLECOINS = {
    'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg',
    'tether-eurt','euro-coin','gemini-dollar','usds','true-usd','paypal-usd','frax','crvusd',
    'bridged-usd-coin-base','usdz-token','tbtc','wbtc','wrapped-bitcoin','staked-ether',
    'wrapped-steth','coinbase-wrapped-btc','renzo-restaked-eth','bedrock-unibtc','kelp-dao-restaked-eth',
    'wrapped-eeth','usd0','usual-usd','mountain-protocol-usdm','reserve-rights-token',
    'ethena-usde','paypal-usd','nusd','tbtc','sbtc','susdx',
}

def is_stable(c):
    if c['id'] in STABLECOINS:
        return True
    sym = (c['symbol'] or '').upper()
    name = (c['name'] or '').lower()
    if sym.startswith(('USD','EUR','GBP')):
        return True
    if 'stablecoin' in name or 'pegged' in name:
        return True
    # wrapped/staked dupes
    if c['id'] in ('staked-ether','wrapped-steth','wrapped-eeth','renzo-restaked-eth',
                   'kelp-dao-restaked-eth','bedrock-unibtc','coinbase-wrapped-btc',
                   'wrapped-bitcoin','tbtc','sbtc'):
        return True
    return False

def fmt_price(p):
    if p is None:
        return 'N/A'
    if p >= 10000:
        return f'${p:,.0f}'
    if p >= 100:
        return f'${p:,.2f}'
    if p >= 1:
        return f'${p:.4g}'
    if p >= 0.01:
        return f'${p:.4f}'
    return f'${p:.6f}'

def fmt_vol(v):
    if v is None:
        return 'N/A'
    if v >= 1e9:
        return f'${v/1e9:.1f}B'
    if v >= 1e6:
        return f'${v/1e6:.0f}M'
    return f'${v/1e3:.0f}K'

def fmt_pct(p):
    if p is None:
        return 'N/A'
    return f'{p:+.1f}%'

filtered = []
for c in coins:
    if is_stable(c):
        continue
    vol = c.get('total_volume') or 0
    if vol < 1_000_000:
        continue
    filtered.append(c)

print(f"Filtered coins: {len(filtered)}")

by_24h = sorted(
    [c for c in filtered if c.get('price_change_percentage_24h_in_currency') is not None],
    key=lambda x: x['price_change_percentage_24h_in_currency']
)

losers = by_24h[:10]
winners = list(reversed(by_24h[-10:]))

def get_tags(c, is_winner=True):
    chg24 = c.get('price_change_percentage_24h_in_currency') or 0
    chg7d = c.get('price_change_percentage_7d_in_currency') or 0
    vol = c.get('total_volume') or 0
    mc = c.get('market_cap') or 0
    rank = c.get('market_cap_rank') or 999
    tags = []
    if is_winner:
        if chg24 > 15 and chg7d > 25:
            tags.append('[BREAKOUT]')
        elif chg24 > 20 and chg7d < 0:
            tags.append('[FADE]')
        if rank > 150 and chg24 > 30:
            tags.append('[PUMP-RISK]')
    else:
        if chg24 < -10 and mc > 0 and (vol / mc) > 0.25:
            tags.append('[CAPITULATION]')
        if rank > 150 and chg24 < -20:
            tags.append('[PUMP-RISK]')
    if mc < 50_000_000 and mc > 0:
        tags.append('[MICROCAP]')
    if rank <= 20:
        tags.append('[MAJOR]')
    return tags[:2]

print("\n=== TOP WINNERS (24h) ===")
for i, c in enumerate(winners, 1):
    chg24 = c.get('price_change_percentage_24h_in_currency')
    chg7d = c.get('price_change_percentage_7d_in_currency')
    chg1h = c.get('price_change_percentage_1h_in_currency')
    tags = get_tags(c, True)
    line = (f"{i}. {c['symbol'].upper()} ({c['name']}) — "
            f"{fmt_price(c['current_price'])}  "
            f"{fmt_pct(chg24)} / 7d {fmt_pct(chg7d)} / 1h {fmt_pct(chg1h)}  "
            f"vol:{fmt_vol(c.get('total_volume'))} mcap:{fmt_vol(c.get('market_cap'))} #{c.get('market_cap_rank')}  "
            f"{' '.join(tags)}")
    print(line)

print("\n=== TOP LOSERS (24h) ===")
for i, c in enumerate(losers, 1):
    chg24 = c.get('price_change_percentage_24h_in_currency')
    chg7d = c.get('price_change_percentage_7d_in_currency')
    chg1h = c.get('price_change_percentage_1h_in_currency')
    tags = get_tags(c, False)
    line = (f"{i}. {c['symbol'].upper()} ({c['name']}) — "
            f"{fmt_price(c['current_price'])}  "
            f"{fmt_pct(chg24)} / 7d {fmt_pct(chg7d)} / 1h {fmt_pct(chg1h)}  "
            f"vol:{fmt_vol(c.get('total_volume'))} mcap:{fmt_vol(c.get('market_cap'))} #{c.get('market_cap_rank')}  "
            f"{' '.join(tags)}")
    print(line)

# Market commentary
top100 = [c for c in filtered if c.get('market_cap_rank') and c['market_cap_rank'] <= 100]
green100 = [c for c in top100 if (c.get('price_change_percentage_24h_in_currency') or 0) > 0]
changes_top50 = sorted([c.get('price_change_percentage_24h_in_currency') or 0
                        for c in sorted(top100, key=lambda x: x['market_cap_rank'])[:50]])
mid = len(changes_top50) // 2
median_50 = changes_top50[mid] if changes_top50 else 0

print(f"\n=== MARKET PULSE ===")
print(f"Green in top 100: {len(green100)}/{len(top100)}")
print(f"Median 24h change (top 50): {median_50:+.2f}%")

# BTC price for reference
btc = next((c for c in coins if c['id'] == 'bitcoin'), None)
if btc:
    print(f"BTC: {fmt_price(btc['current_price'])} {fmt_pct(btc.get('price_change_percentage_24h_in_currency'))}")
