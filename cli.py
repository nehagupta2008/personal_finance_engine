from models import Transaction
from storage import StorageManager
from analytics import AnalyticsEngine

class ExpenseCLI:
    def __init__(self):
        self.storage = StorageManager()
        self.analytics = AnalyticsEngine(budget_limit=10000.0)
        self.transactions = self.storage.load()

    def _next_id(self) -> int:
        return max([t.id for t in self.transactions], default=0) + 1

    def add_expense(self):
        title = input("Description: ")
        try:
            amount = float(input("Amount: "))
            category = input("Category (e.g. Food, Travel, Books): ")
            tx = Transaction.create(self._next_id(), title, amount, category)
            self.transactions.append(tx)
            self.storage.save(self.transactions)
            print("Expense added successfully.")
        except ValueError as err:
            print(f"Error: {err}")

    def list_expenses(self):
        if not self.transactions:
            print("No transactions recorded yet.")
            return
        print(f"\n{'ID':<5}{'Title':<20}{'Category':<15}{'Amount':<10}{'Date'}")
        print("-" * 65)
        for t in self.transactions:
            print(f"{t.id:<5}{t.title:<20}{t.category:<15}{t.amount:<10.2f}{t.date}")

    def show_summary(self):
        total = self.analytics.calculate_total(self.transactions)
        breakdown = self.analytics.category_breakdown(self.transactions)
        status = self.analytics.check_budget_status(total)

        print("\n--- Analytics Report ---")
        print(f"Total Spent: {total:.2f}")
        print(f"Budget: {status['budget_limit']:.2f} | Remaining: {status['remaining']:.2f}")
        if status['is_exceeded']:
            print("WARNING: Budget exceeded!")
        print("\nBreakdown by Category:")
        for cat, amt in breakdown.items():
            print(f" - {cat}: {amt:.2f}")
