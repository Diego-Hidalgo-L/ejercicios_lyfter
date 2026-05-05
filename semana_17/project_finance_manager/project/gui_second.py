
import FreeSimpleGUI as sg
from datetime import date

def verify_cancel_window():
    layout = [
        [sg.Text("Are you sure you want to exit? All unsaved changes will be lost.")],

        [sg.Button("Back"), sg.Button("Exit")]
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
        [sg.ColorChooserButton("Choose color", key="-COLOR-")],
        
        [sg.Button("Save"), sg.Button("Cancel")]
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


def show_filter_by_date_window():
    layout = [
        [sg.Text("Filter movements by date")],

        [sg.Text("Start date")], [sg.Input(key='-START_DATE-', tooltip="YYYY-MM-DD")],
        [sg.Text("End date")], [sg.Input(key='-END_DATE-', tooltip="YYYY-MM-DD")], # Podría hacer esto un sg.CalendarButton()

        [sg.Button("Filter")], [sg.Button("Cancel")]
    ]

    window = sg.Window("Filter movements by date", layout)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Cancel"):
            window.close()
            return None
        
        if event == "Filter":
            window.close()
            return values


def show_add_movement_window(type_, categories):
    layout = [
        [sg.Text(f"Add {type_.capitalize()}")],

        [sg.Text("Date")], [sg.Input(key="-DATE-", default_text=date.today())],
        [sg.Text("Title")], [sg.Input(key="-TITLE-")],
        [sg.Text("Amount")], [sg.Input(key="-AMOUNT-")],
        [sg.Text("Category")], [sg.Combo(categories, key="-CATEGORY-", readonly=True)],

        [sg.Button("Save")], [sg.Button("Cancel")]
    ]

    window = sg.Window(f"Add {type_.capitalize()}", layout)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Cancel"):
            if not verify_cancel_window():
                window.close()
                return None
        
        if event == "Save":
            window.close()
            return values