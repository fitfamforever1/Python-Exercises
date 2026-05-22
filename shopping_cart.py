# Shopping Cart

# Variable to store the shopping list
list = []

# Loop to continuously ask the user for items until they type 'done'
while True:
    item = input("Enter an item name to add it to shopping list. (Type 'done' to finish): ")
    if item == "done":
        for item in list:
            print(f"- {item}")
        break
    elif item in list:
        print(f"{item} is already in the shopping list.")
    else:
        list.append(item)
        print(f"{item} has been added to the shopping list.")
