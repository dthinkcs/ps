# 19minutes if you kinda sorta know the algo just do it the brute force way not the brute brute force way
def longestPalindromicSubstring(string):
    # Write your code here.
	maxStr = ""
	curr = ""
	for i in range(len(string)):
		# option 1 pivot about that string
		# string[i - 1] == string[i + 1]
		j = 0
		while True:
			if i - j < 0 or i + j >= len(string):
				break
			if string[i - j] == string[i + j]:
				curr = string[i - j : i + j + 1]
			else:
				break # BUG 1 break remember the bugs ex: vdmi6561 is WRONG
			j += 1

		# BUG 2 must check after this as well
		if len(curr) > len(maxStr):
			maxStr = curr

		# option 2 to pivot one less that that
		# string[i - j] == string[i + j - 1]
		j = 1
		while True:
			if i - j < 0 or i + j - 1 >= len(string):
				break
			if string[i - j] == string[i + j - 1]:
				curr = string[i - j : i + j - 1 + 1]
			else:
				break
			j += 1

		if len(curr) > len(maxStr):
			maxStr = curr
	return maxStr
