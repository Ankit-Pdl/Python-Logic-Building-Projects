from rich import print
from expense import Expense
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self,name,amount,category,date):
        user_expense = Expense(name,amount,category,date)
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
        temp_categories =dict()
        # print(temp_categories)    
        for x in self.expenses:
            if x.category in temp_categories:
                temp_categories[x.category] += x.amount
            else:
                temp_categories[x.category] = x.amount
        for key,value in temp_categories.items():
            print(f"{key}:{value}")

if __name__ =="__main__":
    obj1 = ExpenseTracker()
    obj1.add_expense("veggies",1295,"Health","12 sept")
    obj1.add_expense("burgers",5,"Food","12 sept")
    obj1.add_expense("Beer",12,"Alcohol","13 may")
    obj1.add_expense("Vodka",134,"Alcohol","14th may")
    obj1.get_all_expenses()
    obj1.get_all_total()
    obj1.get_category_summary()

# obj1.get_all_expenses()
# obj1.get_all_total()

