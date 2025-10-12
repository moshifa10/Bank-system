import json
from add_to_json import add_to_json
from add_user import add_user

def main():
    user_info = add_user()
    add_to_json(user_info)

if __name__ == "__main__":
    main()