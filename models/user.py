# User model - Represents user entity with methods for registration, login, password hashing

from werkzeug.security import generate_password_hash
from database.database import create_user, get_user_by_username, validate_password

class User:

    # Initializes user attributes when a User object is created
    def __init__(self, id, username, password_hash):
        self.id = id  # Stores the unique user ID
        self.username = username  # Stores the username
        self.password_hash = password_hash  # Stores the hashed password 

    # Register new user
    @staticmethod
    def register(username, password):
        password_hash = generate_password_hash(password) # hash the password with generate_password_hash
        user_id = create_user(username, password_hash) # create_user from database.py
        return user_id # return new user id

    # Search user by username
    @staticmethod
    def get_by_username(username):
        result = get_user_by_username(username) # get_user_by_username
        # returns user data or none
        if result:
            user_data = result[0]
            return User(user_data['id'], user_data['username'], user_data['password_hash'])
        return None
    
    # Verify if password is correct
    def verify_password(self, password):
        # use validate_password from database.py
        return validate_password(self.id, password)