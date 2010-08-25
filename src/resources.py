import os, pygame
def load_image(name):
	fullname = '../data/images/'+ name
#	global loaded
	try:
#		if not loaded:
#			preload()
#        data = resourcefile.read(fullname)
#        data_io = StringIO(data)
#        image = pygame.image.load(data_io,fullname)
		image = pygame.image.load(fullname)
		if image.get_alpha() is None:
			image = image.convert()
		else:
			image = image.convert_alpha()
	except pygame.error as e:
		print(e)
		raise SystemExit
	return image