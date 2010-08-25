#!/usr/bin/env python

import sprite
import pygame
from resources import load_image

class Player(sprite.Sprite):
	def __init__(self):
		sprite.Sprite.__init__(self)
		self.image = load_image('player.png')
		self.rect = self.image.get_rect()
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		xoffset = (self.area.right - self.rect.left)/2
		yoffset = self.area.bottom - self.rect.centery
		self.direction = 1
		self.setPosition(xoffset, yoffset)
		self.flipped = False
	def update(self):
		sprite.Sprite.update(self)
		tmpimage = self.image
		if tmpimage is not None:
			if self.flipped:
				tmpimage = pygame.transform.flip(tmpimage,1,0)
			self.image=tmpimage
		self.rect.center = self.getPosition()
		self.processMovement()

	def processMovement(self):
		pass
