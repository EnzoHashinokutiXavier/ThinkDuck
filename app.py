# Main Flask application - Initialize Flask app, configure routes, and run the serverfrom flask import Flask
from flask_session import Session
from routes.auth import auth_bp
from routes.projects import projects_bp
from routes.sessions import sessions_bp

app = Flask(__name__)

# Configuração de sessões
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Registrar blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(projects_bp)
app.register_blueprint(sessions_bp)

if __name__ == "__main__":
    app.run(debug=True)