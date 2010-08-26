#!/usr/bin/env python
import sprite
import pygame
from resources import load_image
class Ground(sprite.Sprite):
	def __init__(self):
		sprite.Sprite.__init__(self)
		self.rect = pygame.Rect(90,400,50,50)
		self.image = load_image("player.png")
		self.force = 1.1