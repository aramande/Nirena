from nirena.entity.entity import Entity

class Collidable(Entity):
	def __init__(self, image, friction):
		Entity(self, image)
		self._friction = friction
