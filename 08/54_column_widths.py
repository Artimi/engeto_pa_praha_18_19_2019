data = [
    ['Name', 'Item', 'Amount', 'Unit_Price', 'Total_Price'],
    ['Bettison, Elnora', 'Doxycycline Hyclate', 98, 23.43, 2296.14],
    ['McShee, Glenn', 'DROXIA', 27, 33.86, 914.22],
    ['Conyard, Phil', 'Nadolol', 44, 12.35, 543.4],
    ['Bettison, Elnora', 'Claravis', 91, 9.85, 896.35],
    ['Idalia, Craig', 'Nadolol', 83, 12.35, 1025.05],
    ['Woodison, Annie', 'Metolazone', 46, 43.06, 1980.76],
    ['Woodison, Annie', 'DROXIA', 50, 33.86, 1693.0],
    ['Skupinski, Wilbert', 'Nadolol', 60, 12.35, 741.0],
    ['Conyard, Phil', 'WRINKLESS PLUS', 49, 23.55, 1153.95],
    ['Bettison, Elnora', 'Doxycycline Hyclate', 59, 23.43, 1382.37],
    ['Skupinski, Wilbert', 'Metolazone', 51, 43.06, 2196.06],
    ['McShee, Glenn', 'Claravis', 1, 9.85, 9.85]
]


def len_anything(value):
    return len(str(value))


def get_max_widths(l):
    transposed = list(map(list, zip(*l)))
    max_value = [max(column, key=len_anything) for column in transposed]
    max_widths = list(map(len, max_value))
    return max_widths

    # if not l:
    #   return []
    # max_widths = [0 * len(l[0])]
    # for row in l:
    #     for index, item in enumerate(row):
    #         length = len(str(item))
    #         if length > max_widths[index]:
    #             max_widths[index] = length
    # return max_widths


def print_max_widths(l):
    widths = get_max_widths(l)
    result = [['COLUMN', 'WIDTH']]
    for index, width in enumerate(widths):
        result.append([f'COL {index + 1}', str(width)])
    max_widths_result = get_max_widths(result)
    for c1, c2 in result:
        print('| ' + c1.center(max_widths_result[0]) + ' | ' + c2.center(max_widths_result[1]) + ' |')


print_max_widths(data)
