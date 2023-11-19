import pygame
import sys

class GameObject:
    def __init__(self, image, x, y):
        self.image = image
        self.pos = self.image.get_rect(topleft=(x, y))
pygame.init()

clock = pygame.time.Clock()  
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
player = pygame.image.load("bohater.png")
coin = pygame.image.load("moneta.png")
heart = pygame.image.load("serce.png")
time = pygame.image.load("czas.png")

# Pozycja gracza
player_x = 50
player_y = 50
p = GameObject(player, player_x, player_y)  
t = GameObject(time, 700, 0)


objects = []
for x in range(3):  
    o = GameObject(heart, x * 30, x)
    objects.append(o)

for x in range(3):  
    c = GameObject(coin, 300+x*100, 500)
    objects.append(c)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill((255, 255, 255))

    for o in objects:
        screen.blit(o.image, o.pos)
    screen.blit(p.image, p.pos)
    screen.blit(t.image, t.pos)
    for c in objects: screen.blit(c.image, c.pos)
    screen.blit(player, (player_x, player_y))
    pygame.display.flip()
    


    