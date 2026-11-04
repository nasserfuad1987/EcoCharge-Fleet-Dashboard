# Team Contribution and Pull Request Guide

**ICS 432 — EcoCharge Fleet Dashboard**  
**Team:** Nasser Anwahi, Sultan Allanjawi, and Hamdan Albedwawi

The grading rubric rewards real collaboration, not simply the number of GitHub branches. Everyone should use their own GitHub account so their work is traceable.

## How to contribute using the GitHub website

1. Ask the repository owner to invite you under **Settings → Collaborators**. Accept the invitation.
2. Open a file you can meaningfully improve; use the pencil icon to edit it.
3. Select **Create a new branch for this commit and start a pull request** rather than modifying `main` directly.
4. Use a descriptive branch name, for example `docs/sprint-evidence` or `test/calculator-boundaries`.
5. Add a clear commit message that describes the actual change, such as `docs: clarify input validation rationale`.
6. Submit the pull request with: **what changed**, **why**, **how you verified it**, and **anything the reviewer should examine**.
7. Ask a different team member to open **Files changed → Review changes**, leave specific constructive feedback, and submit **Comment**, **Approve**, or **Request changes** as appropriate.
8. Respond to feedback, make necessary corrections, verify GitHub Actions, and then merge if approved.

## Focused review checklist for PR #4

- [ ] **Nasser:** Verify the dashboard lists exactly five predefined vehicles with valid battery percentages and statuses; check README and sprint documents.
- [ ] **Sultan:** Verify two hours produces $2.25 and that invalid hours cannot create negative or non-finite costs; check the backend form route.
- [ ] **Hamdan:** Inspect unit tests, integration tests, security headers, and both security and ethics memos; compare documentation claims with test evidence.
- [ ] **Reviewer:** Open [the successful 19-test run](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/actions/runs/41884746715) and confirm its result.
- [ ] **Merge owner:** Merge [PR #4](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/4) after real reviews and passing checks, then verify the tests on `main`.

These review assignments are **suggestions for tasks**, not proof of work done.

## Genuine review comment examples

A meaningful review should reference the actual file and behavior. For example:

- “I checked `calculator.py`: can the form bypass the maximum-hours rule if the request is sent manually? Please verify the route test.”
- “The fixed cost formula is correct for the assignment, but please label it as an estimate rather than actual charging expense.”
- “The security memo describes XSS prevention. I verified that the HTML template uses escaped Jinja values; please include a test citation.”

Do not post these example comments as though the observations were independently performed; examine the code first.

## Evidence register for the final report

| Member | Actual contribution / review | URL or commit | Date |
|---|---|---|---|
| Nasser Anwahi | [Complete after verifying] | [Link] | [Date] |
| Sultan Allanjawi | [Complete after verifying] | [Link] | [Date] |
| Hamdan Albedwawi | [Complete after verifying] | [Link] | [Date] |

**Important:** The current repository history is mainly attributed to the connected Nasser account. Do not fabricate individual authorship or backdate contributions. Add each student's genuine work as it happens.
