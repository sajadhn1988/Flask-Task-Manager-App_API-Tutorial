from flask import jsonify, request
from config.db import db
from models.user import User
from flask_jwt_extended import create_access_token

def register_user():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400

        if User.query.filter_by(username=username).first():
            return jsonify({'message': 'Username already exists'}), 400

        user = User(username=username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()

        # Use user.id as a string for identity, add role as additional claim
        token = create_access_token(identity=str(user.id), additional_claims={'role': user.role})
        return jsonify({'token': token, 'user': user.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Server error', 'error': str(e)}), 500

def login_user():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400

        user = User.query.filter_by(username=username).first()
        if not user or not user.verify_password(password):
            return jsonify({'message': 'Invalid credentials'}), 401

        # Use user.id as a string for identity, add role as additional claim
        token = create_access_token(identity=str(user.id), additional_claims={'role': user.role})
        return jsonify({'token': token, 'user': user.to_dict()}), 200
    except Exception as e:
        return jsonify({'message': 'Server error', 'error': str(e)}), 500

def update_user_role(id):
    try:
        data = request.get_json()
        role = data.get('role')

        if role not in ['admin', 'editor', 'viewer']:
            return jsonify({'message': 'Invalid role'}), 400

        user = User.query.get(id)
        if not user:
            return jsonify({'message': 'User not found'}), 404

        user.role = role
        db.session.commit()
        return jsonify({'user': user.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Server error', 'error': str(e)}), 500

def get_all_users(current_user=None):
    try:
        users = User.query.all()
        return jsonify([user.to_dict() for user in users]), 200
    except Exception as e:
        return jsonify({'message': 'Server error', 'error': str(e)}), 500

def delete_user(id):
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({'message': 'User not found'}), 404
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Server error', 'error': str(e)}), 500