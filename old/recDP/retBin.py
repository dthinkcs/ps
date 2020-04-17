def retBin(n):
    if n == 0:
        return [""]
    smallLt = retBin(n - 1)
    return [str(i) + s for i in range(2) for s in smallLt ]

def retBinLong(n):
    if n == 0:
        return [""]

    smallLt = retBin(n - 1)
    lt = []
    for i in range(2):
        for s in smallLt:
            lt.append(str(i) + s)
    return lt

print(retBinLong(int(input().strip())))
