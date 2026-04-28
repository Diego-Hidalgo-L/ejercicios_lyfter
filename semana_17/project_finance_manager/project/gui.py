
import FreeSimpleGUI as sg
from manager import FinanceManager
from datetime import date
from functions_gui import format_movement, show_add_category_window, show_add_movement_window, show_filter_by_date_window, filter_by_date
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
                    start_date = date.fromisoformat(dates["-START_DATE-"])
                    end_date = date.fromisoformat(dates["-END_DATE-"])

                    if start_date > end_date:
                        sg.popup_error("Start date must be before end date")
                        continue

                    filtered = filter_by_date(manager.get_movements(), start_date, end_date)

                    if not filtered:
                        sg.popup("No movements found in that range")
                        continue

                    window["-TABLE-"].update(
                        values=format_movement(filtered)
                    )

                except ValueError:
                    sg.popup_error("Invalid input")
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
                    category = data["-NEW_CATEGORY-"]
                    if not category:
                        sg.popup_error("No category entered")
                        continue
                
                    color = data["-COLOR-"]
                    if not color:
                        sg.popup_error("Choose a color for the category")
                        continue

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

            data = show_add_movement_window(type_, manager.get_categories())

            if data:
                try:
                    mov_date = data["-DATE-"]
                    try:
                        iso_date = date.fromisoformat(mov_date)
                    except ValueError:
                        sg.popup_error("Date must be in the format 'YYYY-MM-DD'")
                        continue
                    if iso_date > date.today():
                        sg.popup_error("Date cannot be in the future")
                        continue

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
                        manager.add_income(mov_date, title.strip(), amount, category)

                    elif type_ == "expense":
                        manager.add_expense(mov_date, title.strip(), amount, category)
                    
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
            movements = [m.convert_movement_to_dict() for m in manager.get_movements()]

            export_csv("semana_17/project_finance_manager/project/data.csv", movements, movements[0].keys())
            sg.popup("Successfully exported to CSV!")


        if event in (sg.WINDOW_CLOSED, "Exit", "Save and Exit", "Cancel"):
            break

    window.close()

