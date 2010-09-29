#!/usr/bin/env python
import sprite
import pygame
import ppcollision
from resources import load_image

#class < ground
class Ground(sprite.Sprite):
	def __init__(self):
		sprite.Sprite.__init__(self)
		self.image = load_image("player.png")
		self.rect = pygame.Rect(90,323,288,200)

class Slope(sprite.Sprite):		
	def __init__(self):
		sprite.Sprite.__init__(self)
		self.image = load_image("slope.png")
		self.rect = self.image.get_rect()
		self.setPosition(250,275)
		
	def hitmask(self, sprites, groups):
		self.rect = self.image.get_rect()
		check_collision(self, sprites, groups)