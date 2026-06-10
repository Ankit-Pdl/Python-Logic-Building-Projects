from rich import print
from expense import Expense
import json
import os

FILE_NAME = "Expense_Tracker/expense.json"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if not os.path.exists(FILE_NAME):
            return

        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)

            for expense_data in data:
                expense = Expense(
                    expense_data["name"],
                    expense_data["amount"],
                    expense_data["category"],
                    expense_data["date"]
                )
                self.expenses.append(expense)

        except json.JSONDecodeError:
            print("[red]JSON file is empty or corrupted. Starting fresh.[/red]")
            self.expenses = []

    def save_expenses(self):
        os.makedirs(os.path.dirname(FILE_NAME), exist_ok=True)  # create folder if missing
        data = []

        for expense in self.expenses:
            data.append(expense.to_dict())

        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    def add_expense(self, name, amount, category, date):
        expense = Expense(name, amount, category, date)
        self.expenses.append(expense)
        self.save_expenses()
        print("[green]Expense Added Successfully![/green]")

    def get_all_expenses(self):
        if not self.expenses:
            print("[red]No expenses found.[/red]")
            return

        print("\n[bold cyan]All Expenses[/bold cyan]\n")

        for expense in self.expenses:
            print(expense)

    def get_all_total(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"\n[bold yellow]Total Expenses: {total}[/bold yellow]")

    def get_category_summary(self):
        if not self.expenses:
            print("[red]No expenses found.[/red]")
            return

        categories = {}

        for expense in self.expenses:
            categories[expense.category] = (
                categories.get(expense.category, 0) + expense.amount
            )

        print("\n[bold magenta]Category Summary[/bold magenta]\n")

        for category, amount in categories.items():
            print(f"{category}: {amount}")


if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\n[bold blue]Expense Tracker[/bold blue]")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Expense Name: ")

            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("[red]Invalid amount![/red]")
                continue

            category = input("Category: ")
            date = input("Date: ")
            tracker.add_expense(name, amount, category, date)

        elif choice == "2":
            tracker.get_all_expenses()

        elif choice == "3":
            tracker.get_all_total()

        elif choice == "4":
            tracker.get_category_summary()

        elif choice == "5":
            print("[green]Goodbye![/green]")
            break

        else:
            print("[red]Invalid choice![/red]")