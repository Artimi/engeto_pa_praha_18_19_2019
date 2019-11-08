import math

a_x = int(input('Point A, X Coordinate: '))
if a_x < 0:
    print('Cannot accept negative number')

a_y = int(input('Point A, Y Coordinate: '))
if a_y < 0:
    print('Cannot accept negative number')

b_x = int(input('Point B, X Coordinate: '))
if b_x < 0:
    print('Cannot accept negative number')

b_y = int(input('Point B, Y Coordinate: '))
if b_y < 0:
    print('Cannot accept negative number')

distance = math.sqrt(abs(a_x - b_x) ** 2 + abs(a_y - b_y) ** 2)
print('The distance between the points A and B is', round(distance, 2))
