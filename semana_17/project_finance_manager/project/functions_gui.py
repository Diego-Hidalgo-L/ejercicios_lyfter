
import FreeSimpleGUI as sg

def verify_cancel_window():
    layout = [
        [sg.Text("Are you sure you want to exit? All unsaved changes will be lost.")],

        [sg.Button("Back")], [sg.Button("Exit")]
    ]
    
    window = sg.Window("Are you sure you want to exit?", layout)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit"):
            window.close()
            return None
        
        if event == "Back":
            window.close()
            return "Back"


def show_add_category_window(categories):
    layout = [
        [sg.Text("Add Category")],

        [sg.Table(
            values=categories,
            headings=["Categories"],
            key="-TABLE-",

            auto_size_columns=False,
            col_widths=[20, 10, 15, 10],
            justification="left",

            expand_x=True,
            expand_y=True
        )],

        [sg.Text("New Category:")], [sg.Input(key="-NEW_CATEGORY-")],
        [sg.Button("Save")], [sg.Button("Cancel")]
    ]

    window = sg.Window("Add a new category", layout)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Cancel"):
            window.close()
            return None
        
        if event == "Save":
            window.close()
            return values


def format_movement(movements):
    return [[m.mov_date, m.title, m.amount, m.category, m.type_] for m in movements]


# Alternativa de format_movement(movements) si la utilizo para FILTRAR POR FECHA:
# def format_movement(movements, start_date, end_date)
    # return [[m.mov_date, m.title, m.amount, m.category, m.type_] for m in movements if start_date <= m.mov_date <= end_date]


def show_add_movement_window(type_, categories):
    layout = [
        [sg.Text(f"Add {type_.capitalize()}")],

        [sg.Text("Date")], [sg.Input(key="-DATE-", default_text="YYYY-MM-DD")],
        [sg.Text("Title")], [sg.Input(key="-TITLE-")],
        [sg.Text("Amount")], [sg.Input(key="-AMOUNT-")],
        [sg.Text("Category")], [sg.Combo(categories, key="-CATEGORY-", readonly=True)],

        [sg.Button("Save")], [sg.Button("Cancel")]
    ]

    window = sg.Window(f"Add {type_.capitalize()}", layout)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Cancel"):
            if verify_cancel_window():
                continue
            window.close()
            return None
        
        if event == "Save":
            window.close()
            return values