# The Payments Challenge: game script

Campaign working name: Month-End Hell (21 Oct 2026). The game is The Payments Challenge (renamed from The Approval Desk on 2 Nov 2026). (draft for sign-off)

Landing page game. Corpay stats only. Nothing here is approved copy yet.

## Stats used

| Use | Figure | Source |
|---|---|---|
| Lead (round 1 result) | 85% of CFOs believe their current payment processes increase the risk of error, fraud or off-policy spend. | ¹ Card-First whitepaper, p7 |
| Supporting band | 83% say spend processes are still more manual than they should be. | ¹ Card-First whitepaper, p4 |
| Supporting band | 99% have experienced a real or attempted AP-related cyber incident in the last two years. | ² Automation Deficit, p11 |
| Round 2 / end | Up to 1% rebate on qualifying spend, worked out from each game's card spend (about £50k to £110k) | Corpay offer, caveat below |

Correction: the pasted list said "86% believe their organisation has been slow to modernise". The whitepaper says **84%** (p4 and p8). Its 86% is "finance teams spend six or more hours per person, per week on expense and payment administration".

Source lines:
- ¹ Censuswide survey (Feb 2026) of 300 UK CFOs with £20m+ turnover. Corpay, The Card-First Approach to Spend Modernisation.
- ² Censuswide × Corpay CFO Survey 2025 (UK findings), 150 CFOs. Corpay, The Automation Deficit.
- Numbered in the order they appear on the page (user, 22 Oct 2026: the band had ² before ¹).
- Rebate caveat (as on the Supplier cards set): *Up to 1% rebate on qualifying spend. Subject to agreed card-based monthly volumes; actual rate depends on monthly spend. Illustrative, not guaranteed.

## How to check a payment, named misses and software renewals (asked for 23 Oct 2026, built 26 Oct in version 28)

**1 and 2 · How to check a payment (a worked example, then where to look).** "Start the payment run" in Cara's email now opens round 1 with the clock waiting (1:15, bar full). A spotlight walks round the real desk in five steps, with an explanation card next to it on desktop and pinned to the bottom on phones. The buttons are Back, Next ("Start the clock" on the last step) and "Skip the example"; Escape also skips. Play again skips the example.
- The tray shows one example payment, tagged "Example only. It isn’t one of your ten payments.". It's a bank-details email ("Example · Email", Today 08:12, "New bank details") from a supplier on this game's supplier file, never the one dealt for the real bank-change problem. It asks for invoice XX-1187 to be paid into a new account whose ending doesn't match the file. Amount £186,742. The "Pay to" row and the supplier's line in the supplier file are highlighted in yellow.
- Steps:
  1. **Start with the payment:** "Each payment shows who it’s for, the invoice or PO, the account it’s going to and the amount. This example is an email asking you to pay {Supplier} into a new account ending {new}."
  2. **Check the supplier file:** "Is the supplier on file, and does the account match? {Supplier} is on file with an account ending {on file}, not {new}. That’s the giveaway, so this payment shouldn’t go out."
  3. **Check the purchase orders:** "Find the PO with the same number as the invoice, because some suppliers have more than one. The amounts must match exactly. A PO marked Paid has already gone out once, so don’t pay it again."
  4. **Check the policy:** "Expenses, software renewals and ad spend aren’t on the supplier file, so check them here: the spending limits for expenses, a current owner for renewals and Connectwork Ads for ad spend."
  5. **Then approve or reject:** "Approve a payment if it passes its checks, and reject it if anything’s wrong, like this example. Four of your ten payments shouldn’t go out, and you’ve got 75 seconds."
  - Steps 3 to 5 reworded on 27 Oct 2026 after reviewer feedback: one rejected a genuine Tallyboard Enterprise renewal because it wasn’t on the supplier file, and another took “within its PO” to mean near-matches were fine. Every genuine invoice matches the PO with the same number exactly; in 9 games out of 10 a supplier has two POs on the list.
- On phones, steps 2 to 4 open the "Suppliers, POs and policy" sheet automatically, and it closes again when the clock starts.
- The hint under the button in Cara's email now reads: "You’ll see one example first, then the clock starts."

**3 · Name each good payment that didn’t go out.** Under the four problem payments, the round 1 result now has "Good payments that didn’t go out · £total". It lists each one by reference, supplier or title, and amount, with a reason and a chip:
- "Held up" (yellow) for good payments rejected by mistake. The user confirmed this meaning on 23 Oct.
- "In the tray" for good payments the clock ran out on.
- Reasons: invoices "Genuine · on the supplier file and matches {PO number}" (e.g. "matches PO-4417"); expenses "Genuine · within the expenses policy"; ads "Genuine · Connectwork Ads is the approved network"; renewals "Genuine · has a current owner (renewals aren’t on the supplier file)". Changed on 27 Oct 2026 from "within its PO", which read as if near-matches were fine.
- The old "You held up n good payments worth £X" note is gone. If anything was left in the tray, a line reads "Those still in the tray when the clock stopped will go out late."

**4 · Renewals read as software.** Both the genuine and the no-owner renewals now show the card type "Software renewal" and "Plan: Annual software licence". The problem version is named "{Product} software renewal", and its phrase reads "…a £X software renewal went through for a tool nobody owns".

## Intro: the inbox opening (user, 23 Oct 2026)

The game opens on a computer showing the player's inbox, with the month-end email waiting. It replaced the separate prize screen and How to play screen (21 Oct 2026). The user's idea: "a fake flashing email inbox on a computer screen where the player has to open their month-end and sort it before christmas". The prize stays front and centre through the copy, the pinned hamper email and the prize tag.

### Christmas theme (user, 22 Oct 2026)
"Clear your desk in time for Christmas": the December payment run needs signing off before the Christmas break, so the game is a mini distraction that also shows what the desk can get like at Christmas. The opener was "Finance can go wild in December" until 22 Oct (it read as a dig at finance teams and failed the logo test), then "Every supplier wants paying before the Christmas break" until 23 Oct.
- Christmas emoji used sparingly: 🎄 on the prize eyebrow and the clear-desk result, and 🎁 on the prize tag, the hamper email, the hamper helper and the draw label.
- Gentle snowfall over the stage, quieter during round 1. It's static under reduced motion.
- Payments are set in December: invoices are due 1 to 21 December, and ongoing cards are next due in January 2027. Christmas payments include a team Christmas party (£1,286, over the restaurant limit), a Christmas client dinner and lunch, a team Christmas lunch, a taxi home after the Christmas party, bank-change emails sent "before the Christmas break", and a Christmas campaign on a consumer ad network.

