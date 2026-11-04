# Architecture and Data-Flow Rationale

## System context

The proof of concept consists of one stateless Flask web application. No external database, identity provider, payment service, real-time vehicle API, GPS module, or telemetry is connected.

```text
Fleet Manager
    |
    | GET /  or  POST / (vehicle_id, duration)
    v
Flask Controller [app.py]
    |-- fleet.py            -> static list of 5 BEVs + allowlisted IDs
    |-- calculator.py       -> Decimal conversion, validation, fixed-rate cost
    |-- templates/index.html -> safely escaped Jinja output
    |-- static/styles.css  -> responsive presentation
    v
Browser: fleet table, battery meters, status, estimate or error
```

## Core decisions and rationale

| Decision | Benefit | Boundary/limitation |
|---|---|---|
| Static five-vehicle array | Reproducible, no privacy-sensitive telemetry | Cannot support operational dispatch decisions |
| Stateless POST calculation | Simple to test, no stored user records | No history, billing or persistence |
| Pure calculator function | Unit tests independent of HTTP, easy regression checks | Fixed power and tariff only |
| Python `Decimal` + ROUND_HALF_UP | Explicit currency rounding; avoids binary-float surprises | An estimate, not metered energy |
| Server-side allowlist and duration checks | Protects against crafted POST bypassing browser validation | Not a substitute for authorization in production |
| Escaped Jinja template + restrictive CSP | Defense against injection in rendered values | Not a formal security guarantee |
| Separate HTML, CSS and Python | Clean code and straightforward maintenance | Slightly more files to manage |

## Quality attributes

- **Correctness:** exact decimal calculation; bounded inputs; interpretable errors.
- **Usability:** visible formula, clear labels, accessible table, native battery meters.
- **Maintainability:** independent data, computation, controller and presentation layers.
- **Security:** no exposed secrets, local development host, output escaping, content security policy, size limits.
- **Privacy:** no personal profiles, live location data or driver telemetry.
- **Reproducibility:** fixed sample dataset and automated tests.

## Explicit exclusions

No real fleet API, charging optimization, geolocation, authentication, payment, persistent database or performance-bonus decision-making. Adding these would change the security and ethics risk assessment and should be part of a separately reviewed release.
