def int_convert(*args):
    result = []
    for item in args:
        try:
            result.append(int(item))
        except ValueError:
            pass
    return result


print(int_convert('Hello', '23', '12', 'Bob', 'new', '4312', '5'))