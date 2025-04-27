import random
import string
import json
import os

# File to save passwords
PASSWORD_FILE = "passwords.json"

# Load existing passwords
if os.path.exists(PASSWORD_FILE):
    with open(PASSWORD_FILE, "r") as f:
        password_data = json.load(f)
else:
    password_data = {}

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password):
    if password in password_data:
        password_data[password] += 1
    else:
        password_data[password] = 1
    with open(PASSWORD_FILE, "w") as f:
        json.dump(password_data, f, indent=4)

def suggest_better_password():
    return generate_password(length=20)

def main():
    password = generate_password()
    print(f"Generated Password: {password}")

    if password in password_data:
        print(f"⚠️ This password has been generated {password_data[password]} times before.")
        print(f"🔄 Suggesting a stronger password: {suggest_better_password()}")
    else:
        print("✅ This is a unique password!")

    save_password(password)

if __name__ == "__main__":
    main()
