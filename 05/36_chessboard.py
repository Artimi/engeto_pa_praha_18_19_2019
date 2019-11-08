


size = int(input('Size: '))
white = input('White: ')

# assert len(white) == 1
if not len(white) == 1:
    print('AssertionError')
    exit()


characters = ' ' + white

for x in range(size):
    for y in range(size):
        print(characters[(x + y) % 2], end='')
    print()
