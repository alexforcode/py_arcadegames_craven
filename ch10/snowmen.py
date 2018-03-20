import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

def drawSnowman(screen, x, y):
    pygame.draw.ellipse(screen, WHITE, (35+x, 0+y, 25, 25))
    pygame.draw.ellipse(screen, WHITE, (23+x, 20+y, 50, 50))
    pygame.draw.ellipse(screen, WHITE, (0+x, 65+y, 100, 100))

size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Snowmen')

clock = pygame.time.Clock()

done = False
while done == False:

    # ---------- Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # ---------->>>>>>

    # ---------- Игровая логика 
    
    # ---------->>>>>>
    
    # ---------- Рисование
    screen.fill(BLACK)

    drawSnowman(screen, 10, 10)
    drawSnowman(screen, 300, 10)
    drawSnowman(screen, 10, 300)

    pygame.display.flip()
    # ---------->>>>>>
    clock.tick(60)

pygame.quit()