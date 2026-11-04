# Reference Assignment Review and Improvements

**Purpose:** Use the previous ICS 432 submission as a benchmark for structure and clarity, not as code or text to copy.

**Reference sources:**
- Previous group's 15-page *ICS432 Assignment 2 Report* (provided for comparison).
- [Previous group's GitHub repository](https://github.com/s-m76/ICS432_A2).

## What the reference demonstrates

The previous group organized its report around project setup, Agile planning, testing, security, ethics, and the final demonstration. It illustrated the fleet table and calculator with screenshots and described three calculator tests. That organization is useful because an evaluator can connect each deliverable to supporting evidence.

## Important differences in our project

**1. Stronger validation in the actual application.** The reference's browser example accepted negative charging hours, although its separate testing file rejected them. Our application's backend uses the same validated charging function exercised by unit tests and HTTP integration tests, so negative hours do not produce a price.

**2. More reproducible testing.** The reference described three tests and reported their results. Our advanced branch contains 12 calculator unit tests plus seven HTTP integration tests. A [successful GitHub Actions run](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/actions/runs/41883696384) verifies all 19. Passing tests support the tested behaviors but do not prove the application has no bugs.

**3. Better separation of files.** The advanced EcoCharge code separates static fleet records, the calculation function, Flask routing, and page styling. This makes the small project easier to inspect and maintain.

**4. More specific security evidence.** The previous dashboard included an embedded tunneling credential in its published code. We deliberately do not copy that credential, use an external tunnel, or suggest exposing the development server publicly. We discuss practical threats such as invalid inputs and XSS without claiming that a small prototype is production-ready.

**5. Clearer limitations and ethics.** We distinguish fixed demonstration data from real fleet telemetry, and discuss why using future location information would require privacy safeguards and restricted access.

## What we still need to finish

A stronger write-up does not replace evidence. Before submission we need real contributions/reviews from group members, the advanced changes reviewed and merged into `main`, confirmation of the final tests on `main`, and a five-minute recording demonstrating the actual working interface.

**Academic integrity:** This review summarizes observations about the reference. Our application code, documentation and analysis should remain our own work. The previous group's names, code, screenshots, and credentials must not be presented as ours.
