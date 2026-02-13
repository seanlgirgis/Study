"""
Modern Python Foundations for Data Engineering (Zero to Hero)
=============================================================
This script demonstrates the "Modern Standard" of Python (3.10+) used at top tech companies.
It covers: Type Hinting, Dataclasses, f-strings, and Collection types.

Run this file to see the output: `python 01_Modern_Python_Foundation.py`
"""

import datetime
from typing import List, Dict, Optional, Tuple, Set
from dataclasses import dataclass
from collections import defaultdict, Counter

# ==========================================
# 1. TYPE HINTING (The "New" Standard)
# ==========================================
# Old Python: def add(x, y): return x + y
# Problem: Is x a string? An int? A list?

def add_numbers(x: int, y: int) -> int:
    """Adds two integers. Modern code uses docstrings and types."""
    return x + y

def greet_user(name: str, age: Optional[int] = None) -> str:
    """Optional[int] means it can be an int OR None."""
    if age:
         # Modern f-string (Faster and cleaner than .format() or %)
        return f"Hello {name}, you are {age} years old."
    return f"Hello {name}, age unknown."

# ==========================================
# 2. DATACLASSES (Structs for Data)
# ==========================================
# Old Python: Classes with __init__, __repr__, __eq__ written manually.
# Modern Python: @dataclass does it all for you.

@dataclass
class Transaction:
    id: str
    amount: float
    timestamp: datetime.datetime
    category: str = "Uncategorized"  # Default value

    def is_large_transaction(self) -> bool:
        return self.amount > 1000.0

# ==========================================
# 3. MODERN COLLECTIONS (Beyond Lists)
# ==========================================

def analyze_transactions(transactions: List[Transaction]) -> None:
    print(f"\n--- Analyzing {len(transactions)} Transactions ---")
    
    # A. List Comprehension (Clean filtering)
    large_txns = [t for t in transactions if t.is_large_transaction()]
    print(f"Large Transactions found: {len(large_txns)}")

    # B. DefaultDict (No more 'if key in dict' checks)
    # Groups transactions by category automatically.
    category_totals: Dict[str, float] = defaultdict(float)
    
    for t in transactions:
        category_totals[t.category] += t.amount
    
    print("Totals by Category:")
    for cat, total in category_totals.items():
        print(f"  - {cat}: ${total:,.2f}") # f-string number formatting

    # C. Counter (Frequency analysis in one line)
    # Counts how many transactions per category.
    category_counts = Counter(t.category for t in transactions)
    print("Counts by Category:", dict(category_counts))

# ==========================================
# 4. EXECUTION
# ==========================================

if __name__ == "__main__":
    # creating data using the Type-Safe Constructor
    data = [
        Transaction(id="T1", amount=50.0, timestamp=datetime.datetime.now(), category="Food"),
        Transaction(id="T2", amount=1200.0, timestamp=datetime.datetime.now(), category="Travel"),
        Transaction(id="T3", amount=20.0, timestamp=datetime.datetime.now(), category="Food"),
        Transaction(id="T4", amount=5000.0, timestamp=datetime.datetime.now(), category="Electronics"),
    ]

    # Function Calls
    print(greet_user("Sean", 30))
    print(f"10 + 20 = {add_numbers(10, 20)}")
    
    analyze_transactions(data)

    print("\n--- End of Lesson 01 ---")
