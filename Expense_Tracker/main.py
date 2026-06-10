from rich import print
from tracker import ExpenseTracker
tracker = ExpenseTracker()

def main():
    while True:
        print("\n--- EXPENSE TRACKER MENU ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spending")
        print("4. View Category Summary")
        print("5. Exit")
        
        choice = int(input("Choose an option (1-5): "))
        match choice:
            case 1:
               
                name = input("Enter the name of your purchased item: ")
                amount = float(input("how much was it?:$"))
                category = input("Enter the category of item: ")
                date = input("In which day did you bought it: ")
                tracker.add_expense(name, amount, category, date)
            case 2:
                tracker.get_all_expenses()
            case 3:
                tracker.get_all_total()
            case 4:
                tracker.get_category_summary()
            case 5:
                
                print("[bold green]Goodbye![/bold green]")
                break            
            case _:
                print("[bold red]Invalid option. Please choose between 1 and 5.[/bold red]")
if __name__ =="__main__":
    main()





                