# Test Plan and Evidence Register

## Why the test layers are separate

**Unit tests** in `tests/test_calculator.py` test only the critical charging-cost function, fulfilling the assignment requirement. **HTTP integration tests** in `tests/test_routes.py` additionally verify that the form calls the same validated function and safely renders results.

## Expected behavior

| Test scenario | Input | Expected result | Evidence |
|---|---|---|---|
| Normal case | 2 hours | $2.25 | `test_two_hours` and HTTP POST |
| Half-up money rounding | 1 hour | $1.13 | `test_one_hour_half_up_rounding` |
| Reference rounding edge | 5 hours | $5.63 | `test_five_hours_half_up_rounding` |
| Lower boundary | 0 hours | $0.00 | `test_zero_hours` |
| Upper boundary | 24 hours | $27.00 | `test_maximum_24_hours` |
| Negative | -8 hours | User-facing validation error | Unit and route tests |
| Non-numeric | `hello` | ValueError; friendly route error | Unit and route tests |
| Non-finite | `NaN`, infinity | ValueError and a form error | Unit and route tests |
| Invalid vehicle | `EV-999` | No calculation; validation message | Route test |
| Reflected markup | `<script>...` | Escaped as text, not executable markup | Route test |
| Oversized request | 5000 digit duration | HTTP 413 | Route test |
| Headers | GET / | CSP, X-Content-Type-Options, X-Frame-Options | Route test |
| Unknown URL | GET /unknown | HTTP 404 | `test_unknown_route_returns_404` |
| Out-of-range duration | 24.01 hours | Clear validation error | `test_over_maximum_duration_returns_error` |

**Execution status (4 November 2026):** The standalone calculator module was verified locally (12/12 calculator unit tests). Crucially, [GitHub Actions run 41889004694](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/actions/runs/41889004694) **completed successfully with 25/25 tests: 12 calculator unit tests and 13 Flask integration tests, 0 failures**. This verifies both the pure function and its HTTP integration for the tested cases. Automated results establish the tested software behavior; they do not establish independent human code reviews or visual accessibility.

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```


## Traceability

| Requirement | Implementation | Test / documentation |
|---|---|---|
| Static fleet overview | `fleet.py`, `templates/index.html` | `test_get_renders_five_vehicles` |
| Cost calculator | `calculator.py`, `app.py` | `test_two_hours`, `test_valid_post_displays_expected_cost` |
| Graceful failure | `calculate_charging_cost`, `home` | Negative, text, non-finite, invalid vehicle tests |
| Security foresight | `app.py`, escaped templates | XSS, size and headers tests; `security_analysis.md` |
| Ethical foresight | No live telemetry | `ethical_considerations.md` |
