

def minimum(sequence):
    if not sequence:
        return None
    min_value = sequence[0]
    for value in sequence:
        if value < min_value:
            min_value = value
    return min_value


def maximum(sequence):
    if not sequence:
        return None
    max_value = sequence[0]
    for value in sequence:
        if value > max_value:
            max_value = value
    return max_value


print(minimum([1, 2, 3, -4, 5]))
print(maximum([1, 2, 3, -4, 5]))
