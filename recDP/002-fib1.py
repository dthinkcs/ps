def fib(n, memo):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo) # WAY TO THINK about this: assume we get the answer for lower values (initially when writing code; after you finished then execute and see power of PMI)
    return memo[n]

memo = {}
print(fib(6, memo)) # 8
print(fib(4, memo)) # 3

# overlapping (sub)problems
# optimal (sub)structure

#           fib(8)
#   fib(7)         fib(6)
# fib(6) fib(5)    .  .

# first write the general case i.e. the recurrence breakdown: assume you'll get the lower answers and asssume you have given the base cases
#   then, write all the base cases
#     then, execute(execution context,etc) and check
#       [then, the O(T(n)), O(S(n))]