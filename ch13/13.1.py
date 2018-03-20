import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLOCK_WIDTH = 20
BLOCK_HEIGHT = 15

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def resetPos(self):
        self.rect.y = random.randrange(-100, -10)
        self.rect.x = random.randrange(0, screen_width - BLOCK_WIDTH)

    def update(self):
        self.rect.y += 1
        if self.rect.y > screen_height:
            self.resetPos()

class Player(Block):
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.mouse.set_visible(0)

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK, BLOCK_WIDTH, BLOCK_HEIGHT)
    block.rect.x = random.randrange(screen_width - BLOCK_WIDTH)
    block.rect.y = random.randrange(screen_height - BLOCK_HEIGHT)
    block_list.add(block)
    all_sprites_list.add(block)

player = Player(RED, BLOCK_WIDTH, BLOCK_HEIGHT)
all_sprites_list.add(player)

clock = pygame.time.Clock()

score = 0
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    all_sprites_list.update()

    block_hit_list = pygame.sprite.spritecollide(player, block_list, False)

    for block in block_hit_list:
        score += 1
        block.resetPos()
        print(score)

    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()