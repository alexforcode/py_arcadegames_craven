import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

def recursiveDraw(screen, x, y, width, height, count):

    pygame.draw.line(screen, BLACK, (x+width*.25, y+height//2),(x+width*.75, y+height//2), 3)
    pygame.draw.line(screen, BLACK, (x+width*.25, y+(height*.5)//2),(x+width*.25, y+(height*1.5)//2), 3)
    pygame.draw.line(screen, BLACK, (x+width*.75, y+(height*.5)//2),(x+width*.75, y+(height*1.5)//2), 3)

    if count > 0:
        count -= 1
        recursiveDraw(screen, x, y, width//2, height//2, count)
        recursiveDraw(screen, x+width//2, y, width//2, height//2, count)
        recursiveDraw(screen, x, y+width//2, width//2, height//2, count)
        recursiveDraw(screen, x+width//2, y+width//2, width//2, height//2,count)

pygame.init() 

screen = pygame.display.set_mode([700, 700])
pygame.display.set_caption('Simple Fractal')
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

    fractal_level = 5
    recursiveDraw(screen, 0, 0, 700, 700, fractal_level)

    pygame.display.flip() 
    # ---------->>>>>>
    clock.tick(60)

pygame.quit()