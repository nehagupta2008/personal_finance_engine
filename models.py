from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Transaction:
    id: int
    title: str
    amount: float
    category: str
    date: str

    @classmethod
    def create(cls, trans_id: int, title: str, amount: float, category: str):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if not title.strip():
            raise ValueError("Title cannot be empty.")
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return cls(trans_id, title.strip(), round(amount, 2), category.strip().title(), date_str)

    def to_dict(self):
        return asdict(self)
