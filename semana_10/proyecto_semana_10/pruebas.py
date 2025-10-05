

def input_grades():
    spanish_grade = float(input("Please enter the student's Spanish grade: "))
    english_grade = float(input("Please enter the student's English grade: "))
    social_grade = float(input("Please enter the student's Social Studies grade: "))
    science_grade = float(input("Please enter the student's Science grade: "))

    return spanish_grade, english_grade, social_grade, science_grade


def calculate_individual_avg(spanish_grade, english_grade, social_grade, science_grade): # Optimize to not be limited to just 4 subjects
    individual_avg = (spanish_grade + english_grade + social_grade + science_grade) / 4
    individual_avg_rounded = round(individual_avg, 2)

    print(individual_avg_rounded)


def main():
    spanish_grade, english_grade, social_grade, science_grade = input_grades()
    calculate_individual_avg(spanish_grade, english_grade, social_grade, science_grade)


main()