# App configurations - Secret key, database path, Flask settings

import os
from datetime import timedelta

# Gets the directory where this file (config.py) is located
# Avoids hardcoded values
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Configure secret key for Flask
# Encrypt session cookies (login data) and protect against CSRF attacks (request forgery)
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production') # If not set, uses 'dev-secret-key-change-in-production' for development
# DO NOT USE DEFAULT KEY IN PRODUCTION

# Sets the path for the database.db file
# Uses BASE_DIR + relative path
DATABASE_PATH = os.path.join(BASE_DIR, 'database', 'database.db')

# Configures session to expire when browser closes
SESSION_PERMANENT = False

# Defines where session information is stored
SESSION_TYPE = 'filesystem' # 'filesystem' = saves in files (flask_session/ folder)

# Enables auto-reload
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true' # If not set, default is 'True'
# In production, set to false


# In development:
# random secret key for testing
# session saved in files
# debug true for autoreload
# database in database/database.db

# In production:
# secret key defined
# debug false
# database path defined