# Programmer: Ethan VanLandegent
# Date: 3.12.2024
# Program: Password Generator
# Resource: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA

import hashlib
import getpass

def main():
    password = getpass.getpass("Enter your password: ")
    salt = "somerandomsalt"  # Change this to a random value
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    print("Hashed password:", hashed_password)

if __name__ == "__main__":
    main()
