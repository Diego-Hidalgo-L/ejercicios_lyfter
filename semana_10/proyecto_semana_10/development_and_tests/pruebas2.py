

def create_grades_dict():
    grades_dict = {'Spanish': 0, 'English': 0, 'Social Studies': 0, 'Science': 0}
    for subject in grades_dict.keys():
        grade = float(input(f"Please enter the student's {subject} grade: "))
        grades_dict[f'{subject}'] = grade
    
    return grades_dict


def calculate_avg(grades_dict):
    total_sum = 0
    for grade in grades_dict.values():
        total_sum += grade

    avg = total_sum / len(grades_dict)
    return avg


def main():
    grades_dict = create_grades_dict()
    avg = calculate_avg(grades_dict)
    print(avg)


main()