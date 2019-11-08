

def rev(sequence):
    result = []
    for item in sequence:
        result.insert(0, item)
    return result


print(rev(range(10)))
print(rev(['New', 'Years', 'Eve']))
print(rev('Hello World'))
