from nirena.util.resources import load_image, get_class
from nirena.util.direction import Direction

class Entity:
	def __init__(self, sprite, point, layer, angle=Direction(0.0), scale=1.0, trans=255, 
			mirror_x=False, mirror_y=False, tint=0, if_wrap=0, region_size = (0, 0)):
		"""
		Creates an entity with their own sprite and position on the screen.
		
		@param layer: An integer telling the world what layer the entity will be visible on
		@param scale: A decimal coeficient to multiply size by
		@param trans: Opaque value of the image from 1-255 where 255 is completely opaque
		@param tint: Tints the sprite into another color. Not sure how this works, implement on own risk
		@param if_wrap: Not sure how this works or what it does, implement on own risk 
		@param region_size: Not sure how this works or what it does, implement on own risk 
		"""
		self.pos = [0,0]
		self.size = [0,0]
		self.layer = layer
		self.setSprite(sprite)
		self.setPosition(point)
		self.rotate(angle)
		if mirror_x: self.flip(true)
		if mirror_y: self.flip(false)
		
	def setSprite(self, sprite):
		"""
		@param sprite: Expects an image, filename is relative to the directory data/images
		@raise ValueError: If C{sprite} is C{None} or an empty string
		"""
		if sprite == "" or sprite == None:
			raise ValueError("Sprite has to have a value")
		self.sprite = load_image(sprite)
		self.size[0] = self.sprite.get_rect().width
		self.size[1] = self.sprite.get_rect().height
		
	def setPosition(self, point):
		""" 
		@param point: Expects an object of C{Point(x, y)} 
		@raise ValueError: If C{point} is C{None} """
		pass
	
	def rotate(self, direction):
		""" Rotate the sprite around the z-axis, this adds to any previous rotation the sprite might've had.
		
		@param direction: Expects an object of C{Direction(self, degree)} 
		@raise ValueError: If C{direction} is C{None} """
		pass
		
	def flip(self, x):
		""" Flips the sprite in one direction or the other. Useful replacement for a turning animation.
		
		@param x: Expects a boolean value, C{True} to flip on x-axel, C{False} to flip on y-axel
		@raise ValueError: If C{x} is anything but a boolean value """
		if x: pass #pygame.transform.flip(tmpimage,1,0)
		else: pass #pygame.transform.flip(tmpimage,0,1)
		pass
		
	def draw(self):
		pass
