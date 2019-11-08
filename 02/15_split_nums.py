number = input('Give me some number: ')

half = len(number) // 2
if not half:
    print('No input provided')
else:
    first = number[:half]
    second = number[half:]

    first = int(first)
    second = int(second)

    if first % 2 == 0 and second % 2 == 0:
        print('Success')
    elif first % 2 == 0 and second % 2 != 0:
        print('First')
    elif first % 2 != 0 and second % 2 == 0:
        print('Second')
    else:
        print('Neither')
