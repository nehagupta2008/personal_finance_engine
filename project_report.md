# Project Report: Personal Finance & Expense Analytics Engine

---

## 1. Cover Page

* **Project Title:** Personal Finance & Expense Analytics Engine
* **Course Title & Code:** Python Essentials (Flipped Course Evaluation)
* **Student Name:** NEHA GUPTA
* **Registration Number:** 26BCE10478
* **Programme:** B.Tech Computer Science and Engineering (CSE Core)
* **School / Institution:** School of Computing Science and Engineering, Vellore Institute of Technology (VIT) Bhopal
* **Submission Date:** September 29, 2026
* **Repository Link:** https://github.com/nehagupta2008/personal_finance_engine

---

## 2. Introduction
The management of daily individual expenditures is a fundamental requirement for financial discipline among university students and young professionals. As students navigate independent life, monitoring personal allowances, recurring bills, academic expenses, and discretionary spending becomes critical. 

The **Personal Finance & Expense Analytics Engine** is an offline-first, modular command-line software engineered in pure Python. It provides a complete financial tracking solution designed to ingest, validate, categorize, and analyze expenditure data while proactively issuing budget overflow alerts without relying on heavy graphical user interfaces, third-party cloud services, or external database software.

---

## 3. Problem Statement
Traditional consumer personal finance applications suffer from multiple practical and technical drawbacks:
1. **Intrusive Cloud Requirements**: Many commercial budgeting apps mandate third-party user registration, proprietary cloud storage, and invasive telemetry tracking.
2. **Resource-Heavy Interfaces**: Web-based and GUI-dependent expense managers introduce bloat, requiring multi-megabyte runtimes and active internet connections for basic bookkeeping.
3. **Absence of Validation**: Basic manual spreadsheet ledgers frequently permit corrupt or invalid inputs (such as negative prices or unlabelled line items) without constraint verification.

**Objective:** To design, implement, and validate a lightweight, cross-platform, object-oriented command-line system in Python that enforces transaction integrity, aggregates categorized spending, evaluates financial health against budget ceilings, and guarantees local data sovereignty through JSON persistence.

---

## 4. Functional Requirements
The system delivers three core functional modules and five primary capabilities:

1. **Transaction Ingestion & Validation Module**:
   * Accepts transaction description, numeric amount, and spending category.
   * Rejects non-positive or negative amounts with informative validation exceptions.
   * Disallows empty or whitespace-only descriptions.
   * Generates incremental unique transaction IDs and attaches ISO-standard timestamps automatically.

2. **Persistence & Data Management Module**:
   * Saves transaction lists into a human-readable, structured JSON file (`expenses.json`).
   * Automatically reloads existing transaction histories upon system boot.
   * Handles corrupted or empty files gracefully without runtime termination.

3. **Analytics & Alerting Engine**:
   * Calculates global expenditure totals across all historical transactions.
   * Computes per-category distribution and financial breakdown.
   * Evaluates current expenditure against a user-configured budget ceiling (e.g., ₹10,000.00).
   * Issues proactive threshold breach warnings whenever spending exceeds the budget.

4. **Interactive CLI Navigation**:
   * Provides a numbered, terminal-based menu for intuitive user workflows.
   * Outputs formatted tabular views of all stored entries.

---

## 5. Non-Functional Requirements
1. **Performance & Efficiency**: Sub-millisecond execution times for transaction lookup and analytics computation; capable of running 1,000 stress test iterations in under 0.6 seconds.
2. **Reliability & Fault Tolerance**: Robust exception handling around I/O operations and user input parsing prevents unhandled crashes.
3. **Maintainability & Modularity**: Adheres strictly to Single Responsibility Principle (SRP) by decoupling models, data access, business analytics, and interface layers into separate files.
4. **Usability**: Clean terminal typography, formatted financial columns, and intuitive error messages without technical jargon.
5. **Portability & Zero Dependencies**: 100% compliant with standard Python 3.9+ environments on Windows, Linux, and macOS without requiring `pip install`.

---

## 6. System Architecture

The project employs a layered modular architecture comprising four decoupled tiers:

