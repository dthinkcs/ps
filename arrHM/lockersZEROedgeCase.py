t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    m = int(input().strip())
    if m == 0:
        print(n)
    else:
        print(n - n // m)
