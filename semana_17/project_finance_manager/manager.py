
from datetime import date

class FinanceManager:
    DEFAULT_COLORS = [
    "#FF6B6B", "#4ECDC4", "#FFD166",
    "#6A4C93", "#456122", "#1A535C"
]

    def __init__(self):
        self.categories = {}
        self.movements = []

    # Categories
    def category_exists(self, name):
        return name in self.categories
    
    def _get_next_color(self):
        used_colors = [data["color"] for data in self.categories.values() if "color" in data]

        for color in self.DEFAULT_COLORS:
            if color not in used_colors:
                return color

        import random
        return random.choice(self.DEFAULT_COLORS)
    
    def update_category_color(self, category_name, new_color):
        if not self.category_exists(category_name):
            raise ValueError(f"The category '{category_name}' does not exist")
        
        self.categories[category_name]["color"] = new_color

    def add_category(self, category):
        if isinstance(category, dict):
            name = category.get("name", "").strip()
            color = category.get("color")
        else:
            name = category.strip()
            color = None

        if not name:
            raise ValueError("The category cannot be empty")

        if self.category_exists(name):
            raise ValueError(f"The category '{name}' already exists")
        
        if not color:
            color = self._get_next_color()
        
        self.categories[name] = {
            "color": color
        }

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
    
    def validate_movement(self, data):
        mov_date = data.get("-DATE-")
        try:
            iso_date = date.fromisoformat(mov_date)
        except ValueError:
            raise ValueError("Date must be in the format 'YYYY-MM-DD'")
        if iso_date > date.today():
            raise ValueError("Date cannot be in the future")

        title = data.get("-TITLE-").strip()
        if not title:
            raise ValueError("Title is required")

        amount_input = data.get("-AMOUNT-")
        if not amount_input:
            raise ValueError("Amount is required")
        try:
            amount = float(amount_input)
        except ValueError:
            raise ValueError("Amount must be a number")

        category = data.get("-CATEGORY-")
        if not category:
            raise ValueError("Please select a category")

        return mov_date, title, amount, category
    
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
            "categories": [
                {
                    "name": name,
                    "color": data["color"]
                }
                for name, data in self.categories.items()
            ], 
            "movements": [
                m.convert_movement_to_dict()
                for m in self.movements
            ]
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
    
    @property
    def date(self):
        return date.fromisoformat(self.mov_date)

    def convert_movement_to_dict(self):
        return {
            "date": self.mov_date,
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "type": self.type_
        }