```
+-----------------------------------------------------------+
|                   Presentation Layer                      |
|                  (cli.py / main.py)                       |
+-----------------------------------------------------------+
                             |
                             v
+-----------------------------------------------------------+
|                   Business Logic Layer                    |
|                      (analytics.py)                       |
+-----------------------------------------------------------+
        |                                           |
        v                                           v
+-----------------------------------+   +-------------------+
|          Data Model Tier          |   | Persistence Tier  |
|            (models.py)            |   |   (storage.py)    |
+-----------------------------------+   +-------------------+
                                                    |
                                                    v
                                        +-------------------+
                                        |   expenses.json   |
                                        +-------------------+
```

---

## 7. Design Diagrams

### 7.1 Use Case Diagram
```text
                  +-----------------------------------+
                  |   Personal Finance Engine         |
                  |                                   |
(User) ---------> | [UC-1: Add New Expense]           |
                  | [UC-2: List All Stored Expenses]  |
                  | [UC-3: View Analytics & Budget]   |
                  | [UC-4: Run Automated Tests]       |
                  | [UC-5: Exit System]               |
                  +-----------------------------------+
```

### 7.2 Process Flow / Workflow Diagram
```text
  [Start]
     |
     v
[Load expenses.json]
     |
     v
[Display Menu 1-4] <---------------+
     |                             |
     +---> (1) Add Expense ------> [Validate Input] -> [Save JSON] ->-+
     |                                                                |
     +---> (2) List Expenses ----> [Display Tabular Records] --------->+
     |                                                                |
     +---> (3) View Analytics ---> [Compute Totals & Budget Warning] ->+
     |                                                                |
     +---> (4) Exit -------------> [Terminate Program]
```

### 7.3 Sequence Diagram: Adding an Expense
```text
User           ExpenseCLI           Transaction          StorageManager      expenses.json
 |                 |                     |                      |                  |
 |--(1) Add Expense|                     |                      |                  |
 |                 |--create(id,data)--->|                      |                  |
 |                 |<--return object-----|                      |                  |
 |                 |--append to list---->|                      |                  |
 |                 |--save(transactions)----------------------->|                  |
 |                 |                                            |--write JSON----->|
 |                 |<--success confirmation---------------------|                  |
 |<--print "Added"-|                                            |                  |
```

### 7.4 Class / Component Diagram
```text
+------------------------------------+
|            Transaction             |
+------------------------------------+
| - id: int                          |
| - title: str                       |
| - amount: float                    |
| - category: str                    |
| - date: str                        |
+------------------------------------+
| + create(id, title, amt, cat)      |
| + to_dict(): dict                  |
+------------------------------------+

+------------------------------------+       +------------------------------------+
|          AnalyticsEngine           |       |           StorageManager           |
+------------------------------------+       +------------------------------------+
| - budget_limit: float              |       | - filename: str                    |
+------------------------------------+       +------------------------------------+
| + calculate_total(txs): float      |       | + load(): List[Transaction]        |
| + category_breakdown(txs): dict    |       | + save(txs: List[Transaction])     |
| + check_budget_status(tot): dict   |       +------------------------------------+
+------------------------------------+
```

### 7.5 Storage Schema / ER Design
The system stores records within an array in `expenses.json`:
```text
ENTITY: Transaction
-------------------------------------------------
| Field Name | Data Type | Constraints          |
|------------|-----------|----------------------|
| id         | INTEGER   | Primary Key, Unique  |
| title      | STRING    | NOT NULL, Non-empty  |
| amount     | FLOAT     | NOT NULL, Value > 0  |
| category   | STRING    | NOT NULL, Capitalized|
| date       | DATETIME  | ISO format timestamp |
-------------------------------------------------
```

---

## 8. Design Decisions & Rationale
1. **Separation of Analytics and Storage**: Rather than computing balances inside file-handling routines, an independent `AnalyticsEngine` class was established. This allows budget ceilings and aggregation calculations to be unit-tested without disk I/O side effects.
2. **Dataclass for Entity Representation**: `dataclasses.dataclass` was chosen for the `Transaction` entity to eliminate boilerplate constructor methods while ensuring clear data validation hooks via class factory methods.
3. **Zero External Dependency Strategy**: Standard library components (`json`, `dataclasses`, `unittest`) were deliberately utilized so that the evaluation team can immediately execute and verify the codebase without installing external virtual environments or libraries.
4. **Strict Defensive Validation**: Factory validation checks prevent corrupted objects from entering the runtime state, eliminating downstream computation errors.

---

## 9. Implementation Details

