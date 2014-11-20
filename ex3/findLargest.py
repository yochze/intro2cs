#############################################################                   
# FILE : findLargest.py                                                                
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex3 2014-2015                                             
# DESCRIPTION:                                                                  
# Program the retrieve number of riders from users and returns
# the position of the rider wearing the tallest hat and his hat 
# size. 
# #############################################################     

riders_count = int(input("Enter the number of riders:"))

largest_hat = [0,0] # In this list the program will save the location of 
                    # the rider with largest hat and the largest hat size.
                    # For example if Rider #2 has the largest 120 hat
                    # The list will be [2, 120]

for rider in range(0,riders_count):
    # Iterating through all riders from 0 to riders_count (based on user input)
    hat_size = int(input("How tall is the hat?")) # Asking for hat height.

    if hat_size > largest_hat[1]: 
        # Triggering condition: If it's bigger than the current
        # tallest hat, save rider and its hat. Otherwise - do nothing.
        largest_hat[1] = hat_size
        largest_hat[0] = rider

# Print result
print("Gandalf's position is: " + str(largest_hat[0]+1))
