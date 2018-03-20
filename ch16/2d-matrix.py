import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
WIDTH = 20
HEIGHT = 20
MARGIN = 5

grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)

pygame.init() 

screen = pygame.display.set_mode([255, 255])
pygame.display.set_caption('Matrix')
clock = pygame.time.Clock()

done = False
while not done:
    # ---------- Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = int(pos[0]/(WIDTH+MARGIN))
            row = int(pos[1]/(HEIGHT+MARGIN))
            print("Click:", pos, "Grid coordinates:", row+1, column+1)
            grid[row][column] = 1
    # ---------->>>>>>
    # ---------- Игровая логика 
    
    # ---------->>>>>   
    # ---------- Рисование
    screen.fill(BLACK)

    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen, color, ((MARGIN + WIDTH) * column + MARGIN, (MARGIN + WIDTH) * row + MARGIN, WIDTH, HEIGHT))

    pygame.display.flip() 
    # ---------->>>>>>
    clock.tick(60)

pygame.quit()