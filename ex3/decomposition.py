#############################################################                   
# FILE : decomposition.py                                                            
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex3 2014-2015                                             
# DESCRIPTION:          
# Getting a positive integer from user, where each digit in the number
# represent a different quantity of goblets drank by gimli at a 
# single day. Each digit's position represent the day of drinking that
# quantity.
# In the first loop the program seperates the input number to digits
# stored in list. 
# The second loop, iterates through the genereated list and prints
# the number of goblets drank during each day.
# #############################################################  

# Setting variables
n      = 1  # The 
digits = [] # List to represent the digits


composed_number = int(input("Insert composed number:"))
while composed_number >= n and (composed_number != composed_number % n):
    # If n's number of digits has passed
    # the composed_number input number of digit
    # then calculation is over, and end program.
    
    # append the new digit to the list of digits,
    # the new digit is the input, divided by the current
    # n (which is 10^steps) modulo 10 to get the units.
    digits.append( composed_number // n % 10 )
    n*=10 # Incrementing n by 10 times.


# Printing results:
idx = 1 # Setting the index (also days) to 1.

# Iterating through the list enerated from the previous loop.
# Each cell in the list contains a digit representing number of goblets.
for digit in digits:
    print("The number of goblets Gimli drank on day " + 
            str(idx) + " was " + str(digit)) # Printing.
    idx += 1 # Next day.
