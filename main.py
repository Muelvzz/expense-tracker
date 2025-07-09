import pandas as pd
from datetime import datetime

file = "data.csv"
df = pd.read_csv(file, sep=";")
time = datetime.now().strftime("%Y-%m-%d")

print("EXPENSE TRACKER")

while True:
    try:

        user_action = input("Type add, show, edit, delete or exit: ")

        if user_action.startswith("add"):

            user_entry = input("Enter the expenses: ")
            entry_list = list(user_entry.split(" "))
            description = entry_list[0].capitalize()
            amount = int(entry_list[1])

            with open(file, "a", newline="") as f:
                f.write(f"{description};{amount};{time}\n")

        elif user_action.startswith("show"):
            df.index += 1
            print(df)

        elif user_action.startswith("edit"):

            with open(file, "r") as f:

                df.index += 1

                print(df)
                print(" ")
                try:
                    user_edit = int(input("Enter the number to edit: "))

                    if user_edit in df.index:
                        new_entry = input("Enter the new value using this format [desctription] [amount]: ")
                        new_entry_list = list(new_entry.split(" "))

                        new_description = new_entry_list[0].capitalize()
                        new_amount = int(new_entry_list[1])

                        df.at[user_edit, 'description'] = new_description
                        df.at[user_edit, 'amount'] = new_amount
                        df.at[user_edit, 'date'] = time

                        df.to_csv("data.csv", sep=";", index=False)

                        print("successfully updated")

                    else:
                        print("The number is out of the index")
                    
                except (ValueError, IndexError):
                    print("Invalid input")


        elif user_action.startswith("exit"):
            break

        else:
            print("please enter add, show, edit or exit")

    except TypeError:
        print("Sorry, the format should be [description] [amount]")