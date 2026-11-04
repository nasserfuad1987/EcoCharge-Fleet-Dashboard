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

## Running and demonstrating the dashboard

The GitHub repository stores source code and evidence; **it does not host the Flask website**. Running the app on your own computer is **optional for reviewing the repository or GitHub Actions tests**, but the course's five-minute demo must show the actual working interface. You may demonstrate the original, separately shared Google Colab prototype, noting that it is a separate version and may not include the advanced GitHub features. To demonstrate the advanced GitHub version, run/deploy this version in an environment that supports Flask.

### Optional: run this version locally

Requires Python 3.10+.

```bash
git clone https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard.git
cd EcoCharge-Fleet-Dashboard
python3 -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
python3 -m pip install -r requirements.txt
python3 app.py
```

**After the server starts**, visit **http://127.0.0.1:5050** on the same computer. The link is not publicly hosted. Stop Flask using Ctrl+C.

**Why port 5050?** Some Macs reserve port 5000 for another service (such as AirPlay Receiver), which can show HTTP 403. If port 5050 is also occupied, choose an available port and edit the last line of `app.py`.

## Test and analyze

```bash
python -m unittest discover -s tests -v
python -m compileall -q app.py calculator.py fleet.py
```

**Unit tests:** `tests/test_calculator.py` targets only cost calculation as required, including boundary and invalid-value cases.

**Additional integration tests:** `tests/test_routes.py` checks real Flask GET/POST behavior, vehicle allowlist, escaped markup, security headers and request size. **Verified CI evidence:** [GitHub Actions run 41868004476](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/actions/runs/41868004476) completed successfully with **19/19 tests** (12 unit + 7 Flask integration). The run was inspected, including its execution log.

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

## GitHub collaboration evidence

- [PR #1: fleet overview](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/1) - merged
- [PR #2: tests and planning documents](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/pull/2) - merged
- A subsequent code-quality improvement PR may be added and should be peer-reviewed.

**Team members:** [Fill actual names and usernames]  
**Two-week sprint dates:** [Fill actual start and end]  
**Instructor-approved change:** GitHub may substitute for GitLab (retain approval evidence).

The first two PRs were merged using one linked GitHub account. **They are not evidence of independent student reviews.** Each group member should make identifiable contributions and give genuine PR feedback.

## Documentation

- [Architecture and data flow](docs/architecture.md)
- [Product backlog](docs/product_backlog.md)
- [Sprint plan](docs/sprint_plan.md)
- [Retrospective draft (verify and personalize)](docs/sprint_retrospective.md)
- [Security memo (~200 words)](docs/security_memo.md)
- [Extended security analysis](docs/security_analysis.md)
- [ACM ethics memo (~200 words)](docs/ethical_considerations.md)
- [Test plan and evidence register](docs/testing_evidence.md)
- [Code review and prevented defect](docs/code_review.md)
- [Five-minute demo script](docs/demo_script.md)

## Constraints

The data is illustrative, and the fixed power and price do not account for real charging efficiency, grid tariffs, battery state of charge or market rates. Do not use the output for actual billing or operational dispatch. This release has no database, live vehicle API or location tracking.
