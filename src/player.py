#!/usr/bin/env python

import pygame
import sprite
from resources import load_image

class Player(sprite.Sprite):
	def __init__(self):
		sprite.Sprite.__init__(self)
		self.image = load_image('hero.png')
		self.rect = self.image.get_rect()
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		xoffset = (self.area.right - self.rect.left)/2
		yoffset = self.area.bottom - self.rect.centery
		self.direction = 1
		self.setPosition(xoffset, yoffset)
		self.flipped = False
		self.velx = 0
		self.vely = 0
		self.accy = 0
		self.normal = 0
		self.force = 0
		self.jumping = False
		
	def update(self):
		sprite.Sprite.update(self)
		tmpimage = self.image
		if tmpimage is not None:
			if self.flipped:
				tmpimage = pygame.transform.flip(tmpimage,1,0)
			self.image=tmpimage
		self.rect.left += self.velx
		self.vely += self.accy + self.gravity - self.normal
		self.rect.top += self.vely 
		self.accy = 0

	def processMovement(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT or \
			event.key == pygame.K_a:
				self.velx = -2
			elif event.key == pygame.K_RIGHT or \
			event.key == pygame.K_d:
				self.velx = +2
			elif event.key == pygame.K_UP or \
			event.key == pygame.K_w or \
			event.key == pygame.K_SPACE or \
			event.key == pygame.K_z:
				if not self.jumping:
					self.accy = -10.0
					self.jumping = True
			elif event.key == pygame.K_DOWN:
				pass
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				self.velx = 0
			elif event.key == pygame.K_RIGHT:
				self.velx = 0
			elif event.key == pygame.K_UP:
				self.accy = 0
			elif event.key == pygame.K_DOWN:
				pass
				
	def isCollidingWith(self, sprites, groups):
		self.normal = 0
		for sprite in sprites:
			if groups['ground'] in sprite.groups():
				if(self.vely > 0):
					self.vely = 0
					self.normal = sprite.force
					self.jumping = False