from typing import List, Dict, Any
from models import Transaction

class AnalyticsEngine:
    def __init__(self, budget_limit: float = 5000.0):
        self.budget_limit = budget_limit

    @staticmethod
    def calculate_total(transactions: List[Transaction]) -> float:
        return round(sum(t.amount for t in transactions), 2)

    @staticmethod
    def category_breakdown(transactions: List[Transaction]) -> Dict[str, float]:
        breakdown: Dict[str, float] = {}
        for t in transactions:
            breakdown[t.category] = breakdown.get(t.category, 0.0) + t.amount
        return {k: round(v, 2) for k, v in breakdown.items()}

    def check_budget_status(self, total_spent: float) -> Dict[str, Any]:
        exceeded = total_spent > self.budget_limit
        return {
            "budget_limit": self.budget_limit,
            "total_spent": total_spent,
            "remaining": round(self.budget_limit - total_spent, 2),
            "is_exceeded": exceeded
        }
