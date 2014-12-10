#############################################################
# FILE : balanced_brackets.py
# WRITER : Yochay Ettun , yochze
# EXERCISE : intro2cs ex6
# DESCRIPTION:
#
#############################################################

def is_balanced(s):
    """
    Function to test if the brackets inside a string are balanced.
    The function iterates the given string
    if an open bracket was found, it incrementing the expected closures count
    if it found a closure it decrementing the expected closures count.
    If in some stage the expected_closures is negative (meaning: too 
    much closures), then the string is not balanced and it reutrn false to
    user. Otherwise, if the expected count is 0 then it returns true.

    INPUT: Any string.
    OUTPUT: True or False depending if the string is balanced brackets-wise.
    """
    left_p, right_p  = "(", ")" # Set parenthesis to variables.

    result = True         # Default to True
    expected_closures = 0 # Reset expected_closures

    for char in s:

        if char == left_p:
            expected_closures += 1
        elif char == right_p:
            if expected_closures == 0:
                result = False
            else:
                expected_closures -= 1
    
    if result and expected_closures == 0:
        return True
    else:
        return False
        
# print(is_balanced("a(b))")) # Error
# print(is_balanced("a(b)")) # Good
# print(is_balanced("())b((")) # Error
# print(is_balanced("a(basjdf)()")) # good
# print(is_balanced("a(ba(sjdf)()")) # good


def violated_helper(s, ec, n):
    """ 
    A helper function that recursively iterates through the string s
    and returns the index of the first error parenthesis (n) of the string
    Or returns the length of the string if the whole string can be 
    fixed to have balanced parenthesis.

    INPUT: s  == A brackets' balanced string.
           ec == expected_closures integer
           n  == current char index
    
    OUTPUT: Index of the error (n) or size of string (len(s)).
        
    """     
    left_p, right_p  = "(", ")" # Set parenthesis to variables.

    if s[n] == left_p:
        # Check the char in the n place
        # if it's left_p expected_closures (ec) should be incremented by 1
        # if it's right_p then ec should be decremented by 1.
        ec += 1
    elif s[n] == right_p:
        ec -= 1

    if ec < 0: 
        # Base Case #1:
        # The string doesn't have matching parenthesis.
        # Stopping the recursion and Return index of the char
        # that violated the string.
        return n         

    elif ec > 0 and (n+1 == len(s)):
        # Base Case #2:
        # Iterated the entire string and found that the string can be 
        # completed to a balanced parenthesis string.
        # So return the length of the string.
        return len(s) # Size of string
        
    else:
        # Continue iterating recursively through the string 
        # and incrementing the char index number
        return violated_helper(s, ec, n+1)

def violated_balanced(s):
    """ 
      A wrapping function to determine the exactly violation of a certain
      string.

    """
    balanced = -1 # Set confirmed balanced
    
    if is_balanced(s):
        # Check with an external method if the string is balanced.
        # if so, return the balanced variable (-1).
        return(balanced)
    else:
        # The string is not balanced. Hence, call the recursive
        # function with initial values 
        # (
        # s for string
        # 0 for expected_closures
        # 0 for current char index. )
        
        # and return its output

        return violated_helper(s, 0, 0)

def match_brackets(s):
    mylist = []
    
    return matcher(s, mylist, 0) 


def matcher(s, mylist, n):
    if len(s)-1 != n:
        if s[n] == "(":
            res = find_closure(s[n:]) - n
            print("closure: "  + str(find_closure(s[n:])) + " -  "+ str(n) )

        elif s[n] == ")":
            res =  n - find_opener(s[:n]) 
            print("opener: " + str(n) + " - " + str(find_opener(s[:n])))

        else:
            res = 0

        mylist.append(res) 
        return matcher(s, mylist, n+1)

    else:
        return mylist

        
def find_opener(s):
    if not is_balanced(s[1:]):
        return(len(s)-1)
    else:
        return find_opener(s[1:])



def find_closure(s):
    if not is_balanced(s[:-1]):
        return(len(s)-1)
    else:
        return find_closure(s[:-1])

print(find_opener("asd(sdf)"))
print(find_closure("(sdf)s"))
print(find_closure("(aasdfsdf)asdfsdf"))



print(match_brackets("ss(aasdfsdf)asd()()fsdf"))
print(len("ss(aasdfsdf)as()dfsdf"))
print(match_brackets("(()())")) #  [5, 1, -1, 1, -1, -5]
print(match_brackets("()"))
