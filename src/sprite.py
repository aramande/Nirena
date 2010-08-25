#!/usr/bin/env python
import pygame
class Sprite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.x = 0
		self.y = 0

	def update(self):
		pass

	def setPosition(self, xy, y=None):
		if y == None:
			(self.x,self.y) = xy
		else:
			self.x = xy
			self.y = y
	
	def getPosition(self):
		return self.x,self.y
		
	def setVelocity(self,xy,y=None):
		if y == None:
			(self.velx,self.vely) = xy
		else:
			self.velx = xy
			self.vely = y
		
	def getVelocity(self):
		return self.velx,self.vely
