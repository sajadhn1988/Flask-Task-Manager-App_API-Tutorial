from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
from models.user import User
from flask import jsonify

def auth_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        current_user = User.query.get(user_id)
        if not current_user:
            return jsonify({'message': 'User not found'}), 404
        return fn(*args, **kwargs)  # Do not pass current_user
    return wrapper