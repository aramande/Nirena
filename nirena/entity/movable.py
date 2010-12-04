from nirena.entity import Entity
from nirena.util.direction import Direction

class Movable(Entity):
	def __init__(self, image, friction, point, layer, angle=Direction(0.0), scale=1.0, trans=255, 
			mirror_x=False, mirror_y=False, tint=0, if_wrap=0, region_size = (0, 0)):
		""" 
		@param friction: The force of friction that will be relevant when colliding, expects numeric value 
		@see: L{Entity} """
		Entity.__init__(self, image, point, layer, angle, scale, trans, mirror_x, mirror_y, tint, if_wrap, region_size)
		self._friction = friction
		
	def tick(self, delta):
		""" Runs once for every frame, any modifications to position or state of the entity should be made here.

		@param delta: Time since last frame in milliseconds """
		pass

	def addListener(self, listener):
		""" Add a listener to listen to events.
		
		@param listener: Expects any listener from nirena.event or an object with the function listen(event=None) 
		where event is a relevant event object where applicable """
		pass
		