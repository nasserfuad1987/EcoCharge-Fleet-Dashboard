# Two-Week Sprint Plan

**Project:** EcoCharge Fleet Dashboard  
**Course:** ICS 432 – Software Engineering  
**Course Team 4:** Hamdan Mohammad Saeed Bin Salmin Albedwawi; Nasser Fuad Abdulla Ahmad Anwahi; Sultan Ibrahim Mohamad Allanjawi  
**Planned sprint:** October 26–November 8, 2026 (14 days)  

## 1. Sprint Goal

Build a simple, reliable web dashboard for a small electric-vehicle fleet. By the submission deadline, the application should show five predefined electric vehicles and allow a manager to calculate an estimated charging cost. We will also document our design decisions, test the calculation, consider security and ethics, and explain our GitHub workflow.

The application is a **prototype**: the vehicle data is static and the charging rate is fixed. It does not connect to real cars, chargers, or payment systems.

## 2. Planned Roles

- **Nasser Fuad Abdulla Ahmad Anwahi — Project coordination and documentation:** organize the repository, maintain the product backlog and sprint plan, help with the fleet overview, and check the final README.
- **Sultan Ibrahim Mohamad Allanjawi — Application development:** focus on the vehicle-selection form, charging formula, and handling invalid duration inputs.
- **Hamdan Mohammad Saeed Bin Salmin Albedwawi — Quality and responsible software:** focus on calculator testing, potential security risks, and the ACM ethics memo.
- **All members:** inspect the final features, review each other's actual work, and participate in the demonstration.

The team used the shared GitHub account `nasserfuad1987` for repository activity. Commits and pull requests document work completed through that account, while the planned member responsibilities describe the group's division of tasks; the platform does not distinguish individual contributions.

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

**November 5–6 — Documentation and code review:** complete the security and ethics memos, review the README, and document the potential bug prevented through code or testing.

**November 7 — Final review:** verify the features and test results, complete a retrospective from actual observations, and record the five-minute demonstration.

**November 8 — Submission:** check the repository's `main` branch, supporting documents, video access, and instructor-approved use of GitHub; submit before 11:59 PM.

**Schedule context:** The sprint dates represent the project plan. GitHub's recorded repository development begins on November 4, 2026.

## 5. Scrum Check-ins and Definition of Done

The simplified Scrum workflow covers sprint planning, task progress, integrating feature branches through pull requests, and reflecting on the sprint.

A task is done when its acceptance criteria are met; relevant changes and tests are saved in GitHub; the documentation is updated; and the required feature branches have been merged into `main`.

## 6. Deliverables and Evidence

- **Source code:** `app.py` plus related modules and interface files in the final `main` branch.
- **Feature history:** [PR #1](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/1) and [PR #2](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/2) are merged; [PR #4](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/4) merged the advanced implementation.
- **Automated testing:** [GitHub Actions evidence](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/actions/runs/41889860974) records 25 passing tests on `main`.
- **Written evidence:** backlog, retrospective, security and ethical analysis, and README in `docs/` and the repository root.
- **Demonstration design:** The demonstration outline covers the fleet, calculator, tests, and GitHub history.
