import hashlib
import os
import time

# File paths
# USERDATA_FILE = os.path.join("..", "Network-Security-Assignment", "Assignment", "App", "user", "userdata.txt")
USERDATA_FILE = os.path.join("..", "App", "user", "userdata.txt")

# Print the absolute path
print("Absolute Path:", os.path.abspath(USERDATA_FILE))

# Check if the path exists
print("Path Exists:", os.path.exists(USERDATA_FILE))
# USERDATA_FILE = os.path.join("..", "Network-Security-Assignment/Assignment/App/user", "userdata.txt")
USERDATA_FILE = os.path.join("..", "App/user", "userdata.txt")
DICTIONARY_FILE = os.path.join("rockyou.txt")

# Function to hash the password with SHA-256
def hash_with_sha256(password):
    return hashlib.sha1(password.encode()).hexdigest()

# Function to load userdata from the file
def load_userdata(filename):
    userdata = {}
    if not os.path.exists(filename):
        print(f"Error: '{filename}' not found.")
        return userdata

    with open(filename, "r") as file:
        for line in file:
            username, hashed_password = line.strip().split(":")
            userdata[username] = hashed_password
    return userdata

# Function to perform dictionary attack
def dictionary_attack(userdata_file, dictionary_file):
    # Load user data and dictionary
    userdata = load_userdata(userdata_file)
    if not userdata:
        return {}

    if not os.path.exists(dictionary_file):
        print(f"Error: '{dictionary_file}' not found.")
        return {}

    with open(dictionary_file, "r", encoding="utf-8", errors="ignore") as file:
        dictionary = [line.strip() for line in file]

    # Try cracking passwords
    cracked_passwords = {}
    for username, hashed_password in userdata.items():
        found_password = ""
        for word in dictionary:
            if hash_with_sha256(word) == hashed_password:
                found_password = word
                break
        cracked_passwords[username] = found_password

    return cracked_passwords

# Main function for dictionary attack
def main():
    start_time = time.time()  # Ghi nhận thời gian bắt đầu
    
    print("Starting Dictionary Attack...")
    cracked = dictionary_attack(USERDATA_FILE, DICTIONARY_FILE)
    
    end_time = time.time()  # Ghi nhận thời gian kết thúc
    elapsed_time = end_time - start_time  # Tính thời gian thực thi
    
    if cracked:
        print("\nCracked Passwords:")
        for username, password in cracked.items():
            print(f"Username: '{username}', Password: '{password}'")
    else:
        print("No passwords were cracked or files are missing.")
    
    # Hiển thị thời gian thực thi
    print(f"\nTime taken: {elapsed_time:.2f} seconds")



if __name__ == "__main__":
    main()
