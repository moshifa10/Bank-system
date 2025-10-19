import json
import os
import time
from plyer import notification
import sys
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
                else:
                    count -= 1
        except ValueError:
            print("Please your options should be a number!!!!!!")
            count -= 1
            continue
        except KeyError:
            print("Please Make sure that Pin and ID are correct")
            count -= 1
            continue
    if count == 0:
        return None

def loggedIn(data: dict):
    print("Loading", end="")
    start_time = time.time()
    while time.time() - start_time < 5:
        print(".", end="")
        sys.stdout.flush()
        time.sleep(0.5)
    print(f"\n{data['name']} Logged In  🚀 🚀")
    while True:
        notification.notify(
            title = "ALERT!!!!",
            message = f"{data["name"]} Logged In.",
            timeout = 10
        )
        time.sleep(3) 
        break
    


        

# print(find_user())