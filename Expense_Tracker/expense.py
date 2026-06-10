class Expense:
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
        return (
            f"Name: {self.name} | "
            f"Amount: {self.amount} | "
            f"Category: {self.category} | "
            f"Date: {self.date}"
        )

    def to_dict(self):
        return {
            "name": self.name,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }