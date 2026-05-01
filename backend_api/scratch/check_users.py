import os
import sys

# Add parent directory to sys.path to find database module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import database
from flask import Flask

app = Flask(__name__)
# Initialize bcrypt or other extensions if needed
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
database.bcrypt = bcrypt

with app.app_context():
    try:
        conn, db_type = database.get_db_connection()
        c = conn.cursor()
        c.execute("SELECT id, name, email, role FROM users")
        users = c.fetchall()
        print(f"Users in DB: {users}")
        conn.close()
    except Exception as e:
        print(f"DB Error: {e}")
