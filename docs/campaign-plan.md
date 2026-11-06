# Month-End Hell: campaign plan

The plan as it stands on 2 November 2026, for anyone (human or Claude) picking up the campaign. Nothing is signed off yet. Anything marked proposed still needs agreeing. The working history is in `archive/` and isn't needed to run the campaign.

## At a glance

| | |
|---|---|
| Campaign | **Month-End Hell** (working name; check with the brand team before paid media) |
| Hero asset | **The Payments Challenge**: a browser game on a landing page. You sign off a desk of supplier payments by hand, then watch the same desk run on Corpay cards |
| Theme | 🎄 "Clear your desk in time for Christmas." Every supplier payment and expense report needs approving before the Christmas break, so the game is a two-minute break that also shows what the desk can get like |
| Prize | 🎁 A Christmas hamper big enough for a team of up to ten. Free prize draw, open whatever the score, UK addresses only |
| Audience (proposed) | UK finance leaders and their teams (CFOs, finance directors, AP and finance ops at £20m+ turnover businesses), plus Corpay UK customers |
| Business rationale | Lead gen |
| Channels | The game on an Allstar Marketo landing page, two launch emails and the entrant journey in Marketo, and a sales handoff. Social and other promotion to plan |
| Key dates | Launch 9 Nov 2026 (target; may move, 30 Oct) · L1 launch email 10 Nov · L2 reminder 1 Dec · E6 last call 8 Dec · draw closes 11 Dec · winner emailed by 18 Dec |
| Owners | As set on the Notion page |

## Objectives (proposed)

- Make finance teams feel the cost of manual sign-off, then show the same desk handled by Corpay card controls.
- Grow the marketing audience. Entering the draw opts people in to marketing, so the score email and the colleague challenge go to everyone who enters.
- Spread inside companies through the colleague challenge.
- Drive downloads of the whitepaper *The Card-First Approach to Spend Modernisation*, and Talk to an expert requests.
- Hand warm accounts to Sales: expert clicks and repeat players.
- Land the up to 1% rebate on supplier card spend, always with its caveat.

## Key messages

- "Clear your desk in time for Christmas." (campaign line and opening headline)
- "Every supplier payment and expense report needs your approval before the Christmas break. Take five with this mini game, then enter the draw to win a Christmas hamper for your team of up to ten." (opening screen)
- "Finance doesn't have to be this stressful." (prize draw)
- "Put the control in the payment." (end screen)
- Corpay cards carry merchant controls, spend category limits and amount limits, so the checks happen before the money moves.
- Up to 1% rebate on qualifying spend.* The caveat goes everywhere a rebate figure appears: "*Up to 1% rebate on qualifying spend. Subject to agreed card-based monthly volumes; actual rate depends on monthly spend. Illustrative, not guaranteed."
- Stats (Corpay research only), numbered in the order they appear:
  - 85% of CFOs believe their current payment processes increase the risk of error, fraud or off-policy spend.¹
  - 83% of UK CFOs say spend processes are still more manual than they should be.¹
  - 99% of CFOs have experienced a real or attempted AP-related cyber incident in the last two years.²
  - Sources: ¹ Censuswide survey (Feb 2026) of 300 UK CFOs with £20m+ turnover, for The Card-First Approach to Spend Modernisation. ² Censuswide × Corpay CFO Survey 2025 (UK findings), 150 CFOs, The Automation Deficit.
- Tone: Corpay UK tone of voice. No exclamation marks, rhetorical questions or dashes. "Corpay", never "Corpay Complete". UK spelling.

## The player journey

1. **Inbox:** under "🎄 Corpay Christmas prize draw", the headline "Clear your desk in time for Christmas." and the intro above. Beside it, a computer shows the player's inbox: Cara Pay's month-end email (Needs sign-off) at the top, the pinned hamper email from Corpay, the office closing at 5pm, a bank-change email (External) and Secret Santa. The prize tag overlaps the monitor. Every email and folder opens, including a Sent email asking the AP team for Secret Santa ideas for Cara.
2. **The month-end email:** ten payments worth £Xm need signing off before the 5pm bank cut-off, so the player has 75 seconds. Invoices need their supplier and account on the supplier file and the same amount as their PO. Expenses, software renewals and ad spend aren't on the supplier file, so they're checked against the policy. Four of the ten shouldn't go out. "Start the payment run" opens a five-step "How to check a payment" walkthrough with one example bad payment, then "Start the clock". Play again skips the walkthrough.
3. **Round 1 · your desk (75 seconds):** payments arrive one at a time. The player approves or rejects each one against the supplier file, purchase orders and the policy, which is grouped by payment type.
4. **Round 1 result:** "You stopped n of 4", with Correct calls (n of 10) and Time taken. The title reads "Finished early" or "Time's up". Every good payment that didn't go out is listed with why it was genuine (for example "matches PO-4417"), and holding up good payments gets its own line. "A clear desk for Christmas" only when all four problems are stopped and nothing good was held up. Lead stat: 85%.
5. **Round 2 · the same desk on Corpay:** it plays itself, one payment a second, and card controls stop all four problems. It shows the card spend and the up to 1% rebate. Each payment can be clicked to see the control behind it, and an Ongoing supplier payments tab shows the payments that repeat.
6. **End:** the score against Corpay, the CTAs (Download the whitepaper, Talk to an expert, Play again) and the prize draw form. After entering, every player gets a "Challenge your colleagues" share link.

