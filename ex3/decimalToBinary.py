#############################################################                   
# FILE : decimalToBinary.py                                                            
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex3 2014-2015                                             
# DESCRIPTION:                                                                  
# #############################################################   

decimal = int(input("give me decimal"))
binary  = 0
i = 1
BASE= 2

while decimal > 0:
    r = decimal % BASE 
    binary += i*r
    i *= 10
    decimal //= BASE

print(binary)
