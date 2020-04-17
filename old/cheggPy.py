def exchange(word, idx1=0, idx2=-1):
    if not (idx1 >= 0 and idx1 < len(word) or idx1 < 0 and abs(idx1) <= len(word)):
        return ""  # invalid case
    if not (idx2 >= 0 and idx2 < len(word) or idx2 < 0 and abs(idx2) <= len(word)):
        return "" # invalid case

    new_word = ""
    for l in word:
        if l == word[idx1]:
            new_word += word[idx2]
        elif l == word[idx2]:
            new_word += word[idx1]
        else:
            new_word += l
    return new_word

print(exchange("banana"))
print(exchange("banana", 2))
print(exchange("strawberry"))
print(exchange("strawberries", 2, 4))
print(exchange("strawberries", -2, -4))
print(exchange("constitution", 53))



