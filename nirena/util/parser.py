import db_path from resources

class Parser:

	def __init__(self):
		self.worldmap = open(db_path("map.txt"), 'rw')
		self.objects = open(db_path("object.txt"), 'rw')
	
	def loadMap(self):
		a_map = None
		return a_map
	
	def getObject(self, id):
		obj = None
		return obj