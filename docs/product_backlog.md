# EcoCharge Product Backlog

| ID | User story | Acceptance criteria | Priority |
|---|---|---|---|
| US-01 | As a fleet manager, I want to see all EVs and battery levels to plan vehicle availability. | Table displays 5–10 sample EVs with ID, model, battery %, and status. | High |
| US-02 | As a manager, I want to select a vehicle and enter charging hours to estimate electricity cost. | Uses hours × 7.5 kW × $0.15/kWh and shows USD to two decimals. | High |
| US-03 | As a manager, I want invalid charging durations rejected so incorrect estimates are not displayed. | Non-numeric, negative, and non-finite values produce a clear error. | High |
| US-04 | As a developer, I want cost calculation unit tests to catch regressions. | Tests cover valid positive and invalid hours. | High |
| US-05 | As an evaluator, I want run instructions, security and ethics notes, and PR history to assess the prototype. | README and evidence links are available. | High |
