# Project Statement: Personal Finance & Expense Analytics Engine

## Student Details
* **Student Name:** NEHA GUPTA
* **Registration Number:** 26BCE10478
* **Programme:** B.Tech Computer Science and Engineering (CSE Core)
* **Course:** Python Essentials (Flipped Course Evaluation)

---

## 1. Problem Statement
Managing daily expenditures and maintaining budget adherence is a major challenge for university students and independent professionals. Most existing commercial personal finance applications require cloud sign-ups, display ads, depend on complex database servers, or enforce heavyweight graphical interfaces.

There is a distinct need for a lightweight, modular, offline-first command-line system that provides transparent, secure transaction tracking, category-wise expenditure analytics, and automated budget violation alerts without external dependencies.

---

## 2. Scope of the Project
The **Personal Finance & Expense Analytics Engine** provides a terminal-based solution implemented using modular Python programming. The scope covers:
- Complete input validation on transaction creation to ensure clean financial data.
- Structured JSON-based local file persistence for cross-session consistency.
- Category breakdown and aggregated expenditure analytics.
- Real-time comparison against budget ceilings with automated alert triggers.
- Automated validation through test suites for high reliability.

---

## 3. Target Users
* **B.Tech / University Students**: To track monthly allowances, hostel expenses, and educational purchases.
* **Command-Line & Technical Users**: Developers seeking a fast, offline ledger tool without GUI overhead.
* **Privacy-Focused Users**: Users requiring local storage without cloud tracking or telemetry.

---

## 4. High-Level Features
1. **Transaction Management & Data Validation**: Enforces positive float values, mandatory non-empty titles, and auto-generated timestamps.
2. **Persistence Module**: Manages reading and writing data to local JSON storage (`expenses.json`) with robust error handling.
3. **Analytics Engine**: Calculates dynamic sum totals, spending percentages, and per-category distributions.
4. **Budget Threshold Monitor**: Evaluates aggregate expenditure against user-configured limits and issues warnings when limits are exceeded.
5. **Quality Assurance via Automated Testing**: Comprehensive unit test suite implemented with `unittest`.
