def mean(data):
    return sum(data) / len(data)


def modus(data):
    return max(set(data), key=data.count)


def median(data):
    sorted_data = sorted(data)
    data_length = len(sorted_data)
    if data_length % 2 == 0:
        return (sorted_data[data_length // 2] + sorted_data[(data_length // 2) - 1]) / 2
    else:
        return sorted_data[data_length // 2]


def statistics(data):
    options = ['sum', 'count', 'mean', 'modus', 'median', 'q']
    while True:
        operation = input(f'What do you want to know? options = {options}').lower()
        if operation not in options:
            continue

        if operation == 'q':
            break
        elif operation == 'sum':
            print('sum = ', sum(data))
        elif operation == 'count':
            number = input('Please enter a number you want to find: ')
            if not number.isnumeric():
                print('Not a number')
                continue
            number = int(number)
            count = data.count(number)
            print('count = ', count)
        elif operation == 'mean':
            result = mean(data)
            print('mean = ', result)
        elif operation == 'modus':
            result = modus(data)
            print('modus = ', result)
        elif operation == 'median':
            result = median(data)
            print('median = ', result)


statistics([
    35, 14, 26, 48, 49, 26, 18,
    25, 16, 16, 39, 17, 10, 29, 30
])
