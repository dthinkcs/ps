def C(n, r):
    if n < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1

    return C(n - 1, r - 1) + C(n - 1, r)

print(C(0, 0))

# bug
# if n <= 0 or r > n:
#         return 0

