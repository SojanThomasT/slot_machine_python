import random

# Constants for the game
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Slot machine setup
ROWS = 3
COLS = 3

# Symbol count and values for the game
symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}
symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}

# Function to check for winning lines
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    
    for line in range(lines):
        symbols_in_line = set(column[line] for column in columns)
        if len(symbols_in_line) == 1:
            symbol = symbols_in_line.pop()
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# Function to get a random slot machine spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        all_symbols.extend([symbol] * symbol_count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

# Function to print the slot machine output
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

# Function to deposit money into the game
def deposit():
    while True:
        amount = input("What would you like to deposit? ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

# Function to get the number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

# Function to get the bet amount
def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line? ₹")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ₹{MIN_BET} - ₹{MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

# Function to handle a spin of the slot machine
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ₹{balance}")
        else:
            break
      
    print(f"You are betting ₹{bet} on {lines} lines. The total bet is equal to: ₹{total_bet}")
    slot = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slot)
    winnings, winning_lines = check_winnings(slot, lines, bet, symbol_value)
    print(f"You won ₹{winnings}")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

# Main game loop
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ₹{balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

# Start the game by calling the deposit function
main()
