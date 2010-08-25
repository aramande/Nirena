#!/usr/bin/env python

class Sprite:
	def __init__(self, sheetimage, groups):
		return self
	def add(self, groups):
		""" Adds the sprite to @groups """
		return True
	def remove(self, groups):
		""" Removes the sprite from @groups """
		return True
	def kill(self):
		""" Removes the sprite from any groups and cleans up after itself """
		pass
	def groups():
		""" Lists all groups this sprite is a member of """
		return groups
	def isAlive(self):
		""" Returns true if sprite has any remaining groups """
		return True
	def update():
		""" Updates the sprite """

class Group:
	sprites = []
	def __init__(self, sprites):
		return self
	def add(self, sprites):
		""" Adds the @sprites to group """
		return True
	def remove(self, sprites):
		""" Removes the @sprites from group """
		return True
	def empty(self):
		""" Removes all sprites from the group """
		pass
	def copy(self):
		""" Returns a copy of the group """
		return ""
	def isEmpty():
		""" Returns true if group contains no sprites """
		pass
	def sprites():
		""" Returns the list of sprites """
		return sprites
	def update():
		""" Updates all the sprites in the group """
		pass
	def len():
		""" Returns the number of sprites in the group """
		return sprites.len()