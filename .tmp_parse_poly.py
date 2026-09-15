import json, sys
events = json.load(sys.stdin)
for e in events[:20]:
    title = e.get('title', e.get('question','?'))[:90]
    vol24 = e.get('volume24hr', 0) or 0
    end_date = e.get('endDate') or e.get('end_date') or '?'
    end = end_date[:10] if end_date != '?' else '?'
    markets = e.get('markets', [])
    if markets:
        m = markets[0]
        outcomes = m.get('outcomePrices', '[]')
        q = m.get('question', title)[:90]
        print(f'"{q}" | vol24h:${float(vol24):,.0f} | ends:{end} | outcomes:{outcomes}')
    else:
        print(f'"{title}" | vol24h:${float(vol24):,.0f} | ends:{end}')
