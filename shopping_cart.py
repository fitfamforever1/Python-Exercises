list = []
price = []
quantity = []
total = 0

while True:
    item = input("Enter the name of the item (or 'done' to finish): ")
    if item == 'done':
        for x in range(len(list)):
            print(f"- {list[x]}: ${price[x]:.2f} x {quantity[x]}")
            total += price[x] * quantity[x]
        print(f"Total cost: ${total:.2f}")
        break
    cost = float(input("Enter the price of the item: "))
    q = int(input("Enter the quantity of the item: "))
    list.append(item)
    price.append(cost)
    quantity.append(q)