### 1 · Inbox (first screen)
- Left: eyebrow "🎄 Corpay Christmas prize draw" (owner comment on the artifact, 28 Oct 2026) · H1 "Clear your desk in time for Christmas." · Sub "Every supplier payment and expense report needs your approval before the Christmas break. Take five with this mini game, then enter the draw to win a Christmas hamper for your team of up to ten. Everyone who plays can enter, whatever their score." (user's Figma edit, 28 Oct 2026)
- Button: Open the email · Helper: Two rounds, about two minutes. No sign-up to play. Closes 11 December 2026. Prize draw terms apply. (The terms link is a placeholder.)
- Right: a computer showing a generic "Mail" app (not styled on any real email client), Fri 18 Dec 16:42, folders Inbox (4), Flagged, Sent, Drafts, Archive. Emails, newest first:
  1. Cara Pay, Finance Director · 16:41 · tag "Needs sign-off" · "Your December payment run needs signing off" · "Ten payments are waiting for you, and the bank cut-off is 5pm." Highlighted, and pulses gently (about every two seconds) until it's opened. It's still under reduced motion.
  2. Corpay · 16:30 · tag "Pinned" · "🎁 Win a Christmas hamper for your team" · "Everyone who plays can enter the draw, whatever their score. Closes 11 December."
  3. Office Manager · 15:58 · "Office closes at 5pm today" · "Have a lovely break, and see you on Monday 4 January."
  4. [Supplier from the deal] · [time from the deal] · tag "External" · "New bank details" · the opening line of that game's bank-change email (for example Harlow Logistics, 09:14, "Hi, we’ve moved banks before the Christmas break…"). It's the same email that turns up on the desk in round 1.
  5. Secret Santa · Thu · read · "Secret Santa: £15 limit, no exceptions" · "Gifts under the tree in the kitchen by Thursday, please." (Hidden on phones.)
- Prize tag ("🎁 · The prize · A Christmas hamper · For a team of up to ten · Draw closes 11 December 2026") overlaps the bottom right of the monitor, smaller below 1360px. On phones it sits under the helper. Swap in a photo of the real hamper once the supplier is chosen.
- Clicking the month-end email or "Open the email" opens it. Opened emails lose their unread dot, and the counts drop.
- Cara Pay is a made-up name and a nod to Corpay (user, 23 Oct 2026). The user first said to use "just finance director", then suggested Cara Pay.

### 1b · The month-end email (replaces How to play)
- "‹ Inbox" back link · Subject: Your December payment run needs signing off · From: Cara Pay, Finance Director · To you · 16:41
- Body (figures built from the deal):
  - Hi,
  - "Ten payments worth £8.7m are waiting for your sign-off, and the bank cut-off is 5pm, so you’ve got 75 seconds."
  - "Check each one on your desk. Invoices need their supplier and account on the supplier file, and the same amount as their PO. Expenses, software renewals and ad spend aren’t on the supplier file, so check those against the policy. Reject anything that’s wrong, whether that’s fraud, an error or spend that breaks policy. Four of the ten shouldn’t go out." (reworded 27 Oct 2026)
  - "Thanks, and have a good Christmas. / Cara"
- Button: Start the payment run (starts the 75-second clock) · Hint: "Use the buttons, the ← and → keys, or a swipe." (touch screens: "Use the buttons or swipe the card.")
- The left copy stays put. The "Open the email" button steps aside on desktop and disappears on phones, where the copy also hides so the email fills the screen.

### 1c · The other emails and folders (user, 23 Oct 2026: "would be quite fun if you could open other things in the inbox", then "a sent email asking for ideas for what to buy Cara Pay")
Every email and folder opens. Each email has a "‹ [folder]" back link and an "Open the payment run email" button, except the month-end email, which has "Start the payment run". Only the month-end email starts the round. Folders are a sidebar on desktop and a row of tabs on phones.
- **Hamper email** (Inbox, Corpay, 16:30, Pinned): "🎁 Win a Christmas hamper for your team". "Hi," · "Everyone who plays The Payments Challenge can enter our prize draw for a Christmas hamper big enough for a team of up to ten, whatever their score." · "Sign off the payment run, then enter the draw at the end. It closes on 11 December 2026, and prize draw terms apply." · "The Corpay team"
- **Office Manager** (Inbox, 15:58, to all staff): "Office closes at 5pm today". "Hi all," · "The office closes at 5pm today and opens again on Monday 4 January." · "Before you go, please clear out the fridge, switch off your monitor and give the office tree some water. The last of the mince pies are in the kitchen." · "Have a lovely break. / The office team"
- **New bank details** (Inbox, External): the dealt bank-change email, with the supplier name, sender address and time from the deal. A yellow banner reads "External sender. This email came from outside your organisation." The body is the deal's email text, plus Invoice, Pay to (new account ending …) and Amount, signed "Thanks, / Accounts team". Under the button: "It’s in today’s payment run too."
- **Secret Santa** (Inbox, Mon, to the finance team; hidden in the phone list): "Secret Santa: £15 limit, no exceptions". "Hi all," · "Names went out this morning, so check who you’ve got." · "Gifts go under the tree in the kitchen by Thursday, and we’ll open them at the Christmas party." · "The limit is £15, no exceptions. Anything that comes in at £15.01 will be rejected." · "Merry Christmas, / The Secret Santa committee"
- **Sent · "Secret Santa: I’ve got Cara"** (You, to AP team, Tue): "Hi all," · "Don’t tell anyone, but I’ve got Cara Pay for Secret Santa." · "I need ideas. It has to come in under £15, and she signs off every payment we make, so whatever I get had better pass her approval." · "So far all I’ve come up with is a nice pen, a mug that says “Approved” or a fairly awful cat calendar. Ideas welcome." · "Thanks"
- **Sent · "Re: Christmas party taxis"** (You, to Office Manager, Wed): "Hi," · "Two of us need a taxi home after the party, please. We’ll keep the receipts for the expenses claim." · "Thanks"
- **Drafts · "Out of office: back on 4 January"** (Draft, not sent yet): "Thanks for your email. I’m out of the office until Monday 4 January." · "For anything urgent, please contact Cara Pay, Finance Director." · "Have a good Christmas."
- **Flagged:** "Nothing flagged. The payment run is waiting in your inbox." **Archive:** "Nothing archived since last Christmas."
- Header notes: Inbox "n unread" (or "All read"), Sent "2 sent", Drafts "1 draft". The Inbox badge counts down as emails are opened and hides at zero.

### Other Christmas lines
- Round 1 title: "Round 1 · Your desk before Christmas", with "Approve or reject each payment before the office shuts for Christmas."
- Result when all four are stopped and every good payment went out: "Every problem payment was stopped and every good one went out. That’s a clear desk for Christmas. 🎄" (only then: see Round 1 result)
- Round 2 sub: "Same ten payments. This time the card rules do the checking, and the desk is clear before Christmas."
- The old "What to look out for" panel (fraud, errors, off-policy) was dropped with How to play. Its points now sit in Cara's email, and the desk itself has the supplier file, POs and policy.
- Play again skips the inbox and deals a new desk straight into round 1.

## How each game is dealt (user, 21 Oct 2026)

The user asked for "60 random playable payments", because the same 20 came up every game. The game now holds a pool of 60 and deals 20 at random each time:
- **Half-length game (user, 22 Oct 2026: "make the game half as long 10 invoices, 4 errors"):** each game deals 10 payments, 6 genuine and 4 problems, with a 75-second round 1 (the same 7.5 seconds a payment as before).
- **6 genuine payments:** 5 supplier invoices and 1 other, which is an in-person expense, a Connectwork Ads charge or a software renewal with an owner. All 60 payments in the pool still come up. (Was 7 invoices and 2 expenses until 22 Oct 2026. Over-limit charges now pay nothing in round 2, so an extra invoice keeps the largest payment near its old size.)
- **4 problems, each of a different kind.** A bank-change email is in every game, because it's the only problem that still moves money in round 2 (paid to the supplier's own card). The other three kinds are drawn from the remaining nine, and each kind has three versions.
- **Order:** the first payment is always genuine, and no two problems come back to back.
- **The desk follows the deal.** The supplier file lists every supplier on the desk (2 to 6), including the real supplier behind a bank-change email or a lookalike. The PO list shows the deal's POs (5 to 8): an already-paid PO is marked "Paid", and over-PO and extra-zero invoices show their PO amount. The ongoing tab has 2 to 7 cards: each supplier's first invoice is its monthly contract, plus the Connectwork ad budget and, if it was dealt, the ownerless renewal as an expired card.
- **Desk size:** each game picks one of three sizes, and Play again always picks a different one. Amounts in the pool are for the smallest desk. Each game scales them so round 2 card spend lands in its band, so every figure stays non-round. Expenses aren't scaled.

