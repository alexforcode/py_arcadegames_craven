import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

def recursiveDraw(screen, x, y, width, height):
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 1)
    # ограничение рекурсии рисования прямоугольника
    if (width > 14):
        x += width * .1
        y += height * .1
        width *= .8
        height *= .8
        recursiveDraw(screen, x, y, width, height)

pygame.init() 

screen = pygame.display.set_mode([700, 500])
pygame.display.set_caption('Recursive Rectangle')
clock = pygame.time.Clock()

done = False
while not done:
    # ---------- Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # ---------->>>>>>
    # ---------- Игровая логика 
    
    # ---------->>>>>   
    # ---------- Рисование
    screen.fill(WHITE)

    recursiveDraw(screen, 0, 0, 700, 500)

    pygame.display.flip() 
    # ---------->>>>>>
    clock.tick(60)

pygame.quit()