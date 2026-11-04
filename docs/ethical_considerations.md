# Ethical Considerations Memo — Fleet Location Privacy

**To:** EcoCharge Innovations Project Team
**Subject:** Privacy protections for a future connected fleet

A future EcoCharge system might display real-time vehicle locations to help managers schedule charging and trips. However, repeated location observations could reveal drivers' daily routines, workplaces, breaks, and visits to sensitive places. Even when location records use vehicle identifiers rather than names, managers may be able to infer which driver operated a particular vehicle. This could create intrusive workplace surveillance or expose personal information if the data is improperly shared.

The **ACM Code of Ethics**, Principle **1.6 (Respect privacy)**, supports collecting only information necessary for a legitimate purpose and giving individuals understandable notice about its use. Principle **1.7 (Honor confidentiality)** also supports restricting access to sensitive information. EcoCharge should therefore apply data minimization and role-based access control. For example, dispatch managers may see a current operational location only when needed, while ordinary staff should not see identifiable trip histories. The company should also specify limited retention periods, encrypt traffic with HTTPS, maintain access logs, and communicate its collection and deletion rules to drivers.

The present prototype contains only static demonstration data and does **not** track live locations. Before any live feature is deployed, the team should consult affected drivers and assess applicable data-protection requirements.

**Reference:** Association for Computing Machinery (2018), [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics).
