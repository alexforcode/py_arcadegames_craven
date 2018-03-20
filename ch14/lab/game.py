from monsters import *
import random

monster_list = []
for i in range(10):
    if bool(random.getrandbits(1)):
        monster = Goblin()
    else:
        monster = Orc()
    monster_list.append(monster)

for monster in monster_list:
    monster.print()