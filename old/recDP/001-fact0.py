def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

print(fact(5)) # 120
print(fact(7)) # 5040