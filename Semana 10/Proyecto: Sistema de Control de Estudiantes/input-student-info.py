

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


def main():
    student_name, student_section = input_student_info()
    spanish_score, english_score, social_score, science_score = input_scores()
    individual_avg = calculate_individual_avg(spanish_score, english_score, social_score, science_score)
    dict_entry = create_dict_entry(student_name, student_section, spanish_score, english_score, social_score, science_score, individual_avg)
    print(dict_entry)


main()