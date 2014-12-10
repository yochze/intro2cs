#############################################################
# FILE : palindrome.py
# WRITER : Yochay Ettun , yochze
# EXERCISE : intro2cs ex6
# DESCRIPTION:
# Two recursive functions to determine whether a string is palindrome
# or not.
# The first gets a full string and returns boolean according to the 
# string palindromically.
# The second program gets a string and two indexes representing a 
# substring in the original string. Then it tests if the substring
# is palindrome or not. return a boolean accordingly.
#############################################################


def is_palindrome_1(my_string):
    """ Recursive program to check if a string is palindrome.
        every iteration the program compare two values (first and last char)
        if they match, it substract those chars and compare recursively
        next two chars until it's the size of 1 or 0.
        Then it returns True.

        INPUT: Any string
        OUTPUT: True if palindrome, otherwise False
        """
    if len(my_string) < 2: 
        # Base condition, if we reached here then the string
        # is palindrome. So return true
        return True
    else:
        # Length of string is not <2 , continue matching chars
        # recursively.
        if my_string[0] != my_string[-1]:
            # No match between last and first char of current string.
            # string is not palindrome. Return false.
            return False
        else:
            # String is still palindrome. Continue next iteration
            # without first and last chars of current string.
            return is_palindrome_1(my_string[1:-1])

def is_palindrome_2(s, i, j):
    """ Recursive program to determine if a substring is palindrome.
        the program is similar to the previous program, but different
        as it is given with two indexes to determine if the substring
        of those indexes is palindrome.

        INPUT: Any string, i and j integers in the range of len(string).
        OUTPUT: True if palindrome, otherwise False
    """
    if i == j or i == j+1 or len(s) == 0:
        # Base case:
        # If smaller index (by definition) is bigger than larger index by 1
        # Or the length of the string is 0 , it means that the string
        # has passed all iteration and is palindrome. return true.
        return True
    else:
        if s[i] == s[j]:
            # Compare last and first char.
            # If they're true, continue to the next pair of chars
            # while incrementing i and decrementing j .
            return is_palindrome_2(s, i+1, j-1)
        else:
            # Chars are not matching, the string is not palindrome.
            # Stop and return false.
            return False
