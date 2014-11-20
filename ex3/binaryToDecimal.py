#############################################################                   
# FILE : binaryToDecimal.py                                                            
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex3 2014-2015                                             
# DESCRIPTION:                                                                  
# Given a binary number , the program calculates its decimal (base 10)
# representation form and prints it.
# #############################################################  


binary  = str(input("Insert number in binary representation:"))
length  = len(binary) # Getting the length of the binary number for future use.
decimal = 0

for num in range(1, length+1):
    # Repeating from 1 to the length size of the binary number.
    # Each iteration will increment the decimal var with the 
    # calculated number.

    digit = int(binary[length-num]) # assigning digit var the current 
                                    # number extracted from the binary
                                    # (the forloop goes from left to right)
    
    decimal +=  digit * (2**(num-1)) # Incrementing decimal value with
                                     # the extracted digit times 2^position
                                     # (simple binary to decimal formula)

# Printing the decimal number
print("The decimal value of the inserted binary number is " + str(decimal))
