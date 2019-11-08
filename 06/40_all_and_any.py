

def all_true(sequence):
    for item in sequence:
        if not item:
            return False
    return True


print(all_true([43, 45, 87, 21, 23]))
print(all_true([]))
print(all_true([0, 12, 431, 3]))


def any_true(sequence):
    for item in sequence:
        if item:
            return True
    return False


print()
print(any_true([43, 45, 87, 21, 23]))
print(any_true([]))
print(any_true([0, 12, 431, 3]))
print(any_true(['', [], (), 0]))



