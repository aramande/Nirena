#!/usr/bin/env python

import sys
import pygame
import pygame.mixer
import player

pygame.init()

#window
pygame.display.set_caption('Project 13')
size = width, height = 640,480
screen = pygame.display.set_mode(size)

#variables
clock = pygame.time.Clock()
player = pygame.sprite.GroupSingle(player.Player())
render = pygame.sprite.RenderPlain()
render.add(player)

while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:sys.exit()
		player.update()
		render.draw(screen)
		pygame.display.flip()
		#fps
		clock.tick(60)
