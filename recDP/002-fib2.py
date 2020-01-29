def fibo(n):
    fib = {0: 0, 1: 1}
    for i in range(2, n + 1): # Bug start from 2
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

print(fibo(6)) # 8
print(fibo(4)) # 3

# overlapping (sub)problems
# optimal (sub)structure

#           fib(8)
#   fib(7)         fib(6)
# fib(6) fib(5)    .  .

# first write the general case i.e. the recurrence breakdown: assume you'll get the lower answers and asssume you have given the base cases
#   then, write all the base cases
#     then, execute(execution context,etc) and check
#       [then, the O(T(n)), O(S(n))]