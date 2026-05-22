# Weight converter | kg - lb and lb - kg

# Variables
unit = input("Enter unit to be converted to (kg / lb): ")
weight = float(input("Enter the weight: "))

# Calculation
if unit == "kg":
    weight = round(weight * 0.453592, 1)
    print(f"You weight is {weight} kg")
elif unit == "lb":
    weight = round(weight / 0.453592, 1)
    print(f"You weight is {weight} lb")

# Error
else:
    print("Invalid unit")
