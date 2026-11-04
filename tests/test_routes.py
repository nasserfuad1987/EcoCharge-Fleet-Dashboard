"""Flask integration checks; complementary to calculator-only unit tests."""
import unittest
from app import app


class DashboardRouteTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_get_renders_five_vehicles(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        for identifier in ("EV-001", "EV-002", "EV-003", "EV-004", "EV-005"):
            self.assertIn(identifier, html)
        self.assertIn("Fleet overview", html)

    def test_valid_post_displays_expected_cost(self):
        response = self.client.post("/", data={"vehicle_id": "EV-001", "duration": "2"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("$2.25", response.get_data(as_text=True))

    def test_negative_post_returns_friendly_error(self):
        response = self.client.post("/", data={"vehicle_id": "EV-001", "duration": "-8"})
        html = response.get_data(as_text=True)
        self.assertIn("between 0 and 24", html)
        self.assertNotIn("Estimated charging cost</span><strong>", html)

    def test_invalid_vehicle_id_rejected(self):
        response = self.client.post("/", data={"vehicle_id": "EV-999", "duration": "2"})
        self.assertIn("Please select a valid vehicle", response.get_data(as_text=True))

    def test_reflected_markup_escaped(self):
        payload = "<script>alert('x')</script>"
        response = self.client.post("/", data={"vehicle_id": "EV-001", "duration": payload})
        html = response.get_data(as_text=True)
        self.assertNotIn(payload, html)
        self.assertIn("&lt;script&gt;", html)

    def test_non_numeric_post_returns_error(self):
        response = self.client.post(
            "/", data={"vehicle_id": "EV-001", "duration": "hello"}
        )
        html = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Enter a valid number of hours.", html)
        self.assertNotIn("Estimated charging cost</span><strong>", html)

    def test_nonfinite_post_returns_error(self):
        for duration in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(duration=duration):
                response = self.client.post(
                    "/", data={"vehicle_id": "EV-001", "duration": duration}
                )
                html = response.get_data(as_text=True)
                self.assertIn("between 0 and 24", html)
                self.assertNotIn("Estimated charging cost</span><strong>", html)

    def test_maximum_duration_displays_correct_cost(self):
        response = self.client.post(
            "/", data={"vehicle_id": "EV-005", "duration": "24"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("$27.00", response.get_data(as_text=True))

    def test_over_maximum_duration_returns_error(self):
        response = self.client.post(
            "/", data={"vehicle_id": "EV-001", "duration": "24.01"}
        )
        html = response.get_data(as_text=True)
        self.assertIn("between 0 and 24", html)
        self.assertNotIn("Estimated charging cost</span><strong>", html)

    def test_zero_duration_cost(self):
        response = self.client.post(
            "/", data={"vehicle_id": "EV-002", "duration": "0"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("$0.00", response.get_data(as_text=True))

    def test_unknown_route_returns_404(self):
        response = self.client.get("/unknown")
        self.assertEqual(response.status_code, 404)

    def test_security_headers_set(self):
        response = self.client.get("/")
        self.assertEqual(response.headers.get("X-Content-Type-Options"), "nosniff")
        self.assertIn("script-src 'none'", response.headers.get("Content-Security-Policy", ""))
        self.assertEqual(response.headers.get("X-Frame-Options"), "DENY")

    def test_oversized_post_rejected(self):
        response = self.client.post(
            "/", data={"vehicle_id": "EV-001", "duration": "1" * 5000}
        )
        self.assertEqual(response.status_code, 413)


if __name__ == "__main__":
    unittest.main()
