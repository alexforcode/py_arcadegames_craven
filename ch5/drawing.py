import pygame

pygame.init()   # запуск pygame

# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

PI = 3.141592653   # Пи

size = [700, 500]   # размер окна
screen = pygame.display.set_mode(size)

pygame.display.set_caption('First Game')   # заголовок окна

clock = pygame.time.Clock()   # контроль частоты обновления экрана
font = pygame.font.Font('6865_0.ttf', 36)   # стандартный шрифт для отрисовки, 25 размера

done = False
while done == False:

    # ---------- Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # если игрок нажал закрыть
            done = True   # флаг для выхода из цикла
    # ---------->>>>>>

    # ---------- Игровая логика 
    
    # ---------->>>>>>
    
    # ---------- Рисование
    screen.fill(WHITE)   # установить фон
    # рисование линии (pygame.org/docs/ref/draw.html#pygame.draw.line)
    # for x in range(0, 100, 10):
    #     pygame.draw.line(screen, BLACK, (0, 10+x), (100, 110+x), 5)
    # рисование прямоугольника (pygame.org/docs/ref/draw.html#pygame.draw.rect)
    # pygame.draw.rect(screen, BLACK, (20, 20, 250, 100), 2)
    # рисование эллипса (pygame.org/docs/ref/draw.html#pygame.draw.ellipse)
    # pygame.draw.ellipse(screen, BLACK, (20, 20, 250, 100), 0)
    # рисование дуги (pygame.org/docs/ref/draw.html#pygame.draw.arc)
    # pygame.draw.arc(screen, BLACK, (20, 20, 250, 100), PI/2, PI, 2)
    # pygame.draw.arc(screen, RED, (20, 20, 250, 100), 0, PI/2, 2)
    # pygame.draw.arc(screen, BLACK, (20, 20, 250, 100), 3*PI/2, 2*PI, 2)
    # pygame.draw.arc(screen, GREEN, (20, 20, 250, 100), PI, 3*PI/2, 2)
    # рисование многоугольника (pygame.org/docs/ref/draw.html#pygame.draw.polygon)
    # pygame.draw.polygon(screen, RED, [(200, 50), (100, 100), (200, 200)], 2)
    # отрисовка текста (pygame.org/docs/ref/font.html#pygame.font.Font)
    stamp = font.render('Score: '+str(1150082), True, BLACK)   # картинка с текстом для отрисовки
    screen.blit(stamp, (300, 200))   # отрисовка на экране

    pygame.display.flip()   # обновить экран, показать результат рисования 
    # ---------->>>>>>
    clock.tick(60)   # 20 кадров в секунду

pygame.quit()   # завершение pygame