
def matching(opening, closing):
    return opening == '(' and closing == ')' or opening == '{' and closing == '}' or opening == '[' and closing == ']'

def checkBalanced(expr):
### Implement your code here

    stack = []
    for c in expr:
        if c == '(' or c == '{' or c == '[':
            stack.extend(c)
        elif c == ')' or c == '}' or c == ']':
            if len(stack) == 0:
                return False
            else:
                opening = stack.pop()
                if not matching(opening, c):
                    return False
    if len(stack) != 0:
        return False

    return True

exp=input()
if checkBalanced(exp):
    print('true')
else:
    print('false')
