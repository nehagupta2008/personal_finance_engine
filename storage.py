import json
import os
from typing import List
from models import Transaction

class StorageManager:
    def __init__(self, filename="expenses.json"):
        self.filename = filename

    def load(self) -> List[Transaction]:
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Transaction(**item) for item in data]
        except (json.JSONDecodeError, IOError):
            return []

    def save(self, transactions: List[Transaction]):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in transactions], f, indent=4)
