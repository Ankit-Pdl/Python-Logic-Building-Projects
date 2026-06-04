from rich import print
from expense import Expense
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self,title,amount,category,date):
        user_expense = Expense(title,amount,category,date)
        self.expenses.append(user_expense)
    def get_all_expenses(self):
        for expense in self.expenses:
            print(expense)
    def get_all_total(self):
        total =0
        for temp in self.expenses:
            total +=temp.amount
        print(f"Total:{total}")  
    def get_category_summary(self):
        temp_categories =set()
        for x in self.expenses:
            temp_categories.add(x.category)
        print(temp_categories)    
            



obj1  = ExpenseTracker()
obj1.add_expense("burgers",5,"food","12 sept")
obj1.add_expense("veggies",1295,"Health","12 sept")
obj1.get_category_summary()

# obj1.get_all_expenses()
# obj1.get_all_total()

