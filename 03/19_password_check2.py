data = {'user1': 'password1', 'Mark': '1234', 'Danny': 'qwert'}

username = input('Please enter username: ')
password = input('Please enter password: ')

if username not in data or data[username] != password:
    print('Password or username are WRONG!')
else:
    print('Permission GRANTED!')

