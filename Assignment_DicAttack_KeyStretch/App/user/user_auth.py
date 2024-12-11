import os
import bcrypt

USER_DATA_FILE = os.path.join(os.path.dirname(__file__), "userdata.txt")

# Function to hash the password using bcrypt
def hash_password(password):
    salt = bcrypt.gensalt()  
    hashed_password = bcrypt.hashpw(password.encode(), salt)  
    return hashed_password, salt

# Check if a username exists
def is_username_exist(username):
    if not os.path.exists(USER_DATA_FILE):
        return False

    with open(USER_DATA_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if len(parts) == 3:
                saved_username, _, _ = parts
                if saved_username == username:
                    return True
    return False

# Save user credentials
def save_user(username, password):
    if is_username_exist(username):
        print("Error: Username already exists.")
        return
    hashed_password, salt = hash_password(password)  # Hash the password
    with open(USER_DATA_FILE, "a") as file:
        file.write(f"{username}:{hashed_password.decode()}:{salt.decode()}\n")  # Store hash and salt as strings

# Verify login credentials
def verify_login(username, password):
    if not os.path.exists(USER_DATA_FILE):
        return False
    with open(USER_DATA_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if len(parts) == 3:
                stored_username, stored_hashed_password, stored_salt = parts
                if stored_username == username:
                    # bcrypt already handles salt, so we just hash the input password and compare
                    if bcrypt.checkpw(password.encode(), stored_hashed_password.encode()):
                        return True
    return False
