import pygame
FPS = 500
m = 1

class Ball():
    def __init__(self, pas):
        self.x = pas[0]
        self.y = pas[1]
        self.color = (255, 255, 0)
        self.r = 50
        self.m = 1
        self.step_x = 0
        self.step_y = 0


    def move(self):
        self.x += self.step_x
        self.y += self.step_y

    def change_dir(self, x, y):
        self.step_x = x
        self.step_y = y
        if self.x + 50 == 800:
            self.m = -1
        if self.x == 50:
            self.m = 1
        self.x = self.x + self.m


    def update(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((800, 600))
x, y = 100, 100
running = True
first_ball = Ball((100, 100))
first_ball.change_dir(1, 0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    first_ball.update()
    first_ball.move()
    if first_ball.x + first_ball.r == 800 or first_ball.x == first_ball.r:
        first_ball.change_dir(-first_ball.step_x,0)

    clock.tick(FPS)
    pygame.display.flip()
    pass

pygame.quit()
