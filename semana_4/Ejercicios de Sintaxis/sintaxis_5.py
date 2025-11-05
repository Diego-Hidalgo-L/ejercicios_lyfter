

# 5. Dada n cantidad de notas de un estudiante, calcular:
    # a. Cuantas notas tiene aprobadas (mayor a 70).
    # b. Cuantas notas tiene desaprobadas (menor a 70).
    # c. El promedio de todas.
    # d. El promedio de las aprobadas.
    # e. El promedio de las desaprobadas.

grade_counter = 1
passed_grades = 0
failed_grades = 0
average_total_grades = 0
average_passed_grades = 0
average_failed_grades = 0

total_grades = int(input('Please enter the total number of grades: '))

while (grade_counter <= total_grades):
    current_grade = int(input(f'Please enter grade number {grade_counter}: '))
    if (current_grade < 70):
        failed_grades += 1
        average_failed_grades += current_grade
    else:
        passed_grades += 1
        average_passed_grades += current_grade
    average_total_grades += current_grade
    grade_counter += 1

average_total_grades = float(average_total_grades / total_grades)
if (passed_grades != 0): # No se puede dividir 0 / 0
    average_passed_grades = float(average_passed_grades / passed_grades)
else:
    average_passed_grades = 0

if (failed_grades != 0): # No se puede dividir 0 / 0
    average_failed_grades = float(average_failed_grades / failed_grades)
else:
    average_failed_grades = 0

print(f"The total number of passed grades is {passed_grades}")
print(f"The total number of failed grades is {failed_grades}")
print(f"The average of passed grades is {average_passed_grades}")
print(f"The average of failed grades is {average_failed_grades}")
print(f"The average of all the grades is {average_total_grades}")