import pygame

pygame.init()

class Bohater:
    def __init__(self, x, y):
        # Inicjalizacja bohatera
        self.x = x  # pozycja x bohatera
        self.y = y  # pozycja y bohatera
        self.width = 50  # szerokość bohatera
        self.height = 50  # wysokość bohatera
        self.speed = 5  # prędkość poruszania się bohatera
        self.image = pygame.image.load("Bohater.png") # obrazek bohatera

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

    def draw(self, screen): #screen to okno gry
        screen.blit(self.image, (self.x, self.y))

pygame.quit()

