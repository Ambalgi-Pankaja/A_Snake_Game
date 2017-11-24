# Snake Game!!!

import pygame, sys, random, time

# checking initialization for PyGame
check_errors = pygame.init()
# (6, 0)
if (check_errors[1] > 0):
    print("(!) Had {0} initializing errors, exiting....".format(check_errors[1]))
    sys.exit(-1)
else:
    print ("(+) PyGame initialized successfully!!")

# play surface
playSurface = pygame.display.set_mode((720,460))
pygame.display.set_caption('Snake_Game !!')

# Colors
red = pygame.Color(255, 0, 0) #gameover
green = pygame.Color(0, 255, 0) #snake
#blue = pygame.Color(0, 0, 255) #food
white = pygame.Color(255, 255, 255) #background
black = pygame.Color(0, 0, 0) #score
brown = pygame.Color(165, 42, 42) #food

#FPS Controller - Frame per second controller
fpsController = pygame.time.Clock()

snakePos = [100,50] #initial position
snakeBody = [[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,72)*10, random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changeTo = direction

score = 0
# Game over function
def gameOver():
    myFont = pygame.font.SysFont('calibri', 72)
    GOSurf = myFont.render('Game Over!', True, red)
    GOrect = GOSurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOSurf, GOrect)
    showScore(0)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit() #pygame quit
    sys.exit() #console exit

def showScore(choice):
    sFont = pygame.font.SysFont('calibri', 24)
    sSurf = sFont.render('Score: {0}'.format(score), True, black)
    sRect = sSurf.get_rect()
    if choice == 1:
        sRect.midtop = (80, 10)
    else:
        sRect.midtop = (360,120)
    playSurface.blit(sSurf, sRect)


# Main Logic of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeTo = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeTo = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeTo = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeTo = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

# validation of direction
    if changeTo == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeTo == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeTo == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

#changing direction update snake position
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()
    #Food Spawn
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10, random.randrange(1,46)*10]
    foodSpawn = True

    # Background fill
    playSurface.fill(white)

    #Draw Snake
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0],pos[1],10,10))

    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    #Boundry set up
    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()
    #Self eating
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    showScore(1)
    pygame.display.flip()
    fpsController.tick(25)