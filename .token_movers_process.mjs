import { readFileSync } from 'fs';

const data = JSON.parse(readFileSync('/dev/stdin', 'utf8'));

const STABLECOINS = new Set([
  'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg',
  'usds','usdb','frax','lusd','susd','husd','busd','usdp','neutrino','origin-dollar',
  'dola-borrowing-right','celo-dollar'
]);
const WRAPPED = new Set([
  'wrapped-bitcoin','wrapped-ether','staked-ether','rocket-pool-eth','cbeth','reth','frxeth',
  'sfrxeth','wbeth','ankr-reward-bearing-staked-eth','weeth','wsteth'
]);

const ch24 = c => c.price_change_percentage_24h_in_currency ?? c.price_change_percentage_24h ?? 0;
const ch7d = c => c.price_change_percentage_7d_in_currency ?? 0;
const ch1h = c => c.price_change_percentage_1h_in_currency ?? 0;

const filtered = data.filter(c => {
  if (STABLECOINS.has(c.id)) return false;
  if (WRAPPED.has(c.id)) return false;
  if ((c.total_volume ?? 0) < 1_000_000) return false;
  const sym = (c.symbol ?? '').toUpperCase();
  if (sym.startsWith('USD') || sym.startsWith('EUR') || sym.startsWith('GBP')) return false;
  return true;
});

// BTC/ETH
const btc = data.find(c => c.id === 'bitcoin');
const eth = data.find(c => c.id === 'ethereum');
console.log(`BTC|${btc.current_price}|${ch24(btc).toFixed(1)}`);
console.log(`ETH|${eth.current_price}|${ch24(eth).toFixed(1)}`);

// Pulse
const top100 = filtered.filter(c => (c.market_cap_rank ?? 999) <= 100);
const green = top100.filter(c => ch24(c) > 0).length;
const top50 = [...top100].sort((a,b) => (b.market_cap ?? 0) - (a.market_cap ?? 0)).slice(0, 50);
const changes50 = top50.map(c => ch24(c)).sort((a,b) => a-b);
const median50 = changes50[Math.floor(changes50.length/2)] ?? 0;
console.log(`PULSE|${green}|${top100.length}|${median50.toFixed(1)}`);

// Sort by 24h
const sorted = [...filtered].sort((a,b) => ch24(b) - ch24(a));
const winners = sorted.slice(0, 10);
const losers = sorted.slice(-10).reverse();

const fmtRow = (prefix, c) => {
  const rank = c.market_cap_rank ?? 999;
  const sym = (c.symbol ?? '').toUpperCase();
  const mcap = c.market_cap ?? 0;
  const vol = c.total_volume ?? 0;
  return `${prefix}|${rank}|${sym}|${c.name}|${c.current_price}|${ch24(c).toFixed(2)}|${ch7d(c).toFixed(2)}|${ch1h(c).toFixed(2)}|${vol}|${mcap}`;
};

console.log('---WINNERS---');
winners.forEach(c => console.log(fmtRow('W', c)));
console.log('---LOSERS---');
losers.forEach(c => console.log(fmtRow('L', c)));
