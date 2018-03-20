import random

# I
'''print(random.randrange(1, 11))'''

# II
'''for i in range(10):
    print(random.random() * 10 + 1)'''

# III
'''heads, tails = 0, 0
for i in range(50):
    choice = random.choice([0, 1])
    if choice == 0:
        print('орел')
        heads += 1
    else:
        print('решка')
        tails += 1
print('Решка: {0}, орел: {1}'.format(tails, heads))'''

# IV
'''user_choice = int(input('Ваш выбор (камень - 1, ножницы - 2, бумага - 3): '))
comp_choice = random.choice([1, 2, 3])
if comp_choice == 1:
    print('Компьютер выбрал камень')
elif comp_choice == 2:
    print('Компьютер выбрал ножницы')
else:
    print('Компьютер выбрал бумагу')
if user_choice == comp_choice:
    print('Ничья')
elif (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 3) or (user_choice == 3 and comp_choice == 1):
    print('Вы выиграли!')
else:
    print('Вы проиграли!')'''