## How the game works

**Payment pool:** 60 payments. Each game deals 10, so every game is different.
- **6 genuine:** 5 supplier invoices and 1 other: an in-person expense, a Connectwork Ads charge or a software renewal that has an owner.
- **4 problems, each of a different kind.** A bank-change email is in every game. The other three come from the remaining nine kinds:

| Problem kind | Type | Stopped on Corpay by |
|---|---|---|
| Bank-change email | Fraud | Merchant control: paid to the supplier's own card |
| Lookalike supplier | Fraud | No card exists for an unknown supplier |
| Duplicate of a paid PO | Error | Single-use card already used |
| Extra zero | Error | Amount limit: the over-limit charge is declined |
| Over its PO | Error | Amount limit: the over-limit charge is declined |
| Restaurant over £150 a bill | Off-policy | Spend category limit on the physical card |
| Rail fare over £250 | Off-policy | Spend category limit on the physical card |
| Taxi over £75 a journey | Off-policy | Spend category limit on the physical card |
| Software renewal with no owner | Off-policy | Card expiry |
| Ads on a consumer network | Off-policy | Marketing card locked to Connectwork Ads |

**Desk sizes:** each game picks one at random, and Play again always picks a different one.

| Desk | Round 2 card spend | Rebate (up to) | Largest payment |
|---|---|---|---|
| Small | £5.0m to £5.7m | £50k to £57k | up to about £1.17m |
| Medium | £7.1m to £8.1m | £71k to £81k | up to about £1.67m |
| Large | £10.1m to £11.0m | £101k to £110k | up to about £2.27m |

**Product accuracy rules (keep these in every asset):**
- Corpay doesn't match invoices to POs unless the extra module is bought. Round 2 shows card controls only, with no invoice matching and no automatic reconciliation.
- A charge over a card's limit is declined outright. It's never part-paid.
- In-person spend (restaurants, rail, taxis) goes on the team's physical Corpay card. Everything else is a virtual card.
- Cards control by merchant, spend category and amount, plus single-use cards and expiry. Never by head count or ticket class.
- Supplier and ad network names are made up. Connectwork Ads is the approved network; Feedloop, Snapreel and Pinstream are consumer networks.

## Prize draw and consent

- **Fields:** first name, last name, work email, job title and company, all required. No tick boxes.
- **Marketing opt-in:** entering opts people in to marketing, following the Marketo team's usual process. The line above the button reads "By entering, you agree to the prize draw terms and Corpay's privacy policy. We'll email you your score and your company leaderboard, plus insights, news and offers from Corpay. You can unsubscribe at any time."
- **UK addresses only:** the hamper can only be delivered to a UK address. The emails say so; the game's draw panel and the prize draw terms still need the same line.
- **Result field:** on submit, the game fills one hidden Marketo field with a line like "Close call · 6 of 10 · £0 paid in error · 1:03". It only picks the E1 version (by "starts with" the result name), and no score figures appear in emails. The field is Person Notes (SOAP API name MktoPersonNotes), confirmed by the Marketo team on 30 Oct. Each entry overwrites it, so nothing else should rely on it. The review build has a mock form that stores and sends nothing.
- **Sharing:** players share the link themselves. Corpay never emails colleagues they name (PECR refer-a-friend rules).
- **Dates:** the draw closes on 11 December 2026, and the winner is emailed by 18 December.

## Hosting

- The game goes on an **Allstar Marketo landing page**, through the UK Marketo team (asked on 29 October). It can't go on the main corpay.com site, and the UK only has Allstar Marketo pages.
- It's one HTML file of about 470 KB with its fonts and images built in, and no server code or database. It works on any address: the share link uses the page's own address, and its corpay.com links are ordinary links out.
- **The Marketo team to confirm:** that a landing page template can hold it, the page address, the form's embed code (the form is ready, and the result goes in Person Notes), and cookie consent (Munchkin tracking runs on the page).
- Live and tested by 9 November, a day before L1. After the draw closes on 11 December, the page switches to a draw-closed version or comes down.
- The launch version has no leaderboard.

