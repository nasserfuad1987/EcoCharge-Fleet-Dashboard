"""Sample fleet records; no database, GPS, or personal data."""
FLEET = (
    {"id": "EV-001", "model": "Tesla Model 3", "battery": 82, "status": "Available"},
    {"id": "EV-002", "model": "Hyundai IONIQ 5", "battery": 45, "status": "Charging"},
    {"id": "EV-003", "model": "Kia EV6", "battery": 67, "status": "On Trip"},
    {"id": "EV-004", "model": "Porsche Taycan", "battery": 23, "status": "Charging"},
    {"id": "EV-005", "model": "GMC HUMMER EV", "battery": 96, "status": "Available"},
)

VALID_VEHICLE_IDS = frozenset(vehicle["id"] for vehicle in FLEET)
