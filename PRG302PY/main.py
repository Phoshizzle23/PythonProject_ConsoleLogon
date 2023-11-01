import os
import random
import string
import time


#########################
# Name: Matthew Woodward
# Student ID: 881145384
# Subject: PRG302 - Project 1
#########################
# The goal of this project is to provide a simple user login program.
# The following is a breakdown of the code:
# In this Python program we have the following fuctions: generate_password(), register_user(), view_users() & login().
# The generate_password() function will generate a new password based on the users options selected.
# The register_user() function prompts the user to input their user name and password and writes that information to a text file named "accounts.txt" using a with statement.
# The view_users() function reads the "account.txt" file and displays its contents to the console.
# The login() function reads the "account.txt" file to check if the entered name and password match any of the registered users.
# If a match is found, the function prints "Login successful." Then displays the contents of "Welcome.txt". If no match is found, the function prints "Invalid name or password."
# A while loop is used to present the user with a menu of options: register a new user, user login, view registered users, or quit the application.
# The user's choice is obtained using the input() function and the appropriate function is called based on the choice.
# To ensure that the view_users() function is only called when the "users.txt" file exists, the os.path.isfile() function is used to check its existence before reading from it.
# If the file does not exist, a message is printed to inform the user that no users have been registered yet.
# The login() function reads the "account.txt" file to check if the entered name and password match any of the registered users.
# If a match is found, the function prints "Login successful." and displays the contents of "Welcome.txt". If no match is found, the function prints "Invalid name or password."


def generate_password(length=10):
    # Provides options for the user to select from to build their password
    while True:
        characters = string.ascii_letters + string.digits + string.punctuation
        use_letters = input("Include letters (y/n): ").lower() == "y"
        use_numbers = input("Include numbers (y/n): ").lower() == "y"
        use_symbols = input("Include symbols (y/n): ").lower() == "y"

        if use_letters or use_numbers or use_symbols:
            # At least one character type is selected, break out of the loop
            break
        else:
            print("You must select at least one character type.")

    while True:
        length = int(input("Enter the password length (8-12): "))
        if 8 <= length <= 12:
            # The length is within the valid range, break out of the loop
            break
        else:
            print("Invalid password length. It must be between 8 and 12 characters.")

    # Once valid choices for character types and a valid password length are provided,
    # the following line generates a random password
    password = "".join(random.choice(characters) for _ in range(length))
    return password


def register_user():
    # Prompt user for user name and password or generate password
    print("User Registration")
    name = input("Enter your user name: ")
    choice_pass = input("Do you want to generate a random password? (Y/N): ").lower()
    if choice_pass == "y" or choice_pass == "":
        password = generate_password()
        print("Your password is:", password)
    else:
        password = input("Enter your password: ")
    # Write user data to "account.txt" file using "with" statement
    with open("accounts.txt", "a") as file:
        file.write(f"{name}, {password}\n")
    # Print success message
    print("User registered successfully.")


def login():
    # Prompt user for name and password
    print("User Login")
    name = input("Enter your user name: ")
    password = input("Enter your password: ")

    # Open "account.txt" file and search for matching user data
    with open("accounts.txt", "r") as file:
        for line in file:
            user_data = line.strip().split(", ")
            # If a match is found - print success message and display welcome message from "Welcome.txt" file
            if user_data[0] == name and user_data[1] == password:
                print("Login successful.")
                with open("Welcome.txt", "r") as welcome_file:
                    contents = welcome_file.read()
                    print(contents)
                return
    # If no match is found - print error message
    print("Invalid user name or password.")


def view_users():
    # Check if "account.txt" file exists using os.path.isfile() function
    if os.path.isfile("accounts.txt"):
        # If file exists - open it and print each line
        with open("accounts.txt", "r") as file:
            for line in file:
                print(line.strip())
    else:
        # If file does not exist - print error message
        print("No users registered yet.")


while True: # Display menu options
    print("Welcome to the User Registration App!")
    print("A. Register a new user")
    print("B. Login")
    print("C. View registered users")
    print("D. Quit")

    # Read user choice from input
    choice = input("Enter your choice (A/B/C/D): ").lower()
    # Call appropriate function based on user choice
    if choice == "a":
        register_user()
    elif choice == "b":
        login()
    elif choice == "c":
        view_users()
    elif choice == "d":
        print("Exiting...")
        # delay for 2 seconds before exiting
        time.sleep(2)
        break
    else:
        # If choice is invalid - print error message and loop again
        print("Invalid choice. Please try again.")
