#############################################################
# FILE : balanced_brackets.py
# WRITER : Yochay Ettun , yochze
# EXERCISE : intro2cs ex6
# DESCRIPTION:
# Several functions to determine if a string has a balanced
# structure of parenthesis.
# Also functions to determine what is wrong in an unbalanced
# string. And another function to map the parenthesis and chars
# in a balanced string.
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
    """
    Wrapper function to call matcher recursive function.
    The matcher function is called only if the input string is 
    a balanced parenthesis string.

    INPUT:  Any string.
    OUTPUT: An empty list if string is not balanced. Or:
            A list in size of string, containing:
            0 if not "(" or ")"
            number of matching parenthesis index.
    """
    if is_balanced(s):
        # Run recursive function if the string is balanced.
        mylist = [0] * len(s) # prefill the output list with 0s
        templist = [] # temp list will behave as stack inside the recursive
                      # function.

        return matcher(s, templist, mylist, 0)  # Return and  call recursion
    else:
        return [] # String is not balanced,  return empty list.


def matcher(s, templist, mylist, n):
    """
    The recursive function that eventually returns a list of required elements
    (0 if not parenthesis, or index number of matching parenthesis)

    INPUT:  s        == The string
            templist == list with opened parenthesis indexes
            mylist   == The output containing 0 or index of matching 
                        parenthesis.
            n        == number of iteration (i.e. the index)

    OUTPUT: either the recursive output. Or the mylist list with the final
            output.

    """
    left_p, right_p  = "(", ")" # Set parenthesis to variables.
    if n < len(s):
        # Base Case:
        # If n (number of recursive iterations) is equal to the length of
        # the input string, stop and return the list.
        # Otherwise, keep iterating through the string.
        if s[n] == left_p:
            # If it's an open parenthsis, append the index number to templist
            # and call the function again (recursively).
            templist.append(n)
            return matcher(s, templist, mylist, n+1)

        elif s[n] == right_p:
            # If it's a closing parenthesis then it is matching the 
            # last opened parenthesis that was stored in the list.
            # therefore, remove the item from the templist
            # and store difference (i-n/n-i) in the appropriate index.
            i = templist[-1]
            templist.pop() # Remove last element from list.
            mylist[i] = n - i # Store difference of indexes in list
            mylist[n] = i - n 
            return matcher(s, templist, mylist, n+1) # Call the function 
                                                     # again on the next idx.

        else:
            return matcher(s, templist, mylist, n+1)
    else:
        return mylist
