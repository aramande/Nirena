class Viewport:
	""" Shows a small part of the world """
	def __init__(self, center=None, offset=None):
		""" Defaults to center on an entity or a point, if no values are entered, default viewport will stay at 0,0 of the world
		
		@param center: Expects an Entity or Point or two coordinates relative to the world that will be centered upon 
		@param offset: Coordinate offset, accepts a Point or two coordinates """
		pass
	
	def recenter(self, center=None, offset=None):
		""" Center around a new entity or point, if None are entered, the previous values will be used (use this feature if the viewport is unsynced).
		
		@param center: Expects an Entity or Point or two coordinates relative to the world that will be centered upon 
		@param offset: Coordinate offset, accepts a Point or two coordinates """
		pass
		
	def draw(self):
		""" Draws all the entities in the area inside the viewport """
		pass
