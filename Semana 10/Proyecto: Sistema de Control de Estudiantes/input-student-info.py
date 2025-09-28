

def input_student_info():
    student_name = input("Please enter the student's full name: ")
    student_section = input("Please enter the student's section: ")
    
    return student_name, student_section


def input_scores():
    spanish_score = int(input("Please enter the student's Spanish score: "))
    english_score = int(input("Please enter the student's English score: "))
    social_score = int(input("Please enter the student's Social Studies score: "))
    science_score = int(input("Please enter the student's Science score: "))

    return spanish_score, english_score, social_score, science_score


def calculate_individual_avg(spanish_score, english_score, social_score, science_score):
    individual_avg = (spanish_score + english_score + social_score + science_score) / 4

    return individual_avg


def create_dict_entry(student_name, student_section, spanish_score, english_score, social_score, science_score, individual_avg):
    dict_entry = {}
    
    dict_entry['Name'] = student_name
    dict_entry['Section'] = student_section
    dict_entry['Spanish'] = spanish_score
    dict_entry['English'] = english_score
    dict_entry['Social Studies'] = social_score
    dict_entry['Science'] = science_score
    dict_entry['Average'] = individual_avg
    
    return dict_entry


def input_dict_entry_to_students_list(students_list, dict_entry):
    students_list.append(dict_entry)
    print("\nStudent information entered successfully!")


def ask_if_another_student():
    while True:
        try:
            another_student = input("Do you want to enter another student's information? Yes or No: ")
            another_student = another_student.upper()

            if another_student == "YES" or another_student == "NO":
                print("\n")
                return another_student
            else:
                raise ValueError
        except ValueError:
            print("Invalid answer. Please answer Yes or No.")


def create_students_list():
    students_list = []

    while True:
        student_name, student_section = input_student_info()
        spanish_score, english_score, social_score, science_score = input_scores()
        individual_avg = calculate_individual_avg(spanish_score, english_score, social_score, science_score)
        dict_entry = create_dict_entry(student_name, student_section, spanish_score, english_score, social_score, science_score, individual_avg)
        input_dict_entry_to_students_list(students_list, dict_entry)
        
        another_student = ask_if_another_student()
        if another_student == "NO":
            break

    return students_list


def main():
    students_list = create_students_list()
    print(students_list)


main()