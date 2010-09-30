#!/usr/bin/env python

import sys
import pygame
import pygame.mixer
import player
import ground
import nose
import optparse
from pygame.locals import *
from resources import load_image
from settings import *

def rungame():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,SCREEN_DEPTH)
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
	s_ground = ground.Ground()
	s_slope = ground.Slope()
	g_ground = pygame.sprite.GroupSingle(s_ground)
	g_slope = pygame.sprite.GroupSingle(s_slope)
	solid_obstacles = pygame.sprite.Group((s_ground, s_slope)) #Do not remove paranthesis 
	groups['ground'] = g_ground
	groups['slope'] = g_slope
	groups['solid_obstacles'] = solid_obstacles
	render.add(g_ground)
	render.add(g_slope)
	PHYSICS = 0.1
	
#mainloop
	while True:
		pygame.event.pump()
		for event in pygame.event.get():
			#Testing for various exit signals from the user
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()
			hero.sprite.processMovement(event)
			
		hero.sprite.isCollidingWith(pygame.sprite.spritecollide(hero.sprite, solid_obstacles, False), groups)
		hero.update(clock.get_time())	
		screen.blit(background, (0,0))
		render.draw(screen)
		pygame.display.update()
		pygame.display.flip()
		clock.tick(FPS)

#testing
p = optparse.OptionParser()
p.add_option('--test', '-t', action ='store_true', help='run the game through all tests')
options, arguments = p.parse_args()
if options.test == True:
	temp_argv = sys.argv
	sys.argv = [sys.argv[0]]
	nose.main()
	sys.argv = temp_argv
else:
	rungame()