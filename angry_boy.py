import pygame
from pygame.draw import *
from variables import *

pygame.init()


def angry_boy(screen):
    # Main screen where we draw

    screen.fill(gray)  # Changing of color of main screen

    circle(screen, yellow, (250, 250), 100)

    # Drawing left eye
    circle(screen, black, (200, 210), 16, 1)
    circle(screen, some_red, (200, 210), 15)
    circle(screen, black, (200, 210), 5)

    # Drawing right eye
    circle(screen, black, (300, 210), 16, 1)
    circle(screen, some_red, (300, 210), 15)
    circle(screen, black, (300, 210), 5)

    # Draw mouth
    rect(screen, black, (200, 310, 100, 15))

    # Draw eyebrow
    polygon(screen, black, [[225, 200], [235, 190], [165, 115], [150, 125]])
    polygon(screen, black, [[275, 200], [265, 190], [335, 115], [350, 125]])

