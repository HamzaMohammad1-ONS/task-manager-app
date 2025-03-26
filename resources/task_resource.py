from flask_restful import Resource, Api
from flask import request, jsonify
from models import db, Task

class TaskResource(Resource):
    def get(self):
        tasks = Task.query.all()
        return jsonify([{'id': task.id, 'title': task.title, 'description': task.description, 'priority': task.priority, 'done': task.done} for task in tasks])

    def post(self):
        data = request.get_json()
        new_task = Task(
            title=data['title'],
            description=data.get('description'),
            priority=data.get('priority', 'Normal'),
            done=data.get('done', False)
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task created', 'task': {'id': new_task.id, 'title': new_task.title}})

    def put(self, task_id):
        data = request.get_json()
        task = Task.query.get_or_404(task_id)
        task.title = data['title']
        task.description = data.get('description', task.description)
        task.priority = data.get('priority', task.priority)
        task.done = data.get('done', task.done)
        db.session.commit()
        return jsonify({'message': 'Task updated', 'task': {'id': task.id, 'title': task.title}})

    def delete(self, task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted'})
