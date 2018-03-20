# I
'''num = 9
for i in range(9):
    for j in range(i+1):
        num += 1
        print(num, end=" ")
    print()'''

# II
'''rows = int(input('Введите количество строк: '))
print()
for i in range(rows*2):
    print('o', end='')
print()
for i in range(rows-2):
    print('o', end='')
    for j in range(rows*2-2):
        print(' ', end='')
    print('o')
for i in range(rows*2):
    print('o', end='')
print()'''

# III
# ??????????????????????

# IV
'''import pygame
pygame.init()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Рисуем')

clock = pygame.time.Clock()

done = False

while done == False:
    # ловим событие закрытия окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    # отрисовываем сетку из квадратов
    x = 0
    for row in range(size[0]):
        y = 0
        for col in range(size[1]):
            pygame.draw.rect(screen, GREEN, (x, y, 5, 5))
            y += 10
        x += 10

    pygame.display.flip()   

    clock.tick(60)

pygame.quit()'''

