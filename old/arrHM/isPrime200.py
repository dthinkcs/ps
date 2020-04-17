
def isPrime(n):
    if n == 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

for i in range(3, 200, 2):
    if(isPrime(i) == (i % 3 != 0 and i % 5 != 0 and i % 7 != 0)) == False:
        print(i)
