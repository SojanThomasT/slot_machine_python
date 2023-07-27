MAX_LINES = 3
#defining code for deposit:
def deposit():
  while True:
@@ -12,4 +12,25 @@ def deposit():
    else:
      print("Please enter a number")
  return amount

def get_number_of_lines():
  while True:
    lines = input("Enter the number of lines to be on (1-" + str(MAX_LINES) +  ")? " )
    if lines.isdigit():
      lines = int(lines)
      if (1 <= lines <= MAX_LINES):
        break
      else:
        print("Enter a valid number of lines. ")
    else:
      print("Please enter a number")
  return lines

def main()
  balance = deposit()
  lines = get_number_of_lines()
  print(balance,lines)

#callinh function deposit
main()