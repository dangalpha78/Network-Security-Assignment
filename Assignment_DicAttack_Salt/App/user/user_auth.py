import os
import hashlib
import random
import string

# USER_DATA_FILE = "Network-Security-Assignment/App/user/userdata.txt"
USER_DATA_FILE = os.path.join(os.path.dirname(__file__), "userdata.txt")

print("Absolute Path:", os.path.abspath(USER_DATA_FILE))

# Function to create a salt
def generate_salt(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def hash_password(password, salt=None):
    if salt is None:
        salt = generate_salt()  # Generate a new salt if not provided
    password_with_salt = password + salt
    return hashlib.sha256(password_with_salt.encode()).hexdigest(), salt  # Use SHA-256 for better security


def is_username_exist(username):
    if not os.path.exists(USER_DATA_FILE):
        return False

    with open(USER_DATA_FILE, "r") as file:
        for line in file:
            line = line.strip()  
            if not line:  
                continue
            
            parts = line.split(":")
            if len(parts) == 3: 
                saved_username, _, _ = parts 
                if saved_username == username:
                    return True
            else:
                print(f"Skipping invalid line: {line}")  
                
    return False



def save_user(username, password):
    salt = generate_salt()
    hashed_password, salt = hash_password(password, salt)
    with open(USER_DATA_FILE, "a") as file:
        file.write(f"{username}:{hashed_password}:{salt}\n")


# Verify the password during login
def verify_login(username, password):
    if not os.path.exists(USER_DATA_FILE):
        return False
    with open(USER_DATA_FILE, "r") as file:
        for line in file:
            stored_username, stored_hashed_password, stored_salt = line.strip().split(":")
            if stored_username == username:
                hashed_input_password, _ = hash_password(password, stored_salt)
                if stored_hashed_password == hashed_input_password:
                    return True
    return False

