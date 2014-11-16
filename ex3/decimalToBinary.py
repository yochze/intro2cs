#############################################################                   
# FILE : decimalToBinary.py                                                            
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex3 2014-2015                                             
# DESCRIPTION:                                                                  
# #############################################################   

decimal = int(input("give me decimal"))
binary  = 0
i = 1
base = 2

while decimal > 0:
    r = decimal % base 
    binary += i*r
    i *= 10
    decimal //= base 

print(binary)
