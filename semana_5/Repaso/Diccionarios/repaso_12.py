
students = [
    {"name": "Ana", "grade": "A"},
    {"name": "Luis", "grade": "B"},
    {"name": "Sofía", "grade": "A"},
]

result = {}

for student in students:
    name = student.get("name")
    grade = student.get("grade")

    # también se puede usar if grade not in result:
    if result.get(grade) is None:
        result[grade] = []

    result[grade].append(name)


print(result)