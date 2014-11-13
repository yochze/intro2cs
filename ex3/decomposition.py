#############################################################                   
# FILE : decomposition.py                                                            
# WRITER : Yochay Ettun , yochze,  201517018                                    
# EXERCISE : intro2cs ex3 2014-2015                                             
# DESCRIPTION:                                                                  
# #############################################################  

composed_number = int(input("Insert composed number:"))
n = 1
digits = []

while composed_number > n:
    c = composed_number % n
    if c == composed_number:
        break
    else:
        digits.append( composed_number // n % 10 )
        n*=10

idx = 1
for digit in digits:
    print("The number of goblets Gimli drank on day " + 
            str(idx) + " was " + str(digit))
    idx += 1
    
