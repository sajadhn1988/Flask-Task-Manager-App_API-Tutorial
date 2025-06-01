from flask import Blueprint
from controllers.task_controller import get_all_tasks, get_task_by_id, create_task, update_task, delete_task
from middleware.auth import auth_required
from middleware.role import role_required

task_bp = Blueprint('tasks', __name__)

task_bp.route('/get-all', methods=['GET'])(auth_required(role_required(['admin', 'editor', 'viewer'])(get_all_tasks)))
task_bp.route('/single-task/<int:id>', methods=['GET'])(auth_required(role_required(['admin', 'editor', 'viewer'])(get_task_by_id)))
task_bp.route('/create', methods=['POST'])(auth_required(role_required(['admin', 'editor'])(create_task)))
task_bp.route('/update/<int:id>', methods=['PUT'])(auth_required(role_required(['admin', 'editor'])(update_task)))
task_bp.route('/delete/<int:id>', methods=['DELETE'])(auth_required(role_required(['admin'])(delete_task)))