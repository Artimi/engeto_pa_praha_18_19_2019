

def pairs(sequence):
    return [pair for pair in zip(sequence[:-1], sequence[1:])]


def pascal(n):
    result = []
    for row in range(n):
        if row == 0:
            result.append([1])
        else:
            current_row = [1]
            for pair in pairs(result[-1]):
                current_row.append(pair[0] + pair[1])
            current_row.append(1)
            result.append(current_row)
    return result


def print_pascal(n):
    pascal_triangle = pascal(abs(n))
    if n == 0:
        return
    text_triangle = [' '.join(map(str, row)) for row in pascal_triangle]
    max_row_length = len(text_triangle[-1])
    if n < 0:
        text_triangle = reversed(text_triangle)
    for row in text_triangle:
        print(row.center(max_row_length))


print_pascal(-10)
