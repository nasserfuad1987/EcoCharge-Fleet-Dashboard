"""Unit tests for charging calculation only (assignment-critical logic)."""
import unittest
from decimal import Decimal

from calculator import calculate_charging_cost


class ChargingCostTests(unittest.TestCase):
    def test_two_hours(self):
        self.assertEqual(calculate_charging_cost(2), Decimal("2.25"))

    def test_one_hour_half_up_rounding(self):
        self.assertEqual(calculate_charging_cost(1), Decimal("1.13"))

    def test_five_hours_half_up_rounding(self):
        self.assertEqual(calculate_charging_cost(5), Decimal("5.63"))

    def test_half_hour(self):
        self.assertEqual(calculate_charging_cost("0.5"), Decimal("0.56"))

    def test_zero_hours(self):
        self.assertEqual(calculate_charging_cost(0), Decimal("0.00"))

    def test_maximum_24_hours(self):
        self.assertEqual(calculate_charging_cost(24), Decimal("27.00"))

    def test_negative_duration(self):
        with self.assertRaises(ValueError):
            calculate_charging_cost(-8)

    def test_non_numeric_duration(self):
        for bad in ("hello", "", None):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                calculate_charging_cost(bad)

    def test_non_finite_duration(self):
        for bad in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                calculate_charging_cost(bad)

    def test_beyond_maximum_duration(self):
        with self.assertRaises(ValueError):
            calculate_charging_cost("24.01")

    def test_overly_long_input_rejected(self):
        with self.assertRaises(ValueError):
            calculate_charging_cost("1" * 10000)

    def test_precise_cents(self):
        self.assertEqual(calculate_charging_cost("3.6"), Decimal("4.05"))


if __name__ == "__main__":
    unittest.main()
