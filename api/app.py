
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory task storage
tasks = {}
task_id_counter = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.json
    task_id = task_id_counter
    tasks[task_id] = {"id": task_id, "name": data.get("name"), "status": data.get("status", "pending")}
    task_id_counter += 1
    return jsonify(tasks[task_id]), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404
    tasks[task_id].update(data)
    return jsonify(tasks[task_id])

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404
    del tasks[task_id]
    return '', 204

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(list(tasks.values()))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
