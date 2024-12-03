import os
import hashlib

USER_DATA_FILE = "user/userdata.txt"

# Function to hash the password
# We use SHA-1 hash function
def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()

# Check if the username exist or not
def is_username_exist(username):
    if not os.path.exists(USER_DATA_FILE):
        return False
    
    with open(USER_DATA_FILE, "r") as file:
        for line in file:
            if line: # Check if first line is NULL or not
                saved_username, _ = line.split(":")
                if saved_username == username:
                    return True
    return False

# Store user's username and password
def save_user(username, password):
    hashed_password = hash_password(password)
    with open(USER_DATA_FILE, "a") as file:
        file.write(f"{username}:{hashed_password}\n")

# Login verification
def verify_login(username, password):
    hashed_password = hash_password(password)
    if not os.path.exists(USER_DATA_FILE):
        return False
    with open(USER_DATA_FILE, "r") as file:
        for line in file:
            stored_username, stored_hashed_password = line.strip().split(":")
            if stored_username == username and stored_hashed_password == hashed_password:
                return True
    return False
