
import FreeSimpleGUI as sg
from manager import FinanceManager
from datetime import date
from pathlib import Path
from gui_second import show_add_category_window, show_add_movement_window, show_filter_by_date_window
from functions import format_movement, filter_by_date, validate_filter_dates
from persistence import save_data, load_data, export_csv


def run_app():
    manager = FinanceManager()
    load_data(manager)

    layout = [
        [sg.Text("My First Finance Manager")],

        [sg.Button("Filter by date"), sg.Button("Reset Filter")],
        [sg.Table(
            values=format_movement(manager.get_movements()),
            headings=["Date", "Title", "Amount", "Category", "Type"],
            key="-TABLE-",

            auto_size_columns=False,
            col_widths=[15, 12, 12, 15, 12],
            justification="center",

            expand_x=True,
            expand_y=True,
            num_rows=10
        )],

        [sg.Button("Add Category"), sg.Button("Add Income"), sg.Button("Add Expense")],
        # [sg.Button("Edit entry")],
        [sg.Button("Export to CSV")],
        [sg.Button("Save and Exit"), sg.Button("Cancel")]
    ]

    window = sg.Window("Finance Manager", layout, resizable=True)

    while True:
        event, values = window.read()

        if event == "Filter by date":
            print("'Filter by date' clicked")
            
            dates = show_filter_by_date_window()

            if dates:
                try:
                    start_date, end_date = validate_filter_dates(dates)

                    filtered = filter_by_date(manager.get_movements(), start_date, end_date)

                    if not filtered:
                        sg.popup("No movements found in that range")
                        continue

                    window["-TABLE-"].update(
                        values=format_movement(filtered)
                    )

                except ValueError as e:
                    sg.popup_error(str(e))
                except Exception as e:
                    sg.popup_error(str(e))
                    continue
        

        if event == "Reset Filter":
            print("'Reset Filter' clicked")

            window["-TABLE-"].update(
                        values=format_movement(manager.get_movements())
                    )


        if event == "Add Category":
            print("'Add Category' clicked")

            data = show_add_category_window(manager.get_categories())

            if data:
                try:
                    category = data.get("-NEW_CATEGORY-")
                
                    # color = data["-COLOR-"]
                    # if not color:
                    #     sg.popup_error("Choose a color for the category")
                    #     continue

                    manager.add_category(category)

                    save_data(manager)

                except Exception as e:
                    sg.popup_error(str(e))
                    continue


        if event in ("Add Income", "Add Expense"):
            if event == "Add Income":
                print("'Add Income' clicked")
                type_ = "income"
            
            elif event == "Add Expense":
                print("'Add Expense' clicked")
                type_ = "expense"

            if not manager.get_categories():
                sg.popup_error("There are no categories. You must enter a category first.")
                continue

            data = show_add_movement_window(type_, manager.get_categories())

            if data:
                try:
                    mov_date, title, amount, category = manager.validate_movement(data)
                except ValueError as e:
                    sg.popup_error(str(e))
                    continue

                try:
                    if type_ == "income":
                        manager.add_income(mov_date, title, amount, category)

                    elif type_ == "expense":
                        manager.add_expense(mov_date, title, amount, category)
                    
                    save_data(manager)
                    sg.popup("Changes saved!")

                    window["-TABLE-"].update(
                        values=format_movement(manager.get_movements())
                    )
                
                except Exception as e:
                    sg.popup_error(str(e))
                    continue
        

        # if event == "Edit entry":
        #     pass


        if event == "Export to CSV":
            CSV_FILE = Path("semana_17/project_finance_manager/project/data.csv")
            movements = [m.convert_movement_to_dict() for m in manager.get_movements()]

            try:
                export_csv(CSV_FILE, movements, movements[0].keys())
                sg.popup("Successfully exported to CSV!")
            except IndexError:
                sg.popup_error("There is no data available to export to CSV.")
                continue


        if event in (sg.WINDOW_CLOSED, "Exit", "Save and Exit", "Cancel"):
            break

    window.close()

