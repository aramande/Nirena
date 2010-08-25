#!/usr/bin/env python

import sys
import pygame
import pygame.mixer

pygame.init()

#variables
clock = pygame.time.Clock()

#window
pygame.display.set_caption('Project 13')
size = width, height = 640,480
screen = pygame.display.set_mode(size)

#loop
while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()
#fps        
        clock.tick(60)
