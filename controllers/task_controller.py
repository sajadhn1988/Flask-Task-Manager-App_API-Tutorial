from flask import jsonify, request
from config.db import db
from models.task import Task

def get_all_tasks():
    try:
        tasks = Task.query.all()
        return jsonify([task.to_dict() for task in tasks]), 200
    except Exception as e:
        return jsonify({'message': 'Server error', 'error': str(e)}), 500

def get_task_by_id(id):
    try:
        task = Task.query.get(id)
        if not task:
            return jsonify({'message': 'Task not found'}), 404
        return jsonify(task.to_dict()), 200
    except Exception as e:
        return jsonify({'message': 'Server error', 'error': str(e)}), 500

def create_task():
    try:
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        status = data.get('status', 'pending')

        if not title:
            return jsonify({'message': 'Title is required'}), 400

        if status not in ['pending', 'in-progress', 'completed']:
            return jsonify({'message': 'Invalid status'}), 400

        task = Task(title=title, description=description, status=status)
        db.session.add(task)
        db.session.commit()
        return jsonify(task.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Server error', 'error': str(e)}), 500

def update_task(id):
    try:
        data = request.get_json()
        task = Task.query.get(id)
        if not task:
            return jsonify({'message': 'Task not found'}), 404

        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.status = data.get('status', task.status)

        if task.status not in ['pending', 'in-progress', 'completed']:
            return jsonify({'message': 'Invalid status'}), 400

        db.session.commit()
        return jsonify(task.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Server error', 'error': str(e)}), 500

def delete_task(id):
    try:
        task = Task.query.get(id)
        if not task:
            return jsonify({'message': 'Task not found'}), 404
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Server error', 'error': str(e)}), 500