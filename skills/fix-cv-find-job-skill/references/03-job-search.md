# Phase 3 — Job search and match table

Survey everything first, rank it, and only then apply. Applying as you find
openings wastes the best applications on whatever happened to appear first.

## Before searching, collect the parameters

Ask in one grouped block, not one question at a time:

1. **Which platforms.** Name the ones they use. General boards, industry-specific
   boards, company career pages, professional networks, recruitment agencies,
   public sector portals. Whatever their field actually uses. For each one, ask
   how to check whether they already applied there — an "applied jobs" list, a
   search filter, an application history page. Record it per platform; phase 4
   uses it for the duplicate check before every application.
2. **They must already be logged in** on every platform named. Say this plainly:
   this skill never creates accounts and never enters passwords. Ask them to log
   in now, in this browser, before continuing.
3. **Salary — a table, not one figure.** What the applicant wants to earn
   depends on seniority and on market, so collect it as a table: one row per
   seniority level × market combination they might realistically apply under. A
   "market" is whatever actually changes the number for them — a country, a
   region, a remote-versus-local split.

   | Seniority | Market | Target | Floor | Currency |
   |---|---|---|---|---|

   If they do not know a figure for a row, search for the going range for that
   seniority and market, present it with where it came from, and only fill the
   row in once they accept it or adjust it. Never fill a row from a search
   result without their sign-off.

   Also ask, once, for the **range anchor**: when a posting publishes a range
   instead of asking for a figure, do they want it read as the bottom, the
   middle, or the top? Record that decision now — it applies every time a
   posting has a range, not decided fresh each time.
4. **Target seniority.** Which level they are aiming at, which they will accept,
   and confirm: they will not apply below this floor even when a lower-level
   posting otherwise scores well. A posting's own stated seniority still governs
   which salary row and screening answers apply to it — see below — but it
   never lowers the floor on which postings are worth applying to at all.
5. **Location and arrangement.** Remote, hybrid, on-site, willing to relocate,
   commuting radius, time zones they can work.
6. **Hard disqualifiers.** The requirements they genuinely cannot meet. Language
   level, a licence they do not hold, a clearance, night shifts, travel, a
   physical requirement, a visa status. These become automatic discard filters.
   When one of these fires against a real posting, record the posting's own
   wording for the requirement as evidence next to the discard — not a
   paraphrase — so the discard is checkable later.
7. **Exclusions.** Companies they will not work for, or have already applied to.

## The salary rules

- Free-text field → write the equivalent of "negotiable" in the posting's
  language, unless the user told you to always state a number.
- Field that forces a value → look up the row in the salary table for the
  **seniority stated in the posting** (not the applicant's own) and the market
  that posting belongs to, and use that figure. A junior posting gets the
  junior row's number, in that market.
- If the posting gives a range → use the range-anchor decision recorded during
  parameter collection — bottom, middle or top. Never decide it per posting and
  never fall back to a default that was not explicitly chosen.
- **Currency conversion is mandatory.** A numeric field is read in the posting's
  local currency. Writing a figure in the wrong currency reads as an error to
  the employer and gets the application discarded. Convert before writing.
- Try free text first. Only fall back to a number when the validator rejects it.

## Searching

Search each platform for postings matching the target roles from phase 1, using
the vocabulary of that market — including the alternative titles identified in
the audit, which is where most people's search goes wrong.

Prefer recent postings. Anything older than roughly six weeks in a fast market
is likely filled; judge by the norms of the field.

Group tabs so several postings can be read at once, and read the full posting
rather than the search-result snippet. Digest emails and listing previews are
routinely truncated and routinely misleading.

## Scoring the match

Score each opening out of 100 and show the reasoning, not just the number.

**Raises the score:** strong overlap with the user's core skills and tools;
required experience inside the user's actual range; the location and arrangement
they want; the pay band at or above their floor; an industry they already know;
requirements the CV can evidence directly.

**Lowers the score:** required experience well above theirs; a hard credential
they lack; a specialisation outside their history; a stale posting; an
arrangement that does not suit; pay below their floor.

**Discard outright, and record why:** any hard disqualifier from the parameters
— with the posting's own wording kept as evidence next to the reason; postings
below the applicant's own stated seniority floor, even when otherwise a strong
fit; postings that are closed, filled or expired; duplicates of something
already applied to, checked with that platform's own duplicate-verification
path from the parameters; anything requiring account creation or a paid
service to apply.

The discard list goes in the report. A user who sees *eleven openings discarded
for requiring a licence you do not hold* learns more about their market than one
who only sees the matches.

## The table

Sort best match first.

| # | Company | Role | Link | Match | Why | Keywords to carry | Posted | Status |
|---|---|---|---|---|---|---|---|---|

Follow it with:

- **Discarded**, grouped by reason.
- **Needs a decision** — genuinely borderline ones, with the trade-off stated.
- **Patterns worth knowing** — a credential that keeps appearing, a tool the
  market wants that the user lacks, a title that returns better results than the
  one they were searching. This is often worth more than any single application.

Update the campaign brief with everything found.

## Close the phase

> Here is the full survey, ranked. Nothing has been sent.
>
> Want me to apply to these? I can go through them in order, and you can tell me
> to skip any of them.

Wait for the answer. If yes, go to `references/04-auto-apply.md`.
