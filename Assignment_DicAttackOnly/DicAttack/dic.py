import hashlib
import os
import time

USERDATA_FILE = os.path.join("..", "App/user", "userdata.txt")
DICTIONARY_FILE = os.path.join("rockyou.txt")

# Function to hash the password with SHA-256
def hash_with_sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()

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

# Function to perform dictionary attack with timing for each password
# Function to perform dictionary attack and measure time to crack each password
def dictionary_attack_with_timing(userdata_file, dictionary_file):
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
        print(f"\nCracking password for user: {username}")
        user_start_time = time.perf_counter()   # Start timer for cracking this user's password
        found_password = None

        for word in dictionary:
            if hash_with_sha256(word) == hashed_password:
                found_password = word
                break

        user_end_time = time.perf_counter()   # Stop timer after finding the password
        elapsed_time = user_end_time - user_start_time

        if found_password:
            print(f"Password found: '{found_password}' for user '{username}'. Time taken: {elapsed_time:.30f} seconds")
            cracked_passwords[username] = found_password
        else:
            print(f"Password for user '{username}' not found in the dictionary. Time taken: {elapsed_time:.30f} seconds")
            cracked_passwords[username] = ""

    return cracked_passwords

# Main function for dictionary attack
def main():
    start_time = time.time()  # Record start time

    print("Starting Dictionary Attack...")
    print("Hashing only")
    cracked = dictionary_attack_with_timing(USERDATA_FILE, DICTIONARY_FILE)

    end_time = time.time()  # Record end time
    elapsed_time = end_time - start_time  # Calculate total elapsed time

    if cracked:
        print("\nCracked Passwords:")
        for username, password in cracked.items():
            print(f"Username: '{username}', Password: '{password}'")
    else:
        print("No passwords were cracked or files are missing.")

    # Display total execution time
    print(f"\nTotal time taken: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
