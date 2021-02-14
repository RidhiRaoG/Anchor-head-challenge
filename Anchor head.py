import pygame
from random import randint
import time
from pygame.locals import *
for i in range(1000):
    location = 4
    distance = 0
    reached = 0
    fall = 0
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Drawing Rectangles")
    pos_x = 237
    pos_y = 159
    pos_y2 = 590
    pos_x2 = 300.5
    color = 255, 255, 0
    color1 = 115, 0, 10
    width = 0  # solid fill
    pos = pos_x, pos_y, 137, 441
    pos1 = pos_x2, pos_y2, 10, 10

    def move_on_screen(coordinate, direction = 0):
        global pos1
        global pos_y2
        global pos_x2
        pygame.draw.rect(screen, color, pos, width)
        pygame.draw.rect(screen, color1, pos1, width)
        pygame.display.update ()
        time.sleep(1)
        if coordinate == "y":
            pos_y2 -= 21
            pos1 = pos_x2, pos_y2, 10, 10
        else:
            if direction == 0:
                pos_x2 -= 21
                pos1 = pos_x2, pos_y2, 10, 10
            else:
                pos_x2 += 21
                pos1 = pos_x2, pos_y2, 10, 10
        pygame.draw.rect(screen, color1, pos1, width)
        pygame.display.update()

    while distance < 21:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                sys.exit()
        screen.fill((0, 0, 200))
        distance += 1
        print(distance)
        move_on_screen("y")
        pygame.display.update()
        n = randint(0, 1)
        print("Random generated number is ",n)
        if n == 0:
            location -= 1
        elif n == 1:
            location += 1
        move_on_screen("x", direction = n)
        if location < 1 or location > 7:
            location = 4
            distance = 0
            fall += 1
            pos_x2= 300.5
            pos_y2= 590

    reached += 1
    print (reached/(reached+fall), "is the probability of success.")