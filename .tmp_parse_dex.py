import json, sys
d = json.load(sys.stdin)
pairs = d.get('pairs', [])[:15]
for p in pairs:
    sym = p.get('baseToken', {}).get('symbol', '?')
    chain = p.get('chainId', '?')
    v24 = p.get('volume', {}).get('h24', 0)
    pc24 = p.get('priceChange', {}).get('h24', 0)
    print(f"{sym} | {chain} | 24h:{pc24:+.1f}% | vol24h:${v24:,.0f}")
