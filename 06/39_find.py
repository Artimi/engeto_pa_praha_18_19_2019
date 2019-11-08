


def find(sequence, item):
    for index, element in enumerate(sequence):
        print(element, '==', item)
        if element == item:
            return index
    return -1


print(find(['pear', 'apple', (23, 45), 653, {'name': 'John'}], 'apple'))
