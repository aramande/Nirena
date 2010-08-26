#!/usr/bin/env python

import sys
import pygame
import pygame.mixer
import player
import ground
from pygame.locals import *
from resources import load_image

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption('Project 13')

#variables
groups = {}
clock = pygame.time.Clock()
player = pygame.sprite.GroupSingle(player.Player())
player.sprite.setPosition(100,100)
groups['player'] = player
render = pygame.sprite.RenderPlain()
render.add(player)
background = load_image("background.jpg")
ground = pygame.sprite.GroupSingle(ground.Ground())
groups['ground'] = ground
render.add(ground)
while True:
	pygame.event.pump()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:sys.exit()
		player.sprite.processMovement(event)
       	#fps
	clock.tick(60)
	player.sprite.isCollidingWith(pygame.sprite.spritecollide(player.sprite, ground, False), groups)

	screen.blit(background, (0,0))
	player.update()
	render.draw(screen)
	#updates screen
	pygame.display.update()

