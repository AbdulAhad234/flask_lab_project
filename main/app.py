from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
todos = []

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/health")
def health():
    return "OK", 200

@app.route("/add", methods=["POST"])
def add_todo():
    data = request.get_json(silent=True)
    if not data or "task" not in data:
        return jsonify({"error": "Invalid data"}), 400
    todos.append({"task": data["task"], "done": False})
    return jsonify({"message": "Task added"}), 201

@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle(task_id):
    if 0 <= task_id < len(todos):
        todos[task_id]["done"] = not todos[task_id]["done"]
        return jsonify({"message": "Toggled"}), 200
    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
