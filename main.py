
def deposit():
    while True: # Loop runs until valid number is provided
        amount = input("What would you like to deposit? £ ")
        if amount.isdigit():    # Check inputted amount is a number
            amount = int(amount)    # Convert amount from string to integer
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0!")
        else:
            print("Please enter a number.")
    
    return amount

def main():
    balance = deposit()

main()