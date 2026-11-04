# Extended Software Security Analysis

This complements the required ~200-word memo. It is a **reasoned threat model**, not a penetration-test certificate.

## 1. Assets, trust boundaries and attack surface

**Assets:** integrity of estimated charging costs, availability of the dashboard, accuracy of displayed fleet records, and user trust in stated limitations.

**Trust boundaries:** browser/form data is untrusted; server-side logic decides vehicle membership and permitted duration; static data and templates originate in this repository. There is no database, login, real vehicle connection or private API key.

**Attack surface:** the single GET/POST route, the `vehicle_id` and `duration` parameters, HTTP response rendering, and the development server if mistakenly exposed.

## 2. Threat and mitigation matrix

| Threat / relevant weakness | Attack path | Potential impact | Risk in local prototype | Control implemented | Verification |
|---|---|---|---|---|---|
| Input manipulation / CWE-20 | Forge POST with `-8`, `NaN`, `EV-999`, or oversized duration | False/invalid price, crash, resource misuse | Medium likelihood, low-to-moderate impact | Decimal validation, 0–24 range, vehicle allowlist, 4 KB request cap | Calculator unit tests + HTTP integration tests |
| Cross-site scripting / CWE-79 | If future vehicle text becomes user-controlled, insert markup into rendered output | Defaced UI; script execution or data exposure if future accounts exist | Low likelihood now, higher impact if production data added | Jinja HTML escaping, no `safe`, no JavaScript, restrictive CSP | Reflected markup and response-header integration tests |

These risk levels are qualitative judgments, not measurements. They apply to **this stateless local prototype**, not to a real production fleet system.

## 3. Static security analysis

Static analysis examines code without executing it. A manual review checks for: direct use of `float` for currency; trusted-only vehicle IDs; use of `render_template` with Jinja escaping instead of unsafe HTML concatenation; debug mode disabled; secrets committed to code; and unexpected external network calls. This review identified the need to isolate and bound form inputs. It does not demonstrate that automated SAST has run.

For a future development pipeline, a tool such as Bandit could detect common Python security patterns. Running it and capturing output should be reported as separate evidence, not assumed.

## 4. Dynamic security analysis

Dynamic analysis exercises running behavior. The calculator unit suite covers 0, 24, decimals, negative, too-large, text, `NaN`, infinity, and long inputs. HTTP integration tests check GET/POST behavior, invalid vehicle IDs, HTML escaping, security headers, and oversized submissions. [GitHub Actions run 41868004476](https://github.com/nasserfuad1987/EcoCharge-Fleet-Dashboard/actions/runs/41868004476) completed with 19/19 tests passing on 4 November 2026 (12 unit and 7 route integration methods). Browser testing should independently confirm legibility, keyboard navigation, and error messages. A passing unit test does **not** prove the actual route applies validation; route tests address that gap.

## 5. Residual risk and future controls

The development server is not production-ready. If exposed publicly or connected to live vehicle data, EcoCharge would require authentication, least-privilege authorization, HTTPS, rate limiting, access logs, security monitoring, secure deployment, and a data protection assessment. CSRF tokens become important if subsequent POST endpoints change state. Currently, the cost form calculates a result without modifying stored data.

**Security references:**
1. OWASP, [Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html).
2. OWASP, [Cross-Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet).
3. OWASP, [Secure Code Review Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html).
