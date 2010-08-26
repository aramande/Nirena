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
	def update(self):
		sprite.Sprite.update(self)
		tmpimage = self.image
		if tmpimage is not None:
			if self.flipped:
				tmpimage = pygame.transform.flip(tmpimage,1,0)
			self.image=tmpimage
		self.rect.left += self.velx
		self.rect.top += self.vely

	def processMovement(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.velx = -1
			elif event.key == pygame.K_RIGHT:
				self.velx = +1
			elif event.key == pygame.K_UP:
				self.vely = -1
			elif event.key == pygame.K_DOWN:
				self.vely = +1
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				self.velx= 0
			elif event.key == pygame.K_RIGHT:
				self.velx= 0
			elif event.key == pygame.K_UP:
				self.vely= 0
			elif event.key == pygame.K_DOWN:
				self.vely= 0
