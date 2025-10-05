

student1 = {'Name': 'Luis Diego Hidalgo',
    'Section': '12A',
    'Spanish': 97.0,
    'English': 98.0,
    'Social Studies': 88.5,
    'Science': 40.0,
    'Average': 94.0}


student2 = {'Name': 'Mateo Fonseca',
    'Section': '4B',
    'Spanish': 90.0,
    'English': 91.8,
    'Social Studies': 59.0,
    'Science': 55.0,
    'Average': 90.825}

# students = student1 + student2 # NO FUNCIONA

students = {**student1, **student2}

print(students)