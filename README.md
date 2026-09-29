# Personal Finance & Expense Analytics Engine

## Student Details
* **Student Name:** NEHA GUPTA
* **Registration Number:** 26BCE10478
* **Programme:** B.Tech Computer Science and Engineering (CSE Core)
* **Course:** Python Essentials (Flipped Course Evaluation)

---

## Project Overview
The **Personal Finance & Expense Analytics Engine** is a modular, offline-first command-line application built in pure Python. It allows users to track daily expenses, categorize transactions, validate numerical inputs, and generate aggregated spending reports alongside threshold-based budget alerts.

The project follows clean object-oriented architecture and software modularity principles, designed to be completely cross-platform and executable in any standard terminal without requiring GUI libraries, web frameworks, or external package installations.

---

## Key Features
* **Three-Tier Architecture**: Clear separation of data models, local JSON persistence, analytics engine, and CLI presentation.
* **Robust Input Validation**: Validates non-empty descriptions, strictly positive expense values, and auto-generates ISO timestamps.
* **Category Breakdown & Metrics**: Aggregates total expenditure and calculates real-time spending distributions per category (e.g. Food, Books, Travel).
* **Budget Monitoring & Alerting**: Proactively evaluates expenditures against configured budget limits and alerts users if spending exceeds thresholds.
* **Persistent Local Storage**: Stores records in human-readable JSON (`expenses.json`) with automatic serialization and deserialization.
* **Automated Unit Testing**: Includes unit tests verifying core transaction logic, data integrity constraints, and analytics calculations.

---

## Technologies Used
* **Programming Language:** Python 3.9+
* **Standard Libraries:** `dataclasses`, `json`, `datetime`, `unittest`, `typing` (Pure Python Standard Library — zero external package dependencies)
* **User Interface:** Command Line Interface (CLI)

---

## Environment Setup & Execution Instructions

### 1. Prerequisites
Ensure Python 3.9 or higher is installed on your system:
```bash
python --version
```

### 2. Clone the Repository
```bash
git clone https://github.com/nehagupta2008/personal_finance_engine.git
cd personal_finance_engine
```

### 3. Dependency Installation
No external dependencies or virtual environment setups are required. The project uses standard library modules.

### 4. Running the Project via Terminal
To start the application, execute:
```bash
python main.py
```

#### Terminal Menu Navigation:
```text
=== Personal Finance Engine ===
1. Add Expense
2. List All Expenses
3. View Analytics & Budget
4. Exit
Enter option [1-4]: 
```

---

## Instructions for Testing
To execute the automated unit test suite:
```bash
python -m unittest test_tracker.py
```

### Expected Output:
```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

---

## Repository Structure
```text
personal_finance_engine/
│── models.py        # Module 1: Transaction data model & input validation
│── storage.py       # Module 2: File persistence & JSON data storage
│── analytics.py     # Module 3: Expense analytics, totals & budget rules
│── cli.py           # Command-line interaction & user flow
│── main.py          # Application entrypoint
│── test_tracker.py  # Automated unit tests (unittest)
│── statement.md     # Problem statement, scope & target users
└── README.md        # Comprehensive documentation & execution guide
```
