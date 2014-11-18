#############################################################                   
# FILE : twoDimensionalSeek.py                                                            
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex3 2014-2015                                             
# DESCRIPTION:                                                                  
# #############################################################  
right, forward = 0, 0
right_or_left = "right"
forward_or_backward = "forward"

position = "A"

#      FORWARD 
# LEFT    +     RIGHT
#      BACKWARD
#   C

while True:
    direction = raw_input("Next turn:")
    if direction == "right":
        steps = int(input("steps: "))

        if position == "A":
            position = "B"
            right += steps

        elif position == "B":
            position = "C"
            forward -= steps

        elif position == "C":
            position = "D"
            right -= steps

        elif position == "D":
            position = "A"
            forward += steps
        
    elif direction == "left":
        steps = int(input("steps: "))

        if position == "A":
            position = "D"
            right -= steps

        elif position == "B":
            position = "A"
            forward += steps

        elif position == "C":
            position = "B"
            right += steps

        elif position == "D":
            position = "C"
            forward -= steps
        

    elif direction == "end":
        if right < 0:
            right_or_left = "left"
        if forward < 0:
            forward_or_backward = "backward"
        print("Ending")
        print('Gandalf should fly ' + str(abs(right)) + ' steps ' 
                + right_or_left + ' and ' + str(abs(forward))
                + ' steps ' + forward_or_backward)
        break
