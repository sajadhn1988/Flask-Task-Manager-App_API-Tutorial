from flask_jwt_extended import get_jwt
from functools import wraps
from flask import jsonify

def role_required(required_roles):
    def decorator(fn):  # Define fn as the function being decorated
        @wraps(fn)
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            user_role = claims.get('role')
            if not user_role or user_role not in required_roles:
                return jsonify({'message': 'Access denied: insufficient permissions'}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator