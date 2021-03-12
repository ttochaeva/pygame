import pygame
FPS = 500
clock = pygame.time.Clock()
m = 1
pygame.init()
screen = pygame.display.set_mode((800, 600))
x, y = 100, 100
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 50)
    if x + 50 == 800:
        m = -1
    if x == 50:
        m = 1
    x = x + m
    clock.tick(FPS)
    pygame.display.flip()
    pass

pygame.quit()
