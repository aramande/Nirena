#!/usr/bin/env python

import sys
import pygame
import pygame.mixer
import player
from pygame.locals import *
from resources import load_image

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption('Project 13')

#variables
clock = pygame.time.Clock()
player = pygame.sprite.GroupSingle(player.Player())
render = pygame.sprite.RenderPlain()
render.add(player)
#background = load_image("background.jpg")
player.sprite.setPosition(100,100)
#loop
while True:
	pygame.event.pump()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:sys.exit()
		#player.sprite.processMovement(event)
		player.sprite.processMovement(event)

	#screen.blit(background, (0,0))
	player.update()
	render.draw(screen)
	#updates screen
	pygame.display.update()
	#fps
	clock.tick(60)

