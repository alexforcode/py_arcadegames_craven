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
pygame.mouse.set_visible(0)   # прячем курсор

clock = pygame.time.Clock()

done = False
while done == False:

    # ---------- Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # ---------->>>>>>

    # ---------- Игровая логика 
    pos = pygame.mouse.get_pos()   # определяем позицию курсора
    mouse_x = pos[0]
    mouse_y = pos[1]
    # ---------->>>>>>
    
    # ---------- Рисование
    screen.fill(BLACK)

    drawChar(screen, mouse_x, mouse_y)   # отрисовываем char'а 

    pygame.display.flip()
    # ---------->>>>>>
    clock.tick(60)

pygame.quit()