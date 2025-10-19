import sys
from plyer import notification
import time

# Here its when user logged and need to buy something
def pay(amount: int, data: dict):
    if amount > data["amount"]:
        return None
    else:
        data["amount"] -= amount

        print("Loading", end="")
        start_time = time.time()
        while time.time() - start_time < 5:
                print(".", end="")
                sys.stdout.flush()
                time.sleep(0.5)
        print("\nPaid 🚀 🚀")
        while True:
            notification.notify(
                title = "ALERT!!!!",
                message = f"{data["name"]} Paid {amount}.",
                timeout = 10
            )
            time.sleep(3) 
            break
    
def payment_money(data):
    while True:
        try:
            amount = int(input("Enter your Amount? ")) 
        except ValueError:
            print("Please provide only digits!!!!!!!!")
            continue
        else:
            paid = pay(amount, data)
            print(paid)

