days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_number = input('Give me some day: ')
if not day_number: # not '' == True
    print('No input provided')
elif not day_number.isnumeric():
    print('Enter only numbers please.')
elif not(0 <= int(day_number) -1 <= 6):
    print('ERROR')
else:
    print(days[int(day_number) -1])
