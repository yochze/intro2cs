#############################################################                   
# FILE : decimalToBinary.py                                                            
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex3 2014-2015                                             
# DESCRIPTION:                                                                  
# Given a decimal binary (base 10) the program calculates the
# number's binary representation.
# #############################################################   

decimal = int(input("Insert number in decimal representation:"))
binary  = 0 
i = 1 

while decimal > 0:
    # The iteration works until decimal reaches to 0.
    # Every step of the iteration, decimal value is replaced with
    # a whole half of it e.g. (61 // 2 == 30), thus reaches to 0 eventually.
    
    binary += i * (decimal % 2) # In each step it increments the binary
                                # value with i times decimal modulu 2

    i *= 10 # Increment i by 10 times (basically it's 10^n)
    decimal //= 2 

# Printing the binary result
print("The binary value of the inserted decimal number is " + str(binary))
