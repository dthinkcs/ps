def isPalin(w):
    return w[::-1] == w
print("isPalin('dad') =", isPalin("dad"))
print("isPalin('diddy') =", isPalin("diddy"))

def removePunc(s):
    puncs = ".,\"\';:!?-[]()"
    for punc in puncs:
        s = s.replace(punc, '')
    return s
s = "This is a statement; followed by a, question?"
print(s)
print("After removing Punctutation:", removePunc(s))


def sortWords(w):
    return sorted(w)
w = ['Cat', 'Bat', 'Xat', 'Mat']
print(w, 'Sorted Alphabetically:', sortWords(w))


def mergeMail(names, body):
    strOut = ""
    for name in names:
        strOut += "Dear" + name + ",\n\t" + body + "\n"
    return strOut

names = ['Rishabh', 'Tony', 'Peter', 'Bruce']
body = "You are cordially invited to the International Summit For Science And Technology."
mergeMail(names, body)



def reDemo():
    import re

    phone = "983-123-8912 # This is Phone Number"

    # Delete Python-style comments
    num = re.sub(r'#.*$', "", phone)
    print("Phone Num : ", num)

    # Remove anything other than digits
    num = re.sub(r'\D', "", phone) # other than digits
    print("Phone Num : ", num)

reDemo()


def environmentDemo():
    import os
    for key in os.environ:
        print(key, os.environ[key])
environmentDemo()
