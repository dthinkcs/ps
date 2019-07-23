def longestCommonSubsequence(str1, str2):
    # Write your code here.
	dp = [ [[] for j in range(len(str1) + 1)] for i in range(len(str2) + 1) ]; #print(dp)

	for i in range(len(dp)):
		dp[i][0] = []
	for j in range(len(dp[0])):
		dp[0][j] = []

	for i in range(1, len(dp)):
		for j in range(1, len(dp[0])):
			#print(i, j); print(dp)
			if str1[j - 1] == str2[i - 1]:
				dp[i][j] = dp[i - 1][j - 1] + [str1[j - 1]]
			else:
				#dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key = lambda x : len(x))
				dp[i][j] =  dp[i - 1][j] + [str2[i - 1]] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1] + [str1[j - 1]]

	return dp[-1][-1]

print(longestCommonSubsequence("abc", "abc"))
