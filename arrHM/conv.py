def base10To3(n):
    if n < 3:
        return n
    return 10 * (base10To3(n // 3)) + n % 3

t = int(input())
for _ in range(t):
    n = int(input())
    print(base10To3(n))
