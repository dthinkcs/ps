def isPrime(n):
    if n == 0 or n == 1:
        return False

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def isPalin(n):
    return n == n[::-1]

t = int(input().strip())
for _ in range(t):
    n = (input().strip())
    if isPalin(n) and isPrime(int(n)):
        print(1)
    else:
        print(0)
