# Security Risk Assessment Memo

**To:** EcoCharge Innovations Development Team
**Subject:** Two relevant dashboard security risks

**1. Cross-site scripting (XSS).** In a future connected system, fleet model names and status labels might come from external data sources. If these values are inserted directly into HTML without escaping, an attacker could execute a malicious script in a manager's browser. Such code could alter the dashboard, deceive its users, or access information visible to the current page. The mitigation is to retain Jinja's HTML escaping, avoid the `safe` filter for untrusted content, and add tests when accepting editable data. The current implementation renders data through escaped template variables.

**2. Improper input validation.** A client can bypass the browser's numeric input restrictions and send a negative duration, letters, or values such as `NaN` in a crafted request. Without checks, the calculator could return misleading prices or cause server errors. The mitigation is server-side validation before cost calculation. Our function converts inputs to `Decimal`, rejects non-numeric and non-finite values, and requires 0–24 hours. Unit tests cover representative cases. The 24-hour maximum is a prototype design decision rather than a charging-industry rule.

This prototype uses fixed sample vehicles and no accounts, payments, or real-time telemetry. A deployed system would additionally require authentication, authorization, HTTPS, appropriate monitoring, and secure data management.
