def one_diff(s, t):

    if len(s) != len(t):
        return False

    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1

    return count == 1

print(one_diff("banana", "apple"))
print(one_diff("need", "reed"))
print(one_diff("goof", "good"))
print(one_diff("food", "feed"))


