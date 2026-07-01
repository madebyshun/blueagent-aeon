import urllib.request, json, sys

url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false&price_change_percentage=1h,24h,7d'
try:
    with urllib.request.urlopen(url, timeout=30) as r:
        data = json.loads(r.read())
except Exception as e:
    print(f'ERROR: {e}', file=sys.stderr)
    sys.exit(1)

stablecoin_ids = {
    'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg',
    'binance-usd','frax','gemini-dollar','liquity-usd','pax-dollar','ethena-usde','paypal-usd',
    'alchemix-usd','dola-borrowing-right','usdc','crvusd','usdb','usd0','resolv-usr',
    'tether-eurt','euro-coin','stasis-eurs'
}
stablecoin_sym_prefix = ('USD','EUR','GBP','USDT','USDC','BUSD','DAI','FRAX','TUSD')
wrapped = {
    'wrapped-bitcoin','wrapped-ether','staked-ether','wrapped-steth',
    'rocket-pool-eth','coinbase-wrapped-staked-eth','lido-staked-ether'
}

filtered = []
for c in data:
    sym = c['symbol'].upper()
    cid = c['id']
    name_lower = c['name'].lower()
    if cid in stablecoin_ids or cid in wrapped:
        continue
    if any(sym == s for s in ('USDT','USDC','BUSD','DAI','FRAX','TUSD','USDP','GUSD','LUSD','USDX','SUSD','MUSD','CUSD','ZUSD','EURC','EURS','EURT')):
        continue
    if any(sym.startswith(p) for p in ('USD','EUR','GBP')):
        continue
    if 'stablecoin' in name_lower or 'pegged' in name_lower:
        continue
    vol = c.get('total_volume') or 0
    if vol < 1_000_000:
        continue
    filtered.append(c)

def fmt_price(p):
    if p is None:
        return 'N/A'
    if p >= 1000:
        return f'${p:,.0f}'
    if p >= 1:
        return f'${p:.4g}'
    if p >= 0.001:
        return f'${p:.4f}'
    return f'${p:.6f}'

def fmt_vol(v):
    if v >= 1e9:
        return f'${v/1e9:.2f}B'
    if v >= 1e6:
        return f'${v/1e6:.1f}M'
    return f'${v/1e3:.0f}K'

by_24h = sorted(filtered, key=lambda x: x.get('price_change_percentage_24h') or 0, reverse=True)

print('TOP 15 WINNERS (24h):')
for c in by_24h[:15]:
    p24 = c.get('price_change_percentage_24h') or 0
    p7 = c.get('price_change_percentage_7d_in_currency') or 0
    p1 = c.get('price_change_percentage_1h_in_currency') or 0
    vol = c.get('total_volume') or 0
    mc = c.get('market_cap') or 0
    print(f'{c["market_cap_rank"]:>4}. {c["symbol"].upper():<8} {c["name"][:24]:<25} {fmt_price(c["current_price"]):<14} 24h:{p24:+.1f}%  7d:{p7:+.1f}%  1h:{p1:+.1f}%  vol:{fmt_vol(vol)}  mc:{fmt_vol(mc)}')

print()
print('TOP 15 LOSERS (24h):')
for c in list(reversed(by_24h[-15:])):
    p24 = c.get('price_change_percentage_24h') or 0
    p7 = c.get('price_change_percentage_7d_in_currency') or 0
    p1 = c.get('price_change_percentage_1h_in_currency') or 0
    vol = c.get('total_volume') or 0
    mc = c.get('market_cap') or 0
    print(f'{c["market_cap_rank"]:>4}. {c["symbol"].upper():<8} {c["name"][:24]:<25} {fmt_price(c["current_price"]):<14} 24h:{p24:+.1f}%  7d:{p7:+.1f}%  1h:{p1:+.1f}%  vol:{fmt_vol(vol)}  mc:{fmt_vol(mc)}')

print()
top100 = [c for c in filtered if (c.get('market_cap_rank') or 999) <= 100]
top50 = [c for c in filtered if (c.get('market_cap_rank') or 999) <= 50]
pos = sum(1 for c in top100 if (c.get('price_change_percentage_24h') or 0) > 0)
vals50 = sorted([c.get('price_change_percentage_24h') or 0 for c in top50])
n = len(vals50)
median50 = (vals50[n//2-1]+vals50[n//2])/2 if n%2==0 else vals50[n//2]
print(f'MARKET PULSE: {pos}/{len(top100)} positive in top-100. Median top-50 24h: {median50:+.2f}%')

btc = next((c for c in data if c['id']=='bitcoin'), None)
eth = next((c for c in data if c['id']=='ethereum'), None)
syn = next((c for c in data if c['id']=='synapse-2'), None)
if btc:
    print(f'BTC: ${btc["current_price"]:,.0f} ({btc["price_change_percentage_24h"]:+.2f}%)')
if eth:
    print(f'ETH: ${eth["current_price"]:,.2f} ({eth["price_change_percentage_24h"]:+.2f}%)')
if syn:
    p24 = syn.get('price_change_percentage_24h') or 0
    p7 = syn.get('price_change_percentage_7d_in_currency') or 0
    vol = syn.get('total_volume') or 0
    mc = syn.get('market_cap') or 0
    print(f'SYN (check): rank={syn["market_cap_rank"]} price={fmt_price(syn["current_price"])} 24h:{p24:+.1f}% 7d:{p7:+.1f}% vol:{fmt_vol(vol)} mc:{fmt_vol(mc)}')
