from nirena.util.resources import db_path
from nirena.entity.entity import Entity
#from nirena.game.world import World
from xml.sax import make_parser, handler

class XMLReader(handler.ContentHandler):
	def __init__(self):
		self._surface = []
		self._vector = []
		self._node = []

	def startElement(self, name, attrs):
		if name == "surface":
			if len(self._surface) == int(attrs.get('id')):
				self._surface += [None]
				self._vector += [None]
			if attrs.getValue('type') == "friction":
				self._vector[int(attrs.get('id'))] = True
			self._surface[int(attrs.get('id'))] = attrs
		elif name == "vector":
			i = 0
			while i < len(self._vector):
				if self._vector[i] == True:
					self._vector[i] = attrs
					break
				i += 1
		elif name == "node":
			pass

	def getSurfaces(self):
		return self._surface

	def getVectors(self):
		return self._vector

	def getNodes(self):
		return self._node

	def endDocument(self):
		pass

def _init(filename):
	"Internal initializing function"
	xparser = make_parser()
	reader = XMLReader()
	xparser.setContentHandler(reader)
	objects = xparser.parse(db_path(filename))
	return reader

def loadWorld(filename):
	"Loads the filename as a map and returns the world"
	world = None
	reader = _init(filename)
	nodes = reader.getNodes()
	world = World()
	#convert nodes into nodeobjects here and add them to world
	return world

def loadEntities(filename):
	"Loads entities into the game"
	entities = []
	reader = _init(filename)
	surf = reader.getSurfaces()
	vec = reader.getVectors()
	i = 0
	while i < len(surf):
		if True: #reader.getSurfaces().getValue("type") == "default":
			e = Entity(surf[i].getValue("image"))
		entities += [e]
		i+=1
	return entities
