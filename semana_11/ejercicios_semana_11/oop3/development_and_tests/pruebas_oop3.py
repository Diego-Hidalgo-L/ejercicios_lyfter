
class Student:
    def __init__(self, student_name, student_section, spanish_grade, english_grade, social_grade, science_grade, individual_avg):
        self.student_name = student_name
        self.student_section = student_section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_grade = social_grade
        self.science_grade = science_grade
        self.individual_avg = individual_avg

    def __str__(self):
        return f"{self.student_name}"
    
    def __repr__(self):
        return f"{self.student_name}: {self.student_section}"


students_list = [
    {'Name': 'Luis Diego Hidalgo',
    'Section': '12A',
    'Spanish': 97.0,
    'English': 98.0,
    'Social Studies': 88.5,
    'Science': 40.0,
    'Average': 94.0}
    ,
    {'Name': 'Mateo Fonseca',
    'Section': '4B',
    'Spanish': 90.0,
    'English': 91.8,
    'Social Studies': 59.0,
    'Science': 55.0,
    'Average': 90.825}
    ,
    {'Name': 'Karla Lara',
    'Section': '10C',
    'Spanish': 96.0,
    'English': 86.0,
    'Social Studies': 94.5,
    'Science': 91.0,
    'Average': 91.875}
    ,
    {'Name': 'Brock Mahannah',
    'Section': '12A',
    'Spanish': 83.0,
    'English': 95.0,
    'Social Studies': 97.0,
    'Science': 90.0,
    'Average': 91.25}
    ,
    {'Name': 'Jose Camacho',
    'Section': '11B',
    'Spanish': 90.5,
    'English': 92.0,
    'Social Studies': 85.0,
    'Science': 87.0,
    'Average': 88.625}]

def create_student_obj(student_dict):
    key_map = {
        "Name": "student_name",
        "Section": "student_section",
        "Spanish": "spanish_grade",
        "English": "english_grade",
        "Social Studies": "social_grade",
        "Science": "science_grade",
        "Average": "individual_avg"
    }

    mapped_values = {new: student_dict[old] for old, new in key_map.items()}
    return Student(**mapped_values)

def main():
    for student_dict in students_list:
        student_obj = create_student_obj(student_dict)
        print(student_obj)

main()