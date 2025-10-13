from add_to_json import add_to_json
from add_user import add_user , username_pin
import os


def main():
    options = ["Create account", "Login", "Edit account", "Delete account"]
    
    print("-------------- Welcome to Majozi's Bank System --------------")
    print()
    print("We have options to choose from")
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

        except ValueError:
            print("Please provide a digit and 1-4")

        
if __name__ == "__main__":
    main()