from flask import Flask, request, jsonify
from models import db, Task
import config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    task = Task(title=data["title"], description=data.get("description", ""))
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task created", "id": task.id}), 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "title": t.title, "status": t.status} for t in tasks])

@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify({"id": task.id, "title": task.title, "description": task.description, "status": task.status})

@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.json
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.status = data.get("status", task.status)
    db.session.commit()
    return jsonify({"message": "Task updated"})

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
