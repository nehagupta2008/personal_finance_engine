import sys
from cli import ExpenseCLI

def main():
    app = ExpenseCLI()
    while True:
        print("\n=== Personal Finance Engine ===")
        print("1. Add Expense")
        print("2. List All Expenses")
        print("3. View Analytics & Budget")
        print("4. Exit")
        try:
            choice = input("Enter option [1-4]: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

        if choice == "1":
            app.add_expense()
        elif choice == "2":
            app.list_expenses()
        elif choice == "3":
            app.show_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
