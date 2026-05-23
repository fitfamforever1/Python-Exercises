# Bank Program

# Function for actions
def show_balance():
    print(f"Your current balance is: ${balance:.2f}")

def deposit(amount):
    global balance
    balance += amount
    print(f"You have deposited: ${amount:.2f}")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds. Withdrawal failed.")
    else:
        balance -= amount
        print(f"You have withdrawn: ${amount:.2f}")

# Main function
def main():
    print("Welcome to the Bank!")
    while True:
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Please choose an option: ")
        
        match choice:
            case "1":
                show_balance()
            case "2":
                amount = float(input("Enter amount to deposit: "))
                deposit(amount)
            case "3":
                amount = float(input("Enter amount to withdraw: "))
                withdraw(amount)
            case "4":
                print("Thank you for using the Bank. Goodbye!")
                break
            case _:
                print("Invalid option. Please try again.")

# Variable
balance = 0

# Run the main function
if __name__ == "__main__":
    main()
