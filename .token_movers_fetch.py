import urllib.request
import json

url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false&price_change_percentage=1h,24h,7d'
with urllib.request.urlopen(url, timeout=30) as r:
    data = json.loads(r.read())

STABLECOINS = {
    'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg',
    'usds','frax','gusd','usdt','busd','susd','husd','eurs','stasis-eurs','ageur','usd-plus',
    'crvusd','mkusd','dola','rai','lusd','eurc','noble-usd'
}
WRAPPED = {'wbtc','weth','steth','wsteth','cbeth','reth','sfrxeth','weeth','ezeth','rseth'}

def is_stable(coin):
    sym = coin['symbol'].upper()
    name = coin['name'].lower()
    if coin['id'] in STABLECOINS:
        return True
    if sym.startswith(('USD','EUR','GBP')):
        return True
    if 'stablecoin' in name or 'usd' in name.split():
        return True
    return False

def is_wrapped(coin):
    return coin['id'] in WRAPPED

def ch24(c):
    v = c.get('price_change_percentage_24h_in_currency')
    if v is None:
        v = c.get('price_change_percentage_24h')
    return v or 0

def ch7d(c):
    v = c.get('price_change_percentage_7d_in_currency')
    return v or 0

def ch1h(c):
    v = c.get('price_change_percentage_1h_in_currency')
    return v or 0

def fmt_price(p):
    if p is None:
        return 'N/A'
    if p >= 1000:
        return f'${p:,.0f}'
    elif p >= 1:
        return f'${p:.4f}'
    elif p >= 0.0001:
        return f'${p:.6f}'
    else:
        return f'${p:.8f}'

def fmt_vol(v):
    if v >= 1e9:
        return f'${v/1e9:.1f}B'
    elif v >= 1e6:
        return f'${v/1e6:.0f}M'
    else:
        return f'${v/1e3:.0f}K'

def fmt_mcap(m):
    if m >= 1e9:
        return f'${m/1e9:.1f}B'
    elif m >= 1e6:
        return f'${m/1e6:.0f}M'
    else:
        return f'${m/1e3:.0f}K'

filtered = [c for c in data
            if not is_stable(c)
            and not is_wrapped(c)
            and (c.get('total_volume') or 0) >= 1_000_000]

print(f"STATS: total={len(data)}, filtered={len(filtered)}")

sorted_24h = sorted(filtered, key=lambda c: ch24(c), reverse=True)

print("\nTOP_WINNERS")
for c in sorted_24h[:12]:
    print(f"SYM={c['symbol'].upper()} NAME={c['name']} RANK={c['market_cap_rank']} PRICE={fmt_price(c['current_price'])} CH24={ch24(c):.1f} CH7D={ch7d(c):.1f} CH1H={ch1h(c):.1f} VOL={fmt_vol(c['total_volume'] or 0)} MCAP={fmt_mcap(c['market_cap'] or 0)} RAWVOL={c['total_volume'] or 0} RAWMCAP={c['market_cap'] or 0}")

print("\nTOP_LOSERS")
for c in sorted_24h[-12:]:
    print(f"SYM={c['symbol'].upper()} NAME={c['name']} RANK={c['market_cap_rank']} PRICE={fmt_price(c['current_price'])} CH24={ch24(c):.1f} CH7D={ch7d(c):.1f} CH1H={ch1h(c):.1f} VOL={fmt_vol(c['total_volume'] or 0)} MCAP={fmt_mcap(c['market_cap'] or 0)} RAWVOL={c['total_volume'] or 0} RAWMCAP={c['market_cap'] or 0}")

top100 = [c for c in filtered if (c.get('market_cap_rank') or 999) <= 100]
positive = sum(1 for c in top100 if ch24(c) > 0)
ch24_100 = sorted([ch24(c) for c in top100])
median_100 = ch24_100[len(ch24_100)//2] if ch24_100 else 0

top50 = [c for c in filtered if (c.get('market_cap_rank') or 999) <= 50]
ch24_50 = sorted([ch24(c) for c in top50])
median_50 = ch24_50[len(ch24_50)//2] if ch24_50 else 0

print(f"\nMARKET_PULSE: top100_positive={positive}/{len(top100)} median100={median_100:.1f} median50={median_50:.1f}")
