#############################################################                   
# FILE : findSecondSmallest.py                                                                
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex3 2014-2015                                             
# DESCRIPTION:                                                                  
# Program that for each of 10 dancers, it asks the user for his
# age. At the end it prints the position of the 2nd youngest dancer.
# #############################################################     

# Setting variables, min_dancer is a list with two cells: [age, position]
# it contains the youngest dancer details. It is being updated through the
# iteration. The "smin_dancer" is a similar list, containing the second
# youngest dancer.
# uninitialized constant is to determine that no dancers are stored in the 
# list yet.

UNINITIALIZED = -1 # It is set to -1 which is out of bounds of program input
                   # but still comparible within the iteration.

min_dancer    = [UNINITIALIZED,0] # age, position
smin_dancer   = [UNINITIALIZED,0] # age, position


for dancer in range(1,11):
    # Iterating from 1 to 10 and asking user for current dacer age.
    dancer_age = int(input("What is the age of the current dancer?"))

    if (dancer_age < min_dancer[0]) or (min_dancer[0] == UNINITIALIZED):
        # If the new input dancer is younger than youngest (min_dancer)
        # then, store youngest in second youngest list and save the new 
        # dancer as the youngest.
        # Also, if min_dancer is still uninitialized then save input anyway.

        smin_dancer = min_dancer
        min_dancer  = [dancer_age, dancer]

    elif (min_dancer[0] < dancer_age and dancer_age < smin_dancer[0]) \
    or (smin_dancer[0] == UNINITIALIZED):
        # if bigger the min but smaller than second_min
        # If the new input dancer is older than youngest but younger than
        # second youngest, then store the new input in second youngest list.
        # If second youngest is not initialized yet, then store it anyway.

        smin_dancer = [dancer_age, dancer]
        
# Print the position of second youngest dancer, aka Pipin.
print("Pipin is dancer number " + str(smin_dancer[1]))
