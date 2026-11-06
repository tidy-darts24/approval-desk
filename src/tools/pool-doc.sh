#!/bin/sh
# Prints the 60-payment pool tables and desk-size ranges (as in game-script.md) from the game code in src.html.
cd "$(dirname "$0")/.." && python3 -c "
s = open('src.html').read()
print(s[s.index('  // ---------- The payment pool'):s.index('  const ROUND_MS')] + open('tools/pool-doc-tail.js').read())" > /tmp/approval-desk-pool-doc.js && node /tmp/approval-desk-pool-doc.js
