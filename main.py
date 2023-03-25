MAX_LINES = 3   # constant value - caps letters std Python convention
MAX_BET = 100
MIN_BET = 1

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

def get_number_of_lines():
    while True: # Loop runs until valid number is provided
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():    # Check inputted amount is a number
            lines = int(lines)    # Convert amount from string to integer
            if 1 <= lines <= MAX_LINES: # Check no. lines within range
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    
    return lines

def get_bet():
    while True: # Loop runs until valid number is provided
        amount = input("What would you like to bet on each line? £ ")
        if amount.isdigit():    # Check inputted amount is a number
            amount = int(amount)    # Convert amount from string to integer
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between £{MIN_BET} - £{MAX_BET}.")   #f string only possible in Python 3.
        else:
            print("Please enter a number.")
    
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = lines * bet # Valiable to calculate total bet.
    print(f"You are betting £{bet} on {lines} lines. Total bet is equal to £{total_bet}")

main()