String01 = 'Bratislava'
String02 = 'Budapest'

print('Common characters:', set(String01) & set(String02))
print('Unique characters:', set(String01) - set(String02))