def fact(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    memo[n] = n * fact(n - 1, memo)
    return memo[n]

memo = {}
print(fact(5, memo)) 
print(fact(7, memo))