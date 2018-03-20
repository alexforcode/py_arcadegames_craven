import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

class Ball():
    
    coord_x = 0
    coord_y = 0
    change_x = 0
    change_y = 0
    size = 10
    color = WHITE
    
    def move(self):
        self.coord_x += self.change_x
        self.coord_y += self.change_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.coord_x, self.coord_y), self.size)

pygame.init()

theBall = Ball()
theBall.coord_x = 100
theBall.coord_y = 100
theBall.change_x = 2
theBall.change_y = 1

screen = pygame.display.set_mode([700, 500])
pygame.display.set_caption('Ball')
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

    theBall.move()
    theBall.draw(screen)

    pygame.display.flip() 
    # ---------->>>>>>
    clock.tick(60)

pygame.quit()