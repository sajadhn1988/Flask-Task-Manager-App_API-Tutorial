from flask import Blueprint
from controllers.user_controller import register_user, login_user, update_user_role, get_all_users, delete_user
from middleware.auth import auth_required
from middleware.role import role_required

user_bp = Blueprint('users', __name__)

user_bp.route('/register', methods=['POST'])(register_user)
user_bp.route('/login', methods=['POST'])(login_user)
user_bp.route('/update-role/<int:id>', methods=['PUT'])(auth_required(role_required(['admin'])(update_user_role)))
user_bp.route('/admin-user-list', methods=['GET'])(auth_required(role_required(['admin'])(get_all_users)))
user_bp.route('/delete/<int:id>', methods=['DELETE'])(auth_required(role_required(['admin'])(delete_user)))