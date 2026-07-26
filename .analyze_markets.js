const fs = require('fs');
const data = JSON.parse(fs.readFileSync('.cg_markets_raw.json', 'utf8'));

const STABLE_IDS = new Set(['tether','usd-coin','dai','first-digital-usd','ethena-usde','tusd','usdd','paypal-usd','frax','usdb','true-usd','pax-gold','tether-gold','stasis-eurs','mim','alchemix-usd','dola-borrowing-right','crvusd','liquity-usd','origin-dollar','rai']);
const STABLE_SYMS = new Set(['usdt','usdc','dai','busd','tusd','usdd','usdp','gusd','frax','lusd','pyusd','fdusd','paxg','xaut','eurt','eurs','usde','crvusd','susd','usd1','usdb','musd','cusd']);
const WRAPPED = new Set(['wrapped-bitcoin','wrapped-ether','wrapped-steth','staked-ether','wrapped-eeth','coinbase-wrapped-staked-eth','rocket-pool-eth','mantle-staked-ether','binance-eth']);

function isStable(c) {
  if (STABLE_IDS.has(c.id)) return true;
  const sym = c.symbol.toLowerCase();
  if (STABLE_SYMS.has(sym)) return true;
  if (sym.startsWith('usd') || sym.startsWith('eur') || sym.startsWith('gbp')) return true;
  if (c.name.toLowerCase().includes('stablecoin')) return true;
  return false;
}

function p24(c) { return c.price_change_percentage_24h_in_currency ?? c.price_change_percentage_24h ?? 0; }
function p7d(c) { return c.price_change_percentage_7d_in_currency ?? 0; }
function p1h(c) { return c.price_change_percentage_1h_in_currency ?? 0; }

const filtered = data.filter(c => {
  if (isStable(c)) return false;
  if (WRAPPED.has(c.id)) return false;
  if ((c.total_volume || 0) < 1_000_000) return false;
  return true;
});

console.error('Filtered count:', filtered.length);

const sorted = [...filtered].sort((a, b) => p24(a) - p24(b));
const losers = sorted.slice(0, 10);
const winners = sorted.slice(-10).reverse();

function fmtPrice(p) {
  if (!p) return '?';
  if (p >= 1000) return '$' + p.toLocaleString('en', {maximumFractionDigits: 0});
  if (p >= 1) return '$' + p.toPrecision(5).replace(/\.?0+$/, '');
  if (p >= 0.01) return '$' + p.toFixed(4);
  return '$' + p.toFixed(6);
}

function fmtVol(v) {
  if (v >= 1e9) return '$' + (v/1e9).toFixed(1) + 'B';
  if (v >= 1e6) return '$' + Math.round(v/1e6) + 'M';
  return '$' + Math.round(v/1e3) + 'K';
}

console.log('\n=== WINNERS ===');
for (const c of winners) {
  const rank = c.market_cap_rank || 999;
  const tags = [];
  const p = p24(c), p7 = p7d(c), mc = c.market_cap || 0, vol = c.total_volume || 0;
  if (rank > 150 && p > 30) tags.push('[PUMP-RISK]');
  if (p > 15 && p7 > 25) tags.push('[BREAKOUT]');
  if (p > 20 && p7 < 0) tags.push('[FADE]');
  if (mc < 50_000_000) tags.push('[MICROCAP]');
  if (rank <= 20 && !tags.length) tags.push('[MAJOR]');
  console.log(c.symbol.toUpperCase() + ' (' + c.name + ') #' + rank + ' ' + fmtPrice(c.current_price) + ' 24h:' + p.toFixed(1) + '% 7d:' + p7.toFixed(1) + '% 1h:' + p1h(c).toFixed(1) + '% vol:' + fmtVol(vol) + ' mcap:' + fmtVol(mc) + ' ' + tags.join(''));
}

console.log('\n=== LOSERS ===');
for (const c of losers) {
  const rank = c.market_cap_rank || 999;
  const tags = [];
  const p = p24(c), p7 = p7d(c), mc = c.market_cap || 0, vol = c.total_volume || 0;
  if (p < -10 && mc > 0 && vol/mc > 0.25) tags.push('[CAPITULATION]');
  if (rank <= 20) tags.push('[MAJOR]');
  console.log(c.symbol.toUpperCase() + ' (' + c.name + ') #' + rank + ' ' + fmtPrice(c.current_price) + ' 24h:' + p.toFixed(1) + '% 7d:' + p7.toFixed(1) + '% 1h:' + p1h(c).toFixed(1) + '% vol:' + fmtVol(vol) + ' mcap:' + fmtVol(mc) + ' ' + tags.join(''));
}

// Market pulse
const top100 = filtered.filter(c => (c.market_cap_rank || 999) <= 100);
const green = top100.filter(c => p24(c) > 0).length;
const top50 = filtered.filter(c => (c.market_cap_rank || 999) <= 50);
const pcts50 = top50.map(c => p24(c)).sort((a,b) => a-b);
const med50 = pcts50.length ? pcts50[Math.floor(pcts50.length/2)] : 0;
const btc = data.find(c => c.id === 'bitcoin');
const eth = data.find(c => c.id === 'ethereum');

console.log('\n=== PULSE ===');
console.log('Top-100 green:', green, '/', top100.length);
console.log('Median top-50:', med50.toFixed(2) + '%');
console.log('BTC:', fmtPrice(btc && btc.current_price), (btc ? p24(btc).toFixed(1) : '?') + '%');
console.log('ETH:', fmtPrice(eth && eth.current_price), (eth ? p24(eth).toFixed(1) : '?') + '%');

// All tagged coins for Notable section
console.log('\n=== NOTABLE TAGS ===');
for (const c of sorted) {
  const rank = c.market_cap_rank || 999;
  const tags = [];
  const p = p24(c), p7 = p7d(c), mc = c.market_cap || 0, vol = c.total_volume || 0;
  if (rank > 150 && p > 30) tags.push('PUMP-RISK');
  if (p > 15 && p7 > 25) tags.push('BREAKOUT');
  if (p > 20 && p7 < 0) tags.push('FADE');
  if (p < -10 && mc > 0 && vol/mc > 0.25) tags.push('CAPITULATION');
  if (tags.length) {
    console.log(c.symbol.toUpperCase() + ' #' + rank + ' 24h:' + p.toFixed(1) + '% 7d:' + p7.toFixed(1) + '% vol/mc:' + (mc > 0 ? (vol/mc).toFixed(2) : 'N/A') + ' tags:' + tags.join(','));
  }
}

// Output all symbols for trending cross-reference
console.log('\n=== ALL IDS ===');
console.log(filtered.map(c => c.id).join(','));
