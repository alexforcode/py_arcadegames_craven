'''# I
class Animal():
    name = ''

    def __init__(self, name):
        self.name = name
        print('Animal is born!')

    def eat(self):
        print('Om nom!')

    def makeNoise(self):
        print(self.name, 'says: "GRRR!!!"')

# II
class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        print('Cat is born!')

    def makeNoise(self):
        print(self.name, 'says: "MEOW!!!"')

# III
class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        print('Dog is born!')

    def makeNoise(self):
        print(self.name, 'says: "WOOF!!!"')

# IV
snowflake = Cat('Snowflake')
rex = Dog('Rex')
hank = Dog('Hank')
balu = Animal('Balu')
snowflake.eat()
snowflake.makeNoise()
rex.eat()
rex.makeNoise()
hank.eat()
hank.makeNoise()
balu.eat()
balu.makeNoise()       '''