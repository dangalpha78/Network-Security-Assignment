import hashlib
import os
import time

# Path to your userdata.txt file
USER_DATA_FILE = "../App/user/userdata.txt"
print("Absolute Path:", os.path.abspath(USER_DATA_FILE))

# Path to your rockyou.txt file
ROCKYOU_FILE = "rockyou.txt"

def dictionary_attack():
    if not os.path.exists(USER_DATA_FILE):
        print("User data file not found.")
        return

    if not os.path.exists(ROCKYOU_FILE):
        print("Rockyou file not found.")
        return

    # Read stored user data
    with open(USER_DATA_FILE, "r") as file:
        user_data = [line.strip().split(":") for line in file if line.strip()]

    # Read the rockyou.txt wordlist
    with open(ROCKYOU_FILE, "r", encoding="latin-1") as wordlist:
        passwords = wordlist.read().splitlines()

    print("Starting dictionary attack...")
    start_time = time.time()  # Record the start time of the attack

    # Attempt to crack each user's password
    for username, stored_hash, salt in user_data:
        print(f"\nAttempting to crack password for user: {username}")
        user_start_time = time.time()  # Record start time for this user

        for password in passwords:
            # Combine the password with the salt and hash it
            test_hash = hashlib.sha256((password + salt).encode()).hexdigest()
            if test_hash == stored_hash:
                user_end_time = time.time()  # Record end time for this user
                print(f"Password found for {username}: {password}")
                print(f"Time taken for {username}: {user_end_time - user_start_time:.2f} seconds")
                break
        else:
            user_end_time = time.time()
            print(f"Password for {username} not found in the dictionary.")
            print(f"Time taken for {username}: {user_end_time - user_start_time:.2f} seconds")

    end_time = time.time()  # Record the end time of the attack
    print(f"\nTotal time taken: {end_time - start_time:.2f} seconds")

dictionary_attack()
