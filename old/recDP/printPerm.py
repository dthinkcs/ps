
def printPerm(s, selectedD=""):
    if len(s) == 0: # whatever is unselected is in s
        print(selectedD, end = " ")
    else:
        for i in range(len(s)):
            printPerm(s[:i] + s[i + 1:], selectedD + s[i])
            #        unselected, selected decisions


printPerm(input().strip())
