from add_to_json import add_to_json
from add_user import add_user , username_pin
import os
from login import find_user, loggedIn
from pay import payment_money

def main():
    options = ["Create account", "Login", "Edit account", "Delete account"]
    logged_in_options = ["Pay", "Send"] 
    
    print("-------------- Welcome to Majozi's Bank System --------------")
    print()
    print("You have options to choose from")
    print()
    while True:
        try:
            print("Just select any option from 1-4")
            for count, option in enumerate(options, start=1):
                print(f"{count}) {option}")

            user = int(input("Your option: "))
            if user == 1:
                user_info = add_user()
                user_pin = username_pin(user_info)
                add_to_json(user_pin)
                break
            elif user == 2:
                user_account = find_user()
                # os.system('cls' or 'clear')
                if user_account != None:
                    loggedIn(user_account)
                    while True:
                        try:
                            print("Just select any option from 1-2")
                            for i in range(len(logged_in_options)):
                                print(f"{i+1} {logged_in_options[i]}")

                            user_option = int(input("Your option: "))
                            if user_option == 1:
                                payment_money(user_account)
                                break
                        except ValueError:
                            os.system("cls" or "clear")
                            break
        except ValueError:
            print("Please provide a digit and 1-4")

        
if __name__ == "__main__":
    main()