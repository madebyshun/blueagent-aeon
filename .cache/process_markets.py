import json, sys

data = json.load(sys.stdin)
print(f'Total coins: {len(data)}')

STABLE_IDS = {'tether','usd-coin','dai','first-digital-usd','ethena-usde','tusd','usdd','paypal-usd','frax','usdb','binance-peg-usd','tron-bsc-bridged-usdt','true-usd','pax-gold','tether-gold','mxnt','mxnc','nusd','stasis-eurs','ceur','biusd','par-stablecoin','mim','alchemix-usd'}
STABLE_SYMBOLS = {'USDT','USDC','DAI','BUSD','TUSD','USDD','USDP','GUSD','FRAX','LUSD','PYUSD','FDUSD','PAXG','XAUT','EURT','EURS','USDE','CRVUSD','SUSD'}
WRAPPED_SYMS = {'wbtc','weth','steth','cbeth','reth','wbeth','weeth','beth'}

def is_stable(c):
    if c['id'] in STABLE_IDS:
        return True
    sym = c['symbol'].upper()
    if sym in STABLE_SYMBOLS:
        return True
    if sym.startswith(('USD','EUR','GBP','AUD','JPY','KRW')):
        return True
    if 'stablecoin' in c['name'].lower():
        return True
    return False

def is_wrapped_dup(c):
    return c['symbol'].lower() in WRAPPED_SYMS

def pct24(c):
    v = c.get('price_change_percentage_24h_in_currency') or c.get('price_change_percentage_24h') or 0
    return v if v is not None else 0

def pct1h(c):
    v = c.get('price_change_percentage_1h_in_currency') or 0
    return v if v is not None else 0

def pct7d(c):
    v = c.get('price_change_percentage_7d_in_currency') or 0
    return v if v is not None else 0

filtered = [c for c in data if not is_stable(c) and not is_wrapped_dup(c) and c.get('total_volume') is not None and c['total_volume'] >= 1_000_000]
print(f'After filter: {len(filtered)}')

sorted_by24h = sorted(filtered, key=pct24)
losers = sorted_by24h[:10]
winners = list(reversed(sorted_by24h[-10:]))

print('\n=== TOP WINNERS (24h) ===')
for c in winners:
    rank = c['market_cap_rank'] or 999
    price = c['current_price']
    p24h = pct24(c)
    p7d = pct7d(c)
    p1h = pct1h(c)
    vol = c['total_volume']
    mc = c['market_cap'] or 0
    vol_fmt = f"${vol/1e9:.2f}B" if vol >= 1e9 else f"${vol/1e6:.0f}M"
    mc_fmt = f"${mc/1e9:.1f}B" if mc >= 1e9 else f"${mc/1e6:.0f}M"
    print(f"{c['symbol'].upper()} ({c['name']}) rank#{rank} ${price} 24h:{p24h:+.1f}% 7d:{p7d:+.1f}% 1h:{p1h:+.1f}% vol:{vol_fmt} mcap:{mc_fmt}")

print('\n=== TOP LOSERS (24h) ===')
for c in losers:
    rank = c['market_cap_rank'] or 999
    price = c['current_price']
    p24h = pct24(c)
    p7d = pct7d(c)
    p1h = pct1h(c)
    vol = c['total_volume']
    mc = c['market_cap'] or 0
    vol_fmt = f"${vol/1e9:.2f}B" if vol >= 1e9 else f"${vol/1e6:.0f}M"
    mc_fmt = f"${mc/1e9:.1f}B" if mc >= 1e9 else f"${mc/1e6:.0f}M"
    print(f"{c['symbol'].upper()} ({c['name']}) rank#{rank} ${price} 24h:{p24h:+.1f}% 7d:{p7d:+.1f}% 1h:{p1h:+.1f}% vol:{vol_fmt} mcap:{mc_fmt}")

top100 = [c for c in filtered if (c['market_cap_rank'] or 999) <= 100]
green = sum(1 for c in top100 if pct24(c) > 0)
top50_changes = sorted([pct24(c) for c in filtered if (c['market_cap_rank'] or 999) <= 50])
median50 = top50_changes[len(top50_changes)//2] if top50_changes else 0

btc = next((c for c in data if c['id'] == 'bitcoin'), None)
btc_pct = pct24(btc) if btc else 0
btc_price = btc['current_price'] if btc else 0

print('\n=== MARKET PULSE ===')
print(f'Top-100 green: {green}/{len(top100)}')
print(f'Median 24h (top-50): {median50:+.1f}%')
print(f'BTC: ${btc_price:,.0f} {btc_pct:+.2f}%')

print('\n=== ALL COINS DATA (for tag computation) ===')
for c in sorted_by24h:
    rank = c['market_cap_rank'] or 999
    mc = c['market_cap'] or 0
    vol = c['total_volume']
    p24h = pct24(c)
    p7d = pct7d(c)
    tags = []
    if rank > 150 and p24h > 30:
        tags.append('PUMP-RISK')
    if p24h > 15 and p7d > 25:
        tags.append('BREAKOUT')
    if p24h > 20 and p7d < 0:
        tags.append('FADE')
    if p24h < -10 and mc > 0 and vol/mc > 0.25:
        tags.append('CAPITULATION')
    if mc < 50_000_000:
        tags.append('MICROCAP')
    if rank <= 20:
        tags.append('MAJOR')
    if tags:
        print(f"{c['symbol'].upper()} rank#{rank} 24h:{p24h:+.1f}% 7d:{p7d:+.1f}% vol/mc:{vol/mc:.2f} tags:{','.join(tags)}")
