class Expense:
    def __init__(self, item: str, amount: float, category: str, date: str):
        self.item = item
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
      return f"[{self.category.upper()}] {self.item} - Rs.{self.amount:.2f} | {self.date}"
        

   

if __name__ == "__main__":
     obj1 = Expense("Burger",1,"food","6 july") 
     print(obj1) 