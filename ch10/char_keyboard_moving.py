import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

def drawChar(screen, x, y):
    pygame.draw.ellipse(screen, WHITE, (1+x, y, 10, 10), 0)   # голова
    pygame.draw.line(screen, WHITE, (5+x, 17+y), (10+x, 27+y), 2)   # ноги
    pygame.draw.line(screen, WHITE, (5+x, 17+y), (x, 27+y), 2)
    pygame.draw.line(screen, WHITE, (5+x, 17+y), (5+x, 7+y), 2)   # тело
    pygame.draw.line(screen, WHITE, (5+x, 7+y), (9+x, 17+y), 2)   # руки
    pygame.draw.line(screen, WHITE, (5+x, 7+y), (1+x, 17+y), 2)

pygame.init()

size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Char')

clock = pygame.time.Clock()

x_coord = 10
y_coord = 10
x_speed = 0
y_speed = 0

done = False
while done == False:

    # ---------- Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # изменяем скорость движения при нажатии кнопки
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3
        # изменяем скорость при отпускании кнопки
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0
    # ---------->>>>>>

    # ---------- Игровая логика 
    # передвинем объект в зависимости от скорости
    x_coord += x_speed 
    y_coord += y_speed
    # ---------->>>>>>
    
    # ---------- Рисование
    screen.fill(BLACK)

    drawChar(screen, x_coord, y_coord)   # отрисовываем char'а 

    pygame.display.flip()
    # ---------->>>>>>
    clock.tick(60)

pygame.quit()