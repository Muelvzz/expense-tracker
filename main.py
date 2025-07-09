import pandas as pd
from datetime import datetime

file = "data.csv"
time = datetime.now().strftime("%Y-%m-%d")

print("EXPENSE TRACKER")

while True:
    try:
        user_entry = input("Enter the expenses: ")
        entry_list = list(user_entry.split(" "))
        description = entry_list[0].capitalize()
        amount = int(entry_list[1])

        with open(file, "a", newline="") as file:
            file.write(f"{description};{amount};{time}\n")

    except TypeError:
        print("Sorry, the format should be [description] [amount]")
    
    break