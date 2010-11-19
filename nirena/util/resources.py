import os
import pygame

def load_image(name):
	fullname = 'data/images/'+ name
	return pygame.image.load(fullname) #### REMOVE THIS LINE TO MAKE SPRITES WORK BETTER LATER
	try:
		image = pygame.image.load(fullname)
		if image.get_alpha() is None:
			image = image.convert()
		else:
			image = image.convert_alpha()
	except pygame.error as e:
		print(e)
		raise SystemExit
	return image

def db_path(name):
	fullname = 'data/db/'+ name
	try:
		database = open(fullname, 'r+')
	except None as e:
		print(e)
		raise SystemExit
	database.close()
	return fullname
		
def get_class(obj):
	return obj.__class__.__name__
