import random

MAX_LINES = 3   # constant value - caps letters std Python convention
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]    #[:] makes a copy of the list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end= " | ")
            else:
                print(column[row], end="")

        print()

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
    
    while True:
        bet = get_bet()
        total_bet = lines * bet # Valiable to calculate total bet.
    
        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is £{balance}")
        else:
            break

    print(f"You are betting £{bet} on {lines} lines. Total bet is equal to £{total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won £{winnings}.")
    print(f"You won on lines:", *winning_lines)

main()