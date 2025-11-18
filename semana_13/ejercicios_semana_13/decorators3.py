
from datetime import date 

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
    
    @property
    def age(self):
        today = date.today()
        return (
            today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        )
    
    def check_age(func):
        