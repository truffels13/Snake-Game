# Snake Game
# 19.05.2017 - Ben Ralton
# Game of Snake created from Udemy course "Python Game Development: Creating a Snake Game from scratch by RobotLabs

import pygame, sys, random, time

check_errors = pygame.init()

if check_errors[1] > 0:
    print("(!) Had {0} initialising errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Success")

# Play Surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake!')

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)

fpsController = pygame.time.Clock()

snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
foodSpawn = True

direction = 'RIGHT'
changeTo = direction

score = 0


def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    gameOverSurface = myFont.render('Game Over!', True, red)
    gameOverRectangle = gameOverSurface.get_rect()
    gameOverRectangle.midtop = (360, 20)
    playSurface.blit(gameOverSurface, gameOverRectangle)
    showScore(2)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()  # pygame exit
    sys.exit()  # console exit


def showScore(choice=1):
    myFont = pygame.font.SysFont('monaco', 24)
    scoreSurface = myFont.render('Score : {0}'.format(score), True, black)
    scoreRectangle = scoreSurface.get_rect()
    if choice == 1:
        scoreRectangle.midtop = (80, 10)
    else:
        scoreRectangle.midtop = (360, 120)
    playSurface.blit(scoreSurface, scoreRectangle)


def gameOverConditions():
    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()

    for bodyBlock in snakeBody[1:]:
        if bodyBlock[0] == snakePos[0] and bodyBlock[1] == snakePos[1]:
            gameOver()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeTo = 'RIGHT'
            elif event.key == pygame.K_LEFT or event.key == ord('a'):
                changeTo = 'LEFT'
            elif event.key == pygame.K_UP or event.key == ord('w'):
                changeTo = 'UP'
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                changeTo = 'DOWN'
            elif event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    if changeTo == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    elif changeTo == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    elif changeTo == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    elif changeTo == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snakePos[0] += 10
    elif direction == 'LEFT':
        snakePos[0] -= 10
    elif direction == 'UP':
        snakePos[1] -= 10
    elif direction == 'DOWN':
        snakePos[1] += 10

    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        foodSpawn = False
        score += 1
    else:
        snakeBody.pop()

    if not foodSpawn:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True

    playSurface.fill(white)

    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    gameOverConditions()

    showScore()
    pygame.display.flip()

    fpsController.tick(24)
