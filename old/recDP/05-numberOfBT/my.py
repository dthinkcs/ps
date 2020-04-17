def numberOfBinaryTreeTopologies(n):
    # Write your code here.
	if n == 0:
		return 1 # its not zero Combinatorially(Conveniently) Its 1

	ans = 0
	for i in range(n):
		leftAns = numberOfBinaryTreeTopologies(i)
		rightAns = numberOfBinaryTreeTopologies(n - 1 - i)
		ans += leftAns * rightAns
	return ans

cache = dict()
def numberOfBinaryTreeTopologies(n):
    # Write your code here.
    if n in cache:
        return cache[n]
	if n == 0:
		return 1 # its not zero Combinatorially(Conveniently) Its 1

	ans = 0
	for i in range(n):
		leftAns = numberOfBinaryTreeTopologies(i)
		rightAns = numberOfBinaryTreeTopologies(n - 1 - i)
		ans += leftAns * rightAns
	cache[n] = ans
    return cache[n]
