const fs = require('fs');
const cp = require('child_process');
const msg = fs.readFileSync('.token_movers_msg.txt', 'utf8').trim();
const r = cp.spawnSync('./notify', [msg], {stdio: 'inherit'});
process.exit(r.status || 0);
