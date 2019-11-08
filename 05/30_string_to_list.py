

numbers_string = input('Hello, please write your numbers and press enter to confirm: ')

numbers = numbers_string.split(',')
numbers_list = []
for number in numbers:
    numbers_list.append(int(number.strip()))

print('List:', numbers_list)

# numbers_list = [int(number.strip()) for number in numbers_string]
