import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('Planes!')
clock = pygame.time.Clock()

screen_color = pygame.Surface((1600, 900))
screen_color.fill('lightblue')

# functions:

def createGameGrid(rows, cols, cellsize, pos):
    """Creates a game grid with coordinates for each cell"""
    startX = pos[0]
    startY = pos[1]
    coordGrid = []
    for row in range(rows):
        rowX = []
        for col in range(cols):
            rowX.append((startX, startY))
            startX += cellsize
        coordGrid.append(rowX)
        startX = pos[0]
        startY += cellsize
    return coordGrid

# game variables

rows = 10
cols = 10
cellsize = 61

pGameGrid = createGameGrid(rows, cols, cellsize, (50, 50))
pGameLogic = None

cGameGrid = createGameGrid(rows, cols, cellsize, (1600 - (rows * cellsize), 50))
cGameLogic = None

for _ in pGameGrid:
    print(_)

while True:
    # checking to close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(screen_color, (0, 0))

    pygame.display.update()
    clock.tick(60)