| Desk size | On the desk | Round 2 card spend | Round 2 rebate | Largest payment | Ongoing rebate a year |
|---|---|---|---|---|---|
| Small | £5.0m to £8.8m | £5.0m to £5.7m | £50k to £57k | £855k to £1.15m | £191k to £574k |
| Medium | £7.1m to £12.2m | £7.1m to £8.1m | £71k to £81k | £1.22m to £1.72m | £270k to £818k |
| Large | £10.1m to £16.9m | £10.1m to £11.0m | £101k to £110k | £1.73m to £2.25m | £376k to £1.12m |

Ranges are from 6,000 simulated deals. With half the payments, keeping the rebate bands makes single payments bigger: about £1.17m on the small desk, which used to stay under £750k. The small desk was raised on 22 Oct 2026 (user: "round 2 could be bigger, some payments can go up to 750k"; chose the bigger small desk over capping every desk). The large one goes higher, because £100k back needs over £10m of card spend.

## Round 1: your desk (manual, 75 seconds)

Ad platforms are made up (user, 21 Oct 2026: "meta not linkedin but made up brands"). Connectwork Ads is the approved professional network. Feedloop Ads, Snapreel Ads and Pinstream Ads are consumer networks.

One document at a time: 3 to start, then one more every 6 seconds (sooner if the tray is empty). Approve (→ / swipe right) or Reject (← / swipe left). No right or wrong is shown until the result.

Desk layout (desktop): the Policy card and Done pile on the left, the payment in the centre, the supplier file and purchase orders on the right.

