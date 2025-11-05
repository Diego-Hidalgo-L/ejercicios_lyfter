
class Student:
    def __init__(self, student_name, student_section, spanish_grade, english_grade, social_grade, science_grade, individual_avg):
        self.student_name = student_name
        self.student_section = student_section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_grade = social_grade
        self.science_grade = science_grade
        self.individual_avg = individual_avg

    def to_dict(self):
        return {
            "Name": self.student_name,
            "Section": self.student_section,
            "Spanish": self.spanish_grade,
            "English": self.english_grade,
            "Social Studies": self.social_grade,
            "Science": self.science_grade,
            "Average": self.individual_avg
        }

    def __str__(self):
        return f"{self.student_name}"
    
    def __repr__(self):
        return f"{self.student_name}: {self.student_section}"


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

    for key, value in student_dict.items():
        if isinstance(value, str) and value.replace('.', '', 1).isdigit():
            student_dict[key] = float(value)

    mapped_values = {new: student_dict[old] for old, new in key_map.items()}
    return Student(**mapped_values)


import csv

def read_csv_file_and_extract_students_list(path, students_obj_list):
    try:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)

            for student_dict in reader:
                student_obj = create_student_obj(student_dict)
                students_obj_list.append(student_obj)
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    
    return students_obj_list


def write_csv_file(path, data, headers):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

        rows = [student.to_dict() for student in data]
        writer.writerows(rows)


def main():
    students_obj_list = []
    headers = ["Name", "Section", "Spanish", "English", "Social Studies", "Science", "Average"]

    students_obj_list = read_csv_file_and_extract_students_list('semana_11/ejercicios_semana_11/oop3/project/students_info.csv', students_obj_list)
    # write_csv_file('semana_11/ejercicios_semana_11/oop3/project/students_info.csv', students_obj_list, headers)

    print(students_obj_list[1])


main()