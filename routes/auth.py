# Authentication routes - Handles login, register, and logout endpoints
from flask import Blueprint, render_template, redirect, request, session

auth_bp = Blueprint("auth", __name__)

# Index 
@auth_bp.route("/")
def index():
    user_id = session.get("user_id")
    username = session.get("username")
    return render_template("index.html", user_id=user_id, username=username)

# Register
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    # GET shows form
    # POST: 
        # validate entry (username, password, confirmation)
        # verify if username already exists
        # uses User.register()
        # redirects to login or erro
    return

# Autenticate user
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # GET shows login form
    # POST :
        # validate entry
        # uses User.get_by_username() to search user
        # uses User.verify_password() 
        # saves user_id and username in session
        # redirect to / or erro
    return

# Logout session
@auth_bp.route("/logout")
def logout():
    session.clear() # clear session
    return redirect("/") # redirect to /