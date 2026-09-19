from flask import Flask, request, jsonify
from functions import status_list, read_json, save_json, validate_task, filter_list

app = Flask(__name__)


@app.route("/tasks")
def get_tasks():
    task_list = read_json("tasks.json")
    status_filter = request.args.get("status") 

    if status_filter:
        status_filter = status_filter.strip().capitalize()
        return filter_list(status_filter, task_list)

    return task_list


@app.route("/tasks", methods=["POST"])
def add_task():
    request_body = request.json
    status = request_body.get("status")
    task_list = read_json("tasks.json")

    try:
        validate_task(request_body, task_list)
        request_body["status"] = status.capitalize()
        task_list.append(request_body)
        save_json("tasks.json", task_list)

    except ValueError as e:
        return jsonify(error_message=str(e)), 400

    return jsonify(request_body), 201


@app.route("/tasks/<identifier>", methods=["PATCH", "PUT"])
def edit_task(identifier):
    task_list = read_json("tasks.json")
    title = request.json.get("title")
    description = request.json.get("description")
    status = request.json.get("status")
    task_found = False

    if identifier is None:
        return jsonify(error_message="The identifier is empty"), 404

    for task in task_list:
        if task.get("identifier") == identifier:
            task_found = True

            if title:
                task["title"] = title

            if description:
                task["description"] = description

            if status:
                if status.strip().lower() not in status_list:
                    return jsonify(error_message="Invalid status. Enter one of the following: 'Pending', 'In progress', 'Completed'."), 400

                task["status"] = status.capitalize()

            break

    if not task_found:
        return jsonify(error_message=f"The task '{identifier}' does not exist."), 404

    save_json("tasks.json", task_list)
    return jsonify(message=f"The task '{identifier}' was edited.")


@app.route("/tasks/<identifier>", methods=["DELETE"])
def delete_task(identifier):
    task_list = read_json("tasks.json")

    for i, task in enumerate(task_list):
        if task.get("identifier") == identifier:
            task_list.pop(i)
            save_json("tasks.json", task_list)

            return jsonify(message=f"The task '{identifier}' was deleted.")

    return jsonify(error_message=f"The task '{identifier}' does not exist."), 404


if __name__ == "__main__":
    app.run(host='localhost', port=8000, debug=True)