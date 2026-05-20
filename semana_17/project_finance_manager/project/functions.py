
from datetime import date


def format_movement(movements):
    return [[m.mov_date, m.title, m.amount, m.category, m.type_] for m in movements]


def build_row_colors(movements, manager):
    row_colors = []

    for i, m in enumerate(movements):
        color = manager.categories.get(m.category,{}).get("color", "#FFFFFF")
        row_colors.append((i, "black", color))

    return row_colors


def filter_by_date(movements, start_date, end_date):
    return [m for m in movements if start_date <= m.date <= end_date]


def validate_filter_dates(dates):
    try:
        start_date = date.fromisoformat(dates["-START_DATE-"])
        end_date = date.fromisoformat(dates["-END_DATE-"])
    except ValueError:
        raise ValueError("Invalid input")

    if start_date > end_date:
        raise Exception("Start date must be before end date")
    
    return start_date, end_date


def refresh_table(window, movements, manager):
    window["-TABLE-"].update(
        values=format_movement(movements),
        row_colors=build_row_colors(movements, manager)
    )