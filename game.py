import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

# num_box
# num_box = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

#Title and icon
pygame.display.set_caption('DeadGlory')
icon = pygame.image.load('vg.png')
pygame.display.set_icon(icon)

# character
playerMain = pygame.image.load('mario.png')
playerX = 370
playerY = 536
player_x_change = 0
player_y_change = 0

# Enemy
playerEnemy = pygame.image.load('spider.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemy_x_change = 0.3
enemy_y_change = 0


def player(x, y):
    screen.blit(playerMain, (x, y))


def enemy(x, y):
    screen.blit(playerEnemy, (x, y))


# Gameloop
running = True
while running:
    screen.fill((255, 120, 120))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.4
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.4
            if event.key == pygame.K_UP:
                player_y_change = -0.4
            if event.key == pygame.K_DOWN:
                player_y_change = 0.4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
                player_y_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_x_change = 0
                player_y_change = 0
        if event.type == pygame.QUIT:
            running = False
    playerX += player_x_change
    playerY += player_y_change

    if playerX <= 0:
        playerX = 0
    if playerY <= 0:
        playerY = 0
    if playerX >= 736:
        playerX = 736
    if playerY >= 536:
        playerY = 536

    # # Enemy no borders
    # if enemyX <= 0:
    #     enemyX += 5
    # if enemyY <= 0:
    #     enemyY = 0
    # if enemyX >= 736:
    #     enemyX = enemyX-800
    # if enemyY >= 536:
    #     enemyY = 536
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
