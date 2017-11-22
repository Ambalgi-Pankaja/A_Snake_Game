# Snake Game!!!

import pygame, sys, random, time

check_errors = pygame.init()
# (6, 0)
if (check_errors[1] > 0):
    print("(!) Had {0} initializing errors, exiting....".format(check_errors[1]))
    sys.exit(-1)
else:
    print ("(+) PyGame initialized successfully!!")