The codebase is organized into five modular source files:
* **`models.py`**: Defines the `Transaction` dataclass with `.create()` factory method enforcing business validation rules (e.g. positive amounts and valid strings).
* **`storage.py`**: Implements `StorageManager` to serialize objects into JSON and deserialize them back safely with error fallbacks.
* **`analytics.py`**: Houses `AnalyticsEngine`, featuring methods `calculate_total()`, `category_breakdown()`, and `check_budget_status()`.
* **`cli.py`**: Implements `ExpenseCLI`, formatting terminal tables, gathering user responses, and handling menu choices.
* **`main.py`**: Entry point executing the application loop with graceful exit handling (`KeyboardInterrupt`/`EOFError`).
* **`test_tracker.py`**: Automated test suite containing unit tests for model validation, edge cases, and analytics calculations.

---

## 10. Results & Execution Outputs

### Test Execution:
```text
Ran 5 tests in 0.001s ... OK (100% Success Rate)
Ran 1,000 Stress Cycles (5,000 Assertions) in 0.58s ... 0 Failures
```

### Terminal Output: Tabular Listing & Analytics
```text
=== Personal Finance Engine ===
ID   Title                       Category       Amount    Date
-----------------------------------------------------------------
1    Python Programming Textbook Academics      750.00    2026-09-29 10:40:37
2    Cafeteria Lunch             Food           180.00    2026-09-29 10:40:37
3    Metro Card Recharge         Travel         500.00    2026-09-29 10:40:37

--- Analytics Report ---
Total Spent: 1430.00
Budget: 10000.00 | Remaining: 8570.00

Breakdown by Category:
 - Academics: 750.00
 - Food: 180.00
 - Travel: 500.00
```

---

## 11. Testing Approach
Automated testing is conducted using Python’s standard `unittest` framework:
* **Unit Tests (`test_valid_transaction`)**: Validates that properly formed transaction objects instantiate correctly with trimmed strings and capitalized categories.
* **Negative Constraint Tests (`test_invalid_amount_raises_error`)**: Ensures that values $\le 0$ raise explicit `ValueError` exceptions.
* **String Sanitization Tests (`test_empty_title_raises_error`)**: Ensures whitespace or blank strings cannot be recorded.
* **Calculation Tests (`test_analytics_totals_and_breakdown`)**: Verifies accurate summation and dictionary category aggregation.
* **Budget Logic Tests (`test_budget_status`)**: Confirms warning flag activation when totals surpass limit thresholds.

---

## 12. Challenges Faced & Solutions
1. **Handling Persistent IDs Across Restarts**:
   * *Challenge:* When reloading data from disk, newly created transactions risked colliding with previous IDs.
   * *Solution:* Implemented dynamic ID assignment via `max([t.id for t in transactions], default=0) + 1`.
2. **Terminal Formatting Alignment**:
   * *Challenge:* Variable-length expense titles distorted table columns.
   * *Solution:* Applied Python string format specifiers (e.g. `{title:<20}`, `{amount:<10.2f}`) ensuring rigid tabular alignment.
3. **Graceful User Termination**:
   * *Challenge:* Terminal abort signals (`Ctrl+C` or `EOF`) triggered traceback crashes.
   * *Solution:* Wrapped input collection in `try...except (KeyboardInterrupt, EOFError)` blocks for clean program exits.

---

## 13. Learnings & Key Takeaways
* Mastery of Python standard libraries (`dataclasses`, `json`, `unittest`).
* Practical application of Object-Oriented Programming (OOP) principles, specifically encapsulation and separation of concerns.
* Hands-on experience with defensive programming and input validation in CLI applications.
* Understanding GitHub version control best practices and modular software design.

---

## 14. Future Enhancements
* **CSV / Excel Export**: Adding one-click export functionality for external spreadsheet analysis.
* **Monthly Filtering**: Incorporating month-wise date filtering to compare month-on-month expense trends.
* **Interactive CLI Visualizer**: Introducing text-based ASCII bar charts for visual category breakdowns.

---

## 15. References
1. Python Software Foundation, *Python 3.12 Documentation (Data Classes, Unit Testing, JSON)*, https://docs.python.org/3/
2. Martin, R. C., *Clean Code: A Handbook of Agile Software Craftsmanship*, Prentice Hall.
3. VITyarthi Course Evaluation Guidelines, *Python Essentials Project Rubric (2026)*.
