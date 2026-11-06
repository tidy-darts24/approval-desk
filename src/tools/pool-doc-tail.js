const f = n => '£' + Math.round(n).toLocaleString('en-GB');
const KIND = { invoice: 'Supplier invoice', expense: 'Expense (in person)', ads: 'Ad spend', renewal: 'Software renewal', bank: 'Bank-change email', duplicate: 'Duplicate of a paid PO', zero: 'Extra zero', overPO: 'Over its PO', lookalike: 'Lookalike supplier', restaurant: 'Restaurant over £150', rail: 'Rail fare over £250', taxi: 'Taxi over £75', owner: 'Renewal with no owner', network: 'Ads on a consumer network' };
const rows = good => POOL.filter(p => good ? !TRAP_KINDS.includes(p.kind) : TRAP_KINDS.includes(p.kind)).map(p => {
  const it = p.build({ S: n => n, R: n => n, ongoing: false });
  const doc = it.rows.map(([k, v]) => `${k}: ${v}`).join(' · ');
  const out = `${it.corpay.label} ${f(it.corpay.amount)}`;
  return `| ${p.id} | ${KIND[p.kind]} | ${it.feedTitle || it.ref + ' ' + it.title} · ${doc} | ${f(it.amount)} | ${good ? 'Approve' : 'Reject: ' + it.trap.cat.toLowerCase() + ', ' + it.trap.meta.charAt(0).toLowerCase() + it.trap.meta.slice(1)} | ${it.detail.control}${it.physical ? ' (physical card)' : ''} · ${out} · ${it.detail.rule} |`;
}).join('\n');
const head = '| # | Kind | Payment (as on the desk) | Base amount | Answer | Round 2 on Corpay |\n|---|---|---|---|---|---|';
console.log('### Genuine (30)\n\n' + head + '\n' + rows(true) + '\n\n### Problems (30, ten kinds × three)\n\n' + head + '\n' + rows(false));
const st = [[], [], []];
for (let n = 0; n < 6000; n++) {
  BAND = n % 3; const d = deal(); const it = d.items;
  const paid = it.reduce((t, i) => t + i.corpay.amount, 0), desk = it.reduce((t, i) => t + i.amount, 0), max = Math.max(...it.map(i => i.amount));
  const month = d.ongoing.filter(o => !o.closed).reduce((t, o) => t + o.amount, 0);
  st[BAND].push({ desk, paid, rebate: Math.floor(paid * 0.01), max, year: Math.floor(month * 12 * 0.01) });
}
const big = x => x >= 1e6 ? '£' + (x / 1e6).toFixed(2) + 'm' : '£' + Math.round(x / 1000) + 'k';
const r = (a, k, m = x => '£' + (x / 1e6).toFixed(1) + 'm') => { const v = a.map(x => x[k]); return m(Math.min(...v)) + ' to ' + m(Math.max(...v)); };
console.log('\n| Desk size | On the desk | Round 2 card spend | Round 2 rebate | Largest payment | Ongoing rebate a year |\n|---|---|---|---|---|---|');
['Small', 'Medium', 'Large'].forEach((nm, i) => console.log(`| ${nm} | ${r(st[i], 'desk')} | ${r(st[i], 'paid')} | ${r(st[i], 'rebate', big)} | ${r(st[i], 'max', big)} | ${r(st[i], 'year', big)} |`));
