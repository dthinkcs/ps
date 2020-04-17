def minStepsTo1DP(n, memo):
    ''' Return Minimum no of steps required to reach 1 using using Dynamic Prog'''
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################

    memo[1] = 0

    for i in range(2, n + 1):
        if i in memo:
            return memo[i]

        b = float('inf')
        c = float('inf')
        a = 1 + memo[i - 1]
        if i % 2 == 0:
            b = 1 + memo[i //2]
        if i % 3 == 0:
            c = 1 + memo[i // 3]

        memo[i] = min(a, b, c)
    return memo[n]

# Main
n=int(input())
hm = dict()
print(minStepsTo1DP(n, hm))
