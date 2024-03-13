# Programmer: Ethan VanLandegent
# Date: 3.12.2024
# Program: Password Generator
# Resource: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA

import hashlib
import getpass

def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

def main():
    password = getpass.getpass("Enter your password: ")
    salt = "RandomSalt123"  # Replace with your own salt generation method
    hashed_password = hash_password(password, salt)
    print("Hashed Password:", hashed_password)

if __name__ == "__main__":
    main()
