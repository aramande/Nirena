from nirena.entity import Entity

class Collidable(Entity):
	def __init__(self, image, friction, point, layer, angle=Direction(0.0), scale=1.0, trans=255, 
			mirror_x=False, mirror_y=False, tint=0, if_wrap=0, region_size = (0, 0)):
		""" 
		@param  image  Filename relative to nirena/data/images
		@param  friction  The force of friction that will be relevant when colliding, expects numeric value """
		Entity.__init__(self, image)
		self._friction = friction

	def addListener(self, listener):
		"""  """