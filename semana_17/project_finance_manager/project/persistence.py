
import csv
import json
from pathlib import Path

JSON_FILE = Path("semana_17/project_finance_manager/project/data.json")

def save_data(manager):
    with open(JSON_FILE, "w", encoding='utf-8') as file:
        json.dump(manager.convert_all_to_dict(), file, indent=4)


def load_data(manager):
    if not JSON_FILE.exists():
        return
    
    with open(JSON_FILE, "r", encoding='utf-8') as file:
        data = json.load(file)
    
    for category in data.get("categories", []):
        manager.add_category(category)
    
    for m in data.get("movements", []):
        if m["type"] == "income":
            manager.add_income(m["date"], m["title"], m["amount"], m["category"])
        else:
            manager.add_expense(m["date"], m["title"], abs(m["amount"]), m["category"])


def export_csv(path, data, headers):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

        

