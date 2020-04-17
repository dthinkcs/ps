import copy
def maxSumIncreasingSubsequence(arr):


    dp = [  [arr[x], [arr[x]]] for x in range(len(arr)) ]
    #dp[0] =  [ arr[0], [ arr[0] ] ]
    for i in range(1, len(arr)):
        j = i - 1

        while j >= 0:
            if arr[j] < arr[i]:
                if dp[j][0] + arr[i] > dp[i][0] :
                    dp[i][0] = dp[j][0] + arr[i]
                    dp[i][1] = dp[j][1] + [arr[i]]

			j -= 1


            # big bug  return dp[-1]
    return max(dp, key=lambda x : x[0])
