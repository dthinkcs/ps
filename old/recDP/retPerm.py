# ([abc]) -> a ([bc]), b ([ca]), c ([ab]) ## like 3 * whatever(2)

def retPerm(s):
    return [""] if s == "" else [s[i] + small_str for i in range(len(s)) for small_str in retPerm(s[:i] + s[i + 1:]) ]

print(retPerm(input().strip()))
