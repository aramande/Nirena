#!/usr/bin/env python

import sys
import pygame
from sprite import Sprite

pygame.init()

pygame.display.set_caption('Project 13')
size = width, height = 640,480
screen = pygame.display.set_mode(size)
sprite = Sprite("test.png","test")
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:sys.exit()