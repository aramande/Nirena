#!/usr/bin/env python

import pygame
import sprite
from resources import load_image
from settings import *

class Player(sprite.Sprite):
	def __init__(self):
		sprite.Sprite.__init__(self)
		self.animation = {"idle" : sprite.Animation("alucard/idle", 6, 7),
						  "toidle" : sprite.Animation("alucard/toidle", 6, 7),
						  "walk" : sprite.Animation("alucard/walk", 6, 16),
						  "towalk" : sprite.Animation("alucard/towalk", 6, 15)}
		self.activeAnimation = "idle"
		self.activeTransition = ""
		self.image = self.animation[self.activeAnimation].getFirstImage();
		self.rect = self.image.get_rect()
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		xoffset = (self.area.right - self.rect.left)/2
		yoffset = self.area.bottom - self.rect.centery
		self.direction = 0
		self.setPosition(xoffset, yoffset)
		self.flipped = False
		self.velx = 0
		self.vely = 0
		self.accy = 0
		self.normal = 0
		self.terminalVelocity = 8
		self.jumping = False
		self.fall = True
		
	def setActiveAnimation(self, name):
		"""
			Runs directly after the activeTransition has been run.
			name is the name of the animation within the animation dictionary
			returns false if the name doesn't exist
			"""
		if name in self.animation:
			self.activeAnimation = name
			return True
		return False
		
	def setActiveTransition(self, name):
		"""
			Transition is a special kind of animation, that happens between animations, and before the activeAnimation.
			An empty name means no transition will be played.
			"""
		if name == "" or name in self.animation:
			self.activeTransition = name
			return True
		return False
	
	def verticalVelocity(self, a, dt):
		""" 
			Input current velocity, acceleration and time since 
			last frame to get a new velocity. Negative or zero time throws ValueError.
			This function should be moved to some kind of physics engine later. 
			"""
		if dt <= 0:
			raise ValueError
		v = self.vely + a * dt
		if v > self.terminalVelocity :
			v = self.terminalVelocity
		if not self.fall and v > 0 :
			v = 0
		if v < 0:
			self.jumping = True
		return round(v, 2)
	
	def update(self, dt):
		sprite.Sprite.update(self)
		tmpimage = ""
		if self.activeTransition != "":
			tmpimage = self.animation[self.activeTransition].getImage() #self.image
			if self.animation[self.activeTransition].isLoopedOnce():
				self.animation[self.activeTransition].setUnlooped()
				self.activeTransition = ""
		else:
			tmpimage = self.animation[self.activeAnimation].getImage() #self.image
		if tmpimage is not None:
			if self.flipped:
				tmpimage = pygame.transform.flip(tmpimage,1,0)
			self.image=tmpimage
		if(dt <= 0):
			dt = 0.01
		self.rect.left += self.velx
		self.vely = self.verticalVelocity(self.accy + self.gravity - self.normal, dt)
		self.rect.top += self.vely 
		self.accy = 0

	def processMovement(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT or \
			event.key == pygame.K_a:
				self.velx = -2
				self.setActiveTransition("towalk")
				self.setActiveAnimation("walk")
				self.flipped = True
			elif event.key == pygame.K_RIGHT or \
			event.key == pygame.K_d:
				self.velx = +2
				self.setActiveTransition("towalk")
				self.setActiveAnimation("walk")
				self.flipped = False
			elif event.key == pygame.K_UP or \
			event.key == pygame.K_w or \
			event.key == pygame.K_SPACE or \
			event.key == pygame.K_z:
				if not self.jumping:
					self.accy = -4 * PHYSICS
					self.fall = True
			elif event.key == pygame.K_DOWN:
				pass
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				self.velx = 0
				self.setActiveTransition("toidle")
				self.setActiveAnimation("idle")
			elif event.key == pygame.K_RIGHT:
				self.velx = 0
				self.setActiveTransition("toidle")
				self.setActiveAnimation("idle")
			elif event.key == pygame.K_UP:
				self.accy = 0
			elif event.key == pygame.K_DOWN:
				pass
				
	def isCollidingWith(self, sprites, groups):
		self.fall = True
		for sprite in sprites:
			if groups['ground'] in sprite.groups():
				if(self.vely > 0):
					self.fall = False
					self.jumping = False
					t_x, t_y = self.getPosition()
					junk, t_y = sprite.getPosition()
					self.setPosition(t_x, t_y-(self.rect.bottom-self.rect.top-1.0))