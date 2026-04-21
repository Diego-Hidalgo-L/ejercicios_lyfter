
import FreeSimpleGUI as sg

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
            # verify_cancel_window()
            window.close()
            return None
        
        if event == "Save":
            window.close()
            return values