import json
from rules import rules
# Here I will be adding users 
# now I have to add numbers and email -> valid ones
def add_user()-> dict:
    while True:
        try:
            surname = input("Your Surname?: ").title()
            name = input("Your Name?: ").title()
            id_num = int(input("Your South African ID number?: "))
            if len(surname) < 3 or len(name) < 3:
                print("Surname or Name, Cannot be empty or less than 3 words. Try again !!!!!")
                print() 
                continue
            if len(str(id_num)) < 12 or len(str(id_num)) > 13:
                print("ID cannot be less than 13, or greater than 13 Please try again")
                print()
                continue
        except ValueError:
            print("Please Enter valid Information. Try again")
            print()
        else:
            return {"name" :name,
            "surname": surname,
            "id": id_num,
            "amount": -50}
        

# Now my plan is to prompt for their pin and user name or passcode 

def username_pin(data: dict) -> dict:
    print()
    print("Lets create Pin for account to be secured")
    print("Remember your pin please!!!!!!!!!")
    while True:
        user_rules = input("First click (rules) to show rules I recommend or Click enter if want to continue: ").lower().strip()
        if user_rules == "":
            break
        elif user_rules == "rules":
            print()
            rules()
    while True:
        print()
        try:
            user_pin = input("Create Your pin: ")
            if len(user_pin) < 4 or len(user_pin) > 4:
                print("Your pin should be 4 digits ONLY!!!!!!!! ")
                continue
            if user_pin.count(user_pin[0]) > 2 or user_pin.count(user_pin[1]) > 2:
                print(f"You repeated a digit more than twice which is not allowed !!!!!")
                continue


        except ValueError:
            print("Your pin should be digits only pay attention please!!!!")
            continue
        else:
            print("--------------------IMPORTANT--------------------------")
            print("Remember username is your ID")
            data["pin"] = user_pin
            return data
# my_info = add_user()
# print(username_pin(my_info))