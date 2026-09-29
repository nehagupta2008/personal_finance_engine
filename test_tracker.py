import unittest
from models import Transaction
from analytics import AnalyticsEngine

class TestExpenseTracker(unittest.TestCase):
    def test_valid_transaction(self):
        t = Transaction.create(1, "Notebook", 150.0, "education")
        self.assertEqual(t.title, "Notebook")
        self.assertEqual(t.amount, 150.0)
        self.assertEqual(t.category, "Education")

    def test_invalid_amount_raises_error(self):
        with self.assertRaises(ValueError):
            Transaction.create(2, "Invalid", -10.0, "Food")

    def test_empty_title_raises_error(self):
        with self.assertRaises(ValueError):
            Transaction.create(3, "   ", 50.0, "Food")

    def test_analytics_totals_and_breakdown(self):
        data = [
            Transaction.create(1, "Lunch", 200.0, "Food"),
            Transaction.create(2, "Dinner", 300.0, "Food"),
            Transaction.create(3, "Bus Pass", 500.0, "Travel")
        ]
        self.assertEqual(AnalyticsEngine.calculate_total(data), 1000.0)
        breakdown = AnalyticsEngine.category_breakdown(data)
        self.assertEqual(breakdown["Food"], 500.0)
        self.assertEqual(breakdown["Travel"], 500.0)

    def test_budget_status(self):
        engine = AnalyticsEngine(budget_limit=1000.0)
        status_ok = engine.check_budget_status(800.0)
        self.assertFalse(status_ok["is_exceeded"])
        self.assertEqual(status_ok["remaining"], 200.0)

        status_exceeded = engine.check_budget_status(1200.0)
        self.assertTrue(status_exceeded["is_exceeded"])
        self.assertEqual(status_exceeded["remaining"], -200.0)

if __name__ == "__main__":
    unittest.main()
