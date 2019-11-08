

start = int(input('START: '))
stop = int(input('STOP: ')) + 1
divisor = int(input('DIVISOR: '))

if divisor == 0:
    print('Cannot divide by zero')
    exit()

divided = []
for i in range(start, stop):
    if i % divisor == 0:
        divided.append(i)

# f-strings
print(f'Numbers in range({start:.3f}, {stop}), divisible by {divisor}:')
print(divided)
