import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

pygame.init() 

screen = pygame.display.set_mode([700, 500])
pygame.display.set_caption('First Game')
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
    screen.fill(BLACK)

    pygame.display.flip() 
    # ---------->>>>>>
    clock.tick(60)

pygame.quit()