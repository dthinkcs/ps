# O(n) time | O(1) space
def fib(n):
    curr, next = 0, 1
    for i in range(1, n + 1):
        curr, next = next, curr + next
    return curr
