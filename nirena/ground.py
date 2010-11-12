#!/usr/bin/env python
import sprite
import pygame
from ppcollision import *
from resources import load_image

class Ground(sprite.Sprite):
	def __init__(self):
		sprite.Sprite.__init__(self)
		self.image = load_image("player.png")
		self.rect = self.image.get_rect() #= pygame.Rect(90,323,288,200)
		self.hitmask = get_alpha_hitmask(self.image, self.rect)

class Slope(sprite.Sprite):		
	def __init__(self):
		sprite.Sprite.__init__(self)
		self.image = load_image("slope.png")
		self.rect = self.image.get_rect()
		self.setPosition(80,275)
		self.hitmask = get_alpha_hitmask(self.image, self.rect)
		
	def hitmask(self, sprites, groups):
		self.rect = self.image.get_rect()
		check_collision(self, sprites, groups)