#!/usr/bin/env python

import sys
import pygame
import pygame.mixer
from pygame.locals import *
from sprite import *

pygame.init()

#window
screen = pygame.display.set_mode((640,480),0,32)
pygame.display.get_surface()
pygame.display.set_caption('Project 13')
pygame.display.flip()

#variables
clock = pygame.time.Clock()
sprite = Sprite("test.png","test")
hero = ("../data/sprites/hero.png")
heros = pygame.image.load(hero).convert_alpha()
bg = ("../data/background/background.jpg")
background = pygame.image.load(bg).convert()
x=0
y=0
velx = 0,0
vely = 0,0

#fps
clock.tick(60)


#loop
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()

	screen.blit(background, (0,0))
	screen.blit(heros,(x,y))

#updates screen
	pygame.display.update()

#movement
if event.type == pygame.KEYDOWN:
	    if event.key == 'K_LEFT':
	        velx = -1
	    elif event.key == 'K_RIGHT':
	        velx = +1
	    elif event.key == 'K_UP':
	        vely = -1
	    elif event.key == 'K_DOWN':
	        vely = +1
if event.type == pygame.KEYUP:
            if event.key == 'K_LEFT':
                velx= 0
            elif event.key == 'K_RIGHT':
                velx= 0
            elif event.key == 'K_UP':
                vely= 0
            elif event.key == 'K_DOWN':
                vely= 0

x+= velx
y+= vely
