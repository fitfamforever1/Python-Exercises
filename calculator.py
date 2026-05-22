# Calculator Program

# Variables
o = input("Enter the operator (+, -, *, /): ")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Calculation
if o == "+":
    print(round(a + b, 3))

elif o == "-":
    print(round(a - b, 3))
elif o == "*":
    print(round(a * b, 3))

elif o == "/":
    print(round(a / b, 3))

# Error
else:
    print("Invalid operator")