#############################################################                   
# FILE : totalWeight.py                                                            
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex3 2014-2015                                             
# DESCRIPTION:                                                                  
# #############################################################     

total_weight = 0

while True:
    weight = int(input("Insert weights one by one:"))
    if weight == -1:
        print("Total pack is " + str(total_weight))
        break
    elif weight < 0:
        print("Error smaller than 0")
        break
    elif (total_weight + weight) > 100:
        print("Overweight! Gandalf will not approve")
        break
    else:
        total_weight += weight
