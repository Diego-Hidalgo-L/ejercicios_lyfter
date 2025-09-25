
# 


list_of_employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

dict_by_department = {}


for employee in list_of_employees:
    department = employee.get("department")
    name = employee.get("name")
    email = employee.get("email")

    if department in dict_by_department:
        dict_by_department[department].append({"name": name, "email": email})
    else:
        dict_by_department[department] = [{"name": name, "email": email}]
    
print(dict_by_department)

dict_by_department = {
'Ventas': [
    {'name': 'Carlos', 'email': 'carlos@empresa.com'},
    {'name': 'Luis', 'email': 'luis@empresa.com'}
    ],
'TI':[
    {'name': 'Ana', 'email': 'ana@empresa.com'}
    ],
'RRHH': [
    {'name': 'Sofía', 'email': 'sofia@empresa.com'}
    ]
}