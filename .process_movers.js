const fs = require('fs');
const coins = JSON.parse(fs.readFileSync('.cg_markets.json', 'utf8'));

const STABLECOINS = new Set([
  'tether','usd-coin','dai','first-digital-usd','usde','tusd','usdd','pyusd','fdusd','paxg',
  'tether-eurt','euro-coin','gemini-dollar','usds','true-usd','paypal-usd','frax','crvusd',
  'bridged-usd-coin-base','usdz-token','wrapped-bitcoin','staked-ether',
  'wrapped-steth','coinbase-wrapped-btc','renzo-restaked-eth','bedrock-unibtc','kelp-dao-restaked-eth',
  'wrapped-eeth','usd0','usual-usd','mountain-protocol-usdm','reserve-rights-token',
  'ethena-usde','nusd','tbtc','sbtc','susdx','mantle-staked-ether',
  'lido-staked-ether','rocket-pool-eth','frax-ether','stakewise-staked-eth',
]);

function isStable(c) {
  if (STABLECOINS.has(c.id)) return true;
  const sym = (c.symbol || '').toUpperCase();
  const name = (c.name || '').toLowerCase();
  if (sym.startsWith('USD') || sym.startsWith('EUR') || sym.startsWith('GBP')) return true;
  if (name.includes('stablecoin') || name.includes('pegged')) return true;
  return false;
}

function fmtPrice(p) {
  if (p == null) return 'N/A';
  if (p >= 10000) return '$' + p.toLocaleString('en-US', {maximumFractionDigits: 0});
  if (p >= 100) return '$' + p.toFixed(2);
  if (p >= 1) return '$' + parseFloat(p.toPrecision(4));
  if (p >= 0.01) return '$' + p.toFixed(4);
  return '$' + p.toFixed(6);
}

function fmtVol(v) {
  if (v == null) return 'N/A';
  if (v >= 1e9) return '$' + (v/1e9).toFixed(1) + 'B';
  if (v >= 1e6) return '$' + Math.round(v/1e6) + 'M';
  return '$' + Math.round(v/1e3) + 'K';
}

function fmtPct(p) {
  if (p == null) return 'N/A';
  return (p >= 0 ? '+' : '') + p.toFixed(1) + '%';
}

const filtered = coins.filter(c => {
  if (isStable(c)) return false;
  const vol = c.total_volume || 0;
  return vol >= 1_000_000;
});

console.log('Filtered coins: ' + filtered.length);

const withChange = filtered.filter(c => c.price_change_percentage_24h_in_currency != null);
const by24h = [...withChange].sort((a, b) =>
  a.price_change_percentage_24h_in_currency - b.price_change_percentage_24h_in_currency
);

const losers = by24h.slice(0, 10);
const winners = by24h.slice(-10).reverse();

function getTags(c, isWinner) {
  const chg24 = c.price_change_percentage_24h_in_currency || 0;
  const chg7d = c.price_change_percentage_7d_in_currency || 0;
  const vol = c.total_volume || 0;
  const mc = c.market_cap || 0;
  const rank = c.market_cap_rank || 999;
  const tags = [];
  if (isWinner) {
    if (chg24 > 15 && chg7d > 25) tags.push('[BREAKOUT]');
    else if (chg24 > 20 && chg7d < 0) tags.push('[FADE]');
    if (rank > 150 && chg24 > 30) tags.push('[PUMP-RISK]');
  } else {
    if (chg24 < -10 && mc > 0 && (vol / mc) > 0.25) tags.push('[CAPITULATION]');
    if (rank > 150 && chg24 < -20) tags.push('[PUMP-RISK]');
  }
  if (mc > 0 && mc < 50_000_000) tags.push('[MICROCAP]');
  if (rank <= 20) tags.push('[MAJOR]');
  return tags.slice(0, 2);
}

console.log('\n=== TOP WINNERS (24h) ===');
winners.forEach((c, i) => {
  const chg24 = c.price_change_percentage_24h_in_currency;
  const chg7d = c.price_change_percentage_7d_in_currency;
  const chg1h = c.price_change_percentage_1h_in_currency;
  const tags = getTags(c, true);
  console.log(`${i+1}. ${c.symbol.toUpperCase()} (${c.name}) — ${fmtPrice(c.current_price)}  ${fmtPct(chg24)} / 7d ${fmtPct(chg7d)} / 1h ${fmtPct(chg1h)}  vol:${fmtVol(c.total_volume)} mcap:${fmtVol(c.market_cap)} #${c.market_cap_rank}  ${tags.join(' ')}`);
});

console.log('\n=== TOP LOSERS (24h) ===');
losers.forEach((c, i) => {
  const chg24 = c.price_change_percentage_24h_in_currency;
  const chg7d = c.price_change_percentage_7d_in_currency;
  const chg1h = c.price_change_percentage_1h_in_currency;
  const tags = getTags(c, false);
  console.log(`${i+1}. ${c.symbol.toUpperCase()} (${c.name}) — ${fmtPrice(c.current_price)}  ${fmtPct(chg24)} / 7d ${fmtPct(chg7d)} / 1h ${fmtPct(chg1h)}  vol:${fmtVol(c.total_volume)} mcap:${fmtVol(c.market_cap)} #${c.market_cap_rank}  ${tags.join(' ')}`);
});

// Market pulse
const top100 = filtered
  .filter(c => c.market_cap_rank && c.market_cap_rank <= 100)
  .sort((a, b) => a.market_cap_rank - b.market_cap_rank);
const green100 = top100.filter(c => (c.price_change_percentage_24h_in_currency || 0) > 0);
const top50changes = top100.slice(0, 50)
  .map(c => c.price_change_percentage_24h_in_currency || 0)
  .sort((a, b) => a - b);
const median50 = top50changes[Math.floor(top50changes.length / 2)] || 0;

console.log('\n=== MARKET PULSE ===');
console.log(`Green in top 100: ${green100.length}/${top100.length}`);
console.log(`Median 24h change (top 50): ${fmtPct(median50)}`);

const btc = coins.find(c => c.id === 'bitcoin');
if (btc) console.log(`BTC: ${fmtPrice(btc.current_price)} ${fmtPct(btc.price_change_percentage_24h_in_currency)}`);

// Also print trending symbol IDs to cross-reference
const trendingSymbols = ['chip','marscoin','sui','pengu','sol','link','hype'];
console.log('\n=== TRENDING CHECK IN MARKETS ===');
trendingSymbols.forEach(sym => {
  const match = filtered.find(c => c.symbol.toLowerCase() === sym);
  if (match) {
    const chg24 = match.price_change_percentage_24h_in_currency;
    console.log(`${sym.toUpperCase()}: rank #${match.market_cap_rank} ${fmtPct(chg24)} [in filtered]`);
  } else {
    console.log(`${sym.toUpperCase()}: not in filtered top-250`);
  }
});
