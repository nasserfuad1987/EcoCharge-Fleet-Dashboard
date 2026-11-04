# Security Memo (approximately 200 words)

**Vulnerability 1: Improper input validation.** A malicious client can bypass HTML form restrictions and submit `-8`, `NaN`, non-numeric text, or an unknown vehicle ID directly to the Flask endpoint. Without backend checks, this could produce negative charging estimates, misleading management decisions, or server errors. **Mitigation:** `calculator.py` parses finite numbers with `Decimal`, restricts hours to 0–24, and rejects oversized values; `app.py` allowlists vehicle IDs and limits request size. Calculator unit tests and HTTP integration tests check these defenses. The range is an assignment-specific design decision, not a universal charging rule.

**Vulnerability 2: Cross-site scripting (XSS).** Future integrations might import untrusted vehicle names or status strings. If inserted into HTML unsafely, a crafted value could execute JavaScript, misrepresent fleet information, or expose data available to the browser. **Mitigation:** the page uses Jinja's automatic HTML escaping, avoids rendering untrusted values as raw HTML, and applies a restrictive Content Security Policy. An integration test checks that submitted markup is escaped.

**Residual risk:** this is a local, stateless prototype without accounts, live telemetry, or payment data. Public deployment would additionally need authentication, HTTPS, authorization, monitoring, and privacy controls.

**References:** OWASP Input Validation Cheat Sheet; OWASP Cross-Site Scripting Prevention Cheat Sheet.
