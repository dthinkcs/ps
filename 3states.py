states = "Mississippi Alabama Texas Massachusetts Kansas"
statesList = []
for word in states.split():
    if word.lower().endswith('xas'):
        statesList.append(word)
for word in states.split():
    if word.lower().startswith('k') and word.lower().endswith('s'):
        statesList.append(word)
for word in states.split():
    if word.lower().startswith('m') and word.lower().endswith('s'):
        statesList.append(word)
for word in states.split():
    if word.lower().endswith('a'):
        statesList.append(word)
for word in states.split():
    if word.lower().startswith('m'):
        statesList.append(word)
        break
print(statesList)
