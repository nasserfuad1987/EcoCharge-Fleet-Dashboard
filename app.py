from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Static sample data; no real vehicle telemetry is collected.
FLEET = [
    {"id": "EV-001", "model": "Tesla Model 3", "battery": 82, "status": "Available"},
    {"id": "EV-002", "model": "Hyundai IONIQ 5", "battery": 45, "status": "Charging"},
    {"id": "EV-003", "model": "Kia EV6", "battery": 67, "status": "On Trip"},
    {"id": "EV-004", "model": "Porsche Taycan", "battery": 23, "status": "Charging"},
    {"id": "EV-005", "model": "GMC HUMMER EV", "battery": 96, "status": "Available"},
]

def calculate_charging_cost(hours):
    """Return estimated USD cost for charging hours (fixed 7.5 kW, $0.15/kWh)."""
    try:
        duration = Decimal(str(hours))
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError("Enter a valid number of hours.") from None
    if not duration.is_finite() or not Decimal("0") <= duration <= Decimal("24"):
        raise ValueError("Charging hours must be between 0 and 24.")
    return (duration * Decimal("7.5") * Decimal("0.15")).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )

PAGE = """
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>EcoCharge Fleet Dashboard</title>
<style>
body{font-family:Arial,sans-serif;background:#f1f7f5;color:#183b34;margin:0;padding:24px}
main{max-width:960px;margin:auto}h1{color:#12694f}
section{background:#fff;border-radius:12px;padding:22px;margin:20px 0;box-shadow:0 2px 10px #0000000d}
table{width:100%;border-collapse:collapse}th,td{text-align:left;padding:12px;border-bottom:1px solid #dde7e3}th{background:#e6f3ed}
label{display:block;margin-top:12px;font-weight:bold}select,input{display:block;padding:10px;width:100%;max-width:360px;box-sizing:border-box;margin-top:6px}
button{margin-top:16px;background:#12694f;color:white;padding:12px 20px;border:0;border-radius:6px;cursor:pointer}
.result{color:#12694f;font-weight:bold;font-size:22px}.error{color:#b42318}
small{color:#526b63}
</style>
</head>
<body><main>
<h1>EcoCharge Fleet Dashboard</h1>
<p>Sample electric vehicle fleet · Charging estimates in USD</p>
<section><h2>Fleet Overview</h2>
<table><thead><tr><th>Vehicle ID</th><th>Model</th><th>Battery</th><th>Status</th></tr></thead>
<tbody>{% for vehicle in fleet %}
<tr><td>{{ vehicle.id }}</td><td>{{ vehicle.model }}</td><td>{{ vehicle.battery }}%</td><td>{{ vehicle.status }}</td></tr>
{% endfor %}</tbody></table>
<small>All vehicle information is static demonstration data, not live readings.</small>
</section>
<section><h2>Charging Cost Calculator</h2>
<form method="post">
<label for="vehicle">Vehicle</label>
<select id="vehicle" name="vehicle_id" required>
{% for vehicle in fleet %}<option value="{{ vehicle.id }}" {% if vehicle.id == selected %}selected{% endif %}>{{ vehicle.id }} — {{ vehicle.model }}</option>{% endfor %}
</select>
<label for="hours">Charging duration (hours)</label>
<input id="hours" name="duration" type="number" min="0" max="24" step="any" value="{{ duration }}" required>
<button type="submit">Calculate cost</button>
</form>
{% if cost is not none %}<p class="result">Estimated cost: ${{ cost }}</p>{% endif %}
{% if error %}<p class="error" role="alert">{{ error }}</p>{% endif %}
<p><small>Formula: hours × 7.5 kW × $0.15/kWh. Fixed educational estimate.</small></p>
</section></main></body></html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    selected, duration, cost, error = FLEET[0]["id"], "", None, None
    if request.method == "POST":
        selected = request.form.get("vehicle_id", "")
        duration = request.form.get("duration", "")
        if selected not in {vehicle["id"] for vehicle in FLEET}:
            error = "Please select a valid vehicle."
        else:
            try:
                cost = calculate_charging_cost(duration)
            except ValueError as exc:
                error = str(exc)
    return render_template_string(
        PAGE, fleet=FLEET, selected=selected, duration=duration,
        cost=cost, error=error
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=False)
