# Two-Week Sprint Plan

**Project:** EcoCharge Fleet Dashboard  
**Course:** ICS 432 – Software Engineering  
**Team:** Nasser Anwahi, Sultan Allanjawi, and Hamdan Albedwawi  
**Planned sprint:** October 26–November 8, 2026 (14 days)  
**Assignment deadline:** Sunday, November 8, 2026, at 11:59 PM (UAE time)

## 1. Sprint Goal

Build a simple, reliable web dashboard for a small electric-vehicle fleet. By the submission deadline, the application should show five predefined electric vehicles and allow a manager to calculate an estimated charging cost. We will also document our design decisions, test the calculation, consider security and ethics, and explain our GitHub workflow.

The application is a **prototype**: the vehicle data is static and the charging rate is fixed. It does not connect to real cars, chargers, or payment systems.

## 2. Planned Roles

- **Nasser Anwahi — Project coordination and documentation:** organize the repository, maintain the product backlog and sprint plan, help with the fleet overview, and check the final README.
- **Sultan Allanjawi — Application development:** focus on the vehicle-selection form, charging formula, and handling invalid duration inputs.
- **Hamdan Albedwawi — Quality and responsible software:** focus on calculator testing, potential security risks, and the ACM ethics memo.
- **All members:** inspect the final features, review each other's actual work, and participate in the demonstration.

These are **planned responsibilities**, not a statement that each person has already committed or reviewed code. Actual individual contributions should be linked to their GitHub commits or reviews.

## 3. Product Backlog and Sprint Tasks

**US-01 — Fleet overview (high priority).** As a fleet manager, I want to see vehicle IDs, models, battery percentages, and statuses so I can quickly understand the sample fleet. **Acceptance:** A single page lists 5–10 predefined vehicles with values in the required ranges. **Planned owner:** Nasser.

**US-02 — Charging estimate (high priority).** As a manager, I want to choose a vehicle and enter charging hours so I can estimate electricity cost. **Acceptance:** The form displays a result calculated as hours × 7.5 kW × $0.15/kWh; two hours must produce $2.25. **Planned owner:** Sultan.

**US-03 — Input validation (high priority).** As a user, I want incorrect durations to be rejected clearly so I do not receive misleading costs. **Acceptance:** Negative, non-numeric, and non-finite hours must not produce a price; the server returns an understandable error. **Planned owner:** Sultan.

**US-04 — Testing (high priority).** As a developer, I want repeatable calculator tests so I can detect calculation errors. **Acceptance:** Tests cover positive, negative, and non-numeric values; GitHub Actions records the results. **Planned owner:** Hamdan.

**US-05 — Documentation and review (high priority).** As an evaluator, I want to understand the project decisions and teamwork. **Acceptance:** The repository contains a README, product backlog, sprint plan, retrospective, security memo, ethics memo, and real pull-request records. **Planned owners:** Nasser coordinates documentation; all members contribute and review.

## 4. Planned Sprint Schedule

**October 26–28 — Planning:** agree on the two features, create user stories and acceptance criteria, divide responsibilities, and agree on the GitHub workflow.

**October 29–November 1 — Initial development:** prepare the static fleet and basic interface, then implement the fixed charging-cost formula.

**November 2–4 — Integration and testing:** connect the form to the calculation function, reject invalid values, run automated tests, and document potential weaknesses.

**November 5–6 — Documentation and peer review:** finish the two short memos, check the README, and request genuine teammate feedback on pull requests.

**November 7 — Final review:** verify the features and test results, complete a retrospective from actual observations, and record the five-minute demonstration.

**November 8 — Submission:** check the repository's `main` branch, supporting documents, video access, and instructor-approved use of GitHub; submit before 11:59 PM.

**Planning versus evidence:** The dates above are a proposed schedule. The visible GitHub commit history begins on November 4, 2026. Earlier work, meetings, and ownership should be reported as completed only if the team has separate supporting evidence.

## 5. Scrum Check-ins and Definition of Done

The team should use a planning discussion, short progress check-ins, pull-request reviews, and an end-of-sprint retrospective. Record dates and attendees only for meetings that actually happen.

A task is done when its acceptance criteria are met; relevant changes and tests are saved in GitHub; the documentation is updated; and a teammate has reviewed the changes where required.

## 6. Deliverables and Evidence

- **Source code:** `app.py` plus related modules and interface files in the final `main` branch.
- **Feature history:** [PR #1](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/1) and [PR #2](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/2) are merged; [PR #4](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/4) contains advanced improvements awaiting group review.
- **Automated testing:** [GitHub Actions evidence](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/actions/runs/41883696384) records 19 passing tests on the advanced branch.
- **Written evidence:** backlog, retrospective, security and ethical analysis, and README in `docs/` and the repository root.
- **Demonstration:** the five-minute recording must show the running features and genuine GitHub history; a script alone does not complete this deliverable.
