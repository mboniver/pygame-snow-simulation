import pygame
import random
pygame.init()
pygame.display.set_caption("Snow Simulation")

class Config:
    W, H = 800, 600
    window = pygame.display.set_mode((W,H))
    is_run = True
    fps_cap = 30
    mouse_pos = (-100,-100)

class Colors:
    BLACK = (0, 0, 0)
    SKY = (15, 20, 45)
    BLUE = (0, 0, 90)

class Snowflake:
    def __init__(self, x, y, r, s=1):
        self.x =x
        self.y =y
        self.r =r
        self.speed= s
        self.Color= Colors.BLUE
        self.set_color()
        self.set_wind()

    def fall(self):
        self.y += self.speed
        if random.random()<0.30:
            self.x += self.wind
        if random.random()<0.050:
            self.set_wind()

    def draw(self) :
        pygame.draw.circle(Config.window, self.color, (self.x, self.y), self.r)   

    def set_wind(self):
        self.wind = random.random() * random.randint(-1,1)*2
    def set_color(self):
        self.color = (50, 50, random.randint(60, 255))

    def fall_logic(self):
        if self.y-self.r > Config.H:
            self.y = -self.r -  random.randint(0, 100)
            self.x = random.randint(0, Config.W)
            self.speed =1+random.random()*3
            self.set_color()

mass_balls :list[Snowflake]=[]

for i in range(random.randint(10,30)):
    x = random.randint(0, Config.W)
    y = random.randint(-200, -10)
    s = 1+random.random()*3
    r = random.randint(2,10)
    new_b = Snowflake(x,y,r, s)
    mass_balls.append(new_b)


fps_clock = pygame.time.Clock()
frames = 0
while Config.is_run:
    fps_clock.tick(Config.fps_cap)
    frames += 1

    Config.window.fill(Colors.SKY)

    for b in mass_balls:
        b.fall()
        b.fall_logic()
        b.draw()

    pygame.draw.circle(Config.window, (255,0,0), Config.mouse_pos, 30, 2)    
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Config.is_run = False

        if event.type == pygame.MOUSEMOTION:
            Config.mouse_pos = pygame.mouse.get_pos()


pygame.quit()