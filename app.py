from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config.db import init_db
from routes.task_routes import task_bp
from routes.user_routes import user_bp
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Base Configuration
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')
    app.config['PROPAGATE_EXCEPTIONS'] = True
    
    # Configure CORS
    allowed_origins = [
        os.getenv('BASE_URL'),
        os.getenv('FRONTEND_URL')
    ]
    CORS(app, resources={r"/*": {"origins": allowed_origins}}, supports_credentials=True)

    # Initialize JWT
    jwt = JWTManager(app)
    
    # Initialize Database
    init_db(app)
    
    # Register Blueprints
    app.register_blueprint(task_bp, url_prefix='/tasks')
    app.register_blueprint(user_bp, url_prefix='/users')
    
    # Test route
    @app.route('/test', methods=['GET'])
    def test():
        return jsonify({"message": "This is a test"})
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not found"}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error"}), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.getenv('PORT', 5000))
    app.run(port=port, debug=True)