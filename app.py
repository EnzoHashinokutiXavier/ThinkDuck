# Main Flask application - Initialize Flask app, configure routes, and run the server
from flask import Flask
from flask_session import Session
from config import SECRET_KEY, DEBUG, SESSION_PERMANENT, SESSION_TYPE
from routes.auth import auth_bp
from routes.projects import projects_bp
from routes.sessions import sessions_bp

# Initialize Flask app
app = Flask(__name__)

# Load configuration from config.py
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SESSION_PERMANENT"] = SESSION_PERMANENT
app.config["SESSION_TYPE"] = SESSION_TYPE
Session(app) # Activates session manager

# Register blueprints - connect different route modules to the application
app.register_blueprint(auth_bp) # Authentication routes
app.register_blueprint(projects_bp) # Projects routes
app.register_blueprint(sessions_bp) # Sessions routes

# Start server in development mode
if __name__ == "__main__":
    app.run(debug=DEBUG) # Auto-reload controlled by config.py