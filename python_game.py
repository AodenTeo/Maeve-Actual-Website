# Import and initialize the pygame library

import pygame
import math
import random

pygame.init()

# Here you tell pygame about the screen size
screen = pygame.display.set_mode([800,600])
# Background 
background = pygame.image.load('background_sky.jpg')
# Title and icon
pygame.display.set_caption("Dragon wars")
unicorn = pygame.image.load('unicorn.png')
pygame.display.set_icon(unicorn)

# player
playerImg = pygame.image.load('fairy.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 9


for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('dragon.png')) 
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(10)
    enemyY_change.append(40)


# bullet

# ready means bullet is unseen
# fire means bullet has been fired and is visible

bulletImg = pygame.image.load('pointy_star.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 40
bullet_state = "ready"

# score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)



def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))

def game_over_text(x, y):
    over_text = over_font.render(("GAME OVER"), True, (0, 255, 255))
    screen.blit(over_text, (200, 250))
    
def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

# Here you tell pygame when the game should run
# Game Loop 
running = True 
while running : 
    screen.fill((0,255,255))
    # background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            running = False
         # if keystroke is pressed, check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                 playerX_change = -22 
            if event.key == pygame.K_RIGHT:
                 playerX_change = 22
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 playerX_change = 0
    
    playerX += playerX_change

    if playerX <=0 :
        playerX = 0
    elif playerX >= 736:
        playerX = 736 

    for i in range(num_of_enemies):
        # Game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text(200, 250)
            break  
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 15
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 735:
            enemyX_change[i] = -15
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 15
            print(score_value)
            enemyX[i] = random.randint(0,800)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i], enemyY[i], i)
    
     

    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire": 
        fire_bullet(bulletX, bulletY) 
        bulletY -= bulletY_change
    
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()


# Running pygame in the background even while not playing a game will use up battery, tell pygame to quit once the running loop is broken
pygame.quit()


