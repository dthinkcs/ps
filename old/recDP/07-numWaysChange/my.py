def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
	if n < 0 :
		return 0
	if n == 0:
		return 1 # combinatorially correct
	if len(denoms) == 0:
		return 0
	# take it or leave it
	return numberOfWaysToMakeChange(n - denoms[0], denoms) + numberOfWaysToMakeChange(n, denoms[1:])



def numberOfWaysToMakeChange(n, denoms, cache = dict()):
    # Write your code here.
    if (n, len(denoms)) in cache:
        return cache[(n, len(denoms))]
    if n < 0 :
        return 0
    if n == 0:
        return 1 # combinatorially correct
    if len(denoms) == 0:
        return 0
    # take it or leave it
    cache[(n, len(denoms))] = numberOfWaysToMakeChange(n - denoms[0], denoms, cache) + numberOfWaysToMakeChange(n, denoms[1:], cache)
    return cache[(n, len(denoms))]

print(numberOfWaysToMakeChange(7, [2, 4]) == 0) # True
