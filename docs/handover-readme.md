# The Payments Challenge: handover for Won

From Josh, 2 November 2026. This pack is everything you need to rebuild the game, do the design work on it and build it into Marketo. Read this first, then the game script.

## What's in here

**1-play/PaymentsChallenge.html**
The current game in one file, to check your version against. It works offline and sends nothing: the prize draw form is a mock.

**2-source/**
What the game is built from.
- `src.html`: all the HTML, CSS and JavaScript in one readable file. The fonts and images are placeholders such as `{{FONT_REG}}` and `{{CARD}}`. It has no `<html>` or `<head>` because it was written for a page viewer that adds them.
- `assets/`: GT America Standard Regular and Medium (Corpay's web fonts, internal use only), the Corpay logo SVG, the physical card and the whitepaper book (both exported from Figma at 2x).
- `build.py`: run `python3 build.py` in this folder to put the fonts and images into `src.html` and rebuild the single-file version.
- `tools/pool-doc.sh`: prints the 60-payment pool as tables, straight from the code, so you can check it against the game script.

**3-docs/**
- `game-script.md`: the spec. It has every line of copy, the stats and their source lines, the 60-payment pool, how each game is dealt and scored, round 2, the end screen and the prize draw.
- `campaign-plan.md`: the wider campaign. It covers the player journey, the emails, prize draw and consent, hosting and the open questions.

## What has to stay the same in your version

**Game logic** (all in `game-script.md`)
- Each play deals 10 payments from the pool of 60: 6 genuine and 4 problems, each problem a different kind. A bank-change email is in every game.
- The first payment is always genuine, and no two problems come back to back.
- Round 1 is 75 seconds. Players are scored on correct calls out of 10, then money paid in error, then time taken.
- Each game picks one of three desk sizes and scales the amounts. All totals and rebates are worked out in the code, never typed in, and never round numbers.

**Product accuracy**
- Round 2 shows Corpay card controls only: merchant controls, spend category and amount limits, single-use cards, and the physical card for in-person spend.
- No invoice matching, OCR or automatic reconciliation. Corpay only does those with an extra module.

**Copy, stats and legal**
- The copy isn't signed off yet, but please keep it as it is. If the design needs a change, flag it to Josh rather than rewriting it.
- Every stat keeps its source line, and the rebate keeps its caveat.
- Keep the corpay.com UK footer under the game as it is.

**Brand and build**
- GT America Standard, the Nightfall gradient for the game stage, 12px corners on containers and 8px on buttons, no pill shapes.
- The green "Locked" badge is off palette and already flagged.
- It has to work at phone width. On phones, the suppliers, POs and policy panel becomes a sheet.
- Keep the keyboard focus states and screen-reader labels that are in the current build.
- No server, database, localStorage or third-party scripts beyond Marketo's own form and tracking.

## Marketo build

With the UK Marketo team. What's agreed so far:
- **Page:** an Allstar Marketo landing page. The address is still to be confirmed.
- **Files:** the landing page template holds the HTML only. The JavaScript, CSS, fonts and images go into Design Studio as separate files, linked from the template. Marketo reads `${…}` in a template as its own variables, and the game's JavaScript uses that pattern about 200 times.
- **Testing:** Marketo's preview doesn't run the linked JavaScript, so test the game on an approved page.
- **Form:** the Marketo team's form is ready. Keep the game's own entry form for the design. On submit, the game fills a hidden Marketo form with `MktoForms2` and `form.vals(...)` and submits it. That needs the embed code from the Marketo team (base URL, Munchkin ID and form ID). The handler to hook into is under "Prize draw" in `src.html`. At the moment it stops at `preventDefault` and sends nothing.
- **Fields:** first name, last name, work email, job title and company, all required, with no tick boxes. Plus Person Notes (`MktoPersonNotes`), which gets a result line such as "Close call · 6 of 10 · £0 paid in error · 1:03".
- **Result names:** the game doesn't name results yet. The rules for Sharp eye, Too cautious, Close call and Swamped are in `campaign-plan.md`, under "Email journey". E1 picks its version from how the Person Notes line starts.
- **Person Notes:** each entry overwrites it, so check that nothing else writes to it or relies on it, for example a CRM sync.
- **Opt-in:** entering the draw opts people in to marketing, as agreed with the Marketo team. The wording above the button is in the game.
- **Cookies:** Munchkin tracking sets cookies, so the page needs the cookie consent set-up.
- **Links:** the prize draw terms links are placeholders until the terms page exists.
- **After 11 December:** a draw-closed version of the page, or the page comes down.

## Still open with Josh

- The line above the entry button still mentions "your company leaderboard". The leaderboard is parked, so the wording will change.
- "UK addresses only" still needs adding to the draw panel and the terms.
- Legal sign-off on the draw terms and the opt-in wording.
- The launch date (the target was 9 November) is likely to move.

## Working together

- Your version becomes the master for the game. Josh will stop changing his, so the two don't drift apart.
- If copy or game logic changes, update `game-script.md` too, so it stays the record of what's in the game.
- Share a first pass with Josh for sign-off before it goes live.
