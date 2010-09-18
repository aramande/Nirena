#!/usr/bin/env python
import pygame
from settings import *
from resources import load_image
class Sprite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.gravity = 0.2 * PHYSICS
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

class Animation:
	def __init__(self,imagename,delay,n):
		"""
			@param  imagename  This is the name of the image file, up to the underscore.
			@param  delay  Amount of frames between the images, only whole integers.
			@param  n  Number of images in animation
		"""
		self.imagename = imagename
		self.nframes = n
		self.delay = delay
		self.frame = 0
		self.pause = 0
		self.looped = False
		self.initialize()
		
	def isLoopedOnce(self):
		return self.looped
		
	def setUnlooped(self):
		self.looped = False

	def getFirstImage(self):
		if self.nframes is 1:
			return self.images
		return self.images[0]

	def getImage(self):
		if self.nframes is 1:
			return self.images

		self.pause += 1
		if self.pause >= self.delay:
			self.pause = 0
			self.frame += 1
			if self.frame == len(self.images)-1:
				self.looped = True
			if self.frame >= len(self.images): 
				#Loop animation on overflow
				self.frame = 0
			return self.images[self.frame]

	def initialize(self):
		if self.nframes is 1:
			if self.imagename is not None:
				self.images = load_image(self.imagename)
			else:
				self.images = None
		else:
			self.images = []
			for i in range(self.nframes):
				# Loads files in the pattern "character/animation_xxx.png", where xxx is a 3-digit number, with the first number being 001.
				name = self.imagename + "_%.3d.png" 
				tmpimage = load_image(name % (i+1))
				colorkey = tmpimage.get_at((1,1))
				tmpimage.set_colorkey(colorkey)
				self.images.append(tmpimage)

