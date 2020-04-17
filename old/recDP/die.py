
def printDieRoll(n, outputD=""):
    if n == 0:
        print(outputD, end = " ")
    else:
        for i in range(1, 7):
            # choose i
            # go explore with that choice
            printDieRoll(n - 1, outputD + str(i))
            # unchoose i (since my outputD is different it automatically gets unselected)

printDieRoll(int(input().strip()))
