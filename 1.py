# Lab Exercises
# 1. Write the Python programs to do the following:
# a) Implement simple calculator operations.
# b) Find the transpose of a matrix.
# c) Multiplication of two matrices.
# d) Addition of two matrices.
# e) Sum of natural numbers using recursion.
# f) Fibonacci sequence using recursion.
# g) To convert decimal to binary, octal and hexadecimal.
# h) To illustrate different set operations.
# i) Write a program to find whether a list is palindrome or not.
# j) Write a Python program to create a Caesar encryption without using maketrans and translate functions. In cryptography, a Caesar cipher, is one of the simplest and most widely known encryption techniques. In this method each alphabet in the input is replaced by another alphabet with some fixed no of positions down the alphabet.
# Example: ZOO is replaced with CRR
# Additiona1 Exercises
# 1. Write a Python program to generate the prime numbers between m and n.
# 2. Write a Python program to sort the contents of a list without using in built in sort method.
# 3. Write a Python program to find the sum of the elements of the list using recursion
# 4. Write a program to remove the duplicate elements of a list
# 5. Write a Python program to reverse the list without using any of the methods/slicing
# Lab Exercises
# 1. Write the Python programs to do the following:
# a) To check whether the string is palindrome or not.
# b) To remove punctuations from the string.
# c) Sort words in alphabetic order.
# d) To merge mails.
# e) To find and replace a string using regular expressions.
# f) To display environment variables.
# Additional Exercises
# ITT LAB MANUAL
# 1. Write a Python program named states.py that declares a variable states with value "Mississippi Alabama Texas Massachusetts Kansas". write a Python program that does the following:
# a) Search for a word in variable states that ends in xas. Store this word in element 0 of a list named statesList.
# b) Search for a word in states that begins with k and ends in s. Perform a case-insensitive comparison. [Note: Passing re.I as a second parameter to method compile performs a case-insensitive comparison.] Store this word in element 1 of statesList.
# c) Search for a word in states that begins with M and ends in s. Store this word in element 2 of the list.
# d) Search for a word in states that ends in a. Store this word in element 3 of the list.
# e) Search for a word that begins with M in states at the beginning of the string. Store this word at element 4 of the list.
# f) Output the array states List to the screen.

n = (eval(input().strip()))
print(n)


def transpose_matrix(matrix):
    newMatrix = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            newMatrix[j][i] = matrix[i][j]
    # print(newMatrix)
    return newMatrix

matrix =  [ [  i**3 - j for j in range(3)] for i in range(3)]
print("Matrix:", matrix)
transposedMatrix = transpose_matrix(matrix)
print("Transpose: ", transposedMatrix)

def mulMatrices(A, B):
    # pxq rxs = pxs
    p, q, r, s = len(A), len(A[0]), len(B), len(B[0])
    assert q == r
    C = [[0 for j in range(p)] for i in range(s)]
    for i in range(p):
        for j in range(s):
            for k in range(q):
                C[i][j] += A[i][k] * B[k][j]
    return C

def I(n):
    return [ [1 if j == i else 0 for j in range(n)] for i in range(n)]
matrixA = matrix
matrixB = transposedMatrix
matrixC = mulMatrices(matrixA, matrixB)
print("Multiplication Result = ", matrixC)

def addMatrices(A, B):
    assert len(A) == len(B) and len(A[0]) == len(B[0])
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("Addition Result = ", addMatrices(matrixA, matrixB))


def sumofFirstNNatrualNumbers(n):
    return (n * (n + 1)) // 2
print(sumofFirstNNatrualNumbers(n))


def fib(n):
    curr, next = 0, 1
    for i in range(n    ):
        curr, next = next, curr + next
    return curr
print(fib(n))

def binOctHex(n):
    return "Binary:{} Octal:{} Hexadecimal:{}".format(bin(n), oct(n), hex(n))
print(binOctHex(n))


def setOperations():
    setA = {i for i in range(5)}
    setB = {i + 2 for i in range(5)}
    print(setA.union(setB)); print(setA.intersection(setB)); print(setA - setB);
setOperations()

def isPalin(w):
    return w[::-1] == w
print("isPalin('dad') =", isPalin("dad"))
print("isPalin('diddy') =", isPalin("diddy"))

def caesarCipher(plaintext, key):

    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
            if c.islower():
                ciphertext += chr(( ord(c) - ord('a') + key ) % 26 + ord('a'))
            else:
                ciphertext += chr(( ord(c) - ord('A') + key ) % 26 + ord('A'))
        else:
            ciphertext += c
    return ciphertext
plaintext = "Attack On Pearl Harbour: December 7, 1941"
print("Plaintext: {}\nCiphertext: {}".format(plaintext, caesarCipher(plaintext, n)))

#----------DONE WRITE BEFORE THIS

def isPrime(n):
    n = abs(n)
    if n in [0, 1]:
        return False
    possibleDivisor = 2
    while possibleDivisor*possibleDivisor <= n:
        if n % possibleDivisor == 0:
            return False
        possibleDivisor += 1
    return True


def generateAllPrimes(m, n):
    listPrimes = []
    for i in range(m, n + 1):
        if isPrime(i):
            listPrimes.append(i)
    return listPrimes

listPrimes = generateAllPrimes(n, n** 2)
print("Primes from {} to {} are: ".format(n, n**2), listPrimes)

def myInPlaceSort(arr):
    for i in range(len(arr) - 1):
        minIdx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIdx]:
                minIdx = j
        if minIdx != i:
            arr[i], arr[minIdx] = arr[minIdx], arr[i]

lt = list(reversed(listPrimes))
print("List:", lt)
myInPlaceSort(lt)
print("Sorted List:", lt)

def sumRec(lt):
    if len(lt) == 0:
        return 0
    return lt[0] + sumRec(lt[1:])
print(lt, " Sum Of List: {}".format(sumRec(lt)))


def removeDup(lt):
    return list(set(lt))

lt = [1, 2, 2, 4]
print(lt, " Duplicates Removed:", removeDup(lt))

def myInPlaceReverse(lt):
    for i in range(len(lt) // 2):
        lt[i], lt[-i-1] = lt[-i-1], lt[i]


myInPlaceReverse(lt)
print("List Reversed:", lt)

# file = open("test.txt", "r") # 'w', 'a' // write and append
# # print(file.read())
# # file = open("test.txt", "r")
# print(file.read(5))
# print(file.tell())
#
# file = open("testfile.txt", "w")
# file.write("Hello! This is Discipline 2020.")
# fhand = open("testfile.txt", "w")
# fhand.write("THIS WILL OVERWRITE")
# fhand.writeline()
# fhand = open("testfile.txt", "a")
# fhand.seek(0)
# fhand.readline(9) # readline(9 characters at max) read will read character by characters // IT CAN BE POSSIBLE len(read) > len(readlines)
# fhand.readlines() # reads all lines -> LIST
