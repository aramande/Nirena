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

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,SCREEN_DEPTH)
stop_splash = False
#Sprites
hero = pygame.sprite.GroupSingle(player.Player())

#Tiles
s_ground = ground.Ground()
s_slope = ground.Slope()

#Groups
g_ground = pygame.sprite.GroupSingle(s_ground)
g_slope = pygame.sprite.GroupSingle(s_slope)
solid_obstacles = pygame.sprite.Group((s_ground, s_slope)) #Do not remove paranthesis

groups = {}
groups['player'] = player
groups['slope'] = g_slope
groups['solid_obstacles'] = solid_obstacles

def input():
	pygame.event.pump()
	for event in pygame.event.get():
		exitsignals(event)	
	
def skipsplash():
	pygame.event.pump()
	for event in pygame.event.get():
		exitsignals(event)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				return True
	return False
	
def playerinput():
	pygame.event.pump()
	for event in pygame.event.get():
		hero.sprite.processMovement(event)
		exitsignals(event)
	
def exitsignals(event):
	if event.type == pygame.QUIT:
		sys.exit()
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_ESCAPE:
			sys.exit()
			

def splash():
	clock = pygame.time.Clock()
	time = pygame.time.get_ticks()
	background = load_image("hacksplash.png")
	while True:
		if skipsplash():
			return
		if time+5000 <= pygame.time.get_ticks() or stop_splash:
			#Stop showing after 5 seconds
			return
		screen.blit(background, (0,0))
		pygame.display.update()
		pygame.display.flip()
		clock.tick(FPS/2)

def mainloop():
	clock = pygame.time.Clock()
	background = load_image("background.jpg") 
	render = pygame.sprite.RenderPlain()
	render.add(hero)
	render.add(g_slope)
	while True:
		playerinput()
		hero.sprite.isCollidingWith(pygame.sprite.spritecollide(hero.sprite, solid_obstacles, False), groups)
		hero.update(clock.get_time())
		screen.blit(background, (0,0))
		render.draw(screen)
		pygame.display.update()
		pygame.display.flip()
		clock.tick(FPS)

def rungame():
	pygame.init()
	pygame.display.set_caption('Project 13')

	hero.sprite.setPosition(100,100)
	##	groups['ground'] = g_ground
	##	render.add(g_ground)
	PHYSICS = 0.1
	splash()
	mainloop()
	
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