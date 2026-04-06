
import json
import os
import FreeSimpleGUI as sg
from manager import FinanceManager


# Functions
# def show_add_category_window(categories):
#     layout = [
#         [sg.Text("Add Category")],

#         [sg.Table(
#             values=categories,
#             headings=["Categories"],
#             key="-TABLE-",

#             auto_size_columns=False,
#             col_widths=[20, 10, 15, 10],
#             justification="left",

#             expand_x=True,
#             expand_y=True,
#             num_rows=10
#         )],

#         [sg.Text("New Category")], [sg.Input()],
#         [sg.Button("Save")], [sg.Button("Cancel")]
#     ]


# def verify_cancel_window():
#     layout = [
#         [sg.Text("Are you sure you want to cancel? All unsaved changes will be lost.")],

#         [sg.Button("Save")], [sg.Button("Exit")]
#     ]
    
#     window = sg.Window("Are you sure you want to cancel?", layout)

#     while True:
#         event, values = window.read()

#         if event in (sg.WINDOW_CLOSED, "Exit"):
#             window.close()
#             return None
        
#         if event == "Save":
#             # save_data(manager)
#             sg.popup("Changes saved!")
#             window.close()
#             return values


def format_movement(movements):
    return [[m.title, m.amount, m.category, m.type_] for m in movements]


def show_add_movement_window(type_, categories):
    layout = [
        [sg.Text(f"Add {type_.capitalize()}")],

        [sg.Text("Title")], [sg.Input(key="-TITLE-")],
        [sg.Text("Amount")], [sg.Input(key="-AMOUNT-")],
        [sg.Text("Category")], [sg.Combo(categories, key="-CATEGORY-", readonly=True)],

        [sg.Button("Save")], [sg.Button("Cancel")]
    ]

    window = sg.Window(f"Add {type_.capitalize()}", layout)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Cancel"):
            # verify_cancel_window()
            window.close()
            return None
        
        if event == "Save":
            window.close()
            return values


def save_data(manager):
    with open("semana_17/project_finance_manager/data.json", "w", encoding='utf-8') as file:
        json.dump(manager.convert_all_to_dict(), file, indent=4)

def load_data(manager):
    if not os.path.exists("semana_17/project_finance_manager/data.json"):
        return
    
    with open("semana_17/project_finance_manager/data.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    
    for category in data.get("categories", []):
        manager.add_category(category)
    
    for m in data.get("movements", []):
        if m["type"] == "income":
            manager.add_income(m["title"], m["amount"], m["category"])
        else:
            manager.add_expense(m["title"], abs(m["amount"]), m["category"])


def run_app():
    manager = FinanceManager()
    load_data(manager)

    # manager.add_category("Work")
    # manager.add_category("Food")

    # manager.add_income("Salary", 1500, "Work")
    # manager.add_expense("Lunch", 20, "Food")


    # Main window:
    layout = [
        [sg.Text("My First Finance Manager")],

        [sg.Table(
            values=format_movement(manager.get_movements()),
            headings=["Title", "Amount", "Category", "Type"],
            key="-TABLE-",

            auto_size_columns=False,
            col_widths=[20, 10, 15, 10],
            justification="left",

            expand_x=True,
            expand_y=True,
            num_rows=10
        )],

        [sg.Button("Add Category")], [sg.Button("Add Income")], [sg.Button("Add Expense")]
    ]

    window = sg.Window("Finance Manager", layout, resizable=True)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit"):
            break

        if event == "Add Category":
            print("'Add Category' clicked")

            window["-TABLE-"].update(
                values=format_movement(manager.get_movements())
            )

        if event in ("Add Income", "Add Expense"):
            if event == "Add Income":
                print("'Add Income' clicked")
                type_ = "income"
            
            elif event == "Add Expense":
                print("'Add Expense' clicked")
                type_ = "expense"

            data = show_add_movement_window(type_, manager.get_categories())

            if data:
                try:
                    title = data["-TITLE-"].strip()
                    if not title:
                        sg.popup_error("Title is required")
                        continue

                    amount_input = data["-AMOUNT-"]
                    if not amount_input:
                        sg.popup_error("Amount is required")
                        continue
                    try:
                        amount = float(amount_input)
                    except ValueError:
                        sg.popup_error("Amount must be a number")
                        continue


                    category = data["-CATEGORY-"]
                    if not category:
                        sg.popup_error("Please select a category")
                        continue

                    if type_ == "income":
                        manager.add_income(title.strip(), amount, category)

                    elif type_ == "expense":
                        manager.add_expense(title.strip(), amount, category)
                    
                    save_data(manager)

                    window["-TABLE-"].update(
                        values=format_movement(manager.get_movements())
                    )
                
                except Exception as e:
                    sg.popup_error(str(e))


    window.close()

