# BUG 1 +ord('a')
# BUG 2 - ord('a')
# BUG 3 all strings are immutable in python
def caesarCipherEncryptor(string, key):
    # Write your code here.
	strn = ""
	for i in range(len(string)):
		strn += chr((ord(string[i]) - ord('a') + key) % 26 + ord('a'))
	return strn
