import os
import sys

# Add parent directory to sys.path to find database module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import database
from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
database.bcrypt = bcrypt

with app.app_context():
    try:
        # Create Admin user
        admin_email = "admin@interviewer.ai"
        admin_password = "Admin@123"
        admin_name = "System Admin"
        
        # Check if already exists
        user = database.authenticate_user(admin_email, admin_password)
        if user:
            print("Admin user already exists.")
        else:
            # Manually inject or use create_user
            user_id, error = database.create_user(
                name=admin_name,
                email=admin_email,
                phone="0000000000",
                password=admin_password,
                photo="", # Empty for now
                role="admin"
            )
            if error:
                print(f"Failed to create admin: {error}")
            else:
                print(f"Admin user created successfully with ID: {user_id}")
                
    except Exception as e:
        print(f"Error: {e}")
