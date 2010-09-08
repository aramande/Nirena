#!/usr/bin/env python

import sys
import pygame
import pygame.mixer
import player
import ground
import nose
from pygame.locals import *
from resources import load_image

def rungame():
	pygame.init()
	screen = pygame.display.set_mode((640,480),0,32)
	pygame.display.set_caption('Project 13')

	#variables
	groups = {}
	clock = pygame.time.Clock()
	hero = pygame.sprite.GroupSingle(player.Player())
	hero.sprite.setPosition(100,100)
	groups['player'] = player
	render = pygame.sprite.RenderPlain()
	render.add(hero)
	background = load_image("background.jpg")
	g_ground = pygame.sprite.GroupSingle(ground.Ground())
	groups['ground'] = g_ground
	render.add(g_ground)
	while True:
		pygame.event.pump()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()
			hero.sprite.processMovement(event)
			
		hero.sprite.isCollidingWith(pygame.sprite.spritecollide(hero.sprite, g_ground, False), groups)
		screen.blit(background, (0,0))
		hero.update(clock.get_time())
		render.draw(screen)
		#updates screen
		pygame.display.update()
		clock.tick(60)
		
if "-t" in sys.argv or "--test" in sys.argv:
	nose.run()
else:
	rungame()