def diskStacking(disks):
    # Write your code here.
	sorted(disks, key = lambda x: x[2]) # sort on the basis of height
	# dp[i] stores the ans to the q what is the maximum height of tower ending with/using this current height
	dp = [ (disks[x][2], [x]) for x in range(len(disks)) ] # particular heights
	for i in range(1, len(dp)):
		print(dp)# check all condintion
		for j in range(i - 1, -1, -1):
			print(dp)
			if disks[j][2] < disks[i][2] and disks[j][1] < disks[i][1] and disks[j][0] < disks[i][0]:
				if dp[j][0] + disks[i][2] > dp[i][0]:
					dp[i] = dp[j][0] + disks[i][2], dp[j][1] + [i]


	print(dp)# NOT THE SAME AS max(dp) print(max(dp, key = lambda x: x[0]))
	return idxToArr( max(dp)[1] , disks)

def idxToArr(idxArr, disks):
	return [ disks[idx] for idx in idxArr ]

print(diskStacking([[2, 1, 2], [3, 2, 3], [2, 3, 4]]))
