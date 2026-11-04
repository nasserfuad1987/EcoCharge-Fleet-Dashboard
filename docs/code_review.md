# Code Review: Preventing an Incorrect Charging Estimate

## Bug scenario
A browser's `type=number` form control is only a convenience. An attacker or accidental client can bypass it using a crafted HTTP POST. If the server simply converts duration to `float` and multiplies, a value of `-8` produces a misleading negative charging cost of `-$9.00`. A value of `NaN` may propagate into calculations, while invalid text can raise an unhandled exception.

## Root cause
Treating client-side restrictions as authoritative instead of validating the input at the server trust boundary.

## Prevention implemented
- `calculator.py` parses the input using `Decimal` and requires a finite number in the explicit 0–24 hour range.
- `app.py` checks vehicle IDs against a fixed allowlist and catches `ValueError`, displaying an error.
- `MAX_CONTENT_LENGTH` limits request bodies.
- Calculator tests verify rejection independently; route integration tests verify the protection is actually wired into the UI.

## Design tradeoff
The 24-hour limit is a scoped prototype rule, not a physical charging constraint. A future real charger would use model-specific charging power, battery capacity, tariffs, and efficiency data. The assignment intentionally uses fixed parameters.

## Testing evidence

The validation rules are implemented in `calculator.py` and called by the form route in `app.py`. Unit and Flask integration tests show that positive input is calculated correctly while negative, non-numeric, and non-finite values are rejected. This documents the potential bug identified and prevented through testing, as required by the assignment.
