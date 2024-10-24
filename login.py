
# ========================================================
# INFORMATION
# Code by Leah Zheng 
# @RatWithJacket on GitHub (ratwithjacket@gmail.com)
# Created on 2024-10-24
# ========================================================

# Required libraries
import sys 
import time 
import secrets
import string
import os
os.system("color") # For colors in the terminal! :)

# ANSI escape codes for cyan text and background
CYAN = "\033[36m"      # Text color cyan
RESET = "\033[0m"      # Reset to default

# Database connection function
def open_db():
    accounts = {} 
    # Opens db and chucks info into key value pairs
    with open("accounts.txt", "r") as db:
        for line in db:
            db_user, db_password = line.strip().split(',', 1) # Remove any whitespace and splits line into two parts at first comma
            accounts[db_user] = db_password # Creates new item with user and password as key value pairs
    return accounts

# Displays home menu stuff
def display_home_menu():
    print("╔══════════╗")
    print("  WELCOME!  ")
    print("╚══════════╝")

    print("1 | LOGIN")
    print("2 | CREATE ACCOUNT")
    print("3 | VIEW ACCOUNTS")
    print("4 | EXIT")
    i = input("\nPick an option [1/2/3/4] : ")
    # Essentially this switch case statement acts like a router 
    match i:
        case "1":
            user_login()
        case "2":
            create_account()
        case "3":
            view_account()
        case "4":
            login_exit()

def user_login():
    # init placeholder variables for username and password
    login_username = ""
    login_password = ""

    print("\n┌──────┐")
    print(" LOGIN ")
    print("└──────┘")
    login_username = input("\nEnter username: ") 
    login_password = input("Enter password: ")

    accounts = open_db()

    if login_username in accounts:
        if accounts[login_username] == login_password: # Pass user submitted username into array to check if they match
            print("\nSuccessful Login!")
            time.sleep(1)
            sys.exit()
        else:
            print("\nIncorrect password. Login failed.")
            display_home_menu()
    else:
        print("\nCredentials not found. Please double check or register.")
        display_home_menu()
# TODO maybe split the username and password thing into its own functions so they dont have to go back??? or add sleep function so it seems slightly more interactive or whatever

def create_account():
    print("\n┌──────────────────┐")
    print(" CREATE NEW ACCOUNT ")
    print("└──────────────────┘")
    new_username = input("Enter username: ") 

    accounts = open_db()
    
    # Check if username already exists otherwise allow user to create a new one
    if new_username in accounts:
        print("Username already taken..!")
        create_account()
    else:
        print("PASSWORD CREATION MENU")
        print("1 | CREATE YOUR OWN PASSWORD")
        print("2 | RANDOMLY GENERATE PASSWORD")
        password_gen_option = input("\nPick an option [1/2] : ")
        if password_gen_option == "1":
            new_password = input("\nEnter a new password: ")
            new_line = new_username + "," + new_password
            with open("accounts.txt", "a") as db:
                db.write("\n" + new_line)
                db.close()
            print("New account created successfully. You can try login now.")
        else:
            print("Would you like your new password to contain: ")
            use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
            use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
            try:
                length = int(input("Enter the desired password length (max 64): "))
                if length < 0:
                    print("Please enter a positive integer.")
                elif length > 64:
                    print("Password too long, please specify a number below 64.")
                else:
                    # TODO pls put this into its own function maybe it looks awful right now sobs
                    # For now it just declares variables with the default
                    characters = string.ascii_letters
                    # Then append associated customisation variables if they are true from the earlier input
                    if use_numbers:
                        characters += string.digits
                    if use_symbols:
                        characters += string.punctuation
                    new_random_password = ''.join(secrets.choice(characters) for _ in range(length))
                    print("Here is your newly generated password: ")
                    print(f"{CYAN}{new_random_password}{RESET}")
                    print("Please write it down or store it somewhere safe.")
            except ValueError:
                print("Please enter a valid number.")
                

display_home_menu()