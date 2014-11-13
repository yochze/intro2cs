#############################################################                   
# FILE : ithElementValue.py                                                            
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex3 2014-2015                                             
# DESCRIPTION:                                                                  
# #############################################################  


orc_number = int(input("Which Orc do you wish to confront?"))

# [ 1,
#   1,
#   2,
#   3,
#   5,
#   8,
#   13 ]

n = 2
curr = 0
previous,pre_previous= 1,1

while n < orc_number:
    curr = pre_previous + previous
    pre_previous = previous
    previous = curr
    n += 1

print("The requred number of arrows is " + str(previous))
