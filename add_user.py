import json

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
        
