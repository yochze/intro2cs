def is_palindrome_1(my_string):
    if len(my_string) == 0:
        return True
    else:
        if my_string[:1] != my_string[-1:]:
            return False
        else:
            is_palindrome_1(my_string[1:-1])

def is_palindrome_2(s, i, j):
    if i > j or len(s) == 0:
        return True
    else:
        if s[i] == s[j]:
            is_palindrome_2(s, i+1, j-1)
        else:
            return False


# print(is_palindrome_1(''))
# print(is_palindrome_2('', 0,0))
