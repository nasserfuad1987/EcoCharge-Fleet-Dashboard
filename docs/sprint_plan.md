# Two-Week Sprint Plan

**Project:** EcoCharge Fleet Dashboard
**Course:** ICS 432 – Software Engineering
**Organization:** EcoCharge Innovations

**Sprint Start Date:** October 26, 2026
**Sprint End Date:** November 8, 2026
**Sprint Duration:** 14 Days
**Assignment Deadline:** Sunday, November 8, 2026, at 11:59 PM

## 1. Sprint Goal

The objective of this sprint is to develop a functional web-based Electric Vehicle (EV) Fleet Dashboard that allows fleet managers to monitor predefined electric vehicles and estimate charging costs.

The project focuses on implementing two core features: a static fleet overview and a charging cost calculator. The sprint also emphasizes software testing, secure development practices, ethical considerations, Agile collaboration, and version control using GitHub.

## 2. Team Members and Responsibilities

| Team Member      | Primary Responsibility                                                     |
| ---------------- | -------------------------------------------------------------------------- |
| Nasser Anwahi    | Project setup, GitHub management, fleet overview, and documentation        |
| Sultan Allanjawi | Charging cost calculator, input validation, and application development    |
| Hamdan Albedwawi | Unit testing, security assessment, ethical analysis, and quality assurance |

All three members are responsible for reviewing code, participating in sprint discussions, and preparing the final demonstration.

## 3. Sprint Tasks and User Stories

| Task                                                              | User Story | Assigned Member  | Expected Evidence                                  |
| ----------------------------------------------------------------- | ---------- | ---------------- | -------------------------------------------------- |
| Create GitHub repository and develop static fleet overview        | US-01      | Nasser Anwahi    | Repository and fleet overview pull request         |
| Implement vehicle selection and charging cost calculator          | US-02      | Sultan Allanjawi | Calculator source code and pull request            |
| Implement server-side validation for charging duration            | US-03      | Sultan Allanjawi | Validation logic and error-handling tests          |
| Develop unit tests for positive, negative, and non-numeric inputs | US-04      | Hamdan Albedwawi | Unit test files and GitHub Actions results         |
| Review feature branches and merge pull requests                   | US-05      | All Team Members | Commit history, pull requests, and review comments |
| Prepare README, product backlog, and Agile documentation          | US-05      | Nasser Anwahi    | Project documentation                              |
| Conduct security risk assessment and ethical analysis             | US-05      | Hamdan Albedwawi | Security and ACM ethics memos                      |
| Prepare the five-minute project demonstration                     | US-05      | All Team Members | Final screen recording                             |

## 4. Two-Week Sprint Schedule

### Phase 1: Planning and Project Setup (October 26–27, 2026)

- Define the project scope, objectives, and expected deliverables.
- Identify user stories and acceptance criteria.
- Assign responsibilities to team members.
- Establish the proposed GitHub collaboration workflow.
- Prepare the initial product backlog and sprint plan.

### Phase 2: Fleet Overview Development (October 28–30, 2026)

- Create a predefined dataset of five electric vehicles.
- Implement vehicle IDs, models, battery percentages, and operational statuses.
- Design the dashboard interface using Flask, HTML, and CSS.
- Organize the fleet overview implementation in a feature branch.
- Review the feature against its acceptance criteria.

### Phase 3: Charging Calculator Development (October 31–November 2, 2026)

- Develop the vehicle selection and charging duration form.

- Implement the fixed charging cost calculation:

  **Cost = Charging Duration × 7.5 kW × $0.15/kWh**

- Implement server-side input validation.

- Ensure negative, non-numeric, and invalid values are rejected.

- Review the calculator implementation before integration.

### Phase 4: Testing and Security Assessment (November 3–4, 2026)

- Develop unit tests for the charging cost calculation function.
- Test positive, negative, zero, and non-numeric inputs.
- Examine boundary conditions and currency rounding.
- Conduct static code review to identify potential vulnerabilities.
- Perform dynamic testing to evaluate application behavior.
- Analyze input validation weaknesses and Cross-Site Scripting (XSS) risks.
- Document identified vulnerabilities, impacts, and mitigations.

### Phase 5: Ethical Analysis and Documentation (November 5–6, 2026)

- Prepare the security risk assessment memo.
- Evaluate potential privacy concerns involving future vehicle location tracking.
- Apply relevant principles from the ACM Code of Ethics.
- Complete the README, product backlog, and supporting documentation.
- Review GitHub commit history and pull request evidence.
- Verify that the project meets the assignment requirements.

### Phase 6: Final Review and Demonstration (November 7, 2026)

- Conduct the final application review.
- Verify the fleet overview and calculator functionality.
- Execute the automated tests and document their results.
- Complete the sprint retrospective.
- Record the five-minute demonstration.
- Review the final report and repository documentation.

### Phase 7: Final Submission (November 8, 2026)

- Confirm that the required source code is available in the GitHub main branch.
- Verify the README and supporting documents.
- Confirm that the final demonstration recording is accessible.
- Review the submission against the grading rubric.
- Submit all required materials before **11:59 PM**.

## 5. Scrum Ceremonies

| Scrum Activity       | Planned Date | Purpose                                                  |
| -------------------- | ------------ | -------------------------------------------------------- |
| Sprint Planning      | October 26   | Establish objectives, user stories, and responsibilities |
| Team Check-in 1      | October 29   | Review fleet overview development                        |
| Team Check-in 2      | November 2   | Assess calculator progress and integration               |
| Team Check-in 3      | November 5   | Discuss testing results, security, and documentation     |
| Code Review          | November 6–7 | Examine changes and verify functionality                 |
| Sprint Retrospective | November 7   | Reflect on successes, challenges, and improvements       |
| Sprint Completion    | November 8   | Final verification and assignment submission             |

## 6. Definition of Done

A sprint task is considered complete when:

1. The required functionality has been implemented according to its acceptance criteria.
2. Relevant code has been committed to GitHub with meaningful commit messages.
3. Applicable unit tests have passed successfully.
4. Errors and invalid inputs are handled appropriately.
5. The code has undergone the required review process.
6. Supporting documentation has been updated.
7. The completed functionality is ready for demonstration.

## 7. Expected Sprint Outcomes

By November 8, 2026, the team aims to deliver:

- A functional EcoCharge Fleet Dashboard displaying five predefined electric vehicles.
- A charging cost calculator using the required fixed formula.
- Automated unit tests and evidence of successful execution.
- A GitHub repository containing organized source code and documentation.
- Evidence of feature branches, meaningful commits, and collaborative pull requests.
- A security memo addressing two relevant vulnerabilities.
- An ethical analysis referencing the ACM Code of Ethics.
- A sprint retrospective documenting lessons learned.
- A five-minute demonstration covering the application and GitHub workflow.
