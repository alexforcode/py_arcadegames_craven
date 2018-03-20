# I
'''name = input('Введите ваше имя: ')
for i in range(10):
    print(name)
print('Готово')'''

# II
'''for i in range(20):
    print('Красный')
for j in range(20):
    print('Золотой')'''

# III
'''for i in range(2, 101, 2):
    print(i)'''

# V
'''a = 10
while a >= 0:
    print(a)
    a -= 1
print('Полетели')'''

# VI
'''print("Эта программа берёт три числа и возвращает их сумму.")
total = 0
for i in range(3):
    x = int(input("Введите число: "))
    total += x
print("Сумма:", total)'''

# VII
'''total, posit, negat, nil = 0, 0, 0, 0
for i in range(7):
    x = int(input('Введите число: '))
    total += x
    if x > 0:
        posit += 1
    elif x < 0:
        negat += 1
    else:
        nil += 1
print('Cумма:', total)
print('Вы ввели {0} положительных чисел, {1} отрицательных чисел и {2} нулей'.format(posit, negat, nil))'''