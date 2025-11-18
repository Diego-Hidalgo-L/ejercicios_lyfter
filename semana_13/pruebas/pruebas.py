class Student:
    spanish_score: int
    english_score: int

    def __init__(self, spanish_score, english_score):
        self.spanish_score = spanish_score
        self.english_score = english_score
    
    @property
    def average_score(self):
        return (self.spanish_score + self.english_score) / 2


student_ian = Student(80, 80)
print(f"Average score: {student_ian.average_score}")

student_ian.spanish_score = 50
print(f"Spanish score: {student_ian.spanish_score}")
print(f"Average score: {student_ian.average_score}")