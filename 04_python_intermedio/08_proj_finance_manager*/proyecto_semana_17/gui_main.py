
import FreeSimpleGUI as sg
from manager import FinanceManager
from gui_second import show_add_category_window, show_edit_category_window, show_add_movement_window, show_filter_by_date_window
from functions import format_movement, build_row_colors, filter_by_date, validate_filter_dates, refresh_table
from persistence import save_data, load_data, export_csv, CSV_FILE


def run_app():
    manager = FinanceManager()
    load_data(manager)

    movements = manager.get_movements()

    layout = [
        [sg.Text("My First Finance Manager")],

        [sg.Button("Filter by date"), sg.Button("Reset Filter")],
        [sg.Table(
            values=format_movement(manager.get_movements()),
            headings=["Date", "Title", "Amount", "Category", "Type"],
            key="-TABLE-",

            row_colors=build_row_colors(movements, manager),
            auto_size_columns=False,
            col_widths=[15, 12, 12, 15, 12],
            justification="center",

            expand_x=True,
            expand_y=True,
            num_rows=10
        )],

        [sg.Button("Add Category"), sg.Button("Edit Category color")],
        [sg.Button("Add Income"), sg.Button("Add Expense")],
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

                    filtered = filter_by_date(movements, start_date, end_date)

                    if not filtered:
                        sg.popup("No movements found in that range")
                        continue

                    refresh_table(window, movements, manager)

                except ValueError as e:
                    sg.popup_error(str(e))
                except Exception as e:
                    sg.popup_error(str(e))
                    continue


        if event == "Reset Filter":
            print("'Reset Filter' clicked")

            refresh_table(window, movements, manager)


        if event == "Add Category":
            print("'Add Category' clicked")

            data = show_add_category_window(manager.get_categories(), movements, manager)

            if data:
                try:
                    category_data = {
                        "name": data.get("-NEW_CATEGORY-"),
                        "color": data.get("-COLOR-")
                    }

                    manager.add_category(category_data)

                    save_data(manager)

                except Exception as e:
                    sg.popup_error(str(e))
                    continue

        
        if event == "Edit Category color":
            print("'Edit category' clicked")

            data = show_edit_category_window(manager.get_categories())

            if data:
                try:
                    name = data.get("-CATEGORY-")
                    color = data.get("-COLOR-")

                    manager.update_category_color(name, color)

                    refresh_table(window, movements, manager)
                    sg.popup("Color changed successfully!")

                    save_data(manager)

                except ValueError as e:
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

                    refresh_table(window, movements, manager)
                
                except Exception as e:
                    sg.popup_error(str(e))
                    continue


        # if event == "Edit entry":
        #     pass


        if event == "Export to CSV":
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

