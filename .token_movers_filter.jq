def stablecoin_ids: ["tether","usd-coin","dai","first-digital-usd","usde","tusd","usdd","pyusd","fdusd","paxg","usds","usdb","frax","lusd","susd","husd","busd","usdp","neutrino","origin-dollar","dola-borrowing-right","celo-dollar"];
def wrapped_ids: ["wrapped-bitcoin","wrapped-ether","staked-ether","rocket-pool-eth","cbeth","reth","frxeth","sfrxeth","wbeth","ankr-reward-bearing-staked-eth","weeth","wsteth"];
def ch24: (.price_change_percentage_24h_in_currency // .price_change_percentage_24h // 0);
def ch7d: (.price_change_percentage_7d_in_currency // 0);
def ch1h: (.price_change_percentage_1h_in_currency // 0);
def is_filtered:
  (.id as $id | stablecoin_ids | contains([$id])) or
  (.id as $id | wrapped_ids | contains([$id])) or
  ((.total_volume // 0) < 1000000) or
  (.symbol | ascii_upcase | startswith("USD")) or
  (.symbol | ascii_upcase | startswith("EUR")) or
  (.symbol | ascii_upcase | startswith("GBP"));

[.[] | select(is_filtered | not)] as $filtered |

# BTC/ETH
(.[] | select(.id == "bitcoin") | "BTC|\(.current_price)|\(ch24)"),
(.[] | select(.id == "ethereum") | "ETH|\(.current_price)|\(ch24)"),

# Pulse: filtered top-100
($filtered | map(select((.market_cap_rank // 999) <= 100)) as $top100 |
  ($top100 | map(select(ch24 > 0)) | length) as $green |
  "PULSE|\($green)|\($top100 | length)"
),

# Top 10 winners
"---WINNERS---",
($filtered | sort_by(ch24) | reverse | .[0:10][] |
  "W|\(.market_cap_rank // 999)|\(.symbol | ascii_upcase)|\(.name)|\(.current_price)|\(ch24)|\(ch7d)|\(ch1h)|\(.total_volume)|\(.market_cap // 0)"
),

# Top 10 losers
"---LOSERS---",
($filtered | sort_by(ch24) | .[0:10][] |
  "L|\(.market_cap_rank // 999)|\(.symbol | ascii_upcase)|\(.name)|\(.current_price)|\(ch24)|\(ch7d)|\(ch1h)|\(.total_volume)|\(.market_cap // 0)"
)
