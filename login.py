
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
print("\nPlease select an option.")
print("1 | LOGIN")
print("2 | CREATE ACCOUNT")
print("3 | VIEW ACCOUNTS")
print("4 | EXIT")

# Placeholder names for username and password
loginUsername = ""
loginPassword = ""

i = input("\nPick an option: [1/2/3/4]")

# ==============
# LOGIN SYSTEM
# ==============
if i == "1":
    print("\n┌──────┐")
    print(" LOGIN: ")
    print("└──────┘")
    loginUsername = input("\nEnter username: ") 
    loginPassword = input("Enter password: ")

    # PARSING ACCOUNTS.TXT
    accounts = {} # New dictionary where all the database information will be stored
    # With statement ensures proper opening and release of resources. 
    with open("accounts.txt", "r") as db:
        for line in db:
            db_user, db_password = line.strip().split(',', 1) # Remove any whitespace and splits line into two parts at first comma
            accounts[db_user] = db_password # Creates new item with user and password as key value pairs
        
    # LOGIN VALIDATION
    if loginUsername in accounts:
        if accounts[loginUsername] == loginPassword: # Pass user submitted username into array to check if they match
            print("\nSuccessful Login!")
            time.sleep(1)
            sys.exit()
        else:
            print("\nIncorrect password.")
    else:
        print("\nCredentials not found. Please double check or register.")
else:
    print("\nPlease select a valid option.")
