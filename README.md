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

Feature branches:
- `feature/fleet-overview` — Flask page, sample vehicles, charging form.
- `feature/cost-calculator` — calculator tests, GitHub Actions, project documentation.

**Pull requests:** [Fleet Overview PR #1](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/1). Add the second PR link and record actual review/merge history after teammates review.

**Team members:** [Add real names, GitHub handles, and individual contributions]
**Sprint dates:** [Add actual two-week period]

> Branch creation and PR authorship by one account do not by themselves demonstrate a 3–4-person collaboration. Have each teammate make meaningful changes and complete actual peer reviews, and show these in the demo.

## Documentation

- [Product Backlog](docs/product_backlog.md)
- [Sprint Plan](docs/sprint_plan.md)
- [Sprint Retrospective Template](docs/sprint_retrospective.md)
- [Security Memo](docs/security_memo.md)
- [ACM Ethics Memo](docs/ethical_considerations.md)
- [Demo Outline](docs/demo_script.md)

## Notes

- All displayed costs are in USD and use fixed assignment rates; these are **not live electricity tariffs**.
- The selected vehicle does not affect the fixed-rate formula.
- The original Colab implementation is available via the separately shared course notebook.
- Before real deployment, add authentication, authorization, and privacy controls.
