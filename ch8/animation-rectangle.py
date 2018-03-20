import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Base Animation')

clock = pygame.time.Clock()

rect_x = 50
rect_y = 50
rect_change_x = 5
rect_change_y = 5

done = False
while done == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, (rect_x, rect_y, 50, 50))
    pygame.draw.rect(screen, RED, (rect_x+10, rect_y+10, 30, 30))
    if rect_x > 650 or rect_x < 0:
        rect_change_x *= -1
    if rect_y > 450 or rect_y < 0:
        rect_change_y *= -1
    rect_x += rect_change_x
    rect_y += rect_change_y

    pygame.display.flip()

    clock.tick(60)

pygame.quit()