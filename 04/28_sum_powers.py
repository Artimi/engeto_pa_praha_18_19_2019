

number = int(input('Please enter your number: '))

result = 0
while number > 0:
    result += number ** number
    number -= 1

print('The result is:', result)
