# Compound Interest Calculator

# Variables
p = 0
i = 0
n = 0
t = 0
m = 0

# Input validation
while p <= 0:
    p = float(input("Enter the principal amount: "))
    if p <= 0:
        p = float(input("Enter the principal amount: "))

while i <= 0:
    i = float(input("Enter the interest rate: "))
    if i <= 0:
        i = float(input("Enter the interest rate: "))

while n <= 0:
    n = int(input("Enter the number of times interest is compounded per year: "))
    if n <= 0:
        n = int(input("Enter the number of times interest is compounded per year: "))

while t <= 0:
    t = int(input("Enter the number of years: "))
    if t <= 0:
        t = int(input("Enter the number of years: "))

while m <= 0:
    m = int(input("Enter the monthly contribution: "))
    if m <= 0:
        m = int(input("Enter the monthly contribution: "))

# Calculate the amount
if p > 0 and i > 0 and n > 0 and t > 0:

    # Convert the interest rate to a decimal and the time to years
    i = i / 100
    m = m * 12 

    # Calculate the amount using the compound interest formula
    
    a = p * (1 + i / n) ** (n * t) + m * ((1 + i / n) ** (n * t) - 1) / (i / n)
    print(f"Amount after {t} years: ${a:.2f}")