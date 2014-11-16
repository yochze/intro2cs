#############################################################                   
# FILE : binaryToDecimal.py                                                            
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex3 2014-2015                                             
# DESCRIPTION:                                                                  
# #############################################################  


binary  = str(input("Inser number in bianry representation:"))
length  = len(binary)
decimal = 0
base    = 2

for num in range(1, length+1):
    digit = int(binary[length-num])
    decimal +=  digit * (base**(num-1))

print("Decimal: " + str(decimal))
