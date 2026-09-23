from flask import json

status_list = ["pending", "in progress", "completed"]

def read_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)

    except FileNotFoundError:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump([], file)

        return []


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def validate_task(request_body, task_list):
    identifier = request_body.get("identifier")
    title = request_body.get("title")
    description = request_body.get("description")
    status = request_body.get("status")

    if identifier is None:
        raise ValueError("The identifier is empty.")

    for task in task_list:
            if task.get("identifier") == identifier:
                raise ValueError(f"The identifier '{identifier}' already exists.")
    
    if not title:
        raise ValueError("The task needs to have a title.")

    if not description:
        raise ValueError("The task needs to have a description.")

    if not status:
        raise ValueError("The task needs to have a status.")

    if status.strip().lower() not in status_list:
        raise ValueError("Invalid status. Enter one of the following: 'Pending', 'In progress', 'Completed'.")


def filter_list(status_filter, task_list):
    return list(
                filter(lambda task: task["status"] == status_filter, task_list)
            )