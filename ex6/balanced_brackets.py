def is_balanced(s):
    LEFT_P  = "("
    RIGHT_P = ")"

    result = True
    expected_closures = 0

    for char in s:

        if char == LEFT_P:
            expected_closures += 1
        elif char == RIGHT_P:
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
    LEFT_P  = "("
    RIGHT_P = ")"

    if s[n] == LEFT_P:
        ec += 1
    elif s[n] == RIGHT_P:
        ec -= 1

    if ec < 0: 
        # print(n)
        return n # Return index of that char
        
    elif ec > 0 and (n+1 == len(s)):
        # print(len(s))
        return len(s) # Size of string
        
    else:
        return violated_helper(s, ec, n+1)



def violated_balanced(s):
    BALANCED = -1
    
    if is_balanced(s):
        return(BALANCED)
    else:
        violated_helper(s, 0, 0)



# print(violated_balanced("a)(ba()sjdf)()")) # good
# print(violated_balanced("a()")) # good
# print(violated_balanced("(((((((")) # 6
# print(violated_balanced("(()(((")) # good
# print(violated_balanced("1(4154t5t")) #, 9)
# print(violated_balanced("14)1")) #, 2)
# print(violated_balanced("14))))1")) #, 2)
# print(violated_balanced("1(4)1)")) #, 5)
# print(violated_balanced("()(())")) #, -1)
# print(violated_balanced("()(()")) #, 5)
# print(violated_balanced("((())")) #, 5)
# print(violated_balanced(")(())")) #, 0)