## Email journey

Built around the four result names. Only {First name} and {Company} come from the form, no email shows figures from the player's game, and rebate copy is the generic "up to 1% back on qualifying supplier spend*". Every preview names the game.

**After entry**

| Email | When | Who | Subject | Preview |
|---|---|---|---|---|
| E0 · You're in the draw | Straight away | Everyone who enters | You're in the draw, {First name} | Thanks for playing The Payments Challenge. The hamper draw closes on 11 December and is open to UK addresses only. |
| E1 · Sharp eye | 10 minutes after entry | Result starts with Sharp eye | Sharp eye, {First name}: nothing got past your desk | In The Payments Challenge you stopped every problem and got every good payment out on time. Here are the same payments on Corpay. |
| E1 · Too cautious | 10 minutes after entry | Result starts with Too cautious | Too cautious, {First name}: your suppliers are still waiting | Nothing got past you in The Payments Challenge, but some good payments didn't go out either. On Corpay, they go through and the problems stop. |
| E1 · Close call | 10 minutes after entry | Result starts with Close call | Close call, {First name}: a few problems slipped through | What got past you in The Payments Challenge tends to get past busy desks at month-end too. Here's how card controls stop it. |
| E1 · Swamped | 10 minutes after entry | Result starts with Swamped | Swamped, {First name}: month-end doesn't have to feel like this | The Payments Challenge gives you 75 seconds to check ten payments by hand. Here are the same payments on Corpay, where the cards do the checking. |
| E2 · Your team's turn | Day 3 | Everyone who entered | Your team's turn at the desk, {First name} | Send them The Payments Challenge before the hamper draw closes on 11 December. |
| E5 · Corpay cards (prospects) | Day 7 | Prospects who entered | Up to 1% back on supplier spend you already make* | Like round 2 of The Payments Challenge, but with your own suppliers: Corpay cards can earn up to 1% back on qualifying supplier spend.* |
| E5 · Your Corpay cards (customers) | Day 7 | Customers who entered | The controls from round 2 are already on your cards | The merchant, spend category and amount limits from round 2 of The Payments Challenge: set up once, working on every payment. |
| E6 · Draw closes soon | 8 December | Everyone who entered | Three days left for your team to enter, {First name} | The hamper draw closes on 11 December. Share The Payments Challenge before it does. |
| E7 · Hamper winner | By 18 December | Everyone who entered | The Payments Challenge hamper draw has closed | Thanks for playing. The winner has been contacted. |

- **E1 versions:** the game works out the result. Sharp eye if 4 of 4 are stopped and nothing is held up; Too cautious if 3 or 4 are stopped but a good payment is held up; Close call if 2 or 3 are stopped; Swamped if 0 or 1. Everyone with the same result gets the same copy: what the result means, the Corpay controls that stop problems on the card, the generic up to 1%*, and the share link.
- **Customer E5:** the three controls from the game and how to use them on their own cards; where else cards fit (recurring suppliers, software renewals, ad spend); single-use cards and card expiry; no rebate figures. Buttons: "Talk to your account manager" and Download the whitepaper. Customer or prospect comes from Marketo's customer list, not the form.
- E3 and E4 (the leaderboard emails) are parked with the leaderboard.

**Launch emails** to existing contacts who haven't played

| Email | When | Who | Subject | Preview |
|---|---|---|---|---|
| L1 · Launch invite (prospects) | Tue 10 November | Prospects | Win a Christmas hamper for your team | Play The Payments Challenge, our 75-second mini game, to enter. Everyone who plays can enter the draw, whatever their score. |
| L1 · Launch invite (customers) | Tue 10 November | Corpay UK customers | Win a Christmas hamper for your finance team | A thank-you for the year: play The Payments Challenge, our mini game, to enter the draw for a hamper for your team. |
| L2 · Reminder (prospects) | Tue 1 December | Prospects who haven't played | Ten days left to win a Christmas hamper for your team | Take on The Payments Challenge: sign off the December payment run in 75 seconds, then enter the draw. |
| L2 · Reminder (customers) | Tue 1 December | Customers who haven't played | Ten days left for your team to win a Christmas hamper | Share The Payments Challenge with your finance team before the draw closes on 11 December. |

