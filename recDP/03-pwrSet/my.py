def powerset(arr):
    # Write your code here.
	if len(arr) == 0:
		return [[]]

	smallSet = powerset(arr[1:]) # find the smallAns
	return smallSet + [ [arr[0]] + v for v in smallSet ] # smallSet + arr[0] to each v you get from smallSet
