


def twoNumberSum(array, targetSum):
    # Write your code here.
	seen = set()
	for num in array:
		if targetSum - num in seen:
			return sorted([num, targetSum - num])
		seen.add(num)
	return []
