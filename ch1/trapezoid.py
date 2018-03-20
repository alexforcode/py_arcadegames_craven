print('Area of a trapezoid')

height = int(input('Enter the height of the trapezoid: '))
bottomBase = int(input('Enter the length of the bottom base: '))
topBase = int(input('Enter the length of the top base: '))

areaTrapezoid = (bottomBase + topBase) * height / 2

print('The area is: {0}'.format(areaTrapezoid))