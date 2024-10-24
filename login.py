
# ========================================================
# INFORMATION
# Code by Leah Zheng 
# @RatWithJacket on GitHub (ratwithjacket@gmail.com)
# Created on 2024-10-24
# ========================================================

# Required libraries
import sys 
import time 


print("╔══════════╗")
print("  WELCOME!  ")
print("╚══════════╝")

print("1 | LOGIN")
print("2 | CREATE ACCOUNT")
print("3 | VIEW ACCOUNTS")
print("4 | EXIT")

# Placeholder names for username and password
loginUsername = ""
login_password = ""

i = input("\nPick an option: [1/2/3/4]")

# ==============
# LOGIN SYSTEM
# ==============
if i == "1":
    print("\n┌──────┐")
    print(" LOGIN ")
    print("└──────┘")
    login_username = input("\nEnter username: ") 
    login_password = input("Enter password: ")

    accounts = {} 

    # Opens db and chucks info into key value pairs
    with open("accounts.txt", "r") as db:
        for line in db:
            db_user, db_password = line.strip().split(',', 1) # Remove any whitespace and splits line into two parts at first comma
            accounts[db_user] = db_password # Creates new item with user and password as key value pairs
        
    # Login validation 
    if login_username in accounts:
        if accounts[login_username] == login_password: # Pass user submitted username into array to check if they match
            print("\nSuccessful Login!")
            time.sleep(1)
            sys.exit()
        else:
            print("\nIncorrect password.")
    else:
        print("\nCredentials not found. Please double check or register.")
else:
    print("\nPlease select a valid option.")

# ==============
# ACCOUNT CREATION
# ==============

if i == "2":
    print("\n┌──────────────────┐")
    print(" CREATE NEW ACCOUNT ")
    print("└──────────────────┘")
    new_username = input("Enter username: ") 

    preexisting_usernames = [] # New array to store preexisting usernames

    # Opens the db file and puts all the usernames into its own array
    with open("accounts.txt", 'r') as db:
        for line in db:
            db_user, db_password = line.strip().split(',', 1)
            preexisting_usernames.append(db_user) # Add only the username to the array, we don't need the password
        # print(preexisting_usernames) # Sanity check
    
    # Check if username already exists otherwise allow user to create a new one
    if new_username in preexisting_usernames:
        print("Username already taken..!")
    else:
        print("PASSWORD CREATION MENU")
        print("1 | CREATE YOUR OWN PASSWORD")
        print("2 | RANDOMLY GENERATE PASSWORD")
        password_gen_option = input("\nPick an option: [1/2]")
        if password_gen_option == "1":

# Okay look gelos I love you guys but your preexisting sample code SUCKS, i want it to run the function repeatedly if the user messes up their input so they dont have to start from scratch.
        
        
