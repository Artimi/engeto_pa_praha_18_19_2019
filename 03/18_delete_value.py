myNewDict = {
    'm': 12345,
    'n': 32145,
    'o': 54321,
    'p': 23232,
    'q': 43210,
    'r': 13579
}

maximalValueOfKey = max(myNewDict.keys())
print(maximalValueOfKey)

if max(myNewDict.values()) > myNewDict[maximalValueOfKey]:
    del myNewDict[maximalValueOfKey]

print(myNewDict)