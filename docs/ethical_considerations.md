# Ethical Memo (approximately 200 words): Location Privacy

**Ethical question.** If EcoCharge expanded from static records to real-time GPS tracking, would the operational benefit justify continuous observation of drivers? Vehicle trajectories can reveal home locations, work schedules, religious visits, breaks, and potentially sensitive personal routines. Even if names are removed, repeated travel patterns may re-identify individuals. Using these records for disciplinary decisions without transparency could undermine trust and create unequal power between managers and employees.

The **ACM Code of Ethics, Principle 1.6 (Respect privacy)** requires legitimate purposes, data minimization, safeguards against re-identification, and transparent collection and retention policies. **Principle 1.2 (Avoid harm)** highlights potential consequences for affected people. **Principle 2.5 (Give comprehensive evaluations)** encourages examining impacts beyond technical functionality.

**Proposed mitigation.** EcoCharge should show depot-level availability by default and reveal precise location only to authorized dispatch personnel when operationally necessary. The system should use role-based access, encrypted transport, short documented retention limits, audit trails, and notices explaining who can access location histories. Drivers should have a way to inspect and challenge inaccurate records. These controls balance fleet coordination with dignity and proportionality rather than assuming that more collected data is always better.

**Scope:** the current prototype contains no real driver or GPS data.

**Reference:** Association for Computing Machinery (2018), ACM Code of Ethics and Professional Conduct.
