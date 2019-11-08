text = input('Give me any string: ')
if text.isdigit():
    print('Numeric')
elif text.isalpha():
    print('Letters Only')
else:
    print('Mixed')