import sys, json

data = json.load(sys.stdin)

STABLECOINS = {'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg','usds','ethena-usde','usual-usd','frax'}
WRAPPED = {'wrapped-bitcoin','wrapped-ether','staked-ether','wrapped-steth','lido-staked-ether'}

filtered = []
for c in data:
    sid = c.get('id','')
    sym = c.get('symbol','').upper()
    name = c.get('name','').lower()
    vol = c.get('total_volume') or 0
    if sid in STABLECOINS or sid in WRAPPED:
        continue
    if sym.startswith(('USD','EUR','GBP')) or 'stablecoin' in name:
        continue
    if vol < 1_000_000:
        continue
    filtered.append(c)

sorted_up = sorted(filtered, key=lambda x: x.get('price_change_percentage_24h_in_currency') or 0, reverse=True)
sorted_dn = sorted(filtered, key=lambda x: x.get('price_change_percentage_24h_in_currency') or 0)

top10_winners = sorted_up[:10]
top10_losers = sorted_dn[:10]

def abbrev(n):
    if n >= 1e9: return f'${n/1e9:.1f}B'
    if n >= 1e6: return f'${n/1e6:.0f}M'
    return f'${n:.0f}'

def fmt_price(price):
    if price >= 1:
        return f'${price:,.4g}'
    elif price >= 0.01:
        return f'${price:.4f}'
    else:
        return f'${price:.6f}'

print('=== WINNERS ===')
for c in top10_winners:
    sym = c.get('symbol','').upper()
    name = c.get('name','')
    rank = c.get('market_cap_rank')
    price = c.get('current_price',0)
    ch24 = c.get('price_change_percentage_24h_in_currency') or 0
    ch7d = c.get('price_change_percentage_7d_in_currency') or 0
    ch1h = c.get('price_change_percentage_1h_in_currency') or 0
    vol = c.get('total_volume') or 0
    mcap = c.get('market_cap') or 0
    print(f"{sym}|{name}|{rank}|{fmt_price(price)}|{ch24:+.1f}%|{ch7d:+.1f}%|{ch1h:+.1f}%|{abbrev(vol)}|{abbrev(mcap)}")

print()
print('=== LOSERS ===')
for c in top10_losers:
    sym = c.get('symbol','').upper()
    name = c.get('name','')
    rank = c.get('market_cap_rank')
    price = c.get('current_price',0)
    ch24 = c.get('price_change_percentage_24h_in_currency') or 0
    ch7d = c.get('price_change_percentage_7d_in_currency') or 0
    ch1h = c.get('price_change_percentage_1h_in_currency') or 0
    vol = c.get('total_volume') or 0
    mcap = c.get('market_cap') or 0
    print(f"{sym}|{name}|{rank}|{fmt_price(price)}|{ch24:+.1f}%|{ch7d:+.1f}%|{ch1h:+.1f}%|{abbrev(vol)}|{abbrev(mcap)}")

top100 = filtered[:100]
positives = sum(1 for c in top100 if (c.get('price_change_percentage_24h_in_currency') or 0) > 0)
top50_changes = sorted([c.get('price_change_percentage_24h_in_currency') or 0 for c in filtered[:50]])
median_50 = top50_changes[25] if len(top50_changes) >= 26 else 0
print()
print(f'=== PULSE ===')
print(f'{positives}/100 positive, median top-50: {median_50:+.2f}%')

print()
print('=== WINNER_IDS ===')
for c in top10_winners:
    print(c.get('id',''))
print()
print('=== LOSER_IDS ===')
for c in top10_losers:
    print(c.get('id',''))
