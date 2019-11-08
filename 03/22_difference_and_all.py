String01 = 'Bratislava'
String02 = 'Budapest'

print('Different characters:',
      set(String01) ^ set(String02))
print('All characters:',
      set(String01) | set(String02))
