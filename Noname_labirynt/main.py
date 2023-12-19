import pygame

pygame.init()
screen = pygame.display.set_mode((960, 768))
pygame.display.set_caption("Noname")
icon = pygame.image.load('bohater.png')
pygame.display.set_icon(icon)

# Gracz
playerImg = pygame.image.load('bohater.png')
playerX = 7*64
playerY = 11*64
playerX_change = 0
playerY_change = 0

# Labirynt
TILESIZE = 64
WIDTH = 15 * TILESIZE
HEIGHT = 12 * TILESIZE

wall = pygame.image.load('stone.png')

map = [
[1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
]

# Wynik
score_value = 0
font1 = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 52)
money = pygame.image.load('money.png')

textX = 10
testY = 10

def show_score(x, y):
    score = font1.render("Score : " + str(score_value), True, (255, 102, 0))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def check_collision(x, y):
    player_rect = pygame.Rect(x, y, TILESIZE, TILESIZE)

    for row in range(len(map)):
        for column in range(len(map[row])):
            if map[row][column] == 1:
                wall_rect = pygame.Rect(column * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE)
                if player_rect.colliderect(wall_rect):
                    return True 

    return False 

running = True
while running:
    screen.fill((0, 51, 51))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rysowanie labiryntu
    for row in range(len(map)):
        for column in range(len(map[row])):
            if map[row][column] == 1:
                screen.blit(wall, (column * TILESIZE, row * TILESIZE))
            if map[row][column] == 2:
                screen.blit(money, (column * TILESIZE, row * TILESIZE))    
    
    # Poruszanie się gracza
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerX > 0 and not check_collision(playerX - 1, playerY):
        playerX -= 2
    if keys[pygame.K_RIGHT] and playerX < WIDTH - TILESIZE and not check_collision(playerX + 1, playerY):
        playerX += 2
    if keys[pygame.K_UP] and playerY > 0 and not check_collision(playerX, playerY - 1):
        playerY -= 2
    if keys[pygame.K_DOWN] and playerY < HEIGHT - TILESIZE and not check_collision(playerX, playerY + 1):
        playerY += 2
    
    # Punkty
    if map[playerY // TILESIZE][playerX // TILESIZE] == 2:
        map[playerY // TILESIZE][playerX // TILESIZE] = 0
        score_value += 1

    player(playerX, playerY)
    show_score(textX, testY)
    
    # Koniec gry
    endgame = pygame.image.load('endgame.png')
    if map[playerY // TILESIZE][playerX // TILESIZE] == 3: 
      screen.blit(endgame, (0, 0))
      end1 = font2.render("WYSZEDŁEŚ Z KOPALNI!", True, (255, 255, 255))
      end2 = font2.render("GRATULACJE!", True, (255, 255, 255))
      screen.blit(end1, (190, 300))
      screen.blit(end2, (270, 380))

    pygame.display.update()