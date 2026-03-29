
import FreeSimpleGUI as sg
from manager import FinanceManager

manager = FinanceManager()

manager.add_category("Work")
manager.add_category("Food")

manager.add_income("Salary", 1500, "Work")
manager.add_expense("Lunch", 20, "Food")


# Internal functions
def format_movement(movements):
    return [[m.title, m.amount, m.category, m.type_] for m in movements]


def show_add_income_window(categories):
    layout = [
        [sg.Text("Add Income")],

        [sg.Text("Title")], [sg.Input(key="-TITLE-")],
        [sg.Text("Amount")], [sg.Input(key="-AMOUNT-")],
        [sg.Text("Category")], [sg.Combo(categories, key="-CATEGORY-")],

        [sg.Button("Save")], [sg.Button("Cancel")]
    ]

    window = sg.Window("Add Income", layout)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Cancel"):
            window.close()
            return None
        
        if event == "Save":
            return values


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

    [sg.Button("Add Category")],
    [sg.Button("Add Income")],
    [sg.Button("Add Expense")]
]


if __name__ == "__main__":
    window = sg.Window("Finance Manager", layout, resizable=True)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit"):
            break

        if event == "Add Category":
            # window["-TABLE-"].update(
            #     values=format_movement(manager.get_movements())
            # )
            print("'Add Category' clicked")

        if event == "Add Income":
            data = show_add_income_window(manager.get_categories())

            if data:
                try:
                    title = data["-TITLE-"].capitalize()
                    amount = float(data["-AMOUNT-"])
                    category = data["-CATEGORY-"].capitalize()

                    manager.add_income(title, amount, category)

                    window["-TABLE-"].update(
                        values=format_movement(manager.get_movements())
                    )
                
                except Exception as e:
                    sg.popup_error(str(e))


        if event == "Add Expense":
            print("'Add Expense' clicked")
    
    window.close()