- **Audiences:** two Marketo smart lists, checked before each send. Prospects are UK finance contacts opted in to Corpay marketing who aren't customers. Customers are finance contacts at Corpay UK customers, with their account managers told before each send. Both leave out anyone who has entered; anyone who enters joins the journey at E0 and drops out of L2.
- **Prospect emails:** the prize first, then how the game works (ten payments, 75 seconds, four that shouldn't go out, then the same desk on Corpay cards), the GIF and a second button. L2 adds the countdown and, only with the real Marketo figure on the day, how many finance teams have played.
- **Customer emails:** open as a thank-you for the year, not a sales pitch. Round 2 shows the controls they already have, with a line pointing to their account manager. No rebate figures, because a customer's rebate depends on their own agreement. L2 adds sharing with the team.
- **All four:** no rebate figure in the subject and no figures from anyone's game. Each link carries its own UTM (launch-1, launch-2, launch-1-customer, launch-2-customer). L1 goes the day after launch, so the live page and form get a day's check first.

**Email template:** one simple layout for every email, in Figma section "Month-End Hell · Email template (simple)" (desktop 600 and phone 375, shown with L1 for prospects).
- A 1200 × 600 header image with no words: a hint of the game desk on the Nightfall stage, with the Corpay logo.
- It leads on the prize: the subject line as the headline, a prize paragraph and a black "Play and enter the draw" button.
- Then "How The Payments Challenge works": one paragraph, a GIF of four payments being approved and rejected with a cursor click (784 KB; the first frame is a full payment card, because Outlook on Windows shows only the first frame), and a second button.
- Small print: "The hamper can only be delivered to a UK address. Prize draw terms apply. One entry per person." The footer has the Allstar FCA line word for word, and every marketing email has an unsubscribe link.
- Each mock starts with a grey "Inbox details" strip (game name, which email, subject and preview) for the Marketo build. It isn't part of the email.
- The game is named in paragraph 1, the subhead and every preview. If the name changes, those places change, along with the E7 subject line.

**Every email:** the rebate caveat sits beside any rebate figure, survey stats carry their source line, and buttons on gradient bands are black.

**Hand to Sales:** a Talk to an expert click in any email creates a CRM task for the account owner with the player's result. For customers, it goes to their account manager. E5 and E6 pause for that contact once Sales is in touch.

## Company leaderboard (parked for launch)

Not in the launch version. Won (designer) is looking at building it with its own data store, and where that data lives needs agreeing first. The rules designed for it:
- It unlocks when five other colleagues have played (six people from one company). A colleague counts once they finish and enter with a work email on the same domain. Personal email domains don't count.
- Ranked by correct calls out of 10, then the least paid in error, then the fastest time. Each player's best game counts, and ties share a position.
- Names show as first name and last initial only with a separate opt-in tick. Everyone else appears as "A colleague".
- Only players at that company can see it, through a private link in E3 and E4. It's never public, it freezes when the draw closes, and it never affects the hamper draw.

## Promotion (to plan)

- **Email:** L1 and L2 (see Email journey).
- **LinkedIn:** organic and paid, using the inbox opening and a short gameplay clip.
- **Sales:** the share link in outreach and account-based plays.
- **Website:** a corpay.com UK banner linking to the game during December, to ask the web team.

## Deliverables and status

| Deliverable | Status | Where |
|---|---|---|
| Playable game | Internal review, version 37 (2 Nov) | https://claude.ai/artifact/3cJNV73ztYbtoGLJJi6gTA (shared with specific people) |
| Game files | Version 37 | share/PaymentsChallenge.html and share/PaymentsChallenge.zip |
| Game script (all copy and the 60 payments) | Current | game-script.md |
| Game feedback form | Live | Notion: The Payments Challenge · Game feedback |
| Game storyboard, inbox opening and walkthrough (desktop and phone) | Draft, awaiting sign-off | Figma page "21 Oct 26 - The Payments Challenge game" |
| Email journey map | Draft, awaiting sign-off | Same Figma page |
| Email template | Mocked up with L1 for prospects, awaiting sign-off | Same Figma page |
| Email builds (L1, L2, E0 to E7) | Not started | Marketo |
| Landing page | Asked the UK Marketo team for an Allstar Marketo landing page (29 Oct) | |
| Marketo form | Ready (30 Oct). The result goes in Person Notes (MktoPersonNotes). Waiting for the embed code, then it's wired into the game | |
| Company leaderboard | Parked for launch; Won investigating | Same Figma page |
| Promotion assets | Not started | |
| Real hamper photo | Needed once the supplier is chosen | |

Figma: https://www.figma.com/design/Bs0eReHhT8hFRLNG4jl8Gj/CPC-Claude-design?node-id=1535-6929

## Measurement (proposed)

- **Funnel:** landing page visits → plays started → round 1 finished → round 2 seen → draw entries
- **Email:** open and click rates for each launch email and each E1 version, and unsubscribes
- **Spread:** share links copied and colleagues brought in
- **Outcomes:** whitepaper downloads, Talk to an expert clicks, Sales handoffs, opportunities
- **Campaign codes and UTMs:** TBC

## Key decisions

- The game: 10 payments dealt from a pool of 60, four of them problems, with 75 seconds on the clock. Scored on correct calls, then paid in error, then time taken.
- Round 2 shows card controls only: merchant, spend category and amount, plus single-use cards and expiry. No invoice matching, because it needs an extra module. In-person spend goes on the physical card.
- Corpay stats only, made-up suppliers and ad networks, and amounts that never look round.
- The prize is a hamper for a team of up to ten, by free draw, open whatever the score, UK addresses only.
- Entering opts people in to marketing (the Marketo team's process), so the form has no tick boxes.
- One hidden Marketo result field. It only picks the E1 version, and no score figures appear in emails.
- Emails lead on the prize, share one simple template and name the game. Prospects and customers get their own launch emails and E5, and customers' expert clicks go to their account manager.
- Hosting is an Allstar Marketo landing page through the UK Marketo team, not the main corpay.com site.
- The leaderboard and its emails (E3, E4) are parked for launch.
- The game is called The Payments Challenge (2 Nov). "Month-End Hell" is still a working name for the campaign.

## Proposal for sign-off: two prizes

Proposed on 26 Oct 2026. Nothing here is built.
- **Prize 1 · 🎁 Christmas hamper:** the free prize draw, as above.
- **Prize 2 · January Pick Me Up:** for the best-performing team (colleagues on the same company email domain), judged in January. The hamper stays the hook; the team prize is a second line, for example "Plus, the best-performing team wins a January Pick Me Up."
- **Team scoring (proposed):** each player's best game counts; the team score is the average correct calls, so a big company can't win on numbers alone; at least six players to qualify; ties broken by lower average paid in error, then faster average time, then more players. Closing and judging dates to set, for example closing 8 January 2027 with the winner told by 15 January.
- **Data:** the one Marketo result field keeps every score from launch, so a team ranking can be worked out later.
- **Knock-on changes:** the game's prize screen, hamper email and end screen add the team prize line; E2 and E6 point to the team prize and a new E8 announces the winner; the leaderboard would need building by early January; Mkt Timelines run into January 2027.
- **Legal:** a prize for the best score is a skill competition, not a draw, so it needs its own terms (what counts as a team, scoring and tie-breaks, who can enter, closing date, prize), and scores are kept until judging with a deletion date after.
- **To sign off:** the two-prize structure, the team scoring rules, the dates, the prize and budget, and the competition terms.

## Open questions and sign-off

- **Legal and compliance:**
  - Prize draw terms (the link is a placeholder): hamper value and supplier, eligibility (UK addresses only) and closing time.
  - With a "challenge" name, the terms and draw copy need to make clear that the hamper is a random draw, not won on score.
  - Marketing opt-in on entry with no tick box: confirm it's acceptable, the wording above the button, and how to handle sole traders or personal email addresses.
  - The line above the button still promises "your company leaderboard", which is parked for launch.
  - "Up to 1%*" in the E5 subject line, where the caveat can't sit beside it.
  - E0 and E7 as service emails.
  - Data retention.
  - The corpay.com regulatory paragraph in the game footer lacks "Limited".
  - If the leaderboard is built: the name opt-in tick, and whether colleagues who unsubscribe still count.
- **Payment sizes:** keeping the rebate bands at 10 payments puts single payments up to about £1.17m on the small desk and £2.27m on the large one. The alternative is to cap payments at £750k, which roughly halves the rebates.
- **Product:** the duplicate outcome assumes the supplier re-charges the same single-use card; confirm the single-use and expiry claims.
- **Brand:**
  - The campaign name.
  - The game name, The Payments Challenge, is generic on the logo test, so keep Corpay next to it.
  - Christmas emoji and snowfall on a Corpay page.
  - The off-palette green "Locked" badge.
  - Made-up supplier names that may match real firms.
  - Cara Pay, the made-up finance director, as a nod to Corpay.
  - A Corpay-branded game on an Allstar web address.
- **Hosting and build (Marketo team):** the landing page and its address, the form's embed code, cookie consent, and the draw-closed version for 11 December. Also check that nothing else writes to or relies on Person Notes (for example a CRM sync), since each entry overwrites it.

## Campaign results

To fill in after launch.

## Lessons learned

To fill in after launch.
