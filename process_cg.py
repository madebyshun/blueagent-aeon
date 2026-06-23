#!/usr/bin/env python3
import json
import statistics

# Load data
with open('/tmp/cg_markets.json', 'r') as f:
    data = json.load(f)

print(f"Total coins loaded: {len(data)}")

# --- FILTERING RULES ---

STABLECOIN_IDS = {
    'tether', 'usd-coin', 'dai', 'usds', 'ethena-usde', 'fdusd', 'tusd', 'usdd',
    'pyusd', 'paxg', 'busd', 'frax', 'figure-heloc', 'stasis-eurs', 'usd1-wlfi',
    'global-dollar', 'ripple-usd', 'blackrock-usd-institutional-digital-liquidity-fund',
    'hashnote-usyc', 'ondo-us-dollar-yield', 'falcon-finance', 'usde', 'tether-gold'
}

STABLECOIN_SYMBOLS = {
    'usdt', 'usdc', 'dai', 'usds', 'usde', 'usdf', 'usdy', 'usyc', 'usd1',
    'rlusd', 'buidl', 'pyusd', 'paxg', 'xaut', 'busd', 'frax', 'usdg'
}

WRAPPED_IDS = {
    'wbtc', 'weth', 'steth', 'reth', 'cbeth', 'wbeth', 'weeth', 'ezeth', 'rseth', 'tbtc'
}

def is_filtered(coin):
    cid = (coin.get('id') or '').lower()
    sym = (coin.get('symbol') or '').lower()
    name = (coin.get('name') or '').lower()
    vol = coin.get('total_volume') or 0

    if cid in STABLECOIN_IDS:
        return True
    if sym in STABLECOIN_SYMBOLS:
        return True
    if sym.startswith('usd') or sym.startswith('eur') or sym.startswith('gbp'):
        return True
    if 'stablecoin' in name:
        return True
    if cid in WRAPPED_IDS:
        return True
    if vol < 1_000_000:
        return True
    return False

filtered = [c for c in data if not is_filtered(c)]
print(f"Filtered coins: {len(filtered)}")

# --- FORMATTING HELPERS ---

def fmt_price(p):
    if p is None:
        return 'N/A'
    if p >= 1000:
        return f"${p:,.2f}"
    elif p >= 1:
        return f"${p:.4f}"
    elif p >= 0.01:
        return f"${p:.5f}"
    else:
        return f"${p:.8f}"

def fmt_large(v):
    if v is None:
        return 'N/A'
    if abs(v) >= 1e9:
        return f"${v/1e9:.2f}B"
    elif abs(v) >= 1e6:
        return f"${v/1e6:.2f}M"
    else:
        return f"${v:,.0f}"

def fmt_pct(p):
    if p is None:
        return 'N/A'
    sign = '+' if p >= 0 else ''
    return f"{sign}{p:.2f}%"

def coin_line(coin, rank=None):
    sym = (coin.get('symbol') or '').upper()
    name = coin.get('name') or ''
    price = coin.get('current_price')
    p24 = coin.get('price_change_percentage_24h_in_currency')
    p7d = coin.get('price_change_percentage_7d_in_currency')
    p1h = coin.get('price_change_percentage_1h_in_currency')
    vol = coin.get('total_volume')
    mcap = coin.get('market_cap')
    rank_str = f"rank={rank}" if rank is not None else f"rank={coin.get('market_cap_rank','?')}"
    return (f"{sym} ({name}) | {rank_str} | price={fmt_price(price)} | "
            f"24h={fmt_pct(p24)} | 7d={fmt_pct(p7d)} | 1h={fmt_pct(p1h)} | "
            f"vol={fmt_large(vol)} | mcap={fmt_large(mcap)}")

# --- STEP 2: Winners and Losers ---

# Sort by 24h change, skip nulls
with_24h = [c for c in filtered if c.get('price_change_percentage_24h_in_currency') is not None]
sorted_24h = sorted(with_24h, key=lambda c: c['price_change_percentage_24h_in_currency'], reverse=True)

top15 = sorted_24h[:15]
bottom15 = sorted_24h[-15:][::-1]  # worst first when reversed

print("\n" + "="*80)
print("TOP 15 WINNERS (24h)")
print("="*80)
for i, c in enumerate(top15, 1):
    print(coin_line(c, rank=i))

print("\n" + "="*80)
print("TOP 15 LOSERS (24h)")
print("="*80)
for i, c in enumerate(bottom15, 1):
    print(coin_line(c, rank=i))

# --- STEP 3: Market breadth (top 100 by market_cap_rank) ---

# Filter to coins ranked 1-100 by market_cap_rank
top100 = [c for c in filtered if c.get('market_cap_rank') is not None and c['market_cap_rank'] <= 100]
top100_sorted = sorted(top100, key=lambda c: c['market_cap_rank'])

total_with_24h = [c for c in top100_sorted if c.get('price_change_percentage_24h_in_currency') is not None]
positive_24h = [c for c in total_with_24h if c['price_change_percentage_24h_in_currency'] > 0]

print(f"\n{'='*80}")
print("STEP 3: MARKET BREADTH (top 100 by market_cap_rank, filtered)")
print("="*80)
print(f"Coins in top 100 (after filter): {len(top100_sorted)}")
print(f"Coins with non-null 24h data: {len(total_with_24h)}")
print(f"Coins with POSITIVE 24h change: {len(positive_24h)}")

# Median 24h of first 50 ranked filtered coins
top50 = top100_sorted[:50]
top50_24h = [c['price_change_percentage_24h_in_currency'] for c in top50 if c.get('price_change_percentage_24h_in_currency') is not None]
if top50_24h:
    med = statistics.median(top50_24h)
    sign = '+' if med >= 0 else ''
    print(f"Median 24h change (first 50 filtered coins): {sign}{med:.2f}%")
    print(f"  (based on {len(top50_24h)} coins with non-null 24h data out of {len(top50)} coins)")

# --- STEP 4: BTC and ETH ---

btc = next((c for c in data if c.get('id') == 'bitcoin'), None)
eth = next((c for c in data if c.get('id') == 'ethereum'), None)

print(f"\n{'='*80}")
print("STEP 4: BTC AND ETH")
print("="*80)
if btc:
    print("BTC:", coin_line(btc))
if eth:
    print("ETH:", coin_line(eth))

# Extra: show all top 100 filtered coins for reference
print(f"\n{'='*80}")
print("ALL TOP-100 FILTERED COINS (by market_cap_rank)")
print("="*80)
for c in top100_sorted:
    print(coin_line(c))