Phones (mobile MVP, 5 Nov 2026):
- The HUD is one line: Time left and In the tray. Paid out, Rebate and the instruction line are hidden on phones (Rebate is always £0 in round 1).
- Approve and Reject are pinned to the bottom of the screen in a decision bar, inside the safe area, with the "Suppliers, POs and policy" button above them. The payment and the bar fit on one screen.
- The supplier file, POs and policy are one sheet that slides up behind the decision bar, so you can still decide with it open. Its top strip repeats the payment you're checking (reference, title, amount, then its rows), because the sheet covers the card.
- While you drag, the card tints blue towards Approve and magenta towards Reject. Phones that support it give a short vibration on each call.
- In the example walk-through, the explanation card sits at the bottom, or at the top when the spotlight is on the decision bar.
- Supplier file (the pool's eight): Northgate Steel 0938 · Harlow Logistics 4471 · Brightwell Packaging 6625 · Kestrel IT Services 3310 · Marlow Energy 5502 · Calder Facilities 2864 · Oakbridge Fleet Services 7149 · Redfern Components 1586. Each game shows only the ones on its desk.
- Policy, grouped by payment type since 27 Oct 2026 (the old "Only pay suppliers and accounts on the supplier file" line read as if it covered every payment):
  - **Invoices:** Supplier and account on the supplier file. Amount matches the PO with the same number.
  - **Expenses:** Restaurants: up to £150 a bill. Rail fares: up to £250 each. Taxis: up to £75 a journey.
  - **Software renewals:** Not on the supplier file. They need a current owner.
  - **Ad spend:** Connectwork Ads only.

## The payment pool (60)

Generated from the game code. Amounts are the small-desk base, before each game's scaling. Over-PO and extra-zero invoices are built from their PO, so they always match the PO list.

### Genuine (30)

| # | Kind | Payment (as on the desk) | Base amount | Answer | Round 2 on Corpay |
|---|---|---|---|---|---|
| 1 | Supplier invoice | NS-2304 Northgate Steel · Pay to: Account ending 0938 · PO: PO-4398 · Due: 12 Dec 2026 | £398,615 | Approve | Merchant control · Paid £398,615 · Paid on a virtual card that only Northgate Steel can charge. |
| 2 | Supplier invoice | NS-2311 Northgate Steel · Pay to: Account ending 0938 · PO: PO-4415 · Due: 14 Dec 2026 | £362,083 | Approve | Merchant control · Paid £362,083 · Paid on a virtual card that only Northgate Steel can charge. |
| 3 | Supplier invoice | NS-2322 Northgate Steel · Pay to: Account ending 0938 · PO: PO-4447 · Due: 18 Dec 2026 | £331,470 | Approve | Merchant control · Paid £331,470 · Paid on a virtual card that only Northgate Steel can charge. |
| 4 | Supplier invoice | HL-3310 Harlow Logistics · Pay to: Account ending 4471 · PO: PO-4412 · Due: 13 Dec 2026 | £384,309 | Approve | Merchant control · Paid £384,309 · Paid on a virtual card that only Harlow Logistics can charge. |
| 5 | Supplier invoice | HL-3329 Harlow Logistics · Pay to: Account ending 4471 · PO: PO-4440 · Due: 18 Dec 2026 | £419,483 | Approve | Merchant control · Paid £419,483 · Paid on a virtual card that only Harlow Logistics can charge. |
| 6 | Supplier invoice | HL-3335 Harlow Logistics · Pay to: Account ending 4471 · PO: PO-4451 · Due: 20 Dec 2026 | £317,642 | Approve | Merchant control · Paid £317,642 · Paid on a virtual card that only Harlow Logistics can charge. |
| 7 | Supplier invoice | BP-7781 Brightwell Packaging · Pay to: Account ending 6625 · PO: PO-4410 · Due: 8 Dec 2026 | £348,236 | Approve | Merchant control · Paid £348,236 · Paid on a virtual card that only Brightwell Packaging can charge. |
| 8 | Supplier invoice | BP-7802 Brightwell Packaging · Pay to: Account ending 6625 · PO: PO-4443 · Due: 19 Dec 2026 | £397,326 | Approve | Merchant control · Paid £397,326 · Paid on a virtual card that only Brightwell Packaging can charge. |
| 9 | Supplier invoice | BP-7795 Brightwell Packaging · Pay to: Account ending 6625 · PO: PO-4426 · Due: 16 Dec 2026 | £308,918 | Approve | Merchant control · Paid £308,918 · Paid on a virtual card that only Brightwell Packaging can charge. |
| 10 | Supplier invoice | KIT-118 Kestrel IT Services · Pay to: Account ending 3310 · PO: PO-4405 · Due: 14 Dec 2026 | £372,690 | Approve | Merchant control · Paid £372,690 · Paid on a virtual card that only Kestrel IT Services can charge. |
| 11 | Supplier invoice | KIT-121 Kestrel IT Services · Pay to: Account ending 3310 · PO: PO-4417 · Due: 15 Dec 2026 | £341,118 | Approve | Merchant control · Paid £341,118 · Paid on a virtual card that only Kestrel IT Services can charge. |
| 12 | Supplier invoice | KIT-126 Kestrel IT Services · Pay to: Account ending 3310 · PO: PO-4438 · Due: 17 Dec 2026 | £318,374 | Approve | Merchant control · Paid £318,374 · Paid on a virtual card that only Kestrel IT Services can charge. |
| 13 | Supplier invoice | ME-0917 Marlow Energy · Pay to: Account ending 5502 · PO: PO-4421 · Due: 14 Dec 2026 | £326,415 | Approve | Merchant control · Paid £326,415 · Paid on a virtual card that only Marlow Energy can charge. |
| 14 | Supplier invoice | ME-0924 Marlow Energy · Pay to: Account ending 5502 · PO: PO-4449 · Due: 20 Dec 2026 | £304,861 | Approve | Merchant control · Paid £304,861 · Paid on a virtual card that only Marlow Energy can charge. |
| 15 | Supplier invoice | CF-0562 Calder Facilities · Pay to: Account ending 2864 · PO: PO-4403 · Due: 11 Dec 2026 | £313,276 | Approve | Merchant control · Paid £313,276 · Paid on a virtual card that only Calder Facilities can charge. |
| 16 | Supplier invoice | CF-0571 Calder Facilities · Pay to: Account ending 2864 · PO: PO-4434 · Due: 16 Dec 2026 | £344,509 | Approve | Merchant control · Paid £344,509 · Paid on a virtual card that only Calder Facilities can charge. |
| 17 | Supplier invoice | OF-1146 Oakbridge Fleet Services · Pay to: Account ending 7149 · PO: PO-4408 · Due: 12 Dec 2026 | £366,742 | Approve | Merchant control · Paid £366,742 · Paid on a virtual card that only Oakbridge Fleet Services can charge. |
| 18 | Supplier invoice | OF-1153 Oakbridge Fleet Services · Pay to: Account ending 7149 · PO: PO-4445 · Due: 19 Dec 2026 | £374,195 | Approve | Merchant control · Paid £374,195 · Paid on a virtual card that only Oakbridge Fleet Services can charge. |
| 19 | Supplier invoice | RC-0835 Redfern Components · Pay to: Account ending 1586 · PO: PO-4419 · Due: 15 Dec 2026 | £413,627 | Approve | Merchant control · Paid £413,627 · Paid on a virtual card that only Redfern Components can charge. |
| 20 | Supplier invoice | RC-0841 Redfern Components · Pay to: Account ending 1586 · PO: PO-4453 · Due: 21 Dec 2026 | £391,058 | Approve | Merchant control · Paid £391,058 · Paid on a virtual card that only Redfern Components can charge. |
| 21 | Expense (in person) | EX-0412 Client lunch for two · Claimed by: Sales team · Merchant category: Restaurant · Receipt: Attached | £96 | Approve | Spend category control (physical card) · Paid £96 · The card allows restaurant spend up to £150 a bill. This bill was £96. |
| 22 | Expense (in person) | EX-0428 Team Christmas lunch · Claimed by: Finance team · Merchant category: Restaurant · Receipt: Attached | £138 | Approve | Spend category control (physical card) · Paid £138 · The card allows restaurant spend up to £150 a bill. This bill was £138. |
| 23 | Expense (in person) | EX-0423 Rail fare, London to Leeds · Claimed by: Operations · Merchant category: Rail travel · Receipt: Attached | £144 | Approve | Spend category control (physical card) · Paid £144 · The card allows rail fares up to £250. This fare was £144. |
| 24 | Expense (in person) | EX-0437 Rail fare, London to Birmingham · Claimed by: Sales team · Merchant category: Rail travel · Receipt: Attached | £86 | Approve | Spend category control (physical card) · Paid £86 · The card allows rail fares up to £250. This fare was £86. |
| 25 | Expense (in person) | EX-0416 Taxi, station to client site · Claimed by: Operations · Merchant category: Taxi · Receipt: Attached | £38 | Approve | Spend category control (physical card) · Paid £38 · The card allows taxi fares up to £75 a journey. This fare was £38. |
| 26 | Expense (in person) | EX-0444 Taxi, office to the airport · Claimed by: Finance team · Merchant category: Taxi · Receipt: Attached | £64 | Approve | Spend category control (physical card) · Paid £64 · The card allows taxi fares up to £75 a journey. This fare was £64. |
| 27 | Ad spend | CW-0388 Connectwork Ads · Campaign: Card-First whitepaper · Audience: UK finance leaders · Requested by: Marketing | £38,270 | Approve | Merchant control · Paid £38,270 · Connectwork Ads is the approved ad network, so the charge went through on the marketing card. |
| 28 | Ad spend | CW-0395 Connectwork Ads · Campaign: Supplier cards launch · Audience: UK procurement leads · Requested by: Marketing | £34,815 | Approve | Merchant control · Paid £34,815 · Connectwork Ads is the approved ad network, so the charge went through on the marketing card. |
| 29 | Software renewal | LL-0214 Ledgerline Analytics · Plan: Annual licence · Owner: Head of FP&A · Renews: 4 Jan 2027 | £72,500 | Approve | Merchant control · Paid £72,500 · The card only pays Ledgerline Analytics, and the licence has a current owner, so the renewal went through. |
| 30 | Software renewal | TB-0631 Tallyboard Enterprise · Plan: Annual licence · Owner: Finance systems team · Renews: 9 Jan 2027 | £58,000 | Approve | Merchant control · Paid £58,000 · The card only pays Tallyboard Enterprise, and the licence has a current owner, so the renewal went through. |

### Problems (30, ten kinds × three)

| # | Kind | Payment (as on the desk) | Base amount | Answer | Round 2 on Corpay |
|---|---|---|---|---|---|
| 31 | Bank-change email | HL-3302 Harlow Logistics · Supplier: Harlow Logistics · Invoice: HL-3302 · Pay to: New account ending 9152 | £392,914 | Reject: fraud, new account didn’t match the supplier file | Merchant control · Paid £392,914 · Paid to Harlow’s own card. The new bank details in the email were never used. |
| 32 | Bank-change email | ME-0912 Marlow Energy · Supplier: Marlow Energy · Invoice: ME-0912 · Pay to: New account ending 3047 | £338,537 | Reject: fraud, new account didn’t match the supplier file | Merchant control · Paid £338,537 · Paid to Marlow’s own card. The new bank details in the email were never used. |
| 33 | Bank-change email | NS-2296 Northgate Steel · Supplier: Northgate Steel · Invoice: NS-2296 · Pay to: New account ending 6618 | £407,206 | Reject: fraud, new account didn’t match the supplier file | Merchant control · Paid £407,206 · Paid to Northgate’s own card. The new bank details in the email were never used. |
| 34 | Duplicate of a paid PO | NS-2291 Northgate Steel · Pay to: Account ending 0938 · PO: PO-4380 · Note: Reminder: payment due | £364,519 | Reject: error, pO-4380 was already paid | Single-use card · Declined £0 · PO-4380 was paid on a single-use card on 3 Dec. The card closed after that payment, so a second charge was declined. |
| 35 | Duplicate of a paid PO | BP-7764 Brightwell Packaging · Pay to: Account ending 6625 · PO: PO-4372 · Note: Second request | £337,845 | Reject: error, pO-4372 was already paid | Single-use card · Declined £0 · PO-4372 was paid on a single-use card on 1 Dec. The card closed after that payment, so a second charge was declined. |
| 36 | Duplicate of a paid PO | RC-0819 Redfern Components · Pay to: Account ending 1586 · PO: PO-4376 · Note: Overdue reminder | £382,316 | Reject: error, pO-4376 was already paid | Single-use card · Declined £0 · PO-4376 was paid on a single-use card on 2 Dec. The card closed after that payment, so a second charge was declined. |
| 37 | Extra zero | BP-7790 Brightwell Packaging · Pay to: Account ending 6625 · PO: PO-4432 · Due: 15 Dec 2026 | £344,200 | Reject: error, pO was raised for £34,420 | Amount limit · Declined £0 · The charge was for £344,200, over the card’s £34,420 limit, so it was declined. Nothing was paid. |
| 38 | Extra zero | KIT-124 Kestrel IT Services · Pay to: Account ending 3310 · PO: PO-4429 · Due: 16 Dec 2026 | £317,360 | Reject: error, pO was raised for £31,736 | Amount limit · Declined £0 · The charge was for £317,360, over the card’s £31,736 limit, so it was declined. Nothing was paid. |
| 39 | Extra zero | CF-0566 Calder Facilities · Pay to: Account ending 2864 · PO: PO-4424 · Due: 14 Dec 2026 | £371,930 | Reject: error, pO was raised for £37,193 | Amount limit · Declined £0 · The charge was for £371,930, over the card’s £37,193 limit, so it was declined. Nothing was paid. |
| 40 | Over its PO | NS-2317 Northgate Steel · Pay to: Account ending 0938 · PO: PO-4436 · Due: 17 Dec 2026 | £414,995 | Reject: error, £28,265 over PO-4436 | Amount limit · Declined £0 · The charge was £28,265 over the card’s £386,730 limit, so it was declined. Nothing was paid. |
| 41 | Over its PO | HL-3318 Harlow Logistics · Pay to: Account ending 4471 · PO: PO-4428 · Due: 15 Dec 2026 | £370,395 | Reject: error, £27,480 over PO-4428 | Amount limit · Declined £0 · The charge was £27,480 over the card’s £342,915 limit, so it was declined. Nothing was paid. |
| 42 | Over its PO | OF-1150 Oakbridge Fleet Services · Pay to: Account ending 7149 · PO: PO-4431 · Due: 16 Dec 2026 | £377,979 | Reject: error, £19,375 over PO-4431 | Amount limit · Declined £0 · The charge was £19,375 over the card’s £358,604 limit, so it was declined. Nothing was paid. |
| 43 | Lookalike supplier | KIS-0441 Kestrel IT Solutions Ltd · Pay to: Account ending 7781 · PO: Not quoted · Due: 9 Dec 2026 | £342,708 | Reject: fraud, supplier and account not on the supplier file | Merchant control · Blocked £0 · There is no card for Kestrel IT Solutions Ltd, so nothing could be paid. Your real supplier is Kestrel IT Services. |
| 44 | Lookalike supplier | BPL-2207 Brightwell Packing Ltd · Pay to: Account ending 6652 · PO: Not quoted · Due: 13 Dec 2026 | £316,394 | Reject: fraud, supplier and account not on the supplier file | Merchant control · Blocked £0 · There is no card for Brightwell Packing Ltd, so nothing could be paid. Your real supplier is Brightwell Packaging. |
| 45 | Lookalike supplier | CFS-0318 Calder Facility Services · Pay to: Account ending 2846 · PO: Not quoted · Due: 11 Dec 2026 | £328,517 | Reject: fraud, supplier and account not on the supplier file | Merchant control · Blocked £0 · There is no card for Calder Facility Services, so nothing could be paid. Your real supplier is Calder Facilities. |
| 46 | Restaurant over £150 | EX-0419 Christmas client dinner for two · Claimed by: Sales team · Merchant category: Restaurant · Receipt: Includes two bottles of champagne | £540 | Reject: off-policy, over the £150 restaurant limit | Spend category control (physical card) · Declined £0 · The card allows restaurant spend up to £150 a bill, so the £540 bill was declined at the till. |
| 47 | Restaurant over £150 | EX-0427 Team Christmas party · Claimed by: Marketing team · Merchant category: Restaurant · Receipt: Attached | £1,286 | Reject: off-policy, over the £150 restaurant limit | Spend category control (physical card) · Declined £0 · The card allows restaurant spend up to £150 a bill, so the £1,286 bill was declined at the till. |
| 48 | Restaurant over £150 | EX-0438 Christmas lunch with a client · Claimed by: Sales team · Merchant category: Restaurant · Receipt: Attached | £214 | Reject: off-policy, over the £150 restaurant limit | Spend category control (physical card) · Declined £0 · The card allows restaurant spend up to £150 a bill, so the £214 bill was declined at the till. |
| 49 | Rail fare over £250 | EX-0431 Rail fare, London to Manchester · Claimed by: Sales team · Merchant category: Rail travel · Receipt: Attached | £468 | Reject: off-policy, over the £250 rail fare limit | Spend category control (physical card) · Declined £0 · The card allows rail fares up to £250, so the £468 fare was declined at the ticket office. |
| 50 | Rail fare over £250 | EX-0435 Rail fare, London to Edinburgh · Claimed by: Operations · Merchant category: Rail travel · Receipt: Attached | £392 | Reject: off-policy, over the £250 rail fare limit | Spend category control (physical card) · Declined £0 · The card allows rail fares up to £250, so the £392 fare was declined at the ticket office. |
| 51 | Rail fare over £250 | EX-0442 Rail fare, Bristol to Newcastle · Claimed by: Finance team · Merchant category: Rail travel · Receipt: Attached | £317 | Reject: off-policy, over the £250 rail fare limit | Spend category control (physical card) · Declined £0 · The card allows rail fares up to £250, so the £317 fare was declined at the ticket office. |
| 52 | Taxi over £75 | EX-0433 Taxi, Heathrow to the office · Claimed by: Sales team · Merchant category: Taxi · Receipt: Attached | £184 | Reject: off-policy, over the £75 taxi limit | Spend category control (physical card) · Declined £0 · The card allows taxi fares up to £75 a journey, so the £184 fare was declined in the cab. |
| 53 | Taxi over £75 | EX-0440 Taxi, Leeds station to client · Claimed by: Operations · Merchant category: Taxi · Receipt: Attached | £96 | Reject: off-policy, over the £75 taxi limit | Spend category control (physical card) · Declined £0 · The card allows taxi fares up to £75 a journey, so the £96 fare was declined in the cab. |
| 54 | Taxi over £75 | EX-0446 Taxi home after the Christmas party · Claimed by: Marketing team · Merchant category: Taxi · Receipt: Attached | £132 | Reject: off-policy, over the £75 taxi limit | Spend category control (physical card) · Declined £0 · The card allows taxi fares up to £75 a journey, so the £132 fare was declined in the cab. |
| 55 | Renewal with no owner | SR-2027 SlideStack Pro · Plan: Annual licence · Owner: None since June · Renews: 1 Jan 2027 | £92,000 | Reject: off-policy, no current owner | Card expiry · Stopped £0 · The SlideStack Pro card was set to expire when its owner left in June, so the renewal was declined. |
| 56 | Renewal with no owner | PW-0812 Pollwise Business · Plan: Annual licence · Owner: None since March · Renews: 8 Jan 2027 | £64,500 | Reject: off-policy, no current owner | Card expiry · Stopped £0 · The Pollwise Business card was set to expire when its owner left in March, so the renewal was declined. |
| 57 | Renewal with no owner | CD-0390 Clipdeck Studio · Plan: Annual licence · Owner: None since August · Renews: 12 Jan 2027 | £78,000 | Reject: off-policy, no current owner | Card expiry · Stopped £0 · The Clipdeck Studio card was set to expire when its owner left in August, so the renewal was declined. |
| 58 | Ads on a consumer network | AD-1182 Feedloop Ads · Campaign: Card-First whitepaper · Audience: Consumers, 18–34 · Requested by: Marketing | £23,640 | Reject: off-policy, ads must run on Connectwork Ads | Merchant control · Declined £0 · The marketing card only pays Connectwork Ads, so the Feedloop Ads charge was declined. |
| 59 | Ads on a consumer network | AD-1190 Snapreel Ads · Campaign: Supplier cards launch · Audience: Students and young adults · Requested by: Marketing | £31,275 | Reject: off-policy, ads must run on Connectwork Ads | Merchant control · Declined £0 · The marketing card only pays Connectwork Ads, so the Snapreel Ads charge was declined. |
| 60 | Ads on a consumer network | AD-1197 Pinstream Ads · Campaign: Christmas campaign · Audience: Home and lifestyle shoppers · Requested by: Marketing | £18,930 | Reject: off-policy, ads must run on Connectwork Ads | Merchant control · Declined £0 · The marketing card only pays Connectwork Ads, so the Pinstream Ads charge was declined. |

Scoring (user, 22 Oct 2026): correct calls out of 10 (problems rejected plus genuine payments approved; anything left in the tray isn't a call), then paid in error, then time taken. This is how the company leaderboard ranks players, so rejecting everything scores 4 of 10. Also shown: problems stopped out of 4; money that went out on problems ("paid in error"); good payments held up; anything left in the tray counts as late. Rebate earned on bank transfers is always £0. With four or more problems through, the result gives a one-line total instead of a list.

## Round 1 result

- Title: "Round 1 · Finished early" if every payment was decided before the clock ran out (22 Oct 2026, user), otherwise "Round 1 · Time’s up". The screen reader announcement starts the same way.
- Counters: Correct calls (n of 10), Time taken (the clock used, 1:15 if it ran out), Paid out, Rebate £0.
- Clear desk only when it's earned: all four stopped and every good payment approved gives "…That’s a clear desk for Christmas. 🎄". All four stopped but good payments held up gives "Every problem payment was stopped, but you held up {n} good payments worth {£} too. Those suppliers will be chasing after Christmas." All four stopped with good payments still in the tray gives "Every problem payment was stopped before it left your desk.", plus the late note.
- End screen comparison adds a first row: Correct calls, yours against 10 of 10 on Corpay.
- H1: You stopped n of 4. · Sub: built from what got through (e.g. "£1,027,291 went to a supplier that isn’t on file, and an invoice went out £88,386 over its PO.")
- Lead stat: 85% of CFOs believe their current payment processes increase the risk of error, fraud or off-policy spend.¹
- List: "Your four problem payments", each Stopped / Got through / In the tray. Button: What if you’d used Corpay? (was "Run the same desk on Corpay" until 5 Nov 2026)

## Round 2: what if you’d used Corpay? (instant reveal)

Simplified on 5 Nov 2026 (user: round 2 only needs to ask "what if you’d used Corpay?" and show the results straight away, interactively). The autoplay, the two tabs, the six-row detail panel and the previous/next arrows are gone.

- Title: "Round 2 · What if you’d used Corpay?" The sub is unchanged.
- Counters: Problems stopped, Paid out and Rebate count up from zero while the ten rows land one after another (about a second and a half in all). In the tray is gone. Under reduced motion everything shows at once.
- List: the ten payments in the order they were dealt. Each row shows the reference and title, the one-line Corpay result (the old feed line), the amount, the chip (Paid / Declined / Blocked / Stopped), and what your desk did with the same payment: "Your desk: stopped it too", "approved it too", "got through", "held it up" or "still in the tray". The last three get a yellow dot, as calls Corpay handled differently.
- Opening a row (click or tap, one open at a time) shows "What Corpay did · <control>", the rule sentence, and "Card: … · Rebate: …". The bank-change email opens by default once the rows have landed. On desktop the card visual on the left follows the open row (virtual or physical). On phones the card visual is hidden, the one-line result only shows in the opened row, and in-person spend shows the physical card as a thumbnail.
- "Click/Tap any payment to see the Corpay control behind it" appears above the list once the reveal is done, and "See how you compare" unlocks.
- Not shown any more: the Ongoing supplier payments tab and its summary line, and the Record and Schedule detail rows. The end screen still has "Rebate a year on ongoing cards", worked out from the same ongoing cards. To confirm with Josh whether it stays now that round 2 no longer explains it.

Problems stopped 4 of 4. The rebate is on all card spend: the genuine payments and the bank-change payment (made to the supplier's own card). Over-limit charges are declined, so they add nothing.

**No invoice matching (user, 22 Oct 2026):** "we don't do invoice matching unless another module is bought, so we have to make sure that the round is accurate to the product".
- Round 2 claims no invoice or PO matching and no automatic reconciliation. Every outcome comes from a card control.
- The detail row that was "Reconciliation" is now "Record": "Card payment recorded with supplier, amount and date", or "Declined charge logged".
- Card limits work as cards do. A charge over the limit is declined outright, never part-paid, so extra-zero and over-PO invoices show "Declined · Over the £X card limit" with £0 paid. The card stays open for the agreed amount.

### Controls (user, 21 Oct 2026)

Every round 2 payment is labelled with the control that handled it, shown as "What Corpay did · <control>":
- Merchant control: the card is locked to one supplier or merchant (supplier invoices, bank-change scams, lookalike suppliers, Connectwork vs the consumer networks, owned renewals).
- Spend category control: restaurants up to £150 a bill, rail fares up to £250 each, taxis up to £75 a journey.
- Amount limit: each single-use card is issued for the agreed amount, and a charge over it is declined (extra zero, over its PO).
- Single-use card: duplicates of an already-paid PO. The card closed after the first payment, so a second charge is declined.
- Card expiry: renewals with no owner.

### Physical card for in-person spend (user, 21 Oct 2026)

"In person payments would use a physical corpay card." Restaurant bills, rail fares bought at the ticket office and taxis are paid on the team's physical Corpay card, not a virtual one. When one of these is selected, the round 2 visual swaps the frosted virtual card for the plum Corpay Visa artwork from Figma (Card/flat-front, 41:6782). The team name sits where a cardholder name would, and the status badge sits top right. On phones the same card appears as a small thumbnail at the top of the opened row. Detail wording: "Card: Physical card · Sales team · restaurants up to £150 a bill" and "…so the £540 bill was declined at the till." Small in-person spend shows its rebate in pence (up to £0.96*).

### Round 2 interactions (until 5 Nov 2026, replaced by the instant reveal above)

Round 2 used to play itself at one payment a second, with a "Today’s payments" tab, an "Ongoing supplier payments" tab (monthly cards, limits, last three months and a yearly rebate summary), a detail panel with Card, What happened, Paid, Record, Schedule and Rebate rows, and previous/next arrows. The ongoing cards are still dealt, because the end screen's yearly rebate row uses them.

## End

- H2: Put the control in the payment.
- Body: Corpay cards carry merchant controls, spend category limits and amount limits, so the checks happen before the money moves. Supplier payments on card can earn up to 1% in rebates.*
- Buttons: Download the whitepaper (primary) · Talk to an expert (secondary) · Play again (link)
- Caveat and source lines as above.

## Prize draw (21 Oct 2026, user idea)

- Sits on the end screen, beside the results.
- Eyebrow: "Win a Christmas hamper for your team". H2 (user's line): "Finance doesn’t have to be this stressful."
- Body: "Leave your details and we’ll enter you into our prize draw for a Christmas hamper big enough for a team of up to ten. Everyone who plays can enter, whatever their score. The draw closes on 11 December 2026."
- Fields: first name, last name, work email, job title, company (all required). Job title added 26 Oct 2026; it sits beside Company.
- No tick boxes (Marketo team, 26 Oct 2026): entering the draw opts people in to marketing, following Corpay's usual Marketo process. One line sits above the button: "By entering, you agree to the prize draw terms and Corpay’s privacy policy. We’ll email you your score and your company leaderboard, plus insights, news and offers from Corpay. You can unsubscribe at any time." The terms link is a placeholder.
- Everyone who enters gets the score email and the colleague challenge. The Marketo team handles opt-in with its usual process.
- Legal to confirm that tying marketing opt-in to draw entry is acceptable.
- Button: "Enter the draw". Small print: "One entry per person. No purchase necessary."
- Success state: "You’re in the draw." Winner emailed by 18 December 2026, then the whitepaper visual and its CTA.
- Everyone who enters also sees "Challenge your colleagues": "Your score is on its way to your inbox. Share the game with your team. Once five other people from {Company} have played, your company leaderboard unlocks and we’ll email it to you." with a Copy link button. The player shares the link themselves; Corpay never emails colleagues they name (PECR refer-a-friend rules).
- Leaderboard unlock (user, 22 Oct 2026): only when five other colleagues have played, not counting the player, so six people from the company in all. Colleagues are matched by work email domain.
- Not wired: the review build's form is a mock that stores and sends nothing. The live page will use a Marketo form embed, with one hidden field that the game fills in on submit. The Marketo team is looking for an existing field to repurpose rather than creating one. The code that fills it ships inside the game file, so the web team only hosts it.
- Open for legal: draw T&Cs, hamper value and supplier, closing date and time, eligibility (UK, business entrants), and the consent wording, now that agreeing to the terms also opts people in to marketing.

## Tracking (5 Nov 2026)

Launch: 16 November 2026 on a Corpay UK Marketo landing page (same Marketo instance; the Corpay UK domain is being set up).

GTM is run by an external agency, so the game is tracked without needing a GTM change:
- **Address and title per step.** Each step rewrites the address with `history.replaceState` (`?step=…`, other query parameters such as UTMs are kept) and sets the page title. GA4 enhanced measurement ("page changes based on browser history events", on by default) counts each one as a page view. The back button is untouched. A reload starts on the intro, and the address goes back to having no step.
- Steps and titles: `email` (the month-end email opens), `example` (How to check a payment), `round-1`, `result`, `corpay` (What if you’d used Corpay?), `end` (Your results) and `entered` (In the draw).
- **In GA4:** Reports, Engagement, Pages and screens, then switch the first column to "Page title and screen class". Page path alone shows one page, because the step is a query parameter.
- **dataLayer.** The same steps push `campaign_*` events (`campaign_game_start`, `campaign_round_complete` with the result name as its label and correct calls as its value, `campaign_corpay_reveal`, `campaign_game_complete`, `campaign_draw_entry` with the result name, `campaign_cta_click` with label `whitepaper` or `talk_to_an_expert`, `campaign_play_again`), all with `campaign_name` = `payments_challenge`. Sculpt is setting up a new Corpay UK GTM container (brief from Josh, 5 Nov 2026) with GA4 for these events, draw entry as a key event, tags only after cookie consent and no personal data in GA4. None of the events or the address carries a name, email or company.
- The colleague share link drops `step`. It still carries the sharer's UTMs.
- GA4 only sees people who accept cookies. Draw entries and scores come through Marketo, so use those for the entrant numbers.

## How to enter and the prize (proposed 6 Nov 2026, for Josh and legal)

Won's new front: the intro has "Play the game" and "How to enter". "How to enter" opens a bottom sheet (a centred dialog on desktop). Figma: Flow section, "Mobile · 1c · How to enter (sheet open)" (2156:8615). Not in the game code yet.
- Intro body: "Every supplier payment and expense report needs your approval before the Christmas break. Take five with this mini game, and your team could win a Christmas hamper."
- Steps: 1. Play the game. It takes about two minutes, and any score counts. 2. Enter your details at the end, using your work email. 3. Share the game with your team. Once five people from your company have entered, you included, your team is in the draw.
- The prize: The Fortnum’s Family Christmas Hamper from Fortnum & Mason (RRP £250), to share with your team. Thirteen Christmas treats in a wicker hamper, including English sparkling wine, Malbec, biscuits and chocolate coins.
- Small print: The draw closes at 5pm on 11 December 2026, and we’ll email the winning team by 18 December 2026. Open to UK residents aged 18 or over. Prize draw terms apply.
- Team rule: five people in total from the same work email domain, the player included, in any order, counted in Marketo after the close. Replaces "for a team of up to ten" and the individual draw. Needs the terms rewritten and legal sign-off.
- The hamper contains alcohol, so entrants must be 18 or over. Check the product page again before launch, as the price and contents can change. Naming the hamper is fine; Fortnum & Mason photos or logos need permission.
- Behaviour: the cross, tapping outside, swiping down or Escape closes the sheet; "Play the game" in the sheet closes it and starts the game; the page behind doesn't scroll and focus stays in the sheet. On short phones the sheet scrolls inside, with the button kept in view.

## Version 2 (6 Nov 2026, from the Figma redesign; copy awaiting sign-off)

Figma: page "Sign-off Season game - Won", Flow section. This section overrides older notes below where they disagree.

- **Intro:** tags "Win a Christmas hamper for your team", "2-minute game", "No sign-up" above the headline. Body: "Every supplier payment and expense report needs your approval before the Christmas break. Take five with this mini game, and your team could win a Christmas hamper." Buttons: Play the game (opens Cara's email), How to enter. Prize tag: The Fortnum's Family Christmas Hamper, to share with your team, draw closes 5pm, 11 December 2026.
- **How to enter:** a dialog (a bottom sheet on phones) with three steps, the prize line, the dates and "Open to UK residents aged 18 or over". Its "Play the game" closes it and opens Cara's email. The hamper email in the inbox carries the team rule too.
- **Team entry:** a company's team is in the draw once five people in total from the same work email domain have entered, the player included. Counted in Marketo after the close. Needs legal sign-off.
- **Round 1 desk:** no round title or instruction on screen (a hidden heading keeps focus and screen readers). HUD: Time left, Paid out, Rebate earned, then the bar. One desk panel: Policy (left), the in-tray (centre, dark), Supplier file and Purchase orders (right). Policy is label and value rows: Supplier and account: On file; Amount: Same as its PO; Restaurants: Up to £150 a bill; Rail fares: Up to £250 each; Taxis: Up to £75 a journey; Software renewals: Supplier file: Not on it, Owner: Needs a current one; Ad spend: Network: Connectwork Ads only. Reject and Approve are docked under the card, with the keyboard hint below them. The Done list is gone.
- **Pressing or dragging a payment:** the card shrinks to 80%, the cards behind hide, and the tray splits into a Reject half and an Approve half down to each button; the half the card is over fills in and the other button dims.
- **Payments by type:** Email (sender monogram, address, External tag, message), Invoice for invoices, ad spend and renewals (blue letterhead bar, supplier monogram), Expense (torn receipt edge). The worked example is "Example email".
- **Result (round 1 and round 2 merged):** headline "You stopped n of 4." Subtitle is totals only, e.g. "Three problem payments got through, worth £X, and one good payment didn't go out.", then "You're not alone: 85% of CFOs believe…¹" (left out when every call was right). Two panels: Your desk and With Corpay, each with Correct calls, Paid in error, Held up and Rebate earned. Only wrong calls get a card: Missed (problem that got through, amount shown as a loss), Not checked (problem left in the tray), Held up (good payment rejected), Still in the tray (good payment the clock ran out on). With Corpay is blurred until "What if you'd used Corpay?", then fills in place: totals count up and each card shows Caught or Paid with the control. Then "Enter the prize draw", the rebate caveat and the ¹ source line. The separate round 2 screen, its tabs and the card visual are gone.
- **End:** banners for Corpay cards (Put the control in the payment, Talk to an expert) and the whitepaper (Download the whitepaper); Play again with an icon; rebate caveat. The score table and "Rebate a year on ongoing cards" are gone. Draw panel copy follows the team rule; the opt-in line no longer mentions a leaderboard; small print adds "Open to UK residents aged 18 or over". After entering: "You're in. Now get your team playing." with the share link and "We'll email the winning team by 18 December 2026."
- **Style:** no light-blue text; no middots in new on-screen copy ("How to check a payment: 2 of 5").

## Result names (built 6 Nov 2026)

The game names each result at the end of round 1, using the rules in campaign-plan.md (Email journey). The name starts the Marketo Person Notes line, which picks the E1 email, and it is the label on the round complete and draw entry events.
- **Sharp eye:** all four problems stopped, and every good payment approved.
- **Too cautious:** three or four problems stopped, but at least one good payment didn't go out. That includes one left in the tray when the clock ran out, because the Sharp eye email says every good payment went out on time.
- **Close call:** two or three stopped, and no good payment missed when three are stopped.
- **Swamped:** none or one stopped.
- Person Notes line, ready for the form: "{Result} · {n} of 10 · {£ paid in error} paid in error · {time taken}", for example "Close call · 6 of 10 · £0 paid in error · 1:03". The result names aren't shown on screen yet.

## Supporting band (below the game)

- 83% of UK CFOs say spend processes are still more manual than they should be.¹
- 99% of CFOs have experienced a real or attempted AP-related cyber incident in the last two years.²

Then the full corpay.com UK footer.

## Playable test (21 Oct 2026)

- Source: src.html, built by `python3 build.py` into approval-desk.html (artifact) and share/PaymentsChallenge.html + PaymentsChallenge.zip.
- Clock: 75 seconds since the game was halved on 22 Oct 2026 (10 payments, 4 problems). Before that it was two and a half minutes. It went 60 seconds (too quick), then 90 seconds, then two minutes when the user asked for more payments at two minutes max, then 2:30 on 22 Oct 2026 (user: "it's really hard to do in 2 minutes"). Decisions show no right or wrong until the result.
- Result copy is built from what got through. Four or five through gives a one-line total instead of a list.
- Round 2 no longer plays itself (5 Nov 2026): the rows land in about a second and a half, and the card only changes when a row is opened. It was about 10 seconds (1 second a payment) before.
- The fixed 20-payment build is kept as src-fixed-20.html.
- Card text (21 Oct 2026, user: "make the font smaller on the card stuff so it fits"): the virtual and physical card text is sized from the card width. That's a 20px name and 16px badge on the 440px card, so the longest name, Oakbridge Fleet Services, fits beside any badge. On a 390px phone it's 15.5px and 12.4px.
- Play-test: `node tools/playtest.mjs <outDir> [width height mobile]` plays every screen headlessly and saves screenshots.

## Company leaderboard (mapped 22 Oct 2026)

- Figma: section "Month-End Hell · Company leaderboard (draft)" on the game page. It has a seven-step journey from sharing the link to the final leaderboard, rules panels (ranking, what it shows, who can see it, open questions), and page designs: desktop locked, desktop unlocked and phone unlocked.
- Rules:
  - Unlocks only when five other colleagues have played, not counting the player.
  - A colleague counts once they finish and enter with a work email on the same domain.
  - Ranked by correct calls out of 10, then paid in error, then time taken. Each player's best game counts.
  - Names need a separate opt-in tick. Others show as "A colleague".
  - Private to opted-in players at the company. It never affects the hamper draw.
- Full campaign plan: campaign-plan.md, also in Notion (Marketing HQ / Delivery Hub), "Month-End Hell · The Payments Challenge campaign plan".

