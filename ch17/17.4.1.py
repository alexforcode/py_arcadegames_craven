# I
'''for i in range(10):
    print('*', end=' ')'''

# II
'''for i in range(10):
    for j in range(10):
        print('*', end=' ')
    print()'''

# III
'''zero_list = []
for i in range(100):
    zero_list.append(0)
print(len(zero_list))
print(zero_list)'''

# VI
'''def num_print(num):
    print(num)
# VII
num_print(7)'''

# VIII
'''def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3
print(average(10, 28, 15))'''

# IX
'''class Ball():
    coord_x = 0
    coord_y = 0
    speed = 0
    
    def __init__(self, x, y, speed):
        self.coord_x = x
        self.coord_y = y
        self.speed = speed

    def update(self):
        self.coord_x += self.speed 
        self.coord_y += self.speed

newBall = Ball(0, 0, 15)
for i in range(10):
    print('x: {0}, y: {1}'.format(newBall.coord_x, newBall.coord_y))
    newBall.update()
print('x: {0}, y: {1}'.format(newBall.coord_x, newBall.coord_y))'''