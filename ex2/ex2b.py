# FILE : ex2b.py
# WRITER : Yochay Ettun , yochze,  201517018
# EXERCISE : intro2cs ex2 2014-2015
# DESCRIPTION:
#
# #############################################################

# try: 
x = int(input("num1:"))
y = int(input("num2:"))
# except ValueError:
#   print("exception")
#   quit()

operation = input("operation:")

# Condition to make the program behave differently for every 
# mathematical operation
if operation == "+":
    # Addition
    result = x + y

elif operation == "-":
    # Difference
     result = x - y

elif operation == "*":
    # Multiplication
    result = x * y

elif operation == "/":
    # Division
    if y == 0:
        # If num2 is 0 then the program quits (no division by 0)
        print("Can't divide by 0")
        quit()
    else:
        result = x // y

elif operation == "%":
    # Modulo
    if y == 0:
        # If num2 is 0 then the program quits (no division by 0)
        print("Can't divide by 0")
        quit()
    else:
        result = x % y

else:
    # Handles unknown operators by printing alert to user and quitting program
    print("Unknown operator")
    quit()

# Print result
print(result)
