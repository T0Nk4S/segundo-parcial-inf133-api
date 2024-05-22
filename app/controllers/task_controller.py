# app/controllers/task_controller.py

from flask import jsonify, request
from models.task_model import Task
from database import db

def list_tasks():
    tasks = Task.query.all()
    return jsonify([task.serialize() for task in tasks]), 200

def create_task():
    data = request.json
    new_task = Task(
        title=data['title'],
        description=data['description'],
        status=data['status'],
        created_at=data['created_at'],
        assigned_to=data['assigned_to']
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.serialize()), 201

def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task.serialize()), 200

def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    data = request.json
    task.status = data.get('status', task.status)
    db.session.commit()
    return jsonify(task.serialize()), 200

def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return '', 204
