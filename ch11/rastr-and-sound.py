import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('My Game')
pygame.mouse.set_visible(0)
clock = pygame.time.Clock()
# загрузить графику
back_image = pygame.image.load('sources/back.jpg').convert()
player_image = pygame.image.load('sources/ship.png').convert()
player_image.set_colorkey(BLACK)   # сделать заданный цвет прозрачным
# загрузить звуки
lazer_shot = pygame.mixer.Sound('sources/lazer.wav')
done = False
while not done:
    # ---------- Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            lazer_shot.play()
    # ---------->>>>>>
    # ---------- Игровая логика 
    player_pos = pygame.mouse.get_pos()
    mouse_x = player_pos[0]
    mouse_y = player_pos[1]
    # ---------->>>>>>    
    # ---------- Рисование
    screen.blit(back_image, (0, 0))       
    screen.blit(player_image, (mouse_x, mouse_y))
    pygame.display.flip() 
    # ---------->>>>>>
    clock.tick(60)

pygame.quit()