def fact(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

print(fact(5)) # 120
print(fact(0)) # 1
print(fact(7)) # 5040