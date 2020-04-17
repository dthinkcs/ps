def levenshteinDistance(str1, str2):

	if len(str1) == 0:
		return len(str2)

	if len(str2) == 0:
		return len(str1)

	if str1[0] == str2[0]:
		return levenshteinDistance(str1[1:], str2[1:])
	else:
		return 1 + min(levenshteinDistance(str1[1:], str2[1:]), levenshteinDistance(str1[1:], str2), levenshteinDistance(str1, str2[1:]))
#DPR-> minimum : take a look at which is needed min or maximum
