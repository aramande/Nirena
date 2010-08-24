#!/usr/bin/python

import sys
import pygame

pygame.init()

pygame.display.set_caption('Project 13')
size = width, height = 600,400
screen = pygame.display.set_mode(size)

while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()