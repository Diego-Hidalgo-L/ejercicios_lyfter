
students_list = [
    # {
    #     'name': 'Diego',
    #     'grades': {'Science': 90, 'Spanish': 97, 'Math': 65},
    #     'highest': 97,
    #     'lowest': 65,
    #     'average': 84.0,
    #     'passed': True
    # },
    # {
    #     'name': 'Lisa',
    #     'grades': {'Science': 60, 'Spanish': 72, 'Math': 53},
    #     'highest': 72,
    #     'lowest': 53,
    #     'average': 61.67,
    #     'passed': False
    # },
    # {
    #     'name': 'Michael',
    #     'grades': {'Spanish': 80, 'Science': 91, 'Math': 85},
    #     'highest': 91,
    #     'lowest': 80,
    #     'average': 85.33,
    #     'passed': True
    # }
]

PASSING_AVG = 70

while True:
    try:
        num_students = int(input("\nHow many students are there? "))

        if num_students > 0:
            break

        print("Please enter a positive number")

    except ValueError:
        print("The number must be an integer")


for student_num in range(1, num_students + 1):
    name = input(f"\nPlease enter the name of student number {student_num}: ").capitalize()

    while True:
        try:
            num_grades = int(input("How many grades does this student have? "))

            if num_grades > 0:
                break

            print("The number must be positive")

        except ValueError:
            print("The number must be an integer")
            continue


    student_dict = {}
    student_dict['name'] = name
    student_dict['grades'] = {}
    high_grade = None
    low_grade = None
    total_sum = 0

    for grade_num in range(1, num_grades + 1):
        grade_name = input(f"Enter the name of grade number {grade_num}: ").capitalize()

        while True:
            try:
                grade_score = int(input(f"Enter the score of grade number {grade_num}: "))

                if 0 <= grade_score <= 100:
                    break

                print("The grade must be between 0 and 100")

            except ValueError:
                print("The number must be an integer")
                continue


        if high_grade is None or grade_score > high_grade:
            high_grade = grade_score

        if low_grade is None or grade_score < low_grade:
            low_grade = grade_score

        total_sum += grade_score
        
        student_dict['grades'][grade_name] = grade_score


    student_dict['highest'] = high_grade
    student_dict['lowest'] = low_grade

    rounded_avg = round(total_sum / num_grades, 2)
    student_dict['average'] = rounded_avg

    student_dict['passed'] = rounded_avg >= PASSING_AVG

    students_list.append(student_dict)


print("\n")
print(students_list)

class_sum = 0
total_passed = 0
total_failed = 0
highest_avg = None
highest_student = None
lowest_avg = None
lowest_student = None

print("\nStudent information:")
for student in students_list:
    avg = student['average']
    class_sum += avg

    if highest_avg is None or avg > highest_avg:
        highest_avg = avg
        highest_student = student['name']
    
    if lowest_avg is None or avg < lowest_avg:
        lowest_avg = avg
        lowest_student = student['name']
    
    if student['passed']:
        total_passed += 1
    else:
        total_failed += 1
    
    print(f"\n{student.get('name')}:")
    print(f"Average: {avg}")
    print(f"Highest grade: {student['highest']}")
    print(f"Lowest grade: {student['lowest']}")
    print("Passed:", "Yes" if student['passed'] else "No")

class_avg = round(class_sum / num_students, 2)


print("\nClass information:")
print(f"Class average: {class_avg}")
print(f"Total students passed: {total_passed}")
print(f"Total students failed: {total_failed}")
print(f"Student with the highest average: {highest_student} ({highest_avg})")
print(f"Student with the lowest average: {lowest_student} ({lowest_avg})\n")