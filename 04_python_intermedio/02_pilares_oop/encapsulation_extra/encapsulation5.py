
class Student:
    def __init__(self):
        self.__grades = []
    
    def add_grade(self, grade):
        if grade < 0 or grade > 100:
            print("The grade can only be between 0 and 100.")
        else:
            self.__grades.append(grade)
    
    def remove_grade(self, index):
        if 0 <= index < len(self.__grades):
            self.__grades.pop(index)
        else:
            print("Invalid index.")
    
    def get_grades(self):
        grades_list = []

        for grade in self.__grades:
            grades_list.append(grade)
        
        return grades_list
    
    @property
    def average(self):
        if self.__grades == []:
            return "The list of grades is empty."
            

        else:
            total_grades = 0
            for grade in self.__grades:
                total_grades += grade
        
            average = total_grades / len(self.__grades)
            return average

s = Student()
s.add_grade(90)
s.add_grade(75)
s.add_grade(110)   # Should give error
s.remove_grade(1)
print(s.average)   # Should print 90

grades = s.get_grades()
grades.append(50)  # Should NOT affect internal grades

print(s.get_grades())   # Should still show only [90]