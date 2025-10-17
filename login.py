import json
import os

# User login

def find_user():
    os.system('cls' or 'clear')
    print("----------------------------   Login 🚀🚀  ----------------------------")
    print()
    with open("data.json") as file:
        data = json.load(file)
    count = 4
    while count > 0:
        try:
            print(f"You have {count} chances to get it correct!!!")
            id = int(input("Your ID number?: "))
            pin = int(input("Your pin: "))
            for i in data["users_details"]:
                if i["id"] == id and i["pin"] == pin:
                    return i
            
        except ValueError:
            print("Please your options should a number!!!!!!")
            count -= 1
            continue
        except KeyError:
            print("Please Make sure that Pin and ID are correct")
            count -= 1
            continue
        

# print(find_user())