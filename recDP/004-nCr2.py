def C(n, r):
    dp = [0] * (r + 1)
    for i in range(n + 1):
        for j in range(min(r, i), -1, -1):
            if j == 0 or j == i:
                dp[j] = 1
            else:
                dp[j] = dp[j] + dp[j - 1] # leave it or take it
    return dp[r]

print(C(14, 7))
