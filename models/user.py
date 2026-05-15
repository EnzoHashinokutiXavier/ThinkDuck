# User model - Represents user entity with methods for registration, login, password hashing

from werkzeug.security import generate_password_hash, check_password_hash
from database.database import create_user, get_user_by_username

class User:

    # Initializes user attributes when a User object is created
    def __init__(self, id, username, password_hash):
        self.id = id  # Stores the unique user ID
        self.username = username  # Stores the username
        self.password_hash = password_hash  # Stores the hashed password 

    # Register new user
    @staticmethod
    def register(username, password):
        # hash the password with generate_assword_hash
        # create_user from database.py
        return # return new user id

    # Search user by username
    @staticmethod
    def get_by_username(username):
        # get_user_by_username
        return # returns user data or none

    # Verify if password is correct
    def verify_password(password):
        # compare password with hash stored
        # use check_password_hash
        return # returns true or false