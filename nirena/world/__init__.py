from nirena.entity import Entity
from nirena.util.resources import load_image

class World:
	""" A world is the equivalent of a single map, with all the relevant entity information. """
	def __init__(self, entities):
		""" 
		@see: C{addEntity(self, entity)}
		"""
		self.entities = []
		self.addEntity(entities)
		
	def getEntitiesWithin(point=None, size=None):
		"""
		Gets all entities that are positioned within the rect position and size.
		Defaults to everything in the world.
		To be implemented.
		
		@param point: Expects a C{Point(x, y)}
		@param size: Expects two digits, signifying width and height
		@return: A list of Entity type items
		"""
		return self.entities
		
	def addEntity(self, entity):
		""" Add one or more entities to the world, they decide their own position.
		
		@param entity: Expects any entity type, or a class with a C{show(self)} function, or a list with either of these as  """
		if entity == None or entity == []:
			raise ValueError("Don't add an entity if you don't have an entity to add")
		
		if entity.__class__ == [].__class__:
			i = 0
			while i < len(entity):
				self.entities.append(entity[i])
				i+=1
		else:
			self.entities.append(entity)
		
	def draw(self):
		""" Draws all entities onto the screen, the order depends on layer and z value of the entity. """
		pass
