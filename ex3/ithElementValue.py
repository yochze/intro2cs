#############################################################                   
# FILE : ithElementValue.py                                                            
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex3 2014-2015                                             
# DESCRIPTION:                                                                  
# An implementation of Fibbonaci sequence calculation for any 
# input. 
# The program gets an integer from user which will be orc_number, 
# it then computes how many arrows are needed for Legolas to kill
# all those orcs.
# #############################################################  

# Receiving an integer from the end-user: 
orc_number = int(input("Which Orc do you wish to confront?"))

# Setting initial values:
# The program will start from 2 because for the first 2 orcs we know
# that a total of 2 arrows required to kill them.
n    = 2 
# previous and pre_previous are set to 1 (1 arrow for each previous orc).
# curr is resetted for use inside the iteration.
previous,pre_previous= 1,1
curr = 0

while n < orc_number: 
    # The loop goes from n until orc_number
    # n is being incremented in every step of the iteration.
    curr = pre_previous + previous # The current orc arrows count.
    pre_previous = previous        # Swaping previous to pre_previous
    previous = curr                # Swaping previous to curr
    n += 1                         # Incrementing n to reach orc_number 

# printing the result
print("The requred number of arrows is " + str(previous))
