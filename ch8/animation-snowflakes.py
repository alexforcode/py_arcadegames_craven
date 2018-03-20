import pygame, random
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Base Animation')

snow_list = []
# добавляем 100 позиций [x, y] снежинок в список
for i in range(100):
    x = random.randrange(0, 700)
    y = random.randrange(0, 500)
    snow_list.append([x, y])

clock = pygame.time.Clock()

rect_x = 50
rect_y = 50
rect_change_x = 5
rect_change_y = 5

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    # для каждой снежиник из списка
    for i in range(len(snow_list)):
        # отрисовываем снежинку из списка
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        # двигаем снежинку на один пикс вниз
        snow_list[i][1] += 1
        # если вышла за экран снизу
        if snow_list[i][1] > 500:
            # двигаем снежинку за экран сверху
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # новая позиция по оси x
            x = random.randrange(0, 700)
            snow_list[i][0] = x       

    pygame.display.flip()

    clock.tick(40)

pygame.quit()