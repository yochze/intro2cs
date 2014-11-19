#############################################################                   
# FILE : totalWeight.py                                                            
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex3 2014-2015                                             
# DESCRIPTION:                                                                  
# Calculating pack weight of Sam and Frodo. Running a loop that 
# asks input from user. If one of the restriction (overweight etc) 
# is violated then the program acts accordingly (alert, end program).
# The loop runs until the ring's weight is entered as input
# #############################################################     

RING_WEIGHT  = -1
MAX_WEIGHT   = 100
total_weight = 0

while True:
    # Iterating while input from user is valid and while 
    # user has not entered the break trigger (the ring).

    # Receiving weight 
    weight = int(input("Insert weights one by one:"))
    if weight == RING_WEIGHT:
        # Ring weight (-1) make the program stop the iteration
        # of receiving input from user, and print the total
        # packed weight.

        print("The total packed weight is " + str(total_weight))
        break

    elif weight < 0:
        # Weight input cannot be negative, if it is - print warning
        # to user, and continue with iteration (next input)

        print("Weights must be non-negative")
        next

    elif (total_weight + weight) > MAX_WEIGHT:
        # If total weight and the last weight input from user
        # has passed max weight (100), print a warning
        # and end the program.

        print("Overweight! Gandalf will not approve")
        break

    else:
        # If everything is OK, increment total weight with the user 
        # new weight input.
        total_weight += weight
