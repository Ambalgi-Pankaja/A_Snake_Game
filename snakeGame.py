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
play_surface = pygame.display.set_mode((720,460))
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