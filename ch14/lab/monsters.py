import random

class Monster():
    char_type = ''
    hit_points = 0

    def print(self):
        print('Monster: {0}. Hit Points: {1}'.format(self.char_type, self.hit_points))

class Goblin(Monster):
    def __init__(self):
        self.char_type = 'Goblin'
        self.hit_points = random.randrange(5, 10)

class Orc(Monster):
    def __init__(self):
        self.char_type = 'Orc'
        self.hit_points = random.randrange(15, 30)