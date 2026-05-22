# Temperature converter | Celsius - Fahrenheit and Fahrenheit - Celsius

# Variables
unit = input("Enter unit to be converted to (C / F): ")
temperature = float(input("Enter the temperature: "))

# Calculation
if unit == "F":
    temperature = round(temperature * 9/5 + 32)
    print(f"The temperature is {temperature} F")
elif unit == "C":
    temperature = round((temperature - 32) * 5/9, 1)
    print(f"The temperature is {temperature} C")

# Error
else:
    print("Invalid unit")
