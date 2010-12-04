from nirena.entity import Entity
from nirena.util.direction import Direction

class Collidable(Entity):
	def __init__(self, image, friction, point, layer, angle=Direction(0.0), scale=1.0, trans=255, 
			mirror_x=False, mirror_y=False, tint=0, if_wrap=0, region_size = (0, 0)):
		""" 
		@param friction: The force of friction that will be relevant when colliding, expects numeric value 
		@see: L{Entity} """
		Entity.__init__(self, image, layer, angle, scale, trans, mirror_x, mirror_y, tint, if_wrap, region_size)
		self._friction = friction

	def addListener(self, listener):
		""" """