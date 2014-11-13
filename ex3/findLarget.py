#############################################################                   
# FILE : findLargest.py                                                                
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex3 2014-2015                                             
# DESCRIPTION:                                                                  
#
# #############################################################     



riders_count = int(input("Enter number of riders:"))

largest_hat = [0,0]

for rider in range(0,riders_count):
    hat_size = int(input("How tall is the hat?"))
    if hat_size > largest_hat[1]:
        largest_hat[1] = hat_size
        largest_hat[0] = rider


print("Gandalf's position is: " + str(largest_hat[0]+1))
