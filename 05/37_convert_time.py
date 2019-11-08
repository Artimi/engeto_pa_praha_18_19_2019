

input_time = input('Please enter your time: ')

hour, minute = input_time.split(':')
hour = int(hour.strip())
minute = int(minute.strip())

if not (0 <= hour <= 23):
    print('Wrong hour', hour)
    exit()
elif not (0 <= minute <= 59):
    print('Wrong minute:', minute)
    exit()

daytime = 'AM'
if int(hour) > 12:
    hour -= 12
    daytime = 'PM'

print('Converted to English:', hour, ':', minute, daytime)