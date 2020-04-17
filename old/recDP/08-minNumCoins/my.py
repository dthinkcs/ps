#meth1 -> last Coin Take
def fn(n, denoms, cache):
    # Write your code here.
	if (n, len(denoms)) in cache:
		return cache[(n, len(denoms))]

    if n == 0:
        return 0
	if n < 0:
		return float('inf')
	# recurrence min for All i (n - denoms[i])
	ans = float('inf')
	for denom in denoms:
		ans = min(ans, 1 + fn(n - denom, denoms, cache))
	cache[(n, len(denoms))] = ans
	return ans



def minNumberOfCoinsForChange(n, denoms):
	cache = dict()
	ans = fn(n, denoms, cache)
	if ans == float('inf'):
		return -1
	else:
		return ans
