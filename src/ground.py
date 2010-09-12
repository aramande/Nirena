#!/usr/bin/env python
import src.sprite
import pygame
from src.resources import load_image
class Ground(src.sprite.Sprite):
	def __init__(self):
		src.sprite.Sprite.__init__(self)
		self.rect = pygame.Rect(90,400,50,50)
		self.image = load_image("player.png")