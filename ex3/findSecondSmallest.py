#############################################################                   
# FILE : findSecondSmallest.py                                                                
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex3 2014-2015                                             
# DESCRIPTION:                                                                  
#
# #############################################################     

# max, second_max, position_of_second max
dancers = [0,0,0]

for dancer in range(0,10):
    dancer_age = int(input("What is the age of the current dancer?"))
    if dancer_age > dancers[0]:
        dancers[1] = dancers[0] # Swap
        dancers[0] = dancer_age 

    elif (dancer_age < dancers[0]) and (dancer_age > dancers[1]):
        dancers[1] = dancer_age
        dancers[2] = dancer # Position

print("Pipin is dancer number " + str(dancers[2] + 1))
