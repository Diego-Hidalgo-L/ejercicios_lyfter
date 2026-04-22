
from datetime import date

class FinanceManager:
    def __init__(self):
        self.categories = {}
        self.movements = []

    # Categories
    def category_exists(self, category):
        return category in self.categories

    def add_category(self, category):
        if not category.strip():
            raise ValueError("The category cannot be empty")

        if self.category_exists(category):
            raise ValueError(f"The category '{category}' already exists")
        
        self.categories[category] = {}
        return f"'{category}' added to Categories"
    
    def get_categories(self):
        return list(self.categories.keys())


    # Movements
    def add_income(self, mov_date, title, amount, category):
        if not mov_date:
            raise ValueError("Enter a date for the movement")

        if not self.category_exists(category):
            raise ValueError(f"The category '{category}' does not exist")

        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

        movement = Movement(mov_date, title, amount, category, 'income')
        self.movements.append(movement)
        
        return "Income registered"

    def add_expense(self, mov_date, title, amount, category):
        if not mov_date:
            raise ValueError("Enter a date for the movement")

        if not self.category_exists(category):
            raise ValueError(f"The category '{category}' does not exist")

        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        
        movement = Movement(mov_date, title, -amount, category, 'expense')
        self.movements.append(movement)

        return "Expense registered"
    
    def get_movements(self):
        return self.movements
    
    def get_movements_by_category(self, category):
        if not self.category_exists(category):
            raise ValueError(f"The category '{category}' does not exist")
        
        return [m for m in self.movements if m.category == category]

    def get_movements_by_type(self, type_):
        if type_ not in ('income', 'expense'):
            raise ValueError("Invalid movement type")
        
        return [m for m in self.movements if m.type_ == type_]

    # Calculations
    def get_total_income(self):
        return sum(m.amount for m in self.movements if m.type_ == 'income')

        # total_income = 0

        # for m in self.movements:
        #     if m.type_ == 'income':
        #         total_income += m.amount
        
        # return total_income
        

    def get_total_expense(self):
        return sum(abs(m.amount) for m in self.movements if m.type_ == 'expense')
    
        # total_expense = 0
        
        # for m in self.movements:
        #     if m.type_ == 'expense':
        #         total_expense += abs(m.amount)
        
        # return total_expense
        

    def get_balance(self):
        return sum(m.amount for m in self.movements)

        # return self.get_total_income() - self.get_total_expense()
    
    def convert_all_to_dict(self):
        return {
            "categories": list(self.get_categories()),
            "movements": [m.convert_movement_to_dict() for m in self.movements]
        }


class Movement:
    def __init__(self, mov_date, title, amount, category, type_):
        # if not date.fromisoformat(mov_date):
        #     raise ValueError("The date is invalid")

        if not title.strip():
            raise ValueError("Title cannot be empty")
        
        if type_ not in ('income', 'expense'):
            raise ValueError("Invalid movement type")

        self.mov_date = mov_date
        self.title = title
        self.amount = amount
        self.category = category
        self.type_ = type_
    
    def __str__(self):
        return f"{self.type_.upper()} | {self.title} | {self.amount} | {self.category}"

    def __repr__(self):
        return f"{self.type_.upper()} | {self.title} | {self.amount} | {self.category}"

    def convert_movement_to_dict(self):
        return {
            "date": self.mov_date,
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "type": self.type_
        }