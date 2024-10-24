
# ========================================================
# INFORMATION
# Code by Leah Zheng 
# @RatWithJacket on GitHub (ratwithjacket@gmail.com)
# Created on 2024-10-24
# This project is a simple account management system that allows users to login, create an account, view the account, and exit the system using a text based UI. 
# Made for educational purposes only for ICTPRG302. 
# ========================================================

"""
TODO
- Add proper exit system
- Add basic input validation / sanitisation..?
- Finish adding colors to everything
- Utilise sleep function so it seems a bit more responsive and cool and stuff.
"""

# Required libraries
import sys 
import time 
import secrets
import string
import os
os.system("color") # For colors in the terminal! :)

# ANSI escape codes for cyan text and background
colors = {
    'RESET': '\033[0m',       
    'RED': '\033[31m',
    'GREEN': '\033[32m',
    'YELLOW': '\033[33m',
    'BLUE': '\033[34m',
    'PINK': '\033[35m',
    'CYAN': '\033[36m',
    'WHITE': '\033[37m'
}

# Database connection function
def open_db():
    accounts = {} 
    # Opens db and chucks info into key value pairs
    with open("accounts.txt", "r") as db:
        for line in db:
            db_user, db_password = line.strip().split(',', 1) # Remove any whitespace and splits line into two parts at first comma
            accounts[db_user] = db_password # Creates new item with user and password as key value pairs
    return accounts

def display_welcome_ui():
    print("\n\n")
    print("╔═════════════════════════════════════╗")
    print("  ┬ ┬┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ┬ ┬┌─┐┌┬┐┌─┐ ")
    print("  │││├┤ │  │  │ ││││├┤   ├─┤│ ││││├┤  ")
    print("  └┴┘└─┘┴─┘└─┘└─┘┴ ┴└─┘  ┴ ┴└─┘┴ ┴└─┘ ")
    print("╚═════════════════════════════════════╝")

def colorise(text, color):
    return f"{colors[color]}{text}{colors['RESET']}"

# Displays home menu stuff
def display_home_menu():
    print("\n┌───────────────┐")
    print("    MAIN MENU    ")
    print("└───────────────┘")
    print("1 | LOGIN")
    print("2 | CREATE ACCOUNT")
    print("3 | VIEW ACCOUNTS")
    print("4 | EXIT")
    i = input(colorise("\nPick an option [1/2/3/4] : ", "PINK"))
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

    print("\nLOGIN ")
    print("───────────────────────────────────────────────")
    login_username = input(colorise("Enter username: ", "PINK"))
    login_password = input(colorise("Enter password: ", "PINK"))

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
    print("\nCREATE NEW ACCOUNT ")
    print("───────────────────────────────────────────────")
    new_username = input(colorise("Enter username: ", "PINK"))

    accounts = open_db()
    
    # Check if username already exists otherwise allow user to create a new one
    if new_username in accounts:
        print("Username already taken..!")
        create_account()
    else:
        print("\n┌───────────────────────┐")
        print(" PASSWORD CREATION MENU")
        print("└───────────────────────┘")
        print("1 | CREATE YOUR OWN PASSWORD")
        print("2 | RANDOMLY GENERATE PASSWORD")
        password_gen_option = input(colorise("\nPick an option [1/2] : ", "PINK"))
        if password_gen_option == "1":
            new_password = input(colorise("Enter a new password: ", "PINK"))
            new_line = new_username + "," + new_password
            with open("accounts.txt", "a") as db:
                db.write("\n" + new_line)
            print(colorise("New account created successfully. You can try login now.", "GREEN"))
        else:
            print("\nRANDOM PASSWORD GENERATOR")
            print("───────────────────────────────────────────────")
            use_numbers = input(colorise("Include numbers? (y/n): ", "PINK")).strip().lower() == 'y'
            use_symbols = input(colorise("Include symbols? (y/n): ", "PINK")).strip().lower() == 'y'
            try:
                length = int(input(colorise("Enter the desired password length (max 64): ", "PINK")))
                if length < 0:
                    print(colorise("Please enter a positive integer.", "RED"))
                elif length > 64:
                    print(colorise("Password too long, please specify a number below 64.", "RED"))
                else:
                    # For now it just declares variables with the default
                    characters = string.ascii_letters
                    # Then append associated customisation variables if they are true from the earlier input
                    if use_numbers:
                        characters += string.digits
                    if use_symbols:
                        characters += string.punctuation
                    new_random_password = ''.join(secrets.choice(characters) for _ in range(length))
                    print("Account created successfully! You can now log in.")
                    print("Here is your newly generated password: ")
                    print(f"{colors['CYAN']}{new_random_password}{colors['RESET']}")
                    print("Please write it down or store it somewhere safe.")
                    display_home_menu()
                    # TODO pls put this into its own function maybe it looks awful right now sobs
            except ValueError:
                print("Please enter a valid number.")
                
def view_account():
    print("\n┌───────────────────────┐")
    print("   FULL LIST OF USERS   ")
    print("└───────────────────────┘")
    accounts = open_db()
    for i, (user, password) in enumerate(accounts.items(), start=1):
        print(f"USER #{i}   |  {user} ")
        print(f"          |  {colors['CYAN']}{password}{colors['RESET']} ")
        print("───────────────────────────────────────────────")

def countdown_animation():
    for i in range(3, 0, -1):
        sys.stdout.write(f"\rTaking you back to the main menu in {i}...")
        sys.stdout.flush()
        time.sleep(1)  # Wait for 1 second

display_welcome_ui()
display_home_menu()

