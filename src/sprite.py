#!/usr/bin/env python
import pygame
class Sprite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.gravity = 1.15
	def update(self):
		pass

	def setPosition(self, xy, y=None):
		if y == None:
			(self.rect.left, self.rect.top) = xy
		else:
			self.rect.left = xy
			self.rect.top = y
	
	def getPosition(self):
		return self.rect.left,self.rect.top
		
	def setVelocity(self,xy,y=None):
		if y == None:
			(self.velx,self.vely) = xy
		else:
			self.velx = xy
			self.vely = y
		
	def getVelocity(self):
		return self.velx,self.vely
