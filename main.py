from add_to_json import add_to_json
from add_user import add_user , username_pin

def main():
    user_info = add_user()
    user_pin = username_pin(user_info)
    add_to_json(user_pin)

if __name__ == "__main__":
    main()