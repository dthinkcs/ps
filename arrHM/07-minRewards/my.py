def minRewards(scores):
    # Write your code here.
	dp = [1] * len(scores)
	for i in range(1, len(scores)):
		dp[i] = 1 + dp[i - 1] if scores[i - 1] < scores[i] else 1

	for i in range(len(scores) - 2, -1, -1):
		if scores[i] > scores[i + 1]: # BUG of scores[i] < scores[i + 1]
			dp[i] = max(1 + dp[i + 1], dp[i])
	return sum(dp)
		
