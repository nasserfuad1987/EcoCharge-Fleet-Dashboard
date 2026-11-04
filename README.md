# EcoCharge Fleet Dashboard

**ICS 432 - Software Engineering | EcoCharge Innovations | Educational prototype**

A responsive Flask web dashboard for monitoring **five predefined battery-electric vehicles** and estimating charging cost. The dashboard demonstrates software quality, collaboration, security and ethical foresight—not a production fleet service.

## Required features

**Feature A - Static Fleet Overview:** Each row shows vehicle ID, model, battery percentage and status (Available, Charging or On Trip). Accessible native battery meters and summary cards make the fixed data easier to understand.

**Feature B - Charging Cost Calculator:** A manager selects a vehicle and enters a duration. The deliberately fixed formula is:

```text
Estimated cost (USD) = charging duration (hours) x 7.5 kW x $0.15/kWh
```

2 hours = $2.25; 5 hours = **$5.63** (Decimal, ROUND_HALF_UP). The selected vehicle does not change the tariff. Inputs must be finite numbers from 0 to 24 hours, inclusive; these bounds are a prototype choice.

## Setup and application demonstration

The dashboard is a Flask application. GitHub stores its source code and automatically runs tests, but does not host the interactive website. To demonstrate both required features in the five-minute recording, run the application in a Python environment (or use the separately shared Colab prototype, which may differ from the latest GitHub version).

Requires Python 3.10+. Clone or download this repository first. From the project folder:

```bash
python3 -m pip install -r requirements.txt
python3 app.py
```

## Test and analyze

```bash
python -m unittest discover -s tests -v
python -m compileall -q app.py calculator.py fleet.py
```

**Unit tests:** `tests/test_calculator.py` targets only cost calculation as required, including boundary and invalid-value cases.

**Additional integration tests:** `tests/test_routes.py` checks real Flask GET/POST behavior, vehicle allowlist, invalid and boundary inputs, HTML escaping, security headers, request size and unknown routes. **Verified CI evidence:** [GitHub Actions run 41889004694](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/actions/runs/41889004694) completed successfully with **25/25 tests** (12 unit + 13 Flask integration).

**Defect prevented:** A crafted HTTP request can bypass browser numeric controls. Without server validation, `-8` hours would incorrectly yield -$9.00. `calculator.py` rejects negative, nonnumeric, nonfinite and over-limit values; the Flask handler displays an error. See [Code Review](docs/code_review.md).

## Project structure

```text
app.py                       Flask routes, form handling, security headers
calculator.py                Pure Decimal charging-cost function
fleet.py                     Five fixed BEV records and allowed IDs
templates/index.html         Jinja page (autoescaped dynamic output)
static/styles.css            Responsive visual design
tests/test_calculator.py     Cost logic unit tests
tests/test_routes.py         Web route integration tests
.github/workflows/tests.yml  GitHub Actions testing
docs/                        Agile plan, ethics, risk analysis, evidence and demo
```

## Security and ethics by design

- Server-side numeric checks, known vehicle IDs, small request size limit
- Escaped Jinja templates, restrictive Content Security Policy, no inline scripts
- Local-only Flask development server, debug disabled, no tokens or external tunnels
- No accounts, real GPS data, driver identities, payments or live charging hardware

These measures are **not a guarantee of production security**. Deploying real fleet telemetry requires access controls, HTTPS, monitoring, data policies and a new risk assessment.

## GitHub Collaboration

**Course Team 4:** Hamdan Mohammad Saeed Bin Salmin Albedwawi; Nasser Fuad Abdulla Ahmad Anwahi; Sultan Ibrahim Mohamad Allanjawi.

**Sprint period:** October 26–November 8, 2026 (planned).

### Team responsibilities (sprint plan)

- **Nasser Fuad Abdulla Ahmad Anwahi:** Repository coordination, fleet overview, README, and Agile documentation.
- **Sultan Ibrahim Mohamad Allanjawi:** Charging calculator, server-side validation, and application development.
- **Hamdan Mohammad Saeed Bin Salmin Albedwawi:** Unit testing, security risk assessment, ethical analysis, and quality assurance.

### Feature branches and pull requests

- `feature/fleet-overview` — Fleet overview and initial Flask application. [Pull Request #1 (merged)](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/1).
- `feature/cost-calculator` — Automated tests, GitHub Actions, and project documentation. [Pull Request #2 (merged)](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/2).
- `improvement/security-testing-report` — Enhanced application structure, validation, security analysis, and expanded testing. [Pull Request #4 (merged)](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/4).

**Testing evidence:** [GitHub Actions — 25 successful tests](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/actions/runs/41889004694).

GitHub was used in place of GitLab with the instructor's approval. **The three team members worked through a shared GitHub account (`nasserfuad1987`)** to manage the repository, commits and pull requests. As a result, GitHub attributes those activities to one account even though the team reports working together. The account-level history documents the project's development, but it does not separately establish each student's individual contributions or independent peer reviews.

## Documentation

- [GitHub collaboration overview](CONTRIBUTING.md)
- [Architecture and data flow](docs/architecture.md)
- [Product backlog](docs/product_backlog.md)
- [Sprint plan](docs/sprint_plan.md)
- [Sprint retrospective](docs/sprint_retrospective.md)
- [Security memo (~200 words)](docs/security_memo.md)
- [Extended security analysis](docs/security_analysis.md)
- [ACM ethics memo (~200 words)](docs/ethical_considerations.md)
- [Test plan and evidence register](docs/testing_evidence.md)
- [Code review and prevented defect](docs/code_review.md)
- [Five-minute demo script](docs/demo_script.md)
- [Review of previous assignment and improvements](docs/reference_review.md)

## Constraints

The data is illustrative, and the fixed power and price do not account for real charging efficiency, grid tariffs, battery state of charge or market rates. Do not use the output for actual billing or operational dispatch. This release has no database, live vehicle API or location tracking.
