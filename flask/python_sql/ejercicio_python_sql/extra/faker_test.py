from faker import Faker
from tarea_3.db import db_manager

fake = Faker()

print(fake.date())

results = db_manager.fetchall("SELECT id FROM cars;")
print(results)