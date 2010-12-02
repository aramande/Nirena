from nirena.entity import Entity

class Movable(Entity):
	def __init__(self, image, friction, point, layer, angle=Direction(0.0), scale=1.0, trans=255, 
			mirror_x=False, mirror_y=False, tint=0, if_wrap=0, region_size = (0, 0)):
		""" 
		@param  image  Filename relative to nirena/data/images
		@param  friction  The force of friction that will be relevant when colliding, expects numeric value """
		Entity.__init__(self, image)
		self._friction = friction
		self._point = point
		self._layer = layer
		
	def tick(self, delta):
		""" Runs once for every frame, any modifications to position or state of the entity should be made here.

		@param  delta  Time since last frame in milliseconds """
		pass

	def addListener(self, listener):
		""" Add a listener to listen to events.
		
		@param  listener  Expects any listener from nirena.event or an object with the function listen(event=None) 
		where event is a relevant event object where applicable """
		pass
		