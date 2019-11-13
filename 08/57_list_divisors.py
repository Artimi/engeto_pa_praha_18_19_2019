HEADER = ['Divisor', 'Numbers Divided']
DIVISORS = list(range(2, 10))


def get_max_widths(l):
    transposed = list(map(list, zip(*l)))
    max_value = [max(column, key=len) for column in transposed]
    max_widths = list(map(len, max_value))
    return max_widths


def get_numbers_divided(divisor, numbers):
    return [
        number for number in numbers
        if number % divisor == 0
    ]


def format_row(row, widths):
    elements = []
    for element, width in zip(row, widths):
        elements.append(element.center(width))
    center = ' | '.join(elements)
    return f'| {center} |'


def format_table(divided):
    table = [HEADER]
    for divisor, numbers_divided in divided:
        table.append((str(divisor), ', '.join(map(str, numbers_divided))))

    max_widths = get_max_widths(table)

    header = format_row(table[0], max_widths)
    separator = '=' * len(header)
    rows = [format_row(row, max_widths) for row in table[1:]]

    return '\n'.join([header, separator] + rows)


def main():
    try:
        start = int(input('START POINT: '))
        end = int(input('END POINT: '))
    except ValueError:
        print('Inserted non-int value!')
        return

    numbers = list(range(start, end + 1))

    divided = [(divisor, get_numbers_divided(divisor, numbers)) for divisor in DIVISORS]
    print(format_table(divided))


main()
