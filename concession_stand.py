# Concession stand program

menu = {
    "hot dog": 2.50,
    "hamburger": 3.00,
    "fries": 1.50,
    "soda": 1.00,
    "candy": 0.75}

cart = []
total = 0.00

print("\nMenu:")
for item, price in menu.items():
    print(f"{item}: ${price:.2f}")

while True:
    item = input("Enter an item to purchase (or 'done' to finish): ").lower()
    if item == "done":
        break
    elif item in menu:
        cart.append(item)
        total = total + menu.get(item, 0)
        print(f"Added {item} to cart. Current total: ${total:.2f}")
    else:
        print("Item not found. Please try again.")

print(f"Final total: ${total:.2f}")
