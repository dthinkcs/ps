def fibo(n):
    curr = 0
    next = 1 # wasBUG: change 2 to 1 coz curr starts from 0
    for _ in range(1, n + 1): # Bug start from 2
        next_next = curr + next
        curr = next
        next = next_next
    return curr

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