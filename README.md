# EcoCharge Fleet Dashboard

**ICS 432 — Software Engineering** | EcoCharge Innovations | Educational prototype

A lightweight Flask web dashboard for monitoring a fixed sample of five electric vehicles and estimating charging costs. Battery percentages and statuses are **static illustrative data**, not live vehicle readings. All sample models are battery-electric vehicles.

## Features

1. **Fleet Overview:** Lists vehicle ID, model, battery percentage, and status.
2. **Charging Cost Calculator:** Select a vehicle, enter 0–24 hours, and estimate cost using:
   `Cost (USD) = hours × 7.5 kW × $0.15/kWh`
   The calculator rounds to two decimal places using decimal half-up rounding.
3. **Validation:** Rejects negative, non-numeric, non-finite, and greater-than-24-hour durations. This upper limit is a prototype design choice.

## Setup and application demonstration

The dashboard is a Flask application. GitHub stores its source code and automatically runs tests, but does not host the interactive website. To demonstrate both required features in the five-minute recording, run the application in a Python environment (or use the separately shared Colab prototype, which may differ from the latest GitHub version).

Requires Python 3.10+.

```bash
python3 -m pip install -r requirements.txt
python3 app.py
```

## Unit Tests

```bash
python -m unittest discover -s tests -v
```

The tests check positive and fractional hours, currency rounding, and rejection of negative, non-numeric, non-finite and excessive values. GitHub Actions is configured to run tests on pushes and pull requests.

### Potential bug identified and prevented

HTML input restrictions can be bypassed by manually crafted HTTP requests. Without server-side validation, a negative charging duration or `NaN` could yield a misleading charge or crash the calculation. The Python function converts inputs to `Decimal`, checks finite values and the allowed range, and raises a `ValueError` for invalid input. The web route renders a friendly error. The tests target this behavior.

## GitHub Collaboration

**Project team:** Nasser Anwahi, Sultan Allanjawi, and Hamdan Albedwawi.

**Planned sprint:** October 26–November 8, 2026 (14 days). **Submission deadline:** November 8, 2026, at 11:59 PM.

### Planned responsibilities

- **Nasser Anwahi:** Repository coordination, fleet overview, README, and Agile documentation.
- **Sultan Allanjawi:** Charging calculator, server-side validation, and application development.
- **Hamdan Albedwawi:** Unit testing, security risk assessment, ethical analysis, and quality assurance.

### Feature branches and pull requests

- `feature/fleet-overview` — Fleet overview and initial Flask application. [Pull Request #1 (merged)](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/1).
- `feature/cost-calculator` — Automated tests, GitHub Actions, and project documentation. [Pull Request #2 (merged)](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/2).
- `improvement/security-testing-report` — Enhanced application structure, validation, security analysis, and expanded testing. [Pull Request #4 (open for review)](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/4).

**Testing evidence:** [GitHub Actions — 19 successful tests](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/actions/runs/41868004476).

GitHub is being used instead of GitLab with the instructor's approval. Team members should document their actual code contributions and independent pull-request reviews before submitting; assigning responsibilities does not establish that those tasks have been performed.

## Documentation

- [Product Backlog](docs/product_backlog.md)
- [Sprint Plan](docs/sprint_plan.md)
- [Sprint Retrospective Template](docs/sprint_retrospective.md)
- [Security Memo](docs/security_memo.md)
- [ACM Ethics Memo](docs/ethical_considerations.md)
- [Demo Outline](docs/demo_script.md)
