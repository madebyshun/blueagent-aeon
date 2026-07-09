import json, sys
data = json.load(sys.stdin)
for m in data:
    q = m.get('question','')
    vol24 = m.get('volume24hr',0) or 0
    vol = m.get('volume',0) or 0
    liq = m.get('liquidity',0) or 0
    prices = m.get('outcomePrices','[]')
    end = m.get('endDate','')[:10]
    if vol24 < 1000:
        continue
    print(f'Q: {q[:90]}')
    print(f'  vol24h=${vol24:,.0f} vol=${vol:,.0f} liq=${liq:,.0f} prices={prices} ends={end}')
    print()
