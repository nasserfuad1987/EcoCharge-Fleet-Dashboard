"""EcoCharge Fleet Dashboard.

One-page Flask educational prototype. No database, accounts, or live tracking.
"""
from flask import Flask, render_template, request
from calculator import calculate_charging_cost
from fleet import FLEET, VALID_VEHICLE_IDS

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 4096  # Cap form bodies to reduce abusive requests.


@app.after_request
def apply_security_headers(response):
    """Defense in depth; does not replace safe template rendering or validation."""
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; script-src 'none'; style-src 'self'; "
        "img-src 'self' data:; object-src 'none'; base-uri 'none'; "
        "form-action 'self'; frame-ancestors 'none'"
    )
    return response


@app.route("/", methods=["GET", "POST"])
def home():
    selected, duration, cost, error = FLEET[0]["id"], "", None, None
    if request.method == "POST":
        selected = request.form.get("vehicle_id", "")
        duration = request.form.get("duration", "")
        if selected not in VALID_VEHICLE_IDS:
            error = "Please select a valid vehicle."
        else:
            try:
                cost = calculate_charging_cost(duration)
            except ValueError as exc:
                error = str(exc)

    counts = {
        status: sum(vehicle["status"] == status for vehicle in FLEET)
        for status in ("Available", "Charging", "On Trip")
    }
    return render_template(
        "index.html", fleet=FLEET, counts=counts, selected=selected,
        duration=duration, cost=cost, error=error,
    )


if __name__ == "__main__":
    # Local-only development server; do not expose publicly as a production server.
    app.run(host="127.0.0.1", port=5000, debug=False)
