
''' 
def isNsubset(s1, s2):
    exist = True
    for item in s1:
        if item not in s2:
            exist = False
    return exist

Issues with this version of isNsubset is that it takes 
Quadratic Time because each item in s1 needs to be 
needs to be searched in s2 to find whether it is in s2 or not.
Also this version finds if s1 is a subset of s2 while the second
version finds if s1 is a proper subset of s2.
Also we could have ended earlier by modifying the program a little.
def isNsubset(s1, s2):
    for item in s1:
        if item not in s2:
            return False
    return Ture

The logic of the following bersion of isNsubset is
that it first converts all the lists into tuples and 
then checks if the set t1 is a proper subset of set t2.
Pros: The time complexity of the program has reduced from quadratic time to linear time 
Cons: the logic of the program is written in an imperative manner
which makes it less readable
The use of the tuple constructor is important because a set in 
python must contain immutable elements.


'''

def isNsubset(s1, s2):
    t1 = []; t2 = []
    for item in s1:
        t1.append(tuple(item))
    for item in s2:
        t2.append(tuple(item))
    return set(t1) < set(t2)

# (c)
def inNsubset(s1, s2):
    t1 = list(map(tuple, s1))
    t2 = list(map(tuple, s2))
    return set(t1) < set(t2)

# (d)
def isNsubset(s1, s2):
    return sum([True for ele in s1 if ele in s2]) == len(s1)

def isNsubset(s1, s2):
    f = lambda ele: (True if ele in s2 else False)
    return sum(list(map(f, s1))) == len(s1)
    
# def isNsubset(s1, s2):
#     return set(map(tuple, s1)) <= set(map(tuple, s2))



def main():
    sA = ([0], [1, 2, 3], [4, 5], [6, 7, 8], [9])
    sB = ([4, 5], [6, 7, 8])
    print( isNsubset(sA, sB)) # -> False
    print( isNsubset(sB, sA)) # -> True

if __name__ == "__main__":
    main()