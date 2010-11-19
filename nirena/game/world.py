from nirena.entity.entity import Entity
from nirena.util.resources import load_image

class World:
	def __init__(self, background, entities, positions):
		if background == None or background == "":
			raise ValueError("World has to have a background")
		
		self.background = load_image(background)
		self.entities = []
		self.addEntity(entities, positions)
		
	def getEntitiesWithin(*rect):
		"""
			Gets all entities that are positioned within the rect position and size.
			To be implemented.
		"""
		return self.entities
		
	def addEntity(self, entity, position):
		if entity == None or entity == []:
			raise ValueError("Don't add an entity if you don't have an entity to add")
		if position == None or position == []:
			raise ValueError("Don't add an entity if you don't have an position for your entity")
		
		if entity.__class__ == [].__class__:
			if len(entity) != len(position):
				raise IndexError("Entities and Positions has to have the same length.")
			i = 0
			while i < len(entity):
				entity[i].setPosition(position[i])
				i+=1
		else:
			entity.setPosition(position)
		self.entities.append(entity)
		
	def draw(self):
		pass
