import unittest
from decimal import Decimal
from app import calculate_charging_cost


class ChargingCostTests(unittest.TestCase):
    def test_positive_hours(self):
        self.assertEqual(calculate_charging_cost(2), Decimal("2.25"))

    def test_fractional_hours(self):
        self.assertEqual(calculate_charging_cost("0.5"), Decimal("0.56"))

    def test_rounding(self):
        self.assertEqual(calculate_charging_cost(5), Decimal("5.63"))

    def test_negative_hours_rejected(self):
        with self.assertRaises(ValueError):
            calculate_charging_cost(-1)

    def test_non_numeric_rejected(self):
        with self.assertRaises(ValueError):
            calculate_charging_cost("hello")

    def test_non_finite_rejected(self):
        for value in ("NaN", "Infinity"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                calculate_charging_cost(value)

    def test_too_many_hours_rejected(self):
        with self.assertRaises(ValueError):
            calculate_charging_cost(25)


if __name__ == "__main__":
    unittest.main()
